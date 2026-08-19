from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_openai_plugin", ROOT / "scripts" / "build_openai_plugin.py")
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(mod)

COMMIT = "d" * 40


class OpenAIPluginProvenanceTests(unittest.TestCase):
    def test_explicit_source_commit_is_stamped(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = mod.build(Path(tmp) / "skillz", source_commit=COMMIT)
            self.assertEqual(manifest["sourceCommit"], COMMIT)

    def test_default_build_remains_unstamped_and_deterministic_contract_compatible(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = mod.build(Path(tmp) / "skillz")
            self.assertNotIn("sourceCommit", manifest)

    def test_invalid_source_commit_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "full 40-character"):
                mod.build(Path(tmp) / "skillz", source_commit="deadbeef")


if __name__ == "__main__":
    unittest.main()
