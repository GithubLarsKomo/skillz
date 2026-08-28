from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_capability_index import build_index  # noqa: E402


class CompleteEvaluationCoverageTests(unittest.TestCase):
    def test_every_skill_has_an_evaluation_suite(self) -> None:
        index = build_index(ROOT)
        missing = {
            skill["name"]
            for skill in index["skills"]
            if skill["evaluation"]["mode"] == "none"
        }
        self.assertEqual(missing, set())
        self.assertTrue(index["evaluationCoverageComplete"])
        self.assertEqual(index["evaluatedSkillCount"], index["skillCount"])

    def test_every_user_facing_skill_remains_evaluated(self) -> None:
        index = build_index(ROOT)
        missing = {
            skill["name"]
            for skill in index["skills"]
            if skill["invocation"]["userFacing"] and skill["evaluation"]["mode"] == "none"
        }
        self.assertEqual(missing, set())

    def test_ambiguous_output_count_remains_zero(self) -> None:
        index = build_index(ROOT)
        ambiguous = {
            contract["output"]
            for skill in index["skills"]
            for contract in skill["outputContracts"]
            if contract["ambiguous"]
        }
        self.assertEqual(ambiguous, set())


if __name__ == "__main__":
    unittest.main()
