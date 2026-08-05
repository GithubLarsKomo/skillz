from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from query_capabilities import (  # noqa: E402
    get_skill,
    invocation,
    listing_payload,
    load_index,
    main,
    names,
    query_mode,
    query_output,
    query_portable,
    query_requires,
    query_skill_listing,
)


INDEX = {
    "schemaVersion": 1,
    "skills": [
        {
            "name": "alpha",
            "description": "Alpha engineering entrypoint",
            "invocation": {"userFacing": True, "category": "engineering"},
            "requires": [],
            "dependents": ["beta"],
            "outputs": ["shared", "alpha-out"],
            "portableFiles": ["references/a.md"],
            "evaluation": {"mode": "rubric", "passed": True},
        },
        {
            "name": "beta",
            "description": "Beta internal helper",
            "invocation": {"userFacing": False, "category": None},
            "requires": ["alpha"],
            "dependents": [],
            "outputs": ["shared"],
            "portableFiles": [],
            "evaluation": {"mode": "compatibility", "passed": True},
        },
        {
            "name": "medical-device-example",
            "description": "Medical device regulatory specialist",
            "invocation": {"userFacing": True, "category": "regulated-engineering"},
            "requires": [],
            "dependents": [],
            "outputs": [],
            "portableFiles": [],
            "evaluation": {"mode": "none", "passed": None},
        },
    ],
}


class CapabilityQueryTests(unittest.TestCase):
    def write_index(self, root: Path, data: dict | None = None) -> Path:
        path = root / "index.json"
        path.write_text(json.dumps(data or INDEX), encoding="utf-8")
        return path

    def test_skill_and_dependency_queries(self):
        self.assertEqual(get_skill(INDEX, "alpha")["dependents"], ["beta"])
        self.assertEqual(names(query_requires(INDEX, "alpha")), ["beta"])
        self.assertTrue(invocation(get_skill(INDEX, "alpha"))["userFacing"])

    def test_unknown_skill_fails(self):
        with self.assertRaisesRegex(LookupError, "unknown skill"):
            get_skill(INDEX, "missing")
        with self.assertRaisesRegex(LookupError, "unknown skill"):
            query_requires(INDEX, "missing")

    def test_output_lookup_preserves_ambiguous_producers_deterministically(self):
        self.assertEqual(names(query_output(INDEX, "shared")), ["alpha", "beta"])
        with self.assertRaisesRegex(LookupError, "unknown output"):
            query_output(INDEX, "missing")

    def test_evaluation_mode_filtering(self):
        self.assertEqual(names(query_mode(INDEX, "rubric")), ["alpha"])
        self.assertEqual(names(query_mode(INDEX, "compatibility")), ["beta"])
        self.assertEqual(names(query_mode(INDEX, "none")), ["medical-device-example"])

    def test_portable_file_filtering(self):
        self.assertEqual(names(query_portable(INDEX, True)), ["alpha"])
        self.assertEqual(names(query_portable(INDEX, False)), ["beta", "medical-device-example"])

    def test_default_skills_lists_only_user_facing_entrypoints(self):
        mode, matches = query_skill_listing(INDEX, "")
        self.assertEqual(mode, "entrypoints")
        self.assertEqual(names(matches), ["alpha", "medical-device-example"])
        payload = listing_payload(mode, "", matches)
        self.assertEqual([row["category"] for row in payload["categories"]], ["engineering", "regulated-engineering"])

    def test_skills_query_filters_name_description_and_category(self):
        _, medical = query_skill_listing(INDEX, "medical")
        self.assertEqual(names(medical), ["medical-device-example"])
        _, regulated = query_skill_listing(INDEX, "regulated engineering")
        self.assertEqual(names(regulated), ["medical-device-example"])

    def test_skills_all_includes_internal_without_promoting_it(self):
        mode, matches = query_skill_listing(INDEX, "all")
        self.assertEqual(mode, "all")
        self.assertEqual(names(matches), ["alpha", "beta", "medical-device-example"])
        payload = listing_payload(mode, "all", matches)
        internal = next(group for group in payload["categories"] if group["category"] == "internal")
        self.assertEqual(internal["skills"], [{"name": "beta", "description": "Beta internal helper", "userFacing": False}])

    def test_unsupported_schema_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = self.write_index(root, {"schemaVersion": 2, "skills": []})
            with self.assertRaisesRegex(ValueError, "unsupported capability index schemaVersion"):
                load_index(path)

    def test_cli_returns_nonzero_for_unknown_skill_and_accepts_slash_equivalent_queries(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_index(Path(tmp))
            self.assertEqual(main(["--index", str(path), "--skill", "missing"]), 2)
            self.assertEqual(main(["--index", str(path), "--output", "shared", "--json"]), 0)
            self.assertEqual(main(["--index", str(path), "--skills", "--json"]), 0)
            self.assertEqual(main(["--index", str(path), "--skills", "medical", "--json"]), 0)
            self.assertEqual(main(["--index", str(path), "--skills", "all", "--json"]), 0)


if __name__ == "__main__":
    unittest.main()
