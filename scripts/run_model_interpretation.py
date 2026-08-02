#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from adapt_model_interpretation import adapt
from score_capability_interpretations import load_json as load_benchmark_json, score_case, validate_benchmark

SCHEMA_VERSION = 1
REQUEST_SCHEMA_VERSION = 1
REQUEST_RESPONSE_SCHEMA = "capability-model-interpretation-v1"
FIXTURE_SCHEMA_VERSION = 1


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def read_json(path: str, label: str) -> dict:
    try:
        text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        data = json.loads(text)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read {label} JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{label} root must be an object")
    return data


def validate_request(request: dict) -> dict:
    required = {
        "schemaVersion", "requestId", "sourceText", "capabilityIndex",
        "availableCapabilities", "availableOutputs", "responseSchema", "controlRules",
    }
    if set(request) != required:
        raise ValueError("interpretation request has invalid fields")
    if request.get("schemaVersion") != REQUEST_SCHEMA_VERSION:
        raise ValueError(f"unsupported interpretation request schemaVersion {request.get('schemaVersion')!r}")
    if not isinstance(request.get("requestId"), str) or not request["requestId"]:
        raise ValueError("requestId must be a non-empty string")
    if request.get("responseSchema") != REQUEST_RESPONSE_SCHEMA:
        raise ValueError(f"responseSchema must be {REQUEST_RESPONSE_SCHEMA!r}")
    return request


def parse_fixture(fixture: dict) -> tuple[str, dict]:
    if set(fixture) != {"schemaVersion", "providerId", "response"}:
        raise ValueError("fixture provider must contain exactly schemaVersion, providerId, and response")
    if fixture.get("schemaVersion") != FIXTURE_SCHEMA_VERSION:
        raise ValueError(f"unsupported fixture provider schemaVersion {fixture.get('schemaVersion')!r}")
    provider_id = fixture.get("providerId")
    if not isinstance(provider_id, str) or not provider_id:
        raise ValueError("fixture providerId must be a non-empty string")
    response = fixture.get("response")
    if isinstance(response, dict):
        proposal = response
    elif isinstance(response, str):
        try:
            proposal = json.loads(response)
        except json.JSONDecodeError as exc:
            raise ValueError(f"provider output is not valid JSON: {exc}") from exc
        if not isinstance(proposal, dict):
            raise ValueError("provider output JSON root must be an object")
    else:
        raise ValueError("fixture response must be an object or JSON string")
    return provider_id, proposal


def find_benchmark_case(benchmark: dict, case_id: str) -> dict:
    cases = validate_benchmark(benchmark)
    for case in cases:
        if case["id"] == case_id:
            return case
    raise ValueError(f"unknown benchmark case id: {case_id}")


def run(request: dict, fixture: dict, benchmark: dict | None = None, case_id: str | None = None) -> dict:
    request = validate_request(request)
    provider_id = "unknown"
    proposal: dict | None = None
    validation_error: str | None = None
    adapter_compatible = False
    benchmark_finding = None
    try:
        provider_id, proposal = parse_fixture(fixture)
        adapt(proposal)
        adapter_compatible = True
        if benchmark is not None or case_id is not None:
            if benchmark is None or case_id is None:
                raise ValueError("benchmark and case id must be provided together")
            benchmark_finding = score_case(find_benchmark_case(benchmark, case_id), proposal)
    except ValueError as exc:
        validation_error = str(exc)

    accepted = adapter_compatible and validation_error is None
    return {
        "schemaVersion": SCHEMA_VERSION,
        "requestId": request["requestId"],
        "provider": {"kind": "fixture", "id": provider_id},
        "status": "accepted" if accepted else "rejected",
        "proposal": proposal,
        "adapterCompatible": adapter_compatible,
        "validationError": validation_error,
        "benchmarkFinding": benchmark_finding,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run one capability interpretation through a provider-neutral fixture adapter.")
    parser.add_argument("request", help="Interpretation request JSON file or '-' for stdin")
    parser.add_argument("fixture", help="Fixture provider JSON file")
    parser.add_argument("--benchmark", type=Path)
    parser.add_argument("--case-id")
    args = parser.parse_args(argv)
    if args.request == "-" and args.fixture == "-":
        print("ERROR: request and fixture cannot both read from stdin", file=sys.stderr)
        return 2
    try:
        request = read_json(args.request, "interpretation request")
        fixture = read_json(args.fixture, "fixture provider")
        benchmark = load_benchmark_json(args.benchmark) if args.benchmark else None
        result = run(request, fixture, benchmark, args.case_id)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(canonical_json(result))
    return 0 if result["status"] == "accepted" else 1


if __name__ == "__main__":
    raise SystemExit(main())
