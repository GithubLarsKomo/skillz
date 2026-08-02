from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_provider_promotion_bundle as bundle_builder
import prepare_registry_promotion as promotion
import qualify_model_provider as qualifier
import score_capability_interpretations as scorer


class PrepareRegistryPromotionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.benchmark = scorer.load_json(ROOT / "benchmarks/capability-interpretation-v1.json")
        cls.index = scorer.load_json(ROOT / "docs/skill-capability-index.json")
        cls.proposals = scorer.load_json(ROOT / "benchmarks/capability-interpretation-baseline-v1.json")

    def make_repo_and_bundle(self):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        repo = root / "repo"
        bundle_dir = root / "bundle"
        (repo / "providers").mkdir(parents=True)
        (repo / "qualifications").mkdir(parents=True)
        (repo / "benchmarks").mkdir(parents=True)
        (repo / "docs").mkdir(parents=True)
        (repo / "providers" / "index.json").write_text('{"schemaVersion":1,"entries":[]}\n', encoding="utf-8")
        (repo / "qualifications" / "index.json").write_text('{"schemaVersion":1,"entries":[]}\n', encoding="utf-8")
        shutil.copy2(ROOT / "benchmarks/capability-interpretation-v1.json", repo / "benchmarks" / "capability-interpretation-v1.json")
        shutil.copy2(ROOT / "docs/skill-capability-index.json", repo / "docs" / "skill-capability-index.json")
        config = {
            "schemaVersion": 1,
            "providerId": "promotion-test",
            "endpoint": "https://provider.example/v1/chat/completions",
            "modelId": "promotion-model",
            "apiKeyEnv": "CAPABILITY_PROVIDER_API_KEY",
            "timeoutSeconds": 60,
        }
        qualification = qualifier.qualify(
            config["providerId"], config["modelId"], self.benchmark, self.proposals, self.index, config
        )
        bundle_builder.write_bundle(bundle_builder.build_bundle(config, qualification), bundle_dir)
        return temp, repo, bundle_dir

    def test_dry_run_is_deterministic_and_writes_nothing(self):
        temp, repo, bundle_dir = self.make_repo_and_bundle()
        with temp:
            before_provider = (repo / "providers" / "index.json").read_bytes()
            before_qualification = (repo / "qualifications" / "index.json").read_bytes()
            first = promotion.prepare(bundle_dir, repo)
            second = promotion.prepare(bundle_dir, repo)
            self.assertEqual(promotion.public_plan(first, False), promotion.public_plan(second, False))
            self.assertEqual(promotion.public_plan(first, False)["status"], "dry-run")
            self.assertEqual((repo / "providers" / "index.json").read_bytes(), before_provider)
            self.assertEqual((repo / "qualifications" / "index.json").read_bytes(), before_qualification)
            self.assertFalse((repo / first["providerPath"]).exists())
            self.assertFalse((repo / first["qualificationPath"]).exists())

    def test_apply_writes_and_verifies_exact_pair(self):
        temp, repo, bundle_dir = self.make_repo_and_bundle()
        with temp:
            plan = promotion.prepare(bundle_dir, repo)
            result = promotion.apply(plan, repo)
            self.assertEqual(result["status"], "applied")
            self.assertTrue((repo / plan["providerPath"]).exists())
            self.assertTrue((repo / plan["qualificationPath"]).exists())
            provider_index = json.loads((repo / "providers" / "index.json").read_text(encoding="utf-8"))
            qualification_index = json.loads((repo / "qualifications" / "index.json").read_text(encoding="utf-8"))
            self.assertEqual(provider_index["entries"], [plan["providerEntry"]])
            self.assertEqual(qualification_index["entries"], [plan["qualificationEntry"]])

    def test_duplicate_identity_is_rejected(self):
        temp, repo, bundle_dir = self.make_repo_and_bundle()
        with temp:
            plan = promotion.prepare(bundle_dir, repo)
            promotion.apply(plan, repo)
            with self.assertRaisesRegex(ValueError, "already registered"):
                promotion.prepare(bundle_dir, repo)

    def test_stale_capability_index_evidence_is_rejected(self):
        temp, repo, bundle_dir = self.make_repo_and_bundle()
        with temp:
            index = json.loads((repo / "docs" / "skill-capability-index.json").read_text(encoding="utf-8"))
            index["skillCount"] = index.get("skillCount", 0) + 1
            (repo / "docs" / "skill-capability-index.json").write_text(json.dumps(index), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "capability-index fingerprint"):
                promotion.prepare(bundle_dir, repo)

    def test_unsafe_identity_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "providerId must match"):
            promotion.safe_identity("provider/escape", "providerId")
        with self.assertRaisesRegex(ValueError, "modelId must match"):
            promotion.safe_identity("../model", "modelId")

    def test_post_write_failure_rolls_back_all_four_files(self):
        temp, repo, bundle_dir = self.make_repo_and_bundle()
        with temp:
            plan = promotion.prepare(bundle_dir, repo)
            provider_index_before = (repo / "providers" / "index.json").read_bytes()
            qualification_index_before = (repo / "qualifications" / "index.json").read_bytes()
            with mock.patch.object(promotion, "verify_applied", side_effect=ValueError("synthetic verification failure")):
                with self.assertRaisesRegex(ValueError, "rolled back"):
                    promotion.apply(plan, repo)
            self.assertEqual((repo / "providers" / "index.json").read_bytes(), provider_index_before)
            self.assertEqual((repo / "qualifications" / "index.json").read_bytes(), qualification_index_before)
            self.assertFalse((repo / plan["providerPath"]).exists())
            self.assertFalse((repo / plan["qualificationPath"]).exists())


if __name__ == "__main__":
    unittest.main()
