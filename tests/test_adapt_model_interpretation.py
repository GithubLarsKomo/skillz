from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import adapt_model_interpretation as adapter
import admit_capability_intent as admission
import normalize_capability_intent_envelope as envelope_module


class AdaptModelInterpretationTests(unittest.TestCase):
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
            "model": "model-x",
            "sourceRefs": ["source:b", "source:a", "source:b"],
            "confidence": "low",
            "confidenceBasis": ["basis:b", "basis:a", "basis:b"],
            "reviewReasons": ["ambiguity:b", "ambiguity:a", "ambiguity:b"],
        }

    def test_valid_proposal_stamps_model_provenance_and_review(self):
        envelope = adapter.adapt(self.proposal())
        self.assertEqual(envelope["provenance"]["producerKind"], "model")
        self.assertEqual(envelope["provenance"]["producer"], "model-x")
        self.assertTrue(envelope["review"]["reviewRequired"])
        admission.validate_producer_policy(envelope)
        with self.assertRaisesRegex(ValueError, "review is required"):
            admission.admit(envelope, None)

    def test_arrays_are_deterministically_normalized(self):
        envelope = adapter.adapt(self.proposal())
        self.assertEqual(envelope["provenance"]["sourceRefs"], ["source:a", "source:b"])
        self.assertEqual(envelope["confidence"]["basis"], ["basis:a", "basis:b"])
        self.assertEqual(envelope["review"]["reasons"], ["ambiguity:a", "ambiguity:b"])

    def test_invalid_nested_intent_fails(self):
        proposal = self.proposal()
        proposal["intent"]["mystery"] = True
        with self.assertRaisesRegex(ValueError, "unknown intent field"):
            adapter.adapt(proposal)

    def test_invalid_confidence_fails(self):
        proposal = self.proposal()
        proposal["confidence"] = "certain"
        with self.assertRaisesRegex(ValueError, "unsupported confidence level"):
            adapter.adapt(proposal)

    def test_envelope_control_fields_are_forbidden(self):
        proposal = self.proposal()
        proposal["reviewRequired"] = False
        with self.assertRaisesRegex(ValueError, "unknown model interpretation field"):
            adapter.adapt(proposal)
        proposal = self.proposal()
        proposal["producerKind"] = "manual"
        with self.assertRaisesRegex(ValueError, "unknown model interpretation field"):
            adapter.adapt(proposal)

    def test_repeated_output_is_byte_stable(self):
        first = envelope_module.render_json(adapter.adapt(self.proposal()))
        second = envelope_module.render_json(adapter.adapt(self.proposal()))
        self.assertEqual(first, second)

    def test_file_and_stdin_cli_are_equivalent(self):
        payload = json.dumps(self.proposal())
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "proposal.json"
            path.write_text(payload, encoding="utf-8")
            file_run = subprocess.run(
                [sys.executable, str(SCRIPTS / "adapt_model_interpretation.py"), str(path)],
                capture_output=True,
                text=True,
                check=False,
            )
            stdin_run = subprocess.run(
                [sys.executable, str(SCRIPTS / "adapt_model_interpretation.py"), "-"],
                input=payload,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(file_run.returncode, 0, file_run.stderr)
        self.assertEqual(stdin_run.returncode, 0, stdin_run.stderr)
        self.assertEqual(file_run.stdout, stdin_run.stdout)


if __name__ == "__main__":
    unittest.main()
