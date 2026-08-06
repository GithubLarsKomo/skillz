import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_openai_plugin", ROOT / "scripts" / "build_openai_plugin.py")
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(mod)


def tree_digest(root: Path) -> str:
    h = hashlib.sha256()
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        h.update(str(path.relative_to(root)).encode())
        h.update(b"\0")
        h.update(path.read_bytes())
        h.update(b"\0")
    return h.hexdigest()


class OpenAIPluginDistributionTests(unittest.TestCase):
    def test_build_is_deterministic_and_frontmatter_is_openai_compatible(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            one = root / "one" / "skillz"
            two = root / "two" / "skillz"
            first = mod.build(one)
            second = mod.build(two)
            self.assertEqual(first, second)
            self.assertEqual(tree_digest(one), tree_digest(two))
            self.assertGreater(len(first["skills"]), 20)
            packaged = (one / "skills" / "communication-memory-governance" / "SKILL.md").read_text(encoding="utf-8")
            frontmatter = packaged.split("---", 2)[1]
            self.assertIn("name: communication-memory-governance", frontmatter)
            self.assertIn("description:", frontmatter)
            self.assertNotIn("version:", frontmatter)
            self.assertNotIn("owners:", frontmatter)
            agent_metadata = (one / "skills" / "communication-memory-governance" / "agents" / "openai.yaml").read_text(encoding="utf-8")
            self.assertIn('display_name: "Communication Memory Governance"', agent_metadata)
            self.assertIn("short_description:", agent_metadata)
            self.assertIn("allow_implicit_invocation: true", agent_metadata)
            self.assertIn("sourceSha256", first["skills"]["communication-memory-governance"]["files"]["agents/openai.yaml"])

    def test_openai_metadata_can_disable_implicit_invocation_without_changing_portable_skill_contract(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "SKILL.md"
            source.write_text(
                "---\n"
                "name: deliberate-router\n"
                "description: Route a user deliberately to the right workflow.\n"
                "userFacing: true\n"
                "implicitInvocation: false\n"
                "---\n\n"
                "# Deliberate Router\n",
                encoding="utf-8",
            )
            packaged = mod.render_openai_skill(source).decode("utf-8")
            self.assertNotIn("implicitInvocation", packaged)
            metadata = mod.render_openai_agent_metadata(source).decode("utf-8")
            self.assertIn("allow_implicit_invocation: false", metadata)
            self.assertIn('display_name: "Deliberate Router"', metadata)

    def test_openai_metadata_rejects_invalid_implicit_invocation_value(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "SKILL.md"
            source.write_text(
                "---\n"
                "name: broken\n"
                "description: Broken test skill.\n"
                "implicitInvocation: sometimes\n"
                "---\n\n"
                "# Broken\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "implicitInvocation must be true or false"):
                mod.render_openai_agent_metadata(source)

    def test_plugin_version_matches_repository_version(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "skillz"
            mod.build(out)
            plugin = json.loads((out / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
            self.assertEqual(plugin["version"], (ROOT / "VERSION").read_text(encoding="utf-8").strip())
            self.assertEqual(plugin["skills"], "./skills/")
            self.assertNotIn("apps", plugin)
            self.assertNotIn("mcpServers", plugin)

    def test_deterministic_tar_is_byte_identical(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            out = root / "skillz"
            mod.build(out)
            a = root / "a.tar"
            b = root / "b.tar"
            mod.write_deterministic_tar(out, a)
            mod.write_deterministic_tar(out, b)
            self.assertEqual(a.read_bytes(), b.read_bytes())

    def test_source_hash_drift_blocks_distribution(self):
        with tempfile.TemporaryDirectory() as td:
            source = ROOT / "skills" / "agent-handoff" / "SKILL.md"
            original = mod.source_sha(source)
            sync = mod.load_json(ROOT / ".skill-sync.json")
            self.assertEqual(original, sync["skills"]["agent-handoff"]["files"]["SKILL.md"])
            bad = dict(sync)
            bad["skills"] = dict(sync["skills"])
            bad_files = dict(sync["skills"]["agent-handoff"]["files"])
            bad_files["SKILL.md"] = "0" * 64
            bad["skills"]["agent-handoff"] = {"files": bad_files}
            old_load = mod.load_json
            try:
                mod.load_json = lambda path: bad if path == mod.SYNC else old_load(path)
                with self.assertRaisesRegex(ValueError, "source hash drift"):
                    mod.build(Path(td) / "bad")
            finally:
                mod.load_json = old_load


if __name__ == "__main__":
    unittest.main()
