from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from evaluate_skills import run as evaluate_all  # noqa: E402
from generate_capability_health import build_health  # noqa: E402
from generate_capability_index import build_index  # noqa: E402
from generate_repository_metadata import parse_frontmatter  # noqa: E402


class ArchitectureConsolidationP2Tests(unittest.TestCase):
    def read_skill(self, slug: str) -> tuple[dict[str, object], str]:
        path = ROOT / "skills" / slug / "SKILL.md"
        self.assertTrue(path.is_file(), slug)
        return parse_frontmatter(path), path.read_text(encoding="utf-8")

    def test_discoverability_is_resolved_orthogonally(self) -> None:
        index = build_index(ROOT)
        by_name = {item["name"]: item for item in index["skills"]}
        self.assertEqual(by_name["sport-athlete-management"]["governance"]["discoverability"], "public")
        self.assertEqual(by_name["learning-delivery-workflow"]["governance"]["discoverability"], "internal")
        self.assertEqual(by_name["skill-portfolio-audit"]["governance"]["discoverability"], "advanced")
        self.assertEqual(by_name["skill-lifecycle-migration"]["governance"]["discoverability"], "advanced")
        self.assertEqual(by_name["sport-training-programming"]["governance"]["discoverability"], "compatibility")
        counts = index["discoverabilityCounts"]
        self.assertGreaterEqual(counts["advanced"], 2)
        self.assertGreaterEqual(counts["internal"], 47)
        self.assertGreaterEqual(counts["compatibility"], 2)
        self.assertEqual(counts["public"] + counts["advanced"], index["entrypointCount"])
        self.assertEqual(counts["internal"] + counts["compatibility"], index["skillCount"] - index["entrypointCount"])
        self.assertEqual(sum(counts.values()), index["skillCount"])

    def test_deprecated_skills_have_explicit_migration_metadata(self) -> None:
        for slug in ("dr-komorowski-sport-report-renderer", "sport-training-programming"):
            fm, _ = self.read_skill(slug)
            self.assertEqual(fm.get("status"), "deprecated")
            self.assertEqual(fm.get("discoverability"), "compatibility")
            self.assertTrue(str(fm.get("replacedBy", "")).strip())
            self.assertTrue(str(fm.get("deprecatedSince", "")).strip())
            self.assertNotEqual(str(fm.get("userFacing", "false")).lower(), "true")

    def test_one_shot_sport_plan_has_single_canonical_owner(self) -> None:
        canonical_fm, canonical = self.read_skill("sport-training-plan-workflow")
        legacy_fm, legacy = self.read_skill("sport-training-programming")
        self.assertIn("sport-training-plan.json", canonical_fm.get("outputs", []))
        self.assertNotIn("sport-training-plan.json", legacy_fm.get("outputs", []))
        self.assertEqual(legacy_fm.get("replacedBy"), "sport-training-plan-workflow")
        self.assertIn("sport-training-plan-workflow", legacy_fm.get("requires", []))
        self.assertIn("keine zweite Trainingsplan-Engine", legacy)
        self.assertIn("genau einen Producer für `sport-training-plan.json`", canonical)

    def test_active_sport_consumers_no_longer_route_to_legacy_monolith(self) -> None:
        report_fm, report = self.read_skill("sport-diagnostics-training-report-workflow")
        self.assertIn("sport-training-plan-workflow", report_fm.get("requires", []))
        self.assertNotIn("sport-training-programming", report_fm.get("requires", []))
        self.assertIn("sport-training-plan-workflow", report)

        _, athlete = self.read_skill("sport-athlete-management")
        self.assertIn("für einen einmaligen Plan `sport-training-plan-workflow` verwenden", athlete)
        self.assertIn("Compatibility-Fassade", athlete)

    def test_governance_meta_capabilities_are_layered(self) -> None:
        portfolio_fm, _ = self.read_skill("skill-portfolio-audit")
        lifecycle_fm, _ = self.read_skill("skill-lifecycle-migration")
        eval_fm, _ = self.read_skill("skill-evaluation-suite-authoring")
        normalizer_fm, _ = self.read_skill("artifact-contract-normalizer")
        self.assertEqual(portfolio_fm.get("discoverability"), "advanced")
        self.assertEqual(lifecycle_fm.get("discoverability"), "advanced")
        self.assertEqual(eval_fm.get("discoverability"), "internal")
        self.assertEqual(normalizer_fm.get("discoverability"), "internal")
        self.assertIn("skill-portfolio-audit", lifecycle_fm.get("requires", []))
        self.assertIn("skill-portfolio-audit", normalizer_fm.get("requires", []))

    def test_p2_keeps_health_complete_and_outputs_unambiguous(self) -> None:
        evaluation_summary, evaluation_errors = evaluate_all(ROOT)
        self.assertEqual(
            evaluation_errors,
            [],
            "P2 evaluation failures:\n" + "\n".join(evaluation_errors),
        )
        self.assertTrue(evaluation_summary["passed"])

        health = build_health(ROOT)
        self.assertGreaterEqual(health["skillCount"], 280)
        self.assertGreaterEqual(health["entrypointCount"], 231)
        self.assertTrue(health["evaluationCoverageComplete"])
        self.assertTrue(health["executedEvaluationsPassed"])
        self.assertEqual(health["missingEvaluations"], [])
        self.assertEqual(health["missingEntrypointEvaluations"], [])
        self.assertEqual(health["ambiguousOutputs"], [])


if __name__ == "__main__":
    unittest.main()
