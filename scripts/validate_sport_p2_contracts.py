#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

COMMON = {"schema_version", "athlete_id", "generated_at", "source_refs", "uncertainties", "safety_flags"}
REQUIRED = {
    "performance-psychology-plan": COMMON | {"plan_version", "performance_question", "target_behavior", "skills", "practice_blocks", "cues", "transfer_situations", "monitoring", "re_evaluation"},
    "mental-health-routing": COMMON | {"routing_version", "concern_summary", "observed_signals", "functioning_course", "routing_level", "training_boundaries", "support_path", "privacy_minimization", "confidence"},
    "training-music-profile": COMMON | {"profile_version", "preferences", "exclusions", "session_goals", "activation_target", "timing", "selection_rules", "safety_constraints", "feedback_fields"},
    "environment-adjustment": COMMON | {"adjustment_version", "exposures", "environment_travel_data", "target_event", "acclimation_strategy", "circadian_strategy", "microcycle_adjustments", "hydration_cooling_context", "monitoring", "next_re_evaluation"},
}
ROUTING_LEVELS = {"performance_support", "monitor", "professional_review", "urgent"}
EXPOSURES = {"heat", "cold", "altitude_hypoxia", "travel_fatigue", "jet_lag"}
FORBIDDEN_DIRECT_MUTATION_FIELDS = {"revised_plan", "plan_patch", "automatic_plan_change"}


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

    forbidden = sorted(FORBIDDEN_DIRECT_MUTATION_FIELDS & set(data))
    if forbidden:
        errors.append("P2 artifacts must not directly mutate training plans: " + ", ".join(forbidden))

    if kind == "performance-psychology-plan":
        for forbidden_field in ("diagnosis", "psychotherapy_plan", "medication_advice"):
            if forbidden_field in data:
                errors.append(f"performance psychology must not contain {forbidden_field}")

    if kind == "mental-health-routing":
        level = data.get("routing_level")
        if level not in ROUTING_LEVELS:
            errors.append("invalid routing_level")
        if level == "urgent":
            boundaries = data.get("training_boundaries")
            support = data.get("support_path")
            if not isinstance(boundaries, dict) or boundaries.get("performance_optimization_paused") is not True:
                errors.append("urgent routing requires training_boundaries.performance_optimization_paused=true")
            if not isinstance(support, dict) or support.get("immediate") is not True:
                errors.append("urgent routing requires support_path.immediate=true")
        for forbidden_field in ("diagnosis", "psychotherapy", "medication_plan"):
            if forbidden_field in data:
                errors.append(f"mental-health routing must not contain {forbidden_field}")

    if kind == "training-music-profile":
        bpm = data.get("bpm_context")
        if bpm is not None:
            if not isinstance(bpm, dict) or bpm.get("descriptive_only") is not True:
                errors.append("bpm_context must be descriptive_only=true")
        for forbidden_field in ("mandatory_bpm_zone", "physiological_zone_from_bpm"):
            if forbidden_field in data:
                errors.append(f"training music must not contain {forbidden_field}")

    if kind == "environment-adjustment":
        exposures = data.get("exposures")
        if not isinstance(exposures, list) or not exposures:
            errors.append("exposures must be a non-empty list")
        elif any(value not in EXPOSURES for value in exposures):
            errors.append("invalid exposure")
        if isinstance(exposures, list) and "jet_lag" in exposures:
            circadian = data.get("circadian_strategy")
            if not isinstance(circadian, dict) or not circadian:
                errors.append("jet_lag exposure requires circadian_strategy")
        for forbidden_field in ("medical_clearance", "sleep_medication_plan"):
            if forbidden_field in data:
                errors.append(f"environment adjustment must not contain {forbidden_field}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Sport Athlete Management P2 v1 payload.")
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
