from __future__ import annotations

from pathlib import Path

from mcp.server import MCPServer

from skillz_core import get_skill, invocation, listing_payload, load_index, query_skill_listing

DEFAULT_ROOT = Path(__file__).resolve().parents[2]


def create_server(repository_root: Path | None = None) -> MCPServer:
    root = (repository_root or DEFAULT_ROOT).resolve()
    index_path = root / "docs" / "skill-capability-index.json"
    index = load_index(index_path)
    server = MCPServer("skillz-mcp")

    @server.tool()
    def search_skills(
        query: str = "",
        category: str | None = None,
        include_internal: bool = False,
        limit: int = 25,
    ) -> dict:
        """Search the canonical Skillz capability index without executing skills."""
        if limit < 1 or limit > 100:
            raise ValueError("limit must be between 1 and 100")
        mode, matches = query_skill_listing(index, "all" if include_internal and not query.strip() else query)
        if include_internal and query.strip():
            normalized = query.strip().casefold()
            terms = [term for term in normalized.split() if term]
            matches = []
            for skill in index["skills"]:
                meta = invocation(skill)
                skill_category = str(meta.get("category") or "internal")
                haystack = " ".join((skill.get("name", ""), skill.get("description", ""), skill_category)).casefold()
                if all(term in haystack for term in terms):
                    matches.append(skill)
            matches.sort(key=lambda item: (str(invocation(item).get("category") or "internal"), item["name"]))
            mode = "all"
        if category is not None:
            matches = [skill for skill in matches if str(invocation(skill).get("category") or "internal") == category]
        matches = matches[:limit]
        return listing_payload(mode, query, matches)

    @server.tool()
    def get_skill_tool(name: str) -> dict:
        """Return exact indexed metadata for one skill; no fuzzy fallback and no execution."""
        skill = dict(get_skill(index, name))
        skill["resourceUris"] = {
            "metadata": f"skillz://skills/{name}",
            "body": f"skillz://skills/{name}/SKILL.md",
            "references": f"skillz://skills/{name}/references/",
        }
        return skill

    return server
