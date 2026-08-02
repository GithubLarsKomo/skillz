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

SCHEMA_VERSION = 1
DEFAULT_INDEX = Path(__file__).resolve().parents[1] / "docs" / "skill-capability-index.json"


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
        request.get("outputs", []),
        request.get("dependencies", []),
        request.get("evaluationModes", []),
        request.get("portableFiles", "irrelevant"),
    )
    return resolver.resolve(resolver.load_index(index_path), constraints)


def run(source_text: str, fixture: dict, review: dict | None, index_path: Path = DEFAULT_INDEX) -> dict:
    try:
        index = request_builder.load_index(index_path)
        interpretation_request = request_builder.build_request(source_text, index)
    except ValueError as exc:
        return failed("request", str(exc))

    request_id = interpretation_request["requestId"]
    model_run = model_runner.run(interpretation_request, fixture)
    if model_run["status"] != "accepted" or model_run["proposal"] is None:
        return failed("model-run", model_run.get("validationError") or "model run rejected", request_id, model_run)

    try:
        envelope = model_adapter.adapt(model_run["proposal"])
        normalized_review = admission.normalize_review(review) if review is not None else None
        intent = admission.admit(envelope, normalized_review)
        admission_result = {
            "status": "approved",
            "reviewProvided": normalized_review is not None,
            "intent": intent,
        }
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the complete offline model-to-capability pipeline with explicit review admission.")
    parser.add_argument("source", help="Source text file or '-' for stdin")
    parser.add_argument("fixture", help="Fixture provider JSON file")
    parser.add_argument("--review", help="Explicit capability-intent-review-v1 JSON file")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    try:
        source_text = read_text(args.source)
        fixture = read_json(args.fixture, "fixture provider")
        review = read_json(args.review, "review") if args.review else None
        result = run(source_text, fixture, review, args.index)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(canonical_json(result))
    return 0 if result["status"] == "resolved" else 1


if __name__ == "__main__":
    raise SystemExit(main())
