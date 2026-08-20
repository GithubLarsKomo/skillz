from __future__ import annotations

from pathlib import Path
from typing import Any

from mcp.server import MCPServer

from skillz_core import (
    catalog_identity,
    consumer_info,
    dependency_traversal,
    describe_path,
    get_skill,
    invocation,
    listing_payload,
    load_graph,
    load_index,
    normalize_constraints,
    producer_info,
    query_skill_listing,
    read_utf8_text,
    resolve,
    safe_relative_path,
    validate_catalog as validate_catalog_core,
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
    skills_root = (root / "skills").resolve()
    index = load_index(index_path)
    graph = load_graph(graph_path)
    identity = catalog_identity(
        index,
        graph,
        version_path=version_path,
        runtime_commit=runtime_commit,
        runtime_version=runtime_version,
    )
    resource_meta = {"catalogHash": identity["catalogHash"]}
    server = MCPServer("skillz-mcp")

    def skill_metadata(name: str) -> dict[str, Any]:
        skill = dict(get_skill(index, name))
        skill["resourceUris"] = {
            "metadata": f"skillz://skills/{name}",
            "body": f"skillz://skills/{name}/SKILL.md",
            "references": f"skillz://skills/{name}/references/",
            "assets": f"skillz://skills/{name}/assets",
        }
        return skill

    def skill_root(name: str) -> Path:
        get_skill(index, name)
        return safe_relative_path(skills_root, name)

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
        return skill_metadata(name)

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
        return identity

    @server.tool()
    def validate_catalog() -> dict[str, Any]:
        """Validate in-memory serving invariants without invoking repository scripts or shell commands."""
        return validate_catalog_core(index, graph)

    @server.resource(
        "skillz://index",
        name="skillz_index",
        description="Canonical generated Skillz capability index.",
        mime_type="application/json",
        meta=resource_meta,
    )
    def skillz_index() -> dict[str, Any]:
        return index

    @server.resource(
        "skillz://graph",
        name="skillz_graph",
        description="Canonical generated Skillz dependency graph.",
        mime_type="application/json",
        meta=resource_meta,
    )
    def skillz_graph() -> dict[str, Any]:
        return graph

    @server.resource(
        "skillz://status",
        name="skillz_status",
        description="Identity and fail-closed freshness status for the loaded Skillz catalog.",
        mime_type="application/json",
        meta=resource_meta,
    )
    def skillz_status() -> dict[str, Any]:
        return identity

    @server.resource(
        "skillz://skills/{name}",
        name="skill_metadata",
        description="Compact indexed metadata for one exact Skillz skill.",
        mime_type="application/json",
        meta=resource_meta,
    )
    def skill_metadata_resource(name: str) -> dict[str, Any]:
        return skill_metadata(name)

    @server.resource(
        "skillz://skills/{name}/SKILL.md",
        name="skill_body",
        description="Canonical SKILL.md body for one exact Skillz skill.",
        mime_type="text/markdown; charset=utf-8",
        meta=resource_meta,
    )
    def skill_body_resource(name: str) -> str:
        return read_utf8_text(skill_root(name), "SKILL.md")

    @server.resource(
        "skillz://skills/{name}/references/{+relative_path}",
        name="skill_reference",
        description="Bounded UTF-8 text reference beneath an exact Skillz skill.",
        mime_type="text/plain; charset=utf-8",
        meta=resource_meta,
    )
    def skill_reference_resource(name: str, relative_path: str) -> str:
        references_root = safe_relative_path(skill_root(name), "references")
        return read_utf8_text(references_root, relative_path)

    @server.resource(
        "skillz://skills/{name}/assets",
        name="skill_assets",
        description="Metadata-only listing of the assets directory for one exact Skillz skill.",
        mime_type="application/json",
        meta=resource_meta,
    )
    def skill_assets_resource(name: str) -> dict[str, Any]:
        root_path = skill_root(name)
        assets_root = safe_relative_path(root_path, "assets")
        if not assets_root.exists():
            return {"skill": name, "path": "assets", "type": "directory", "entries": []}
        payload = describe_path(root_path, "assets")
        return {"skill": name, **payload}

    @server.resource(
        "skillz://skills/{name}/assets/{+relative_path}",
        name="skill_asset_metadata",
        description="Metadata for an asset path; binary asset contents are never served.",
        mime_type="application/json",
        meta=resource_meta,
    )
    def skill_asset_metadata_resource(name: str, relative_path: str) -> dict[str, Any]:
        assets_root = safe_relative_path(skill_root(name), "assets")
        payload = describe_path(assets_root, relative_path)
        return {"skill": name, **payload}

    return server
