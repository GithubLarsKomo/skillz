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

import provider_config_registry as registry
import qualify_model_provider as qualifier


class ProviderConfigRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.benchmark = json.loads((ROOT / "benchmarks/capability-interpretation-v1.json").read_text(encoding="utf-8"))
        cls.proposals = json.loads((ROOT / "benchmarks/capability-interpretation-baseline-v1.json").read_text(encoding="utf-8"))
        cls.index = json.loads((ROOT / "docs/skill-capability-index.json").read_text(encoding="utf-8"))
        cls.config = {
            "schemaVersion": 1,
            "providerId": "local-openai",
            "endpoint": "http://127.0.0.1:11434/v1/chat/completions",
            "modelId": "fixture-model",
            "apiKeyEnv": None,
            "timeoutSeconds": 5,
        }
        cls.qualification = qualifier.qualify(
            "local-openai", "fixture-model", cls.benchmark, cls.proposals, cls.index, provider_config=cls.config
        )

    def make_root(self, entries=None, config=None, qualification=None):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "providers").mkdir()
        (root / "qualifications").mkdir()
        entries = [] if entries is None else entries
        (root / "providers" / "index.json").write_text(json.dumps({"schemaVersion": 1, "entries": entries}), encoding="utf-8")
        if config is not None:
            (root / "providers" / "local.json").write_text(json.dumps(config), encoding="utf-8")
        q_entries = []
        if qualification is not None:
            (root / "qualifications" / "local.json").write_text(json.dumps(qualification), encoding="utf-8")
            q_entries.append({"providerId": "local-openai", "modelId": "fixture-model", "path": "qualifications/local.json"})
        (root / "qualifications" / "index.json").write_text(json.dumps({"schemaVersion": 1, "entries": q_entries}), encoding="utf-8")
        return temp, root

    def entry(self):
        return {"providerId": "local-openai", "modelId": "fixture-model", "path": "providers/local.json"}

    def test_empty_registry_is_valid(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        result = registry.verify(root / "providers" / "index.json")
        self.assertEqual(result["entryCount"], 0)

    def test_exact_lookup_returns_valid_config(self):
        temp, root = self.make_root([self.entry()], self.config)
        self.addCleanup(temp.cleanup)
        result = registry.lookup(root / "providers" / "index.json", "local-openai", "fixture-model")
        self.assertEqual(result, self.config)

    def test_duplicate_identity_rejected(self):
        temp, root = self.make_root([self.entry(), self.entry()], self.config)
        self.addCleanup(temp.cleanup)
        with self.assertRaisesRegex(ValueError, "duplicate provider config identity"):
            registry.verify(root / "providers" / "index.json")

    def test_unknown_secret_field_rejected(self):
        bad = dict(self.config, apiKey="secret-token")
        temp, root = self.make_root([self.entry()], bad)
        self.addCleanup(temp.cleanup)
        with self.assertRaisesRegex(ValueError, "invalid fields"):
            registry.verify(root / "providers" / "index.json")

    def test_pair_resolution_succeeds_when_config_matches_qualification(self):
        temp, root = self.make_root([self.entry()], self.config, self.qualification)
        self.addCleanup(temp.cleanup)
        config, qualification = registry.resolve_pair(
            root / "providers" / "index.json",
            root / "qualifications" / "index.json",
            "local-openai", "fixture-model", self.benchmark, self.index,
        )
        self.assertEqual(config, self.config)
        self.assertEqual(qualification, self.qualification)

    def test_pair_resolution_rejects_config_drift(self):
        changed = dict(self.config, endpoint="http://127.0.0.1:9999/v1/chat/completions")
        temp, root = self.make_root([self.entry()], changed, self.qualification)
        self.addCleanup(temp.cleanup)
        with self.assertRaisesRegex(ValueError, "provider-config fingerprint"):
            registry.resolve_pair(
                root / "providers" / "index.json",
                root / "qualifications" / "index.json",
                "local-openai", "fixture-model", self.benchmark, self.index,
            )


if __name__ == "__main__":
    unittest.main()
