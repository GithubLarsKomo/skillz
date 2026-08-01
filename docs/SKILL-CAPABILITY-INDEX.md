# Skill Capability Index

`docs/skill-capability-index.json` is a deterministic, generated view of the repository for agents and orchestrators. It is descriptive only: it does not execute, route, rank, or select skills.

Generate all repository metadata with:

```bash
python scripts/generate_repository_metadata.py
```

Validate without writing with:

```bash
python scripts/generate_repository_metadata.py --check
```

## Schema

The index uses `schemaVersion: 1` and contains repository-wide evaluation counts plus one entry per skill. Each skill entry includes:

- `name` and canonical frontmatter `description`
- hard `requires` dependencies and reverse `dependents`
- declared `outputs`
- `outputContracts` copied from the dependency-graph semantics, including ambiguity and conservative consumer inference
- portable synchronized files under `references/`, `scripts/`, and `assets/`
- evaluation mode: `rubric`, `compatibility`, or `none`
- deterministic case/result counts and committed-baseline pass state

The generator reuses `generate_dependency_graph.build_graph()` and `evaluate_skills.run()` rather than implementing parallel dependency or scoring rules.

Ambiguous output producers remain explicitly ambiguous. The index never invents producer/consumer relationships.

## Consumption contract

Consumers may use this file to inspect capabilities and composition constraints without reparsing all source files. They must still treat `SKILL.md`, evaluation fixtures, and repository generators as the source of truth.

The file is generated and must not be edited manually. CI verifies it through the existing read-only repository metadata check.
