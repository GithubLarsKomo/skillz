from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import run_model_interpretation as runner


class ModelInterpretationRunnerTests(unittest.TestCase):
    def request(self) -> dict:
        return {
            "schemaVersion": 1,
            "requestId": "request-123",
            "sourceText": "Create a review decision artifact.",
            "capabilityIndex": {"schemaVersion": 1, "sha256": "abc"},
            "availableCapabilities": ["two-axis-code-review"],
            "availableOutputs": ["review-decision.md"],
            "responseSchema": "capability-model-interpretation-v1",
            "controlRules": ["Do not emit reviewRequired."],
        }

    def proposal(self) -> dict:
        return {
            "schemaVersion": 1,
            "intent": {
                "schemaVersion": 1,
                "desiredOutputs": ["review-decision.md"],
                "requiredDependencies": [],
                "allowedEvaluationModes": ["compatibility"],
                "portableFiles": "irrelevant",
            },
            "model": "fixture-model",
            "sourceRefs": ["request:request-123"],
            "confidence": "high",
            "confidenceBasis": ["explicit output requested"],
            "reviewReasons": ["model interpretation requires review"],
        }

    def fixture(self, response=None) -> dict:
        return {
            "schemaVersion": 1,
            "providerId": "fixture:test",
            "response": self.proposal() if response is None else response,
        }

    def benchmark(self) -> dict:
        return {
            "schemaVersion": 1,
            "cases": [
                {
                    "id": "case-1",
                    "sourceText": "Create a review decision artifact.",
                    "expectedIntent": self.proposal()["intent"],
                    "forbiddenConstraints": {
                        "desiredOutputs": [],
                        "requiredDependencies": [],
                        "allowedEvaluationModes": [],
                    },
                    "allowedConfidenceLevels": ["high"],
                    "requiredReviewReasons": ["model interpretation requires review"],
                    "forbiddenReviewReasons": [],
                }
            ],
        }

    def test_success_propagates_request_and_provider(self):
        result = runner.run(self.request(), self.fixture())
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(result["requestId"], "request-123")
        self.assertEqual(result["provider"], {"kind": "fixture", "id": "fixture:test"})
        self.assertTrue(result["adapterCompatible"])
        self.assertIsNone(result["validationError"])

    def test_malformed_provider_output_is_rejected(self):
        result = runner.run(self.request(), self.fixture("not-json"))
        self.assertEqual(result["status"], "rejected")
        self.assertIn("not valid JSON", result["validationError"])
        self.assertFalse(result["adapterCompatible"])

    def test_forbidden_envelope_control_is_rejected_by_existing_adapter(self):
        proposal = self.proposal()
        proposal["reviewRequired"] = False
        result = runner.run(self.request(), self.fixture(proposal))
        self.assertEqual(result["status"], "rejected")
        self.assertIn("unknown model interpretation field", result["validationError"])

    def test_wrong_proposal_schema_version_is_rejected(self):
        proposal = self.proposal()
        proposal["schemaVersion"] = 2
        result = runner.run(self.request(), self.fixture(proposal))
        self.assertEqual(result["status"], "rejected")
        self.assertIn("unsupported model interpretation schemaVersion", result["validationError"])

    def test_optional_benchmark_scoring_reuses_existing_scorer(self):
        result = runner.run(self.request(), self.fixture(), self.benchmark(), "case-1")
        self.assertEqual(result["status"], "accepted")
        self.assertTrue(result["benchmarkFinding"]["passed"])
        self.assertEqual(result["benchmarkFinding"]["caseId"], "case-1")

    def test_benchmark_arguments_must_be_paired(self):
        result = runner.run(self.request(), self.fixture(), self.benchmark(), None)
        self.assertEqual(result["status"], "rejected")
        self.assertIn("provided together", result["validationError"])

    def test_repeated_output_is_byte_stable(self):
        first = runner.canonical_json(runner.run(self.request(), self.fixture(), self.benchmark(), "case-1"))
        second = runner.canonical_json(runner.run(self.request(), self.fixture(), self.benchmark(), "case-1"))
        self.assertEqual(first, second)

    def test_invalid_request_fails_before_provider(self):
        request = self.request()
        request["responseSchema"] = "other"
        with self.assertRaisesRegex(ValueError, "responseSchema"):
            runner.run(request, self.fixture())


if __name__ == "__main__":
    unittest.main()
