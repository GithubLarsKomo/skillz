# Skillz Architecture Consolidation — P3 Typed Artifact Contracts

Status: implemented on `feat/skillz-architecture-p3-artifact-contracts`.

## Goal

Replace selected broad legacy consumer inference from `requires` with explicit, evidence-backed `consumes` contracts for high-value workflow spines.

This tranche deliberately does **not** try to minimize the health metric `Outputs without inferred consumers`. Terminal outputs are valid, and explicit `consumes` can correctly reveal that some outputs previously looked consumed only because every output of a required skill was inferred as an input.

## Contract semantics

The dependency graph treats an explicit `consumes` declaration as authoritative for artifact consumption. Legacy inference from all outputs of a required skill remains only for consumers without an explicit `consumes` list.

Therefore a migration is safe only when the actual consumed artifacts are known from the normative workflow contract. Partial or speculative lists are not acceptable.

## Migrated spines

### Sport planning spine

Explicit artifact handoffs now include:

- `athlete-profile.json` -> `sport-goal-performance-model`
- `sport-performance-model.json` -> `sport-season-periodization`
- `sport-season-plan.json` -> `sport-mesocycle-planning`
- `sport-mesocycle.json` -> `sport-microcycle-planning`
- athlete/performance/meso/micro artifacts -> `sport-strength-power-programming`
- athlete/diagnostics/performance/meso/micro artifacts -> `sport-endurance-programming`
- all canonical planning artifacts plus strength/endurance prescriptions -> `sport-training-plan-workflow`

This keeps `sport-training-plan.json` as the single canonical one-shot plan output while making its upstream data spine explicit.

### Sport report delivery spine

Explicit handoffs now include:

- `dr-komorowski-sport-report.docx` -> `dr-komorowski-sport-pdf-report-renderer`
- `sport-diagnostics.json`, `sport-training-plan.json`, canonical DOCX and derived PDF -> `sport-diagnostics-training-report-workflow`

The PDF renderer therefore consumes exactly the canonical DOCX instead of inheriting all conceptual outputs merely because the DOCX renderer is required.

### Presentation QA spine

Explicit handoffs now include:

- `presentation-template-profile.json` -> `presentation-layout-qa`
- `presentation-layout-qa.json` -> `presentation-render-verifier`
- template profile, revised presentation text/language report, structural QA artifacts and render QA artifacts -> `template-presentation-workflow`

A key regression assertion verifies that `presentation-layout-qa` no longer receives the human-readable `presentation-template-profile.md` through broad `requires` inference.

### Person report delivery

`person-profile-document-delivery` now explicitly consumes:

- `final-revised-text`
- `precision-writing-report.json`

This matches its normative requirement for a finalized, fidelity-verified report rather than every output reachable from `precision-writing-revision`.

## Regression protection

Added:

- `tests/test_architecture_consolidation_p3_artifact_contracts.py`
- `.github/workflows/artifact-contract-regression.yml`

The regression verifies:

1. exact evidence-backed `consumes` declarations;
2. every consumed artifact has exactly one canonical producer;
3. generated capability-index consumer edges contain the intended consumer;
4. explicit `consumes` removes known false broad-inference edges;
5. no ambiguous output producer is introduced.

The dedicated CI workflow also verifies generated repository metadata before running the contract regression.

## Validation

The materialization run passed:

- dependency graph tests,
- metadata schema validation,
- role-selection contracts,
- typed-consumes migration,
- repository metadata generation,
- typed artifact-contract regression,
- cross-domain workflow benchmark regression,
- OpenAI plugin build,
- metadata reproducibility,
- Obsidian generation,
- repository contract validation,
- all **281** skill evaluation suites.

The one-time Python migration helper was removed after materialization and the normal metadata-sync workflow was restored to the canonical `main` configuration.

## Health after migration

- skills: **281**
- user-facing entrypoints: **231**
- evaluation coverage: **281/281**
- executed evaluations: **PASS**
- ambiguous outputs: **0**
- outputs without inferred consumers: **271**

The last number increased from 270 to 271. This is expected and desirable in this case: explicit contracts removed false inferred consumers while adding the real consumer edges. The metric is a review queue, not a target to minimize.

## Next candidates

Further typed-consumes migration should be evidence-led. Priority candidates are:

1. contract matter-state handoffs;
2. person-research orchestration above the already explicit dossier -> report boundary;
3. generic document core handoffs where concrete artifacts are already named;
4. selected frontend design context/shaping/review handoffs;
5. regulated-engineering chains only where current explicit contracts are incomplete.

Do not mass-add every output of every `requires` skill to `consumes`; that would merely reproduce the legacy inference in a more verbose form.
