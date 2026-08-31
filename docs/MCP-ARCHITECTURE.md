# Skillz MCP Server Architecture

## Status

Proposed architecture for `feat/mcp-server`.

The MCP server is a stable, read-only access layer over the existing `skillz` capability model. It does **not** replace the repository, duplicate its metadata, execute skills, or become a second agent runtime.

## 1. Architectural goal

`skillz` has grown from a collection of Markdown instructions into a machine-readable capability system with:

- `docs/skill-capability-index.json` as the canonical discovery surface,
- `requires`, `dependents`, `outputs`, and `outputContracts`,
- deterministic query and exact-resolution primitives,
- a generated dependency graph,
- version/provenance support,
- schema-backed capability-intent and model-interpretation pipelines,
- evaluation evidence and repository validation,
- provider, plugin, and distribution boundaries.

The MCP server exposes these capabilities to MCP clients through a small, versioned meta-API. The number of MCP tools must remain approximately constant as the number of skills grows.

## 2. Core decisions

### AD-1 — The capability index remains the source of truth

`docs/skill-capability-index.json` is the canonical MCP catalog input. The MCP server must not maintain a second hand-authored registry or database of skills.

Generated or runtime-stamped derivatives may be cached, but they must be reproducibly derived from the committed repository state.

### AD-2 — MCP is an adapter, not an agent runtime

The initial MCP server is read-only. It may:

- discover skills,
- read skill content and related repository resources,
- resolve exact declared capability constraints,
- traverse dependency and output-contract relationships,
- report catalog identity and validation state.

It must not initially:

- execute a skill,
- execute arbitrary files from `scripts/`,
- invoke GitHub writes,
- modify the repository,
- invoke external tools on behalf of a skill,
- silently invoke an LLM,
- turn every skill into its own MCP tool.

Execution is a later gateway concern and must remain separate from discovery and routing.

### AD-3 — Reuse deterministic Python capability logic

The repository already implements the important deterministic boundaries in Python:

- `scripts/query_capabilities.py`,
- `scripts/resolve_capabilities.py`,
- `scripts/generate_dependency_graph.py`,
- `scripts/stamp_capability_index.py`,
- the capability-intent/model-admission pipeline.

The MCP implementation should therefore use the official Python MCP SDK v2 and extract reusable logic from CLI scripts into importable modules rather than reimplementing the same semantics in another language.

CLI behavior must remain backward compatible and should become a thin wrapper over the same library used by MCP.

### AD-4 — Deterministic and probabilistic routing stay separate

The existing repository explicitly separates:

1. discovery,
2. exact capability resolution,
3. natural-language interpretation,
4. orchestration/execution.

The MCP server preserves those boundaries.

Phase 1 exposes deterministic discovery and exact resolution only.

A later natural-language tool may wrap the existing admitted model-capability pipeline, but only when a qualified provider is explicitly configured. It must return the admitted intent and deterministic resolver result so that probabilistic interpretation remains inspectable.

### AD-5 — Skills are primarily Resources; meta-operations are Tools

Skill bodies, references, schemas, contracts, generated graphs, and architecture documents are information and should be exposed as MCP Resources.

Operations that accept arguments and compute a result are MCP Tools.

Do not register one MCP Tool per skill.

## 3. Target component model

```text
MCP client
(ChatGPT / Codex / Claude / IDE / local agent)
        |
        | MCP 2026-07-28 or compatible legacy negotiation
        v
+-----------------------------+
| skillz-mcp                  |
|                             |
|  MCP transport + schemas    |
|          |                  |
|  tool/resource adapters     |
|          |                  |
|  skillz_core                |
|   - catalog                 |
|   - query                   |
|   - resolver                |
|   - graph                   |
|   - provenance/status       |
|   - validation facade       |
+-------------+---------------+
              |
              v
+-----------------------------+
| canonical repository data   |
|                             |
| docs/skill-capability-      |
|   index.json                |
| docs/skill-dependency-      |
|   graph.json                |
| skills/*/SKILL.md           |
| skills/*/references/*       |
| schemas/*                   |
| contracts/*                 |
| evaluations/*               |
| VERSION                     |
+-----------------------------+
```

## 4. Proposed repository structure

The MCP code should be isolated from portable skill content while sharing a small importable core with existing CLIs.

```text
src/
  skillz_core/
    __init__.py
    catalog.py
    query.py
    resolver.py
    graph.py
    provenance.py
    validation.py

mcp/
  pyproject.toml
  src/
    skillz_mcp/
      __init__.py
      server.py
      tools.py
      resources.py
      paths.py
      settings.py
  tests/
    test_tools.py
    test_resources.py
    test_contract_parity.py
    test_stdio.py
    test_http.py

scripts/
  query_capabilities.py       # compatibility CLI over skillz_core
  resolve_capabilities.py     # compatibility CLI over skillz_core
  ...
```

An alternative single root `pyproject.toml` is acceptable if implementation work demonstrates that it does not complicate the repository's portable distribution model. The important boundary is shared deterministic core vs MCP adapter, not the exact packaging directory.

## 5. MCP surface v1

### 5.1 Tools

The v1 public tool surface should remain small.

#### `search_skills`

Purpose: deterministic discovery of skills from the canonical index.

Inputs:

- `query?: string`
- `category?: string`
- `include_internal?: boolean = false`
- `limit?: integer`

Rules:

- Match only declared index fields.
- Preserve existing deterministic `/skills <query>` semantics unless the specification explicitly introduces a versioned extension.
- Never invent synonyms or semantic matches.
- Return stable ordering.

#### `get_skill`

Purpose: return structured metadata for one exact skill and Resource URIs for progressive disclosure.

Inputs:

- `name: string`

Result includes at least:

- name,
- description,
- invocation metadata,
- requires,
- dependents,
- outputs,
- output contracts,
- portable files,
- evaluation metadata,
- Resource URI for `SKILL.md`,
- available reference/resource children.

Unknown names fail explicitly.

#### `resolve_capabilities`

Purpose: expose the existing exact structured resolver.

Inputs mirror the versioned resolver request:

- outputs,
- dependencies,
- evaluation modes,
- portable-files constraint.

Rules:

- Intersection only.
- No natural-language interpretation.
- No ranking.
- Unknown declared constraints are errors.
- Ambiguous output producers remain ambiguous.

This tool is the MCP equivalent of `scripts/resolve_capabilities.py`, not a new router.

#### `get_dependencies`

Purpose: inspect composition edges for one skill.

Inputs:

- `name: string`
- `direction: requires | dependents`
- `transitive?: boolean = false`

Rules:

- Direct edges come from canonical `requires`/generated dependency data.
- Transitive traversal must be cycle-safe even though repository validation rejects cycles.
- Return deterministic topological or lexical ordering as specified by the contract.

#### `find_producers`

Purpose: find declared producers of an exact output contract.

Inputs:

- `output: string`

Result includes all producers and ambiguity status. The MCP server must never choose a preferred producer when the repository marks the output ambiguous.

#### `find_consumers`

Purpose: return declared downstream consumers for an exact output contract or producer/output pair.

Inputs:

- `output: string`
- optional `producer: string`

The result is derived from `outputContracts`; it does not infer dataflow from prose.

#### `catalog_status`

Purpose: return identity and freshness evidence.

Result includes when available:

- repository,
- ref,
- version,
- exact source commit SHA,
- capability-index schema version,
- skill count,
- entrypoint count,
- evaluation summary,
- catalog content hash.

`current` must only be asserted when exact source identity can be proven. A matching semantic version alone is not sufficient.

#### `validate_catalog`

Purpose: provide a read-only validation facade suitable for MCP clients.

Phase 1 should validate loaded catalog/graph invariants without executing arbitrary repository scripts. It may report which repository-native validation commands should be run for full CI parity.

Full repository validation remains a CI/build responsibility unless a later design safely exposes it.

### 5.2 Deferred tools

The following names are intentionally **not** in the phase-1 public surface:

- `resolve_workflow`
- `interpret_goal`
- `execute_skill`
- `execute_workflow`
- any provider-specific tool

`resolve_workflow` requires additional semantics beyond the current exact resolver. It belongs to Phase 2 after deterministic graph composition rules are specified and tested.

`interpret_goal` may later wrap the existing model-capability pipeline, but must be opt-in and provider-qualified.

Execution belongs to Phase 3.

## 6. MCP Resources

The server should expose progressive-disclosure resources with stable URIs.

Recommended URI space:

```text
skillz://index
skillz://graph
skillz://status
skillz://skills/{name}
skillz://skills/{name}/SKILL.md
skillz://skills/{name}/references/{relative-path}
skillz://skills/{name}/assets/{relative-path}
skillz://schemas/{name}
skillz://contracts/{name}
skillz://docs/{name}
```

### Resource rules

- Resource paths are resolved only under explicit allowlisted repository roots.
- `..`, absolute paths, symlink escape, and encoded path traversal are rejected.
- Binary resources are not exposed in Phase 1 unless a concrete client need is demonstrated.
- `scripts/` are not generally exposed as executable resources; source may be exposed later for inspection if explicitly allowlisted.
- Resource content should include or be associated with catalog source identity where the MCP SDK permits metadata.

## 7. Progressive disclosure

A client should normally receive:

1. compact discovery metadata from `search_skills`,
2. structured metadata from `get_skill`,
3. `SKILL.md` only for selected skills,
4. references/assets/contracts only when required.

The server must avoid returning the entire 129+ skill corpus in one call merely because it is available.

This keeps context cost approximately proportional to the selected workflow rather than to repository size.

## 8. Graph semantics

The server must preserve existing repository semantics:

- hard dependency edges come only from `requires`,
- cycles are invalid,
- `outputs` are handoff-contract declarations,
- all producers are recorded,
- ambiguous output contracts remain ambiguous,
- no producer-consumer edge is guessed where the repository cannot prove one,
- orphan outputs are informational unless separately prohibited.

Phase-2 workflow composition may traverse these edges but may not manufacture missing dependencies from natural-language descriptions.

## 9. Natural-language interpretation boundary

The repository already contains a model-capability pipeline that:

1. builds an interpretation request,
2. invokes a provider,
3. adapts the proposal,
4. performs review/admission,
5. compiles admitted intent,
6. invokes the deterministic resolver.

If MCP later exposes this capability, the server must not collapse these stages into an opaque `best_skill` function.

The response must retain:

- request identity,
- provider/model identity,
- qualification evidence,
- admitted capability intent,
- review/admission state,
- deterministic resolver output,
- explicit failed stage when unsuccessful.

No external model provider is configured or called by default.

## 10. Transport strategy

### Local

Use MCP stdio for local clients and developer workflows.

### Remote

Use stateless Streamable HTTP for remote clients.

The implementation should target the current MCP 2026-07-28 protocol through the official Python MCP SDK v2 while retaining SDK-provided compatibility with supported legacy clients.

The application itself should not implement protocol negotiation manually.

## 11. Caching and catalog identity

The catalog is mostly immutable within one deployed source commit, making it highly cacheable.

At build/deployment time:

1. identify the exact source commit,
2. create the runtime-stamped capability index using the existing provenance mechanism,
3. compute a deterministic content hash over canonical MCP catalog inputs,
4. start the server with that immutable identity.

The process should keep parsed index/graph data in memory and invalidate only when the configured source identity changes.

For local development, explicit reload mode may watch file mtimes or reload per request. Production should prefer immutable deploys over mutable live repositories.

## 12. Security model

### Phase-1 guarantees

- read-only filesystem access,
- no repository writes,
- no GitHub writes,
- no arbitrary subprocess execution,
- no skill-script execution,
- no model-provider call by default,
- no secrets in catalog responses,
- strict resource-root allowlist,
- bounded request and response sizes,
- explicit errors for unknown resource paths and schema versions.

### Remote deployment

Authentication and network exposure are deployment concerns but must be designed before public exposure.

Recommended initial posture:

- private endpoint,
- TLS terminated by the existing reverse proxy,
- authenticated access,
- rate/size limits,
- structured request logging without skill-content or secret leakage.

Local stdio requires no network authentication.

## 13. Versioning

There are three distinct version axes:

1. `skillz` repository release version (`VERSION`),
2. capability-index schema version,
3. `skillz-mcp` API/package version.

They must not be conflated.

Breaking MCP tool/resource contract changes require a `skillz-mcp` major version or a versioned tool/schema transition even when repository skill content changes only by patch/minor versions.

Every production response should be traceable to an exact repository source commit.

## 14. Testing strategy

### Unit tests

Cover:

- capability-index loading and schema rejection,
- deterministic search behavior,
- exact resolution behavior,
- dependency traversal,
- ambiguous outputs,
- unknown skill/output errors,
- path traversal rejection,
- provenance/status rules,
- catalog hash stability.

### Contract-parity tests

For the same input, MCP tools and existing CLI JSON output must agree on shared semantics.

Examples:

- `search_skills` vs `query_capabilities.py --skills ... --json`,
- `get_skill` vs `--skill ... --json`,
- `resolve_capabilities` vs `resolve_capabilities.py --request ... --json`.

These tests prevent the MCP layer from becoming a divergent second implementation.

### MCP integration tests

Use the official MCP client against the in-process/stdio server to verify:

- server discovery,
- tool listing,
- tool calls,
- resource listing/read,
- errors,
- protocol compatibility.

Add Streamable HTTP integration tests before remote deployment.

### Repository gates

The existing repository metadata checks, dependency-cycle checks, schema validation, evaluation scoring, and skill validation continue to run independently of MCP tests.

## 15. Phased delivery

### Phase 0 — Core extraction

Refactor reusable deterministic logic out of CLI-only modules while preserving current CLI output and tests.

### Phase 1 — Read-only MCP registry

Deliver:

- stdio server,
- deterministic tools listed in Section 5.1,
- progressive-disclosure resources,
- catalog provenance/status,
- contract-parity tests.

No semantic LLM routing and no execution.

### Phase 2 — Graph wayfinding

Specify and add:

- deterministic workflow graph traversal,
- explainable route construction,
- gap detection,
- alternatives when contracts are ambiguous,
- optional `resolve_workflow` once its semantics are stable.

### Phase 2b — Optional admitted natural-language routing

Wrap the existing model-capability pipeline only behind explicit configuration and provider qualification.

### Phase 3 — Execution gateway

Only after separate architecture approval, define an execution gateway that delegates to capable hosts/adapters rather than reimplementing browser, GitHub, document, shell, or agent runtimes inside `skillz-mcp`.

## 16. Compatibility with existing distributions

The OpenAI/Codex plugin distribution remains valid and is not replaced by MCP.

MCP becomes another distribution/access surface over the same capability source of truth.

Longer term, slash commands such as `/skills` and `/skill <name>` may be implemented by calling the MCP tools/resources, but their current repository semantics remain authoritative during migration.

## 17. Principal risks

### Risk: turning MCP into a second catalog

Mitigation: no hand-maintained MCP registry; derive from canonical generated metadata.

### Risk: semantic router drift

Mitigation: preserve deterministic resolver and admitted model pipeline as separate stages.

### Risk: one-tool-per-skill explosion

Mitigation: fixed meta-tool surface plus Resources.

### Risk: hidden execution authority

Mitigation: Phase 1 is read-only and cannot execute skill scripts or external actions.

### Risk: Python CLI and MCP behavior diverge

Mitigation: extract shared core and require parity tests.

### Risk: stale catalog identity

Mitigation: runtime stamping with exact source SHA and fail-closed freshness semantics.

## 18. Architecture acceptance criteria

This architecture is successfully implemented when:

1. adding a new correctly indexed skill requires no MCP code change,
2. an MCP client can discover and inspect skills without loading the whole corpus,
3. deterministic MCP queries match existing CLI semantics,
4. ambiguous output contracts remain visibly ambiguous,
5. every response can be tied to a catalog version and, in production, exact source SHA,
6. the server cannot write to the repository or execute skills in Phase 1,
7. local stdio and remote stateless HTTP use the same domain logic,
8. existing plugin/slash-command distribution continues to work unchanged.
