from __future__ import annotations

import asyncio
import os
from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass
from typing import Any

import httpx
import jwt
from mcp.server.auth.provider import AccessToken, TokenVerifier
from mcp.server.auth.settings import AuthSettings
from pydantic import AnyHttpUrl

JWKSLoader = Callable[[], Awaitable[Mapping[str, Any]]]


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


_AUTH_ENV_KEYS = (
    "SKILLZ_MCP_AUTH_ISSUER_URL",
    "SKILLZ_MCP_AUTH_RESOURCE_URL",
    "SKILLZ_MCP_AUTH_JWKS_URL",
    "SKILLZ_MCP_AUTH_AUDIENCE",
)


def auth_config_from_env(environ: Mapping[str, str] | None = None) -> RemoteAuthConfig | None:
    """Load auth config only when explicitly configured; reject partial remote auth."""
    env = environ if environ is not None else os.environ
    present = {key: str(env.get(key, "")).strip() for key in _AUTH_ENV_KEYS}
    if not any(present.values()):
        return None
    missing = [key for key, value in present.items() if not value]
    if missing:
        raise ValueError(f"incomplete MCP auth configuration; missing: {', '.join(missing)}")

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
            client_id = str(claims.get("azp") or claims.get("client_id") or self.config.audience)
            expires_at = int(claims["exp"])
            return AccessToken(
                token=token,
                client_id=client_id,
                scopes=self._scopes(claims),
                expires_at=expires_at,
                resource=self.config.resource_url,
                subject=subject,
                claims={"iss": str(claims["iss"])},
            )
        except (jwt.InvalidTokenError, httpx.HTTPError, KeyError, TypeError, ValueError):
            return None
