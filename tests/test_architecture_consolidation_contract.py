from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_dependency_graph import build_graph  # noqa: E402
from generate_repository_metadata import parse_frontmatter  # noqa: E402


class ArchitectureConsolidationContractTests(unittest.TestCase):
    def test_known_wrapper_artifacts_have_single_canonical_producer(self):
        graph = build_graph(ROOT)
        contracts = {item["output"]: item for item in graph["outputContracts"]}

        expected = {
            "learning-mission.json": "learning-mission",
            "learning-next-step.json": "learning-next-step",
            "learning-state.json": "learning-state",
            "multi-source-learning-model.json": "multi-source-learning-synthesis",
            "presentation-template-profile.json": "presentation-template-profiler",
            "presentation-qa.md": "template-presentation-workflow",
        }

        for artifact, producer in expected.items():
            with self.subTest(artifact=artifact):
                contract = contracts[artifact]
                self.assertFalse(contract["ambiguous"])
                self.assertEqual(contract["producers"], [producer])

    def test_legacy_direct_sport_renderer_is_deprecated_and_not_discoverable(self):
        path = ROOT / "skills" / "dr-komorowski-sport-report-renderer" / "SKILL.md"
        frontmatter = parse_frontmatter(path)

        self.assertEqual(frontmatter.get("status"), "deprecated")
        self.assertEqual(frontmatter.get("replacedBy"), "dr-komorowski-sport-pdf-report-renderer")
        self.assertNotEqual(frontmatter.get("userFacing"), True)
        self.assertNotIn("category", frontmatter)


if __name__ == "__main__":
    unittest.main()
