#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from adapt_model_interpretation import adapt
from compile_capability_intent import normalize_intent
from normalize_capability_intent_envelope import CONFIDENCE_LEVELS

SCHEMA_VERSION = 1
LIST_FIELDS = ("desiredOutputs", "requiredDependencies", "allowedEvaluationModes")


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return value


def string_list(value: object, label: str) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{label} must be an array of strings")
    return sorted(set(value))


def validate_benchmark(data: dict) -> list[dict]:
    if set(data) != {"schemaVersion", "cases"}:
        raise ValueError("benchmark must contain only schemaVersion and cases")
    if data.get("schemaVersion") != SCHEMA_VERSION:
        raise ValueError(f"unsupported benchmark schemaVersion {data.get('schemaVersion')!r}; expected {SCHEMA_VERSION}")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("benchmark cases must be a non-empty array")
    seen: set[str] = set()
    normalized: list[dict] = []
    required_fields = {
        "id", "sourceText", "expectedIntent", "forbiddenConstraints",
        "allowedConfidenceLevels", "requiredReviewReasons", "forbiddenReviewReasons",
    }
    for index, case in enumerate(cases):
        if not isinstance(case, dict) or set(case) != required_fields:
            raise ValueError(f"cases[{index}] has invalid fields")
        case_id = case["id"]
        if not isinstance(case_id, str) or not case_id:
            raise ValueError(f"cases[{index}].id must be a non-empty string")
        if case_id in seen:
            raise ValueError(f"duplicate benchmark case id: {case_id}")
        seen.add(case_id)
        if not isinstance(case["sourceText"], str) or not case["sourceText"].strip():
            raise ValueError(f"{case_id}: sourceText must be non-empty")
        expected = normalize_intent(case["expectedIntent"])
        forbidden = case["forbiddenConstraints"]
        if not isinstance(forbidden, dict) or set(forbidden) != set(LIST_FIELDS):
            raise ValueError(f"{case_id}: forbiddenConstraints must contain exactly {', '.join(LIST_FIELDS)}")
        forbidden = {field: string_list(forbidden[field], f"{case_id}.forbiddenConstraints.{field}") for field in LIST_FIELDS}
        confidence = string_list(case["allowedConfidenceLevels"], f"{case_id}.allowedConfidenceLevels")
        if not confidence or any(level not in CONFIDENCE_LEVELS for level in confidence):
            raise ValueError(f"{case_id}: allowedConfidenceLevels contains unsupported values")
        normalized.append({
            "id": case_id,
            "sourceText": case["sourceText"],
            "expectedIntent": expected,
            "forbiddenConstraints": forbidden,
            "allowedConfidenceLevels": confidence,
            "requiredReviewReasons": string_list(case["requiredReviewReasons"], f"{case_id}.requiredReviewReasons"),
            "forbiddenReviewReasons": string_list(case["forbiddenReviewReasons"], f"{case_id}.forbiddenReviewReasons"),
        })
    return sorted(normalized, key=lambda item: item["id"])


def validate_proposal_set(data: dict) -> dict[str, dict]:
    if set(data) != {"schemaVersion", "proposals"}:
        raise ValueError("proposal set must contain only schemaVersion and proposals")
    if data.get("schemaVersion") != SCHEMA_VERSION:
        raise ValueError(f"unsupported proposal-set schemaVersion {data.get('schemaVersion')!r}; expected {SCHEMA_VERSION}")
    proposals = data.get("proposals")
    if not isinstance(proposals, list):
        raise ValueError("proposal set proposals must be an array")
    result: dict[str, dict] = {}
    for index, item in enumerate(proposals):
        if not isinstance(item, dict) or set(item) != {"caseId", "proposal"}:
            raise ValueError(f"proposals[{index}] must contain exactly caseId and proposal")
        case_id = item["caseId"]
        if not isinstance(case_id, str) or not case_id:
            raise ValueError(f"proposals[{index}].caseId must be non-empty")
        if case_id in result:
            raise ValueError(f"duplicate proposal caseId: {case_id}")
        if not isinstance(item["proposal"], dict):
            raise ValueError(f"{case_id}: proposal must be an object")
        result[case_id] = item["proposal"]
    return result


def score_case(case: dict, proposal: dict | None) -> dict:
    finding = {
        "caseId": case["id"],
        "adapterCompatible": False,
        "validationError": None,
        "missingRequiredConstraints": {field: [] for field in LIST_FIELDS},
        "inventedConstraints": {field: [] for field in LIST_FIELDS},
        "forbiddenConstraintsObserved": {field: [] for field in LIST_FIELDS},
        "portableFilesMismatch": False,
        "confidenceAccepted": False,
        "missingReviewReasons": [],
        "forbiddenReviewReasonsObserved": [],
        "passed": False,
    }
    if proposal is None:
        finding["validationError"] = "missing proposal"
        return finding
    try:
        envelope = adapt(proposal)
    except ValueError as exc:
        finding["validationError"] = str(exc)
        return finding

    finding["adapterCompatible"] = True
    actual = envelope["intent"]
    expected = case["expectedIntent"]
    for field in LIST_FIELDS:
        actual_values = set(actual[field])
        expected_values = set(expected[field])
        forbidden_values = set(case["forbiddenConstraints"][field])
        finding["missingRequiredConstraints"][field] = sorted(expected_values - actual_values)
        finding["inventedConstraints"][field] = sorted(actual_values - expected_values)
        finding["forbiddenConstraintsObserved"][field] = sorted(actual_values & forbidden_values)
    finding["portableFilesMismatch"] = actual["portableFiles"] != expected["portableFiles"]
    finding["confidenceAccepted"] = proposal["confidence"] in case["allowedConfidenceLevels"]
    reasons = set(proposal["reviewReasons"])
    finding["missingReviewReasons"] = sorted(set(case["requiredReviewReasons"]) - reasons)
    finding["forbiddenReviewReasonsObserved"] = sorted(reasons & set(case["forbiddenReviewReasons"]))

    finding["passed"] = (
        finding["adapterCompatible"]
        and all(not values for values in finding["missingRequiredConstraints"].values())
        and all(not values for values in finding["inventedConstraints"].values())
        and all(not values for values in finding["forbiddenConstraintsObserved"].values())
        and not finding["portableFilesMismatch"]
        and finding["confidenceAccepted"]
        and not finding["missingReviewReasons"]
        and not finding["forbiddenReviewReasonsObserved"]
    )
    return finding


def score(benchmark: dict, proposal_set: dict) -> dict:
    cases = validate_benchmark(benchmark)
    proposals = validate_proposal_set(proposal_set)
    known_ids = {case["id"] for case in cases}
    unknown_ids = sorted(set(proposals) - known_ids)
    if unknown_ids:
        raise ValueError(f"proposal set contains unknown caseId(s): {', '.join(unknown_ids)}")
    findings = [score_case(case, proposals.get(case["id"])) for case in cases]
    passed_count = sum(1 for item in findings if item["passed"])
    return {
        "schemaVersion": SCHEMA_VERSION,
        "caseCount": len(findings),
        "passedCount": passed_count,
        "failedCount": len(findings) - passed_count,
        "passed": passed_count == len(findings),
        "cases": findings,
    }


def render_json(payload: dict) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Score structured capability interpretation proposals against an offline gold benchmark.")
    parser.add_argument("benchmark", type=Path)
    parser.add_argument("proposals", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        summary = score(load_json(args.benchmark), load_json(args.proposals))
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(render_json(summary))
    else:
        for case in summary["cases"]:
            print(f"{'PASS' if case['passed'] else 'FAIL'} {case['caseId']}")
        print(f"Summary: {summary['passedCount']}/{summary['caseCount']} passed")
    return 0 if summary["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
