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

import bootstrap_skillz as bootstrap


class BootstrapSkillzTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = bootstrap.load_manifest()

    def test_source_manifest_verifies(self):
        bootstrap.verify_source(self.manifest)

    def test_selected_skill_installs_only_manifest_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "installed"
            result = bootstrap.install(self.manifest, target, ["repository-skill-bootstrap"])
            self.assertEqual([item["name"] for item in result["installed"]], ["repository-skill-bootstrap"])
            expected = set(self.manifest["skills"]["repository-skill-bootstrap"]["files"])
            actual = {path.relative_to(target / "repository-skill-bootstrap").as_posix() for path in (target / "repository-skill-bootstrap").rglob("*") if path.is_file()}
            self.assertEqual(actual, expected)
            for rel, digest in self.manifest["skills"]["repository-skill-bootstrap"]["files"].items():
                self.assertEqual(bootstrap.sha256(target / "repository-skill-bootstrap" / rel), digest)

    def test_unknown_skill_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "unknown skill"):
                bootstrap.install(self.manifest, Path(tmp), ["does-not-exist"])

    def test_duplicate_selection_is_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = bootstrap.install(self.manifest, Path(tmp), ["agent-handoff", "agent-handoff"])
            self.assertEqual([item["name"] for item in result["installed"]], ["agent-handoff"])


if __name__ == "__main__":
    unittest.main()
