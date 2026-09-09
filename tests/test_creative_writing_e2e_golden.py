from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "benchmarks" / "creative-writing-e2e-golden-v1.json"
RENDERER = (
    ROOT
    / "skills"
    / "epub3-publication-renderer"
    / "scripts"
    / "render_epub3.py"
)


class CreativeWritingE2EGoldenTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads(
            (ROOT / "docs" / "skill-capability-index.json").read_text(encoding="utf-8")
        )
        cls.skills = {skill["name"]: skill for skill in cls.index["skills"]}
        cls.benchmark = json.loads(BENCHMARK.read_text(encoding="utf-8"))

    def requires_closure(self, name: str) -> set[str]:
        seen: set[str] = set()
        pending = list(self.skills[name]["requires"])
        while pending:
            dependency = pending.pop()
            if dependency in seen:
                continue
            self.assertIn(dependency, self.skills, f"{name}: missing required skill {dependency}")
            seen.add(dependency)
            pending.extend(self.skills[dependency]["requires"])
        return seen

    def scenario(self, scenario_id: str) -> dict:
        return next(
            scenario
            for scenario in self.benchmark["scenarios"]
            if scenario["id"] == scenario_id
        )

    def test_golden_scenarios_have_distinct_identity_and_domain(self):
        scenarios = self.benchmark["scenarios"]
        self.assertEqual(len(scenarios), 2)
        self.assertEqual(
            len({scenario["id"] for scenario in scenarios}),
            len(scenarios),
        )
        self.assertEqual(
            len({scenario["domain"] for scenario in scenarios}),
            len(scenarios),
        )

    def test_entrypoint_and_all_sequence_workers_are_active_and_evaluated(self):
        for scenario in self.benchmark["scenarios"]:
            entrypoint = self.skills[scenario["entrypoint"]]
            self.assertTrue(entrypoint["invocation"]["userFacing"], scenario["id"])
            self.assertIn(
                entrypoint["governance"]["discoverability"],
                {"public", "advanced"},
                scenario["id"],
            )
            self.assertNotEqual(
                entrypoint["governance"]["status"],
                "deprecated",
                scenario["id"],
            )
            self.assertTrue(entrypoint["evaluation"]["passed"], scenario["id"])

            closure = self.requires_closure(scenario["entrypoint"])
            self.assertEqual(
                len(scenario["sequence"]),
                len(set(scenario["sequence"])),
                scenario["id"],
            )
            for name in scenario["sequence"]:
                self.assertIn(
                    name,
                    closure,
                    f"{scenario['id']}: {name} is outside entrypoint requires closure",
                )
                skill = self.skills[name]
                self.assertNotEqual(
                    skill["governance"]["discoverability"],
                    "compatibility",
                    f"{scenario['id']}: {name}",
                )
                self.assertNotEqual(
                    skill["governance"]["status"],
                    "deprecated",
                    f"{scenario['id']}: {name}",
                )
                self.assertTrue(skill["evaluation"]["passed"], f"{scenario['id']}: {name}")

    def test_science_golden_preserves_evidence_and_fidelity_boundaries(self):
        scenario = self.scenario("science-storytelling-to-elevenreader-epub")
        sequence = scenario["sequence"]

        required = {
            "round-based-requirements-grilling",
            "research-to-evidence-note",
            "science-storytelling-workflow",
            "creative-writing-workshop",
            "creative-prose-revision",
            "precision-writing-revision",
            "creative-writing-epub-delivery",
        }
        self.assertTrue(required.issubset(sequence))
        self.assertNotIn("fiction-series-writing-workflow", sequence)
        self.assertNotIn("story-bible-continuity", sequence)
        self.assertIn(
            "research-to-evidence-note",
            self.skills["science-storytelling-workflow"]["requires"],
        )
        self.assertIn(
            "precision-writing-revision",
            self.skills["science-storytelling-workflow"]["requires"],
        )

    def test_fiction_golden_preserves_canon_knowledge_and_project_memory_boundaries(self):
        scenario = self.scenario("multivolume-fiction-to-elevenreader-epub")
        sequence = scenario["sequence"]

        required = {
            "speculative-worldbuilding",
            "ensemble-character-architecture",
            "character-voice-fingerprint",
            "series-architecture",
            "fiction-series-writing-workflow",
            "creative-writing-workshop",
            "creative-prose-revision",
            "story-bible-continuity",
            "fiction-reader-reality-review",
            "fiction-award-jury-review",
            "creative-revision-regression",
            "project-second-brain",
            "creative-writing-epub-delivery",
        }
        self.assertTrue(required.issubset(sequence))
        self.assertNotIn("science-storytelling-workflow", sequence)
        self.assertNotIn("research-to-evidence-note", sequence)

        continuity = self.skills["story-bible-continuity"]
        self.assertTrue(
            {
                "speculative-worldbuilding",
                "ensemble-character-architecture",
                "series-architecture",
            }.issubset(continuity["requires"])
        )
        self.assertTrue(
            {
                "story-bible-index.json",
                "knowledge-state.json",
                "continuity-review.json",
                "canon-impact-analysis.json",
            }.issubset(continuity["outputs"])
        )

        fiction = self.skills["fiction-series-writing-workflow"]
        self.assertTrue(
            {
                "character-voice-fingerprint",
                "fiction-reader-reality-review",
                "creative-revision-regression",
                "fiction-award-jury-review",
            }.issubset(fiction["requires"])
        )

        voice = self.skills["character-voice-fingerprint"]
        self.assertIn("ensemble-character-architecture", voice["requires"])
        self.assertTrue(
            {
                "character-voice-fingerprint.json",
                "voice-collision-register.json",
                "character-voice-audit.json",
            }.issubset(voice["outputs"])
        )

        reader = self.skills["fiction-reader-reality-review"]
        self.assertTrue(
            {
                "reader-emotional-ledger.json",
                "reader-character-reconstruction.md",
                "reader-vs-architecture-comparison.json",
                "reader-reality-gate.json",
            }.issubset(reader["outputs"])
        )

        regression = self.skills["creative-revision-regression"]
        self.assertIn("creative-prose-revision", regression["requires"])
        self.assertTrue(
            {
                "revision-impact-classification.json",
                "gate-invalidation-map.json",
                "creative-revision-regression.json",
            }.issubset(regression["outputs"])
        )

        award = self.skills["fiction-award-jury-review"]
        self.assertIn("creative-revision-regression", award["requires"])

    def test_fiction_golden_orders_reader_before_award_and_regression(self):
        sequence = self.scenario("multivolume-fiction-to-elevenreader-epub")["sequence"]
        self.assertLess(
            sequence.index("character-voice-fingerprint"),
            sequence.index("fiction-series-writing-workflow"),
        )
        self.assertLess(
            sequence.index("fiction-reader-reality-review"),
            sequence.index("fiction-award-jury-review"),
        )
        self.assertLess(
            sequence.index("fiction-award-jury-review"),
            sequence.index("creative-revision-regression"),
        )

    def test_delivery_owns_public_epub_and_delegates_listener_and_renderer(self):
        root_outputs = set(self.skills["creative-writing-workflow"]["outputs"])
        delivery = self.skills["creative-writing-epub-delivery"]
        renderer = self.skills["epub3-publication-renderer"]

        self.assertNotIn("creative-writing.epub", root_outputs)
        self.assertIn("creative-writing.epub", delivery["outputs"])
        self.assertEqual(
            set(delivery["requires"]),
            {"narrative-audiobook-listener-review", "epub3-publication-renderer"},
        )
        self.assertIn("epub3-publication.epub", renderer["outputs"])
        self.assertTrue(
            all(not contract["ambiguous"] for contract in delivery["outputContracts"])
        )
        self.assertTrue(
            all(not contract["ambiguous"] for contract in renderer["outputContracts"])
        )

    def test_audio_tutorial_and_creative_writing_share_one_epub_renderer(self):
        audio = self.skills["audio-tutorial-workflow"]
        self.assertIn("epub3-publication-renderer", audio["requires"])
        self.assertFalse(
            (
                ROOT
                / "skills"
                / "audio-tutorial-workflow"
                / "scripts"
                / "render_epub.py"
            ).exists()
        )

    def test_behavioral_invariants_are_not_placeholders(self):
        for scenario in self.benchmark["scenarios"]:
            self.assertGreaterEqual(len(scenario["mustPreserve"]), 4, scenario["id"])
            self.assertGreaterEqual(len(scenario["mustNotDo"]), 3, scenario["id"])
            for statement in scenario["mustPreserve"] + scenario["mustNotDo"]:
                self.assertGreaterEqual(len(statement.strip()), 24, scenario["id"])

    def test_epub_renderer_executes_and_preserves_narrative_semantics(self):
        spec = importlib.util.spec_from_file_location(
            "skillz_epub3_publication_renderer",
            RENDERER,
        )
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        manuscript = """# The Signal Beyond the Ice
## A Golden Test

# Chapter One

Mara held the sample to the light. The label read **β-Amyloid**.

*Nothing about this was simple*, she thought.

---

"Do you hear it?" Tom asked.

# Chapter Two

The answer arrived much later, and it did not arrive as a number.
"""

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "manuscript.md"
            epub = tmp_path / "book.epub"
            validation_path = tmp_path / "validation.json"
            source.write_text(manuscript, encoding="utf-8")

            module.render_epub(
                source,
                epub,
                validation_path,
                "Golden Test Author",
                "en-US",
            )

            validation = json.loads(validation_path.read_text(encoding="utf-8"))
            self.assertEqual(validation["structuralStatus"], "pass")
            self.assertEqual(
                validation["elevenReaderCompatibility"],
                "structural-pass",
            )
            self.assertEqual(validation["chapterCount"], 2)
            self.assertTrue(validation["mimetypeFirst"])
            self.assertTrue(validation["mimetypeStored"])
            self.assertTrue(validation["requiredFilesPresent"])
            self.assertTrue(validation["xmlParsePass"])
            self.assertTrue(validation["navigationPresent"])
            self.assertTrue(validation["ncxPresent"])
            self.assertTrue(validation["javascriptFree"])

            with zipfile.ZipFile(epub, "r") as archive:
                infos = archive.infolist()
                self.assertEqual(infos[0].filename, "mimetype")
                self.assertEqual(infos[0].compress_type, zipfile.ZIP_STORED)
                chapter_one = archive.read("OEBPS/chapter_001.xhtml").decode("utf-8")
                chapter_two = archive.read("OEBPS/chapter_002.xhtml").decode("utf-8")
                nav = archive.read("OEBPS/nav.xhtml").decode("utf-8")

            self.assertIn("β-Amyloid", chapter_one)
            self.assertIn("<em>Nothing about this was simple</em>", chapter_one)
            self.assertIn('<hr class="scene-break"/>', chapter_one)
            self.assertIn('"Do you hear it?" Tom asked.', chapter_one)
            self.assertIn(
                "The answer arrived much later, and it did not arrive as a number.",
                chapter_two,
            )
            self.assertIn("Chapter One", nav)
            self.assertIn("Chapter Two", nav)


if __name__ == "__main__":
    unittest.main()
