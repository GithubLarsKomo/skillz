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

import qualification_registry as registry
import qualify_model_provider as qualifier
from score_capability_interpretations import load_json


class QualificationRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.benchmark = load_json(ROOT / "benchmarks" / "capability-interpretation-v1.json")
        cls.proposals = load_json(ROOT / "benchmarks" / "capability-interpretation-baseline-v1.json")
        cls.index = load_json(ROOT / "docs" / "skill-capability-index.json")

    def make_repo(self, entries):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "qualifications").mkdir()
        index_path = root / "qualifications" / "index.json"
        index_path.write_text(json.dumps({"schemaVersion": 1, "entries": entries}), encoding="utf-8")
        return temp, root, index_path

    def artifact(self, provider_id="provider:test", model_id="model:test"):
        return qualifier.qualify(provider_id, model_id, self.benchmark, self.proposals, self.index)

    def test_empty_registry_is_valid(self):
        temp, root, index_path = self.make_repo([])
        self.addCleanup(temp.cleanup)
        result = registry.verify(index_path, self.benchmark, self.index)
        self.assertEqual(result, {"schemaVersion": 1, "entryCount": 0, "entries": []})

    def test_valid_entry_verifies_and_looks_up_exact_identity(self):
        entry = {"providerId": "provider:test", "modelId": "model:test", "path": "qualifications/provider-test.json"}
        temp, root, index_path = self.make_repo([entry])
        self.addCleanup(temp.cleanup)
        artifact = self.artifact()
        (root / entry["path"]).write_text(json.dumps(artifact), encoding="utf-8")
        verified = registry.verify(index_path, self.benchmark, self.index)
        self.assertEqual(verified["entryCount"], 1)
        looked_up = registry.lookup(index_path, "provider:test", "model:test", self.benchmark, self.index)
        self.assertEqual(looked_up, artifact)

    def test_stale_benchmark_is_rejected(self):
        entry = {"providerId": "provider:test", "modelId": "model:test", "path": "qualifications/provider-test.json"}
        temp, root, index_path = self.make_repo([entry])
        self.addCleanup(temp.cleanup)
        artifact = dict(self.artifact(), benchmarkSha256="0" * 64)
        (root / entry["path"]).write_text(json.dumps(artifact), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "benchmark fingerprint"):
            registry.verify(index_path, self.benchmark, self.index)

    def test_stale_capability_index_is_rejected(self):
        entry = {"providerId": "provider:test", "modelId": "model:test", "path": "qualifications/provider-test.json"}
        temp, root, index_path = self.make_repo([entry])
        self.addCleanup(temp.cleanup)
        artifact = dict(self.artifact(), capabilityIndexSha256="0" * 64)
        (root / entry["path"]).write_text(json.dumps(artifact), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "capability-index fingerprint"):
            registry.verify(index_path, self.benchmark, self.index)

    def test_duplicate_identity_is_rejected(self):
        entries = [
            {"providerId": "provider:test", "modelId": "model:test", "path": "qualifications/a.json"},
            {"providerId": "provider:test", "modelId": "model:test", "path": "qualifications/b.json"},
        ]
        temp, root, index_path = self.make_repo(entries)
        self.addCleanup(temp.cleanup)
        artifact = self.artifact()
        (root / "qualifications" / "a.json").write_text(json.dumps(artifact), encoding="utf-8")
        (root / "qualifications" / "b.json").write_text(json.dumps(artifact), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "duplicate qualification identity"):
            registry.verify(index_path, self.benchmark, self.index)

    def test_unqualified_artifact_is_rejected(self):
        entry = {"providerId": "provider:test", "modelId": "model:test", "path": "qualifications/provider-test.json"}
        temp, root, index_path = self.make_repo([entry])
        self.addCleanup(temp.cleanup)
        artifact = dict(self.artifact(), qualified=False)
        (root / entry["path"]).write_text(json.dumps(artifact), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "not qualified"):
            registry.verify(index_path, self.benchmark, self.index)

    def test_lookup_unknown_identity_fails(self):
        temp, root, index_path = self.make_repo([])
        self.addCleanup(temp.cleanup)
        with self.assertRaisesRegex(ValueError, "not registered"):
            registry.lookup(index_path, "missing", "model", self.benchmark, self.index)


if __name__ == "__main__":
    unittest.main()
