from __future__ import annotations

import argparse
import os
from pathlib import Path
from urllib.parse import urlparse

from mcp.server.transport_security import TransportSecuritySettings

from .auth import RemoteAuthConfig, auth_config_from_env, build_token_verifier, static_tokens_from_env
from .server import create_server

LOOPBACK_HOSTS = {"127.0.0.1", "localhost", "::1"}
DEFAULT_MAX_REQUEST_BYTES = 262_144


def _transport_security(auth_config: RemoteAuthConfig | None) -> TransportSecuritySettings | None:
    if auth_config is None:
        return None
    parsed = urlparse(auth_config.resource_url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("SKILLZ_MCP_AUTH_RESOURCE_URL must be an absolute HTTP(S) URL")
    host = parsed.hostname
    origin = f"{parsed.scheme}://{parsed.netloc}"
    allowed_hosts = [host, f"{host}:*"]
    for loopback in sorted(LOOPBACK_HOSTS):
        allowed_hosts.extend((loopback, f"{loopback}:*"))
    return TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=allowed_hosts,
        allowed_origins=[origin],
    )


def _max_request_bytes() -> int:
    raw = os.environ.get("SKILLZ_MCP_MAX_REQUEST_BYTES", str(DEFAULT_MAX_REQUEST_BYTES))
    try:
        value = int(raw)
    except ValueError as exc:
        raise ValueError("SKILLZ_MCP_MAX_REQUEST_BYTES must be an integer") from exc
    if value < 1 or value > 4_194_304:
        raise ValueError("SKILLZ_MCP_MAX_REQUEST_BYTES must be between 1 and 4194304")
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the read-only Skillz MCP server.")
    parser.add_argument("--repository-root", type=Path, default=None)
    parser.add_argument(
        "--transport",
        choices=("stdio", "streamable-http"),
        default="stdio",
        help="MCP transport; remote HTTP requires configured authentication.",
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    try:
        auth_config = auth_config_from_env()
        static_credentials = static_tokens_from_env()
        max_request_bytes = _max_request_bytes()
    except ValueError as exc:
        parser.error(str(exc))

    token_verifier = None
    if auth_config is not None:
        token_verifier = build_token_verifier(auth_config, static_credentials=static_credentials)

    runtime_commit = os.environ.get("SKILLZ_MCP_COMMIT_SHA") or os.environ.get("SOURCE_COMMIT")
    runtime_version = os.environ.get("SKILLZ_MCP_VERSION")
    server = create_server(
        args.repository_root,
        runtime_commit=runtime_commit,
        runtime_version=runtime_version,
        auth_config=auth_config,
        token_verifier=token_verifier,
    )

    if args.transport == "stdio":
        server.run(transport="stdio")
        return

    if args.host not in LOOPBACK_HOSTS and auth_config is None:
        parser.error("remote Streamable HTTP requires authentication; configure OAuth resource-server settings")

    try:
        transport_security = _transport_security(auth_config)
    except ValueError as exc:
        parser.error(str(exc))

    server.run(
        transport="streamable-http",
        host=args.host,
        port=args.port,
        stateless_http=True,
        json_response=True,
        max_request_body_size=max_request_bytes,
        transport_security=transport_security,
    )


if __name__ == "__main__":
    main()
