from __future__ import annotations

import asyncio
import json
import subprocess
import sys
import unittest
from pathlib import Path

from mcp import Client

from skillz_core import (
    get_skill,
    listing_payload,
    load_index,
    normalize_constraints,
    query_skill_listing,
    resolve,
)
from skillz_mcp import create_server

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "docs" / "skill-capability-index.json"
QUERY_CLI = ROOT / "scripts" / "query_capabilities.py"
RESOLVER_CLI = ROOT / "scripts" / "resolve_capabilities.py"


def run_json_cli(*args: str) -> dict:
    completed = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


class CLIMCPParityTests(unittest.TestCase):
    def test_query_cli_matches_core_exact_skill(self) -> None:
        index = load_index(INDEX_PATH)
        expected = get_skill(index, "disciplined-diagnosis")
        actual = run_json_cli(str(QUERY_CLI), "--skill", "disciplined-diagnosis", "--json")
        self.assertEqual(actual, expected)

    def test_query_cli_matches_core_listing(self) -> None:
        index = load_index(INDEX_PATH)
        mode, matches = query_skill_listing(index, "diagnosis")
        expected = listing_payload(mode, "diagnosis", matches)
        actual = run_json_cli(str(QUERY_CLI), "--skills", "diagnosis", "--json")
        self.assertEqual(actual, expected)

    def test_resolver_cli_matches_core(self) -> None:
        index = load_index(INDEX_PATH)
        constraints = normalize_constraints(["agent-handoff.json"], [], [], "irrelevant")
        expected = resolve(index, constraints)
        actual = run_json_cli(str(RESOLVER_CLI), "--output", "agent-handoff.json", "--json")
        self.assertEqual(actual, expected)

    def test_mcp_matches_core_for_discovery_and_resolver(self) -> None:
        async def run() -> None:
            index = load_index(INDEX_PATH)
            mode, matches = query_skill_listing(index, "diagnosis")
            expected_search = listing_payload(mode, "diagnosis", matches[:10])
            expected_skill = get_skill(index, "disciplined-diagnosis")
            constraints = normalize_constraints(["agent-handoff.json"], [], [], "irrelevant")
            expected_resolver = resolve(index, constraints)

            async with Client(create_server(ROOT)) as client:
                search = await client.call_tool("search_skills", {"query": "diagnosis", "limit": 10})
                self.assertFalse(search.is_error)
                self.assertEqual(search.structured_content, expected_search)

                detail = await client.call_tool("get_skill", {"name": "disciplined-diagnosis"})
                self.assertFalse(detail.is_error)
                self.assertIsNotNone(detail.structured_content)
                assert detail.structured_content is not None
                actual_skill = dict(detail.structured_content)
                resource_uris = actual_skill.pop("resourceUris")
                self.assertEqual(actual_skill, expected_skill)
                self.assertEqual(resource_uris, {
                    "metadata": "skillz://skills/disciplined-diagnosis",
                    "body": "skillz://skills/disciplined-diagnosis/SKILL.md",
                    "references": "skillz://skills/disciplined-diagnosis/references/",
                })

                resolved = await client.call_tool(
                    "resolve_capabilities",
                    {"outputs": ["agent-handoff.json"], "portable_files": "irrelevant"},
                )
                self.assertFalse(resolved.is_error)
                self.assertEqual(resolved.structured_content, expected_resolver)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
