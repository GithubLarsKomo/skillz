# Obsidian Skill Universe

The repository exposes a deterministic Obsidian projection under `obsidian/` so the skill system can be explored visually without turning Obsidian into a second source of truth.

## Source-of-truth boundary

Canonical data remains in:

- `skills/*/SKILL.md`
- `docs/skill-capability-index.json`
- `docs/skill-dependency-graph.json`
- executable benchmark scenarios under `benchmarks/`

Everything under the generated Obsidian projection is derived from those sources. Do not edit generated skill, category, workflow or canvas files manually.

## Generated structure

```text
obsidian/
  Skill Universe.md
  Skill Universe.canvas
  skills/
    <skill>.md
  categories/
    <category>.md
  workflows/
    <benchmark-scenario>.md
```

Each generated skill note contains:

- capability description
- category and invocation state
- `requires` links
- reverse `required by` links
- declared outputs
- inferred output consumers
- evaluation state
- canonical source path

Category notes are derived from capability metadata. Workflow notes are generated only from benchmark scenarios that expose a valid `sequence` made entirely of known skills. No parallel workflow taxonomy is maintained.

## Obsidian usage

Recommended setup:

1. Open the repository's `obsidian/` directory as an Obsidian Vault.
2. Open `Skill Universe.md` as the entry page.
3. Open `Skill Universe.canvas` for the directed architecture view. Arrow direction means `requires`.
4. Use Graph View for the linked universe across skills, categories and benchmark workflows.
5. Filter with tags such as `#skill`, `#skill-category`, `#skill-workflow` or the generated `#skill-category/<category>` tags.

Local Obsidian settings are intentionally ignored by Git through `obsidian/.obsidian/`.

## Regeneration

The projection is part of normal repository metadata generation:

```bash
python scripts/generate_repository_metadata.py
```

CI verifies staleness with:

```bash
python scripts/generate_repository_metadata.py --check
python -m unittest tests.test_generate_obsidian_skill_universe
```

The dedicated generator can also be invoked directly:

```bash
python scripts/generate_obsidian_skill_universe.py
python scripts/generate_obsidian_skill_universe.py --check
```

## Design constraints

- Obsidian is a projection, never the authoritative skill catalog.
- Skill/category/workflow notes are fully reproducible.
- Stale generated files are detected in `--check` mode and removed during regeneration.
- Canvas edges are created only from canonical `requires` edges and remain directed.
- Workflow views come only from executable benchmark sequences with valid skill references.
- User-local `.obsidian` workspace state is not committed.
