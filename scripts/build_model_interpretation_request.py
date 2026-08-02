#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

SCHEMA_VERSION = 1
INDEX_SCHEMA_VERSION = 1
RESPONSE_SCHEMA = "capability-model-interpretation-v1"
DEFAULT_INDEX = Path(__file__).resolve().parents[1] / "docs" / "skill-capability-index.json"
CONTROL_RULES = [
    "Do not emit producerKind or other provenance controls.",
    "Do not emit reviewRequired or admission decisions.",
    "Return only capability-model-interpretation-v1 fields.",
]


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def validate_index(data: object) -> dict:
    if not isinstance(data, dict):
        raise ValueError("capability index root must be an object")
    if data.get("schemaVersion") != INDEX_SCHEMA_VERSION:
        raise ValueError(f"unsupported capability index schemaVersion {data.get('schemaVersion')!r}; expected {INDEX_SCHEMA_VERSION}")
    skills = data.get("skills")
    if not isinstance(skills, list):
        raise ValueError("capability index skills must be a list")
    for index, skill in enumerate(skills):
        if not isinstance(skill, dict) or not isinstance(skill.get("name"), str) or not skill["name"]:
            raise ValueError(f"capability index skills[{index}].name must be non-empty")
        outputs = skill.get("outputs")
        if not isinstance(outputs, list) or any(not isinstance(item, str) for item in outputs):
            raise ValueError(f"capability index skills[{index}].outputs must be an array of strings")
    return data


def load_index(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read capability index: {exc}") from exc
    return validate_index(data)


def build_request(source_text: str, index: dict) -> dict:
    if not isinstance(source_text, str) or not source_text.strip():
        raise ValueError("source text must be non-empty")
    index = validate_index(index)
    skills = index["skills"]
    capability_names = sorted({skill["name"] for skill in skills})
    outputs = sorted({output for skill in skills for output in skill["outputs"]})
    index_fingerprint = sha256_text(canonical_json(index))
    basis = {
        "schemaVersion": SCHEMA_VERSION,
        "sourceText": source_text,
        "capabilityIndex": {"schemaVersion": INDEX_SCHEMA_VERSION, "sha256": index_fingerprint},
        "availableCapabilities": capability_names,
        "availableOutputs": outputs,
        "responseSchema": RESPONSE_SCHEMA,
        "controlRules": sorted(CONTROL_RULES),
    }
    request_id = sha256_text(canonical_json(basis))
    return {"requestId": request_id, **basis}


def render_json(payload: dict) -> str:
    return canonical_json(payload)


def read_source(path: str) -> str:
    try:
        return sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"cannot read source text: {exc}") from exc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build a deterministic provider-neutral capability interpretation request.")
    parser.add_argument("source", help="Source text file or '-' for stdin")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    try:
        payload = build_request(read_source(args.source), load_index(args.index))
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(render_json(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
