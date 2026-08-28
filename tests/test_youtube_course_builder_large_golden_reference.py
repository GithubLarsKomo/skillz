from pathlib import Path
import ast
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "youtube-learning" / "pcr-qpcr-course-large-golden.json"
GENERATOR = ROOT / "scripts" / "generate_youtube_course_large_golden.py"
VERIFIER = ROOT / "scripts" / "verify_youtube_course_large_golden_render.py"


class TestYouTubeCourseBuilderLargeGoldenReference(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_real_source_set_has_twelve_unique_videos(self):
        sources = self.data["sources"]
        self.assertEqual(len(sources), 12)
        self.assertEqual(len({s["youtubeVideoId"] for s in sources}), 12)
        self.assertGreaterEqual(len({s["channel"] for s in sources}), 4)
        self.assertTrue(all(len(s["youtubeVideoId"]) == 11 for s in sources))

    def test_source_set_spans_pcr_and_qpcr_learning_roles(self):
        roles = {s["role"] for s in self.data["sources"]}
        for required in {"foundation-overview", "components", "primer-design", "laboratory-workflow", "qpcr-introduction", "experimental-planning", "error-sources", "validation", "normalization", "data-analysis", "melt-curve-interpretation"}:
            self.assertIn(required, roles)

    def test_module_path_is_not_source_or_playlist_order(self):
        self.assertFalse(self.data["pathRules"]["playlistOrderBinding"])
        self.assertEqual([m["moduleId"] for m in self.data["modules"]], [f"M{i}" for i in range(1, 9)])
        self.assertEqual(self.data["modules"][4]["state"], "variant")

    def test_prerequisite_graph_is_acyclic(self):
        modules = {m["moduleId"]: m for m in self.data["modules"]}
        visiting, visited = set(), set()
        def visit(mid):
            if mid in visiting:
                self.fail(f"cycle at {mid}")
            if mid in visited:
                return
            visiting.add(mid)
            for pre in modules[mid].get("prerequisites", []):
                self.assertIn(pre, modules)
                visit(pre)
            visiting.remove(mid); visited.add(mid)
        for mid in modules:
            visit(mid)
        self.assertEqual(len(visited), 8)

    def test_all_modules_have_objectives_exit_criteria_and_sources(self):
        objectives = self.data["learningObjectives"]
        for module in self.data["modules"]:
            self.assertTrue(module["competencePromise"])
            self.assertTrue(module["exitCriteria"])
            self.assertTrue(module["sourceScope"])
            for oid in module["objectives"]:
                self.assertIn(oid, objectives)

    def test_each_module_has_formative_evidence_bound_check(self):
        modules = {m["moduleId"] for m in self.data["modules"]}
        covered = set()
        for check in self.data["knowledgeChecks"]:
            self.assertIn(check["moduleId"], modules)
            self.assertTrue(check["objectiveIds"])
            self.assertTrue(check["sourceIds"])
            covered.add(check["moduleId"])
        self.assertEqual(covered, modules)

    def test_render_targets_cover_requested_surfaces(self):
        self.assertEqual(set(self.data["renderTargets"]), {"html", "svg", "pptx", "pptx-pdf", "docx", "pdf"})
        acceptance = self.data["acceptance"]
        self.assertTrue(acceptance["sameCourseFingerprintAcrossFormats"])
        self.assertTrue(acceptance["renderEverySlide"])
        self.assertTrue(acceptance["renderEveryDocumentPage"])
        self.assertTrue(acceptance["htmlWideAndNarrow"])

    def test_ci_is_deterministic_and_does_not_download_video(self):
        policy = self.data["sourcePolicy"]
        self.assertFalse(policy["liveDownloadInCi"])
        self.assertGreaterEqual(len(self.data["sources"]), policy["sourceCountMinimum"])
        self.assertLessEqual(len(self.data["sources"]), policy["sourceCountMaximum"])

    def test_generator_and_render_verifier_are_valid_python(self):
        for path in (GENERATOR, VERIFIER):
            self.assertTrue(path.is_file())
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


if __name__ == "__main__":
    unittest.main()
