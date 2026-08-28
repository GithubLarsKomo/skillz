from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from evaluate_skills import run as evaluate_all  # noqa: E402
from generate_capability_index import build_index  # noqa: E402


PRESENTATION_SKILLS = {
    "presentation-template-profiler",
    "presentation-language-rewriter",
    "presentation-layout-qa",
    "presentation-render-verifier",
    "template-presentation-workflow",
    "euroimmun-presentation-workflow",
}


class ArchitectureConsolidationP1PresentationEvaluationTests(unittest.TestCase):
    def test_presentation_stack_has_recorded_passing_evaluations(self) -> None:
        summary, errors = evaluate_all(ROOT)
        presentation_errors = [
            error for error in errors if any(f"skills/{name}/" in error for name in PRESENTATION_SKILLS)
        ]
        self.assertEqual(presentation_errors, [], "\n".join(presentation_errors))

        index = build_index(ROOT)
        by_name = {item["name"]: item for item in index["skills"]}
        for name in PRESENTATION_SKILLS:
            evaluation = by_name[name]["evaluation"]
            self.assertNotEqual(evaluation["mode"], "none", name)
            self.assertEqual(evaluation["caseCount"], 3, name)
            self.assertEqual(evaluation["recordedResultCount"], 3, name)
            self.assertTrue(evaluation["passed"], name)

        self.assertGreaterEqual(summary["suiteCount"], len(PRESENTATION_SKILLS))


if __name__ == "__main__":
    unittest.main()
