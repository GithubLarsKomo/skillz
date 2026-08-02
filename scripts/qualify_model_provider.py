#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from build_model_interpretation_request import canonical_json, validate_index
from provider_qualification_config import fingerprint as provider_config_fingerprint
from score_capability_interpretations import SCHEMA_VERSION as SCORER_SCHEMA_VERSION, load_json, score

SCHEMA_VERSION = 2


def fingerprint(value: object) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def qualify(provider_id: str, model_id: str, benchmark: dict, proposals: dict, capability_index: dict, provider_config: dict | None = None) -> dict:
    if not isinstance(provider_id, str) or not provider_id.strip():
        raise ValueError("provider id must be non-empty")
    if not isinstance(model_id, str) or not model_id.strip():
        raise ValueError("model id must be non-empty")
    capability_index = validate_index(capability_index)
    summary = score(benchmark, proposals)
    return {
        "schemaVersion": SCHEMA_VERSION,
        "providerId": provider_id,
        "modelId": model_id,
        "providerConfigSha256": provider_config_fingerprint(provider_id, model_id, provider_config),
        "benchmarkSha256": fingerprint(benchmark),
        "proposalSetSha256": fingerprint(proposals),
        "capabilityIndexSha256": fingerprint(capability_index),
        "scorerSchemaVersion": SCORER_SCHEMA_VERSION,
        "caseCount": summary["caseCount"],
        "passedCount": summary["passedCount"],
        "failedCount": summary["failedCount"],
        "qualified": summary["passed"],
    }


def render_json(payload: dict) -> str:
    return canonical_json(payload)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Qualify a provider/model proposal set against the capability interpretation benchmark.")
    parser.add_argument("provider_id")
    parser.add_argument("model_id")
    parser.add_argument("benchmark", type=Path)
    parser.add_argument("proposals", type=Path)
    parser.add_argument("capability_index", type=Path)
    args = parser.parse_args(argv)
    try:
        result = qualify(
            args.provider_id,
            args.model_id,
            load_json(args.benchmark),
            load_json(args.proposals),
            load_json(args.capability_index),
        )
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(render_json(result))
    return 0 if result["qualified"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
