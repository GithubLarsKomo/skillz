# ChatGPT for Windows — Skillz MCP

ChatGPT for Windows can connect directly to the protected Skillz MCP endpoint with its **Streamable HTTP** custom-MCP configuration.

The Windows UI currently accepts a bearer-token **environment-variable name** rather than performing the interactive OAuth flow itself. Skillz therefore supports a second, narrowly scoped authentication path alongside Authentik OAuth:

- interactive clients: Authentik OAuth/OIDC JWTs,
- header-oriented clients such as the current ChatGPT for Windows MCP UI: named static bearer credentials.

Both paths authorize only `skillz:read` and use the same endpoint:

`https://skillz.ratzeburg-ai.de/mcp`

## Security model

A static bearer credential is:

- generated with at least 256 bits of cryptographic randomness,
- stored in clear text only on the client that uses it,
- stored on the server only as a SHA-256 digest,
- associated with a non-secret credential identifier such as `chatgpt-windows-lars`,
- internally mapped only to `skillz:read`,
- independently revocable by removing its digest from Coolify and redeploying,
- never written to application logs.

The server environment variable is:

`SKILLZ_MCP_STATIC_TOKEN_HASHES`

Its format is a comma-separated list of named SHA-256 digests:

```text
chatgpt-windows-lars=<64-hex-sha256>,deepseek-service=<64-hex-sha256>
```

Do not put clear-text bearer tokens into `SKILLZ_MCP_STATIC_TOKEN_HASHES`.

## Generate a credential on Windows

Run this in PowerShell on the Windows machine that will run ChatGPT:

```powershell
$bytes = New-Object byte[] 32
[System.Security.Cryptography.RandomNumberGenerator]::Fill($bytes)
$token = "skz_" + [Convert]::ToBase64String($bytes).TrimEnd('=').Replace('+','-').Replace('/','_')
$hashBytes = [System.Security.Cryptography.SHA256]::HashData(
    [System.Text.Encoding]::UTF8.GetBytes($token)
)
$hash = [Convert]::ToHexString($hashBytes).ToLowerInvariant()

"Client token: $token"
"Server hash:  $hash"
```

The `Client token` is the secret. Do not commit it or paste it into GitHub, logs, tickets, or Coolify as the server credential.

The `Server hash` is safe to configure as the server-side verifier value.

## Configure Coolify

Keep the existing Authentik OAuth variables and add the named digest:

```dotenv
SKILLZ_MCP_AUTH_ISSUER_URL=https://auth.ratzeburg-ai.de/application/o/skillz/
SKILLZ_MCP_AUTH_RESOURCE_URL=https://skillz.ratzeburg-ai.de/mcp
SKILLZ_MCP_AUTH_JWKS_URL=https://auth.ratzeburg-ai.de/application/o/skillz/jwks/
SKILLZ_MCP_AUTH_AUDIENCE=https://skillz.ratzeburg-ai.de/mcp
SKILLZ_MCP_AUTH_REQUIRED_SCOPES=skillz:read
SKILLZ_MCP_AUTH_ALGORITHMS=RS256
SKILLZ_MCP_STATIC_TOKEN_HASHES=chatgpt-windows-lars=<SERVER_HASH>
```

For multiple static clients, append additional named digests separated by commas. Use a different random token for every client/harness.

After changing the token list, redeploy/restart the immutable Skillz MCP container.

## Store the client secret on Windows

Store the clear-text token as a **user environment variable**:

```powershell
[Environment]::SetEnvironmentVariable(
    "SKILLZ_MCP_TOKEN",
    $token,
    "User"
)
```

Restart ChatGPT for Windows after creating or changing the environment variable so the application inherits the new environment.

Avoid putting the token into the MCP URL, a fixed custom header in the UI, source-controlled configuration, or a PowerShell profile.

## Configure ChatGPT for Windows

Open the custom MCP form and use:

```text
Name
Skillz

Type
Streamable HTTP

URL
https://skillz.ratzeburg-ai.de/mcp

Bearer-Token-Umgebungsvariable
SKILLZ_MCP_TOKEN
```

No additional `Authorization` header is required; the bearer-token field supplies it.

Leave custom headers empty unless a future client-specific requirement is documented.

## Acceptance test

After saving the MCP configuration, verify from ChatGPT for Windows that Skillz tools are visible and call at least:

1. `catalog_status`,
2. `search_skills` with a known query,
3. `get_skill` for one exact result.

The server log may contain an authentication event similar to:

```json
{"credentialId":"chatgpt-windows-lars","event":"static_bearer_authenticated","scope":"skillz:read"}
```

It must never contain the bearer token itself.

## Rotation and revocation

To rotate a token:

1. generate a new client token and hash,
2. add/replace the corresponding digest in `SKILLZ_MCP_STATIC_TOKEN_HASHES`,
3. redeploy Skillz MCP,
4. update `SKILLZ_MCP_TOKEN` on Windows,
5. restart ChatGPT for Windows,
6. confirm the old token now returns `401`.

To revoke a client, remove only its named digest from `SKILLZ_MCP_STATIC_TOKEN_HASHES` and redeploy. Other static credentials and Authentik OAuth clients remain unaffected.

## Design boundary

Static bearer credentials are deliberately limited to the current **read-only Phase-1 MCP surface**. They must not automatically gain future write/execution capabilities. If a later Skillz MCP phase introduces side effects, static credentials require a new explicit authorization review before they can access them.
