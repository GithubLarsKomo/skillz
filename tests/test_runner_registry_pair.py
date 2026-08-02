from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_model_interpretation_request as request_builder
import qualify_model_provider as qualifier
import run_model_capability_pipeline as pipeline
import run_model_interpretation as runner
import score_capability_interpretations as scorer


class RegistryPairRunnerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((ROOT / "docs/skill-capability-index.json").read_text(encoding="utf-8"))
        cls.benchmark = scorer.load_json(ROOT / "benchmarks/capability-interpretation-v1.json")
        cls.proposals = scorer.load_json(ROOT / "benchmarks/capability-interpretation-baseline-v1.json")
        cls.proposal = cls.proposals["proposals"][0]["proposal"]
        cls.request = request_builder.build_request("Create the review decision artifact.", cls.index)
        cls.config = {
            "schemaVersion": 1,
            "providerId": "registry-provider",
            "endpoint": "http://127.0.0.1:11434/v1/chat/completions",
            "modelId": "registry-model",
            "apiKeyEnv": None,
            "timeoutSeconds": 5,
        }
        cls.qualification = qualifier.qualify(
            cls.config["providerId"], cls.config["modelId"], cls.benchmark, cls.proposals, cls.index, cls.config
        )

    def review(self):
        return {
            "schemaVersion": 1,
            "decision": "approved",
            "reviewer": "reviewer-1",
            "reasons": ["checked structured interpretation"],
        }

    def fake_transport(self, endpoint, body, headers, timeout):
        payload = {"choices": [{"message": {"content": json.dumps(self.proposal)}}]}
        return json.dumps(payload).encode("utf-8")

    def make_registries(self, *, config=True, qualification=True, drift=False):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "providers").mkdir()
        (root / "qualifications").mkdir()
        provider_entries = []
        qualification_entries = []
        if config:
            provider_config = dict(self.config)
            if drift:
                provider_config["endpoint"] = "http://127.0.0.1:9999/v1/chat/completions"
            (root / "providers/provider.json").write_text(json.dumps(provider_config), encoding="utf-8")
            provider_entries.append({"providerId": self.config["providerId"], "modelId": self.config["modelId"], "path": "providers/provider.json"})
        if qualification:
            (root / "qualifications/provider.json").write_text(json.dumps(self.qualification), encoding="utf-8")
            qualification_entries.append({"providerId": self.config["providerId"], "modelId": self.config["modelId"], "path": "qualifications/provider.json"})
        provider_registry = root / "providers/index.json"
        qualification_registry = root / "qualifications/index.json"
        provider_registry.write_text(json.dumps({"schemaVersion": 1, "entries": provider_entries}), encoding="utf-8")
        qualification_registry.write_text(json.dumps({"schemaVersion": 1, "entries": qualification_entries}), encoding="utf-8")
        return temp, provider_registry, qualification_registry

    def test_exact_pair_runs_model_with_fake_transport(self):
        temp, providers, qualifications = self.make_registries()
        self.addCleanup(temp.cleanup)
        config, qualification = runner.resolve_registry_pair(
            providers, qualifications, self.config["providerId"], self.config["modelId"], self.benchmark, self.index
        )
        result = runner.run_openai_compatible(
            self.request, config, qualification, self.benchmark, self.index, transport=self.fake_transport, environ={}
        )
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(result["provider"]["id"], self.config["providerId"])

    def test_full_pipeline_pair_requires_human_review(self):
        temp, providers, qualifications = self.make_registries()
        self.addCleanup(temp.cleanup)
        result = pipeline.run(
            "Create the review decision artifact.", None, None, pipeline.DEFAULT_INDEX,
            provider_mode="openai-compatible",
            provider_registry=providers,
            qualification_registry=qualifications,
            provider_id=self.config["providerId"],
            model_id=self.config["modelId"],
            benchmark=self.benchmark,
            transport=self.fake_transport,
        )
        self.assertEqual(result["failedStage"], "review-admission")
        self.assertIsNone(result["resolverOutput"])

    def test_full_pipeline_pair_resolves_after_review(self):
        temp, providers, qualifications = self.make_registries()
        self.addCleanup(temp.cleanup)
        result = pipeline.run(
            "Create the review decision artifact.", None, self.review(), pipeline.DEFAULT_INDEX,
            provider_mode="openai-compatible",
            provider_registry=providers,
            qualification_registry=qualifications,
            provider_id=self.config["providerId"],
            model_id=self.config["modelId"],
            benchmark=self.benchmark,
            transport=self.fake_transport,
        )
        self.assertEqual(result["status"], "resolved")
        self.assertGreaterEqual(result["resolverOutput"]["candidateCount"], 1)

    def test_empty_provider_registry_blocks_before_transport(self):
        temp, providers, qualifications = self.make_registries(config=False)
        self.addCleanup(temp.cleanup)
        called = False
        def transport(*args):
            nonlocal called
            called = True
            return b"{}"
        result = pipeline.run(
            "Create the review decision artifact.", None, self.review(), pipeline.DEFAULT_INDEX,
            provider_mode="openai-compatible", provider_registry=providers, qualification_registry=qualifications,
            provider_id=self.config["providerId"], model_id=self.config["modelId"], benchmark=self.benchmark, transport=transport,
        )
        self.assertEqual(result["failedStage"], "provider-run")
        self.assertIn("not registered", result["error"])
        self.assertFalse(called)

    def test_empty_qualification_registry_blocks_before_transport(self):
        temp, providers, qualifications = self.make_registries(qualification=False)
        self.addCleanup(temp.cleanup)
        called = False
        def transport(*args):
            nonlocal called
            called = True
            return b"{}"
        result = pipeline.run(
            "Create the review decision artifact.", None, self.review(), pipeline.DEFAULT_INDEX,
            provider_mode="openai-compatible", provider_registry=providers, qualification_registry=qualifications,
            provider_id=self.config["providerId"], model_id=self.config["modelId"], benchmark=self.benchmark, transport=transport,
        )
        self.assertEqual(result["failedStage"], "provider-run")
        self.assertIn("not registered", result["error"])
        self.assertFalse(called)

    def test_config_drift_blocks_before_transport(self):
        temp, providers, qualifications = self.make_registries(drift=True)
        self.addCleanup(temp.cleanup)
        with self.assertRaisesRegex(ValueError, "provider-config fingerprint"):
            runner.resolve_registry_pair(
                providers, qualifications, self.config["providerId"], self.config["modelId"], self.benchmark, self.index
            )

    def test_cli_pair_conflict_is_explicit(self):
        args = SimpleNamespace(
            provider_mode="openai-compatible",
            provider_input="provider.json",
            qualification=Path("qualification.json"),
            qualification_registry=Path("qualifications/index.json"),
            provider_registry=Path("providers/index.json"),
            provider_id=self.config["providerId"],
            model_id=self.config["modelId"],
            benchmark=Path("benchmark.json"),
            capability_index=Path("index.json"),
        )
        with self.assertRaisesRegex(ValueError, "mutually exclusive"):
            runner.validate_registry_pair_args(args)


if __name__ == "__main__":
    unittest.main()
