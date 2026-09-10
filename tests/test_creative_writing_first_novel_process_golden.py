from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "benchmarks" / "creative-writing-first-novel-process-golden-v1.json"


class CreativeWritingFirstNovelProcessGoldenTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.benchmark = json.loads(BENCHMARK.read_text(encoding="utf-8"))
        cls.fixtures = {item["id"]: item for item in cls.benchmark["fixtures"]}

    def skill_text(self, name: str) -> str:
        return (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")

    def test_snapshot_is_read_only_and_ci_is_decoupled_from_first_novel(self):
        provenance = self.benchmark["provenance"]
        self.assertEqual(provenance["sourceRepository"], "GithubLarsKomo/first-novel")
        self.assertEqual(provenance["accessMode"], "read-only-analysis")
        self.assertFalse(provenance["copiedManuscriptText"])
        self.assertFalse(provenance["liveSourceRequiredForCI"])
        self.assertRegex(provenance["sourceCommit"], r"^[0-9a-f]{40}$")

        source_keys: set[tuple[str, str]] = set()
        for fixture in self.benchmark["fixtures"]:
            for source in fixture["sourceArtifacts"]:
                self.assertFalse(source["path"].startswith("manuscript/"), source["path"])
                self.assertRegex(source["blobSha"], r"^[0-9a-f]{40}$")
                source_key = (source["path"], source["blobSha"])
                self.assertNotIn(source_key, source_keys)
                source_keys.add(source_key)

    def test_fixture_set_maps_exactly_to_the_three_new_longform_controls(self):
        self.assertEqual(
            {fixture["skill"] for fixture in self.benchmark["fixtures"]},
            {
                "fiction-reader-reality-review",
                "character-voice-fingerprint",
                "creative-revision-regression",
            },
        )
        self.assertEqual(len(self.fixtures), 3)

    def test_reader_reality_fixture_preserves_freeze_before_intent_semantics(self):
        fixture = self.fixtures["reader-reality-valid-freeze-with-minor-divergence"]
        observed = fixture["observed"]
        policy = fixture["expectedPolicy"]

        self.assertEqual(observed["isolationStatus"], "VALID_INTACT")
        self.assertFalse(observed["architectureSeenBeforeReaderFreeze"])
        self.assertFalse(observed["repositorySearchBeforeReaderFreeze"])
        self.assertEqual(observed["frozenReaderArtifactCount"], 2)
        self.assertTrue(observed["architectureOpenedOnlyAfterFreeze"])
        self.assertEqual(observed["criticalFindings"], 0)
        self.assertEqual(observed["majorFindings"], 0)
        self.assertGreater(observed["minorFindings"], 0)
        self.assertTrue(observed["architectureSpecificityCouldRemainLowerSalienceWithoutBecomingMajor"])

        self.assertEqual(policy["gate"], "pass-with-watchpoints")
        self.assertTrue(policy["mustFreezeBeforeIntent"])
        self.assertTrue(policy["mustNotUpgradeEveryArchitectureMismatchToMajor"])
        self.assertTrue(policy["mustInvalidateIfArchitectureSeenBeforeFreeze"])
        self.assertTrue(policy["mustPreserveFrozenReaderEvidenceAfterIntentAccess"])

        skill = self.skill_text(fixture["skill"])
        for anchor in [
            "Reader vor Intent",
            "Freeze vor Architektur",
            "Keine nachträgliche Korrektur der Blind-Rekonstruktion",
            "invalid",
        ]:
            self.assertIn(anchor, skill)

    def test_voice_fixture_distinguishes_leak_from_intentional_shared_language(self):
        fixture = self.fixtures["voice-collision-versus-intentional-shared-language"]
        observed = fixture["observed"]
        policy = fixture["expectedPolicy"]

        self.assertEqual(
            set(observed["requiredChecks"]),
            {
                "speaker-swap",
                "short-phrase-collision",
                "metaphor-domain",
                "status-address",
                "narrator-contamination",
                "blind-attribution",
            },
        )
        self.assertEqual(observed["actGateBeforeRevision"]["blockingMajorCollisionCount"], 1)
        self.assertEqual(observed["actGateBeforeRevision"]["intentionalSharedLanguageCount"], 2)
        self.assertEqual(observed["actGateAfterTargetedRevision"]["majorOpen"], 0)
        self.assertEqual(observed["actGateAfterTargetedRevision"]["status"], "pass")
        self.assertTrue(observed["sameSurfacePhraseCanBeEitherLeakOrIntentionalBorrowing"])
        self.assertEqual(observed["canonImpactOfVoiceRepair"], "none")
        self.assertEqual(observed["revealImpactOfVoiceRepair"], "none")
        self.assertEqual(observed["plotImpactOfVoiceRepair"], "none")

        self.assertTrue(policy["mustDistinguishCollisionFromIntentionalBorrowing"])
        self.assertTrue(policy["mustBlockOnOpenMajorCollision"])
        self.assertTrue(policy["mustAllowSharedInstitutionalOrRelationshipLanguageWithReason"])
        self.assertTrue(policy["mustNotRequirePlotOrCanonChangeForSurfaceVoiceRepair"])

        skill = self.skill_text(fixture["skill"])
        for anchor in [
            "Speaker-Swap-Test",
            "Blind Attribution Test",
            "Narrator-Contamination-Check",
            "intentional-shared-register",
        ]:
            self.assertIn(anchor, skill)

    def test_regression_fixture_uses_changed_function_not_text_volume(self):
        fixture = self.fixtures["multi-chapter-subtractive-revision-targeted-regression"]
        observed = fixture["observed"]
        policy = fixture["expectedPolicy"]

        self.assertEqual(observed["touchedChapterCount"], 5)
        self.assertEqual(observed["oldWordCount"] + observed["deltaWords"], observed["newWordCount"])
        self.assertLess(observed["deltaWords"], 0)
        for key in [
            "eventChanges",
            "leadDecisionChanges",
            "failedTrialChanges",
            "nonhumanAgencyChanges",
            "secondaryAgencyChanges",
            "politicalConsequenceChanges",
        ]:
            self.assertEqual(observed[key], 0, key)

        self.assertFalse(observed["freshBlindThreeChamberRerun"])
        self.assertTrue(observed["frozenBlindEvidenceWasPreserved"])
        self.assertTrue(observed["originalS3Resolved"])
        self.assertTrue(observed["nonblockingS2WatchpointsRemain"])
        self.assertTrue(observed["protectListRegressionPassed"])

        self.assertEqual(policy["impactClass"], "R2")
        self.assertEqual(policy["requiredRerun"], "targeted-regression")
        self.assertFalse(policy["fullBlindReaderRerunRequired"])
        self.assertTrue(policy["mustCheckProtectConstraints"])
        self.assertTrue(policy["mustCheckCollateralDamage"])
        self.assertTrue(policy["mustNotClaimResidualWatchpointsResolved"])
        self.assertTrue(policy["mustNotInferImpactFromWordCountOrFileCountAlone"])

        skill = self.skill_text(fixture["skill"])
        for anchor in [
            "R2 — Multi-Scene Presentation",
            "Delta nach Funktion",
            "Protect vor Optimierung",
            "Kein Full Rerun ohne funktionalen Grund",
        ]:
            self.assertIn(anchor, skill)


if __name__ == "__main__":
    unittest.main()
