#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    scored = 0

    for result_file in sorted((ROOT / "skills").glob("*/tests/results/*.json")):
        scored += 1
        skill_dir = result_file.parents[2]
        fixture_file = skill_dir / "tests" / "evaluation.json"
        try:
            result = json.loads(result_file.read_text(encoding="utf-8"))
            fixture = json.loads(fixture_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(f"{result_file.relative_to(ROOT)}: cannot load evaluation data: {exc}", errors)
            continue

        slug = skill_dir.name
        case_id = result.get("caseId")
        if result.get("skill") != slug:
            fail(f"{result_file.relative_to(ROOT)}: skill must equal '{slug}'", errors)

        cases = {case.get("id"): case for case in fixture.get("cases", []) if isinstance(case, dict)}
        case = cases.get(case_id)
        if not case:
            fail(f"{result_file.relative_to(ROOT)}: unknown caseId '{case_id}'", errors)
            continue

        required = result.get("requiredBehaviors")
        forbidden = result.get("forbiddenBehaviors")
        if not isinstance(required, list) or not isinstance(forbidden, list):
            fail(f"{result_file.relative_to(ROOT)}: behavior assessments must be lists", errors)
            continue

        required_map = {item.get("behavior"): item for item in required if isinstance(item, dict)}
        forbidden_map = {item.get("behavior"): item for item in forbidden if isinstance(item, dict)}

        for behavior in case.get("requiredBehaviors", []):
            item = required_map.get(behavior)
            if not item:
                fail(f"{result_file.relative_to(ROOT)}: missing required assessment: {behavior}", errors)
                continue
            if item.get("passed") is not True:
                fail(f"{result_file.relative_to(ROOT)}: required behavior did not pass: {behavior}", errors)
            if not isinstance(item.get("evidence"), str) or not item["evidence"].strip():
                fail(f"{result_file.relative_to(ROOT)}: required behavior lacks evidence: {behavior}", errors)

        for behavior in case.get("forbiddenBehaviors", []):
            item = forbidden_map.get(behavior)
            if not item:
                fail(f"{result_file.relative_to(ROOT)}: missing forbidden assessment: {behavior}", errors)
                continue
            if item.get("observed") is not False:
                fail(f"{result_file.relative_to(ROOT)}: forbidden behavior was observed: {behavior}", errors)
            if not isinstance(item.get("evidence"), str) or not item["evidence"].strip():
                fail(f"{result_file.relative_to(ROOT)}: forbidden behavior lacks evidence: {behavior}", errors)

        if result.get("overall") != "pass":
            fail(f"{result_file.relative_to(ROOT)}: overall must be 'pass' for committed baselines", errors)

    if scored == 0:
        errors.append("no recorded evaluation results found")

    if errors:
        print("Recorded evaluation scoring failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"OK: {scored} recorded evaluation results scored")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
