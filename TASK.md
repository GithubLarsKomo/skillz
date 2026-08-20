# TASK — Skillz MCP Server

## Goal

Implement the read-only `skillz-mcp` server defined by `docs/MCP-ARCHITECTURE.md` and `SPEC.md` without changing canonical skill semantics or introducing skill execution.

Tasks are ordered to keep each step independently reviewable and to preserve existing CLI behavior throughout the refactor.

## Phase 0 — Baseline and shared core

### T0.1 Capture baseline behavior

- [ ] Run the current repository validation suite on `feat/mcp-server` before implementation changes.
- [ ] Record current results for generated metadata checks, dependency graph validation, schema validation, skill evaluations, and existing capability-pipeline tests.
- [ ] Add representative golden JSON fixtures for current `query_capabilities.py` and `resolve_capabilities.py` behavior if equivalent fixtures do not already exist.

**Done when:** a failing later refactor can be distinguished from a pre-existing failure.

### T0.2 Introduce importable `skillz_core` package

- [ ] Create an importable package for deterministic catalog behavior.
- [ ] Move or extract index loading and schema-version validation from CLI scripts.
- [ ] Move or extract deterministic search/listing behavior.
- [ ] Move or extract exact skill lookup.
- [ ] Move or extract exact capability resolution.
- [ ] Move or extract provenance/status logic.
- [ ] Preserve current error semantics.

**Constraint:** do not change public CLI output intentionally in this task.

**Done when:** shared logic can be called directly from tests without invoking subprocesses.

### T0.3 Convert existing CLIs to compatibility wrappers

- [ ] Refactor `scripts/query_capabilities.py` to call `skillz_core`.
- [ ] Refactor `scripts/resolve_capabilities.py` to call `skillz_core`.
- [ ] Preserve CLI flags, exit codes, stable ordering, and JSON shapes.
- [ ] Run existing CLI tests.
- [ ] Add parity tests comparing pre-refactor fixtures with new wrapper output.

**Done when:** users and slash-command integrations see no behavioral change.

### T0.4 Add graph query helpers

- [ ] Load canonical/generated dependency metadata.
- [ ] Implement direct `requires` lookup.
- [ ] Implement direct `dependents` lookup.
- [ ] Implement transitive traversal with deterministic ordering.
- [ ] Implement exact output producer lookup.
- [ ] Implement output consumer lookup from `outputContracts`.
- [ ] Preserve ambiguous producer sets without ranking.

**Done when:** graph helpers are fully deterministic and unit tested.

### T0.5 Add catalog identity helper

- [ ] Define deterministic catalog hash inputs.
- [ ] Include capability index and graph identity at minimum.
- [ ] Reuse existing `VERSION` and runtime provenance semantics.
- [ ] Ensure `current` requires exact commit evidence.
- [ ] Add tests for `current`, `stale`, `unknown`, and unstamped development states.

**Done when:** identical canonical inputs produce identical identity and freshness results.

## Phase 1A — MCP package skeleton

### T1.1 Create isolated MCP package

- [ ] Add MCP package metadata under the chosen repository structure.
- [ ] Declare supported Python version.
- [ ] Add official MCP Python SDK v2 dependency with compatible major constraint.
- [ ] Keep MCP dependencies out of portable skill bundles and unrelated distribution builds.
- [ ] Add package-local test configuration.

**Done when:** the MCP package installs independently in a clean environment.

### T1.2 Implement server factory

- [ ] Create one server factory used by all transports.
- [ ] Set stable server identity `skillz-mcp`.
- [ ] Load repository/catalog configuration explicitly.
- [ ] Load catalog once for immutable production mode.
- [ ] Fail startup clearly on unsupported capability-index schema.
- [ ] Log loaded version/commit/schema identity without dumping catalog content.

**Done when:** an in-process MCP client can discover the server.

### T1.3 Add stdio entry point

- [ ] Add documented stdio command/entry point.
- [ ] Ensure stdout is reserved for protocol traffic.
- [ ] Send diagnostics to stderr/structured logging as required by the SDK.
- [ ] Add stdio smoke test.

**Done when:** an official MCP client can connect over stdio and list tools/resources.

## Phase 1B — MCP tools

### T1.4 Implement `search_skills`

- [ ] Implement SPEC input schema.
- [ ] Reuse deterministic search/listing core.
- [ ] Default to user-facing entrypoints only.
- [ ] Support category filtering.
- [ ] Support `include_internal`.
- [ ] Apply bounded limit.
- [ ] Return compact metadata only.
- [ ] Add CLI/MCP parity tests.

**Done when:** representative `/skills` and `/skills <query>` cases match existing semantics.

### T1.5 Implement `get_skill`

- [ ] Require exact skill name.
- [ ] Return all indexed metadata fields required by SPEC.
- [ ] Return stable Resource URIs for body/references.
- [ ] Reject unknown names without fuzzy fallback.
- [ ] Add parity test against `query_capabilities.py --skill ... --json`.

**Done when:** a client can discover a skill compactly and then choose whether to load its body.

### T1.6 Implement `resolve_capabilities`

- [ ] Mirror resolver-request v1 fields.
- [ ] Reuse shared exact resolver.
- [ ] Preserve intersection semantics.
- [ ] Preserve unranked candidates.
- [ ] Preserve valid empty candidate results.
- [ ] Preserve explicit errors for unknown outputs/dependencies.
- [ ] Preserve ambiguous output contracts.
- [ ] Add parity tests against resolver CLI fixtures.

**Done when:** MCP and CLI produce semantically equivalent resolver output.

### T1.7 Implement `get_dependencies`

- [ ] Implement `requires|dependents` direction enum.
- [ ] Implement direct traversal.
- [ ] Implement optional transitive traversal.
- [ ] Return deterministic order and traversal evidence.
- [ ] Reject unknown skills.

**Done when:** graph traversal is reproducible and covered by cycle-safety tests.

### T1.8 Implement `find_producers`

- [ ] Require exact output name.
- [ ] Return every declared producer.
- [ ] Return explicit ambiguity status.
- [ ] Reject unknown outputs.
- [ ] Add fixture with at least one ambiguous output when repository data permits; otherwise add isolated test fixture.

**Done when:** the server never silently selects one producer among several.

### T1.9 Implement `find_consumers`

- [ ] Derive consumers from `outputContracts` only.
- [ ] Support optional exact producer constraint.
- [ ] Reject producer/output mismatches.
- [ ] Add deterministic tests.

**Done when:** no consumer relationship depends on description-text inference.

### T1.10 Implement `catalog_status`

- [ ] Return repository/ref/version/commit when available.
- [ ] Return schema version and catalog counts.
- [ ] Return evaluation summary from index.
- [ ] Return deterministic catalog hash.
- [ ] Return fail-closed freshness status.
- [ ] Add tests proving version equality alone cannot produce `current`.

**Done when:** a client can identify exactly which skill corpus it is using.

### T1.11 Implement `validate_catalog`

- [ ] Validate loaded schema/invariants in process.
- [ ] Validate skill-name uniqueness.
- [ ] Validate required skill references.
- [ ] Validate dependency acyclicity or verified generated-graph consistency.
- [ ] Validate output-contract structure required for serving.
- [ ] Do not invoke shell commands or arbitrary scripts.
- [ ] Return recommended full repository validation commands separately.

**Done when:** the MCP validation call is safely read-only and clearly distinct from CI validation.

## Phase 1C — MCP Resources

### T1.12 Implement resource path policy

- [ ] Define explicit allowlisted roots.
- [ ] Implement canonical path normalization.
- [ ] Reject `..` traversal.
- [ ] Reject absolute paths.
- [ ] Reject encoded traversal variants.
- [ ] Detect/reject symlink escape where applicable.
- [ ] Apply text-size limits.
- [ ] Unit test attack cases.

**Done when:** no Resource URI can escape configured repository roots.

### T1.13 Implement catalog resources

- [ ] `skillz://index`
- [ ] `skillz://graph`
- [ ] `skillz://status`
- [ ] Add appropriate MIME/content type metadata.
- [ ] Keep responses traceable to catalog identity.

**Done when:** clients can inspect canonical generated metadata without filesystem knowledge.

### T1.14 Implement skill resources

- [ ] `skillz://skills/{name}` compact metadata.
- [ ] `skillz://skills/{name}/SKILL.md` canonical body.
- [ ] `skillz://skills/{name}/references/{relative-path}`.
- [ ] `skillz://skills/{name}/assets/{relative-path}` listing/metadata behavior.
- [ ] Do not serve arbitrary binaries in v1 unless explicitly approved.
- [ ] Reject resources for unknown skills.

**Done when:** progressive disclosure works for a selected skill without loading unrelated skill content.

### T1.15 Implement repository metadata resources

- [ ] `skillz://schemas/{name}`.
- [ ] `skillz://contracts/{name}`.
- [ ] `skillz://docs/{name}` with an explicit documentation allowlist or safe root policy.
- [ ] Add negative tests for unsupported paths/extensions.

**Done when:** schemas/contracts can be inspected through MCP without broad filesystem exposure.

## Phase 1D — Integration, HTTP, security

### T1.16 Add MCP integration test harness

- [ ] Use official MCP Python client.
- [ ] Test server discovery.
- [ ] Test tool listing.
- [ ] Test each tool success path.
- [ ] Test representative errors.
- [ ] Test resource listing/read.
- [ ] Test invalid-resource rejection.
- [ ] Test catalog identity exposure.

**Done when:** protocol behavior is tested independently of direct Python function calls.

### T1.17 Add stateless Streamable HTTP entry point

- [ ] Add HTTP server entry point using SDK-supported 2026-07-28 behavior.
- [ ] Reuse the same server/domain factory as stdio.
- [ ] Keep application state immutable/read-only.
- [ ] Add HTTP integration tests.
- [ ] Verify supported legacy compatibility through SDK behavior where practical.

**Done when:** an official MCP client can use the same tools/resources over HTTP.

### T1.18 Add remote authentication boundary

- [ ] Choose deployment authentication mechanism compatible with target MCP clients.
- [ ] Document reverse-proxy/TLS assumptions.
- [ ] Add request-size/rate-limit recommendations.
- [ ] Ensure the server is not documented as public/anonymous by default.

**Done when:** remote production deployment has an explicit authenticated threat boundary.

### T1.19 Add operational logging

- [ ] Structured startup identity log.
- [ ] Request type/tool/resource identifier.
- [ ] Latency and error category.
- [ ] No full skill-body logging by default.
- [ ] No credentials or provider secrets.

**Done when:** service operation can be diagnosed without leaking repository/user content unnecessarily.

## Phase 1E — CI and distribution compatibility

### T1.20 Add MCP CI job

- [ ] Install MCP package in clean environment.
- [ ] Run core unit tests.
- [ ] Run CLI/MCP parity tests.
- [ ] Run MCP integration tests.
- [ ] Keep existing `validate-skills` and generated-metadata gates intact.

**Done when:** MCP regressions block PRs without weakening existing repository gates.

### T1.21 Verify existing OpenAI/Codex plugin distribution

- [ ] Build existing plugin distribution after core extraction.
- [ ] Confirm no MCP dependency leaks into portable distribution.
- [ ] Confirm `/skills` discovery metadata remains unchanged unless intentionally versioned.

**Done when:** MCP is additive rather than a breaking replacement distribution.

### T1.22 Document local use

- [ ] Add stdio configuration example for common MCP clients.
- [ ] Document repository-root configuration.
- [ ] Document provenance behavior for unstamped local development.
- [ ] Document read-only/security boundary.

**Done when:** a developer can connect a local client without reading source code.

### T1.23 Document remote deployment

- [ ] Document immutable build/stamp step.
- [ ] Document exact source SHA injection/stamping.
- [ ] Document HTTP entry point.
- [ ] Document authentication/TLS boundary.
- [ ] Document health/operational checks without adding mutable server state.

**Done when:** deployment is reproducible from an exact repository commit.

## Phase 1 release gate

- [ ] All SPEC v1 requirements mapped to tests or documented implementation evidence.
- [ ] All existing repository validation gates pass.
- [ ] CLI/MCP parity suite passes.
- [ ] stdio MCP integration passes.
- [ ] HTTP MCP integration passes.
- [ ] resource path security suite passes.
- [ ] no skill execution or repository write path exists in MCP handlers.
- [ ] exact source identity is visible in production status.
- [ ] newly added indexed test skill is discoverable without MCP code changes.

**Phase 1 ends here. Do not add semantic routing or execution to close a Phase-1 gap.**

## Phase 2 — Deterministic graph wayfinding

Start only after Phase 1 is stable.

### T2.1 Specify workflow graph semantics

- [ ] Define what constitutes a workflow route.
- [ ] Define permitted edge types.
- [ ] Define starting and terminal conditions.
- [ ] Define ambiguity behavior.
- [ ] Define gap reporting.
- [ ] Define route ordering without arbitrary ranking.
- [ ] Add versioned workflow-result schema.

### T2.2 Implement workflow graph engine

- [ ] Compose only declared dependency/output edges.
- [ ] Produce explainable route evidence.
- [ ] Detect missing links.
- [ ] Return alternatives instead of silently resolving ambiguity.
- [ ] Add graph fixtures and property tests.

### T2.3 Add `resolve_workflow`

- [ ] Expose only after T2.1/T2.2 acceptance.
- [ ] Keep exact structured inputs distinct from natural-language interpretation.
- [ ] Return route evidence and unresolved ambiguities.

## Phase 2b — Optional admitted natural-language interpretation

Start only if there is a demonstrated client need.

### T2B.1 Reuse existing model-capability pipeline

- [ ] Wrap existing interpretation-request, provider-run, admission, compile, and deterministic resolver stages.
- [ ] Do not create a second prompt/router implementation.
- [ ] Require qualified provider configuration.
- [ ] Return admitted intent and deterministic result.
- [ ] Preserve explicit failed-stage reporting.

### T2B.2 Add `interpret_goal`

- [ ] Make provider use explicit.
- [ ] Document data sent to provider.
- [ ] Never call provider from `search_skills`, `get_skill`, or `resolve_capabilities`.
- [ ] Add fixture-mode tests and qualified-provider integration tests.

## Phase 3 — Execution gateway research only

Do not implement without a new approved architecture/SPEC.

- [ ] Identify target host runtimes and adapters.
- [ ] Define authorization model for reads vs writes vs side effects.
- [ ] Define execution evidence/handoff contracts.
- [ ] Define cancellation, retries, idempotency, and audit requirements.
- [ ] Prove that execution can be delegated without embedding browser/GitHub/document/shell runtimes inside the registry server.

## Recommended first implementation slice

Implement in this exact order:

1. T0.1 baseline.
2. T0.2 shared core extraction.
3. T0.3 CLI compatibility wrappers.
4. T1.1 MCP package skeleton.
5. T1.2 server factory.
6. T1.4 `search_skills`.
7. T1.5 `get_skill`.
8. T1.3 stdio entry point.
9. T1.16 minimal integration test for those two tools.

This slice proves the architecture with minimal surface area before graph, resources, HTTP, or deployment complexity is added.
