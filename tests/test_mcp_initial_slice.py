from __future__ import annotations

import asyncio
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

    def test_mcp_lists_and_calls_initial_tools(self) -> None:
        async def run() -> None:
            server = create_server(ROOT)
            async with Client(server) as client:
                listed = await client.list_tools()
                names = {tool.name for tool in listed.tools}
                self.assertTrue({"search_skills", "get_skill"}.issubset(names))

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

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
