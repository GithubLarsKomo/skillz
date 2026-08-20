from __future__ import annotations

import argparse
from pathlib import Path

from .server import create_server


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the read-only Skillz MCP server.")
    parser.add_argument("--repository-root", type=Path, default=None)
    args = parser.parse_args()
    create_server(args.repository_root).run(transport="stdio")


if __name__ == "__main__":
    main()
