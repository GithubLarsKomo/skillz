from __future__ import annotations

import argparse
from pathlib import Path

from .server import create_server


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the read-only Skillz MCP server.")
    parser.add_argument("--repository-root", type=Path, default=None)
    parser.add_argument(
        "--transport",
        choices=("stdio", "streamable-http"),
        default="stdio",
        help="MCP transport; HTTP binds to localhost by default and is unauthenticated in Phase 1.",
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    server = create_server(args.repository_root)
    if args.transport == "stdio":
        server.run(transport="stdio")
        return
    server.run(
        transport="streamable-http",
        host=args.host,
        port=args.port,
        stateless_http=True,
        json_response=True,
    )


if __name__ == "__main__":
    main()
