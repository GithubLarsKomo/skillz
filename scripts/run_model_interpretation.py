#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from adapt_model_interpretation import adapt
from model_interpretation_request_contract import canonical_json, validate_request
from score_capability_interpretations import load_json as load_benchmark_json, score_case, validate_benchmark

SCHEMA_VERSION = 1
FIXTURE_SCHEMA_VERSION = 1


def read_json(path: str, label: str) -> dict:
    try:
        text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        data = json.loads(text)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read {label} JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{label} root must be an object")
    return data


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
    for case in validate_benchmark(benchmark):
        if case["id"] == case_id:
            return case
    raise ValueError(f"unknown benchmark case id: {case_id}")


def _result(request: dict, kind: str, provider_id: str, proposal: dict | None, validation_error: str | None, benchmark_finding=None) -> dict:
    adapter_compatible = proposal is not None and validation_error is None
    return {
        "schemaVersion": SCHEMA_VERSION,
        "requestId": request["requestId"],
        "provider": {"kind": kind, "id": provider_id},
        "status": "accepted" if adapter_compatible else "rejected",
        "proposal": proposal,
        "adapterCompatible": adapter_compatible,
        "validationError": validation_error,
        "benchmarkFinding": benchmark_finding,
    }


def run(request: dict, fixture: dict, benchmark: dict | None = None, case_id: str | None = None) -> dict:
    request = validate_request(request)
    provider_id = "unknown"
    proposal = None
    finding = None
    try:
        provider_id, proposal = parse_fixture(fixture)
        adapt(proposal)
        if benchmark is not None or case_id is not None:
            if benchmark is None or case_id is None:
                raise ValueError("benchmark and case id must be provided together")
            finding = score_case(find_benchmark_case(benchmark, case_id), proposal)
        return _result(request, "fixture", provider_id, proposal, None, finding)
    except ValueError as exc:
        return _result(request, "fixture", provider_id, proposal, str(exc), finding)


def run_openai_compatible(request: dict, config: dict, qualification: dict, benchmark: dict, capability_index: dict, *, case_id: str | None = None, transport=None, environ=None) -> dict:
    request = validate_request(request)
    provider_id = config.get("providerId", "unknown") if isinstance(config, dict) else "unknown"
    proposal = None
    finding = None
    try:
        import openai_compatible_provider as provider
        kwargs = {"environ": environ}
        if transport is not None:
            kwargs["transport"] = transport
        proposal = provider.invoke(request, config, qualification, benchmark, capability_index, **kwargs)
        provider_id = config["providerId"]
        if case_id is not None:
            finding = score_case(find_benchmark_case(benchmark, case_id), proposal)
        return _result(request, "openai-compatible", provider_id, proposal, None, finding)
    except ValueError as exc:
        return _result(request, "openai-compatible", provider_id, proposal, str(exc), finding)


def validate_mode_args(mode: str, qualification, benchmark, capability_index, qualification_registry=None) -> None:
    if mode == "fixture":
        if qualification is not None or qualification_registry is not None or capability_index is not None:
            raise ValueError("fixture mode does not accept qualification, qualification-registry, or capability-index arguments")
        return
    if benchmark is None or capability_index is None:
        raise ValueError("openai-compatible mode requires --benchmark and --capability-index")
    if (qualification is None) == (qualification_registry is None):
        raise ValueError("openai-compatible mode requires exactly one of --qualification or --qualification-registry")


def resolve_qualification(config: dict, direct_qualification: dict | None, registry_path: Path | None, benchmark: dict, capability_index: dict) -> dict:
    if direct_qualification is not None:
        return direct_qualification
    if registry_path is None:
        raise ValueError("qualification source is required")
    import openai_compatible_provider as provider
    import qualification_registry as registry
    config = provider.validate_config(config)
    return registry.lookup(registry_path, config["providerId"], config["modelId"], benchmark, capability_index)


def resolve_registry_pair(provider_registry: Path, qualification_registry: Path, provider_id: str, model_id: str, benchmark: dict, capability_index: dict) -> tuple[dict, dict]:
    import provider_config_registry
    return provider_config_registry.resolve_pair(
        provider_registry,
        qualification_registry,
        provider_id,
        model_id,
        benchmark,
        capability_index,
    )


def validate_registry_pair_args(args) -> bool:
    pair_mode = args.provider_registry is not None or args.provider_id is not None or args.model_id is not None
    if not pair_mode:
        return False
    if args.provider_mode != "openai-compatible":
        raise ValueError("registry-pair mode requires --provider-mode openai-compatible")
    if args.provider_input is not None or args.qualification is not None:
        raise ValueError("registry-pair mode is mutually exclusive with provider input and direct qualification")
    if args.provider_registry is None or args.qualification_registry is None or not args.provider_id or not args.model_id:
        raise ValueError("registry-pair mode requires --provider-registry, --qualification-registry, --provider-id, and --model-id")
    if args.benchmark is None or args.capability_index is None:
        raise ValueError("registry-pair mode requires --benchmark and --capability-index")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run one capability interpretation through an explicit provider adapter.")
    parser.add_argument("request", help="Interpretation request JSON file or '-' for stdin")
    parser.add_argument("provider_input", nargs="?", help="Fixture JSON or provider-config JSON file")
    parser.add_argument("--provider-mode", choices=("fixture", "openai-compatible"), default="fixture")
    qualification_group = parser.add_mutually_exclusive_group()
    qualification_group.add_argument("--qualification", type=Path)
    qualification_group.add_argument("--qualification-registry", type=Path)
    parser.add_argument("--provider-registry", type=Path)
    parser.add_argument("--provider-id")
    parser.add_argument("--model-id")
    parser.add_argument("--benchmark", type=Path)
    parser.add_argument("--capability-index", type=Path)
    parser.add_argument("--case-id")
    args = parser.parse_args(argv)
    if args.request == "-" and args.provider_input == "-":
        print("ERROR: request and provider input cannot both read from stdin", file=sys.stderr)
        return 2
    try:
        pair_mode = validate_registry_pair_args(args)
        request = read_json(args.request, "interpretation request")
        benchmark = load_benchmark_json(args.benchmark) if args.benchmark else None
        if pair_mode:
            capability_index = read_json(str(args.capability_index), "capability index")
            config, qualification = resolve_registry_pair(
                args.provider_registry,
                args.qualification_registry,
                args.provider_id,
                args.model_id,
                benchmark,
                capability_index,
            )
            result = run_openai_compatible(request, config, qualification, benchmark, capability_index, case_id=args.case_id)
        else:
            if args.provider_input is None:
                raise ValueError("provider input is required outside registry-pair mode")
            validate_mode_args(args.provider_mode, args.qualification, args.benchmark, args.capability_index, args.qualification_registry)
            provider_input = read_json(args.provider_input, "provider input")
            if args.provider_mode == "fixture":
                result = run(request, provider_input, benchmark, args.case_id)
            else:
                capability_index = read_json(str(args.capability_index), "capability index")
                direct_qualification = read_json(str(args.qualification), "qualification") if args.qualification else None
                qualification = resolve_qualification(provider_input, direct_qualification, args.qualification_registry, benchmark, capability_index)
                result = run_openai_compatible(request, provider_input, qualification, benchmark, capability_index, case_id=args.case_id)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(canonical_json(result))
    return 0 if result["status"] == "accepted" else 1


if __name__ == "__main__":
    raise SystemExit(main())
