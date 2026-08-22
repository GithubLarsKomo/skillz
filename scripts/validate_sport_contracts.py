#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

COMMON = {"schema_version", "athlete_id", "generated_at", "source_refs", "uncertainties", "safety_flags"}
REQUIRED = {
    "athlete-profile": COMMON | {"profile_version", "valid_from", "sport", "discipline", "age_band", "training_age_years", "availability"},
    "performance-model": COMMON | {"model_version", "outcome_goals", "performance_goals", "process_goals", "limiters", "kpis"},
    "season-plan": COMMON | {"season_id", "version", "start_date", "end_date", "competitions", "macrocycles", "revision_points"},
    "mesocycle": COMMON | {"mesocycle_id", "season_id", "version", "start_date", "end_date", "primary_adaptation", "maintenance_qualities", "load_strategy", "entry_criteria", "exit_criteria"},
    "microcycle": COMMON | {"microcycle_id", "mesocycle_id", "version", "start_date", "end_date", "focus", "sessions"},
    "daily-checkin": COMMON | {"local_date", "sleep_quality_1_5", "fatigue_1_5", "soreness_1_5", "stress_1_5", "motivation_1_5"},
    "completed-session": COMMON | {"completed_session_id", "started_at", "completed_at", "duration_min", "session_rpe", "completion_status"},
    "adaptation-decision": COMMON | {"adaptation_decision_id", "decision_level", "action", "safety_state", "trigger", "input_snapshot", "rationale", "confidence", "human_override"},
    "athlete-management-state": COMMON | {"state_version", "profile_ref", "performance_model_ref", "season_ref", "mesocycle_ref", "microcycle_ref", "next_training_decision"},
}
ACTIONS = {"proceed", "reduce_volume", "reduce_intensity", "substitute", "move_session", "recovery", "progress", "delay_progression", "retest", "health_route", "medical_review", "review_required"}


def _number_in(value: object, low: float, high: float) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and low <= value <= high


def validate(kind: str, data: dict) -> list[str]:
    errors: list[str] = []
    if kind not in REQUIRED:
        return [f"unsupported kind: {kind}"]
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

    if kind == "daily-checkin":
        for field in ("sleep_quality_1_5", "fatigue_1_5", "soreness_1_5", "stress_1_5", "motivation_1_5"):
            value = data.get(field)
            if value is not None and not _number_in(value, 1, 5):
                errors.append(f"{field} must be null or within 1..5")
        pain = data.get("pain_0_10")
        if pain is not None and not _number_in(pain, 0, 10):
            errors.append("pain_0_10 must be null or within 0..10")

    if kind == "completed-session":
        duration = data.get("duration_min")
        rpe = data.get("session_rpe")
        if not _number_in(duration, 0, float("inf")):
            errors.append("duration_min must be >= 0")
        if not _number_in(rpe, 0, 10):
            errors.append("session_rpe must be within 0..10")
        if _number_in(duration, 0, float("inf")) and _number_in(rpe, 0, 10) and "session_load" in data:
            expected = float(duration) * float(rpe)
            if abs(float(data["session_load"]) - expected) > 1e-9:
                errors.append("session_load must equal duration_min * session_rpe")

    if kind == "adaptation-decision":
        if data.get("decision_level") not in {"acute", "tactical", "strategic"}:
            errors.append("invalid decision_level")
        if data.get("action") not in ACTIONS:
            errors.append("invalid action")
        if data.get("safety_state") not in {"GREEN", "YELLOW", "ORANGE", "RED"}:
            errors.append("invalid safety_state")
        if not _number_in(data.get("confidence"), 0, 1):
            errors.append("confidence must be within 0..1")
        if data.get("safety_state") == "RED" and data.get("action") not in {"health_route", "medical_review", "review_required"}:
            errors.append("RED decisions cannot continue normal training progression")
        if not isinstance(data.get("input_snapshot"), dict):
            errors.append("input_snapshot must be an object")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Sport Athlete Management v1 payload.")
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
