import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_generator():
    spec = importlib.util.spec_from_file_location(
        "generate_obsidian_skill_universe",
        ROOT / "scripts" / "generate_obsidian_skill_universe.py",
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class GenerateObsidianSkillUniverseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.generator = load_generator()

    def test_repository_projection_matches_capability_and_dependency_metadata(self):
        outputs = self.generator.build_outputs(ROOT)
        index = json.loads((ROOT / "docs/skill-capability-index.json").read_text(encoding="utf-8"))
        graph = json.loads((ROOT / "docs/skill-dependency-graph.json").read_text(encoding="utf-8"))

        skill_notes = [path for path in outputs if path.parts[:2] == ("obsidian", "skills")]
        self.assertEqual(len(skill_notes), index["skillCount"])

        canvas = json.loads(outputs[Path("obsidian/Skill Universe.canvas")])
        skill_nodes = [node for node in canvas["nodes"] if node["type"] == "file"]
        requires_edges = [edge for edge in canvas["edges"] if edge.get("label") == "requires"]
        self.assertEqual(len(skill_nodes), index["skillCount"])
        self.assertEqual(len(requires_edges), len(graph["requirementEdges"]))
        self.assertTrue(all(edge.get("toEnd") == "arrow" for edge in requires_edges))

        by_name = {skill["name"]: skill for skill in index["skills"]}
        for name, skill in by_name.items():
            note = outputs[Path(f"obsidian/skills/{name}.md")]
            self.assertIn(f"sourcePath: \"skills/{name}/SKILL.md\"", note)
            for dependency in skill["requires"]:
                self.assertIn(f"[[skills/{dependency}|{dependency}]]", note)
            for dependent in skill["dependents"]:
                self.assertIn(f"[[skills/{dependent}|{dependent}]]", note)

    def test_workflow_notes_are_derived_only_from_valid_benchmark_sequences(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "docs").mkdir()
            (root / "benchmarks").mkdir()
            index = {
                "schemaVersion": 1,
                "skillCount": 2,
                "evaluationPassed": True,
                "skills": [
                    {
                        "name": "alpha",
                        "description": "Alpha",
                        "invocation": {"userFacing": True, "category": "engineering"},
                        "requires": ["beta"],
                        "dependents": [],
                        "outputs": [],
                        "outputContracts": [],
                        "evaluation": {"mode": "rubric", "caseCount": 3, "recordedResultCount": 3, "passed": True},
                    },
                    {
                        "name": "beta",
                        "description": "Beta",
                        "invocation": {"userFacing": False, "category": None},
                        "requires": [],
                        "dependents": ["alpha"],
                        "outputs": [],
                        "outputContracts": [],
                        "evaluation": {"mode": "rubric", "caseCount": 3, "recordedResultCount": 3, "passed": True},
                    },
                ],
            }
            graph = {"schemaVersion": 1, "requirementEdges": [{"from": "alpha", "to": "beta"}]}
            (root / "docs/skill-capability-index.json").write_text(json.dumps(index), encoding="utf-8")
            (root / "docs/skill-dependency-graph.json").write_text(json.dumps(graph), encoding="utf-8")
            (root / "benchmarks/e2e.json").write_text(
                json.dumps(
                    {
                        "scenarios": [
                            {"id": "valid-flow", "sequence": ["alpha", "beta"], "mustPreserve": ["direction"]},
                            {"id": "invalid-flow", "sequence": ["alpha", "missing-skill"]},
                        ]
                    }
                ),
                encoding="utf-8",
            )

            outputs = self.generator.build_outputs(root)
            self.assertIn(Path("obsidian/workflows/valid-flow.md"), outputs)
            self.assertNotIn(Path("obsidian/workflows/invalid-flow.md"), outputs)
            self.assertIn("[[skills/alpha|alpha]]", outputs[Path("obsidian/workflows/valid-flow.md")])
            self.assertIn("[[skills/beta|beta]]", outputs[Path("obsidian/workflows/valid-flow.md")])

    def test_check_mode_detects_stale_and_extra_generated_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "docs").mkdir()
            index = {
                "schemaVersion": 1,
                "skillCount": 1,
                "evaluationPassed": True,
                "skills": [
                    {
                        "name": "alpha",
                        "description": "Alpha",
                        "invocation": {"userFacing": True, "category": "engineering"},
                        "requires": [],
                        "dependents": [],
                        "outputs": [],
                        "outputContracts": [],
                        "evaluation": {"mode": "rubric", "caseCount": 3, "recordedResultCount": 3, "passed": True},
                    }
                ],
            }
            graph = {"schemaVersion": 1, "requirementEdges": []}
            (root / "docs/skill-capability-index.json").write_text(json.dumps(index), encoding="utf-8")
            (root / "docs/skill-dependency-graph.json").write_text(json.dumps(graph), encoding="utf-8")

            self.assertEqual(self.generator.run(root, False), 0)
            self.assertEqual(self.generator.run(root, True), 0)
            extra = root / "obsidian/skills/obsolete.md"
            extra.write_text("obsolete", encoding="utf-8")
            self.assertEqual(self.generator.run(root, True), 1)
            self.assertEqual(self.generator.run(root, False), 0)
            self.assertFalse(extra.exists())


if __name__ == "__main__":
    unittest.main()
