# SPEC — Skillz MCP Server

## 1. Purpose

Implement a read-only Model Context Protocol server for `GithubLarsKomo/skillz` that exposes the repository's canonical capability catalog, dependency/output graph, skill resources, validation state, and provenance through a small stable MCP surface.

The implementation MUST reuse existing deterministic capability semantics and MUST NOT create a parallel skill registry, hidden semantic router, or skill-execution runtime.

Normative terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are used deliberately.

## 2. Scope

### 2.1 In scope for v1

- shared importable deterministic capability core,
- MCP stdio server,
- MCP stateless Streamable HTTP server,
- skill discovery,
- exact skill lookup,
- exact structured capability resolution,
- dependency traversal,
- output producer/consumer lookup,
- progressive-disclosure Resources,
- catalog provenance/status,
- read-only catalog validation facade,
- parity tests against existing CLI behavior,
- MCP integration tests,
- deployment documentation.

### 2.2 Out of scope for v1

- skill execution,
- workflow execution,
- repository mutation,
- GitHub mutation,
- arbitrary subprocess execution,
- automatic execution of files under `skills/*/scripts/`,
- one MCP tool per skill,
- implicit external LLM calls,
- semantic similarity/vector search,
- opaque natural-language `best skill` selection,
- public unauthenticated remote deployment.

## 3. Canonical inputs

### REQ-DATA-001

`docs/skill-capability-index.json` MUST remain the canonical skill discovery and capability metadata source.

### REQ-DATA-002

The MCP server MUST support capability-index `schemaVersion: 1` initially and MUST fail explicitly for unsupported versions.

### REQ-DATA-003

Dependency and output semantics MUST remain consistent with generated repository metadata:

- hard dependencies from `requires`,
- downstream declarations from `dependents`/generated graph,
- outputs from `outputs`,
- producer ambiguity from `outputContracts`,
- no guessed producer-consumer relationships.

### REQ-DATA-004

Skill text MUST be read from the exact indexed skill directory and not from a duplicated MCP copy.

### REQ-DATA-005

The server MUST treat `VERSION`, runtime-stamped capability provenance, and MCP package/API version as separate version axes.

## 4. Shared deterministic core

### REQ-CORE-001

Reusable behavior currently embedded in CLI scripts MUST be factored into importable modules without changing existing CLI semantics.

At minimum the shared core MUST cover:

- index loading/validation,
- deterministic skill listing/filtering,
- exact skill lookup,
- exact capability resolution,
- dependency lookup/traversal,
- output producer/consumer lookup,
- provenance/status evaluation.

### REQ-CORE-002

`scripts/query_capabilities.py` and `scripts/resolve_capabilities.py` MUST remain supported compatibility entry points.

### REQ-CORE-003

For equivalent inputs, the CLI JSON result and MCP tool result MUST be semantically identical for shared fields.

### REQ-CORE-004

The shared core MUST NOT depend on MCP transport classes.

## 5. MCP implementation platform

### REQ-MCP-001

The server SHOULD use the official Python MCP SDK v2.

Rationale: the repository's capability and validation implementation is already Python-first, allowing direct reuse and parity testing.

### REQ-MCP-002

The implementation MUST target MCP protocol revision 2026-07-28 through SDK-supported negotiation/serving behavior rather than hand-written protocol negotiation.

### REQ-MCP-003

The same domain/core logic MUST serve both stdio and Streamable HTTP transports.

### REQ-MCP-004

The server MUST expose a stable server name `skillz-mcp` and an independently versioned server package/API version.

## 6. MCP Tools v1

The v1 tool names below are normative.

### 6.1 `search_skills`

#### Input

```json
{
  "query": "optional string",
  "category": "optional category slug",
  "include_internal": false,
  "limit": 50
}
```

#### Requirements

- **REQ-TOOL-SEARCH-001:** default discovery MUST exclude non-user-facing skills.
- **REQ-TOOL-SEARCH-002:** `include_internal=true` MAY include all indexed skills.
- **REQ-TOOL-SEARCH-003:** query matching MUST be deterministic and limited to declared metadata fields.
- **REQ-TOOL-SEARCH-004:** v1 MUST NOT perform synonym expansion, embeddings, semantic similarity, or LLM ranking.
- **REQ-TOOL-SEARCH-005:** category filtering MUST use declared invocation category.
- **REQ-TOOL-SEARCH-006:** results MUST have deterministic ordering.
- **REQ-TOOL-SEARCH-007:** result items MUST remain compact and MUST NOT inline complete `SKILL.md` bodies.

### 6.2 `get_skill`

#### Input

```json
{
  "name": "exact-skill-name"
}
```

#### Requirements

- **REQ-TOOL-SKILL-001:** names MUST match exactly.
- **REQ-TOOL-SKILL-002:** unknown skills MUST produce an explicit MCP error/result error; no fuzzy fallback is allowed.
- **REQ-TOOL-SKILL-003:** result MUST include description, invocation metadata, dependencies, dependents, outputs, output contracts, portable files, and evaluation metadata when present.
- **REQ-TOOL-SKILL-004:** result MUST include Resource URI(s) for progressive disclosure of the skill body and available reference children.

### 6.3 `resolve_capabilities`

#### Input

Equivalent to capability-resolver request v1:

```json
{
  "outputs": [],
  "dependencies": [],
  "evaluationModes": [],
  "portableFiles": "irrelevant"
}
```

#### Requirements

- **REQ-TOOL-RESOLVE-001:** behavior MUST reuse the existing deterministic resolver semantics.
- **REQ-TOOL-RESOLVE-002:** constraints MUST be combined by intersection.
- **REQ-TOOL-RESOLVE-003:** candidates MUST be unranked.
- **REQ-TOOL-RESOLVE-004:** unknown output or dependency names MUST be explicit errors.
- **REQ-TOOL-RESOLVE-005:** empty candidate sets MUST be valid results.
- **REQ-TOOL-RESOLVE-006:** ambiguous output contracts MUST remain ambiguous.
- **REQ-TOOL-RESOLVE-007:** the tool MUST NOT interpret natural-language goals.

### 6.4 `get_dependencies`

#### Input

```json
{
  "name": "skill-name",
  "direction": "requires",
  "transitive": false
}
```

`direction` MUST be `requires` or `dependents`.

#### Requirements

- **REQ-TOOL-DEPS-001:** direct traversal MUST reflect canonical declared graph edges.
- **REQ-TOOL-DEPS-002:** transitive traversal MUST be deterministic and cycle-safe.
- **REQ-TOOL-DEPS-003:** unknown skills MUST be explicit errors.
- **REQ-TOOL-DEPS-004:** traversal MUST NOT infer relationships from descriptions.

### 6.5 `find_producers`

#### Input

```json
{
  "output": "exact-output-name"
}
```

#### Requirements

- **REQ-TOOL-PROD-001:** return all exact declared producers.
- **REQ-TOOL-PROD-002:** result MUST state whether the output is ambiguous.
- **REQ-TOOL-PROD-003:** the server MUST NOT choose a preferred producer when more than one is declared.
- **REQ-TOOL-PROD-004:** unknown outputs MUST be explicit errors.

### 6.6 `find_consumers`

#### Input

```json
{
  "output": "exact-output-name",
  "producer": "optional-exact-skill-name"
}
```

#### Requirements

- **REQ-TOOL-CONS-001:** consumers MUST be derived from output-contract metadata only.
- **REQ-TOOL-CONS-002:** when `producer` is supplied, it MUST be validated as an actual declared producer for the requested output.
- **REQ-TOOL-CONS-003:** no consumer MAY be inferred from prose.

### 6.7 `catalog_status`

#### Input

No required arguments.

#### Result

At minimum:

```json
{
  "repository": "GithubLarsKomo/skillz",
  "ref": "...",
  "version": "...",
  "commitSha": "... or null",
  "indexSchemaVersion": 1,
  "skillCount": 0,
  "entrypointCount": 0,
  "evaluationPassed": true,
  "catalogHash": "...",
  "freshness": "current|stale|unknown|not-compared"
}
```

#### Requirements

- **REQ-TOOL-STATUS-001:** exact source commit MUST be preferred over semantic version for identity.
- **REQ-TOOL-STATUS-002:** `current` MUST NOT be asserted solely from a matching version.
- **REQ-TOOL-STATUS-003:** catalog hash MUST be deterministic for identical canonical inputs.
- **REQ-TOOL-STATUS-004:** local un-stamped development states MAY report `unknown` or `not-compared` rather than inventing provenance.

### 6.8 `validate_catalog`

#### Requirements

- **REQ-TOOL-VALIDATE-001:** validation MUST be read-only.
- **REQ-TOOL-VALIDATE-002:** v1 MUST NOT execute arbitrary repository scripts or shell commands as part of an MCP request.
- **REQ-TOOL-VALIDATE-003:** validation MUST cover in-memory catalog invariants necessary for safe serving.
- **REQ-TOOL-VALIDATE-004:** the response MAY list repository-native commands required for full CI-equivalent validation.
- **REQ-TOOL-VALIDATE-005:** full CI validation remains a build/CI responsibility.

## 7. MCP Resources v1

### REQ-RES-001

The server MUST support these resource families:

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

### REQ-RES-002

Resource lookup MUST use explicit allowlisted roots.

### REQ-RES-003

Path traversal using `..`, absolute paths, encoded traversal, or symlink escape MUST be rejected.

### REQ-RES-004

Phase 1 SHOULD expose UTF-8 text resources only. Binary assets MAY be listed as metadata but SHOULD NOT be served until a concrete client requirement exists.

### REQ-RES-005

Reading `skillz://skills/{name}` SHOULD return compact structured metadata; reading `.../SKILL.md` returns the full canonical skill body.

### REQ-RES-006

The server MUST NOT bulk-inline all skill bodies in catalog discovery responses.

## 8. Progressive disclosure

### REQ-PD-001

A normal client flow SHOULD be:

1. `search_skills`,
2. `get_skill`,
3. read selected `SKILL.md`,
4. read selected references/contracts only as needed.

### REQ-PD-002

Context volume SHOULD scale with selected skills rather than total repository size.

## 9. Natural-language capability routing

### REQ-NL-001

Natural-language interpretation is NOT part of the v1 MCP surface.

### REQ-NL-002

A future `interpret_goal` or `resolve_workflow` capability MUST reuse the repository's existing capability-intent/model-admission pipeline rather than introduce an independent semantic router.

### REQ-NL-003

Any future provider-backed interpretation MUST require explicit provider configuration and qualification.

### REQ-NL-004

No external provider may be called implicitly by basic discovery or deterministic resolution tools.

## 10. Workflow resolution

### REQ-WF-001

`resolve_workflow` MUST NOT be exposed until Phase 2 specifies deterministic graph composition semantics.

### REQ-WF-002

Phase-2 workflow composition MUST preserve ambiguity and MUST NOT fabricate dependency or output edges.

### REQ-WF-003

A workflow result MUST be explainable as repository-declared edges plus explicitly identified interpretation decisions.

## 11. Execution boundary

### REQ-EXEC-001

Phase 1 MUST NOT expose `execute_skill` or `execute_workflow`.

### REQ-EXEC-002

A future execution gateway MUST delegate to external capable runtimes/adapters and MUST NOT duplicate browser, GitHub, shell, document, or agent runtime functionality inside the MCP registry server.

### REQ-EXEC-003

Any future write or side-effect capability requires a separate architecture/security approval.

## 12. Caching and provenance

### REQ-CACHE-001

Production deployments SHOULD use an immutable repository snapshot identified by exact source commit.

### REQ-CACHE-002

The existing runtime capability-index stamping mechanism SHOULD be used during build/deployment.

### REQ-CACHE-003

Parsed capability index and graph SHOULD be cached in process for the immutable deployment lifetime.

### REQ-CACHE-004

Development reload mode MAY reload on file changes but MUST NOT alter production identity semantics.

### REQ-CACHE-005

Tool/resource list caching MAY use the catalog identity as the invalidation boundary where supported by the MCP SDK/protocol.

## 13. Security

### REQ-SEC-001

Phase 1 filesystem access MUST be read-only.

### REQ-SEC-002

Only configured repository roots may be read.

### REQ-SEC-003

MCP requests MUST NOT trigger shell commands, Git commands, GitHub writes, network fetches, or skill-script execution.

### REQ-SEC-004

The server MUST impose bounded input lengths and sensible response-size limits.

### REQ-SEC-005

Remote HTTP deployment MUST require authenticated access before it is considered production-ready.

### REQ-SEC-006

Logs MUST NOT contain secrets and SHOULD avoid logging full skill bodies or user-provided source text by default.

### REQ-SEC-007

Provider credentials, if Phase 2b is later enabled, MUST come from deployment configuration and MUST NOT be stored in the capability catalog.

## 14. Error behavior

### REQ-ERR-001

Unknown skill names, output names, dependency names, unsupported schema versions, invalid resource paths, and invalid enum values MUST fail explicitly.

### REQ-ERR-002

Errors MUST distinguish invalid input from valid empty results.

Example: no skills satisfying valid exact constraints is a valid resolver result, not a transport error.

### REQ-ERR-003

The server MUST NOT broaden a failed exact query into fuzzy or semantic matching.

## 15. Testing

### REQ-TEST-001 — unit tests

Unit tests MUST cover at least:

- index schema acceptance/rejection,
- search visibility/category/query behavior,
- exact skill lookup,
- resolver intersection,
- unknown constraints,
- empty candidate set,
- ambiguous output contracts,
- dependency traversal,
- producer/consumer lookup,
- path traversal rejection,
- provenance/freshness,
- deterministic catalog hash.

### REQ-TEST-002 — CLI/MCP parity

Parity tests MUST compare MCP/domain results with current CLI JSON semantics for shared operations.

### REQ-TEST-003 — MCP integration

Integration tests MUST verify with an official MCP client:

- server discovery,
- tool listing,
- successful tool calls,
- expected tool errors,
- resource listing/read,
- invalid resource rejection,
- stdio transport.

### REQ-TEST-004 — HTTP integration

Streamable HTTP integration tests MUST pass before remote deployment.

### REQ-TEST-005 — existing gates

Existing repository generation, schema, graph, evaluation, and skill validation checks MUST continue to pass unchanged unless an explicitly reviewed refactor updates them.

## 16. Packaging and deployment

### REQ-PKG-001

MCP-specific dependencies MUST NOT become dependencies of portable skill bundles unless required by that distribution.

### REQ-PKG-002

The MCP package MUST declare a supported Python version and pin the MCP SDK to a compatible major range.

### REQ-PKG-003

Provide separate documented entry points for:

- stdio,
- Streamable HTTP.

### REQ-PKG-004

The server MUST be runnable against an explicitly configured repository root or packaged immutable catalog snapshot.

### REQ-PKG-005

The existing OpenAI/Codex plugin distribution MUST continue to build independently.

## 17. Observability

### REQ-OBS-001

The server SHOULD emit structured operational logs for startup, catalog identity, request type, latency, and errors.

### REQ-OBS-002

Logs SHOULD use identifiers and counts rather than full content where possible.

### REQ-OBS-003

Startup MUST report the loaded repository/version/commit identity and supported capability-index schema version.

## 18. Compatibility

### REQ-COMPAT-001

Adding a new valid indexed skill MUST require zero MCP code changes.

### REQ-COMPAT-002

Adding a new user-facing category MUST require zero MCP code changes unless the MCP API itself constrains categories.

### REQ-COMPAT-003

New output contracts MUST be discoverable automatically from generated metadata.

### REQ-COMPAT-004

Existing `/skills`, `/skills all`, `/skills <query>`, `/skills status`, and `/skill <name>` semantics remain authoritative until a client is explicitly migrated to MCP.

## 19. Acceptance criteria for v1

The feature is complete when all of the following are true:

1. `skillz-mcp` starts over stdio and exposes the specified v1 tool/resource surface.
2. The same server logic can be hosted as stateless Streamable HTTP.
3. `search_skills`, `get_skill`, and `resolve_capabilities` pass parity tests against existing deterministic CLI behavior.
4. Dependency and output-contract queries preserve ambiguity and never infer edges from prose.
5. Resource traversal cannot escape allowlisted roots.
6. Production catalog identity includes exact source commit SHA.
7. MCP requests cannot mutate the repository or execute skill scripts.
8. Existing repository validation and plugin distribution remain green.
9. A newly added indexed skill appears through MCP without changing MCP source code.
10. No external model provider is required for Phase-1 server startup or use.
