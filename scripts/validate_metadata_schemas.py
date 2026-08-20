#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_SCHEMA = ROOT / "schemas" / "skill-capability-index-v1.schema.json"
QUERY_SCHEMA = ROOT / "schemas" / "capability-query-output-v1.schema.json"
RESOLVER_SCHEMA = ROOT / "schemas" / "capability-resolver-output-v1.schema.json"
INDEX_FILE = ROOT / "docs" / "skill-capability-index.json"
QUERY_SCRIPT = ROOT / "scripts" / "query_capabilities.py"
RESOLVER_SCRIPT = ROOT / "scripts" / "resolve_capabilities.py"


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from exc


def type_matches(value: object, expected: str) -> bool:
    mapping = {
        "object": dict,
        "array": list,
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "null": type(None),
    }
    if expected in {"integer", "number"} and isinstance(value, bool):
        return False
    return isinstance(value, mapping[expected])


def validate(value: object, schema: dict, path: str = "$") -> list[str]:
    errors: list[str] = []
    if "anyOf" in schema:
        branches = schema["anyOf"]
        if not isinstance(branches, list):
            return [f"{path}: schema anyOf must be a list"]
        branch_errors = [validate(value, branch, path) for branch in branches]
        if not any(not item for item in branch_errors):
            errors.append(f"{path}: does not match any allowed schema shape")
        return errors

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}, got {value!r}")
        return errors
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: unsupported value {value!r}; expected one of {schema['enum']!r}")
        return errors

    expected_type = schema.get("type")
    if expected_type is not None:
        allowed = expected_type if isinstance(expected_type, list) else [expected_type]
        if not any(type_matches(value, item) for item in allowed):
            errors.append(f"{path}: expected type {allowed!r}, got {type(value).__name__}")
            return errors

    if isinstance(value, str) and "minLength" in schema:
        minimum = schema["minLength"]
        if not isinstance(minimum, int) or isinstance(minimum, bool) or minimum < 0:
            errors.append(f"{path}: schema minLength must be a non-negative integer")
            return errors
        if len(value) < minimum:
            errors.append(f"{path}: string length {len(value)} is less than minLength {minimum}")

    if isinstance(value, list) and "minItems" in schema:
        minimum = schema["minItems"]
        if not isinstance(minimum, int) or isinstance(minimum, bool) or minimum < 0:
            errors.append(f"{path}: schema minItems must be a non-negative integer")
            return errors
        if len(value) < minimum:
            errors.append(f"{path}: array length {len(value)} is less than minItems {minimum}")

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        minimum = schema.get("minimum")
        maximum = schema.get("maximum")
        if minimum is not None and value < minimum:
            errors.append(f"{path}: value {value!r} is less than minimum {minimum!r}")
        if maximum is not None and value > maximum:
            errors.append(f"{path}: value {value!r} is greater than maximum {maximum!r}")

    if isinstance(value, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                errors.append(f"{path}.{key}: missing required property")
        properties = schema.get("properties", {})
        for key, item in value.items():
            child = f"{path}.{key}"
            if key in properties:
                errors.extend(validate(item, properties[key], child))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{child}: unknown property")
    elif isinstance(value, list) and "items" in schema:
        for idx, item in enumerate(value):
            errors.extend(validate(item, schema["items"], f"{path}[{idx}]") )
    return errors


def validate_file(data_path: Path, schema_path: Path) -> list[str]:
    schema = load_json(schema_path)
    data = load_json(data_path)
    if not isinstance(schema, dict):
        return [f"{schema_path}: schema root must be an object"]
    return validate(data, schema)


def script_json(script: Path, label: str, *args: str) -> object:
    command = [sys.executable, str(script), "--json", *args]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        raise ValueError(f"{label} fixture failed ({' '.join(args)}): {result.stderr.strip()}")
    return json.loads(result.stdout)


def run(root: Path) -> list[str]:
    global ROOT, INDEX_SCHEMA, QUERY_SCHEMA, RESOLVER_SCHEMA, INDEX_FILE, QUERY_SCRIPT, RESOLVER_SCRIPT
    ROOT = root
    INDEX_SCHEMA = root / "schemas" / "skill-capability-index-v1.schema.json"
    QUERY_SCHEMA = root / "schemas" / "capability-query-output-v1.schema.json"
    RESOLVER_SCHEMA = root / "schemas" / "capability-resolver-output-v1.schema.json"
    INDEX_FILE = root / "docs" / "skill-capability-index.json"
    QUERY_SCRIPT = root / "scripts" / "query_capabilities.py"
    RESOLVER_SCRIPT = root / "scripts" / "resolve_capabilities.py"

    errors = validate_file(INDEX_FILE, INDEX_SCHEMA)
    query_schema = load_json(QUERY_SCHEMA)
    resolver_schema = load_json(RESOLVER_SCHEMA)
    if not isinstance(query_schema, dict):
        errors.append(f"{QUERY_SCHEMA}: schema root must be an object")
    else:
        for label, payload in (
            ("single-skill", script_json(QUERY_SCRIPT, "query", "--skill", "agent-handoff")),
            ("list-result", script_json(QUERY_SCRIPT, "query", "--evaluation-mode", "compatibility")),
        ):
            for error in validate(payload, query_schema):
                errors.append(f"query:{label}: {error}")
    if not isinstance(resolver_schema, dict):
        errors.append(f"{RESOLVER_SCHEMA}: schema root must be an object")
    else:
        payload = script_json(
            RESOLVER_SCRIPT,
            "resolver",
            "--requires",
            "iterate-software-projects",
            "--evaluation-mode",
            "compatibility",
        )
        for error in validate(payload, resolver_schema):
            errors.append(f"resolver:representative: {error}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate versioned machine-readable metadata contracts offline.")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()
    errors = run(args.root.resolve())
    if errors:
        print("Metadata schema validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("PASS metadata schema contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
