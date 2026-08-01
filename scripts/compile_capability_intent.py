#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

INTENT_SCHEMA_VERSION = 1
REQUEST_SCHEMA_VERSION = 1
VALID_MODES = {"rubric", "compatibility", "none"}
VALID_PORTABLE = {"required", "forbidden", "irrelevant"}


def load_json(path: str) -> dict:
    try:
        text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        data = json.loads(text)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read intent JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("intent root must be an object")
    return data


def normalize_intent(intent: dict) -> dict:
    allowed = {"schemaVersion", "desiredOutputs", "requiredDependencies", "allowedEvaluationModes", "portableFiles"}
    unknown = sorted(set(intent) - allowed)
    if unknown:
        raise ValueError(f"unknown intent field(s): {', '.join(unknown)}")
    if intent.get("schemaVersion") != INTENT_SCHEMA_VERSION:
        raise ValueError(f"unsupported intent schemaVersion {intent.get('schemaVersion')!r}; expected {INTENT_SCHEMA_VERSION}")

    outputs = intent.get("desiredOutputs", [])
    dependencies = intent.get("requiredDependencies", [])
    modes = intent.get("allowedEvaluationModes", [])
    portable = intent.get("portableFiles", "irrelevant")
    for label, value in (("desiredOutputs", outputs), ("requiredDependencies", dependencies), ("allowedEvaluationModes", modes)):
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            raise ValueError(f"{label} must be an array of strings")
    invalid_modes = sorted(set(modes) - VALID_MODES)
    if invalid_modes:
        raise ValueError(f"unsupported evaluation mode(s): {', '.join(invalid_modes)}")
    if portable not in VALID_PORTABLE:
        raise ValueError(f"unsupported portableFiles value: {portable!r}")

    return {
        "schemaVersion": INTENT_SCHEMA_VERSION,
        "desiredOutputs": sorted(set(outputs)),
        "requiredDependencies": sorted(set(dependencies)),
        "allowedEvaluationModes": sorted(set(modes)),
        "portableFiles": portable,
    }


def compile_intent(intent: dict) -> dict:
    normalized = normalize_intent(intent)
    return {
        "schemaVersion": REQUEST_SCHEMA_VERSION,
        "outputs": normalized["desiredOutputs"],
        "dependencies": normalized["requiredDependencies"],
        "evaluationModes": normalized["allowedEvaluationModes"],
        "portableFiles": normalized["portableFiles"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compile structured capability intent into a resolver request.")
    parser.add_argument("intent", help="Intent JSON file or '-' for stdin")
    args = parser.parse_args(argv)
    try:
        payload = compile_intent(load_json(args.intent))
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
