from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from skillz_core import read_utf8_text, safe_relative_path


class MCPResourcePathPolicyTests(unittest.TestCase):
    def test_allows_normal_relative_path(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            target = root / "nested" / "file.txt"
            target.parent.mkdir()
            target.write_text("hello", encoding="utf-8")
            self.assertEqual(safe_relative_path(root, "nested/file.txt"), target.resolve())
            self.assertEqual(read_utf8_text(root, "nested/file.txt"), "hello")

    def test_rejects_traversal_and_encoded_traversal(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for value in ("../secret", "%2e%2e/secret", "%252e%252e/secret", "a/../secret"):
                with self.subTest(value=value):
                    with self.assertRaises(ValueError):
                        safe_relative_path(root, value)

    def test_rejects_absolute_windows_backslash_and_nul_paths(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for value in ("/etc/passwd", "C:/Windows/System32", r"..\secret", "bad\x00name"):
                with self.subTest(value=value):
                    with self.assertRaises(ValueError):
                        safe_relative_path(root, value)

    @unittest.skipIf(os.name == "nt", "symlink creation semantics differ on Windows runners")
    def test_rejects_symlink_escape(self) -> None:
        with tempfile.TemporaryDirectory() as td, tempfile.TemporaryDirectory() as outside_td:
            root = Path(td)
            outside = Path(outside_td)
            (outside / "secret.txt").write_text("secret", encoding="utf-8")
            (root / "escape").symlink_to(outside, target_is_directory=True)
            with self.assertRaises(ValueError):
                safe_relative_path(root, "escape/secret.txt")

    def test_enforces_text_size_limit_and_utf8(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "large.txt").write_text("abcd", encoding="utf-8")
            with self.assertRaises(ValueError):
                read_utf8_text(root, "large.txt", max_bytes=3)
            (root / "binary.bin").write_bytes(b"\xff\xfe")
            with self.assertRaises(ValueError):
                read_utf8_text(root, "binary.bin")


if __name__ == "__main__":
    unittest.main()
