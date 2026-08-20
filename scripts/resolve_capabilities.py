#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillz_core import load_index, normalize_constraints, resolve
from skillz_core.resolver import VALID_MODES, VALID_PORTABLE

REQUEST_SCHEMA_VERSION = 1
REQUEST_FIELDS = {"schemaVersion", "outputs", "dependencies", "evaluationModes", "portableFiles"}
DEFAULT_INDEX = ROOT / "docs" / "skill-capability-index.json"


def load_request(source: str) -> dict:
    try:
        text = sys.stdin.read() if source == "-" else Path(source).read_text(encoding="utf-8")
        data = json.loads(text)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read resolver request: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("resolver request root must be an object")
    if data.get("schemaVersion") != REQUEST_SCHEMA_VERSION:
        raise ValueError(f"unsupported resolver request schemaVersion {data.get('schemaVersion')!r}; expected {REQUEST_SCHEMA_VERSION}")
    unknown = sorted(set(data) - REQUEST_FIELDS)
    if unknown:
        raise ValueError(f"unknown resolver request field(s): {', '.join(unknown)}")
    for key in ("outputs", "dependencies", "evaluationModes"):
        value = data.get(key, [])
        if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
            raise ValueError(f"resolver request {key} must be an array of strings")
    portable = data.get("portableFiles", "irrelevant")
    if not isinstance(portable, str):
        raise ValueError("resolver request portableFiles must be a string")
    return normalize_constraints(data.get("outputs", []), data.get("dependencies", []), data.get("evaluationModes", []), portable)


def render_human(payload: dict) -> str:
    if not payload["candidates"]:
        return "No candidates match all explicit constraints."
    return "\n".join(f"{candidate['name']}: {', '.join(candidate['matchReasons']) or 'no constraints'}" for candidate in payload["candidates"])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Resolve an unranked capability candidate set from exact structured constraints.")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX, help=argparse.SUPPRESS)
    parser.add_argument("--json", action="store_true", help="Emit stable machine-readable JSON.")
    parser.add_argument("--request", help="Read a versioned resolver request from a JSON file, or '-' for stdin.")
    parser.add_argument("--output", action="append", default=[], help="Require an exact declared output; repeatable.")
    parser.add_argument("--requires", action="append", default=[], help="Require an exact direct skill dependency; repeatable.")
    parser.add_argument("--evaluation-mode", action="append", default=[], help="Allow an exact evaluation mode; repeatable.")
    parser.add_argument("--portable-files", choices=sorted(VALID_PORTABLE), default="irrelevant", help="Require, forbid, or ignore portable files.")
    args = parser.parse_args(argv)
    try:
        flag_constraints_used = bool(args.output or args.requires or args.evaluation_mode or args.portable_files != "irrelevant")
        if args.request and flag_constraints_used:
            raise ValueError("--request cannot be combined with individual constraint flags")
        constraints = load_request(args.request) if args.request else normalize_constraints(args.output, args.requires, args.evaluation_mode, args.portable_files)
        payload = resolve(load_index(args.index), constraints)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    else:
        print(render_human(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
