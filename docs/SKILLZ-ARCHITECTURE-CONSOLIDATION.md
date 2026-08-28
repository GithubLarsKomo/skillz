# Skillz Architecture Consolidation

Status: active architecture wave  
Branch: `feat/skillz-architecture-consolidation`  
Baseline: `main` at start of wave  
Date: 2026-08-28

## Objective

Consolidate `GithubLarsKomo/skillz` from a rapidly growing skill library into a governed capability platform with clear ownership, typed artifact handoffs, deliberate discovery surfaces, explicit lifecycle migration, stronger evaluation coverage and reusable delivery layers.

The wave MUST preserve useful domain specialization. Consolidation is justified only when it removes duplicated ownership, duplicated orchestration, legacy parallel paths or infrastructure duplication without erasing meaningful lifecycle or specialist boundaries.

## Architectural invariants

1. A domain specialist keeps ownership of specialist reasoning; wrappers and orchestrators do not duplicate it.
2. An artifact has one canonical producer wherever possible.
3. Orchestrators may expose or reference worker artifacts, but should declare as owned outputs only artifacts they actually create.
4. `requires` expresses hard skill prerequisites; `consumes` should increasingly express concrete artifact dependencies.
5. User-facing discovery is reserved for deliberate task-level entrypoints. Technical workers, renderers and compatibility paths should not inflate the default surface.
6. Generated metadata remains generated. Canonical `SKILL.md`, schemas, benchmark definitions and generators are edited; generated projections are regenerated.
7. Existing specialist boundaries in Legal, FDA, IVDR, QMS, Sport and Learning are not merged merely because their names or outputs are adjacent.
8. Deprecated paths remain reproducible until their documented compatibility obligation ends.

## Baseline health findings

At the start of this wave the canonical capability-health projection reports:

- 270 skills;
- 229 user-facing entrypoints;
- 245 evaluation suites;
- 25 skills without evaluation suites;
- 15 user-facing entrypoints without evaluation suites;
- 6 ambiguous outputs;
- 261 outputs without inferred consumers.

The six ambiguous outputs are concentrated in orchestration/wrapper ownership:

- `learning-mission.json` — `learning-mission`, `teach`;
- `learning-next-step.json` — `learning-next-step`, `teach`;
- `learning-state.json` — `learning-state`, `teach`;
- `multi-source-learning-model.json` — `multi-source-learning-synthesis`, `youtube-playlist-learning-workflow`;
- `presentation-qa.md` — `template-presentation-workflow`, `euroimmun-presentation-workflow`;
- `presentation-template-profile.json` — `presentation-template-profiler`, `template-presentation-workflow`, `euroimmun-presentation-workflow`.

These are treated as ownership defects, not as evidence that the underlying skills should be merged.

# P0 — capability health and ownership

## P0.1 Eliminate ambiguous output ownership

### Canonical producer rule

| Artifact | Canonical producer | Wrappers/orchestrators that must stop claiming ownership |
|---|---|---|
| `learning-mission.json` | `learning-mission` | `teach` |
| `learning-next-step.json` | `learning-next-step` | `teach` |
| `learning-state.json` | `learning-state` | `teach` |
| `multi-source-learning-model.json` | `multi-source-learning-synthesis` | `youtube-playlist-learning-workflow` |
| `presentation-template-profile.json` | `presentation-template-profiler` | `template-presentation-workflow`, `euroimmun-presentation-workflow` |
| `presentation-qa.md` | `template-presentation-workflow` | `euroimmun-presentation-workflow` |

Affected canonical paths:

- `skills/teach/SKILL.md`
- `skills/youtube-playlist-learning-workflow/SKILL.md`
- `skills/template-presentation-workflow/SKILL.md`
- `skills/euroimmun-presentation-workflow/SKILL.md`

Required generated projections after regeneration:

- `docs/skill-dependency-graph.json`
- `docs/SKILL-DEPENDENCIES.md`
- `docs/skill-capability-index.json`
- `docs/CAPABILITY-HEALTH.md`
- `obsidian/`
- plugin/distribution mirrors as defined by the repository metadata pipeline.

Acceptance criteria:

- ambiguous output count = 0;
- worker artifacts remain available through the workflow but retain one canonical producer;
- no domain worker is deleted;
- existing workflow semantics remain intact.

## P0.2 Evaluation debt gate

Target the currently unevaluated Presentation/Learning/YouTube cluster first.

Priority paths include:

- `skills/presentation-template-profiler/`
- `skills/presentation-language-rewriter/`
- `skills/presentation-layout-qa/`
- `skills/presentation-render-verifier/`
- `skills/template-presentation-workflow/`
- `skills/euroimmun-presentation-workflow/`
- `skills/youtube-video-ingestion/`
- `skills/multimodal-learning-analysis/`
- `skills/learning-summary-synthesis/`
- `skills/procedure-sop-extractor/`
- `skills/learning-source-arbitration/`
- `skills/multi-source-learning-synthesis/`
- `skills/learning-visual-planner/`
- `skills/learning-content-design-system/`
- `skills/learning-svg-generator/`
- `skills/learning-image-generator/`
- `skills/learning-landingpage-renderer/`
- `skills/learning-document-delivery/`
- `skills/learning-artifact-qa/`
- `skills/youtube-learning-workflow/`
- `skills/youtube-playlist-learning-workflow/`
- `skills/course-concept-graph/`
- `skills/learning-path-planner/`
- `skills/learning-activity-generator/`
- `skills/youtube-course-builder-workflow/`

Desired policy:

- `stable + userFacing + evaluation:none` => CI error;
- `candidate + userFacing + evaluation:none` => CI warning initially, later error;
- `internal + evaluation:none` => warning unless explicitly exempted;
- `deprecated` => compatibility suite only is sufficient.

Acceptance criteria:

- every stable user-facing entrypoint has a deterministic suite;
- repository health distinguishes “all executed suites passed” from “evaluation coverage complete”.

## P0.3 Deprecate the legacy direct sport PDF entrypoint

Canonical path:

- `skills/dr-komorowski-sport-report-renderer/SKILL.md`

Target metadata:

```yaml
status: deprecated
replacedBy: dr-komorowski-sport-pdf-report-renderer
```

The compatibility renderer should no longer be a normal user-facing discovery entrypoint. It remains invokable explicitly for historical ReportLab reproduction.

Replacement path:

`dr-komorowski-sport-docx-report-renderer -> dr-komorowski-sport-pdf-report-renderer`

Acceptance criteria:

- `/skills` does not promote the legacy renderer;
- `/skills all` can still expose it as deprecated/internal compatibility capability;
- historical rendering behavior is preserved.

## P0.4 Remove stale hard-coded inventory from curated universe documentation

Canonical curated document:

- `docs/SKILL-UNIVERSE.md`

The document may remain curated, but hard-coded counts such as historic 108/90 inventory must not compete with the generated capability index.

Replace static inventory claims with a pointer to:

- `docs/skill-capability-index.json`;
- `docs/CAPABILITY-HEALTH.md`.

Acceptance criteria:

- no stale inventory number remains in a manually curated architecture document;
- generated Obsidian universe remains authoritative for current counts.

# P1 — typed composition and shared delivery

## P1.1 Expand explicit artifact consumption

Migrate high-value dependency spines from broad inferred `requires` consumption to explicit `consumes` contracts.

Priority spine:

```text
loaded source
  -> source-to-context
  -> source-context.json
  -> research/evidence or multimodal analysis
  -> normalized domain/content model
  -> delivery
  -> QA evidence
```

First consumers to review:

- `research-to-evidence-note`;
- `multimodal-learning-analysis`;
- `structured-knowledge-artifact`;
- `document-generation-forensics`;
- selected legal/regulatory research consumers.

Acceptance criteria:

- consumers declare the smallest artifact set they actually need;
- hard skill dependencies remain only where execution/semantic dependency is real;
- no ambiguous artifact is accepted by `consumes`.

## P1.2 Connect `source-to-context` as the common source normalization primitive

Current issue: `source-to-context` is architecturally useful but has no downstream consumers.

Target:

```text
Web / PDF / DOCX / Connector / OCR / YouTube / audio/video adapters
                            -> source-to-context
                            -> source-context.json
```

YouTube-specific timecodes, transcript indices and frame anchors remain extensions but should be representable from the generic source context.

Acceptance criteria:

- provenance survives normalization;
- source-specific adapters do not duplicate research synthesis;
- generic research and learning paths can consume the same normalized context.

## P1.3 Add `learning-delivery-workflow`

Purpose: remove repeated rendering and QA orchestration from single-video, playlist and course-building workflows.

Target flow:

```text
learning-content-model.json
multi-source-learning-model.json
course-learning-model.json
          -> learning-delivery-workflow
          -> HTML | PPTX | DOCX | PDF
          -> cross-format QA
```

Expected dependencies:

- `learning-content-design-system`;
- `learning-visual-planner`;
- `learning-svg-generator`;
- `learning-image-generator`;
- `learning-landingpage-renderer`;
- `learning-document-delivery`;
- `template-presentation-workflow`;
- `learning-artifact-qa`.

After extraction, the YouTube orchestrators should focus on content-model production rather than delivery implementation.

## P1.4 Add generic template document workflow

New proposed capabilities:

- `document-template-profiler`;
- `document-layout-qa`;
- `document-render-verifier`;
- `template-document-workflow`.

Target architecture:

```text
structured content + template/brand context
              -> document-template-profiler
              -> template-document-workflow
              -> DOCX
              -> PDF
              -> structural + visual parity QA
```

Migrate domain wrappers progressively:

- EUROIMMUN corporate reports;
- Dr.-Komorowski sport reports;
- person profile reports;
- learning documents.

Corporate wrappers retain brand-specific DESIGN.md, template identity, terminology and governance only.

# P2 — portfolio governance and discovery

## P2.1 Add `skill-portfolio-audit`

Inputs:

- capability index;
- dependency graph;
- output contracts;
- evaluations;
- workflows/benchmarks;
- lifecycle metadata.

Outputs:

- `skill-portfolio-health.json`;
- `skill-consolidation-plan.md`;
- `skill-gap-analysis.json`.

Checks:

- overlapping entrypoints;
- redundant orchestration;
- monoliths that duplicate newer composed stacks;
- low-value leaf workers exposed as public entrypoints;
- orphan primitives;
- ambiguous ownership;
- evaluation debt;
- missing complementary capabilities;
- lifecycle inconsistencies.

## P2.2 Add `skill-evaluation-suite-authoring`

Generate or update evaluation fixtures from:

- trigger/description;
- declared inputs/outputs;
- invariants;
- negative boundaries;
- completion criteria;
- compatibility obligations.

Must not self-approve generated suites without deterministic validation.

## P2.3 Add `skill-lifecycle-migration`

Support:

- rename;
- merge;
- split;
- supersede;
- deprecate;
- compatibility façade;
- consumer migration.

Outputs should include affected dependents, artifact migration plan and required compatibility tests.

## P2.4 Add role/domain/discovery metadata

Do not replace existing discovery categories. Add orthogonal metadata after schema/design review.

Proposed dimensions:

```yaml
domain:
  - learning
  - engineering
  - legal
  - medical-device
  - sport
  - knowledge
role: context|adapter|analyzer|planner|transformer|orchestrator|renderer|verifier|router|governance
discoverability: primary|advanced|internal
```

Compatibility with existing `userFacing` must be defined before rollout.

## P2.5 Reduce default entrypoint inflation

Default `/skills` should primarily expose task-level facades and major specialist entrypoints.

Candidates for advanced/internal discovery review include:

- technical renderers;
- profilers;
- layout/render QA workers;
- image/SVG generators;
- compatibility renderers;
- internal adapters.

Do not hide a specialist merely because it is narrow; hide it when direct user invocation adds little compared with its parent orchestrator.

# P3 — workflow coverage and platform hardening

## P3.1 Add end-to-end workflow benchmarks

Current workflow/benchmark coverage is strongest in regulated engineering. Add executable E2E benchmark sequences for:

- engineering lifecycle;
- software performance optimization;
- frontend/design workflow;
- contract lifecycle;
- executive legal/compliance governance;
- person research/report delivery;
- template presentation production;
- YouTube single-video learner;
- YouTube playlist synthesis;
- YouTube course builder;
- sport athlete-management loop;
- thought-to-concept flow;
- purchase decision workflow.

## P3.2 Add `workflow-benchmark-authoring`

The skill should turn an approved workflow architecture into deterministic E2E sequence definitions with required artifacts, expected gates and negative-path assertions.

Generated Obsidian workflow views should derive from executable benchmark/workflow definitions instead of parallel hand curation where possible.

## P3.3 Repository branch protection / CI gate

Recommended required checks for `main`:

- repository metadata `--check`;
- metadata schemas;
- skill frontmatter schema;
- dependency-cycle validation;
- ambiguous-output health gate;
- evaluation suites;
- capability/discovery query tests;
- plugin/distribution build/sync checks.

Branch protection is a repository setting and is not simulated by skill metadata.

# Domain-specific consolidation decisions

## Keep separate

The following boundaries are intentionally valuable and should not be merged without new evidence:

- FDA vs IVDR regulatory specialists;
- individual postmarket/vigilance lifecycle capabilities;
- legal specialist domains;
- `sport-adaptation-analysis` vs `sport-training-adaptation-engine`;
- YouTube single-video vs playlist vs course-building content semantics;
- structural presentation QA vs visual render verification;
- research evidence synthesis vs durable memory governance.

## Consolidate/migrate

### Sport programming

`sport-training-programming` is a legacy-style broad planner compared with the newer composed stack. Migrate it toward a compatibility façade over:

- `sport-goal-performance-model`;
- `sport-season-periodization`;
- `sport-mesocycle-planning`;
- `sport-microcycle-planning`;
- `sport-endurance-programming`;
- `sport-strength-power-programming`.

Do not remove it until report/workflow consumers are migrated and compatibility is evaluated.

### Learning delivery

Extract common rendering/QA orchestration; keep content semantics in the existing single-video, playlist and course workflows.

### Document delivery

Extract generic template/document parity logic from corporate/domain-specific renderers; preserve brand adapters.

# Execution order

1. Resolve output ownership ambiguity.
2. Deprecate legacy direct sport renderer from default discovery.
3. Remove stale curated inventory claims.
4. Regenerate repository metadata and verify health.
5. Add missing evaluation suites for the newest Presentation/Learning cluster.
6. Introduce explicit consumption on the highest-value artifact spines.
7. Connect `source-to-context`.
8. Extract `learning-delivery-workflow`.
9. Build generic template-document workflow.
10. Migrate legacy sport programming façade.
11. Add portfolio/lifecycle/evaluation authoring capabilities.
12. Expand E2E workflow benchmarks.
13. Tighten discovery and repository protection.

# Verification commands

After each structural tranche, run the repository-native validation pipeline rather than hand-editing generated files:

```bash
python scripts/generate_repository_metadata.py
python scripts/generate_repository_metadata.py --check
python scripts/validate_metadata_schemas.py
```

Then execute the repository's test/evaluation commands defined by current CI and confirm:

- no dependency cycles;
- no unknown `requires` or `consumes`;
- ambiguous output count meets the tranche target;
- generated capability index and Obsidian projection are current;
- plugin/distribution mirrors are synchronized;
- evaluation results remain green.

# Completion definition

The consolidation wave is complete when Skillz has:

- zero accidental ambiguous artifact producers;
- complete evaluation coverage for stable public entrypoints;
- no stale manually maintained inventory counts;
- legacy paths explicitly deprecated and removed from default discovery;
- a reusable source-context spine;
- a shared Learning delivery layer;
- a generic template-document delivery layer;
- explicit portfolio/lifecycle governance capabilities;
- materially broader E2E workflow benchmark coverage;
- a smaller and more intentional default discovery surface without loss of specialist capability.
