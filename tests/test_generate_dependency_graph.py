from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_dependency_graph import build_graph, render_json, run  # noqa: E402


SKILL = """---\nname: {name}\ndescription: A sufficiently long description for dependency graph testing.\n{requires_line}{requires}{consumes_line}{consumes}{outputs_line}{outputs}---\n\n## Trigger\nTest.\n"""


def write_skill(
    root: Path,
    name: str,
    requires: list[str] | None = None,
    consumes: list[str] | None = None,
    outputs: list[str] | None = None,
) -> None:
    path = root / "skills" / name / "SKILL.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    requires = requires or []
    consumes = consumes or []
    outputs = outputs or []
    requires_line = "requires:\n" if requires else "requires: []\n"
    consumes_line = "consumes:\n" if consumes else "consumes: []\n"
    outputs_line = "outputs:\n" if outputs else "outputs: []\n"
    req = "".join(f"  - {item}\n" for item in requires)
    con = "".join(f"  - {item}\n" for item in consumes)
    out = "".join(f"  - {item}\n" for item in outputs)
    path.write_text(
        SKILL.format(
            name=name,
            requires_line=requires_line,
            requires=req,
            consumes_line=consumes_line,
            consumes=con,
            outputs_line=outputs_line,
            outputs=out,
        ),
        encoding="utf-8",
    )


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
            contracts = {item["output"]: item for item in graph["outputContracts"]}
            self.assertEqual(contracts["contract-a"]["consumerSkills"], ["b"])
            self.assertEqual(contracts["contract-a"]["consumptionStatus"], "inferred")
            self.assertNotIn("contract-a", graph["orphanOutputs"])
            self.assertIn("contract-b", graph["orphanOutputs"])

    def test_explicit_consumes_tracks_artifact_without_hard_dependency(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "producer", outputs=["handoff.json", "report.md"])
            write_skill(root, "consumer", consumes=["handoff.json"])
            graph = build_graph(root)
            self.assertEqual(graph["requirementEdges"], [])
            self.assertEqual(
                graph["consumptionEdges"],
                [{"consumer": "consumer", "artifact": "handoff.json", "producer": "producer"}],
            )
            contracts = {item["output"]: item for item in graph["outputContracts"]}
            self.assertEqual(contracts["handoff.json"]["consumerSkills"], ["consumer"])
            self.assertEqual(contracts["handoff.json"]["consumptionStatus"], "explicit")
            self.assertEqual(contracts["report.md"]["consumerSkills"], [])

    def test_explicit_consumes_overrides_broad_required_skill_inference(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "producer", outputs=["normative.json", "human.md", "scorecard.json"])
            write_skill(root, "consumer", requires=["producer"], consumes=["normative.json", "scorecard.json"])
            graph = build_graph(root)
            contracts = {item["output"]: item for item in graph["outputContracts"]}
            self.assertEqual(contracts["normative.json"]["consumerSkills"], ["consumer"])
            self.assertEqual(contracts["scorecard.json"]["consumerSkills"], ["consumer"])
            self.assertEqual(contracts["human.md"]["consumerSkills"], [])

    def test_unknown_consumed_artifact_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "consumer", consumes=["missing.json"])
            with self.assertRaisesRegex(ValueError, "unknown consumed artifact"):
                build_graph(root)

    def test_ambiguous_consumed_artifact_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "a", outputs=["shared.json"])
            write_skill(root, "b", outputs=["shared.json"])
            write_skill(root, "consumer", consumes=["shared.json"])
            with self.assertRaisesRegex(ValueError, "ambiguous producers"):
                build_graph(root)

    def test_self_consumption_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "a", consumes=["own.json"], outputs=["own.json"])
            with self.assertRaisesRegex(ValueError, "self-consumption"):
                build_graph(root)

    def test_ambiguous_output_is_recorded_without_invented_consumers(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "a", outputs=["shared"])
            write_skill(root, "b", outputs=["shared"])
            write_skill(root, "c", requires=["a"])
            graph = build_graph(root)
            contract = graph["outputContracts"][0]
            self.assertTrue(contract["ambiguous"])
            self.assertEqual(contract["producers"], ["a", "b"])
            self.assertEqual(contract["consumerSkills"], [])
            self.assertNotIn("shared", graph["orphanOutputs"])

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
