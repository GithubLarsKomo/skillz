#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import build_model_interpretation_request as request_builder
import openai_compatible_provider as provider
import qualify_model_provider as qualifier
from score_capability_interpretations import load_json, validate_benchmark

SCHEMA_VERSION = 1
DEFAULT_BENCHMARK = Path(__file__).resolve().parents[1] / "benchmarks" / "capability-interpretation-v1.json"
DEFAULT_INDEX = Path(__file__).resolve().parents[1] / "docs" / "skill-capability-index.json"


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def provider_config(provider_id: str, endpoint: str, model_id: str, api_key_env: str | None, timeout_seconds: int) -> dict:
    config = {
        "schemaVersion": 1,
        "providerId": provider_id,
        "endpoint": endpoint,
        "modelId": model_id,
        "apiKeyEnv": api_key_env,
        "timeoutSeconds": timeout_seconds,
    }
    return provider.validate_config(config)


def _case_by_id(benchmark: dict, case_id: str) -> dict:
    for case in validate_benchmark(benchmark):
        if case["id"] == case_id:
            return case
    raise ValueError(f"unknown benchmark case id: {case_id}")


def collect_case(case: dict, index: dict, config: dict, *, transport=provider.default_transport, environ=None) -> dict:
    request = request_builder.build_request(case["sourceText"], index)
    body = canonical_json(provider.render_request_body(request, config)).encode("utf-8")
    headers = provider.build_headers(config, environ)
    raw = transport(config["endpoint"], body, headers, config["timeoutSeconds"])
    proposal = provider.bind_model_identity(provider.parse_provider_response(raw), config["modelId"])
    return {"caseId": case["id"], "proposal": proposal}


def run_live(
    mode: str,
    provider_id: str,
    endpoint: str,
    model_id: str,
    benchmark: dict,
    capability_index: dict,
    *,
    case_id: str | None = None,
    api_key_env: str | None = "CAPABILITY_PROVIDER_API_KEY",
    timeout_seconds: int = 60,
    transport=provider.default_transport,
    environ=None,
) -> tuple[dict, dict | None]:
    if mode not in {"smoke-only", "qualify"}:
        raise ValueError("mode must be 'smoke-only' or 'qualify'")
    benchmark_cases = validate_benchmark(benchmark)
    capability_index = request_builder.validate_index(capability_index)
    config = provider_config(provider_id, endpoint, model_id, api_key_env, timeout_seconds)

    if mode == "smoke-only" and not case_id:
        raise ValueError("smoke-only mode requires a benchmark case id")
    selected = [_case_by_id(benchmark, case_id)] if mode == "smoke-only" else benchmark_cases

    proposal_rows: list[dict] = []
    completed_ids: list[str] = []
    try:
        for case in selected:
            proposal_rows.append(collect_case(case, capability_index, config, transport=transport, environ=environ))
            completed_ids.append(case["id"])
    except ValueError as exc:
        return {
            "schemaVersion": SCHEMA_VERSION,
            "mode": mode,
            "status": "failed",
            "failedStage": "provider-collection",
            "providerId": provider_id,
            "modelId": model_id,
            "benchmarkSha256": qualifier.fingerprint(benchmark),
            "capabilityIndexSha256": qualifier.fingerprint(capability_index),
            "caseCount": len(selected),
            "completedCaseCount": len(completed_ids),
            "completedCaseIds": completed_ids,
            "qualified": None,
            "error": str(exc),
        }, None

    proposals = {"schemaVersion": 1, "proposals": proposal_rows}
    if mode == "smoke-only":
        return {
            "schemaVersion": SCHEMA_VERSION,
            "mode": mode,
            "status": "passed",
            "failedStage": None,
            "providerId": provider_id,
            "modelId": model_id,
            "benchmarkSha256": qualifier.fingerprint(benchmark),
            "capabilityIndexSha256": qualifier.fingerprint(capability_index),
            "caseCount": 1,
            "completedCaseCount": 1,
            "completedCaseIds": completed_ids,
            "qualified": None,
            "error": None,
        }, None

    try:
        qualification = qualifier.qualify(provider_id, model_id, benchmark, proposals, capability_index)
    except ValueError as exc:
        return {
            "schemaVersion": SCHEMA_VERSION,
            "mode": mode,
            "status": "failed",
            "failedStage": "qualification",
            "providerId": provider_id,
            "modelId": model_id,
            "benchmarkSha256": qualifier.fingerprint(benchmark),
            "capabilityIndexSha256": qualifier.fingerprint(capability_index),
            "caseCount": len(selected),
            "completedCaseCount": len(completed_ids),
            "completedCaseIds": completed_ids,
            "qualified": False,
            "error": str(exc),
        }, None

    summary = {
        "schemaVersion": SCHEMA_VERSION,
        "mode": mode,
        "status": "qualified" if qualification["qualified"] else "not-qualified",
        "failedStage": None if qualification["qualified"] else "qualification",
        "providerId": provider_id,
        "modelId": model_id,
        "benchmarkSha256": qualification["benchmarkSha256"],
        "capabilityIndexSha256": qualification["capabilityIndexSha256"],
        "caseCount": qualification["caseCount"],
        "completedCaseCount": len(completed_ids),
        "completedCaseIds": completed_ids,
        "passedCount": qualification["passedCount"],
        "failedCount": qualification["failedCount"],
        "qualified": qualification["qualified"],
        "error": None,
    }
    return summary, qualification


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Manually validate a live OpenAI-compatible capability interpretation provider.")
    parser.add_argument("--mode", choices=("smoke-only", "qualify"), required=True)
    parser.add_argument("--provider-id", required=True)
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--case-id")
    auth = parser.add_mutually_exclusive_group()
    auth.add_argument("--api-key-env", default="CAPABILITY_PROVIDER_API_KEY")
    auth.add_argument("--no-auth", action="store_true")
    parser.add_argument("--timeout-seconds", type=int, default=60)
    parser.add_argument("--benchmark", type=Path, default=DEFAULT_BENCHMARK)
    parser.add_argument("--capability-index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--qualification-out", type=Path)
    args = parser.parse_args(argv)

    try:
        benchmark = load_json(args.benchmark)
        capability_index = load_json(args.capability_index)
        summary, qualification = run_live(
            args.mode,
            args.provider_id,
            args.endpoint,
            args.model_id,
            benchmark,
            capability_index,
            case_id=args.case_id,
            api_key_env=None if args.no_auth else args.api_key_env,
            timeout_seconds=args.timeout_seconds,
            environ=os.environ,
        )
        if qualification is not None and args.qualification_out is not None:
            args.qualification_out.write_text(canonical_json(qualification) + "\n", encoding="utf-8")
    except (OSError, ValueError) as exc:
        print(canonical_json({
            "schemaVersion": SCHEMA_VERSION,
            "mode": args.mode,
            "status": "failed",
            "failedStage": "configuration",
            "providerId": args.provider_id,
            "modelId": args.model_id,
            "qualified": None,
            "error": str(exc),
        }))
        return 2

    print(canonical_json(summary))
    if summary["status"] in {"passed", "qualified"}:
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
