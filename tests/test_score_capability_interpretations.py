from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import score_capability_interpretations as scorer


class InterpretationBenchmarkScorerTests(unittest.TestCase):
    def benchmark(self) -> dict:
        return {
            "schemaVersion": 1,
            "cases": [
                {
                    "id": "case-a",
                    "sourceText": "Produce a review decision and require compatibility evaluation.",
                    "expectedIntent": {
                        "schemaVersion": 1,
                        "desiredOutputs": ["review-decision.md"],
                        "requiredDependencies": [],
                        "allowedEvaluationModes": ["compatibility"],
                        "portableFiles": "irrelevant",
                    },
                    "forbiddenConstraints": {
                        "desiredOutputs": ["deployment-plan.md"],
                        "requiredDependencies": ["disciplined-diagnosis"],
                        "allowedEvaluationModes": ["none"],
                    },
                    "allowedConfidenceLevels": ["high"],
                    "requiredReviewReasons": ["human-check"],
                    "forbiddenReviewReasons": ["ignore-review"],
                }
            ],
        }

    def proposal(self, **overrides) -> dict:
        proposal = {
            "schemaVersion": 1,
            "intent": {
                "schemaVersion": 1,
                "desiredOutputs": ["review-decision.md"],
                "requiredDependencies": [],
                "allowedEvaluationModes": ["compatibility"],
                "portableFiles": "irrelevant",
            },
            "model": "test-model",
            "sourceRefs": ["source:a"],
            "confidence": "high",
            "confidenceBasis": ["explicit"],
            "reviewReasons": ["human-check"],
        }
        proposal.update(overrides)
        return proposal

    def proposal_set(self, proposal: dict | None = None) -> dict:
        return {"schemaVersion": 1, "proposals": [{"caseId": "case-a", "proposal": proposal or self.proposal()}]}

    def test_exact_match_passes(self):
        result = scorer.score(self.benchmark(), self.proposal_set())
        self.assertTrue(result["passed"])
        self.assertEqual(result["passedCount"], 1)

    def test_missing_and_invented_constraints_are_reported_separately(self):
        proposal = self.proposal()
        proposal["intent"] = dict(proposal["intent"])
        proposal["intent"]["desiredOutputs"] = ["deployment-plan.md"]
        result = scorer.score(self.benchmark(), self.proposal_set(proposal))
        finding = result["cases"][0]
        self.assertEqual(finding["missingRequiredConstraints"]["desiredOutputs"], ["review-decision.md"])
        self.assertEqual(finding["inventedConstraints"]["desiredOutputs"], ["deployment-plan.md"])
        self.assertEqual(finding["forbiddenConstraintsObserved"]["desiredOutputs"], ["deployment-plan.md"])
        self.assertFalse(finding["passed"])

    def test_adapter_rejects_envelope_control_fields(self):
        proposal = self.proposal(reviewRequired=False)
        result = scorer.score(self.benchmark(), self.proposal_set(proposal))
        finding = result["cases"][0]
        self.assertFalse(finding["adapterCompatible"])
        self.assertIn("unknown model interpretation field", finding["validationError"])

    def test_missing_review_reason_and_confidence_mismatch_fail(self):
        proposal = self.proposal(confidence="low", reviewReasons=[])
        result = scorer.score(self.benchmark(), self.proposal_set(proposal))
        finding = result["cases"][0]
        self.assertFalse(finding["confidenceAccepted"])
        self.assertEqual(finding["missingReviewReasons"], ["human-check"])

    def test_missing_proposal_is_a_case_failure(self):
        result = scorer.score(self.benchmark(), {"schemaVersion": 1, "proposals": []})
        self.assertEqual(result["failedCount"], 1)
        self.assertEqual(result["cases"][0]["validationError"], "missing proposal")

    def test_unknown_case_id_is_rejected(self):
        proposal_set = {"schemaVersion": 1, "proposals": [{"caseId": "other", "proposal": self.proposal()}]}
        with self.assertRaisesRegex(ValueError, "unknown caseId"):
            scorer.score(self.benchmark(), proposal_set)

    def test_output_is_byte_stable(self):
        first = scorer.render_json(scorer.score(self.benchmark(), self.proposal_set()))
        second = scorer.render_json(scorer.score(self.benchmark(), self.proposal_set()))
        self.assertEqual(first, second)

    def test_committed_seed_baseline_passes(self):
        benchmark = json.loads((ROOT / "benchmarks" / "capability-interpretation-v1.json").read_text(encoding="utf-8"))
        proposals = json.loads((ROOT / "benchmarks" / "capability-interpretation-baseline-v1.json").read_text(encoding="utf-8"))
        result = scorer.score(benchmark, proposals)
        self.assertTrue(result["passed"])
        self.assertEqual(result["caseCount"], 5)


if __name__ == "__main__":
    unittest.main()
