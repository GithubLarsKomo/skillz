#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from normalize_capability_intent_envelope import normalize_envelope, render_json

REVIEW_SCHEMA_VERSION = 1
REVIEW_DECISIONS = {"approved", "rejected"}


def load_json(path: str, label: str) -> dict:
    try:
        text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        data = json.loads(text)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read {label} JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{label} root must be an object")
    return data


def normalize_review(review: dict) -> dict:
    allowed = {"schemaVersion", "decision", "reviewer", "reasons"}
    unknown = sorted(set(review) - allowed)
    if unknown:
        raise ValueError(f"unknown review field(s): {', '.join(unknown)}")
    if review.get("schemaVersion") != REVIEW_SCHEMA_VERSION:
        raise ValueError(
            f"unsupported review schemaVersion {review.get('schemaVersion')!r}; expected {REVIEW_SCHEMA_VERSION}"
        )
    missing = sorted({"decision", "reviewer", "reasons"} - set(review))
    if missing:
        raise ValueError(f"missing review field(s): {', '.join(missing)}")
    decision = review["decision"]
    if decision not in REVIEW_DECISIONS:
        raise ValueError(f"unsupported review decision: {decision!r}")
    reviewer = review["reviewer"]
    if not isinstance(reviewer, str):
        raise ValueError("reviewer must be a string")
    reasons = review["reasons"]
    if not isinstance(reasons, list) or not all(isinstance(item, str) for item in reasons):
        raise ValueError("review reasons must be an array of strings")
    return {
        "schemaVersion": REVIEW_SCHEMA_VERSION,
        "decision": decision,
        "reviewer": reviewer,
        "reasons": sorted(set(reasons)),
    }


def validate_producer_policy(envelope: dict) -> None:
    producer_kind = envelope["provenance"]["producerKind"]
    review_required = envelope["review"]["reviewRequired"]
    if producer_kind == "model" and not review_required:
        raise ValueError("model-produced intent envelopes must require explicit review")


def admit(envelope: dict, review: dict | None) -> dict:
    validate_producer_policy(envelope)
    review_required = envelope["review"]["reviewRequired"]
    if review is not None and review["decision"] == "rejected":
        raise ValueError("review decision rejected")
    if review_required:
        if review is None:
            raise ValueError("review is required before intent admission")
        if review["decision"] != "approved":
            raise ValueError("review approval is required before intent admission")
    return envelope["intent"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Admit a provenance-aware capability intent into the deterministic pipeline.")
    parser.add_argument("envelope", help="Intent envelope JSON file or '-' for stdin")
    parser.add_argument("--review", help="Optional capability-intent-review-v1 JSON file, or '-' for stdin")
    args = parser.parse_args(argv)
    if args.envelope == "-" and args.review == "-":
        print("ERROR: envelope and review cannot both read from stdin", file=sys.stderr)
        return 2
    try:
        try:
            envelope = normalize_envelope(load_json(args.envelope, "intent envelope"))
        except ValueError as exc:
            raise ValueError(f"envelope validation: {exc}") from exc
        try:
            validate_producer_policy(envelope)
        except ValueError as exc:
            raise ValueError(f"producer policy: {exc}") from exc
        review = None
        if args.review:
            try:
                review = normalize_review(load_json(args.review, "review"))
            except ValueError as exc:
                raise ValueError(f"review validation: {exc}") from exc
        try:
            intent = admit(envelope, review)
        except ValueError as exc:
            raise ValueError(f"admission policy: {exc}") from exc
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(render_json(intent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
