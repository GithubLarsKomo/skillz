import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "render_epub.py"
spec = importlib.util.spec_from_file_location("render_epub", SCRIPT)
render_epub = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(render_epub)


class RenderEpubTests(unittest.TestCase):
    def test_renders_navigable_epub(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "tutorial.md"
            target = root / "tutorial.epub"
            source.write_text(
                "# Testtutorial\n\n## Untertitel\n\n# Kapitel eins\n\nErster Absatz.\n\n# Kapitel zwei\n\nZweiter Absatz.\n",
                encoding="utf-8",
            )
            render_epub.render_epub(source, target, "Test", "de")
            with zipfile.ZipFile(target, "r") as zf:
                self.assertEqual(zf.namelist()[0], "mimetype")
                self.assertIn("OEBPS/nav.xhtml", zf.namelist())
                nav = zf.read("OEBPS/nav.xhtml").decode("utf-8")
                self.assertIn("Kapitel eins", nav)
                self.assertIn("Kapitel zwei", nav)

    def test_rejects_missing_chapters(self):
        with self.assertRaises(ValueError):
            render_epub.parse_markdown("# Nur ein Titel\n\nKein Kapitel.")


if __name__ == "__main__":
    unittest.main()
