from __future__ import annotations

from typing import Any

from .graph import graph_by_name


def validate_catalog(index: dict[str, Any], graph: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    index_skills = index.get("skills", [])
    names = [item.get("name") for item in index_skills if isinstance(item, dict)]
    string_names = [name for name in names if isinstance(name, str)]
    if len(string_names) != len(index_skills):
        errors.append("capability index contains skill entries without string names")
    duplicates = sorted({name for name in string_names if string_names.count(name) > 1})
    for name in duplicates:
        errors.append(f"duplicate skill name: {name}")
    known = set(string_names)

    try:
        graph_skills = graph_by_name(graph)
    except ValueError as exc:
        errors.append(str(exc))
        graph_skills = {}

    missing_graph = sorted(known - set(graph_skills))
    extra_graph = sorted(set(graph_skills) - known)
    for name in missing_graph:
        errors.append(f"skill missing from dependency graph: {name}")
    for name in extra_graph:
        errors.append(f"dependency graph contains unknown skill: {name}")

    index_requires: dict[str, list[str]] = {}
    for skill in index_skills:
        if not isinstance(skill, dict) or not isinstance(skill.get("name"), str):
            continue
        name = skill["name"]
        requires = sorted(str(item) for item in skill.get("requires", []))
        index_requires[name] = requires
        for dependency in requires:
            if dependency not in known:
                errors.append(f"skill {name} requires unknown skill: {dependency}")

        for contract in skill.get("outputContracts", []):
            if not isinstance(contract, dict):
                errors.append(f"skill {name} contains a non-object outputContract")
                continue
            output = contract.get("output")
            if not isinstance(output, str) or not output:
                errors.append(f"skill {name} contains outputContract without output")
                continue
            if output not in skill.get("outputs", []):
                warnings.append(f"skill {name} has outputContract for undeclared local output: {output}")
            if not isinstance(contract.get("ambiguous"), bool):
                errors.append(f"skill {name} outputContract {output} requires boolean ambiguous")
            producers = contract.get("producers")
            consumers = contract.get("consumerSkills")
            if not isinstance(producers, list) or not all(isinstance(item, str) for item in producers):
                errors.append(f"skill {name} outputContract {output} requires string producers array")
                producers = []
            if not isinstance(consumers, list) or not all(isinstance(item, str) for item in consumers):
                errors.append(f"skill {name} outputContract {output} requires string consumerSkills array")
                consumers = []
            for producer in producers:
                if producer not in known:
                    errors.append(f"outputContract {output} references unknown producer: {producer}")
            for consumer in consumers:
                if consumer not in known:
                    errors.append(f"outputContract {output} references unknown consumer: {consumer}")

    for name, item in graph_skills.items():
        graph_requires = sorted(str(dep) for dep in item.get("requires", []))
        for dependency in graph_requires:
            if dependency not in graph_skills:
                errors.append(f"dependency graph skill {name} requires unknown skill: {dependency}")
        if name in index_requires and graph_requires != index_requires[name]:
            errors.append(f"dependency graph drift for skill: {name}")

    state: dict[str, int] = {name: 0 for name in graph_skills}

    def visit(name: str, stack: list[str]) -> None:
        if state[name] == 2:
            return
        if state[name] == 1:
            try:
                start = stack.index(name)
                cycle = stack[start:] + [name]
            except ValueError:
                cycle = stack + [name]
            errors.append("dependency cycle: " + " -> ".join(cycle))
            return
        state[name] = 1
        for dependency in sorted(str(dep) for dep in graph_skills[name].get("requires", [])):
            if dependency in graph_skills:
                visit(dependency, stack + [name])
        state[name] = 2

    for name in sorted(graph_skills):
        if state[name] == 0:
            visit(name, [])

    errors = sorted(set(errors))
    warnings = sorted(set(warnings))
    return {
        "schemaVersion": 1,
        "valid": not errors,
        "errorCount": len(errors),
        "warningCount": len(warnings),
        "errors": errors,
        "warnings": warnings,
        "recommendedFullValidationCommands": [
            "python scripts/validate_skills.py",
            "python scripts/validate_metadata_schemas.py",
            "python scripts/evaluate_skills.py",
        ],
    }
