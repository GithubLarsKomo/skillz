from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import run_model_capability_pipeline as pipeline


class ModelCapabilityPipelineTests(unittest.TestCase):
    def proposal(self, output: str = "review-decision.md") -> dict:
        return {
            "schemaVersion": 1,
            "intent": {
                "schemaVersion": 1,
                "desiredOutputs": [output],
                "requiredDependencies": [],
                "allowedEvaluationModes": [],
                "portableFiles": "irrelevant",
            },
            "model": "fixture-model",
            "sourceRefs": ["source:test"],
            "confidence": "high",
            "confidenceBasis": ["explicit output"],
            "reviewReasons": ["model interpretation requires review"],
        }

    def fixture(self, output: str = "review-decision.md", response=None) -> dict:
        return {
            "schemaVersion": 1,
            "providerId": "fixture:e2e",
            "response": self.proposal(output) if response is None else response,
        }

    def review(self, decision: str = "approved") -> dict:
        return {
            "schemaVersion": 1,
            "decision": decision,
            "reviewer": "reviewer-1",
            "reasons": ["checked structured interpretation"],
        }

    def test_approved_happy_path_reaches_resolver(self):
        result = pipeline.run(
            "Create the review decision artifact.",
            self.fixture(),
            self.review(),
            pipeline.DEFAULT_INDEX,
        )
        self.assertEqual(result["status"], "resolved")
        self.assertIsNone(result["failedStage"])
        self.assertEqual(result["admission"]["status"], "approved")
        self.assertGreaterEqual(result["resolverOutput"]["candidateCount"], 1)

    def test_missing_review_never_reaches_resolver(self):
        result = pipeline.run("Create the review decision artifact.", self.fixture(), None, pipeline.DEFAULT_INDEX)
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["failedStage"], "review-admission")
        self.assertIsNone(result["resolverOutput"])
        self.assertIn("review is required", result["error"])

    def test_rejected_review_never_reaches_resolver(self):
        result = pipeline.run(
            "Create the review decision artifact.", self.fixture(), self.review("rejected"), pipeline.DEFAULT_INDEX
        )
        self.assertEqual(result["failedStage"], "review-admission")
        self.assertIsNone(result["resolverOutput"])
        self.assertIn("rejected", result["error"])

    def test_malformed_model_output_fails_at_model_run(self):
        result = pipeline.run(
            "Create the review decision artifact.", self.fixture(response="not-json"), self.review(), pipeline.DEFAULT_INDEX
        )
        self.assertEqual(result["failedStage"], "model-run")
        self.assertIsNone(result["admission"])
        self.assertIsNone(result["resolverOutput"])

    def test_valid_unknown_output_resolves_to_zero_candidates(self):
        result = pipeline.run(
            "Use a capability that does not exist.",
            self.fixture("definitely-unknown-output.xyz"),
            self.review(),
            pipeline.DEFAULT_INDEX,
        )
        self.assertEqual(result["status"], "resolved")
        self.assertEqual(result["resolverOutput"]["candidateCount"], 0)

    def test_repeated_success_is_byte_stable(self):
        first = pipeline.canonical_json(
            pipeline.run("Create the review decision artifact.", self.fixture(), self.review(), pipeline.DEFAULT_INDEX)
        )
        second = pipeline.canonical_json(
            pipeline.run("Create the review decision artifact.", self.fixture(), self.review(), pipeline.DEFAULT_INDEX)
        )
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
