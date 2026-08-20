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


async def wait_for_port(host: str, port: int) -> None:
    for _ in range(50):
        try:
            reader, writer = await asyncio.open_connection(host, port)
            writer.close()
            await writer.wait_closed()
            return
        except OSError:
            await asyncio.sleep(0.1)
    raise AssertionError("HTTP MCP server did not become reachable")


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
                await wait_for_port("127.0.0.1", port)
                async with Client(url) as client:
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
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=5)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
