from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_model_interpretation_request as builder


class ModelInterpretationRequestTests(unittest.TestCase):
    def index(self) -> dict:
        return {
            "schemaVersion": 1,
            "skills": [
                {"name": "b-skill", "outputs": ["b.json", "shared.json"]},
                {"name": "a-skill", "outputs": ["a.json", "shared.json"]},
            ],
        }

    def test_ordering_and_output_are_deterministic(self):
        first = builder.build_request("source", self.index())
        second = builder.build_request("source", self.index())
        self.assertEqual(first, second)
        self.assertEqual(first["availableCapabilities"], ["a-skill", "b-skill"])
        self.assertEqual(first["availableOutputs"], ["a.json", "b.json", "shared.json"])
        self.assertEqual(builder.render_json(first), builder.render_json(second))

    def test_source_text_change_changes_request_id_only_not_index_fingerprint(self):
        first = builder.build_request("source one", self.index())
        second = builder.build_request("source two", self.index())
        self.assertNotEqual(first["requestId"], second["requestId"])
        self.assertEqual(first["capabilityIndex"]["sha256"], second["capabilityIndex"]["sha256"])

    def test_index_content_change_changes_fingerprint_and_request_id(self):
        first = builder.build_request("source", self.index())
        changed = copy.deepcopy(self.index())
        changed["skills"][0]["outputs"].append("new.json")
        second = builder.build_request("source", changed)
        self.assertNotEqual(first["capabilityIndex"]["sha256"], second["capabilityIndex"]["sha256"])
        self.assertNotEqual(first["requestId"], second["requestId"])

    def test_index_key_order_does_not_change_fingerprint(self):
        first_index = self.index()
        second_index = {"skills": first_index["skills"], "schemaVersion": 1}
        first = builder.build_request("source", first_index)
        second = builder.build_request("source", second_index)
        self.assertEqual(first["capabilityIndex"]["sha256"], second["capabilityIndex"]["sha256"])
        self.assertEqual(first["requestId"], second["requestId"])

    def test_control_rules_forbid_model_owned_provenance_and_admission(self):
        request = builder.build_request("source", self.index())
        rules = " ".join(request["controlRules"])
        self.assertIn("producerKind", rules)
        self.assertIn("reviewRequired", rules)
        self.assertEqual(request["responseSchema"], "capability-model-interpretation-v1")

    def test_malformed_index_fails(self):
        with self.assertRaisesRegex(ValueError, "outputs must be an array"):
            builder.build_request("source", {"schemaVersion": 1, "skills": [{"name": "x", "outputs": "bad"}]})
        with self.assertRaisesRegex(ValueError, "source text must be non-empty"):
            builder.build_request("   ", self.index())

    def test_committed_index_builds_successfully(self):
        index = builder.load_index(ROOT / "docs" / "skill-capability-index.json")
        request = builder.build_request("Create a review decision artifact.", index)
        self.assertEqual(request["schemaVersion"], 1)
        self.assertGreater(len(request["availableCapabilities"]), 0)
        self.assertGreater(len(request["availableOutputs"]), 0)


if __name__ == "__main__":
    unittest.main()
