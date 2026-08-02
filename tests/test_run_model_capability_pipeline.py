from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import qualify_model_provider as qualifier
import run_model_capability_pipeline as pipeline

BENCHMARK = ROOT / "benchmarks" / "capability-interpretation-v1.json"
BASELINE = ROOT / "benchmarks" / "capability-interpretation-baseline-v1.json"


class ModelCapabilityPipelineTests(unittest.TestCase):
    def proposal(self, output: str = "review-decision.md", dependencies: list[str] | None = None) -> dict:
        return {
            "schemaVersion": 1,
            "intent": {
                "schemaVersion": 1,
                "desiredOutputs": [output],
                "requiredDependencies": dependencies or [],
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

    def provider_config(self) -> dict:
        return {
            "schemaVersion": 1,
            "providerId": "local-openai",
            "endpoint": "http://127.0.0.1:11434/v1/chat/completions",
            "modelId": "fixture-model",
            "apiKeyEnv": None,
            "timeoutSeconds": 5,
        }

    def provider_inputs(self):
        benchmark = json.loads(BENCHMARK.read_text(encoding="utf-8"))
        proposals = json.loads(BASELINE.read_text(encoding="utf-8"))
        index = json.loads(pipeline.DEFAULT_INDEX.read_text(encoding="utf-8"))
        qualification = qualifier.qualify("local-openai", "fixture-model", benchmark, proposals, index)
        return benchmark, qualification

    def fake_transport(self, endpoint, body, headers, timeout):
        payload = {"choices": [{"message": {"content": json.dumps(self.proposal())}}]}
        return json.dumps(payload).encode("utf-8")

    def test_approved_happy_path_reaches_resolver(self):
        result = pipeline.run("Create the review decision artifact.", self.fixture(), self.review(), pipeline.DEFAULT_INDEX)
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
        result = pipeline.run("Create the review decision artifact.", self.fixture(), self.review("rejected"), pipeline.DEFAULT_INDEX)
        self.assertEqual(result["failedStage"], "review-admission")
        self.assertIsNone(result["resolverOutput"])
        self.assertIn("rejected", result["error"])

    def test_malformed_model_output_fails_at_provider_run(self):
        result = pipeline.run("Create the review decision artifact.", self.fixture(response="not-json"), self.review(), pipeline.DEFAULT_INDEX)
        self.assertEqual(result["failedStage"], "provider-run")
        self.assertIsNone(result["admission"])
        self.assertIsNone(result["resolverOutput"])

    def test_valid_conflicting_constraints_resolve_to_zero_candidates(self):
        proposal = self.proposal("review-decision.md", dependencies=["central-skill-repository-curation"])
        result = pipeline.run(
            "Require a review decision from a capability that also depends on central repository curation.",
            self.fixture(response=proposal),
            self.review(),
            pipeline.DEFAULT_INDEX,
        )
        self.assertEqual(result["status"], "resolved")
        self.assertEqual(result["resolverOutput"]["candidateCount"], 0)

    def test_qualified_openai_compatible_provider_reaches_resolver(self):
        benchmark, qualification = self.provider_inputs()
        result = pipeline.run(
            "Create the review decision artifact.",
            self.provider_config(),
            self.review(),
            pipeline.DEFAULT_INDEX,
            provider_mode="openai-compatible",
            qualification=qualification,
            benchmark=benchmark,
            transport=self.fake_transport,
        )
        self.assertEqual(result["status"], "resolved")
        self.assertEqual(result["modelRun"]["provider"]["kind"], "openai-compatible")
        self.assertGreaterEqual(result["resolverOutput"]["candidateCount"], 1)

    def test_stale_provider_qualification_blocks_before_review(self):
        benchmark, qualification = self.provider_inputs()
        qualification["capabilityIndexSha256"] = "0" * 64
        result = pipeline.run(
            "Create the review decision artifact.", self.provider_config(), self.review(), pipeline.DEFAULT_INDEX,
            provider_mode="openai-compatible", qualification=qualification, benchmark=benchmark, transport=self.fake_transport,
        )
        self.assertEqual(result["failedStage"], "provider-run")
        self.assertIsNone(result["admission"])
        self.assertIn("fingerprint", result["error"])

    def test_provider_transport_failure_blocks_before_review(self):
        benchmark, qualification = self.provider_inputs()
        def failing_transport(endpoint, body, headers, timeout):
            raise ValueError("provider transport error: offline")
        result = pipeline.run(
            "Create the review decision artifact.", self.provider_config(), self.review(), pipeline.DEFAULT_INDEX,
            provider_mode="openai-compatible", qualification=qualification, benchmark=benchmark, transport=failing_transport,
        )
        self.assertEqual(result["failedStage"], "provider-run")
        self.assertIsNone(result["admission"])
        self.assertIn("transport", result["error"])

    def test_provider_success_without_review_never_reaches_resolver(self):
        benchmark, qualification = self.provider_inputs()
        result = pipeline.run(
            "Create the review decision artifact.", self.provider_config(), None, pipeline.DEFAULT_INDEX,
            provider_mode="openai-compatible", qualification=qualification, benchmark=benchmark, transport=self.fake_transport,
        )
        self.assertEqual(result["failedStage"], "review-admission")
        self.assertIsNone(result["resolverOutput"])

    def test_repeated_success_is_byte_stable(self):
        first = pipeline.canonical_json(pipeline.run("Create the review decision artifact.", self.fixture(), self.review(), pipeline.DEFAULT_INDEX))
        second = pipeline.canonical_json(pipeline.run("Create the review decision artifact.", self.fixture(), self.review(), pipeline.DEFAULT_INDEX))
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
