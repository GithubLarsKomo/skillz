from __future__ import annotations

import asyncio
import json
import unittest
from pathlib import Path

from mcp import Client

from skillz_mcp import create_server
from skillz_mcp.observability import LOGGER_NAME

ROOT = Path(__file__).resolve().parents[1]


class MCPObservabilityTests(unittest.TestCase):
    def test_structured_logs_include_identity_and_operations_but_not_arguments(self) -> None:
        secret_marker = "DO-NOT-LOG-THIS-ARGUMENT"

        async def run() -> None:
            with self.assertLogs(LOGGER_NAME, level="INFO") as captured:
                async with Client(create_server(ROOT)) as client:
                    result = await client.call_tool(
                        "search_skills",
                        {"query": secret_marker, "limit": 5},
                    )
                    self.assertFalse(result.is_error)
                    resource = await client.read_resource("skillz://status")
                    self.assertTrue(resource.contents)

            payloads = [json.loads(record.getMessage()) for record in captured.records]
            startup = [item for item in payloads if item.get("event") == "catalog_loaded"]
            self.assertEqual(len(startup), 1)
            self.assertEqual(startup[0]["indexSchemaVersion"], 1)
            self.assertEqual(len(startup[0]["catalogHash"]), 64)
            self.assertIn("skillCount", startup[0])

            tool_logs = [
                item
                for item in payloads
                if item.get("event") == "mcp_request"
                and item.get("method") == "tools/call"
                and item.get("identifier") == "search_skills"
            ]
            self.assertTrue(tool_logs)
            self.assertEqual(tool_logs[-1]["outcome"], "success")
            self.assertGreaterEqual(tool_logs[-1]["latencyMs"], 0)

            resource_logs = [
                item
                for item in payloads
                if item.get("event") == "mcp_request"
                and item.get("method") == "resources/read"
                and item.get("identifier") == "skillz://status"
            ]
            self.assertTrue(resource_logs)

            serialized = "\n".join(json.dumps(item, sort_keys=True) for item in payloads)
            self.assertNotIn(secret_marker, serialized)
            self.assertNotIn('"arguments"', serialized)

        asyncio.run(run())

    def test_errors_log_category_without_tool_arguments(self) -> None:
        secret_marker = "DO-NOT-LOG-THIS-UNKNOWN-SKILL"

        async def run() -> None:
            with self.assertLogs(LOGGER_NAME, level="WARNING") as captured:
                async with Client(create_server(ROOT)) as client:
                    result = await client.call_tool("get_skill", {"name": secret_marker})
                    self.assertTrue(result.is_error)

            payloads = [json.loads(record.getMessage()) for record in captured.records]
            errors = [
                item
                for item in payloads
                if item.get("event") == "mcp_request"
                and item.get("method") == "tools/call"
                and item.get("identifier") == "get_skill"
                and item.get("outcome") == "error"
            ]
            self.assertTrue(errors)
            self.assertTrue(errors[-1]["errorCategory"])
            serialized = "\n".join(json.dumps(item, sort_keys=True) for item in payloads)
            self.assertNotIn(secret_marker, serialized)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
