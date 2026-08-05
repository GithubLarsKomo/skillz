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
- `userFacing` controls discovery only. It does not by itself decide whether an agent harness may invoke a skill implicitly; harness policy is a separate concern.

The capability-index generator materializes this as:

```json
"invocation": {
  "userFacing": true,
  "category": "engineering"
}
```

The index also records `entrypointCount` and `entrypointCategories`.

## Deterministic CLI

The capability query CLI mirrors the intended slash-command semantics and also exposes deterministic routing:

```bash
python scripts/query_capabilities.py --skills
python scripts/query_capabilities.py --skills all
python scripts/query_capabilities.py --skills medical
python scripts/query_capabilities.py --skill large-work-wayfinder
python scripts/query_capabilities.py --route "plan a large regulatory software change"
```

- `--skills` lists only deliberate user-facing entrypoints, grouped by category.
- `--skills all` lists every skill and marks non-entrypoints as internal.
- `--skills <query>` deterministically filters user-facing entrypoints by tokens appearing in skill name, description, or category.
- `--skill <name>` shows description, invocation metadata, dependencies, dependents, outputs, and evaluation mode.
- `--route <goal>` ranks user-facing entrypoints for a natural-language goal and returns their declared prerequisites, likely downstream skills, and outputs. Routing is advisory only: it never executes a skill or treats a dependency edge as an instruction to run every dependency first.

Use `--json` for stable machine-readable output.

### Inventory versus routing

Keep these two operations separate:

- **Inventory** answers “what skills exist?” and is served by `/skills` / `--skills`.
- **Routing** answers “which current entrypoint best fits this goal?” and is served by `/skill-route <goal>` / `--route <goal>`.

The distinction prevents a stale hand-written router from becoming a second source of truth. Routing derives from the same committed capability metadata used by discovery, and the user or calling agent remains responsible for choosing whether to execute the recommendation.

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

`/skill-route <goal>` ranks the current user-facing entrypoints for the goal
using the capability index. Show the best match first, explain the matching
terms and declared dependency/downstream context, and keep the result
advisory until the user asks to execute a skill.
```

This is a prompt-level command convention. A client may additionally expose the same commands as native UI/autocomplete actions, but the repository contract does not depend on a particular client.

## Phase-boundary rule

Do not use a handoff merely because a phase ended. Choose the cheapest context transition that preserves the primary source:

1. **Continue** when the current session still has the relevant primary context and the next phase is directly related.
2. **Subagent/delegation** when a tightly scoped side task can be completed independently and returned as evidence.
3. **Compact/summarize in place** when the same harness and workspace continue but context pressure is material.
4. **Handoff** when state must actually travel to another session, harness, workspace, repository context, person, or independently resumed branch of work.

A handoff earns its extra structure by portability. If nothing needs to travel, prefer a cheaper boundary.

## Categories

Categories describe discovery surfaces, not dependency ownership. A specialist may depend on many foundations and still be a valid user-facing entrypoint. The initial curated categories are:

- `engineering`
- `regulated-engineering`
- `productivity`
- `research-knowledge`
- `communication-memory`
- `skill-system`

Adding a new category requires at least one explicit `userFacing: true` skill and must remain stable enough to be useful in discovery UI.

## Related guidance

- [`OPENAI-PLUGIN-DISTRIBUTION.md`](OPENAI-PLUGIN-DISTRIBUTION.md) explains harness-specific invocation metadata without changing canonical skill content.
- [`AIHERO-V1.2.2-COMPLEMENTARY-PATTERNS.md`](AIHERO-V1.2.2-COMPLEMENTARY-PATTERNS.md) records the complementary patterns adopted from the v1.2.2 comparison and the patterns intentionally not duplicated as new skills.
