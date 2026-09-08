from __future__ import annotations

import asyncio
import json
import sys
import unittest
from pathlib import Path

from mcp import Client, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parents[1]


class MCPStdioSmokeTests(unittest.TestCase):
    def test_installed_module_serves_tools_and_resources_over_stdio(self) -> None:
        async def run() -> None:
            parameters = StdioServerParameters(
                command=sys.executable,
                args=["-m", "skillz_mcp", "--repository-root", str(ROOT)],
                cwd=ROOT,
            )
            async with Client(stdio_client(parameters)) as client:
                self.assertIsNotNone(client.server_info)
                assert client.server_info is not None
                self.assertEqual(client.server_info.name, "skillz-mcp")

                tools = await client.list_tools()
                tool_names = {tool.name for tool in tools.tools}
                self.assertIn("search_skills", tool_names)
                self.assertIn("catalog_status", tool_names)

                status = await client.read_resource("skillz://status")
                payload = json.loads(status.contents[0].text)
                self.assertEqual(payload["indexSchemaVersion"], 1)
                self.assertEqual(len(payload["catalogHash"]), 64)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
