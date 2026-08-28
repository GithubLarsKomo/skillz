# Skillz Architecture Consolidation — P3 Benchmark Foundation

Status: implemented on `feat/skillz-architecture-p3`.

## Goal

Extend executable architecture coverage beyond the heavily benchmarked regulated-engineering domain without creating a second benchmark framework or overstating structural checks as real artifact execution.

## Implemented

### Versioned workflow benchmark contract

Added:

- `schemas/workflow-benchmark-v1.schema.json`
- `benchmarks/cross-domain-workflows-e2e-v1.json`

The contract captures for every scenario:

- stable scenario id,
- domain,
- canonical user-facing entrypoint,
- intent,
- expected worker sequence,
- `mustPreserve` invariants,
- `mustNotDo` boundaries.

The offline metadata validator now validates the cross-domain benchmark and implements regex `pattern` validation instead of silently ignoring schema patterns.

### Cross-domain executable contract regression

Added `tests/test_cross_domain_workflows_e2e.py`.

It verifies:

- unique scenario identity,
- active evaluated user-facing entrypoints,
- reachability of every sequence worker through the entrypoint's transitive `requires` closure,
- no unintended deprecated or compatibility-only skill in an active sequence,
- PASS evaluation evidence for every participant,
- non-placeholder preserve/forbidden invariants,
- retained shared-learning-delivery boundaries,
- no regression from Sport to the deprecated `sport-training-programming` facade,
- generic presentation routing through the generic template core,
- contract routing through the compatibility entrypoint plus canonical matter state machine.

### Covered workflow domains

The initial suite contains 11 cross-domain scenarios:

1. software performance optimization,
2. governed frontend redesign,
3. contract lifecycle to legal final gate,
4. person research to auditable report,
5. template presentation production,
6. single-video YouTube learning,
7. playlist/multi-video YouTube learning,
8. YouTube course building,
9. longitudinal sport athlete management,
10. thought capture to structured concept,
11. current-evidence purchase decision.

This is intentionally complementary to the existing regulated-engineering E2E suite.

### Workflow benchmark authoring capability

Added internal governance skill:

- `workflow-benchmark-authoring`

It composes:

- `skill-evaluation-suite-authoring`
- `artifact-contract-normalizer`

The worker requires dependency-closure evidence, active lifecycle/discoverability, current evaluation PASS, ownership checks and explicit preserve/forbidden invariants.

A binding rule prevents evidence inflation:

> Contract-level E2E is not equivalent to actual artifact execution.

Render, runtime, browser, compiler, API or document parity may only be claimed when a corresponding executable gate really performs that work.

### Durable architecture tests

Added:

- `tests/test_architecture_consolidation_p3.py`

Updated P2 regression tests to use baseline invariants rather than frozen exact repository counts. This keeps the architecture regression meaningful when legitimate future skills are added.

The normal `Validate skills` workflow now runs:

- cross-domain workflow E2E contracts,
- P2 architecture regression,
- P3 architecture regression.

## Validated health

After canonical metadata materialization:

- skills: **281**
- user-facing entrypoints: **231**
- discoverability: **229 public / 2 advanced / 48 internal / 2 compatibility**
- evaluation suites: **281**
- executed suites: **PASS**
- evaluation coverage: **281/281**
- user-facing coverage: **231/231**
- missing evaluation suites: **0**
- ambiguous outputs: **0**

## Validation performed

The feature-branch materialization run passed:

- dependency graph tests,
- metadata schema tests,
- role-selection schema and policy tests,
- repository metadata generation,
- cross-domain workflow E2E contracts,
- P2 architecture regression,
- P3 architecture regression,
- OpenAI plugin build,
- metadata reproducibility,
- Obsidian generation,
- repository contract validation,
- all 281 skill evaluation suites.

The temporary feature-branch metadata trigger was removed after materialization; `.github/workflows/sync-generated-metadata.yml` is restored to the canonical `main` version.

## Deliberately not claimed

The new cross-domain suite is an executable **contract/architecture** benchmark. It does not by itself prove that every workflow produced real external artifacts in CI.

Existing specialized artifact gates remain authoritative where available, for example Sport visual parity and document/presentation render verification.

## Remaining P3 work

Recommended next tranche:

1. evidence-based typed `consumes` expansion for high-value orchestrators and handoffs;
2. artifact-contract normalization focused on real producer/consumer evidence rather than reducing the unconsumed-output metric mechanically;
3. progressive thinning of selected domain document wrappers onto the generic document core;
4. review of public entrypoints that should move to `advanced` or `internal` discoverability;
5. branch protection / required-CI policy after the final check set is stable.

The `Outputs without inferred consumers` health metric remains a review queue, not an error target: terminal user-facing outputs are expected to remain unconsumed.
