#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = ROOT / "docs" / "skill-capability-index.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


compiler = load_module("compile_capability_intent", ROOT / "scripts" / "compile_capability_intent.py")
resolver = load_module("resolve_capabilities", ROOT / "scripts" / "resolve_capabilities.py")


def run_pipeline(intent_source: str, index_path: Path) -> dict:
    try:
        intent = compiler.load_json(intent_source)
        request = compiler.compile_intent(intent)
    except ValueError as exc:
        raise ValueError(f"compiler stage: {exc}") from exc

    try:
        constraints = resolver.normalize_constraints(
            request.get("outputs", []),
            request.get("dependencies", []),
            request.get("evaluationModes", []),
            request.get("portableFiles", "irrelevant"),
        )
        return resolver.resolve(resolver.load_index(index_path), constraints)
    except ValueError as exc:
        raise ValueError(f"resolver stage: {exc}") from exc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Compile structured capability intent and resolve it against the capability index."
    )
    parser.add_argument("intent", help="Intent JSON file or '-' for stdin")
    parser.add_argument("--json", action="store_true", help="Emit stable machine-readable JSON.")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    try:
        payload = run_pipeline(args.intent, args.index)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    else:
        print(resolver.render_human(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
