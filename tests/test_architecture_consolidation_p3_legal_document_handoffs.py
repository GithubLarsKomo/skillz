from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_repository_metadata import parse_frontmatter  # noqa: E402


EXPECTED_CONSUMES: dict[str, list[str]] = {
    "euroimmun-pdf-report-renderer": [
        "euroimmun-report.docx",
    ],
    "legal-negotiation-strategy": [
        "client-strategy.json",
        "legal-decision-boundaries.json",
        "legal-risk-register.json",
        "commercial-exposure-analysis.json",
        "legal-risk-decision-handoff.json",
    ],
    "legal-redline-review-loop": [
        "contract-review.json",
        "contract-issue-list.json",
        "negotiation-positions.json",
    ],
    "legal-matter-final-gate": [
        "legal-risk-register.json",
        "legal-risk-decision-handoff.json",
        "privilege-routing.json",
        "counsel-scope.json",
    ],
    "contract-matter-workflow": [
        "agreement-deal-model.json",
        "agreement-clause-coverage.json",
        "agreement-specialist-routes.json",
        "contract-review.json",
        "contract-issue-list.json",
        "contract-risk-input.json",
        "contract-draft.md",
        "contract-drafting-report.json",
        "contract-open-points.md",
        "negotiation-positions.json",
        "redline-delta.json",
        "negotiation-state.json",
        "legal-final-gate.json",
        "legal-open-points.md",
    ],
}


class ArchitectureConsolidationP3LegalDocumentHandoffsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.index = json.loads((ROOT / "docs" / "skill-capability-index.json").read_text(encoding="utf-8"))
        cls.skills = {skill["name"]: skill for skill in cls.index["skills"]}

    def test_frontmatter_declares_expected_handoffs(self) -> None:
        for slug, expected in EXPECTED_CONSUMES.items():
            frontmatter = parse_frontmatter(ROOT / "skills" / slug / "SKILL.md")
            self.assertEqual(frontmatter.get("consumes"), expected, slug)

    def test_every_consumed_artifact_has_one_canonical_producer(self) -> None:
        producers: dict[str, list[str]] = {}
        for skill in self.index["skills"]:
            for output in skill["outputs"]:
                producers.setdefault(output, []).append(skill["name"])

        for consumer, artifacts in EXPECTED_CONSUMES.items():
            for artifact in artifacts:
                self.assertEqual(
                    len(producers.get(artifact, [])),
                    1,
                    f"{consumer}: {artifact} producers={producers.get(artifact, [])}",
                )

    def test_generated_consumer_edges_are_present_and_unambiguous(self) -> None:
        contracts: dict[str, dict] = {}
        for skill in self.index["skills"]:
            for contract in skill["outputContracts"]:
                contracts[contract["output"]] = contract

        for consumer, artifacts in EXPECTED_CONSUMES.items():
            for artifact in artifacts:
                self.assertFalse(contracts[artifact]["ambiguous"], artifact)
                self.assertIn(consumer, contracts[artifact]["consumerSkills"], f"{consumer} <- {artifact}")

    def test_euroimmun_pdf_has_single_docx_source_contract(self) -> None:
        docx_contract = next(
            contract
            for contract in self.skills["euroimmun-docx-report-renderer"]["outputContracts"]
            if contract["output"] == "euroimmun-report.docx"
        )
        self.assertIn("euroimmun-pdf-report-renderer", docx_contract["consumerSkills"])
        self.assertEqual(
            parse_frontmatter(ROOT / "skills" / "euroimmun-pdf-report-renderer" / "SKILL.md")["consumes"],
            ["euroimmun-report.docx"],
        )

    def test_contract_matter_prefers_state_artifacts_over_human_views(self) -> None:
        matter = EXPECTED_CONSUMES["contract-matter-workflow"]
        self.assertIn("agreement-deal-model.json", matter)
        self.assertIn("contract-issue-list.json", matter)
        self.assertIn("negotiation-state.json", matter)
        self.assertIn("legal-final-gate.json", matter)
        self.assertNotIn("contract-review.md", matter)
        self.assertNotIn("negotiation-playbook.md", matter)
        self.assertNotIn("redline-review.md", matter)

    def test_redline_loop_consumes_issue_lineage_and_machine_negotiation_positions(self) -> None:
        self.assertEqual(
            EXPECTED_CONSUMES["legal-redline-review-loop"],
            ["contract-review.json", "contract-issue-list.json", "negotiation-positions.json"],
        )

    def test_no_ambiguous_outputs_are_introduced(self) -> None:
        ambiguous = [
            contract
            for skill in self.index["skills"]
            for contract in skill["outputContracts"]
            if contract["ambiguous"]
        ]
        self.assertEqual([], ambiguous)


if __name__ == "__main__":
    unittest.main()
