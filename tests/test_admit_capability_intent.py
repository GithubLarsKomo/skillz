from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admit_capability_intent as admission
import normalize_capability_intent_envelope as envelope_module


class AdmitCapabilityIntentTests(unittest.TestCase):
    def envelope(self, review_required: bool = False) -> dict:
        return envelope_module.normalize_envelope(
            {
                "schemaVersion": 1,
                "intent": {
                    "schemaVersion": 1,
                    "desiredOutputs": ["review-decision.md"],
                    "requiredDependencies": [],
                    "allowedEvaluationModes": ["compatibility"],
                    "portableFiles": "irrelevant",
                },
                "provenance": {
                    "producerKind": "model" if review_required else "manual",
                    "producer": "producer",
                    "sourceRefs": ["source:b", "source:a", "source:b"],
                },
                "confidence": {
                    "level": "low" if review_required else "asserted",
                    "basis": ["basis:b", "basis:a", "basis:b"],
                },
                "review": {
                    "reviewRequired": review_required,
                    "reasons": ["reason:b", "reason:a", "reason:b"] if review_required else [],
                },
            }
        )

    def review(self, decision: str = "approved") -> dict:
        return admission.normalize_review(
            {
                "schemaVersion": 1,
                "decision": decision,
                "reviewer": "reviewer-1",
                "reasons": ["b", "a", "b"],
            }
        )

    def test_no_review_required_succeeds_without_review_artifact(self):
        envelope = self.envelope(False)
        self.assertEqual(admission.admit(envelope, None), envelope["intent"])

    def test_review_required_without_decision_fails(self):
        with self.assertRaisesRegex(ValueError, "review is required"):
            admission.admit(self.envelope(True), None)

    def test_explicit_approval_succeeds_and_returns_canonical_intent(self):
        envelope = self.envelope(True)
        self.assertEqual(admission.admit(envelope, self.review("approved")), envelope["intent"])

    def test_rejection_always_blocks_admission(self):
        with self.assertRaisesRegex(ValueError, "rejected"):
            admission.admit(self.envelope(False), self.review("rejected"))
        with self.assertRaisesRegex(ValueError, "rejected"):
            admission.admit(self.envelope(True), self.review("rejected"))

    def test_malformed_review_artifact_fails_explicitly(self):
        with self.assertRaisesRegex(ValueError, "unsupported review decision"):
            admission.normalize_review(
                {"schemaVersion": 1, "decision": "maybe", "reviewer": "r", "reasons": []}
            )
        with self.assertRaisesRegex(ValueError, "unknown review field"):
            admission.normalize_review(
                {
                    "schemaVersion": 1,
                    "decision": "approved",
                    "reviewer": "r",
                    "reasons": [],
                    "mystery": True,
                }
            )

    def test_review_reasons_are_deterministically_normalized(self):
        review = self.review("approved")
        self.assertEqual(review["reasons"], ["a", "b"])

    def test_repeated_success_output_is_byte_stable(self):
        envelope = self.envelope(True)
        intent = admission.admit(envelope, self.review("approved"))
        first = envelope_module.render_json(intent)
        second = envelope_module.render_json(admission.admit(envelope, self.review("approved")))
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
