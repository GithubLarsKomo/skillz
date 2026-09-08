from __future__ import annotations

import asyncio
import hashlib
import hmac
import json
import logging
import os
import re
from collections.abc import Awaitable, Callable, Mapping, Sequence
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlparse

import httpx
import jwt
from mcp.server.auth.provider import AccessToken, TokenVerifier
from mcp.server.auth.settings import AuthSettings
from pydantic import AnyHttpUrl

JWKSLoader = Callable[[], Awaitable[Mapping[str, Any]]]
ALLOWED_SIGNING_ALGORITHMS = frozenset({"RS256", "ES256", "ES384", "ES512"})
STATIC_TOKEN_ENV = "SKILLZ_MCP_STATIC_TOKEN_HASHES"
_STATIC_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")
_AUTH_LOGGER = logging.getLogger("skillz_mcp.auth")


@dataclass(frozen=True)
class RemoteAuthConfig:
    """Immutable OAuth resource-server configuration for remote HTTP deployment."""

    issuer_url: str
    resource_url: str
    jwks_url: str
    audience: str
    required_scopes: tuple[str, ...] = ("skillz:read",)
    algorithms: tuple[str, ...] = ("RS256",)

    def auth_settings(self) -> AuthSettings:
        return AuthSettings(
            issuer_url=AnyHttpUrl(self.issuer_url),
            resource_server_url=AnyHttpUrl(self.resource_url),
            required_scopes=list(self.required_scopes),
        )


@dataclass(frozen=True)
class StaticTokenCredential:
    """One revocable static credential stored server-side only as a SHA-256 digest."""

    identifier: str
    sha256_hex: str


_AUTH_ENV_KEYS = (
    "SKILLZ_MCP_AUTH_ISSUER_URL",
    "SKILLZ_MCP_AUTH_RESOURCE_URL",
    "SKILLZ_MCP_AUTH_JWKS_URL",
    "SKILLZ_MCP_AUTH_AUDIENCE",
)


def _require_https(name: str, value: str) -> None:
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.hostname:
        raise ValueError(f"{name} must be an absolute HTTPS URL")


def hash_static_token(token: str) -> str:
    """Return the server-side digest representation for a high-entropy bearer token."""
    if len(token) < 32:
        raise ValueError("static MCP bearer token must contain at least 32 characters")
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def static_tokens_from_env(environ: Mapping[str, str] | None = None) -> tuple[StaticTokenCredential, ...]:
    """Parse `id=sha256hex` credentials; no clear-text server-side token configuration is accepted."""
    env = environ if environ is not None else os.environ
    raw = str(env.get(STATIC_TOKEN_ENV, "")).strip()
    if not raw:
        return ()

    normalized = raw.replace(";", ",").replace("\n", ",")
    credentials: list[StaticTokenCredential] = []
    seen: set[str] = set()
    for entry in (item.strip() for item in normalized.split(",")):
        if not entry:
            continue
        identifier, separator, digest = entry.partition("=")
        identifier = identifier.strip()
        digest = digest.strip().lower()
        if not separator or not _STATIC_ID_RE.fullmatch(identifier):
            raise ValueError(f"invalid static MCP token entry: {entry!r}")
        if identifier in seen:
            raise ValueError(f"duplicate static MCP token identifier: {identifier}")
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ValueError(f"static MCP token {identifier!r} must be configured as a SHA-256 hex digest")
        credentials.append(StaticTokenCredential(identifier=identifier, sha256_hex=digest))
        seen.add(identifier)
    if not credentials:
        raise ValueError(f"{STATIC_TOKEN_ENV} does not contain any usable credentials")
    return tuple(credentials)


def auth_config_from_env(environ: Mapping[str, str] | None = None) -> RemoteAuthConfig | None:
    """Load auth config only when explicitly configured; reject partial or weak remote auth."""
    env = environ if environ is not None else os.environ
    present = {key: str(env.get(key, "")).strip() for key in _AUTH_ENV_KEYS}
    if not any(present.values()):
        return None
    missing = [key for key, value in present.items() if not value]
    if missing:
        raise ValueError(f"incomplete MCP auth configuration; missing: {', '.join(missing)}")

    _require_https("SKILLZ_MCP_AUTH_ISSUER_URL", present["SKILLZ_MCP_AUTH_ISSUER_URL"])
    _require_https("SKILLZ_MCP_AUTH_RESOURCE_URL", present["SKILLZ_MCP_AUTH_RESOURCE_URL"])
    _require_https("SKILLZ_MCP_AUTH_JWKS_URL", present["SKILLZ_MCP_AUTH_JWKS_URL"])
    if present["SKILLZ_MCP_AUTH_AUDIENCE"] != present["SKILLZ_MCP_AUTH_RESOURCE_URL"]:
        raise ValueError("SKILLZ_MCP_AUTH_AUDIENCE must equal SKILLZ_MCP_AUTH_RESOURCE_URL")

    scopes = tuple(
        item for item in str(env.get("SKILLZ_MCP_AUTH_REQUIRED_SCOPES", "skillz:read")).replace(",", " ").split() if item
    )
    if not scopes:
        raise ValueError("SKILLZ_MCP_AUTH_REQUIRED_SCOPES must contain at least one scope")

    algorithms = tuple(
        item for item in str(env.get("SKILLZ_MCP_AUTH_ALGORITHMS", "RS256")).replace(",", " ").split() if item
    )
    if not algorithms:
        raise ValueError("SKILLZ_MCP_AUTH_ALGORITHMS must contain at least one algorithm")
    unsupported = sorted(set(algorithms) - ALLOWED_SIGNING_ALGORITHMS)
    if unsupported:
        raise ValueError(f"unsupported MCP JWT signing algorithms: {', '.join(unsupported)}")

    return RemoteAuthConfig(
        issuer_url=present["SKILLZ_MCP_AUTH_ISSUER_URL"],
        resource_url=present["SKILLZ_MCP_AUTH_RESOURCE_URL"],
        jwks_url=present["SKILLZ_MCP_AUTH_JWKS_URL"],
        audience=present["SKILLZ_MCP_AUTH_AUDIENCE"],
        required_scopes=scopes,
        algorithms=algorithms,
    )


class AuthentikJWTTokenVerifier(TokenVerifier):
    """Verify Authentik-issued JWT access tokens against a bounded JWKS cache."""

    def __init__(
        self,
        config: RemoteAuthConfig,
        *,
        jwks_loader: JWKSLoader | None = None,
        request_timeout_seconds: float = 5.0,
    ) -> None:
        self.config = config
        self._jwks_loader = jwks_loader
        self._request_timeout_seconds = request_timeout_seconds
        self._keys: dict[str, Any] = {}
        self._lock = asyncio.Lock()

    async def _fetch_jwks(self) -> Mapping[str, Any]:
        if self._jwks_loader is not None:
            return await self._jwks_loader()
        async with httpx.AsyncClient(
            timeout=self._request_timeout_seconds,
            follow_redirects=False,
            headers={"Accept": "application/json"},
        ) as client:
            response = await client.get(self.config.jwks_url)
            response.raise_for_status()
            payload = response.json()
        if not isinstance(payload, Mapping):
            raise ValueError("JWKS response must be a JSON object")
        return payload

    async def _refresh_keys(self) -> None:
        async with self._lock:
            payload = await self._fetch_jwks()
            raw_keys = payload.get("keys")
            if not isinstance(raw_keys, list) or not raw_keys:
                raise ValueError("JWKS response does not contain keys")
            keys: dict[str, Any] = {}
            for item in raw_keys:
                if not isinstance(item, Mapping):
                    continue
                kid = item.get("kid")
                if not isinstance(kid, str) or not kid:
                    continue
                keys[kid] = jwt.PyJWK.from_dict(dict(item)).key
            if not keys:
                raise ValueError("JWKS response contains no usable keyed signing keys")
            self._keys = keys

    async def _key_for_token(self, token: str) -> tuple[Any, str]:
        header = jwt.get_unverified_header(token)
        algorithm = str(header.get("alg") or "")
        if algorithm not in self.config.algorithms:
            raise jwt.InvalidAlgorithmError("token signing algorithm is not allowed")
        kid = header.get("kid")
        if not isinstance(kid, str) or not kid:
            raise jwt.InvalidTokenError("token header does not contain kid")
        key = self._keys.get(kid)
        if key is None:
            await self._refresh_keys()
            key = self._keys.get(kid)
        if key is None:
            raise jwt.InvalidTokenError("token signing key is unknown")
        return key, algorithm

    @staticmethod
    def _scopes(claims: Mapping[str, Any]) -> list[str]:
        values: list[str] = []
        raw_scope = claims.get("scope")
        if isinstance(raw_scope, str):
            values.extend(raw_scope.split())
        elif isinstance(raw_scope, list):
            values.extend(str(item) for item in raw_scope if item)
        raw_scopes = claims.get("scopes")
        if isinstance(raw_scopes, list):
            values.extend(str(item) for item in raw_scopes if item)
        return sorted(set(values))

    async def verify_token(self, token: str) -> AccessToken | None:
        try:
            key, algorithm = await self._key_for_token(token)
            claims = jwt.decode(
                token,
                key=key,
                algorithms=[algorithm],
                audience=self.config.audience,
                issuer=self.config.issuer_url,
                options={"require": ["aud", "exp", "iss", "sub"]},
            )
            subject = str(claims["sub"])
            client_id = str(claims.get("azp") or claims.get("client_id") or "unknown-oauth-client")
            expires_at = int(claims["exp"])
            return AccessToken(
                token=token,
                client_id=client_id,
                scopes=self._scopes(claims),
                expires_at=expires_at,
                resource=self.config.resource_url,
                subject=subject,
                claims={"iss": str(claims["iss"]), "aud": claims["aud"], "auth_type": "oauth_jwt"},
            )
        except (jwt.InvalidTokenError, httpx.HTTPError, KeyError, TypeError, ValueError):
            return None


class StaticBearerTokenVerifier(TokenVerifier):
    """Verify named high-entropy bearer tokens against server-side SHA-256 digests."""

    def __init__(
        self,
        credentials: Sequence[StaticTokenCredential],
        *,
        resource_url: str,
        scope: str = "skillz:read",
    ) -> None:
        self.credentials = tuple(credentials)
        self.resource_url = resource_url
        self.scope = scope

    async def verify_token(self, token: str) -> AccessToken | None:
        digest = hashlib.sha256(token.encode("utf-8")).hexdigest()
        matched: StaticTokenCredential | None = None
        for credential in self.credentials:
            if hmac.compare_digest(digest, credential.sha256_hex):
                matched = credential
        if matched is None:
            return None

        _AUTH_LOGGER.info(
            json.dumps(
                {
                    "event": "static_bearer_authenticated",
                    "credentialId": matched.identifier,
                    "scope": self.scope,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        identity = f"static:{matched.identifier}"
        return AccessToken(
            token=token,
            client_id=identity,
            scopes=[self.scope],
            resource=self.resource_url,
            subject=identity,
            claims={"auth_type": "static_bearer", "credential_id": matched.identifier},
        )


class CompositeTokenVerifier(TokenVerifier):
    """Accept a token when one configured verifier accepts it, preserving verifier order."""

    def __init__(self, verifiers: Sequence[TokenVerifier]) -> None:
        self.verifiers = tuple(verifiers)
        if not self.verifiers:
            raise ValueError("composite token verifier requires at least one verifier")

    async def verify_token(self, token: str) -> AccessToken | None:
        for verifier in self.verifiers:
            result = await verifier.verify_token(token)
            if result is not None:
                return result
        return None


def build_token_verifier(
    config: RemoteAuthConfig,
    *,
    static_credentials: Sequence[StaticTokenCredential] = (),
    oauth_verifier: TokenVerifier | None = None,
) -> TokenVerifier:
    """Build the production verifier: static read-only credentials first, Authentik OAuth second."""
    oauth = oauth_verifier or AuthentikJWTTokenVerifier(config)
    if not static_credentials:
        return oauth
    static = StaticBearerTokenVerifier(static_credentials, resource_url=config.resource_url)
    return CompositeTokenVerifier((static, oauth))
