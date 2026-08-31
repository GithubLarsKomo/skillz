# Skillz MCP local use

The local server is read-only and uses the same deterministic `skillz_core` implementation as the CLI wrappers.

## Install

From the repository root:

```bash
python -m pip install .
```

## stdio

Run directly:

```bash
skillz-mcp --repository-root /path/to/skillz
```

Equivalent module invocation:

```bash
python -m skillz_mcp --repository-root /path/to/skillz
```

A generic MCP client configuration looks like:

```json
{
  "mcpServers": {
    "skillz": {
      "command": "skillz-mcp",
      "args": ["--repository-root", "/path/to/skillz"]
    }
  }
}
```

stdio does not use HTTP OAuth. Its security boundary is the local process that launches the server.

## Local Streamable HTTP

For local integration testing only:

```bash
skillz-mcp \
  --repository-root /path/to/skillz \
  --transport streamable-http \
  --host 127.0.0.1 \
  --port 8000
```

Endpoint: `http://127.0.0.1:8000/mcp`

Loopback HTTP may run without OAuth. A non-loopback bind fails closed unless all remote OAuth environment variables are configured.

## Provenance

`catalog_status` and `skillz://status` expose deterministic catalog identity. A source commit can be supplied with:

```bash
export SKILLZ_MCP_COMMIT_SHA=<exact-git-sha>
```

or, in Coolify, by mapping `SOURCE_COMMIT` to `SKILLZ_MCP_COMMIT_SHA`.

An unstamped local checkout can report an unknown/not-compared source state; matching semantic versions alone are not treated as proof that generated metadata is current.

## Read-only boundary

The MCP server exposes discovery, exact capability resolution, dependency/output queries, validation, catalog metadata, skill text, references, and narrow repository metadata resources. It does not execute skills, mutate the repository, invoke GitHub writes, start arbitrary subprocesses, or call model providers.

Asset resources are metadata-only in v1; arbitrary binary asset contents are not served.
