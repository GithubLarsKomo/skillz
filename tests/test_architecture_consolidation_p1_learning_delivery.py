from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_capability_index import build_index  # noqa: E402
from generate_dependency_graph import build_graph  # noqa: E402


DELIVERY_WORKERS = {
    "learning-content-design-system",
    "learning-visual-planner",
    "learning-svg-generator",
    "learning-image-generator",
    "learning-landingpage-renderer",
    "learning-document-delivery",
    "template-presentation-workflow",
    "learning-artifact-qa",
}


class ArchitectureConsolidationP1LearningDeliveryTests(unittest.TestCase):
    def test_shared_delivery_layer_owns_orchestration_not_worker_files(self) -> None:
        graph = build_graph(ROOT)
        by_name = {item["name"]: item for item in graph["skills"]}
        delivery = by_name["learning-delivery-workflow"]

        self.assertEqual(set(delivery["requires"]), DELIVERY_WORKERS)
        self.assertEqual(
            set(delivery["outputs"]),
            {"learning-delivery-bundle.json", "learning-delivery-run.json"},
        )
        self.assertTrue(
            {"learning-content-model.json", "multi-source-learning-model.json", "course-learning-model.json"}
            <= set(delivery["consumes"])
        )

        worker_files = {
            "learning-landingpage",
            "learning-handout.docx",
            "learning-handout.pdf",
            "presentation.pptx",
            "presentation.pdf",
            "learning-svg-assets",
            "learning-image-assets",
        }
        self.assertTrue(worker_files.isdisjoint(delivery["outputs"]))

    def test_learning_orchestrators_delegate_delivery_instead_of_repeating_workers(self) -> None:
        graph = build_graph(ROOT)
        by_name = {item["name"]: item for item in graph["skills"]}
        for name in (
            "youtube-learning-workflow",
            "youtube-playlist-learning-workflow",
            "youtube-course-builder-workflow",
        ):
            requires = set(by_name[name]["requires"])
            self.assertIn("learning-delivery-workflow", requires)
            self.assertTrue(
                DELIVERY_WORKERS.isdisjoint(requires),
                f"{name} still directly requires delivery workers: {sorted(DELIVERY_WORKERS & requires)}",
            )

    def test_new_delivery_skill_is_internal_evaluated_and_does_not_create_ambiguity(self) -> None:
        index = build_index(ROOT)
        by_name = {item["name"]: item for item in index["skills"]}
        delivery = by_name["learning-delivery-workflow"]
        self.assertEqual(delivery["invocation"], {"userFacing": False, "category": None})
        self.assertNotEqual(delivery["evaluation"]["mode"], "none")
        self.assertTrue(delivery["evaluation"]["passed"])

        seen: set[str] = set()
        ambiguous: set[str] = set()
        for skill in index["skills"]:
            for contract in skill["outputContracts"]:
                output = str(contract["output"])
                if output in seen:
                    continue
                seen.add(output)
                if contract["ambiguous"]:
                    ambiguous.add(output)
        self.assertEqual(ambiguous, set())


if __name__ == "__main__":
    unittest.main()
