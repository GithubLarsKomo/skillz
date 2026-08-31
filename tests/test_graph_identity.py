from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from skillz_core import catalog_hash, catalog_identity, consumer_info, dependency_traversal, freshness, producer_info


class GraphAndIdentityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = {
            "schemaVersion": 1,
            "skills": [
                {"name": "alpha", "requires": ["beta", "gamma"], "outputs": ["shared.json"]},
                {"name": "beta", "requires": ["delta"], "outputs": []},
                {"name": "gamma", "requires": ["delta"], "outputs": ["shared.json"]},
                {"name": "delta", "requires": ["alpha"], "outputs": []},
            ],
        }
        contract = {
            "output": "shared.json",
            "ambiguous": True,
            "producers": ["alpha", "gamma"],
            "consumerSkills": ["consumer-b", "consumer-a"],
        }
        self.index = {
            "schemaVersion": 1,
            "skillCount": 4,
            "entrypointCount": 2,
            "evaluationSuiteCount": 4,
            "evaluationPassed": True,
            "evaluationErrorCount": 0,
            "skills": [
                {"name": "alpha", "outputs": ["shared.json"], "outputContracts": [contract]},
                {"name": "beta", "outputs": [], "outputContracts": []},
                {"name": "gamma", "outputs": ["shared.json"], "outputContracts": [contract]},
                {"name": "delta", "outputs": [], "outputContracts": []},
            ],
        }

    def test_direct_and_transitive_traversal_are_deterministic_and_cycle_safe(self) -> None:
        direct = dependency_traversal(self.graph, "alpha", direction="requires", transitive=False)
        self.assertEqual(direct["skills"], ["beta", "gamma"])
        transitive = dependency_traversal(self.graph, "alpha", direction="requires", transitive=True)
        self.assertEqual(transitive["skills"], ["beta", "gamma", "delta"])
        self.assertEqual([item["depth"] for item in transitive["traversal"]], [1, 1, 2])

    def test_reverse_dependents_are_derived_from_declared_requires(self) -> None:
        payload = dependency_traversal(self.graph, "delta", direction="dependents", transitive=False)
        self.assertEqual(payload["skills"], ["beta", "gamma"])

    def test_unknown_skill_and_direction_fail_explicitly(self) -> None:
        with self.assertRaisesRegex(LookupError, "unknown skill"):
            dependency_traversal(self.graph, "missing")
        with self.assertRaisesRegex(ValueError, "direction"):
            dependency_traversal(self.graph, "alpha", direction="sideways")

    def test_producers_preserve_ambiguity_without_ranking(self) -> None:
        payload = producer_info(self.index, "shared.json")
        self.assertTrue(payload["ambiguous"])
        self.assertEqual(payload["producers"], ["alpha", "gamma"])

    def test_consumers_come_only_from_output_contracts_and_validate_producer(self) -> None:
        payload = consumer_info(self.index, "shared.json", producer="alpha")
        self.assertEqual(payload["consumers"], ["consumer-a", "consumer-b"])
        with self.assertRaisesRegex(ValueError, "does not produce"):
            consumer_info(self.index, "shared.json", producer="beta")

    def test_catalog_hash_is_deterministic_and_graph_sensitive(self) -> None:
        first = catalog_hash(self.index, self.graph)
        second = catalog_hash(dict(reversed(list(self.index.items()))), dict(reversed(list(self.graph.items()))))
        self.assertEqual(first, second)
        changed = {**self.graph, "skills": self.graph["skills"] + [{"name": "epsilon", "requires": [], "outputs": []}]}
        self.assertNotEqual(first, catalog_hash(self.index, changed))

    def test_freshness_requires_exact_commit_evidence_for_current(self) -> None:
        commit = "a" * 40
        self.assertEqual(freshness(catalog_commit=commit, runtime_commit=commit, catalog_version="1", runtime_version="1"), "current")
        self.assertEqual(freshness(catalog_commit=commit, runtime_commit="b" * 40, catalog_version="1", runtime_version="1"), "stale")
        self.assertEqual(freshness(catalog_commit=None, runtime_commit=None, catalog_version="1", runtime_version="1"), "unknown")
        self.assertEqual(freshness(catalog_commit=None, runtime_commit=None, catalog_version=None, runtime_version=None), "not-compared")

    def test_catalog_identity_reports_counts_hash_and_fail_closed_freshness(self) -> None:
        commit = "c" * 40
        index = {**self.index, "provenance": {"repository": "example/repo", "ref": "refs/heads/main", "version": "1.2.3", "commitSha": commit}}
        with tempfile.TemporaryDirectory() as td:
            version_path = Path(td) / "VERSION"
            version_path.write_text("9.9.9\n", encoding="utf-8")
            payload = catalog_identity(index, self.graph, version_path=version_path, runtime_commit=commit, runtime_version="1.2.3")
        self.assertEqual(payload["repository"], "example/repo")
        self.assertEqual(payload["version"], "1.2.3")
        self.assertEqual(payload["skillCount"], 4)
        self.assertEqual(payload["freshness"], "current")
        self.assertEqual(len(payload["catalogHash"]), 64)


if __name__ == "__main__":
    unittest.main()
