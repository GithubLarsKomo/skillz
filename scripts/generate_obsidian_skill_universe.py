#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

INDEX_JSON = Path("docs/skill-capability-index.json")
GRAPH_JSON = Path("docs/skill-dependency-graph.json")
OBSIDIAN_ROOT = Path("obsidian")
UNIVERSE_MD = OBSIDIAN_ROOT / "Skill Universe.md"
UNIVERSE_CANVAS = OBSIDIAN_ROOT / "Skill Universe.canvas"
GENERATED_DIRS = ("skills", "categories", "workflows")


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def bool_yaml(value: object) -> str:
    if value is True:
        return "true"
    if value is False:
        return "false"
    return "null"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "unnamed"


def load_json(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected JSON object")
    return data


def load_workflows(root: Path, skill_names: set[str]) -> list[dict[str, object]]:
    workflows: list[dict[str, object]] = []
    seen_ids: set[str] = set()
    benchmark_dir = root / "benchmarks"
    if not benchmark_dir.exists():
        return workflows

    for path in sorted(benchmark_dir.glob("*.json")):
        try:
            data = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError, ValueError):
            continue
        scenarios = data.get("scenarios")
        if not isinstance(scenarios, list):
            continue
        for scenario in scenarios:
            if not isinstance(scenario, dict):
                continue
            scenario_id = scenario.get("id")
            sequence = scenario.get("sequence")
            if not isinstance(scenario_id, str) or not scenario_id.strip():
                continue
            if not isinstance(sequence, list) or not sequence:
                continue
            if not all(isinstance(item, str) and item in skill_names for item in sequence):
                continue
            base_id = slugify(scenario_id)
            workflow_id = base_id
            if workflow_id in seen_ids:
                workflow_id = f"{slugify(path.stem)}--{base_id}"
                suffix = 2
                while workflow_id in seen_ids:
                    workflow_id = f"{slugify(path.stem)}--{base_id}-{suffix}"
                    suffix += 1
            seen_ids.add(workflow_id)
            workflows.append({
                "id": workflow_id,
                "scenarioId": scenario_id,
                "source": path.relative_to(root).as_posix(),
                "sequence": list(sequence),
                "mustPreserve": scenario.get("mustPreserve") if isinstance(scenario.get("mustPreserve"), list) else [],
            })
    return sorted(workflows, key=lambda item: str(item["id"]))


def skill_note(skill: dict[str, object]) -> str:
    name = str(skill["name"])
    invocation = skill.get("invocation") if isinstance(skill.get("invocation"), dict) else {}
    category = str(invocation.get("category") or "internal")
    evaluation = skill.get("evaluation") if isinstance(skill.get("evaluation"), dict) else {}
    requires = [str(x) for x in skill.get("requires", [])]
    dependents = [str(x) for x in skill.get("dependents", [])]
    outputs = [str(x) for x in skill.get("outputs", [])]
    output_contracts = skill.get("outputContracts") if isinstance(skill.get("outputContracts"), list) else []

    lines = [
        "---",
        "type: skill",
        "generated: true",
        f"name: {yaml_string(name)}",
        f"category: {yaml_string(category)}",
        f"userFacing: {bool_yaml(invocation.get('userFacing'))}",
        f"evaluationPassed: {bool_yaml(evaluation.get('passed'))}",
        f"evaluationMode: {yaml_string(str(evaluation.get('mode', 'none')))}",
        f"caseCount: {int(evaluation.get('caseCount', 0) or 0)}",
        f"recordedResultCount: {int(evaluation.get('recordedResultCount', 0) or 0)}",
        f"sourcePath: {yaml_string(f'skills/{name}/SKILL.md')}",
        "tags:",
        "  - skill",
        f"  - skill-category/{category}",
        "---",
        "",
        f"# {name}",
        "",
        str(skill.get("description", "")),
        "",
        "> Generated from canonical repository metadata. Do not edit this note manually.",
        "",
        "## Category",
        "",
        f"[[categories/{category}|{category}]]",
        "",
        "## Requires",
        "",
    ]
    lines.extend([f"- [[skills/{dep}|{dep}]]" for dep in requires] or ["- —"])
    lines.extend(["", "## Required by", ""])
    lines.extend([f"- [[skills/{dep}|{dep}]]" for dep in dependents] or ["- —"])
    lines.extend(["", "## Outputs", ""])
    lines.extend([f"- `{output}`" for output in outputs] or ["- —"])
    lines.extend(["", "## Output consumers", ""])
    if output_contracts:
        for contract in output_contracts:
            if not isinstance(contract, dict):
                continue
            output = str(contract.get("output", ""))
            consumers = [str(x) for x in contract.get("consumerSkills", [])] if isinstance(contract.get("consumerSkills"), list) else []
            ambiguous = bool(contract.get("ambiguous", False))
            lines.append(f"### `{output}`")
            lines.append("")
            if ambiguous:
                lines.append("- Ambiguous producer contract; no inferred consumer edge.")
            elif consumers:
                lines.extend(f"- [[skills/{consumer}|{consumer}]]" for consumer in consumers)
            else:
                lines.append("- Terminal or currently unconsumed output.")
            lines.append("")
    else:
        lines.append("- —")
        lines.append("")
    lines.extend([
        "## Evaluation",
        "",
        f"- Mode: `{evaluation.get('mode', 'none')}`",
        f"- Passed: `{evaluation.get('passed')}`",
        f"- Cases: `{evaluation.get('caseCount', 0)}`",
        f"- Recorded results: `{evaluation.get('recordedResultCount', 0)}`",
        "",
        "## Canonical source",
        "",
        f"`skills/{name}/SKILL.md`",
        "",
    ])
    return "\n".join(lines)


def category_note(category: str, skills: list[str]) -> str:
    lines = [
        "---",
        "type: skill-category",
        "generated: true",
        f"category: {yaml_string(category)}",
        "tags:",
        "  - skill-category",
        "---",
        "",
        f"# {category}",
        "",
        "> Generated from skill capability metadata. Do not edit manually.",
        "",
        f"Skills: **{len(skills)}**",
        "",
    ]
    lines.extend(f"- [[skills/{name}|{name}]]" for name in skills)
    lines.append("")
    return "\n".join(lines)


def workflow_note(workflow: dict[str, object]) -> str:
    workflow_id = str(workflow["id"])
    sequence = [str(x) for x in workflow["sequence"]]
    must_preserve = [str(x) for x in workflow.get("mustPreserve", [])]
    lines = [
        "---",
        "type: skill-workflow",
        "generated: true",
        f"workflowId: {yaml_string(workflow_id)}",
        f"scenarioId: {yaml_string(str(workflow['scenarioId']))}",
        f"sourceBenchmark: {yaml_string(str(workflow['source']))}",
        "tags:",
        "  - skill-workflow",
        "---",
        "",
        f"# {workflow['scenarioId']}",
        "",
        "> Generated from an executable repository benchmark. Do not edit manually.",
        "",
        "## Sequence",
        "",
    ]
    for index, skill in enumerate(sequence, start=1):
        lines.append(f"{index}. [[skills/{skill}|{skill}]]")
    lines.extend(["", "## Must preserve", ""])
    lines.extend([f"- {item}" for item in must_preserve] or ["- —"])
    lines.extend(["", "## Source", "", f"`{workflow['source']}`", ""])
    return "\n".join(lines)


def build_canvas(index: dict[str, object], graph: dict[str, object]) -> str:
    skills = index.get("skills")
    if not isinstance(skills, list):
        raise ValueError("capability index: skills must be a list")
    by_category: dict[str, list[dict[str, object]]] = defaultdict(list)
    for skill in skills:
        if not isinstance(skill, dict):
            continue
        invocation = skill.get("invocation") if isinstance(skill.get("invocation"), dict) else {}
        category = str(invocation.get("category") or "internal")
        by_category[category].append(skill)

    nodes: list[dict[str, object]] = [{
        "id": "universe-title",
        "type": "text",
        "text": f"# Skill Universe\n{len(skills)} generated skill nodes\nDirected arrows mean **requires**.",
        "x": 0,
        "y": -240,
        "width": 620,
        "height": 160,
    }]
    skill_positions: dict[str, tuple[int, int]] = {}
    group_width = 1120
    group_gap = 100
    margin_x = 40
    margin_y = 70
    node_width = 300
    node_height = 110
    col_gap = 30
    row_gap = 30
    columns = 3

    for category_index, category in enumerate(sorted(by_category)):
        category_skills = sorted(by_category[category], key=lambda item: str(item["name"]))
        rows = max(1, (len(category_skills) + columns - 1) // columns)
        group_height = margin_y + rows * (node_height + row_gap) + 30
        group_x = category_index * (group_width + group_gap)
        group_y = 0
        nodes.append({
            "id": f"category-{category}",
            "type": "group",
            "label": category,
            "x": group_x,
            "y": group_y,
            "width": group_width,
            "height": group_height,
            "color": str((category_index % 6) + 1),
        })
        for index_in_category, skill in enumerate(category_skills):
            name = str(skill["name"])
            col = index_in_category % columns
            row = index_in_category // columns
            x = group_x + margin_x + col * (node_width + col_gap)
            y = group_y + margin_y + row * (node_height + row_gap)
            skill_positions[name] = (x, y)
            nodes.append({
                "id": f"skill-{name}",
                "type": "file",
                "file": f"obsidian/skills/{name}.md",
                "x": x,
                "y": y,
                "width": node_width,
                "height": node_height,
            })

    edges: list[dict[str, object]] = []
    requirement_edges = graph.get("requirementEdges")
    if not isinstance(requirement_edges, list):
        raise ValueError("dependency graph: requirementEdges must be a list")
    for edge in requirement_edges:
        if not isinstance(edge, dict):
            continue
        source = str(edge.get("from", ""))
        target = str(edge.get("to", ""))
        if source not in skill_positions or target not in skill_positions:
            raise ValueError(f"dependency edge references unknown skill: {source} -> {target}")
        digest = hashlib.sha1(f"{source}->{target}".encode("utf-8")).hexdigest()[:12]
        source_x, _ = skill_positions[source]
        target_x, _ = skill_positions[target]
        from_side = "right" if source_x <= target_x else "left"
        to_side = "left" if source_x <= target_x else "right"
        edges.append({
            "id": f"requires-{digest}",
            "fromNode": f"skill-{source}",
            "fromSide": from_side,
            "toNode": f"skill-{target}",
            "toSide": to_side,
            "toEnd": "arrow",
            "label": "requires",
        })

    canvas = {"nodes": nodes, "edges": edges}
    return json.dumps(canvas, ensure_ascii=False, indent=2, sort_keys=False) + "\n"


def universe_note(index: dict[str, object], categories: dict[str, list[str]], workflows: list[dict[str, object]]) -> str:
    skill_count = int(index.get("skillCount", 0) or 0)
    evaluation_passed = index.get("evaluationPassed")
    lines = [
        "---",
        "type: skill-universe",
        "generated: true",
        "tags:",
        "  - skill-universe",
        "---",
        "",
        "# Skill Universe",
        "",
        "> Generated from `docs/skill-capability-index.json`, `docs/skill-dependency-graph.json` and executable E2E benchmark sequences. Do not edit generated files manually.",
        "",
        f"- Skills: **{skill_count}**",
        f"- Categories: **{len(categories)}**",
        f"- Workflow views: **{len(workflows)}**",
        f"- Repository evaluation passed: **{evaluation_passed}**",
        "",
        "## Views",
        "",
        "- Open `Skill Universe.canvas` for the directed architecture view. Arrows mean `requires`.",
        "- Use Obsidian Graph View for the native linked universe across skills, categories and workflows.",
        "- Filter by `tag:#skill`, `tag:#skill-category` or `tag:#skill-workflow` as needed.",
        "",
        "## Categories",
        "",
    ]
    for category in sorted(categories):
        lines.append(f"- [[categories/{category}|{category}]] ({len(categories[category])})")
    lines.extend(["", "## Workflows", ""])
    if workflows:
        for workflow in workflows:
            lines.append(f"- [[workflows/{workflow['id']}|{workflow['scenarioId']}]]")
    else:
        lines.append("- —")
    lines.extend([
        "",
        "## Source-of-truth rule",
        "",
        "`obsidian/` is a generated projection only. Change skills, dependencies or executable benchmark sequences at their canonical repository source and regenerate metadata; never maintain a parallel Obsidian taxonomy by hand.",
        "",
    ])
    return "\n".join(lines)


def build_outputs(root: Path) -> dict[Path, str]:
    index = load_json(root / INDEX_JSON)
    graph = load_json(root / GRAPH_JSON)
    skills = index.get("skills")
    if not isinstance(skills, list):
        raise ValueError("capability index: skills must be a list")
    skill_names = {str(skill["name"]) for skill in skills if isinstance(skill, dict) and "name" in skill}
    if len(skill_names) != len(skills):
        raise ValueError("capability index: duplicate or invalid skill names")

    categories: dict[str, list[str]] = defaultdict(list)
    outputs: dict[Path, str] = {}
    for skill in skills:
        assert isinstance(skill, dict)
        name = str(skill["name"])
        invocation = skill.get("invocation") if isinstance(skill.get("invocation"), dict) else {}
        category = str(invocation.get("category") or "internal")
        categories[category].append(name)
        outputs[OBSIDIAN_ROOT / "skills" / f"{name}.md"] = skill_note(skill)

    normalized_categories = {category: sorted(names) for category, names in categories.items()}
    for category, names in sorted(normalized_categories.items()):
        outputs[OBSIDIAN_ROOT / "categories" / f"{category}.md"] = category_note(category, names)

    workflows = load_workflows(root, skill_names)
    for workflow in workflows:
        outputs[OBSIDIAN_ROOT / "workflows" / f"{workflow['id']}.md"] = workflow_note(workflow)

    outputs[UNIVERSE_MD] = universe_note(index, normalized_categories, workflows)
    outputs[UNIVERSE_CANVAS] = build_canvas(index, graph)
    return outputs


def managed_existing_files(root: Path) -> set[Path]:
    paths: set[Path] = set()
    for dirname in GENERATED_DIRS:
        base = root / OBSIDIAN_ROOT / dirname
        if base.exists():
            paths.update(path.relative_to(root) for path in base.glob("*.md") if path.is_file())
    for path in (UNIVERSE_MD, UNIVERSE_CANVAS):
        if (root / path).exists():
            paths.add(path)
    return paths


def run(root: Path, check: bool) -> int:
    try:
        expected = build_outputs(root)
        expected_paths = set(expected)
        existing_paths = managed_existing_files(root)
        stale = False

        for relative, content in sorted(expected.items(), key=lambda item: item[0].as_posix()):
            path = root / relative
            actual = path.read_text(encoding="utf-8") if path.exists() else None
            if actual == content:
                continue
            stale = True
            if check:
                print(f"STALE: {relative}", file=sys.stderr)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8", newline="\n")
                print(f"UPDATED: {relative}")

        extras = sorted(existing_paths - expected_paths, key=lambda path: path.as_posix())
        for relative in extras:
            stale = True
            if check:
                print(f"STALE EXTRA: {relative}", file=sys.stderr)
            else:
                (root / relative).unlink()
                print(f"REMOVED: {relative}")

        return 1 if check and stale else 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate deterministic Obsidian skill universe artifacts.")
    parser.add_argument("--check", action="store_true", help="Fail without writing when generated Obsidian artifacts are stale.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help=argparse.SUPPRESS)
    args = parser.parse_args()
    return run(args.root.resolve(), args.check)


if __name__ == "__main__":
    raise SystemExit(main())
