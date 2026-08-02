from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import provider_qualification_config as provider_config_contract
import qualify_model_provider as qualifier


class ProviderQualificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.benchmark = json.loads((ROOT / "benchmarks/capability-interpretation-v1.json").read_text(encoding="utf-8"))
        cls.proposals = json.loads((ROOT / "benchmarks/capability-interpretation-baseline-v1.json").read_text(encoding="utf-8"))
        cls.index = json.loads((ROOT / "docs/skill-capability-index.json").read_text(encoding="utf-8"))
        cls.config = {
            "schemaVersion": 1,
            "providerId": "openai-compatible:test",
            "endpoint": "https://provider.example/v1/chat/completions",
            "modelId": "fixture-model",
            "apiKeyEnv": "TEST_PROVIDER_KEY",
            "timeoutSeconds": 30,
        }

    def test_known_baseline_qualifies(self):
        result = qualifier.qualify("fixture", "fixture-model", self.benchmark, self.proposals, self.index)
        self.assertTrue(result["qualified"])
        self.assertEqual(result["schemaVersion"], 2)
        self.assertEqual(result["failedCount"], 0)
        self.assertEqual(result["passedCount"], result["caseCount"])
        self.assertEqual(len(result["providerConfigSha256"]), 64)

    def test_failed_baseline_is_not_qualified(self):
        proposals = copy.deepcopy(self.proposals)
        proposals["proposals"][0]["proposal"]["intent"]["desiredOutputs"] = []
        result = qualifier.qualify("fixture", "fixture-model", self.benchmark, proposals, self.index)
        self.assertFalse(result["qualified"])
        self.assertGreater(result["failedCount"], 0)

    def test_fingerprints_change_with_content(self):
        baseline = qualifier.qualify("fixture", "fixture-model", self.benchmark, self.proposals, self.index)
        changed_benchmark = copy.deepcopy(self.benchmark)
        changed_benchmark["cases"][0]["sourceText"] += " changed"
        changed = qualifier.qualify("fixture", "fixture-model", changed_benchmark, self.proposals, self.index)
        self.assertNotEqual(baseline["benchmarkSha256"], changed["benchmarkSha256"])
        changed_index = copy.deepcopy(self.index)
        changed_index["skills"][0]["description"] += " changed"
        changed2 = qualifier.qualify("fixture", "fixture-model", self.benchmark, self.proposals, changed_index)
        self.assertNotEqual(baseline["capabilityIndexSha256"], changed2["capabilityIndexSha256"])

    def test_provider_config_fingerprint_changes_with_endpoint_timeout_and_auth_mode(self):
        baseline = qualifier.qualify(
            self.config["providerId"], self.config["modelId"], self.benchmark, self.proposals, self.index,
            provider_config=self.config,
        )
        endpoint_changed = qualifier.qualify(
            self.config["providerId"], self.config["modelId"], self.benchmark, self.proposals, self.index,
            provider_config=dict(self.config, endpoint="https://other.example/v1/chat/completions"),
        )
        timeout_changed = qualifier.qualify(
            self.config["providerId"], self.config["modelId"], self.benchmark, self.proposals, self.index,
            provider_config=dict(self.config, timeoutSeconds=31),
        )
        auth_changed = qualifier.qualify(
            self.config["providerId"], self.config["modelId"], self.benchmark, self.proposals, self.index,
            provider_config=dict(self.config, apiKeyEnv=None),
        )
        self.assertNotEqual(baseline["providerConfigSha256"], endpoint_changed["providerConfigSha256"])
        self.assertNotEqual(baseline["providerConfigSha256"], timeout_changed["providerConfigSha256"])
        self.assertNotEqual(baseline["providerConfigSha256"], auth_changed["providerConfigSha256"])

    def test_credential_value_is_not_part_of_config_fingerprint(self):
        first = provider_config_contract.fingerprint(self.config["providerId"], self.config["modelId"], self.config)
        second = provider_config_contract.fingerprint(self.config["providerId"], self.config["modelId"], dict(self.config))
        self.assertEqual(first, second)
        projection = provider_config_contract.projection(self.config["providerId"], self.config["modelId"], self.config)
        self.assertNotIn("secret-token", json.dumps(projection))
        self.assertEqual(projection["auth"]["environmentVariable"], "TEST_PROVIDER_KEY")

    def test_byte_stable(self):
        first = qualifier.render_json(qualifier.qualify("fixture", "fixture-model", self.benchmark, self.proposals, self.index))
        second = qualifier.render_json(qualifier.qualify("fixture", "fixture-model", self.benchmark, self.proposals, self.index))
        self.assertEqual(first, second)

    def test_malformed_index_fails(self):
        bad = copy.deepcopy(self.index)
        bad["schemaVersion"] = 999
        with self.assertRaisesRegex(ValueError, "unsupported capability index schemaVersion"):
            qualifier.qualify("fixture", "fixture-model", self.benchmark, self.proposals, bad)


if __name__ == "__main__":
    unittest.main()
