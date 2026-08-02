from __future__ import annotations

import json
import sys
import tempfile
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
            cls.config["providerId"], cls.config["modelId"], cls.benchmark, cls.proposals, cls.index,
            provider_config=cls.config,
        )

    def fake_transport(self, *args):
        return json.dumps({"choices": [{"message": {"content": json.dumps(self.proposal)}}]}).encode()

    def make_registry(self, artifact: dict | None):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "qualifications").mkdir()
        entries = []
        if artifact is not None:
            artifact_path = root / "qualifications" / "provider.json"
            artifact_path.write_text(json.dumps(artifact), encoding="utf-8")
            entries.append({
                "providerId": self.config["providerId"],
                "modelId": self.config["modelId"],
                "path": "qualifications/provider.json",
            })
        registry_path = root / "qualifications" / "index.json"
        registry_path.write_text(json.dumps({"schemaVersion": 1, "entries": entries}), encoding="utf-8")
        return temp, registry_path

    def test_fixture_mode_remains_backward_compatible(self):
        fixture = {"schemaVersion": 1, "providerId": "fixture:test", "response": self.proposal}
        result = runner.run(self.request, fixture)
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(result["provider"], {"kind": "fixture", "id": "fixture:test"})

    def test_direct_qualification_mode_remains_backward_compatible(self):
        result = runner.run_openai_compatible(
            self.request, self.config, self.qualification, self.benchmark, self.index,
            transport=self.fake_transport, environ={}
        )
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(result["provider"]["kind"], "openai-compatible")
        expected = dict(self.proposal, model=self.config["modelId"])
        self.assertEqual(result["proposal"], expected)

    def test_exact_registered_lookup_succeeds_with_fake_transport(self):
        temp, registry_path = self.make_registry(self.qualification)
        self.addCleanup(temp.cleanup)
        resolved = runner.resolve_qualification(
            self.config, None, registry_path, self.benchmark, self.index
        )
        result = runner.run_openai_compatible(
            self.request, self.config, resolved, self.benchmark, self.index,
            transport=self.fake_transport, environ={}
        )
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(resolved, self.qualification)

    def test_empty_registry_rejects_before_transport(self):
        temp, registry_path = self.make_registry(None)
        self.addCleanup(temp.cleanup)
        called = False
        def transport(*args):
            nonlocal called
            called = True
            return b"{}"
        with self.assertRaisesRegex(ValueError, "not registered"):
            qualification = runner.resolve_qualification(
                self.config, None, registry_path, self.benchmark, self.index
            )
            runner.run_openai_compatible(
                self.request, self.config, qualification, self.benchmark, self.index,
                transport=transport, environ={}
            )
        self.assertFalse(called)

    def test_stale_registry_rejects_before_transport(self):
        stale = dict(self.qualification, benchmarkSha256="0" * 64)
        temp, registry_path = self.make_registry(stale)
        self.addCleanup(temp.cleanup)
        with self.assertRaisesRegex(ValueError, "benchmark fingerprint"):
            runner.resolve_qualification(self.config, None, registry_path, self.benchmark, self.index)

    def test_stale_direct_qualification_rejected_before_transport(self):
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
        with self.assertRaisesRegex(ValueError, "--benchmark and --capability-index"):
            runner.validate_mode_args("openai-compatible", Path("qualification.json"), None, Path("index.json"))
        with self.assertRaisesRegex(ValueError, "exactly one"):
            runner.validate_mode_args(
                "openai-compatible",
                Path("qualification.json"),
                Path("benchmark.json"),
                Path("index.json"),
                Path("qualifications/index.json"),
            )
        with self.assertRaisesRegex(ValueError, "exactly one"):
            runner.validate_mode_args(
                "openai-compatible",
                None,
                Path("benchmark.json"),
                Path("index.json"),
                None,
            )


if __name__ == "__main__":
    unittest.main()
