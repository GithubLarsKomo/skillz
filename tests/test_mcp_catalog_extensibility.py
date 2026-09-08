from __future__ import annotations

import asyncio
import json
import tempfile
import unittest
from pathlib import Path

from mcp import Client

from skillz_mcp import create_server

ROOT = Path(__file__).resolve().parents[1]
SYNTHETIC_SKILL = "mcp-index-only-fixture"


class MCPCatalogExtensibilityTests(unittest.TestCase):
    def test_new_indexed_skill_is_discoverable_without_server_code_changes(self) -> None:
        async def run() -> None:
            with tempfile.TemporaryDirectory() as td:
                repo = Path(td)
                docs = repo / "docs"
                skills = repo / "skills"
                docs.mkdir(parents=True)
                (skills / SYNTHETIC_SKILL).mkdir(parents=True)

                index = json.loads((ROOT / "docs" / "skill-capability-index.json").read_text(encoding="utf-8"))
                graph = json.loads((ROOT / "docs" / "skill-dependency-graph.json").read_text(encoding="utf-8"))

                index["skills"].append(
                    {
                        "name": SYNTHETIC_SKILL,
                        "description": "Synthetic entrypoint added only through canonical generated metadata.",
                        "invocation": {"userFacing": True, "category": "test-fixture"},
                        "requires": [],
                        "outputs": [],
                        "outputContracts": [],
                        "portableFiles": [],
                    }
                )
                index["skillCount"] = len(index["skills"])
                index["entrypointCount"] = int(index.get("entrypointCount", 0)) + 1
                graph["skills"].append({"name": SYNTHETIC_SKILL, "requires": [], "outputs": []})

                (docs / "skill-capability-index.json").write_text(
                    json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
                )
                (docs / "skill-dependency-graph.json").write_text(
                    json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
                )
                (repo / "VERSION").write_text((ROOT / "VERSION").read_text(encoding="utf-8"), encoding="utf-8")
                (skills / SYNTHETIC_SKILL / "SKILL.md").write_text(
                    "---\n"
                    f"name: {SYNTHETIC_SKILL}\n"
                    "description: Synthetic entrypoint added only through canonical generated metadata.\n"
                    "---\n\n"
                    "# MCP index-only fixture\n",
                    encoding="utf-8",
                )

                async with Client(create_server(repo)) as client:
                    search = await client.call_tool("search_skills", {"query": "index-only fixture"})
                    self.assertFalse(search.is_error)
                    assert search.structured_content is not None
                    names = {
                        skill["name"]
                        for category in search.structured_content["categories"]
                        for skill in category["skills"]
                    }
                    self.assertIn(SYNTHETIC_SKILL, names)

                    detail = await client.call_tool("get_skill", {"name": SYNTHETIC_SKILL})
                    self.assertFalse(detail.is_error)
                    assert detail.structured_content is not None
                    self.assertEqual(detail.structured_content["name"], SYNTHETIC_SKILL)

                    body = await client.read_resource(f"skillz://skills/{SYNTHETIC_SKILL}/SKILL.md")
                    self.assertIn("# MCP index-only fixture", body.contents[0].text)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
