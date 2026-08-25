from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import generate_repository_metadata as gen


class MetadataGenerationTests(unittest.TestCase):
    def make_root(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "skills" / "alpha").mkdir(parents=True)
        (root / "README.md").write_text(
            "# test\n\n<!-- skill-catalog:start -->\nold\n<!-- skill-catalog:end -->\n",
            encoding="utf-8",
        )
        (root / ".skill-sync.json").write_text(
            json.dumps({
                "schemaVersion": 2,
                "repository": "example/repo",
                "hashNormalization": "UTF-8; CRLF and CR converted to LF; exactly one trailing LF",
                "synchronizedAt": "2026-08-01T00:00:00Z",
                "skills": {"stale": {"files": {"SKILL.md": "deadbeef"}}},
            }) + "\n",
            encoding="utf-8",
        )
        return root

    def write_skill(self, root: Path, slug: str = "alpha", description: str = "A sufficiently long skill description for testing.") -> Path:
        path = root / "skills" / slug / "SKILL.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"---\nname: {slug}\ndescription: {description}\n---\n\n# {slug}\n", encoding="utf-8")
        return path

    def test_write_then_check_is_idempotent_and_removes_stale_entries(self) -> None:
        root = self.make_root()
        self.write_skill(root)
        self.assertEqual(gen.run(root, check=False), 0)
        readme_once = (root / "README.md").read_text(encoding="utf-8")
        manifest_once = (root / ".skill-sync.json").read_text(encoding="utf-8")
        self.assertEqual(gen.run(root, check=False), 0)
        self.assertEqual(readme_once, (root / "README.md").read_text(encoding="utf-8"))
        self.assertEqual(manifest_once, (root / ".skill-sync.json").read_text(encoding="utf-8"))
        self.assertEqual(gen.run(root, check=True), 0)
        self.assertNotIn("stale", json.loads(manifest_once)["skills"])

    def test_check_detects_stale_generated_files_without_rewriting(self) -> None:
        root = self.make_root()
        self.write_skill(root)
        before = (root / "README.md").read_text(encoding="utf-8")
        self.assertEqual(gen.run(root, check=True), 1)
        self.assertEqual(before, (root / "README.md").read_text(encoding="utf-8"))

    def test_auxiliary_file_uses_normalized_line_endings(self) -> None:
        root = self.make_root()
        self.write_skill(root)
        aux = root / "skills" / "alpha" / "references" / "guide.md"
        aux.parent.mkdir(parents=True)
        aux.write_bytes(b"one\r\ntwo\r\n\r\n")
        self.assertEqual(gen.run(root, check=False), 0)
        manifest = json.loads((root / ".skill-sync.json").read_text(encoding="utf-8"))
        expected = hashlib.sha256(b"one\ntwo\n").hexdigest()
        self.assertEqual(manifest["skills"]["alpha"]["files"]["references/guide.md"], expected)

    def test_python_bytecode_is_not_treated_as_portable_source(self) -> None:
        root = self.make_root()
        self.write_skill(root)
        script = root / "skills" / "alpha" / "scripts" / "tool.py"
        script.parent.mkdir(parents=True)
        script.write_text("print('ok')\n", encoding="utf-8")
        pycache = script.parent / "__pycache__" / "tool.cpython-312.pyc"
        pycache.parent.mkdir()
        pycache.write_bytes(b"\xcb\x00\x00\x00binary-bytecode")

        self.assertEqual(gen.run(root, check=False), 0)
        manifest = json.loads((root / ".skill-sync.json").read_text(encoding="utf-8"))
        files = manifest["skills"]["alpha"]["files"]
        self.assertIn("scripts/tool.py", files)
        self.assertNotIn("scripts/__pycache__/tool.cpython-312.pyc", files)

    def test_frontmatter_indented_lists_are_preserved(self) -> None:
        root = self.make_root()
        path = root / "skills" / "alpha" / "SKILL.md"
        path.write_text(
            "---\nname: alpha\ndescription: A sufficiently long skill description for testing.\n"
            "requires:\n  - beta\n  - gamma\noutputs:\n  - handoff.json\n---\n\n# alpha\n",
            encoding="utf-8",
        )
        parsed = gen.parse_frontmatter(path)
        self.assertEqual(parsed["requires"], ["beta", "gamma"])
        self.assertEqual(parsed["outputs"], ["handoff.json"])

    def test_malformed_frontmatter_fails_without_writing(self) -> None:
        root = self.make_root()
        path = root / "skills" / "alpha" / "SKILL.md"
        path.write_text("---\nname alpha\n---\n", encoding="utf-8")
        readme_before = (root / "README.md").read_text(encoding="utf-8")
        self.assertEqual(gen.run(root, check=False), 2)
        self.assertEqual(readme_before, (root / "README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
