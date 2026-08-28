from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_dependency_graph import build_graph  # noqa: E402


class ArchitectureConsolidationP1SourceSpineTests(unittest.TestCase):
    def test_source_context_has_explicit_research_and_learning_consumers(self) -> None:
        graph = build_graph(ROOT)
        by_name = {item["name"]: item for item in graph["skills"]}
        expected = {"source-context.json"}
        self.assertEqual(set(by_name["research-to-evidence-note"]["consumes"]), expected)
        self.assertEqual(set(by_name["multimodal-learning-analysis"]["consumes"]), expected)

        contracts = {item["output"]: item for item in graph["outputContracts"]}
        source_context = contracts["source-context.json"]
        self.assertFalse(source_context["ambiguous"])
        self.assertEqual(source_context["producers"], ["source-to-context"])
        self.assertEqual(
            set(source_context["consumerSkills"]),
            {"research-to-evidence-note", "multimodal-learning-analysis"},
        )
        self.assertEqual(source_context["consumptionStatus"], "explicit")


if __name__ == "__main__":
    unittest.main()
