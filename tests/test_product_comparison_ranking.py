from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "product-comparison-ranking" / "scripts" / "rank_products.py"
spec = importlib.util.spec_from_file_location("rank_products", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


CRITERIA = [
    {"id": "quality", "weight": 0.5, "kind": "quality"},
    {"id": "reliability", "weight": 0.3, "kind": "quality"},
    {"id": "price", "weight": 0.2, "kind": "price"},
]


def candidate(candidate_id: str, scores: dict[str, float | None], *, gate: str = "PASS", price: float = 100.0) -> dict:
    return {
        "candidateId": candidate_id,
        "mustHaveStates": [gate],
        "criterionScores": scores,
        "evidenceCoverage": "high",
        "effectivePrice": price,
    }


class ProductComparisonRankingTests(unittest.TestCase):
    def test_clear_winner_remains_high_confidence(self):
        result = module.rank({
            "criteria": CRITERIA,
            "candidates": [
                candidate("a", {"quality": 95, "reliability": 95, "price": 70}),
                candidate("b", {"quality": 80, "reliability": 80, "price": 100}),
            ],
        })
        self.assertEqual(result["rankingConfidence"], "high")
        self.assertTrue(result["sensitivity"]["qualityWinnerStable"])
        self.assertTrue(result["sensitivity"]["pricePerformanceWinnerStable"])
        self.assertFalse(any(result["sensitivity"]["nearTie"].values()))
        self.assertEqual(result["sensitivity"]["winnerChanges"], [])

    def test_near_tie_reduces_confidence_without_forcing_winner_change(self):
        result = module.rank({
            "criteria": CRITERIA,
            "candidates": [
                candidate("a", {"quality": 90, "reliability": 90, "price": 90}),
                candidate("b", {"quality": 89.5, "reliability": 89.5, "price": 89.5}),
            ],
        })
        self.assertEqual(result["winners"]["quality"], "a")
        self.assertEqual(result["rankingConfidence"], "low")
        self.assertTrue(result["sensitivity"]["nearTie"]["quality"])
        self.assertTrue(result["sensitivity"]["nearTie"]["pricePerformance"])
        self.assertEqual(result["sensitivity"]["winnerChanges"], [])
        self.assertIn("top candidates are within the configured near-tie threshold", result["limitations"])

    def test_plausible_weight_shift_exposes_winner_reversal(self):
        result = module.rank({
            "criteria": CRITERIA,
            "candidates": [
                candidate("a", {"quality": 100, "reliability": 70, "price": 80}),
                candidate("b", {"quality": 80, "reliability": 100, "price": 80}),
            ],
        })
        self.assertEqual(result["winners"]["quality"], "a")
        self.assertEqual(result["rankingConfidence"], "low")
        self.assertFalse(result["sensitivity"]["qualityWinnerStable"])
        self.assertTrue(any(change["qualityWinner"] == "b" for change in result["sensitivity"]["winnerChanges"]))
        self.assertIn("winner changes under plausible one-at-a-time weight shifts", result["limitations"])

    def test_missing_material_score_still_reduces_confidence(self):
        result = module.rank({
            "criteria": CRITERIA,
            "candidates": [
                candidate("a", {"quality": 95, "reliability": 95, "price": 80}),
                candidate("uncertain", {"quality": 100, "reliability": None, "price": 100}, gate="UNKNOWN"),
            ],
        })
        self.assertEqual(result["rankingConfidence"], "low")
        self.assertIn("shortlist contains conditional/unknown gates or incomplete utility scores", result["limitations"])

    def test_sensitivity_parameters_are_configurable_and_validated(self):
        result = module.rank({
            "criteria": CRITERIA,
            "sensitivityDelta": 0.02,
            "nearTieThreshold": 0.25,
            "candidates": [
                candidate("a", {"quality": 90, "reliability": 90, "price": 90}),
                candidate("b", {"quality": 89.5, "reliability": 89.5, "price": 89.5}),
            ],
        })
        self.assertEqual(result["sensitivity"]["delta"], 0.02)
        self.assertEqual(result["sensitivity"]["nearTieThreshold"], 0.25)
        self.assertEqual(result["rankingConfidence"], "high")
        with self.assertRaisesRegex(ValueError, "sensitivityDelta"):
            module.rank({"criteria": CRITERIA, "sensitivityDelta": 0, "candidates": []})
        with self.assertRaisesRegex(ValueError, "nearTieThreshold"):
            module.rank({"criteria": CRITERIA, "nearTieThreshold": -1, "candidates": []})


if __name__ == "__main__":
    unittest.main()
