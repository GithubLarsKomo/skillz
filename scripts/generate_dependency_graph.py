#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import json
import sys
from collections import defaultdict
from pathlib import Path

from generate_repository_metadata import parse_frontmatter

GRAPH_JSON = "docs/skill-dependency-graph.json"
GRAPH_MD = "docs/SKILL-DEPENDENCIES.md"


def as_list(value: object, field: str, path: Path) -> list[str]:
    if value in (None, ""):
        return []
    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
        raise ValueError(f"{path}: {field} must be a string list")
    values = [item.strip() for item in value]
    if len(values) != len(set(values)):
        raise ValueError(f"{path}: duplicate {field} entries")
    return values


def load_skills(root: Path) -> dict[str, dict[str, list[str]]]:
    skills: dict[str, dict[str, list[str]]] = {}
    for path in sorted((root / "skills").glob("*/SKILL.md")):
        slug = path.parent.name
        fm = parse_frontmatter(path)
        requires = as_list(fm.get("requires"), "requires", path)
        consumes = as_list(fm.get("consumes"), "consumes", path)
        outputs = as_list(fm.get("outputs"), "outputs", path)
        if slug in requires:
            raise ValueError(f"{path}: self-dependency '{slug}'")
        skills[slug] = {"requires": requires, "consumes": consumes, "outputs": outputs}
    for slug, meta in skills.items():
        for dep in meta["requires"]:
            if dep not in skills:
                raise ValueError(f"skills/{slug}/SKILL.md: unknown required skill '{dep}'")
    return skills


def find_cycle(skills: dict[str, dict[str, list[str]]]) -> list[str] | None:
    state: dict[str, int] = {slug: 0 for slug in skills}
    stack: list[str] = []

    def visit(slug: str) -> list[str] | None:
        state[slug] = 1
        stack.append(slug)
        for dep in skills[slug]["requires"]:
            if state[dep] == 0:
                cycle = visit(dep)
                if cycle:
                    return cycle
            elif state[dep] == 1:
                idx = stack.index(dep)
                return stack[idx:] + [dep]
        stack.pop()
        state[slug] = 2
        return None

    for slug in sorted(skills):
        if state[slug] == 0:
            cycle = visit(slug)
            if cycle:
                return cycle
    return None


def build_graph(root: Path) -> dict[str, object]:
    skills = load_skills(root)
    cycle = find_cycle(skills)
    if cycle:
        raise ValueError("dependency cycle: " + " -> ".join(cycle))

    producers: dict[str, list[str]] = defaultdict(list)
    dependents: dict[str, list[str]] = defaultdict(list)
    explicit_consumers: dict[str, list[str]] = defaultdict(list)

    for slug, meta in skills.items():
        for output in meta["outputs"]:
            producers[output].append(slug)
        for dependency in meta["requires"]:
            dependents[dependency].append(slug)

    for slug, meta in skills.items():
        for artifact in meta["consumes"]:
            owners = producers.get(artifact, [])
            if not owners:
                raise ValueError(f"skills/{slug}/SKILL.md: unknown consumed artifact '{artifact}'")
            if len(owners) > 1:
                raise ValueError(
                    f"skills/{slug}/SKILL.md: consumed artifact '{artifact}' has ambiguous producers: "
                    + ", ".join(sorted(owners))
                )
            if owners[0] == slug:
                raise ValueError(f"skills/{slug}/SKILL.md: self-consumption of '{artifact}'")
            explicit_consumers[artifact].append(slug)

    output_contracts = []
    unconsumed_outputs: list[str] = []
    for output in sorted(producers):
        owners = sorted(producers[output])
        ambiguous = len(owners) > 1
        if ambiguous:
            consumer_skills: list[str] = []
            consumption_status = "ambiguous"
        else:
            owner = owners[0]
            explicit = set(explicit_consumers.get(output, []))
            inferred = {
                consumer
                for consumer in dependents.get(owner, [])
                if not skills[consumer]["consumes"]
            }
            consumer_skills = sorted(explicit | inferred)
            if explicit and inferred:
                consumption_status = "mixed"
            elif explicit:
                consumption_status = "explicit"
            elif inferred:
                consumption_status = "inferred"
            else:
                consumption_status = "unconsumed"
        output_contracts.append({
            "output": output,
            "producers": owners,
            "consumerSkills": consumer_skills,
            "ambiguous": ambiguous,
            "consumptionStatus": consumption_status,
        })
        if consumption_status == "unconsumed":
            unconsumed_outputs.append(output)

    return {
        "schemaVersion": 1,
        "skills": [
            {
                "name": slug,
                "requires": sorted(meta["requires"]),
                "consumes": sorted(meta["consumes"]),
                "outputs": sorted(meta["outputs"]),
            }
            for slug, meta in sorted(skills.items())
        ],
        "requirementEdges": [
            {"from": slug, "to": dep}
            for slug, meta in sorted(skills.items())
            for dep in sorted(meta["requires"])
        ],
        "consumptionEdges": [
            {"consumer": slug, "artifact": artifact, "producer": producers[artifact][0]}
            for slug, meta in sorted(skills.items())
            for artifact in sorted(meta["consumes"])
        ],
        "outputContracts": output_contracts,
        "unconsumedOutputs": unconsumed_outputs,
        "orphanOutputs": unconsumed_outputs,
    }


def render_json(graph: dict[str, object]) -> str:
    return json.dumps(graph, ensure_ascii=False, indent=2, sort_keys=False) + "\n"


def render_markdown(graph: dict[str, object]) -> str:
    lines = [
        "# Skill Dependency Graph",
        "",
        "Generated from canonical `requires`, `consumes`, and `outputs` frontmatter. Do not edit manually.",
        "",
        "```mermaid",
        "graph TD",
    ]
    edges = graph["requirementEdges"]
    assert isinstance(edges, list)
    if edges:
        for edge in edges:
            assert isinstance(edge, dict)
            lines.append(f"  {edge['from'].replace('-', '_')} --> {edge['to'].replace('-', '_')}")
    else:
        lines.append("  no_dependencies[No hard skill dependencies]")
    lines.extend([
        "```",
        "",
        "## Artifact consumption",
        "",
        "`requires` declares hard skill prerequisites. `consumes` declares concrete artifacts a skill can consume without creating a hard prerequisite edge. For backward compatibility, outputs of a required skill are inferred as consumed only when the consumer declares no explicit `consumes` list. Explicit artifact consumption therefore takes precedence over broad legacy inference.",
        "",
        "| Consumer | Artifact | Producer |",
        "|---|---|---|",
    ])
    consumption_edges = graph["consumptionEdges"]
    assert isinstance(consumption_edges, list)
    if consumption_edges:
        for edge in consumption_edges:
            assert isinstance(edge, dict)
            lines.append(f"| `{edge['consumer']}` | `{edge['artifact']}` | `{edge['producer']}` |")
    else:
        lines.append("| — | — | — |")
    lines.extend([
        "",
        "## Output contracts",
        "",
        "`consumerSkills` prefer explicit `consumes` declarations. Legacy consumer inference from hard `requires` remains only for consumers without an explicit artifact list. Ambiguous producers are never guessed. A missing consumer is reported as `unconsumed`, not as an error: terminal user-facing artifacts are valid outputs.",
        "",
        "| Output | Producers | Consumer skills | Status |",
        "|---|---|---|---|",
    ])
    contracts = graph["outputContracts"]
    assert isinstance(contracts, list)
    for item in contracts:
        assert isinstance(item, dict)
        producers_text = ", ".join(f"`{x}`" for x in item["producers"])
        consumers = ", ".join(f"`{x}`" for x in item["consumerSkills"]) or "—"
        status = str(item["consumptionStatus"])
        lines.append(f"| `{item['output']}` | {producers_text} | {consumers} | {status} |")
    if not contracts:
        lines.append("| — | — | — | no outputs declared |")
    return "\n".join(lines) + "\n"


def apply(path: Path, expected: str, check: bool) -> bool:
    actual = path.read_text(encoding="utf-8") if path.exists() else ""
    if actual == expected:
        return False
    if check:
        print(f"STALE: {path}", file=sys.stderr)
        diff = difflib.unified_diff(
            actual.splitlines(),
            expected.splitlines(),
            fromfile=f"{path} (committed)",
            tofile=f"{path} (generated)",
            lineterm="",
        )
        for line in diff:
            print(line, file=sys.stderr)
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(expected, encoding="utf-8", newline="\n")
    print(f"UPDATED: {path}")
    return True


def run(root: Path, check: bool) -> int:
    try:
        graph = build_graph(root)
        stale = apply(root / GRAPH_JSON, render_json(graph), check)
        stale |= apply(root / GRAPH_MD, render_markdown(graph), check)
        return 1 if check and stale else 0
    except (ValueError, UnicodeDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate deterministic skill dependency graph artifacts.")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help=argparse.SUPPRESS)
    args = parser.parse_args()
    return run(args.root.resolve(), args.check)


if __name__ == "__main__":
    raise SystemExit(main())
