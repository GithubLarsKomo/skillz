from __future__ import annotations

import asyncio
import json
import unittest
from pathlib import Path

from mcp import Client

from skillz_core import get_skill, load_index, query_skill_listing
from skillz_mcp import create_server

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "docs" / "skill-capability-index.json"


class MCPInitialSliceTests(unittest.TestCase):
    def test_core_loads_canonical_index_and_exact_skill(self) -> None:
        index = load_index(INDEX)
        self.assertEqual(index["schemaVersion"], 1)
        skill = get_skill(index, "disciplined-diagnosis")
        self.assertEqual(skill["name"], "disciplined-diagnosis")

    def test_core_search_preserves_user_facing_boundary(self) -> None:
        index = load_index(INDEX)
        mode, matches = query_skill_listing(index, "diagnosis")
        self.assertEqual(mode, "entrypoints")
        self.assertTrue(matches)
        self.assertTrue(all(item.get("invocation", {}).get("userFacing") is True for item in matches))

    def test_mcp_lists_and_calls_read_only_tools(self) -> None:
        async def run() -> None:
            server = create_server(ROOT)
            async with Client(server) as client:
                listed = await client.list_tools()
                names = {tool.name for tool in listed.tools}
                self.assertTrue(
                    {
                        "search_skills",
                        "get_skill",
                        "resolve_capabilities",
                        "get_dependencies",
                        "find_producers",
                        "find_consumers",
                        "catalog_status",
                        "validate_catalog",
                    }.issubset(names)
                )

                search = await client.call_tool("search_skills", {"query": "diagnosis", "limit": 10})
                self.assertFalse(search.is_error)
                self.assertIsNotNone(search.structured_content)
                assert search.structured_content is not None
                self.assertGreaterEqual(search.structured_content["count"], 1)

                detail = await client.call_tool("get_skill", {"name": "disciplined-diagnosis"})
                self.assertFalse(detail.is_error)
                self.assertIsNotNone(detail.structured_content)
                assert detail.structured_content is not None
                self.assertEqual(detail.structured_content["name"], "disciplined-diagnosis")
                self.assertTrue(detail.structured_content["resourceUris"]["body"].endswith("/SKILL.md"))

                resolved = await client.call_tool(
                    "resolve_capabilities",
                    {"outputs": ["agent-handoff.json"], "portable_files": "irrelevant"},
                )
                self.assertFalse(resolved.is_error)
                assert resolved.structured_content is not None
                self.assertIn("agent-handoff", [item["name"] for item in resolved.structured_content["candidates"]])

                dependencies = await client.call_tool(
                    "get_dependencies",
                    {"name": "agent-handoff", "direction": "requires", "transitive": False},
                )
                self.assertFalse(dependencies.is_error)
                assert dependencies.structured_content is not None
                self.assertIn("iterate-software-projects", dependencies.structured_content["skills"])

                producers = await client.call_tool("find_producers", {"output": "agent-handoff.json"})
                self.assertFalse(producers.is_error)
                assert producers.structured_content is not None
                self.assertEqual(producers.structured_content["producers"], ["agent-handoff"])
                self.assertFalse(producers.structured_content["ambiguous"])

                consumers = await client.call_tool("find_consumers", {"output": "agent-handoff.json"})
                self.assertFalse(consumers.is_error)
                assert consumers.structured_content is not None
                self.assertGreaterEqual(consumers.structured_content["contractCount"], 1)

                status = await client.call_tool("catalog_status", {})
                self.assertFalse(status.is_error)
                assert status.structured_content is not None
                self.assertEqual(status.structured_content["indexSchemaVersion"], 1)
                self.assertEqual(status.structured_content["graphSchemaVersion"], 1)
                self.assertEqual(len(status.structured_content["catalogHash"]), 64)
                self.assertIn(status.structured_content["freshness"], {"current", "stale", "unknown", "not-compared"})

                validation = await client.call_tool("validate_catalog", {})
                self.assertFalse(validation.is_error)
                assert validation.structured_content is not None
                self.assertTrue(validation.structured_content["valid"], validation.structured_content["errors"])
                self.assertEqual(validation.structured_content["errorCount"], 0)

        asyncio.run(run())

    def test_mcp_lists_and_reads_catalog_resources(self) -> None:
        async def run() -> None:
            async with Client(create_server(ROOT)) as client:
                listed = await client.list_resources()
                by_uri = {str(resource.uri): resource for resource in listed.resources}
                self.assertTrue({"skillz://index", "skillz://graph", "skillz://status"}.issubset(by_uri))
                for uri in ("skillz://index", "skillz://graph", "skillz://status"):
                    self.assertEqual(by_uri[uri].mime_type, "application/json")
                    self.assertIsNotNone(by_uri[uri].meta)

                index_result = await client.read_resource("skillz://index")
                index_payload = json.loads(index_result.contents[0].text)
                self.assertEqual(index_payload["schemaVersion"], 1)
                self.assertEqual(index_payload["skillCount"], 129)

                graph_result = await client.read_resource("skillz://graph")
                graph_payload = json.loads(graph_result.contents[0].text)
                self.assertEqual(graph_payload["schemaVersion"], 1)
                self.assertTrue(graph_payload["skills"])

                status_result = await client.read_resource("skillz://status")
                status_payload = json.loads(status_result.contents[0].text)
                self.assertEqual(len(status_payload["catalogHash"]), 64)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
