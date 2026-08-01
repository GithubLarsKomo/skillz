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

import compile_capability_intent as compiler
import normalize_capability_intent_envelope as envelope_module


class CapabilityIntentEnvelopeTests(unittest.TestCase):
    def base_envelope(self) -> dict:
        return {
            "schemaVersion": 1,
            "intent": {
                "schemaVersion": 1,
                "desiredOutputs": ["review-decision.md"],
                "requiredDependencies": ["agent-handoff"],
                "allowedEvaluationModes": ["compatibility"],
                "portableFiles": "irrelevant",
            },
            "provenance": {
                "producerKind": "manual",
                "producer": "operator",
                "sourceRefs": ["issue:71"],
            },
            "confidence": {"level": "asserted", "basis": ["explicit-user-input"]},
            "review": {"reviewRequired": False, "reasons": []},
        }

    def test_manual_asserted_envelope_normalizes_without_inference(self):
        payload = envelope_module.normalize_envelope(self.base_envelope())
        self.assertEqual(payload["provenance"]["producerKind"], "manual")
        self.assertEqual(payload["confidence"]["level"], "asserted")
        self.assertFalse(payload["review"]["reviewRequired"])

    def test_model_low_confidence_review_required_is_preserved(self):
        envelope = self.base_envelope()
        envelope["provenance"] = {
            "producerKind": "model",
            "producer": "example-model-v1",
            "sourceRefs": ["prompt:abc"],
        }
        envelope["confidence"] = {"level": "low", "basis": ["ambiguous-input"]}
        envelope["review"] = {"reviewRequired": True, "reasons": ["low-confidence"]}
        payload = envelope_module.normalize_envelope(envelope)
        self.assertEqual(payload["confidence"]["level"], "low")
        self.assertTrue(payload["review"]["reviewRequired"])
        self.assertEqual(payload["review"]["reasons"], ["low-confidence"])

    def test_duplicate_metadata_and_intent_values_are_deterministically_normalized(self):
        envelope = self.base_envelope()
        envelope["intent"]["desiredOutputs"] = ["z.json", "a.json", "z.json"]
        envelope["provenance"]["sourceRefs"] = ["b", "a", "b"]
        envelope["confidence"]["basis"] = ["b", "a", "b"]
        envelope["review"]["reasons"] = ["b", "a", "b"]
        payload = envelope_module.normalize_envelope(envelope)
        self.assertEqual(payload["intent"]["desiredOutputs"], ["a.json", "z.json"])
        self.assertEqual(payload["provenance"]["sourceRefs"], ["a", "b"])
        self.assertEqual(payload["confidence"]["basis"], ["a", "b"])
        self.assertEqual(payload["review"]["reasons"], ["a", "b"])

    def test_extracted_intent_matches_shared_canonical_normalization(self):
        envelope = self.base_envelope()
        expected = compiler.normalize_intent(envelope["intent"])
        payload = envelope_module.normalize_envelope(envelope)
        self.assertEqual(payload["intent"], expected)
        self.assertEqual(envelope_module.render_json(payload["intent"]), envelope_module.render_json(expected))

    def test_invalid_nested_intent_fails_at_existing_intent_boundary(self):
        envelope = self.base_envelope()
        envelope["intent"]["allowedEvaluationModes"] = ["mystery"]
        with self.assertRaisesRegex(ValueError, "unsupported evaluation mode"):
            envelope_module.normalize_envelope(envelope)

    def test_unsupported_version_and_unknown_fields_fail_explicitly(self):
        envelope = self.base_envelope()
        envelope["schemaVersion"] = 2
        with self.assertRaisesRegex(ValueError, "unsupported intent envelope schemaVersion"):
            envelope_module.normalize_envelope(envelope)
        envelope = self.base_envelope()
        envelope["mystery"] = True
        with self.assertRaisesRegex(ValueError, "unknown intent envelope field"):
            envelope_module.normalize_envelope(envelope)

    def test_file_and_stdin_are_byte_equivalent_and_repeated_output_is_stable(self):
        envelope = self.base_envelope()
        raw = json.dumps(envelope)
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as handle:
            handle.write(raw)
            path = Path(handle.name)
        try:
            command = [sys.executable, str(SCRIPTS / "normalize_capability_intent_envelope.py")]
            file_run = subprocess.run(command + [str(path)], cwd=ROOT, text=True, capture_output=True, check=False)
            stdin_run = subprocess.run(command + ["-"], cwd=ROOT, text=True, input=raw, capture_output=True, check=False)
            repeat_run = subprocess.run(command + [str(path)], cwd=ROOT, text=True, capture_output=True, check=False)
            extract_run = subprocess.run(command + [str(path), "--extract-intent"], cwd=ROOT, text=True, capture_output=True, check=False)
            self.assertEqual(file_run.returncode, 0, file_run.stderr)
            self.assertEqual(stdin_run.returncode, 0, stdin_run.stderr)
            self.assertEqual(extract_run.returncode, 0, extract_run.stderr)
            self.assertEqual(file_run.stdout, stdin_run.stdout)
            self.assertEqual(file_run.stdout, repeat_run.stdout)
            expected_intent = envelope_module.render_json(compiler.normalize_intent(envelope["intent"])) + "\n"
            self.assertEqual(extract_run.stdout, expected_intent)
        finally:
            path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
