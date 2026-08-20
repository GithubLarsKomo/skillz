from __future__ import annotations

import asyncio
import socket
import subprocess
import sys
import unittest
from pathlib import Path

from mcp import Client

ROOT = Path(__file__).resolve().parents[1]


def free_local_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


class MCPHTTPIntegrationTests(unittest.TestCase):
    def test_stateless_streamable_http_serves_same_read_only_surface(self) -> None:
        async def run() -> None:
            port = free_local_port()
            process = subprocess.Popen(
                [
                    sys.executable,
                    "-m",
                    "skillz_mcp",
                    "--repository-root",
                    str(ROOT),
                    "--transport",
                    "streamable-http",
                    "--host",
                    "127.0.0.1",
                    "--port",
                    str(port),
                ],
                cwd=ROOT,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            url = f"http://127.0.0.1:{port}/mcp"
            try:
                client: Client | None = None
                for _ in range(40):
                    try:
                        candidate = Client(url)
                        await candidate.__aenter__()
                        client = candidate
                        break
                    except Exception:
                        await asyncio.sleep(0.1)
                self.assertIsNotNone(client, "HTTP MCP server did not become reachable")
                assert client is not None
                try:
                    tools = await client.list_tools()
                    names = {tool.name for tool in tools.tools}
                    self.assertIn("search_skills", names)
                    self.assertIn("catalog_status", names)

                    status = await client.call_tool("catalog_status", {})
                    self.assertFalse(status.is_error)
                    assert status.structured_content is not None
                    self.assertEqual(status.structured_content["indexSchemaVersion"], 1)

                    resource = await client.read_resource("skillz://status")
                    self.assertTrue(resource.contents)
                finally:
                    await client.__aexit__(None, None, None)
            finally:
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=5)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
