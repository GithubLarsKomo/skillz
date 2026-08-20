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
                self.assertEqual(index_payload["skillCount"], len(index_payload["skills"]))
                self.assertGreater(index_payload["skillCount"], 0)

                graph_result = await client.read_resource("skillz://graph")
                graph_payload = json.loads(graph_result.contents[0].text)
                self.assertEqual(graph_payload["schemaVersion"], 1)
                self.assertTrue(graph_payload["skills"])

                status_result = await client.read_resource("skillz://status")
                status_payload = json.loads(status_result.contents[0].text)
                self.assertEqual(len(status_payload["catalogHash"]), 64)

        asyncio.run(run())

    def test_mcp_skill_resources_support_progressive_disclosure(self) -> None:
        async def run() -> None:
            async with Client(create_server(ROOT)) as client:
                templates = await client.list_resource_templates()
                template_uris = {template.uri_template for template in templates.resource_templates}
                self.assertTrue(
                    {
                        "skillz://skills/{name}",
                        "skillz://skills/{name}/SKILL.md",
                        "skillz://skills/{name}/references/{+relative_path}",
                        "skillz://skills/{name}/assets/{+relative_path}",
                    }.issubset(template_uris)
                )

                metadata_result = await client.read_resource("skillz://skills/disciplined-diagnosis")
                metadata = json.loads(metadata_result.contents[0].text)
                self.assertEqual(metadata["name"], "disciplined-diagnosis")
                self.assertEqual(metadata["resourceUris"]["body"], "skillz://skills/disciplined-diagnosis/SKILL.md")

                body_result = await client.read_resource("skillz://skills/disciplined-diagnosis/SKILL.md")
                body = body_result.contents[0].text
                self.assertIn("name: disciplined-diagnosis", body)
                self.assertGreater(len(body), 100)

                reference_result = await client.read_resource(
                    "skillz://skills/dr-komorowski-sport-report-renderer/references/brand-guide.md"
                )
                self.assertGreater(len(reference_result.contents[0].text), 100)

                assets_result = await client.read_resource(
                    "skillz://skills/dr-komorowski-sport-report-renderer/assets"
                )
                assets = json.loads(assets_result.contents[0].text)
                self.assertEqual(assets["skill"], "dr-komorowski-sport-report-renderer")
                self.assertEqual(assets["type"], "directory")
                asset_names = {entry["name"] for entry in assets["entries"]}
                self.assertIn("dr-komorowski-logo.svg", asset_names)

                asset_metadata_result = await client.read_resource(
                    "skillz://skills/dr-komorowski-sport-report-renderer/assets/dr-komorowski-logo.svg"
                )
                asset_metadata = json.loads(asset_metadata_result.contents[0].text)
                self.assertEqual(asset_metadata["type"], "file")
                self.assertGreater(asset_metadata["size"], 0)
                self.assertNotIn("content", asset_metadata)
                self.assertNotIn("bytes", asset_metadata)

                with self.assertRaises(Exception):
                    await client.read_resource("skillz://skills/not-a-real-skill")
                with self.assertRaises(Exception):
                    await client.read_resource(
                        "skillz://skills/dr-komorowski-sport-report-renderer/references/%252e%252e%2FSKILL.md"
                    )

        asyncio.run(run())

    def test_mcp_repository_metadata_resources_are_narrow_and_text_only(self) -> None:
        async def run() -> None:
            async with Client(create_server(ROOT)) as client:
                templates = await client.list_resource_templates()
                template_uris = {template.uri_template for template in templates.resource_templates}
                self.assertTrue(
                    {
                        "skillz://schemas/{name}",
                        "skillz://contracts/{name}",
                        "skillz://docs/{name}",
                    }.issubset(template_uris)
                )

                schema_result = await client.read_resource("skillz://schemas/capability-intent-v1.schema.json")
                schema_payload = json.loads(schema_result.contents[0].text)
                self.assertIsInstance(schema_payload, dict)

                contract_result = await client.read_resource(
                    "skillz://contracts/compliance-traceability-v1.schema.json"
                )
                contract_payload = json.loads(contract_result.contents[0].text)
                self.assertIsInstance(contract_payload, dict)

                docs_result = await client.read_resource("skillz://docs/MCP-ARCHITECTURE.md")
                self.assertIn("MCP", docs_result.contents[0].text)

                for uri in (
                    "skillz://schemas/capability-intent-v1.txt",
                    "skillz://contracts/compliance-traceability-v1.txt",
                    "skillz://docs/MCP-ARCHITECTURE.json",
                    "skillz://docs/%252e%252e%2FVERSION.md",
                ):
                    with self.subTest(uri=uri):
                        with self.assertRaises(Exception):
                            await client.read_resource(uri)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
