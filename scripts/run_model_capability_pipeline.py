#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import adapt_model_interpretation as model_adapter
import admit_capability_intent as admission
import build_model_interpretation_request as request_builder
import compile_capability_intent as compiler
import resolve_capabilities as resolver
import run_model_interpretation as model_runner
from score_capability_interpretations import load_json as load_benchmark_json

SCHEMA_VERSION = 1
DEFAULT_INDEX = Path(__file__).resolve().parents[1] / "docs" / "skill-capability-index.json"
PROVIDER_MODES = ("fixture", "openai-compatible")


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def failed(stage: str, error: str, request_id: str | None = None, model_run: dict | None = None, admission_result: dict | None = None) -> dict:
    return {
        "schemaVersion": SCHEMA_VERSION,
        "status": "failed",
        "failedStage": stage,
        "requestId": request_id,
        "modelRun": model_run,
        "admission": admission_result,
        "resolverOutput": None,
        "error": error,
    }


def resolve_admitted_intent(intent: dict, index_path: Path) -> dict:
    request = compiler.compile_intent(intent)
    constraints = resolver.normalize_constraints(
        request.get("outputs", []), request.get("dependencies", []), request.get("evaluationModes", []), request.get("portableFiles", "irrelevant")
    )
    return resolver.resolve(resolver.load_index(index_path), constraints)


def run(
    source_text: str,
    provider_input: dict | None,
    review: dict | None,
    index_path: Path = DEFAULT_INDEX,
    *,
    provider_mode: str = "fixture",
    qualification: dict | None = None,
    qualification_registry: Path | None = None,
    provider_registry: Path | None = None,
    provider_id: str | None = None,
    model_id: str | None = None,
    benchmark: dict | None = None,
    transport=None,
    environ=None,
) -> dict:
    if provider_mode not in PROVIDER_MODES:
        return failed("provider-run", f"unsupported provider mode: {provider_mode}")
    try:
        index = request_builder.load_index(index_path)
        interpretation_request = request_builder.build_request(source_text, index)
    except ValueError as exc:
        return failed("request", str(exc))

    request_id = interpretation_request["requestId"]
    pair_mode = provider_registry is not None or provider_id is not None or model_id is not None
    if provider_mode == "fixture":
        if provider_input is None:
            return failed("provider-run", "fixture mode requires provider input", request_id)
        if qualification is not None or qualification_registry is not None or pair_mode:
            return failed("provider-run", "fixture mode does not accept qualification or registry-pair sources", request_id)
        model_run = model_runner.run(interpretation_request, provider_input, benchmark)
    else:
        if benchmark is None:
            return failed("provider-run", "openai-compatible mode requires benchmark", request_id)
        try:
            if pair_mode:
                if provider_input is not None or qualification is not None:
                    raise ValueError("registry-pair mode is mutually exclusive with direct provider/qualification sources")
                if provider_registry is None or qualification_registry is None or not provider_id or not model_id:
                    raise ValueError("registry-pair mode requires provider registry, qualification registry, provider id, and model id")
                config, resolved_qualification = model_runner.resolve_registry_pair(
                    provider_registry, qualification_registry, provider_id, model_id, benchmark, index
                )
            else:
                if provider_input is None:
                    raise ValueError("openai-compatible mode requires provider input outside registry-pair mode")
                if (qualification is None) == (qualification_registry is None):
                    raise ValueError("openai-compatible mode requires exactly one qualification source")
                config = provider_input
                resolved_qualification = model_runner.resolve_qualification(config, qualification, qualification_registry, benchmark, index)
        except ValueError as exc:
            return failed("provider-run", str(exc), request_id)
        model_run = model_runner.run_openai_compatible(
            interpretation_request, config, resolved_qualification, benchmark, index, transport=transport, environ=environ
        )
    if model_run["status"] != "accepted" or model_run["proposal"] is None:
        return failed("provider-run", model_run.get("validationError") or "provider run rejected", request_id, model_run)

    try:
        envelope = model_adapter.adapt(model_run["proposal"])
        normalized_review = admission.normalize_review(review) if review is not None else None
        intent = admission.admit(envelope, normalized_review)
        admission_result = {"status": "approved", "reviewProvided": normalized_review is not None, "intent": intent}
    except ValueError as exc:
        return failed("review-admission", str(exc), request_id, model_run)

    try:
        resolver_output = resolve_admitted_intent(intent, index_path)
    except ValueError as exc:
        return failed("deterministic-pipeline", str(exc), request_id, model_run, admission_result)

    return {
        "schemaVersion": SCHEMA_VERSION,
        "status": "resolved",
        "failedStage": None,
        "requestId": request_id,
        "modelRun": model_run,
        "admission": admission_result,
        "resolverOutput": resolver_output,
        "error": None,
    }


def read_json(path: str, label: str) -> dict:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read {label} JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{label} root must be an object")
    return value


def read_text(path: str) -> str:
    try:
        return sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"cannot read source text: {exc}") from exc


def validate_cli_args(args) -> bool:
    provider_registry = getattr(args, "provider_registry", None)
    provider_id = getattr(args, "provider_id", None)
    model_id = getattr(args, "model_id", None)
    provider_input = getattr(args, "provider_input", None)
    qualification = getattr(args, "qualification", None)
    qualification_registry = getattr(args, "qualification_registry", None)
    pair_mode = provider_registry is not None or provider_id is not None or model_id is not None
    if args.provider_mode == "fixture":
        if provider_input is None:
            raise ValueError("fixture mode requires provider input")
        if qualification is not None or qualification_registry is not None or pair_mode:
            raise ValueError("fixture mode does not accept qualification or registry-pair sources")
        return False
    if args.benchmark is None:
        raise ValueError("openai-compatible mode requires --benchmark")
    if pair_mode:
        if provider_input is not None or qualification is not None:
            raise ValueError("registry-pair mode is mutually exclusive with direct provider/qualification sources")
        if provider_registry is None or qualification_registry is None or not provider_id or not model_id:
            raise ValueError("registry-pair mode requires --provider-registry, --qualification-registry, --provider-id, and --model-id")
        return True
    if provider_input is None:
        raise ValueError("provider input is required outside registry-pair mode")
    if (qualification is None) == (qualification_registry is None):
        raise ValueError("openai-compatible mode requires exactly one of --qualification or --qualification-registry")
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the complete model-to-capability pipeline with explicit provider mode and review admission.")
    parser.add_argument("source", help="Source text file or '-' for stdin")
    parser.add_argument("provider_input", nargs="?", help="Fixture provider JSON or provider-config JSON file")
    parser.add_argument("--provider-mode", choices=PROVIDER_MODES, default="fixture")
    qualification_group = parser.add_mutually_exclusive_group()
    qualification_group.add_argument("--qualification", type=Path)
    qualification_group.add_argument("--qualification-registry", type=Path)
    parser.add_argument("--provider-registry", type=Path)
    parser.add_argument("--provider-id")
    parser.add_argument("--model-id")
    parser.add_argument("--benchmark", type=Path)
    parser.add_argument("--review", help="Explicit capability-intent-review-v1 JSON file")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    try:
        pair_mode = validate_cli_args(args)
        source_text = read_text(args.source)
        review = read_json(args.review, "review") if args.review else None
        benchmark = load_benchmark_json(args.benchmark) if args.benchmark else None
        provider_input = read_json(args.provider_input, "provider input") if args.provider_input else None
        qualification = read_json(str(args.qualification), "qualification") if args.qualification else None
        result = run(
            source_text,
            provider_input,
            review,
            args.index,
            provider_mode=args.provider_mode,
            qualification=qualification,
            qualification_registry=args.qualification_registry,
            provider_registry=args.provider_registry if pair_mode else None,
            provider_id=args.provider_id if pair_mode else None,
            model_id=args.model_id if pair_mode else None,
            benchmark=benchmark,
        )
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(canonical_json(result))
    return 0 if result["status"] == "resolved" else 1


if __name__ == "__main__":
    raise SystemExit(main())
