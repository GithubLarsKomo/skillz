# Skillz MCP remote deployment

This document defines the production target for the read-only Skillz MCP service.

## Production endpoint

- Public MCP endpoint: `https://skillz.ratzeburg-ai.de/mcp`
- Public liveness endpoint: `https://skillz.ratzeburg-ai.de/healthz`
- Runtime: Docker on the existing Hetzner/Coolify host
- Reverse proxy / TLS: Coolify-managed Traefik on ports 80/443
- Authorization server: authentik at `https://auth.ratzeburg-ai.de`
- MCP transport: stateless Streamable HTTP
- Application port inside the Docker network: `8000`

The MCP endpoint MUST NOT be exposed anonymously. Do not add authentik ForwardAuth in front of `/mcp`: browser-cookie redirects break MCP OAuth discovery. The MCP server itself is the OAuth 2.1 resource server and returns RFC 9728 Protected Resource Metadata plus the required `WWW-Authenticate` challenge. authentik remains the external authorization server.

## authentik application/provider

Create a dedicated authentik OAuth2/OIDC application/provider for Skillz MCP.

Recommended baseline:

- Application name: `Skillz MCP`
- Application slug: `skillz`
- Provider type: OAuth2/OIDC
- Issuer mode: per-provider/default
- Client type: public for PKCE-based interactive clients unless a specific MCP client requires a confidential pre-registered client
- Signing algorithm/key: RSA / `RS256`
- Authorization flow: Authorization Code with PKCE (`S256`)
- `Include claims in id_token`: enabled (authentik default; required for the audience mapping below to enter the signed access token)
- Required Skillz scope: `skillz:read`
- Additional interactive scopes: `openid profile email offline_access`
- Redirect URIs: exact URIs supplied by each pre-registered MCP client; do not use wildcard redirect URIs

### Resource-bound audience mapping

MCP clients identify the target server as `https://skillz.ratzeburg-ai.de/mcp`. The MCP resource server must reject tokens that are not intended for that resource.

authentik normally initializes the JWT `aud` claim from the OAuth provider client ID. For this dedicated provider, override that value through the `skillz:read` scope mapping so the signed access token is resource-bound.

Create an OAuth2 Scope Mapping:

- Name: `Skillz MCP read`
- Scope name: `skillz:read`
- Description: `Read Skillz capability metadata through MCP`
- Expression:

```python
return {
    "aud": "https://skillz.ratzeburg-ai.de/mcp",
}
```

Attach this mapping to the Skillz OAuth2 provider. Keep `Include claims in id_token` enabled. authentik's access-token construction preserves the OAuth client identifier separately in `azp`, while mapped claims are merged into the signed JWT; the server therefore validates the MCP resource URI as `aud` and records `azp` only as client identity.

Enable the managed `offline_access` scope mapping when a client needs refresh tokens. MCP 2026-07-28 permits client pre-registration, so pre-registration is the baseline deployment model. If the selected MCP client requires Dynamic Client Registration or Client ID Metadata Documents, verify that capability separately before production cutover rather than weakening the resource-server checks.

Expected authentik endpoints for the `skillz` application slug:

- Issuer: `https://auth.ratzeburg-ai.de/application/o/skillz/`
- Authorization: `https://auth.ratzeburg-ai.de/application/o/authorize/`
- Token: `https://auth.ratzeburg-ai.de/application/o/token/`
- JWKS: `https://auth.ratzeburg-ai.de/application/o/skillz/jwks/`
- OIDC discovery: `https://auth.ratzeburg-ai.de/application/o/skillz/.well-known/openid-configuration`

Before production use, run a patched authentik release. In particular, authentik's 2026 OAuth-provider client-secret disclosure advisory is fixed in 2026.2.3 and 2025.12.5 or later.

## Coolify application

Create a Git-backed Coolify application from `GithubLarsKomo/skillz` using the repository `Dockerfile`.

Configuration:

1. Build pack: Dockerfile.
2. Base directory: `/`.
3. Internal port / Ports Exposes: `8000`.
4. Domain: `https://skillz.ratzeburg-ai.de`.
5. Health check path: `/healthz`.
6. Keep container port `8000` internal; only Coolify/Traefik publishes 80/443.
7. Enable HTTPS and HTTP-to-HTTPS redirect in the Coolify proxy.
8. Do not attach the existing authentik ForwardAuth middleware to this application.

Set these runtime variables in Coolify:

```dotenv
SKILLZ_MCP_AUTH_ISSUER_URL=https://auth.ratzeburg-ai.de/application/o/skillz/
SKILLZ_MCP_AUTH_RESOURCE_URL=https://skillz.ratzeburg-ai.de/mcp
SKILLZ_MCP_AUTH_JWKS_URL=https://auth.ratzeburg-ai.de/application/o/skillz/jwks/
SKILLZ_MCP_AUTH_AUDIENCE=https://skillz.ratzeburg-ai.de/mcp
SKILLZ_MCP_AUTH_REQUIRED_SCOPES=skillz:read
SKILLZ_MCP_AUTH_ALGORITHMS=RS256
SKILLZ_MCP_MAX_REQUEST_BYTES=262144
SKILLZ_MCP_COMMIT_SHA=$SOURCE_COMMIT
```

The process fails closed if `SKILLZ_MCP_AUTH_AUDIENCE` differs from `SKILLZ_MCP_AUTH_RESOURCE_URL`, if any remote auth URL is not HTTPS, or if a symmetric JWT algorithm is configured.

Coolify provides `SOURCE_COMMIT` for Git-backed applications. Mapping it into `SKILLZ_MCP_COMMIT_SHA` makes the exact deployed source commit visible through `catalog_status` and `skillz://status` without copying `.git` into the production image.

## Transport security

For authenticated remote HTTP, the process binds to `0.0.0.0:8000`, but MCP transport security allowlists the hostname and origin derived from `SKILLZ_MCP_AUTH_RESOURCE_URL`. With the production values this allows `skillz.ratzeburg-ai.de` and `https://skillz.ratzeburg-ai.de` while retaining DNS-rebinding protection. Loopback hostnames are also allowed solely so Docker/Coolify can perform the internal `/healthz` liveness check.

The default MCP request-body limit is 256 KiB. It can be changed with `SKILLZ_MCP_MAX_REQUEST_BYTES`, but the process rejects values above 4 MiB.

At the Traefik/Coolify edge, start with a conservative rate limit such as 60 MCP requests per minute per source with a burst of 20, then adjust from operational evidence. Do not log `Authorization` headers, request bodies, tool arguments, resource contents, or JWTs.

## Verification after deployment

The following checks define the minimum remote acceptance gate:

1. `GET https://skillz.ratzeburg-ai.de/healthz` returns `200` with `{"status":"ok"}`.
2. An unauthenticated request to `/mcp` returns `401`, not a browser redirect.
3. The `WWW-Authenticate` header contains an RFC 9728 `resource_metadata` URL.
4. `GET https://skillz.ratzeburg-ai.de/.well-known/oauth-protected-resource/mcp` identifies the Skillz resource, authentik issuer, and `skillz:read` scope.
5. authentik OIDC discovery reports PKCE `S256`; interactive clients must refuse a provider that does not advertise PKCE support.
6. Decode one issued Skillz access token before cutover and verify `iss=https://auth.ratzeburg-ai.de/application/o/skillz/`, `aud=https://skillz.ratzeburg-ai.de/mcp`, a non-empty `sub`, and scope `skillz:read`.
7. A token with the wrong issuer, resource audience, signature, expiration, or missing `skillz:read` scope cannot access MCP.
8. A valid token can list tools/resources and call `catalog_status`.
9. `catalog_status` reports the deployed `SOURCE_COMMIT` and expected catalog hash/freshness.
10. No MCP handler exposes repository writes, arbitrary subprocess execution, provider calls, or skill execution.

## Client registration

The baseline production model uses OAuth client pre-registration in authentik. For each MCP client:

1. obtain its exact redirect URI(s),
2. register those URIs in the Skillz authentik OAuth provider,
3. configure/use the Skillz provider client ID as required by that client,
4. request `skillz:read`; for durable interactive access also request `offline_access`,
5. use Authorization Code + PKCE S256.

ChatGPT custom MCP apps support OAuth and should have refresh-token/offline access enabled so authorization survives access-token expiry. The exact callback URI must be copied from the client setup UI at registration time; do not guess it.

If future clients require Dynamic Client Registration or Client ID Metadata Documents rather than pre-registration, treat that as an authorization-server compatibility change. Do not add a second OAuth implementation inside Skillz MCP merely to emulate an authorization server.

## Upstream references

- MCP 2026-07-28 Authorization: https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization
- MCP Python SDK authorization: https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/run/authorization.md
- authentik OAuth2/OIDC provider: https://docs.goauthentik.io/add-secure-apps/providers/oauth2/
- Coolify environment variables: https://coolify.io/docs/knowledge-base/environment-variables
- Coolify Dockerfile build pack: https://coolify.io/docs/applications/build-packs/dockerfile
