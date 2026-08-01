from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "evaluate_skills.py"
spec = importlib.util.spec_from_file_location("evaluate_skills", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


class EvaluateSkillsTests(unittest.TestCase):
    def make_repo(self, *, rubric=None, duplicate=False, missing_failure=False, threshold=None):
        tmp = tempfile.TemporaryDirectory()
        root = Path(tmp.name)
        skill = root / "skills" / "demo"
        results = skill / "tests" / "results"
        results.mkdir(parents=True)
        (skill / "SKILL.md").write_text("---\nname: demo\ndescription: A sufficiently long demo skill description for tests.\n---\n# Demo\nanchor one\nanchor two\nanchor three\n", encoding="utf-8")
        case_ids = ["happy-path", "edge-case"] if missing_failure else ["happy-path", "edge-case", "failure-case"]
        cases = []
        for case_id in case_ids:
            cases.append({
                "id": case_id,
                "input": f"This is a sufficiently long evaluation prompt for {case_id}.",
                "requiredBehaviors": [f"required {case_id}"],
                "forbiddenBehaviors": [f"forbidden {case_id}"],
                "skillAnchors": ["anchor one"],
            })
        if duplicate:
            cases.append(dict(cases[0]))
        (skill / "tests" / "evaluation.json").write_text(json.dumps({"schemaVersion": 1, "skill": "demo", "cases": cases}), encoding="utf-8")
        for case in cases[:len(case_ids)]:
            cid = case["id"]
            (results / f"{cid}.json").write_text(json.dumps({
                "skill": "demo",
                "caseId": cid,
                "requiredBehaviors": [{"behavior": f"required {cid}", "passed": True, "evidence": "verified"}],
                "forbiddenBehaviors": [{"behavior": f"forbidden {cid}", "observed": False, "evidence": "verified"}],
                "overall": "pass",
            }), encoding="utf-8")
        if rubric is not None:
            value = dict(rubric)
            if threshold is not None:
                value["threshold"] = threshold
            (skill / "tests" / "rubric.json").write_text(json.dumps(value), encoding="utf-8")
        return tmp, root

    def test_legacy_suite_uses_compatibility_mode(self):
        tmp, root = self.make_repo()
        self.addCleanup(tmp.cleanup)
        summary, errors = module.run(root)
        self.assertFalse(errors)
        self.assertTrue(summary["passed"])
        self.assertTrue(summary["suites"][0]["compatibilityMode"])

    def test_explicit_rubric_is_supported(self):
        rubric = {"schemaVersion": 1, "dimensions": [{"id": "evidence", "weight": 1.0}], "threshold": 1.0, "blockingCriteria": ["missing-evidence"]}
        tmp, root = self.make_repo(rubric=rubric)
        self.addCleanup(tmp.cleanup)
        summary, errors = module.run(root)
        self.assertFalse(errors)
        self.assertFalse(summary["suites"][0]["compatibilityMode"])

    def test_duplicate_case_id_fails(self):
        tmp, root = self.make_repo(duplicate=True)
        self.addCleanup(tmp.cleanup)
        _, errors = module.run(root)
        self.assertTrue(any("duplicate case id" in error for error in errors))

    def test_invalid_threshold_fails(self):
        rubric = {"schemaVersion": 1, "dimensions": [{"id": "evidence", "weight": 1.0}], "threshold": 1.0, "blockingCriteria": []}
        tmp, root = self.make_repo(rubric=rubric, threshold=1.2)
        self.addCleanup(tmp.cleanup)
        _, errors = module.run(root)
        self.assertTrue(any("threshold" in error for error in errors))

    def test_missing_failure_case_fails(self):
        tmp, root = self.make_repo(missing_failure=True)
        self.addCleanup(tmp.cleanup)
        _, errors = module.run(root)
        self.assertTrue(any("missing case classes" in error for error in errors))

    def test_output_order_is_deterministic(self):
        tmp, root = self.make_repo()
        self.addCleanup(tmp.cleanup)
        first, first_errors = module.run(root)
        second, second_errors = module.run(root)
        self.assertEqual(first_errors, second_errors)
        self.assertEqual(json.dumps(first, sort_keys=True), json.dumps(second, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
