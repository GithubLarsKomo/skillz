#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_CASES = ("happy-path", "edge-case", "failure-case")
BASELINE_INIT_COMMAND = "python scripts/evaluate_skills.py --init-missing-baselines"
LEGACY_RUBRIC = {
    "schemaVersion": 1,
    "dimensions": [
        {"id": "required-behaviors", "weight": 0.5, "description": "All required behaviors pass."},
        {"id": "forbidden-behaviors", "weight": 0.3, "description": "No forbidden behavior is observed."},
        {"id": "evidence", "weight": 0.2, "description": "Every assessment has evidence."},
    ],
    "threshold": 1.0,
    "blockingCriteria": ["required-behavior-failed", "forbidden-behavior-observed", "missing-evidence"],
}


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: invalid JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: root must be an object")
    return value


def validate_rubric(path: Path, data: dict) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != 1:
        errors.append(f"{path.relative_to(ROOT)}: unsupported schemaVersion {data.get('schemaVersion')!r}")
    dimensions = data.get("dimensions")
    if not isinstance(dimensions, list) or not dimensions:
        errors.append(f"{path.relative_to(ROOT)}: dimensions must be a non-empty list")
    else:
        ids: set[str] = set()
        for i, item in enumerate(dimensions):
            if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not item["id"]:
                errors.append(f"{path.relative_to(ROOT)}: dimensions[{i}].id must be non-empty")
                continue
            if item["id"] in ids:
                errors.append(f"{path.relative_to(ROOT)}: duplicate dimension id {item['id']!r}")
            ids.add(item["id"])
            weight = item.get("weight")
            if not isinstance(weight, (int, float)) or weight <= 0:
                errors.append(f"{path.relative_to(ROOT)}: dimensions[{i}].weight must be > 0")
    threshold = data.get("threshold")
    if not isinstance(threshold, (int, float)) or not 0 <= threshold <= 1:
        errors.append(f"{path.relative_to(ROOT)}: threshold must be between 0 and 1")
    blocking = data.get("blockingCriteria")
    allowed = {"required-behavior-failed", "forbidden-behavior-observed", "missing-evidence"}
    if not isinstance(blocking, list) or any(item not in allowed for item in blocking):
        errors.append(f"{path.relative_to(ROOT)}: blockingCriteria contains unsupported values")
    return errors


def build_draft_baseline(slug: str, case: dict) -> dict:
    case_id = case["id"]
    return {
        "schemaVersion": 1,
        "skill": slug,
        "caseId": case_id,
        "recordedAt": date.today().isoformat(),
        "evaluator": "baseline-generator",
        "requiredBehaviors": [
            {
                "behavior": behavior,
                "passed": False,
                "evidence": "TODO: verify this required behavior against the skill and record concrete evidence.",
            }
            for behavior in case["requiredBehaviors"]
        ],
        "forbiddenBehaviors": [
            {
                "behavior": behavior,
                "observed": True,
                "evidence": "TODO: verify this forbidden behavior is absent and record concrete evidence.",
            }
            for behavior in case["forbiddenBehaviors"]
        ],
        "overall": "draft",
    }


def init_missing_baselines(root: Path) -> tuple[list[Path], list[str]]:
    global ROOT
    ROOT = root
    created: list[Path] = []
    errors: list[str] = []
    fixtures = sorted((root / "skills").glob("*/tests/evaluation.json"))
    if not fixtures:
        return created, ["no executable evaluation suites found"]

    for fixture_file in fixtures:
        try:
            fixture = load_json(fixture_file)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        slug = fixture_file.parents[1].name
        cases = fixture.get("cases")
        if not isinstance(cases, list):
            errors.append(f"{fixture_file.relative_to(root)}: cases must be a list")
            continue
        results_dir = fixture_file.parent / "results"
        results_dir.mkdir(parents=True, exist_ok=True)
        for index, case in enumerate(cases):
            if not isinstance(case, dict):
                errors.append(f"{fixture_file.relative_to(root)}: cases[{index}] must be an object")
                continue
            case_id = case.get("id")
            required = case.get("requiredBehaviors")
            forbidden = case.get("forbiddenBehaviors")
            if not isinstance(case_id, str) or not case_id:
                errors.append(f"{fixture_file.relative_to(root)}: cases[{index}].id must be non-empty")
                continue
            if not isinstance(required, list) or not required or not all(isinstance(v, str) and v.strip() for v in required):
                errors.append(f"{fixture_file.relative_to(root)}:{case_id}: requiredBehaviors must be a non-empty string list")
                continue
            if not isinstance(forbidden, list) or not forbidden or not all(isinstance(v, str) and v.strip() for v in forbidden):
                errors.append(f"{fixture_file.relative_to(root)}:{case_id}: forbiddenBehaviors must be a non-empty string list")
                continue
            result_file = results_dir / f"{case_id}.json"
            if result_file.exists():
                continue
            result_file.write_text(
                json.dumps(build_draft_baseline(slug, case), ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            created.append(result_file)
    return created, errors


def evaluate_suite(fixture_file: Path) -> tuple[dict, list[str]]:
    errors: list[str] = []
    skill_dir = fixture_file.parents[1]
    slug = skill_dir.name
    fixture = load_json(fixture_file)
    if fixture.get("skill") != slug:
        errors.append(f"{fixture_file.relative_to(ROOT)}: skill must equal '{slug}'")
    if fixture.get("schemaVersion", 1) != 1:
        errors.append(f"{fixture_file.relative_to(ROOT)}: unsupported schemaVersion {fixture.get('schemaVersion')!r}")

    cases = fixture.get("cases")
    if not isinstance(cases, list):
        return {"skill": slug}, errors + [f"{fixture_file.relative_to(ROOT)}: cases must be a list"]
    case_map: dict[str, dict] = {}
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"{fixture_file.relative_to(ROOT)}: cases[{index}] must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{fixture_file.relative_to(ROOT)}: cases[{index}].id must be non-empty")
            continue
        if case_id in case_map:
            errors.append(f"{fixture_file.relative_to(ROOT)}: duplicate case id '{case_id}'")
        case_map[case_id] = case
        for field in ("requiredBehaviors", "forbiddenBehaviors", "skillAnchors"):
            values = case.get(field)
            if not isinstance(values, list) or not values or not all(isinstance(v, str) and v.strip() for v in values):
                errors.append(f"{fixture_file.relative_to(ROOT)}:{case_id}: {field} must be a non-empty string list")
    missing_classes = set(REQUIRED_CASES) - set(case_map)
    if missing_classes:
        errors.append(f"{fixture_file.relative_to(ROOT)}: missing case classes: {', '.join(sorted(missing_classes))}")

    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8").lower()
    for case_id, case in case_map.items():
        prompt = case.get("input")
        if not isinstance(prompt, str) or len(prompt.strip()) < 20:
            errors.append(f"{fixture_file.relative_to(ROOT)}:{case_id}: input is missing or too short")
        for anchor in case.get("skillAnchors", []):
            if anchor.lower() not in skill_text:
                errors.append(f"{fixture_file.relative_to(ROOT)}:{case_id}: anchor not found in SKILL.md: {anchor!r}")

    rubric_file = fixture_file.with_name("rubric.json")
    compatibility = not rubric_file.exists()
    rubric = LEGACY_RUBRIC if compatibility else load_json(rubric_file)
    if not compatibility:
        errors.extend(validate_rubric(rubric_file, rubric))

    result_files = sorted((skill_dir / "tests" / "results").glob("*.json"))
    actual: dict[str, dict] = {}
    for result_file in result_files:
        result = load_json(result_file)
        case_id = result.get("caseId")
        if not isinstance(case_id, str):
            errors.append(f"{result_file.relative_to(ROOT)}: caseId must be a string")
            continue
        if case_id in actual:
            errors.append(f"{result_file.relative_to(ROOT)}: duplicate result for {slug}/{case_id}")
        actual[case_id] = result
        case = case_map.get(case_id)
        if not case:
            errors.append(f"{result_file.relative_to(ROOT)}: unknown caseId '{case_id}'")
            continue
        if result.get("skill") != slug:
            errors.append(f"{result_file.relative_to(ROOT)}: skill must equal '{slug}'")
        req = result.get("requiredBehaviors")
        forb = result.get("forbiddenBehaviors")
        if not isinstance(req, list) or not isinstance(forb, list):
            errors.append(f"{result_file.relative_to(ROOT)}: behavior assessments must be lists")
            continue
        req_map = {i.get("behavior"): i for i in req if isinstance(i, dict)}
        forb_map = {i.get("behavior"): i for i in forb if isinstance(i, dict)}
        expected_req = set(case.get("requiredBehaviors", []))
        expected_forb = set(case.get("forbiddenBehaviors", []))
        if set(req_map) != expected_req:
            errors.append(f"{result_file.relative_to(ROOT)}: required behavior assessments do not exactly match fixture")
        if set(forb_map) != expected_forb:
            errors.append(f"{result_file.relative_to(ROOT)}: forbidden behavior assessments do not exactly match fixture")
        for behavior in expected_req:
            item = req_map.get(behavior, {})
            if item.get("passed") is not True:
                errors.append(f"{result_file.relative_to(ROOT)}: required behavior did not pass: {behavior}")
            if not isinstance(item.get("evidence"), str) or not item.get("evidence", "").strip():
                errors.append(f"{result_file.relative_to(ROOT)}: required behavior lacks evidence: {behavior}")
        for behavior in expected_forb:
            item = forb_map.get(behavior, {})
            if item.get("observed") is not False:
                errors.append(f"{result_file.relative_to(ROOT)}: forbidden behavior was observed: {behavior}")
            if not isinstance(item.get("evidence"), str) or not item.get("evidence", "").strip():
                errors.append(f"{result_file.relative_to(ROOT)}: forbidden behavior lacks evidence: {behavior}")
        if result.get("overall") != "pass":
            errors.append(f"{result_file.relative_to(ROOT)}: overall must be 'pass' for committed baselines")
    for case_id in sorted(set(case_map) - set(actual)):
        expected_path = skill_dir / "tests" / "results" / f"{case_id}.json"
        errors.append(
            f"missing recorded result: {slug}/{case_id}; expected {expected_path.relative_to(ROOT)}; "
            f"create a draft with: {BASELINE_INIT_COMMAND}"
        )

    return {
        "skill": slug,
        "compatibilityMode": compatibility,
        "rubric": rubric,
        "cases": sorted(case_map),
        "recordedResults": sorted(actual),
        "passed": not errors,
    }, errors


def run(root: Path) -> tuple[dict, list[str]]:
    global ROOT
    ROOT = root
    errors: list[str] = []
    suites: list[dict] = []
    for fixture in sorted((root / "skills").glob("*/tests/evaluation.json")):
        try:
            suite, suite_errors = evaluate_suite(fixture)
            suites.append(suite)
            errors.extend(suite_errors)
        except ValueError as exc:
            errors.append(str(exc))
    if not suites:
        errors.append("no executable evaluation suites found")
    return {"schemaVersion": 1, "suiteCount": len(suites), "suites": suites, "passed": not errors}, errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and score all skill evaluation suites.")
    parser.add_argument("--json", action="store_true", help="Emit stable machine-readable JSON.")
    parser.add_argument(
        "--init-missing-baselines",
        action="store_true",
        help="Create safe draft result files for evaluation cases that do not yet have a recorded baseline.",
    )
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()
    root = args.root.resolve()

    if args.init_missing_baselines:
        created, init_errors = init_missing_baselines(root)
        if args.json:
            print(json.dumps({
                "schemaVersion": 1,
                "created": [str(path.relative_to(root)) for path in created],
                "errors": init_errors,
            }, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
        else:
            for path in created:
                print(f"CREATED {path.relative_to(root)}")
            if created:
                print("Draft baselines were created. Replace TODO evidence, verify each assessment, then set overall to 'pass'.")
            else:
                print("No missing evaluation baselines found.")
            if init_errors:
                print("Baseline initialization failed:", file=sys.stderr)
                for error in init_errors:
                    print(f"- {error}", file=sys.stderr)
        return 1 if init_errors else 0

    summary, errors = run(root)
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    else:
        for suite in summary["suites"]:
            mode = "compatibility" if suite["compatibilityMode"] else "rubric"
            print(f"{'PASS' if suite['passed'] else 'FAIL'} {suite['skill']} ({mode}, {len(suite['cases'])} cases)")
        print(f"Summary: {summary['suiteCount']} suites, {'PASS' if summary['passed'] else 'FAIL'}")
    if errors:
        print("Evaluation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
