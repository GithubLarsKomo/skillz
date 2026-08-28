from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_capability_index import build_index  # noqa: E402


PREVIOUSLY_MISSING_USER_FACING = {
    "euroimmun-presentation-workflow",
    "learning-document-delivery",
    "learning-image-generator",
    "learning-landingpage-renderer",
    "learning-summary-synthesis",
    "learning-svg-generator",
    "presentation-language-rewriter",
    "presentation-layout-qa",
    "presentation-render-verifier",
    "presentation-template-profiler",
    "procedure-sop-extractor",
    "template-presentation-workflow",
    "youtube-course-builder-workflow",
    "youtube-learning-workflow",
    "youtube-playlist-learning-workflow",
}


class UserFacingEvaluationCoverageTests(unittest.TestCase):
    def test_previously_missing_user_facing_skills_have_suites(self) -> None:
        index = build_index(ROOT)
        by_name = {skill["name"]: skill for skill in index["skills"]}
        missing = {
            name
            for name in PREVIOUSLY_MISSING_USER_FACING
            if by_name[name]["evaluation"]["mode"] == "none"
        }
        self.assertEqual(missing, set())

    def test_no_user_facing_skill_is_unevaluated(self) -> None:
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
