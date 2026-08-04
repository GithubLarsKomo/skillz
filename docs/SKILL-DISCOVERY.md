# Skill discovery and `/skills` convention

`docs/skill-capability-index.json` is the canonical discovery surface for user-facing skill entrypoints. Do not maintain a separate memorized skill list.

## Skill frontmatter

A skill is internal by default. Mark a deliberate user-facing entrypoint with two flat frontmatter fields:

```yaml
userFacing: true
category: engineering
```

Rules:

- `userFacing` is optional and defaults to `false`.
- `category` is required when `userFacing: true`.
- `category` is a lowercase kebab-case slug.
- `category` without `userFacing: true` is invalid.
- Internal foundations/helpers stay unannotated.

The capability-index generator materializes this as:

```json
"invocation": {
  "userFacing": true,
  "category": "engineering"
}
```

The index also records `entrypointCount` and `entrypointCategories`.

## Deterministic CLI

The existing capability query CLI mirrors the intended slash-command semantics:

```bash
python scripts/query_capabilities.py --skills
python scripts/query_capabilities.py --skills all
python scripts/query_capabilities.py --skills medical
python scripts/query_capabilities.py --skill large-work-wayfinder
```

- `--skills` lists only deliberate user-facing entrypoints, grouped by category.
- `--skills all` lists every skill and marks non-entrypoints as internal.
- `--skills <query>` deterministically filters user-facing entrypoints by tokens appearing in skill name, description, or category.
- `--skill <name>` shows description, invocation metadata, dependencies, dependents, outputs, and evaluation mode.

Use `--json` for stable machine-readable output.

## System-prompt convention

A client or system prompt may define the following textual commands:

```text
When the user sends `/skills`, read the current GitHub-backed
`GithubLarsKomo/skillz/docs/skill-capability-index.json` and show only
skills whose `invocation.userFacing` is true, grouped by
`invocation.category`. Do not use a memorized list.

`/skills all` shows all indexed skills and clearly distinguishes internal
helpers from user-facing entrypoints.

`/skills <query>` filters the user-facing entrypoints using current index
metadata. The assistant may explain relevance, but must not invent a skill
that is absent from the index.

`/skill <name>` shows that indexed skill's purpose, category, dependencies,
outputs, and likely downstream skills. Listing a skill does not execute it.
```

This is a prompt-level command convention. A client may additionally expose the same commands as native UI/autocomplete actions, but the repository contract does not depend on a particular client.

## Categories

Categories describe discovery surfaces, not dependency ownership. A specialist may depend on many foundations and still be a valid user-facing entrypoint. The initial curated categories are:

- `engineering`
- `regulated-engineering`
- `productivity`
- `research-knowledge`
- `communication-memory`
- `skill-system`

Adding a new category requires at least one explicit `userFacing: true` skill and must remain stable enough to be useful in discovery UI.