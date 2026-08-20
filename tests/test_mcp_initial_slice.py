from __future__ import annotations

import asyncio
from pathlib import Path

from mcp import Client

from skillz_core import get_skill, load_index, query_skill_listing
from skillz_mcp import create_server

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "docs" / "skill-capability-index.json"


def test_core_loads_canonical_index_and_exact_skill() -> None:
    index = load_index(INDEX)
    assert index["schemaVersion"] == 1
    skill = get_skill(index, "disciplined-diagnosis")
    assert skill["name"] == "disciplined-diagnosis"


def test_core_search_preserves_user_facing_boundary() -> None:
    index = load_index(INDEX)
    mode, matches = query_skill_listing(index, "diagnosis")
    assert mode == "entrypoints"
    assert matches
    assert all(item.get("invocation", {}).get("userFacing") is True for item in matches)


def test_mcp_lists_and_calls_initial_tools() -> None:
    async def run() -> None:
        server = create_server(ROOT)
        async with Client(server) as client:
            listed = await client.list_tools()
            names = {tool.name for tool in listed.tools}
            assert {"search_skills", "get_skill"}.issubset(names)

            search = await client.call_tool("search_skills", {"query": "diagnosis", "limit": 10})
            assert search.is_error is False
            assert search.structured_content is not None
            assert search.structured_content["count"] >= 1

            detail = await client.call_tool("get_skill", {"name": "disciplined-diagnosis"})
            assert detail.is_error is False
            assert detail.structured_content is not None
            assert detail.structured_content["name"] == "disciplined-diagnosis"
            assert detail.structured_content["resourceUris"]["body"].endswith("/SKILL.md")

    asyncio.run(run())
