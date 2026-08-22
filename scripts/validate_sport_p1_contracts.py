#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

COMMON = {"schema_version", "athlete_id", "generated_at", "source_refs", "uncertainties", "safety_flags"}
REQUIRED = {
    "strength-power-plan": COMMON | {"plan_version", "objective", "mesocycle_ref", "exercises", "progression", "stop_rules"},
    "endurance-plan": COMMON | {"plan_version", "objective", "reference_model", "sessions", "progression", "stop_rules"},
    "recovery-state": COMMON | {"window_start", "window_end", "baseline", "current_signals", "trend", "interventions", "next_re_evaluation"},
    "fueling-plan": COMMON | {"plan_version", "load_context", "session_fueling", "hydration", "protein_strategy", "re_evaluation"},
    "energy-availability-risk": COMMON | {"risk_state", "signals", "confidence", "routing"},
    "rehab-progression": COMMON | {"restriction_source", "current_phase", "entry_criteria", "exit_criteria", "load_components", "response_rules", "next_re_evaluation"},
    "return-after-illness-plan": COMMON | {"symptom_state", "current_stage", "stages", "progression_criteria", "regression_criteria", "medical_routing"},
    "testing-plan": COMMON | {"plan_version", "decision_questions", "tests", "timing", "standardization", "retest_plan"},
    "adaptation-analysis": COMMON | {"analysis_window", "data_coverage", "baseline_method", "trends", "interpretations", "alternative_explanations", "confidence", "next_measurements"},
}
PHASES = {"protection", "restore_load", "force_capacity", "power_elastic", "sport_specific", "return_participation", "return_sport", "return_performance"}
RISK_STATES = {"no_signal", "monitor", "review", "urgent_review", "unknown"}


def _number_in(value: object, low: float, high: float) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and low <= value <= high


def validate(kind: str, data: dict) -> list[str]:
    if kind not in REQUIRED:
        return [f"unsupported kind: {kind}"]
    errors: list[str] = []
    missing = sorted(REQUIRED[kind] - set(data))
    if missing:
        errors.append("missing fields: " + ", ".join(missing))
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if not isinstance(data.get("athlete_id"), str) or not data.get("athlete_id"):
        errors.append("athlete_id must be a non-empty string")
    for field in ("source_refs", "uncertainties", "safety_flags"):
        if field in data and not isinstance(data[field], list):
            errors.append(f"{field} must be a list")

    confidence = data.get("confidence")
    if confidence is not None and not _number_in(confidence, 0, 1):
        errors.append("confidence must be within 0..1")

    if kind == "recovery-state" and "readiness_score" in data:
        errors.append("recovery-state must not expose an opaque readiness_score")
    if kind == "energy-availability-risk":
        if data.get("risk_state") not in RISK_STATES:
            errors.append("invalid risk_state")
        if data.get("risk_state") in {"review", "urgent_review"} and not data.get("routing"):
            errors.append("review states require routing")
    if kind == "rehab-progression" and data.get("current_phase") not in PHASES:
        errors.append("invalid current_phase")
    if kind == "return-after-illness-plan":
        red_flags = data.get("red_flags", [])
        routing = data.get("medical_routing", {})
        if red_flags and not isinstance(routing, dict):
            errors.append("red flags require medical_routing object")
        if red_flags and routing.get("required") is not True:
            errors.append("red flags require medical_routing.required=true")
    if kind == "adaptation-analysis" and "acwr_injury_probability" in data:
        errors.append("adaptation-analysis must not encode ACWR as injury probability")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Sport Athlete Management P1 v1 payload.")
    parser.add_argument("kind", choices=sorted(REQUIRED))
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if not isinstance(data, dict):
        print("ERROR: payload root must be an object", file=sys.stderr)
        return 2
    errors = validate(args.kind, data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: {args.kind}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
