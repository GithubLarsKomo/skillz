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

## Provenance and `/skills status`

A committed file cannot truthfully contain the SHA of the commit that contains that same SHA field: changing the field changes the commit. Therefore the canonical committed capability index stays deterministic and provenance is stamped into a **runtime copy** after the source commit is known.

Create an exact runtime index with repository, ref, version, and full source commit SHA:

```bash
python scripts/stamp_capability_index.py \
  --commit "$GIT_COMMIT" \
  --output build/skill-capability-index.json
```

The stamped copy contains:

```json
"provenance": {
  "repository": "GithubLarsKomo/skillz",
  "ref": "main",
  "version": "0.1.0-beta.1",
  "commitSha": "<full-40-character-sha>"
}
```

OpenAI/Codex plugin builds can carry the same exact source identity in `skillz-distribution-manifest.json`:

```bash
python scripts/build_openai_plugin.py \
  --output build/skillz \
  --source-commit "$GIT_COMMIT"
```

`/skills status` compares the live repository HEAD with the installed/runtime source identity. The deterministic CLI equivalent is:

```bash
python scripts/query_capabilities.py \
  --skills status \
  --repository-head "$LIVE_GITHUB_HEAD" \
  --installed-manifest /path/to/skillz-distribution-manifest.json
```

Status semantics are deliberately fail-closed:

- `current`: installed source commit exactly equals live repository HEAD.
- `stale`: installed source commit differs from live HEAD, or (when no exact commit is available) the installed version differs from the repository version.
- `unknown`: exact freshness cannot be proven, for example an older install reports the same version but no source commit.

A matching version alone must never be reported as `current`. Exact currentness requires the source commit SHA.

## Discovery, exact resolution, and natural-language interpretation

Keep the repository's existing boundaries intact instead of adding a second hand-written router:

- **Discovery** answers “what user-facing entrypoints exist?” Use `/skills` or `scripts/query_capabilities.py`.
- **Exact capability resolution** answers “which skills satisfy these explicit declared constraints?” Use `scripts/resolve_capabilities.py`. It performs deterministic intersection and deliberately does not interpret prose.
- **Natural-language interpretation** converts an unstructured goal into an admitted capability intent before deterministic resolution. Use the existing model-capability pipeline (`scripts/run_model_capability_pipeline.py`) with its provider qualification, review/admission, and resolver stages when machine routing is required.
- **Conversational orientation** may recommend one or a few current entrypoints after reading the capability index, but the recommendation is advisory until the user asks to execute a skill. It must not invent a skill or maintain a separate catalog.

This preserves one capability source of truth while keeping probabilistic interpretation outside deterministic query/resolver primitives.

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

`/skills status` resolves the live GitHub HEAD for GithubLarsKomo/skillz and
compares it with exact installed/runtime provenance when available. Report
current only for an exact source-commit match, stale for a mismatch, and
unknown when the installed source commit cannot be established. A matching
version without a source commit is not proof of currentness.

`/skill <name>` shows that indexed skill's purpose, category, dependencies,
outputs, and likely downstream skills. Listing a skill does not execute it.
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

- [`CAPABILITY-QUERY.md`](CAPABILITY-QUERY.md) defines the deterministic query boundary.
- [`capability-resolver.md`](capability-resolver.md) defines exact deterministic resolution.
- [`OPENAI-PLUGIN-DISTRIBUTION.md`](OPENAI-PLUGIN-DISTRIBUTION.md) explains harness-specific invocation metadata without changing canonical skill content.
- [`AIHERO-V1.2.2-COMPLEMENTARY-PATTERNS.md`](AIHERO-V1.2.2-COMPLEMENTARY-PATTERNS.md) records the complementary patterns adopted from the v1.2.2 comparison and the patterns intentionally not duplicated as new skills.
