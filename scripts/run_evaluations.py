#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_CASES = {"happy-path", "edge-case", "failure-case"}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: invalid JSON: {exc}") from exc


def main() -> int:
    errors: list[str] = []
    evaluated = 0

    for fixture in sorted((ROOT / "skills").glob("*/tests/evaluation.json")):
        evaluated += 1
        skill_dir = fixture.parents[1]
        skill_file = skill_dir / "SKILL.md"
        try:
            data = load_json(fixture)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        slug = skill_dir.name
        if data.get("skill") != slug:
            errors.append(f"{fixture.relative_to(ROOT)}: skill must equal '{slug}'")

        cases = data.get("cases")
        if not isinstance(cases, list):
            errors.append(f"{fixture.relative_to(ROOT)}: cases must be a list")
            continue

        ids = {case.get("id") for case in cases if isinstance(case, dict)}
        missing = REQUIRED_CASES - ids
        extra = ids - REQUIRED_CASES
        if missing:
            errors.append(f"{fixture.relative_to(ROOT)}: missing cases: {', '.join(sorted(missing))}")
        if extra:
            errors.append(f"{fixture.relative_to(ROOT)}: unknown cases: {', '.join(sorted(str(x) for x in extra))}")

        skill_text = skill_file.read_text(encoding="utf-8").lower()
        for case in cases:
            if not isinstance(case, dict):
                errors.append(f"{fixture.relative_to(ROOT)}: every case must be an object")
                continue
            case_id = case.get("id", "<unknown>")
            prompt = case.get("input")
            required = case.get("requiredBehaviors")
            forbidden = case.get("forbiddenBehaviors")
            anchors = case.get("skillAnchors")

            if not isinstance(prompt, str) or len(prompt.strip()) < 20:
                errors.append(f"{fixture.relative_to(ROOT)}:{case_id}: input is missing or too short")
            for field_name, values in (("requiredBehaviors", required), ("forbiddenBehaviors", forbidden), ("skillAnchors", anchors)):
                if not isinstance(values, list) or not values or not all(isinstance(v, str) and v.strip() for v in values):
                    errors.append(f"{fixture.relative_to(ROOT)}:{case_id}: {field_name} must be a non-empty string list")

            if isinstance(anchors, list):
                for anchor in anchors:
                    if isinstance(anchor, str) and anchor.lower() not in skill_text:
                        errors.append(f"{fixture.relative_to(ROOT)}:{case_id}: anchor not found in SKILL.md: {anchor!r}")

    if evaluated == 0:
        errors.append("no executable evaluation fixtures found")

    if errors:
        print("Evaluation validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"OK: {evaluated} executable skill evaluations validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
