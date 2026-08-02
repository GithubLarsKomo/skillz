from __future__ import annotations

import hashlib
import json
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_release_bundle as release


class ReleaseBundleTests(unittest.TestCase):
    def test_beta_version_is_canonical(self):
        self.assertEqual(release.load_version(), "0.1.0-beta.1")

    def test_same_checkout_produces_identical_archive_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "first.tar"
            second = Path(tmp) / "second.tar"
            a = release.build(first)
            b = release.build(second)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(a["archiveSha256"], b["archiveSha256"])
            self.assertEqual(a["version"], "0.1.0-beta.1")

    def test_archive_manifest_hashes_every_payload_member(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive_path = Path(tmp) / "release.tar"
            result = release.build(archive_path)
            root = f"skillz-{result['version']}"
            with tarfile.open(archive_path, "r") as archive:
                members = {member.name: member for member in archive.getmembers() if member.isfile()}
                manifest_raw = archive.extractfile(members[f"{root}/release-manifest.json"]).read()
                manifest = json.loads(manifest_raw)
                self.assertEqual(manifest["version"], "0.1.0-beta.1")
                self.assertEqual(manifest["fileCount"], len(manifest["files"]))
                for rel, expected in manifest["files"].items():
                    data = archive.extractfile(members[f"{root}/{rel}"]).read()
                    self.assertEqual(hashlib.sha256(data).hexdigest(), expected)
                self.assertIn(f"{root}/scripts/bootstrap_skillz.py", members)
                self.assertIn(f"{root}/docs/BETA-RUNBOOK.md", members)
                self.assertIn(f"{root}/skills/repository-skill-bootstrap/SKILL.md", members)


if __name__ == "__main__":
    unittest.main()
