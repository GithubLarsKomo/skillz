#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = ROOT / "docs" / "skill-capability-index.json"
DEFAULT_VERSION = ROOT / "VERSION"
SHA_RE = re.compile(r"^[0-9a-fA-F]{40}$")


def stamp_index(
    index: dict[str, Any],
    *,
    repository: str,
    ref: str,
    version: str,
    commit_sha: str,
) -> dict[str, Any]:
    commit = commit_sha.strip().lower()
    if not SHA_RE.fullmatch(commit):
        raise ValueError("commit SHA must be a full 40-character Git commit SHA")
    if not repository.strip() or not ref.strip() or not version.strip():
        raise ValueError("repository, ref, and version are required")
    stamped = deepcopy(index)
    stamped["provenance"] = {
        "repository": repository.strip(),
        "ref": ref.strip(),
        "version": version.strip(),
        "commitSha": commit,
    }
    return stamped


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Stamp a runtime copy of the capability index with exact repository provenance."
    )
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--commit", required=True, help="Full source Git commit SHA.")
    parser.add_argument("--repository", default="GithubLarsKomo/skillz")
    parser.add_argument("--ref", default="main")
    parser.add_argument("--version")
    args = parser.parse_args(argv)

    try:
        index = json.loads(args.index.read_text(encoding="utf-8"))
        if not isinstance(index, dict):
            raise ValueError("capability index root must be an object")
        version = args.version or DEFAULT_VERSION.read_text(encoding="utf-8").strip()
        stamped = stamp_index(
            index,
            repository=args.repository,
            ref=args.ref,
            version=version,
            commit_sha=args.commit,
        )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(stamped, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
