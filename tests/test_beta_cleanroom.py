from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BetaCleanRoomTests(unittest.TestCase):
    def test_fresh_checkout_installs_and_runs_portable_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            installed = root / "installed-skills"
            project = root / "fresh-project"
            project.mkdir()
            (project / ".git").mkdir()

            install = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "bootstrap_skillz.py"),
                    "--target-dir",
                    str(installed),
                    "--skill",
                    "repository-skill-bootstrap",
                    "--skip-repo-validation",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )
            self.assertEqual(install.returncode, 0, install.stderr or install.stdout)

            helper = installed / "repository-skill-bootstrap" / "scripts" / "bootstrap_repository_context.py"
            self.assertTrue(helper.is_file())
            run = subprocess.run(
                [
                    sys.executable,
                    str(helper),
                    "--repo",
                    str(project),
                    "--project-name",
                    "Clean Room Beta Project",
                ],
                text=True,
                capture_output=True,
            )
            self.assertEqual(run.returncode, 0, run.stderr or run.stdout)

            context_dir = project / "docs" / "agents"
            expected = {"CONFIG.md", "CONTEXT.md", "DECISIONS.md"}
            self.assertEqual({p.name for p in context_dir.iterdir() if p.is_file()}, expected)
            self.assertIn("Clean Room Beta Project", (context_dir / "CONFIG.md").read_text(encoding="utf-8"))

            rerun = subprocess.run(
                [
                    sys.executable,
                    str(helper),
                    "--repo",
                    str(project),
                    "--project-name",
                    "Clean Room Beta Project",
                ],
                text=True,
                capture_output=True,
            )
            self.assertEqual(rerun.returncode, 3)
            self.assertIn("refusing to overwrite", rerun.stderr)


if __name__ == "__main__":
    unittest.main()
