from __future__ import annotations

import unittest
from pathlib import Path

from skillz_core import load_graph, load_index, validate_catalog

ROOT = Path(__file__).resolve().parents[1]


class CatalogValidationTests(unittest.TestCase):
    def test_canonical_catalog_is_valid_for_serving(self) -> None:
        index = load_index(ROOT / "docs" / "skill-capability-index.json")
        graph = load_graph(ROOT / "docs" / "skill-dependency-graph.json")
        payload = validate_catalog(index, graph)
        self.assertTrue(payload["valid"], payload["errors"])
        self.assertEqual(payload["errorCount"], 0)
        self.assertIn("python scripts/validate_skills.py", payload["recommendedFullValidationCommands"])

    def test_duplicate_names_unknown_dependencies_and_cycles_fail(self) -> None:
        index = {
            "schemaVersion": 1,
            "skills": [
                {"name": "alpha", "requires": ["missing"], "outputs": [], "outputContracts": []},
                {"name": "alpha", "requires": [], "outputs": [], "outputContracts": []},
                {"name": "beta", "requires": ["alpha"], "outputs": [], "outputContracts": []},
            ],
        }
        graph = {
            "schemaVersion": 1,
            "skills": [
                {"name": "alpha", "requires": ["beta"], "outputs": []},
                {"name": "beta", "requires": ["alpha"], "outputs": []},
            ],
        }
        payload = validate_catalog(index, graph)
        self.assertFalse(payload["valid"])
        joined = "\n".join(payload["errors"])
        self.assertIn("duplicate skill name: alpha", joined)
        self.assertIn("requires unknown skill: missing", joined)
        self.assertIn("dependency cycle:", joined)

    def test_malformed_output_contract_fails_without_executing_anything(self) -> None:
        index = {
            "schemaVersion": 1,
            "skills": [
                {
                    "name": "alpha",
                    "requires": [],
                    "outputs": ["x.json"],
                    "outputContracts": [{"output": "x.json", "ambiguous": "no", "producers": "alpha", "consumerSkills": []}],
                }
            ],
        }
        graph = {"schemaVersion": 1, "skills": [{"name": "alpha", "requires": [], "outputs": ["x.json"]}]}
        payload = validate_catalog(index, graph)
        self.assertFalse(payload["valid"])
        self.assertTrue(any("boolean ambiguous" in error for error in payload["errors"]))
        self.assertTrue(any("string producers array" in error for error in payload["errors"]))


if __name__ == "__main__":
    unittest.main()
