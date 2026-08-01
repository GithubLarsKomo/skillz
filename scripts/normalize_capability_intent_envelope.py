#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from compile_capability_intent import normalize_intent

ENVELOPE_SCHEMA_VERSION = 1
PRODUCER_KINDS = {"manual", "deterministic", "model"}
CONFIDENCE_LEVELS = {"asserted", "high", "medium", "low", "unknown"}


def load_json(path: str) -> dict:
    try:
        text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        data = json.loads(text)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read intent envelope JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("intent envelope root must be an object")
    return data


def require_object(value: object, label: str, allowed: set[str], required: set[str]) -> dict:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object")
    unknown = sorted(set(value) - allowed)
    if unknown:
        raise ValueError(f"unknown {label} field(s): {', '.join(unknown)}")
    missing = sorted(required - set(value))
    if missing:
        raise ValueError(f"missing {label} field(s): {', '.join(missing)}")
    return value


def string_list(value: object, label: str) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{label} must be an array of strings")
    return sorted(set(value))


def normalize_envelope(envelope: dict) -> dict:
    allowed = {"schemaVersion", "intent", "provenance", "confidence", "review"}
    unknown = sorted(set(envelope) - allowed)
    if unknown:
        raise ValueError(f"unknown intent envelope field(s): {', '.join(unknown)}")
    if envelope.get("schemaVersion") != ENVELOPE_SCHEMA_VERSION:
        raise ValueError(
            f"unsupported intent envelope schemaVersion {envelope.get('schemaVersion')!r}; expected {ENVELOPE_SCHEMA_VERSION}"
        )
    if "intent" not in envelope:
        raise ValueError("missing intent envelope field(s): intent")
    intent = envelope["intent"]
    if not isinstance(intent, dict):
        raise ValueError("intent must be an object")
    normalized_intent = normalize_intent(intent)

    provenance = require_object(
        envelope.get("provenance"),
        "provenance",
        {"producerKind", "producer", "sourceRefs"},
        {"producerKind", "producer", "sourceRefs"},
    )
    producer_kind = provenance["producerKind"]
    if producer_kind not in PRODUCER_KINDS:
        raise ValueError(f"unsupported producerKind: {producer_kind!r}")
    producer = provenance["producer"]
    if not isinstance(producer, str):
        raise ValueError("provenance producer must be a string")
    source_refs = string_list(provenance["sourceRefs"], "provenance sourceRefs")

    confidence = require_object(
        envelope.get("confidence"),
        "confidence",
        {"level", "basis"},
        {"level", "basis"},
    )
    level = confidence["level"]
    if level not in CONFIDENCE_LEVELS:
        raise ValueError(f"unsupported confidence level: {level!r}")
    basis = string_list(confidence["basis"], "confidence basis")

    review = require_object(
        envelope.get("review"),
        "review",
        {"reviewRequired", "reasons"},
        {"reviewRequired", "reasons"},
    )
    review_required = review["reviewRequired"]
    if not isinstance(review_required, bool):
        raise ValueError("review reviewRequired must be a boolean")
    reasons = string_list(review["reasons"], "review reasons")

    return {
        "schemaVersion": ENVELOPE_SCHEMA_VERSION,
        "intent": normalized_intent,
        "provenance": {
            "producerKind": producer_kind,
            "producer": producer,
            "sourceRefs": source_refs,
        },
        "confidence": {"level": level, "basis": basis},
        "review": {"reviewRequired": review_required, "reasons": reasons},
    }


def render_json(payload: dict) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Normalize a provenance-aware capability intent envelope.")
    parser.add_argument("envelope", help="Envelope JSON file or '-' for stdin")
    parser.add_argument(
        "--extract-intent",
        action="store_true",
        help="Emit only the canonical nested capability-intent-v1 payload.",
    )
    args = parser.parse_args(argv)
    try:
        envelope = normalize_envelope(load_json(args.envelope))
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(render_json(envelope["intent"] if args.extract_intent else envelope))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
