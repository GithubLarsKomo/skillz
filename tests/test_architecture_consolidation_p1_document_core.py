from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_capability_index import build_index  # noqa: E402
from generate_dependency_graph import build_graph  # noqa: E402


class ArchitectureConsolidationP1DocumentCoreTests(unittest.TestCase):
    def test_document_core_has_single_responsibility_chain(self) -> None:
        graph = build_graph(ROOT)
        by_name = {item["name"]: item for item in graph["skills"]}

        self.assertEqual(by_name["document-template-profiler"]["requires"], [])
        self.assertEqual(
            by_name["document-layout-qa"]["requires"],
            ["document-template-profiler"],
        )
        self.assertEqual(
            by_name["document-layout-qa"]["consumes"],
            ["document-template-profile.json"],
        )
        self.assertEqual(
            by_name["document-render-verifier"]["requires"],
            ["document-layout-qa"],
        )
        self.assertEqual(
            by_name["document-render-verifier"]["consumes"],
            ["document-layout-qa.json"],
        )
        self.assertEqual(
            set(by_name["template-document-workflow"]["requires"]),
            {"document-template-profiler", "document-layout-qa", "document-render-verifier"},
        )

    def test_document_outputs_have_clear_ownership(self) -> None:
        graph = build_graph(ROOT)
        contracts = {item["output"]: item for item in graph["outputContracts"]}
        expected = {
            "document-template-profile.json": "document-template-profiler",
            "document-layout-qa.json": "document-layout-qa",
            "document-render-qa.json": "document-render-verifier",
            "document-preview.pdf": "document-render-verifier",
            "document.docx": "template-document-workflow",
            "document.pdf": "template-document-workflow",
            "document-qa.md": "template-document-workflow",
            "document-delivery-manifest.json": "template-document-workflow",
        }
        for artifact, producer in expected.items():
            self.assertIn(artifact, contracts)
            self.assertFalse(contracts[artifact]["ambiguous"], artifact)
            self.assertEqual(contracts[artifact]["producers"], [producer])

    def test_all_new_document_capabilities_are_evaluated(self) -> None:
        index = build_index(ROOT)
        by_name = {item["name"]: item for item in index["skills"]}
        for name in (
            "document-template-profiler",
            "document-layout-qa",
            "document-render-verifier",
            "template-document-workflow",
        ):
            self.assertNotEqual(by_name[name]["evaluation"]["mode"], "none", name)
            self.assertTrue(by_name[name]["evaluation"]["passed"], name)

        self.assertEqual(
            by_name["template-document-workflow"]["invocation"],
            {"userFacing": True, "category": "workflow"},
        )
        for name in ("document-template-profiler", "document-layout-qa", "document-render-verifier"):
            self.assertEqual(by_name[name]["invocation"], {"userFacing": False, "category": None})


if __name__ == "__main__":
    unittest.main()
