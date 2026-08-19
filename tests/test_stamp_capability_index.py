from __future__ import annotations

import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from stamp_capability_index import stamp_index  # noqa: E402


COMMIT = "c" * 40


class CapabilityIndexStampTests(unittest.TestCase):
    def test_stamp_adds_exact_runtime_provenance_without_mutating_source(self):
        source = {"schemaVersion": 1, "skills": []}
        stamped = stamp_index(
            source,
            repository="GithubLarsKomo/skillz",
            ref="main",
            version="0.1.0-beta.1",
            commit_sha=COMMIT,
        )
        self.assertNotIn("provenance", source)
        self.assertEqual(stamped["provenance"], {
            "repository": "GithubLarsKomo/skillz",
            "ref": "main",
            "version": "0.1.0-beta.1",
            "commitSha": COMMIT,
        })

    def test_invalid_commit_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "full 40-character"):
            stamp_index(
                {"schemaVersion": 1, "skills": []},
                repository="GithubLarsKomo/skillz",
                ref="main",
                version="0.1.0-beta.1",
                commit_sha="deadbeef",
            )


if __name__ == "__main__":
    unittest.main()
