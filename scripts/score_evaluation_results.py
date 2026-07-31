#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    scored = 0
    expected_results: set[tuple[str, str]] = set()
    actual_results: set[tuple[str, str]] = set()

    for fixture_file in sorted((ROOT / "skills").glob("*/tests/evaluation.json")):
        slug = fixture_file.parents[1].name
        try:
            fixture = load_json(fixture_file)
        except (OSError, json.JSONDecodeError) as exc:
            fail(f"{fixture_file.relative_to(ROOT)}: cannot load fixture: {exc}", errors)
            continue
        for case in fixture.get("cases", []):
            if isinstance(case, dict) and isinstance(case.get("id"), str):
                expected_results.add((slug, case["id"]))

    for result_file in sorted((ROOT / "skills").glob("*/tests/results/*.json")):
        scored += 1
        skill_dir = result_file.parents[2]
        fixture_file = skill_dir / "tests" / "evaluation.json"
        try:
            result = load_json(result_file)
            fixture = load_json(fixture_file)
        except (OSError, json.JSONDecodeError) as exc:
            fail(f"{result_file.relative_to(ROOT)}: cannot load evaluation data: {exc}", errors)
            continue

        slug = skill_dir.name
        case_id = result.get("caseId")
        if isinstance(case_id, str):
            key = (slug, case_id)
            if key in actual_results:
                fail(f"{result_file.relative_to(ROOT)}: duplicate result for {slug}/{case_id}", errors)
            actual_results.add(key)

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
        expected_required = set(case.get("requiredBehaviors", []))
        expected_forbidden = set(case.get("forbiddenBehaviors", []))

        if set(required_map) != expected_required:
            fail(f"{result_file.relative_to(ROOT)}: required behavior assessments do not exactly match fixture", errors)
        if set(forbidden_map) != expected_forbidden:
            fail(f"{result_file.relative_to(ROOT)}: forbidden behavior assessments do not exactly match fixture", errors)

        for behavior in expected_required:
            item = required_map.get(behavior)
            if not item:
                continue
            if item.get("passed") is not True:
                fail(f"{result_file.relative_to(ROOT)}: required behavior did not pass: {behavior}", errors)
            if not isinstance(item.get("evidence"), str) or not item["evidence"].strip():
                fail(f"{result_file.relative_to(ROOT)}: required behavior lacks evidence: {behavior}", errors)

        for behavior in expected_forbidden:
            item = forbidden_map.get(behavior)
            if not item:
                continue
            if item.get("observed") is not False:
                fail(f"{result_file.relative_to(ROOT)}: forbidden behavior was observed: {behavior}", errors)
            if not isinstance(item.get("evidence"), str) or not item["evidence"].strip():
                fail(f"{result_file.relative_to(ROOT)}: forbidden behavior lacks evidence: {behavior}", errors)

        if result.get("overall") != "pass":
            fail(f"{result_file.relative_to(ROOT)}: overall must be 'pass' for committed baselines", errors)

    missing = expected_results - actual_results
    extra = actual_results - expected_results
    for slug, case_id in sorted(missing):
        fail(f"missing recorded result: {slug}/{case_id}", errors)
    for slug, case_id in sorted(extra):
        fail(f"recorded result has no matching fixture: {slug}/{case_id}", errors)

    if not expected_results:
        errors.append("no executable evaluation cases found")

    if errors:
        print("Recorded evaluation scoring failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"OK: {scored} recorded evaluation results cover {len(expected_results)} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
