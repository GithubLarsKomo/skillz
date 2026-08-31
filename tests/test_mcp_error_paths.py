from __future__ import annotations

import asyncio
import unittest
from pathlib import Path

from mcp import Client

from skillz_mcp import create_server

ROOT = Path(__file__).resolve().parents[1]


class MCPErrorPathTests(unittest.TestCase):
    def test_tool_errors_are_explicit_protocol_errors(self) -> None:
        async def run() -> None:
            async with Client(create_server(ROOT)) as client:
                cases = [
                    ("search_skills", {"query": "diagnosis", "limit": 0}),
                    ("get_skill", {"name": "not-a-real-skill"}),
                    ("resolve_capabilities", {"outputs": ["not-a-real-output"]}),
                    ("get_dependencies", {"name": "not-a-real-skill"}),
                    ("find_producers", {"output": "not-a-real-output"}),
                    (
                        "find_consumers",
                        {"output": "agent-handoff.json", "producer": "disciplined-diagnosis"},
                    ),
                ]
                for tool_name, arguments in cases:
                    with self.subTest(tool=tool_name):
                        result = await client.call_tool(tool_name, arguments)
                        self.assertTrue(result.is_error)
                        self.assertTrue(result.content)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
