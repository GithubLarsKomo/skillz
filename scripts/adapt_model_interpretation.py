#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from normalize_capability_intent_envelope import CONFIDENCE_LEVELS, normalize_envelope, render_json

SCHEMA_VERSION = 1
ALLOWED_FIELDS = {"schemaVersion", "intent", "model", "sourceRefs", "confidence", "confidenceBasis", "reviewReasons"}
REQUIRED_FIELDS = ALLOWED_FIELDS


def load_json(path: str) -> dict:
    try:
        text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        data = json.loads(text)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read model interpretation JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("model interpretation root must be an object")
    return data


def string_list(value: object, label: str) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{label} must be an array of strings")
    return sorted(set(value))


def adapt(proposal: dict) -> dict:
    unknown = sorted(set(proposal) - ALLOWED_FIELDS)
    if unknown:
        raise ValueError(f"unknown model interpretation field(s): {', '.join(unknown)}")
    missing = sorted(REQUIRED_FIELDS - set(proposal))
    if missing:
        raise ValueError(f"missing model interpretation field(s): {', '.join(missing)}")
    if proposal.get("schemaVersion") != SCHEMA_VERSION:
        raise ValueError(f"unsupported model interpretation schemaVersion {proposal.get('schemaVersion')!r}; expected {SCHEMA_VERSION}")
    model = proposal["model"]
    if not isinstance(model, str):
        raise ValueError("model must be a string")
    confidence = proposal["confidence"]
    if confidence not in CONFIDENCE_LEVELS:
        raise ValueError(f"unsupported confidence level: {confidence!r}")
    source_refs = string_list(proposal["sourceRefs"], "sourceRefs")
    confidence_basis = string_list(proposal["confidenceBasis"], "confidenceBasis")
    review_reasons = string_list(proposal["reviewReasons"], "reviewReasons")
    intent = proposal["intent"]
    if not isinstance(intent, dict):
        raise ValueError("intent must be an object")

    return normalize_envelope(
        {
            "schemaVersion": 1,
            "intent": intent,
            "provenance": {"producerKind": "model", "producer": model, "sourceRefs": source_refs},
            "confidence": {"level": confidence, "basis": confidence_basis},
            "review": {"reviewRequired": True, "reasons": review_reasons},
        }
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Adapt a structured model interpretation proposal into a review-required capability intent envelope.")
    parser.add_argument("proposal", help="Proposal JSON file or '-' for stdin")
    args = parser.parse_args(argv)
    try:
        payload = adapt(load_json(args.proposal))
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(render_json(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
