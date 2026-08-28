from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "youtube-learning" / "pcr-course-builder-golden.json"
COURSE_DESIGN = ROOT / "docs" / "learning-content" / "course" / "DESIGN.md"
SPEC = ROOT / "docs" / "specs" / "youtube-learner" / "COURSE_BUILDER.md"
SKILLS = {
    "course-concept-graph": ROOT / "skills" / "course-concept-graph" / "SKILL.md",
    "learning-path-planner": ROOT / "skills" / "learning-path-planner" / "SKILL.md",
    "learning-activity-generator": ROOT / "skills" / "learning-activity-generator" / "SKILL.md",
    "youtube-course-builder-workflow": ROOT / "skills" / "youtube-course-builder-workflow" / "SKILL.md",
}


class TestYouTubeCourseBuilderContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.design = COURSE_DESIGN.read_text(encoding="utf-8")
        cls.spec = SPEC.read_text(encoding="utf-8")
        cls.skill_text = {name: path.read_text(encoding="utf-8") for name, path in SKILLS.items()}

    def test_course_builder_files_exist(self):
        self.assertTrue(FIXTURE.is_file())
        self.assertTrue(COURSE_DESIGN.is_file())
        self.assertTrue(SPEC.is_file())
        for path in SKILLS.values():
            self.assertTrue(path.is_file())

    def test_course_builder_is_composable(self):
        workflow = self.skill_text["youtube-course-builder-workflow"]
        for dependency in (
            "youtube-playlist-learning-workflow",
            "course-concept-graph",
            "learning-path-planner",
            "learning-activity-generator",
            "learning-artifact-qa",
        ):
            self.assertIn(f"  - {dependency}", workflow)
        self.assertIn("course-learning-model.json", workflow)

    def test_prerequisite_graph_is_not_playlist_order(self):
        graph = self.skill_text["course-concept-graph"]
        self.assertIn("Playlist-Reihenfolge", graph)
        self.assertIn("Zyklen", graph)
        self.assertTrue(self.fixture["graph"]["mustBeAcyclic"])
        self.assertEqual(self.fixture["graph"]["forbiddenBasis"], "playlist-order-alone")

    def test_learning_path_preserves_real_prerequisites(self):
        planner = self.skill_text["learning-path-planner"]
        self.assertIn("Fast-Track", planner)
        self.assertIn("keine echte fachliche Voraussetzung umgehen", planner)
        self.assertTrue(self.fixture["pathRules"]["fastTrackRequiresEntryCheck"])
        self.assertTrue(self.fixture["pathRules"]["requiredPrerequisitesCannotBeSkipped"])

    def test_modules_have_observable_objectives_and_exit_criteria(self):
        self.assertGreaterEqual(len(self.fixture["modules"]), 4)
        for module in self.fixture["modules"]:
            self.assertTrue(module["objectives"])
            self.assertTrue(module["exitCriteria"])
            self.assertTrue(module["competencePromise"])
        self.assertIn("observable", self.spec)

    def test_qpcr_remains_specialized_extension(self):
        m4 = next(m for m in self.fixture["modules"] if m["moduleId"] == "M4")
        self.assertEqual(m4["state"], "variant")
        self.assertEqual(m4["sourceScope"], ["S2"])
        self.assertIn("qPCR als Erweiterung", m4["exitCriteria"][0])

    def test_assessment_is_formative_not_certifying(self):
        checks = self.fixture["knowledgeChecks"]
        self.assertFalse(checks["psychometricallyValidated"])
        self.assertFalse(checks["certification"])
        self.assertFalse(checks["inventedPassMarkAllowed"])
        activity = self.skill_text["learning-activity-generator"]
        self.assertIn("Keine Behauptung psychometrischer Validität", activity)
        self.assertIn("Keine automatische Zertifizierung", activity)

    def test_conflicts_cannot_be_flattened_into_single_answer(self):
        self.assertFalse(self.fixture["knowledgeChecks"]["conflictedClaimSingleAnswerAllowed"])
        self.assertIn("unresolved material conflict cannot become a single-answer", self.spec)
        self.assertIn("nicht eine fälschlich eindeutige Antwort", self.skill_text["learning-activity-generator"])

    def test_course_design_prevents_fake_progress(self):
        self.assertIn("Do not fabricate completion percentages", self.design)
        self.assertIn("no fake progress/mastery metrics", self.design)
        self.assertFalse(self.fixture["acceptance"]["fakeProgressMetricsAllowed"])

    def test_cross_format_course_fingerprint_is_required(self):
        workflow = self.skill_text["youtube-course-builder-workflow"]
        self.assertIn("denselben unveränderlichen Course-Fingerprint", workflow)
        self.assertTrue(self.fixture["acceptance"]["sameCourseFingerprintAcrossFormats"])
        self.assertIn("same Course-Fingerprint across all renderers", self.spec)

    def test_hybrid_protocol_remains_forbidden(self):
        self.assertFalse(self.fixture["acceptance"]["hybridProtocolAllowed"])
        self.assertIn("hybrid procedure", self.spec)
        self.assertIn("keine neuen fachlichen Claims", self.skill_text["learning-activity-generator"])


if __name__ == "__main__":
    unittest.main()
