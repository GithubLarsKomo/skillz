from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_repository_metadata import parse_frontmatter  # noqa: E402


EXPECTED_CONSUMES: dict[str, list[str]] = {
    "sport-goal-performance-model": ["athlete-profile.json"],
    "sport-season-periodization": ["sport-performance-model.json"],
    "sport-mesocycle-planning": ["sport-season-plan.json"],
    "sport-microcycle-planning": ["sport-mesocycle.json"],
    "sport-strength-power-programming": [
        "athlete-profile.json",
        "sport-performance-model.json",
        "sport-mesocycle.json",
        "sport-microcycle.json",
    ],
    "sport-endurance-programming": [
        "athlete-profile.json",
        "sport-diagnostics.json",
        "sport-performance-model.json",
        "sport-mesocycle.json",
        "sport-microcycle.json",
    ],
    "sport-training-plan-workflow": [
        "athlete-profile.json",
        "sport-diagnostics.json",
        "sport-performance-model.json",
        "sport-season-plan.json",
        "sport-mesocycle.json",
        "sport-microcycle.json",
        "strength-power-plan.json",
        "endurance-plan.json",
    ],
    "dr-komorowski-sport-pdf-report-renderer": ["dr-komorowski-sport-report.docx"],
    "sport-diagnostics-training-report-workflow": [
        "sport-diagnostics.json",
        "sport-training-plan.json",
        "dr-komorowski-sport-report.docx",
        "dr-komorowski-sport-report.pdf",
    ],
    "presentation-layout-qa": ["presentation-template-profile.json"],
    "presentation-render-verifier": ["presentation-layout-qa.json"],
    "template-presentation-workflow": [
        "presentation-template-profile.json",
        "presentation-revised-text",
        "presentation-language-report.json",
        "presentation-layout-qa.json",
        "presentation-layout-qa.md",
        "presentation-render-qa.json",
        "presentation-render-qa.md",
        "presentation-preview.pdf",
    ],
    "person-profile-document-delivery": [
        "final-revised-text",
        "precision-writing-report.json",
    ],
}


class ArchitectureConsolidationP3ArtifactContractsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.index = json.loads((ROOT / "docs" / "skill-capability-index.json").read_text(encoding="utf-8"))
        cls.skills = {skill["name"]: skill for skill in cls.index["skills"]}

    def test_frontmatter_declares_only_evidence_backed_consumes(self) -> None:
        for slug, expected in EXPECTED_CONSUMES.items():
            frontmatter = parse_frontmatter(ROOT / "skills" / slug / "SKILL.md")
            self.assertEqual(frontmatter.get("consumes"), expected, slug)

    def test_every_explicit_consumed_artifact_has_one_canonical_producer(self) -> None:
        producers: dict[str, list[str]] = {}
        for skill in self.index["skills"]:
            for output in skill["outputs"]:
                producers.setdefault(output, []).append(skill["name"])

        for slug, artifacts in EXPECTED_CONSUMES.items():
            for artifact in artifacts:
                self.assertIn(artifact, producers, f"{slug}: unknown consumed artifact {artifact}")
                self.assertEqual(
                    len(producers[artifact]),
                    1,
                    f"{slug}: {artifact} must have one canonical producer, got {producers[artifact]}",
                )

    def test_capability_index_consumer_edges_follow_explicit_contracts(self) -> None:
        contracts_by_output: dict[str, dict] = {}
        for skill in self.index["skills"]:
            for contract in skill["outputContracts"]:
                contracts_by_output.setdefault(contract["output"], contract)

        for consumer, artifacts in EXPECTED_CONSUMES.items():
            for artifact in artifacts:
                contract = contracts_by_output[artifact]
                self.assertFalse(contract["ambiguous"], artifact)
                self.assertIn(consumer, contract["consumerSkills"], f"{consumer} <- {artifact}")

    def test_explicit_consumes_prevent_broad_requires_output_inference(self) -> None:
        # Layout QA needs the machine-readable template profile, not the profiler's human-readable note.
        profile_md = next(
            contract
            for contract in self.skills["presentation-template-profiler"]["outputContracts"]
            if contract["output"] == "presentation-template-profile.md"
        )
        self.assertNotIn("presentation-layout-qa", profile_md["consumerSkills"])

        # The PDF renderer consumes the DOCX, not every conceptual output of an upstream orchestrator.
        docx = next(
            contract
            for contract in self.skills["dr-komorowski-sport-docx-report-renderer"]["outputContracts"]
            if contract["output"] == "dr-komorowski-sport-report.docx"
        )
        self.assertIn("dr-komorowski-sport-pdf-report-renderer", docx["consumerSkills"])

    def test_no_output_ambiguity_is_introduced(self) -> None:
        ambiguous = [
            contract
            for skill in self.index["skills"]
            for contract in skill["outputContracts"]
            if contract["ambiguous"]
        ]
        self.assertEqual([], ambiguous)


if __name__ == "__main__":
    unittest.main()
