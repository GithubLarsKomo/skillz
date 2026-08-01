from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_dependency_graph import build_graph, render_json, run  # noqa: E402


SKILL = """---\nname: {name}\ndescription: A sufficiently long description for dependency graph testing.\nrequires:\n{requires}outputs:\n{outputs}---\n\n## Trigger\nTest.\n"""


def write_skill(root: Path, name: str, requires: list[str] | None = None, outputs: list[str] | None = None) -> None:
    path = root / "skills" / name / "SKILL.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    req = "".join(f"  - {item}\n" for item in (requires or [])) or "  []\n"
    out = "".join(f"  - {item}\n" for item in (outputs or [])) or "  []\n"
    path.write_text(SKILL.format(name=name, requires=req, outputs=out), encoding="utf-8")


class DependencyGraphTests(unittest.TestCase):
    def test_acyclic_graph_and_determinism(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "a", outputs=["contract-a"])
            write_skill(root, "b", requires=["a"], outputs=["contract-b"])
            first = render_json(build_graph(root))
            second = render_json(build_graph(root))
            self.assertEqual(first, second)
            graph = json.loads(first)
            self.assertEqual(graph["requirementEdges"], [{"from": "b", "to": "a"}])

    def test_ambiguous_output_is_recorded_without_invented_edge(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "a", outputs=["shared"])
            write_skill(root, "b", outputs=["shared"])
            graph = build_graph(root)
            contract = graph["outputContracts"][0]
            self.assertTrue(contract["ambiguous"])
            self.assertEqual(contract["producers"], ["a", "b"])

    def test_unknown_dependency_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "a", requires=["missing"])
            with self.assertRaisesRegex(ValueError, "unknown required skill"):
                build_graph(root)

    def test_self_dependency_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "a", requires=["a"])
            with self.assertRaisesRegex(ValueError, "self-dependency"):
                build_graph(root)

    def test_cycle_reports_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "a", requires=["b"])
            write_skill(root, "b", requires=["a"])
            with self.assertRaisesRegex(ValueError, r"a -> b -> a|b -> a -> b"):
                build_graph(root)

    def test_check_detects_stale_artifacts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "a")
            self.assertEqual(run(root, False), 0)
            self.assertEqual(run(root, True), 0)
            (root / "docs" / "SKILL-DEPENDENCIES.md").write_text("stale\n", encoding="utf-8")
            self.assertEqual(run(root, True), 1)


if __name__ == "__main__":
    unittest.main()
