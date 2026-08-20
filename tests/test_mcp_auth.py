from __future__ import annotations

import asyncio
import json
import time
import unittest
from pathlib import Path

import httpx
import jwt
from cryptography.hazmat.primitives.asymmetric import rsa
from mcp.server.auth.provider import AccessToken, TokenVerifier
from mcp.server.transport_security import TransportSecuritySettings

from skillz_mcp.auth import AuthentikJWTTokenVerifier, RemoteAuthConfig, auth_config_from_env
from skillz_mcp.server import create_server

ROOT = Path(__file__).resolve().parents[1]
ISSUER = "https://auth.ratzeburg-ai.de/application/o/skillz/"
RESOURCE = "https://skillz.ratzeburg-ai.de/mcp"
JWKS = "https://auth.ratzeburg-ai.de/application/o/skillz/jwks/"
AUDIENCE = RESOURCE


def config() -> RemoteAuthConfig:
    return RemoteAuthConfig(
        issuer_url=ISSUER,
        resource_url=RESOURCE,
        jwks_url=JWKS,
        audience=AUDIENCE,
        required_scopes=("skillz:read",),
    )


class StaticVerifier(TokenVerifier):
    async def verify_token(self, token: str) -> AccessToken | None:
        if token == "valid-token":
            return AccessToken(token=token, client_id="test-client", scopes=["skillz:read"], subject="test-user")
        if token == "no-scope-token":
            return AccessToken(token=token, client_id="test-client", scopes=["openid"], subject="test-user")
        return None


class MCPAuthTests(unittest.TestCase):
    def test_auth_config_is_opt_in_and_remote_config_fails_closed(self) -> None:
        self.assertIsNone(auth_config_from_env({}))
        with self.assertRaises(ValueError):
            auth_config_from_env({"SKILLZ_MCP_AUTH_ISSUER_URL": ISSUER})

        loaded = auth_config_from_env(
            {
                "SKILLZ_MCP_AUTH_ISSUER_URL": ISSUER,
                "SKILLZ_MCP_AUTH_RESOURCE_URL": RESOURCE,
                "SKILLZ_MCP_AUTH_JWKS_URL": JWKS,
                "SKILLZ_MCP_AUTH_AUDIENCE": RESOURCE,
                "SKILLZ_MCP_AUTH_REQUIRED_SCOPES": "skillz:read offline_access",
            }
        )
        assert loaded is not None
        self.assertEqual(loaded.required_scopes, ("skillz:read", "offline_access"))
        self.assertEqual(loaded.audience, loaded.resource_url)

        with self.assertRaises(ValueError):
            auth_config_from_env(
                {
                    "SKILLZ_MCP_AUTH_ISSUER_URL": ISSUER,
                    "SKILLZ_MCP_AUTH_RESOURCE_URL": RESOURCE,
                    "SKILLZ_MCP_AUTH_JWKS_URL": JWKS,
                    "SKILLZ_MCP_AUTH_AUDIENCE": "some-oauth-client-id",
                }
            )
        with self.assertRaises(ValueError):
            auth_config_from_env(
                {
                    "SKILLZ_MCP_AUTH_ISSUER_URL": "http://auth.example.test/issuer/",
                    "SKILLZ_MCP_AUTH_RESOURCE_URL": RESOURCE,
                    "SKILLZ_MCP_AUTH_JWKS_URL": JWKS,
                    "SKILLZ_MCP_AUTH_AUDIENCE": RESOURCE,
                }
            )
        with self.assertRaises(ValueError):
            auth_config_from_env(
                {
                    "SKILLZ_MCP_AUTH_ISSUER_URL": ISSUER,
                    "SKILLZ_MCP_AUTH_RESOURCE_URL": RESOURCE,
                    "SKILLZ_MCP_AUTH_JWKS_URL": JWKS,
                    "SKILLZ_MCP_AUTH_AUDIENCE": RESOURCE,
                    "SKILLZ_MCP_AUTH_ALGORITHMS": "HS256",
                }
            )

    def test_authentik_jwt_verifier_checks_signature_issuer_resource_audience_and_claims(self) -> None:
        async def run() -> None:
            private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
            public_jwk = json.loads(jwt.algorithms.RSAAlgorithm.to_jwk(private_key.public_key()))
            public_jwk["kid"] = "test-key"

            async def load_jwks() -> dict:
                return {"keys": [public_jwk]}

            verifier = AuthentikJWTTokenVerifier(config(), jwks_loader=load_jwks)
            now = int(time.time())
            token = jwt.encode(
                {
                    "iss": ISSUER,
                    "sub": "user-123",
                    "aud": RESOURCE,
                    "azp": "mcp-client-123",
                    "scope": "openid profile skillz:read",
                    "iat": now,
                    "exp": now + 300,
                },
                private_key,
                algorithm="RS256",
                headers={"kid": "test-key"},
            )
            result = await verifier.verify_token(token)
            self.assertIsNotNone(result)
            assert result is not None
            self.assertEqual(result.client_id, "mcp-client-123")
            self.assertEqual(result.subject, "user-123")
            self.assertIn("skillz:read", result.scopes)
            self.assertEqual(result.resource, RESOURCE)
            self.assertEqual(result.claims["aud"], RESOURCE)

            wrong_audience = jwt.encode(
                {
                    "iss": ISSUER,
                    "sub": "user-123",
                    "aud": "https://other.example.test/mcp",
                    "scope": "skillz:read",
                    "exp": now + 300,
                },
                private_key,
                algorithm="RS256",
                headers={"kid": "test-key"},
            )
            self.assertIsNone(await verifier.verify_token(wrong_audience))

        asyncio.run(run())

    def test_http_auth_exposes_rfc9728_metadata_and_blocks_unauthorized_mcp(self) -> None:
        async def run() -> None:
            server = create_server(ROOT, auth_config=config(), token_verifier=StaticVerifier())
            security = TransportSecuritySettings(
                enable_dns_rebinding_protection=True,
                allowed_hosts=["skillz.ratzeburg-ai.de"],
                allowed_origins=["https://skillz.ratzeburg-ai.de"],
            )
            app = server.streamable_http_app(
                host="0.0.0.0",
                stateless_http=True,
                json_response=True,
                transport_security=security,
            )
            transport = httpx.ASGITransport(app=app)
            async with httpx.AsyncClient(transport=transport, base_url="https://skillz.ratzeburg-ai.de") as client:
                health = await client.get("/healthz")
                self.assertEqual(health.status_code, 200)
                self.assertEqual(health.json(), {"status": "ok"})

                metadata = await client.get("/.well-known/oauth-protected-resource/mcp")
                self.assertEqual(metadata.status_code, 200)
                payload = metadata.json()
                self.assertEqual(payload["resource"], RESOURCE)
                self.assertEqual(payload["authorization_servers"], [ISSUER])
                self.assertEqual(payload["scopes_supported"], ["skillz:read"])

                anonymous = await client.post("/mcp", json={})
                self.assertEqual(anonymous.status_code, 401)
                challenge = anonymous.headers.get("www-authenticate", "")
                self.assertIn("Bearer", challenge)
                self.assertIn("resource_metadata=", challenge)

                invalid = await client.post("/mcp", json={}, headers={"Authorization": "Bearer invalid-token"})
                self.assertEqual(invalid.status_code, 401)

                insufficient = await client.post(
                    "/mcp", json={}, headers={"Authorization": "Bearer no-scope-token"}
                )
                self.assertEqual(insufficient.status_code, 403)
                scope_challenge = insufficient.headers.get("www-authenticate", "")
                self.assertIn("insufficient_scope", scope_challenge)
                self.assertIn("skillz:read", scope_challenge)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
