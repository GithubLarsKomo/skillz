from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from skill_status import installed_identity, load_distribution_manifest, resolve_status  # noqa: E402


HEAD = "a" * 40
OLD = "b" * 40


class SkillStatusTests(unittest.TestCase):
    def test_exact_commit_match_is_current(self):
        status = resolve_status(
            repository_head=HEAD,
            repository_version="1.2.3",
            installed_commit=HEAD,
            installed_version="1.2.3",
        )
        self.assertEqual(status["status"], "current")
        self.assertTrue(status["comparisons"]["commitMatch"])

    def test_commit_mismatch_is_stale_even_if_version_matches(self):
        status = resolve_status(
            repository_head=HEAD,
            repository_version="1.2.3",
            installed_commit=OLD,
            installed_version="1.2.3",
        )
        self.assertEqual(status["status"], "stale")
        self.assertFalse(status["comparisons"]["commitMatch"])

    def test_version_mismatch_is_stale_without_commit(self):
        status = resolve_status(
            repository_head=HEAD,
            repository_version="1.2.3",
            installed_commit=None,
            installed_version="1.2.2",
        )
        self.assertEqual(status["status"], "stale")
        self.assertFalse(status["comparisons"]["versionMatch"])

    def test_same_version_without_installed_commit_is_unknown(self):
        status = resolve_status(
            repository_head=HEAD,
            repository_version="1.2.3",
            installed_commit=None,
            installed_version="1.2.3",
        )
        self.assertEqual(status["status"], "unknown")
        self.assertTrue(status["comparisons"]["versionMatch"])

    def test_distribution_manifest_exposes_version_and_source_commit(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "skillz-distribution-manifest.json"
            path.write_text(json.dumps({"pluginVersion": "1.2.3", "sourceCommit": HEAD}), encoding="utf-8")
            self.assertEqual(installed_identity(load_distribution_manifest(path)), ("1.2.3", HEAD))

    def test_short_sha_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "full 40-character"):
            resolve_status(
                repository_head="abc1234",
                repository_version="1.2.3",
                installed_commit=None,
                installed_version=None,
            )


if __name__ == "__main__":
    unittest.main()
