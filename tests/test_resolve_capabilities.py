from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


resolver = load_module("resolve_capabilities", ROOT / "scripts" / "resolve_capabilities.py")
schemas = load_module("validate_metadata_schemas", ROOT / "scripts" / "validate_metadata_schemas.py")


def skill(name, *, requires=None, outputs=None, mode="compatibility", portable=None, contracts=None):
    return {
        "name": name,
        "description": name,
        "requires": requires or [],
        "dependents": [],
        "outputs": outputs or [],
        "outputContracts": contracts or [],
        "portableFiles": portable or [],
        "evaluation": {"mode": mode, "caseCount": 3, "recordedResultCount": 3, "passed": True},
    }


class ResolveCapabilitiesTests(unittest.TestCase):
    def setUp(self):
        shared = {
            "output": "shared.json",
            "ambiguous": True,
            "producers": ["alpha", "beta"],
            "consumerSkills": [],
        }
        self.index = {
            "schemaVersion": 1,
            "skills": [
                skill("beta", requires=["base"], outputs=["shared.json"], mode="rubric", contracts=[shared]),
                skill("base", outputs=["base.json"]),
                skill("alpha", requires=["base"], outputs=["shared.json"], portable=["scripts/helper.py"], contracts=[shared]),
            ],
        }

    def constraints(self, outputs=None, dependencies=None, modes=None, portable="irrelevant"):
        return resolver.normalize_constraints(outputs or [], dependencies or [], modes or [], portable)

    def test_single_output_preserves_ambiguous_producers_and_order(self):
        payload = resolver.resolve(self.index, self.constraints(outputs=["shared.json"]))
        self.assertEqual([item["name"] for item in payload["candidates"]], ["alpha", "beta"])
        contract = payload["candidates"][0]["matchedOutputContracts"][0]
        self.assertTrue(contract["ambiguous"])
        self.assertEqual(contract["producers"], ["alpha", "beta"])

    def test_combined_constraints_intersect(self):
        payload = resolver.resolve(
            self.index,
            self.constraints(outputs=["shared.json"], dependencies=["base"], modes=["compatibility"], portable="required"),
        )
        self.assertEqual([item["name"] for item in payload["candidates"]], ["alpha"])
        self.assertIn("evaluationMode:compatibility", payload["candidates"][0]["matchReasons"])

    def test_empty_candidate_set_is_valid(self):
        payload = resolver.resolve(
            self.index,
            self.constraints(outputs=["base.json"], dependencies=["base"]),
        )
        self.assertEqual(payload["candidateCount"], 0)
        self.assertEqual(payload["candidates"], [])
        self.assertEqual(len(payload["rejections"]), 3)

    def test_unknown_constraints_fail_explicitly(self):
        with self.assertRaisesRegex(ValueError, "unknown output"):
            resolver.resolve(self.index, self.constraints(outputs=["missing.json"]))
        with self.assertRaisesRegex(ValueError, "unknown dependency"):
            resolver.resolve(self.index, self.constraints(dependencies=["missing-skill"]))
        with self.assertRaisesRegex(ValueError, "unsupported evaluation mode"):
            self.constraints(modes=["mystery"])

    def test_output_validates_against_v1_schema(self):
        payload = resolver.resolve(self.index, self.constraints(outputs=["shared.json"]))
        schema = json.loads((ROOT / "schemas" / "capability-resolver-output-v1.schema.json").read_text())
        self.assertEqual(schemas.validate(payload, schema), [])

    def test_rejections_are_deterministic_and_explain_failed_constraints(self):
        payload = resolver.resolve(self.index, self.constraints(outputs=["base.json"]))
        self.assertEqual([item["name"] for item in payload["rejections"]], ["alpha", "beta"])
        self.assertEqual(payload["rejections"][0]["failedConstraints"], ["output:base.json"])


if __name__ == "__main__":
    unittest.main()
