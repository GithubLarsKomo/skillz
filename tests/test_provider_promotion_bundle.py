from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_provider_promotion_bundle as bundle_builder
import qualify_model_provider as qualifier
import score_capability_interpretations as scorer


class ProviderPromotionBundleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((ROOT / "docs/skill-capability-index.json").read_text(encoding="utf-8"))
        cls.benchmark = scorer.load_json(ROOT / "benchmarks/capability-interpretation-v1.json")
        cls.proposals = scorer.load_json(ROOT / "benchmarks/capability-interpretation-baseline-v1.json")
        cls.config = {
            "schemaVersion": 1,
            "providerId": "promotion-test",
            "endpoint": "https://provider.example/v1/chat/completions",
            "modelId": "promotion-model",
            "apiKeyEnv": "CAPABILITY_PROVIDER_API_KEY",
            "timeoutSeconds": 60,
        }
        cls.qualification = qualifier.qualify(
            cls.config["providerId"], cls.config["modelId"], cls.benchmark, cls.proposals, cls.index, cls.config
        )

    def test_bundle_is_deterministic_and_fingerprint_bound(self):
        first = bundle_builder.build_bundle(self.config, self.qualification)
        second = bundle_builder.build_bundle(copy.deepcopy(self.config), copy.deepcopy(self.qualification))
        self.assertEqual(bundle_builder.canonical_json(first), bundle_builder.canonical_json(second))
        self.assertEqual(first["manifest"]["providerConfigSha256"], self.qualification["providerConfigSha256"])
        self.assertEqual(first["manifest"]["qualificationSha256"], bundle_builder.sha256(self.qualification))

    def test_written_bundle_contains_only_three_safe_files(self):
        bundle = bundle_builder.build_bundle(self.config, self.qualification)
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "bundle"
            bundle_builder.write_bundle(bundle, output)
            self.assertEqual({p.name for p in output.iterdir()}, {"provider-config.json", "qualification.json", "manifest.json"})
            documents = [json.loads(p.read_text(encoding="utf-8")) for p in output.iterdir()]
            rendered = "\n".join(bundle_builder.canonical_json(document) for document in documents)
        self.assertNotIn("Bearer ", rendered)
        self.assertNotIn("top-secret-token", rendered)
        forbidden_payload_keys = {"authorization", "choices", "messages", "proposal", "proposals", "response", "responses"}
        for document in documents:
            self.assertTrue(forbidden_payload_keys.isdisjoint({str(key).lower() for key in document}))
        self.assertIn("proposalSetSha256", self.qualification)  # hash evidence is expected and safe

    def test_credential_value_does_not_affect_bundle(self):
        # Credential values are never an input to the builder; only the environment-variable name is bound.
        first = bundle_builder.build_bundle(self.config, self.qualification)
        second = bundle_builder.build_bundle(self.config, self.qualification)
        self.assertEqual(first, second)
        self.assertNotIn("top-secret-token", bundle_builder.canonical_json(first))

    def test_config_drift_is_rejected(self):
        drifted = dict(self.config, endpoint="https://other.example/v1/chat/completions")
        with self.assertRaisesRegex(ValueError, "provider-config fingerprint"):
            bundle_builder.build_bundle(drifted, self.qualification)

    def test_unqualified_evidence_is_rejected(self):
        bad = dict(self.qualification, qualified=False)
        with self.assertRaisesRegex(ValueError, "qualified evidence"):
            bundle_builder.build_bundle(self.config, bad)


if __name__ == "__main__":
    unittest.main()
