from __future__ import annotations

import json
from collections import deque
from pathlib import Path
from typing import Any

GRAPH_SCHEMA_VERSION = 1
VALID_DIRECTIONS = {"requires", "dependents"}


def load_graph(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read dependency graph: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("dependency graph root must be an object")
    if value.get("schemaVersion") != GRAPH_SCHEMA_VERSION:
        raise ValueError(f"unsupported dependency graph schemaVersion: {value.get('schemaVersion')!r}")
    if not isinstance(value.get("skills"), list):
        raise ValueError("dependency graph skills must be an array")
    return value


def graph_by_name(graph: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for item in graph.get("skills", []):
        if not isinstance(item, dict) or not isinstance(item.get("name"), str):
            raise ValueError("dependency graph skill entries require string names")
        result[item["name"]] = item
    return result


def adjacency(graph: dict[str, Any], direction: str) -> dict[str, list[str]]:
    if direction not in VALID_DIRECTIONS:
        raise ValueError("direction must be requires or dependents")
    skills = graph_by_name(graph)
    direct = {
        name: sorted({str(dep) for dep in item.get("requires", [])})
        for name, item in skills.items()
    }
    if direction == "requires":
        return direct
    reverse = {name: [] for name in skills}
    for source, requirements in direct.items():
        for target in requirements:
            if target in reverse:
                reverse[target].append(source)
    return {name: sorted(set(values)) for name, values in reverse.items()}


def dependency_traversal(
    graph: dict[str, Any],
    name: str,
    *,
    direction: str = "requires",
    transitive: bool = False,
) -> dict[str, Any]:
    edges = adjacency(graph, direction)
    if name not in edges:
        raise LookupError(f"unknown skill: {name}")

    queue: deque[tuple[str, int, str]] = deque(
        (neighbor, 1, name) for neighbor in edges[name]
    )
    seen = {name}
    traversal: list[dict[str, Any]] = []
    while queue:
        current, depth, via = queue.popleft()
        if current in seen:
            continue
        seen.add(current)
        traversal.append({"name": current, "depth": depth, "via": via})
        if transitive:
            for neighbor in edges.get(current, []):
                if neighbor not in seen:
                    queue.append((neighbor, depth + 1, current))

    traversal.sort(key=lambda item: (item["depth"], item["name"], item["via"]))
    return {
        "schemaVersion": 1,
        "name": name,
        "direction": direction,
        "transitive": transitive,
        "count": len(traversal),
        "skills": [item["name"] for item in traversal],
        "traversal": traversal,
    }


def producer_info(index: dict[str, Any], output: str) -> dict[str, Any]:
    producers = sorted(
        {
            str(skill["name"])
            for skill in index.get("skills", [])
            if isinstance(skill, dict) and output in skill.get("outputs", [])
        }
    )
    if not producers:
        raise LookupError(f"unknown output: {output}")

    declared_ambiguous = False
    for skill in index.get("skills", []):
        if not isinstance(skill, dict):
            continue
        for contract in skill.get("outputContracts", []):
            if isinstance(contract, dict) and contract.get("output") == output:
                declared_ambiguous = declared_ambiguous or bool(contract.get("ambiguous"))

    return {
        "schemaVersion": 1,
        "output": output,
        "ambiguous": declared_ambiguous or len(producers) > 1,
        "producerCount": len(producers),
        "producers": producers,
    }


def consumer_info(
    index: dict[str, Any],
    output: str,
    *,
    producer: str | None = None,
) -> dict[str, Any]:
    producer_payload = producer_info(index, output)
    producers = producer_payload["producers"]
    if producer is not None and producer not in producers:
        raise ValueError(f"producer {producer!r} does not produce output {output!r}")

    consumers: set[str] = set()
    contracts_seen = 0
    for skill in index.get("skills", []):
        if not isinstance(skill, dict):
            continue
        for contract in skill.get("outputContracts", []):
            if not isinstance(contract, dict) or contract.get("output") != output:
                continue
            contract_producers = [str(item) for item in contract.get("producers", [])]
            if producer is not None and producer not in contract_producers:
                continue
            contracts_seen += 1
            consumers.update(str(item) for item in contract.get("consumerSkills", []))

    return {
        "schemaVersion": 1,
        "output": output,
        "producer": producer,
        "producerCount": len(producers),
        "producers": producers,
        "contractCount": contracts_seen,
        "consumerCount": len(consumers),
        "consumers": sorted(consumers),
    }
