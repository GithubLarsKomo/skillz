from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_model_interpretation_request as request_builder
import qualify_model_provider as qualifier
import run_model_interpretation as runner
import score_capability_interpretations as scorer


class ModelRunnerProviderModeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((ROOT / "docs" / "skill-capability-index.json").read_text(encoding="utf-8"))
        cls.benchmark = scorer.load_json(ROOT / "benchmarks" / "capability-interpretation-v1.json")
        cls.proposals = scorer.load_json(ROOT / "benchmarks" / "capability-interpretation-baseline-v1.json")
        cls.proposal = cls.proposals["proposals"][0]["proposal"]
        cls.request = request_builder.build_request("Create the review decision artifact.", cls.index)
        cls.config = {
            "schemaVersion": 1,
            "providerId": "openai-compatible:test",
            "endpoint": "http://localhost:11434/v1/chat/completions",
            "modelId": "fixture-model",
            "apiKeyEnv": None,
            "timeoutSeconds": 5,
        }
        cls.qualification = qualifier.qualify(
            cls.config["providerId"], cls.config["modelId"], cls.benchmark, cls.proposals, cls.index
        )

    def test_fixture_mode_remains_backward_compatible(self):
        fixture = {"schemaVersion": 1, "providerId": "fixture:test", "response": self.proposal}
        result = runner.run(self.request, fixture)
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(result["provider"], {"kind": "fixture", "id": "fixture:test"})

    def test_qualified_openai_compatible_mode_uses_fake_transport(self):
        def transport(*args):
            return json.dumps({"choices": [{"message": {"content": json.dumps(self.proposal)}}]}).encode()
        result = runner.run_openai_compatible(
            self.request, self.config, self.qualification, self.benchmark, self.index,
            transport=transport, environ={}
        )
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(result["provider"]["kind"], "openai-compatible")
        expected = dict(self.proposal, model=self.config["modelId"])
        self.assertEqual(result["proposal"], expected)

    def test_stale_qualification_rejected_before_transport(self):
        called = False
        def transport(*args):
            nonlocal called
            called = True
            return b"{}"
        bad = dict(self.qualification, benchmarkSha256="0" * 64)
        result = runner.run_openai_compatible(
            self.request, self.config, bad, self.benchmark, self.index,
            transport=transport, environ={}
        )
        self.assertEqual(result["status"], "rejected")
        self.assertIn("benchmark fingerprint", result["validationError"])
        self.assertFalse(called)

    def test_provider_mode_argument_conflicts_are_explicit(self):
        with self.assertRaisesRegex(ValueError, "fixture mode"):
            runner.validate_mode_args("fixture", Path("qualification.json"), None, Path("index.json"))
        with self.assertRaisesRegex(ValueError, "requires"):
            runner.validate_mode_args("openai-compatible", None, Path("benchmark.json"), Path("index.json"))


if __name__ == "__main__":
    unittest.main()
