from __future__ import annotations

from pathlib import Path
from typing import Any

from mcp.server import MCPServer

from skillz_core import (
    catalog_identity,
    consumer_info,
    dependency_traversal,
    get_skill,
    invocation,
    listing_payload,
    load_graph,
    load_index,
    normalize_constraints,
    producer_info,
    query_skill_listing,
    resolve,
)

DEFAULT_ROOT = Path(__file__).resolve().parents[2]


def create_server(
    repository_root: Path | None = None,
    *,
    runtime_commit: str | None = None,
    runtime_version: str | None = None,
) -> MCPServer:
    root = (repository_root or DEFAULT_ROOT).resolve()
    index_path = root / "docs" / "skill-capability-index.json"
    graph_path = root / "docs" / "skill-dependency-graph.json"
    version_path = root / "VERSION"
    index = load_index(index_path)
    graph = load_graph(graph_path)
    server = MCPServer("skillz-mcp")

    @server.tool()
    def search_skills(
        query: str = "",
        category: str | None = None,
        include_internal: bool = False,
        limit: int = 25,
    ) -> dict[str, Any]:
        """Search the canonical Skillz capability index without executing skills."""
        if limit < 1 or limit > 100:
            raise ValueError("limit must be between 1 and 100")
        mode, matches = query_skill_listing(index, "all" if include_internal and not query.strip() else query)
        if include_internal and query.strip():
            terms = [term for term in query.strip().casefold().split() if term]
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

    @server.tool(name="get_skill")
    def get_skill_metadata(name: str) -> dict[str, Any]:
        """Return exact indexed metadata for one skill; no fuzzy fallback and no execution."""
        skill = dict(get_skill(index, name))
        skill["resourceUris"] = {
            "metadata": f"skillz://skills/{name}",
            "body": f"skillz://skills/{name}/SKILL.md",
            "references": f"skillz://skills/{name}/references/",
        }
        return skill

    @server.tool()
    def resolve_capabilities(
        outputs: list[str] | None = None,
        dependencies: list[str] | None = None,
        evaluation_modes: list[str] | None = None,
        portable_files: str = "irrelevant",
    ) -> dict[str, Any]:
        """Resolve exact declared capability constraints by deterministic intersection."""
        constraints = normalize_constraints(
            outputs or [],
            dependencies or [],
            evaluation_modes or [],
            portable_files,
        )
        return resolve(index, constraints)

    @server.tool()
    def get_dependencies(
        name: str,
        direction: str = "requires",
        transitive: bool = False,
    ) -> dict[str, Any]:
        """Traverse declared skill dependencies deterministically without inference."""
        return dependency_traversal(graph, name, direction=direction, transitive=transitive)

    @server.tool()
    def find_producers(output: str) -> dict[str, Any]:
        """Return every exact declared producer for an output, preserving ambiguity."""
        return producer_info(index, output)

    @server.tool()
    def find_consumers(output: str, producer: str | None = None) -> dict[str, Any]:
        """Return consumers declared in outputContracts only."""
        return consumer_info(index, output, producer=producer)

    @server.tool()
    def catalog_status() -> dict[str, Any]:
        """Return deterministic identity and fail-closed freshness for the loaded catalog."""
        return catalog_identity(
            index,
            graph,
            version_path=version_path,
            runtime_commit=runtime_commit,
            runtime_version=runtime_version,
        )

    return server
