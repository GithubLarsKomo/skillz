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

The index uses `schemaVersion: 1` and contains repository-wide evaluation counts plus one entry per skill. Repository-level evaluation metadata deliberately separates execution success from coverage:

- `evaluationSuiteCount` is the number of discovered suites;
- `evaluatedSkillCount` is the number of indexed skills with a suite;
- `evaluatedEntrypointCount` is the number of user-facing entrypoints with a suite;
- `evaluationCoverageComplete` is true only when every indexed skill has a suite;
- `evaluationPassed` means all executed suites passed and must not be interpreted as proof of complete coverage;
- `evaluationErrorCount` records deterministic evaluation-runner errors.

`discoverabilityCounts` separately reports resolved `public`, `advanced`, `internal`, and `compatibility` capabilities. This is intentionally distinct from lifecycle status and from raw `userFacing` counts.

Each skill entry includes:

- `name` and canonical frontmatter `description`
- invocation metadata (`userFacing`, `category`)
- governance metadata (`status`, resolved `discoverability`, `replacedBy`, `deprecatedSince`)
- hard `requires` dependencies and reverse `dependents`
- declared `outputs`
- `outputContracts` copied from the dependency-graph semantics, including ambiguity and consumer relationships derived from explicit `consumes` metadata or conservative legacy `requires` inference
- portable synchronized files under `references/`, `scripts`, `assets/`, and `agents/`
- evaluation mode: `rubric`, `compatibility`, or `none`
- deterministic case/result counts and committed-baseline pass state

## Discoverability resolution

The index remains backwards compatible with skills that predate explicit discoverability metadata:

1. explicit `discoverability` wins when valid;
2. `status: deprecated` resolves to `compatibility`;
3. `userFacing: true` resolves to `public`;
4. all other skills resolve to `internal`.

`advanced` is therefore always explicit. It is intended for valid user-facing capabilities that should be discoverable for targeted use but not treated as default entrypoints. `compatibility` is reserved for deprecated explicit-use-only surfaces and must not become a second producer of the replacement skill's canonical artifacts.

The generator reuses `generate_dependency_graph.build_graph()` and `evaluate_skills.run()` rather than implementing parallel dependency, artifact-consumption, or scoring rules.

Explicit `consumes` declarations are represented through the dependency graph's output contracts. The capability-index skill object deliberately remains compact and does not duplicate the full consumption-edge list. Ambiguous output producers remain explicitly ambiguous; the index never invents producer/consumer relationships.

## Consumption contract

Consumers may use this file to inspect capabilities, lifecycle, discoverability and composition constraints without reparsing all source files. They must still treat `SKILL.md`, evaluation fixtures, repository generators, and `docs/skill-dependency-graph.json` as the source of truth for detailed artifact-consumption edges.

The file is generated and must not be edited manually. CI verifies it through the existing read-only repository metadata check.
