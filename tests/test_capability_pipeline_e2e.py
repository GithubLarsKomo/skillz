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


compiler = load_module("compile_capability_intent", ROOT / "scripts" / "compile_capability_intent.py")
resolver = load_module("resolve_capabilities", ROOT / "scripts" / "resolve_capabilities.py")
schemas = load_module("validate_metadata_schemas", ROOT / "scripts" / "validate_metadata_schemas.py")


class CapabilityPipelineE2ETests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = resolver.load_index(ROOT / "docs" / "skill-capability-index.json")
        cls.request_schema = json.loads((ROOT / "schemas" / "capability-resolver-request-v1.schema.json").read_text())
        cls.output_schema = json.loads((ROOT / "schemas" / "capability-resolver-output-v1.schema.json").read_text())

    def compile_and_resolve(self, intent: dict):
        request = compiler.compile_intent(intent)
        self.assertEqual(schemas.validate(request, self.request_schema), [])
        constraints = resolver.normalize_constraints(
            request["outputs"],
            request["dependencies"],
            request["evaluationModes"],
            request["portableFiles"],
        )
        payload = resolver.resolve(self.index, constraints)
        self.assertEqual(schemas.validate(payload, self.output_schema), [])
        return request, payload

    def test_real_pipeline_returns_non_empty_candidates(self):
        request, payload = self.compile_and_resolve({
            "schemaVersion": 1,
            "requiredDependencies": ["iterate-software-projects"],
            "allowedEvaluationModes": ["compatibility"],
        })
        self.assertGreater(payload["candidateCount"], 0)
        self.assertEqual(request["dependencies"], ["iterate-software-projects"])

    def test_empty_candidate_set_is_successful(self):
        _, payload = self.compile_and_resolve({
            "schemaVersion": 1,
            "desiredOutputs": ["agent-handoff.json"],
            "requiredDependencies": ["disciplined-diagnosis"],
        })
        self.assertEqual(payload["candidateCount"], 0)
        self.assertEqual(payload["candidates"], [])

    def test_ambiguous_output_contract_is_preserved(self):
        _, payload = self.compile_and_resolve({
            "schemaVersion": 1,
            "desiredOutputs": ["residual-risk-handoff.json"],
        })
        self.assertGreaterEqual(payload["candidateCount"], 2)
        contracts = [
            contract
            for candidate in payload["candidates"]
            for contract in candidate["matchedOutputContracts"]
            if contract["output"] == "residual-risk-handoff.json"
        ]
        self.assertTrue(contracts)
        self.assertTrue(all(contract["ambiguous"] for contract in contracts))
        self.assertTrue(all(len(contract["producers"]) > 1 for contract in contracts))

    def test_duplicate_normalization_and_repeated_execution_are_byte_stable(self):
        intent = {
            "schemaVersion": 1,
            "requiredDependencies": ["iterate-software-projects", "iterate-software-projects"],
            "allowedEvaluationModes": ["compatibility", "compatibility"],
        }
        request1, payload1 = self.compile_and_resolve(intent)
        request2, payload2 = self.compile_and_resolve(intent)
        dump = lambda value: json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        self.assertEqual(dump(request1), dump(request2))
        self.assertEqual(dump(payload1), dump(payload2))
        self.assertEqual(request1["dependencies"], ["iterate-software-projects"])

    def test_schema_valid_but_unknown_output_fails_at_resolver_boundary(self):
        request = compiler.compile_intent({"schemaVersion": 1, "desiredOutputs": ["missing-output.json"]})
        self.assertEqual(schemas.validate(request, self.request_schema), [])
        constraints = resolver.normalize_constraints(
            request["outputs"], request["dependencies"], request["evaluationModes"], request["portableFiles"]
        )
        with self.assertRaisesRegex(ValueError, "unknown output"):
            resolver.resolve(self.index, constraints)


if __name__ == "__main__":
    unittest.main()
