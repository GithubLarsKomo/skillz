from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from query_capabilities import main  # noqa: E402


HEAD = "a" * 40
OLD = "b" * 40
INDEX = {"schemaVersion": 1, "skills": []}


class CapabilityStatusCliTests(unittest.TestCase):
    def write_index(self, root: Path) -> Path:
        path = root / "index.json"
        path.write_text(json.dumps(INDEX), encoding="utf-8")
        return path

    def run_json(self, args: list[str]) -> tuple[int, dict]:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = main(args + ["--json"])
        return code, json.loads(output.getvalue())

    def test_skills_status_reports_current_for_exact_commit(self):
        with tempfile.TemporaryDirectory() as tmp:
            index = self.write_index(Path(tmp))
            code, payload = self.run_json([
                "--index", str(index),
                "--skills", "status",
                "--repository-head", HEAD,
                "--repository-version", "1.2.3",
                "--installed-commit", HEAD,
                "--installed-version", "1.2.3",
            ])
            self.assertEqual(code, 0)
            self.assertEqual(payload["status"], "current")

    def test_skills_status_reads_installed_distribution_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            index = self.write_index(root)
            manifest = root / "skillz-distribution-manifest.json"
            manifest.write_text(json.dumps({"pluginVersion": "1.2.3", "sourceCommit": OLD}), encoding="utf-8")
            code, payload = self.run_json([
                "--index", str(index),
                "--skills", "status",
                "--repository-head", HEAD,
                "--repository-version", "1.2.3",
                "--installed-manifest", str(manifest),
            ])
            self.assertEqual(code, 0)
            self.assertEqual(payload["status"], "stale")
            self.assertEqual(payload["installed"]["commit"], OLD)


if __name__ == "__main__":
    unittest.main()
