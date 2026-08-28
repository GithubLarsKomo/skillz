from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_capability_index import build_index, invocation_metadata, render_json, run  # noqa: E402


SKILL = """---\nname: {name}\ndescription: Capability index test skill with enough detail.\n{invocation}requires: {requires_inline}\noutputs: {outputs_inline}\n---\n\n## Trigger\nTest capability index generation.\n"""


def write_skill(
    root: Path,
    name: str,
    requires: list[str] | None = None,
    outputs: list[str] | None = None,
    user_facing: bool | None = None,
    category: str | None = None,
) -> Path:
    path = root / "skills" / name / "SKILL.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    req = "[]" if not requires else "\n" + "".join(f"  - {item}\n" for item in requires).rstrip("\n")
    out = "[]" if not outputs else "\n" + "".join(f"  - {item}\n" for item in outputs).rstrip("\n")
    invocation = ""
    if user_facing is not None:
        invocation += f"userFacing: {'true' if user_facing else 'false'}\n"
    if category is not None:
        invocation += f"category: {category}\n"
    path.write_text(SKILL.format(name=name, invocation=invocation, requires_inline=req, outputs_inline=out), encoding="utf-8")
    return path


def write_legacy_suite(skill_dir: Path) -> None:
    tests = skill_dir / "tests"
    results = tests / "results"
    results.mkdir(parents=True, exist_ok=True)
    cases = []
    for case_id in ("happy-path", "edge-case", "failure-case"):
        cases.append({
            "id": case_id,
            "input": "A sufficiently long evaluation prompt for capability index testing.",
            "requiredBehaviors": ["does the required thing"],
            "forbiddenBehaviors": ["does the forbidden thing"],
            "skillAnchors": ["Test capability index generation."],
        })
        (results / f"{case_id}.json").write_text(json.dumps({
            "skill": skill_dir.name,
            "caseId": case_id,
            "requiredBehaviors": [{"behavior": "does the required thing", "passed": True, "evidence": "recorded"}],
            "forbiddenBehaviors": [{"behavior": "does the forbidden thing", "observed": False, "evidence": "recorded"}],
            "overall": "pass",
        }), encoding="utf-8")
    (tests / "evaluation.json").write_text(json.dumps({"schemaVersion": 1, "skill": skill_dir.name, "cases": cases}), encoding="utf-8")


class CapabilityIndexTests(unittest.TestCase):
    def test_reuses_graph_semantics_and_records_reverse_dependencies(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "a", outputs=["contract-a"])
            write_skill(root, "b", requires=["a"], outputs=["contract-b"])
            index = build_index(root)
            by_name = {item["name"]: item for item in index["skills"]}
            self.assertEqual(by_name["a"]["dependents"], ["b"])
            self.assertEqual(by_name["a"]["outputContracts"][0]["consumerSkills"], ["b"])
            self.assertEqual(by_name["a"]["evaluation"]["mode"], "none")
            self.assertEqual(by_name["a"]["invocation"], {"userFacing": False, "category": None})
            self.assertEqual(index["evaluatedSkillCount"], 0)
            self.assertFalse(index["evaluationCoverageComplete"])

    def test_entrypoint_metadata_is_materialized_and_summarized(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "alpha", user_facing=True, category="engineering")
            write_skill(root, "beta")
            index = build_index(root)
            by_name = {item["name"]: item for item in index["skills"]}
            self.assertEqual(by_name["alpha"]["invocation"], {"userFacing": True, "category": "engineering"})
            self.assertEqual(index["entrypointCount"], 1)
            self.assertEqual(index["entrypointCategories"], ["engineering"])
            self.assertEqual(index["evaluatedSkillCount"], 0)
            self.assertEqual(index["evaluatedEntrypointCount"], 0)
            self.assertFalse(index["evaluationCoverageComplete"])

    def test_invalid_entrypoint_metadata_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = write_skill(root, "alpha", user_facing=True)
            with self.assertRaisesRegex(ValueError, "erfordert category"):
                build_index(root)
            self.assertEqual(invocation_metadata({"userFacing": "false"}, path), {"userFacing": False, "category": None})
            with self.assertRaisesRegex(ValueError, "kebab-case"):
                invocation_metadata({"userFacing": "true", "category": "Bad Category"}, path)
            with self.assertRaisesRegex(ValueError, "nur zusammen"):
                invocation_metadata({"userFacing": "false", "category": "engineering"}, path)

    def test_legacy_and_rubric_modes_are_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            legacy = write_skill(root, "legacy")
            rubric = write_skill(root, "rubric")
            write_legacy_suite(legacy.parent)
            write_legacy_suite(rubric.parent)
            (rubric.parent / "tests" / "rubric.json").write_text(json.dumps({
                "schemaVersion": 1,
                "dimensions": [{"id": "required-behaviors", "weight": 1.0, "description": "required"}],
                "threshold": 1.0,
                "blockingCriteria": ["required-behavior-failed"],
            }), encoding="utf-8")
            index = build_index(root)
            by_name = {item["name"]: item for item in index["skills"]}
            self.assertEqual(by_name["legacy"]["evaluation"]["mode"], "compatibility")
            self.assertEqual(by_name["rubric"]["evaluation"]["mode"], "rubric")
            self.assertTrue(by_name["legacy"]["evaluation"]["passed"])
            self.assertTrue(by_name["rubric"]["evaluation"]["passed"])
            self.assertEqual(index["evaluatedSkillCount"], 2)
            self.assertTrue(index["evaluationCoverageComplete"])

    def test_ambiguous_outputs_never_invent_consumers(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "a", outputs=["shared"])
            write_skill(root, "b", outputs=["shared"])
            write_skill(root, "c", requires=["a"])
            by_name = {item["name"]: item for item in build_index(root)["skills"]}
            contract = by_name["a"]["outputContracts"][0]
            self.assertTrue(contract["ambiguous"])
            self.assertEqual(contract["consumerSkills"], [])

    def test_deterministic_and_stale_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "b")
            write_skill(root, "a")
            self.assertEqual(render_json(build_index(root)), render_json(build_index(root)))
            self.assertEqual(run(root, False), 0)
            self.assertEqual(run(root, True), 0)
            (root / "docs" / "skill-capability-index.json").write_text("{}\n", encoding="utf-8")
            self.assertEqual(run(root, True), 1)


if __name__ == "__main__":
    unittest.main()
