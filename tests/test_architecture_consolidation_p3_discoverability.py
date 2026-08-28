from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_repository_metadata import parse_frontmatter  # noqa: E402

INDEX = ROOT / "docs" / "skill-capability-index.json"

ADVANCED_CONTRACT_SKILLS = {
    "contract-matter-workflow",
    "agreement-type-analysis",
    "contract-review",
    "contract-drafting",
    "contract-legal-context",
    "legal-negotiation-strategy",
    "legal-redline-review-loop",
}


class ArchitectureConsolidationP3DiscoverabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.index = json.loads(INDEX.read_text(encoding="utf-8"))
        cls.skills = {item["name"]: item for item in cls.index["skills"]}

    def frontmatter(self, slug: str) -> dict[str, object]:
        return parse_frontmatter(ROOT / "skills" / slug / "SKILL.md")

    def test_contract_workflow_remains_default_public_entrypoint(self) -> None:
        default = self.skills["contract-workflow"]
        default_fm = self.frontmatter("contract-workflow")
        self.assertTrue(default["invocation"]["userFacing"])
        self.assertTrue(default_fm.get("implicitInvocation"))
        self.assertEqual(default["governance"]["discoverability"], "public")

    def test_explicit_contract_specialist_surfaces_are_advanced(self) -> None:
        for slug in sorted(ADVANCED_CONTRACT_SKILLS):
            with self.subTest(skill=slug):
                skill = self.skills[slug]
                fm = self.frontmatter(slug)
                self.assertTrue(skill["invocation"]["userFacing"])
                self.assertFalse(fm.get("implicitInvocation"))
                self.assertEqual(skill["governance"]["discoverability"], "advanced")
                self.assertNotEqual(skill["governance"]["status"], "deprecated")
                self.assertTrue(skill["evaluation"]["passed"])

    def test_discoverability_partition_matches_user_facing_contract(self) -> None:
        counts = self.index["discoverabilityCounts"]
        self.assertEqual(counts["public"] + counts["advanced"], self.index["entrypointCount"])
        self.assertEqual(
            counts["internal"] + counts["compatibility"],
            self.index["skillCount"] - self.index["entrypointCount"],
        )
        self.assertGreaterEqual(counts["advanced"], 9)
        self.assertEqual(sum(counts.values()), self.index["skillCount"])

    def test_advanced_is_not_inferred_from_implicit_invocation_flag(self) -> None:
        advanced_names = {
            item["name"]
            for item in self.index["skills"]
            if item["governance"]["discoverability"] == "advanced"
        }
        self.assertTrue(ADVANCED_CONTRACT_SKILLS.issubset(advanced_names))
        self.assertEqual(self.skills["thought-to-concept-flow"]["governance"]["discoverability"], "public")
        self.assertFalse(self.frontmatter("thought-to-concept-flow").get("implicitInvocation"))


if __name__ == "__main__":
    unittest.main()
