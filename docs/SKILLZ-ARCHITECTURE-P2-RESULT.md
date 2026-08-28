# Skillz Architecture Consolidation — P2 Result

Date: 2026-08-28  
Branch: `feat/skillz-architecture-p2`  
Parent wave: `docs/SKILLZ-ARCHITECTURE-CONSOLIDATION.md`

## Status

P2 is implemented and repository-native validation passed before cleanup of the temporary materialization helper.

Generated capability health at the validated P2 tree:

- 280 skills;
- 231 user-facing entrypoints;
- discoverability: 229 `public`, 2 `advanced`, 47 `internal`, 2 `compatibility`;
- 280/280 evaluation suites present;
- 280/280 executed suites PASS;
- evaluation coverage complete;
- 0 missing user-facing evaluations;
- 0 ambiguous outputs.

## P2.1 Lifecycle and discoverability

Lifecycle remains represented by the existing `status` axis:

- `draft`
- `candidate`
- `stable`
- `deprecated`

Discoverability is now a separate resolved governance axis:

- `public` — normal user-facing entrypoint;
- `advanced` — user-facing but intentionally targeted rather than default discovery;
- `internal` — composition-only;
- `compatibility` — deprecated explicit-use-only surface.

For existing skills without explicit metadata, the capability index resolves discoverability backwards-compatibly:

1. deprecated -> `compatibility`;
2. user-facing -> `public`;
3. otherwise -> `internal`.

`advanced` is always explicit. This replaces the earlier draft proposal `primary|advanced|internal`; `public` is used instead of `primary` because it describes visibility rather than ranking or recommendation priority. `compatibility` was added because deprecated legacy surfaces require different treatment from ordinary internal workers.

New deprecations require:

```yaml
status: deprecated
discoverability: compatibility
deprecatedSince: YYYY-MM-DD
replacedBy: replacement-skill
```

Deprecated skills must not remain normal user-facing entrypoints.

## P2.2 Canonical one-shot sport planning

A new `sport-training-plan-workflow` is the canonical entrypoint for a one-shot executable training plan.

It composes:

- `sport-athlete-profile`;
- `sport-performance-diagnostics`;
- `sport-goal-performance-model`;
- `sport-season-periodization`;
- `sport-mesocycle-planning`;
- `sport-microcycle-planning`;
- `sport-strength-power-programming`;
- `sport-endurance-programming`.

Only `sport-training-plan-workflow` owns `sport-training-plan.json`.

`sport-athlete-management` remains the longitudinal closed-loop orchestrator for monitoring, adaptation and plan revision. It now points one-shot requests to `sport-training-plan-workflow`.

`sport-diagnostics-training-report-workflow` was migrated from the legacy monolith to `sport-training-plan-workflow` before the old planner was deprecated.

## P2.3 Legacy sport compatibility façade

`sport-training-programming` is now:

- `status: deprecated`;
- `discoverability: compatibility`;
- explicit-use-only;
- `replacedBy: sport-training-plan-workflow`.

It no longer owns `sport-training-plan.json`. Its only output is:

- `sport-training-programming-compatibility-run.json`.

The façade may normalize old inputs and reference the replacement plan, but it must not reactivate a parallel periodization, strength, endurance or taper engine.

The legacy direct ReportLab renderer `dr-komorowski-sport-report-renderer` was also brought under the same explicit lifecycle contract and its evaluation was converted from a full-renderer expectation to compatibility behavior.

## P2.4 Governance capabilities

Added advanced user-facing governance capabilities:

- `skill-portfolio-audit`;
- `skill-lifecycle-migration`.

Added internal governance workers:

- `skill-evaluation-suite-authoring`;
- `artifact-contract-normalizer`.

This split is intentional: repository owners can explicitly invoke the two portfolio-level workflows, while evaluation fixture authoring and artifact normalization remain composition primitives and do not inflate the normal entrypoint surface.

## P2.5 Evaluation and regression gates

P2 adds durable regression coverage for:

- resolved discoverability semantics;
- explicit deprecation metadata;
- single canonical ownership of `sport-training-plan.json`;
- migration of active sport consumers away from the deprecated monolith;
- governance capability layering;
- complete evaluation coverage;
- zero ambiguous outputs.

Compatibility suites test explicit invocation, replacement routing, input preservation, no duplicate output ownership and safe failure behavior.

## Validation

The validated P2 sync completed successfully with:

- dependency-graph tests;
- metadata-schema tests;
- role-selection schema and routing tests;
- OpenAI agent metadata materialization;
- repository metadata generation;
- P2 architecture regression tests;
- capability-index tests;
- plugin build;
- metadata reproducibility checks;
- Obsidian universe tests;
- repository contract validation;
- all 280 evaluation suites.

Temporary P2 migration/materialization code is not part of the intended steady state. The normal `sync-generated-metadata.yml` configuration is restored after materialization.

## Deferred to P3

P2 deliberately does not mass-classify existing public specialist skills as `advanced`. That requires usage- and routing-aware evidence rather than a blanket metadata rewrite.

Next architecture priorities:

1. broaden executable end-to-end workflow benchmarks outside regulated engineering;
2. add `workflow-benchmark-authoring`;
3. expand explicit typed `consumes` only where artifact-level evidence is clear;
4. progressively thin domain document wrappers onto the generic document core without losing brand/domain-specific behavior;
5. enforce branch protection and required CI checks on `main` if repository settings permit;
6. review selected public entrypoints for evidence-based promotion to `advanced` or demotion to `internal`, without hiding narrow but legitimate specialist capabilities.
