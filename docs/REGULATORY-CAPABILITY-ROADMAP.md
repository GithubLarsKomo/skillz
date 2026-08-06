# Regulatory Capability Roadmap

Status: proposed architecture roadmap

## Goal

Extend `skillz` for IVDR/MDCG, FDA 510(k)/De Novo, ISO 13485/QMSR and adjacent medical-device engineering without duplicating existing cross-cutting capabilities or creating terminal dead ends.

The existing broad specialists remain front-door assessment/orchestration skills:

- `eu-mdr-ivdr-regulatory-specialist`
- `fda-medical-device-ivd-regulatory-specialist`
- `medical-device-qms-iso13485`

New skills should implement narrower regulatory state transitions or produce distinct evidence artifacts. They should reuse existing context, evidence, risk, CAPA, compliance-review, document-control and handoff capabilities rather than reimplement them.

## Architecture rules

1. **One product context**: regulated product facts, intended purpose, claims, markets, specimen/analyte and lifecycle originate in `regulated-product-context`.
2. **One evidence discipline**: source acquisition and claim grounding reuse `research-to-evidence-note`; volatile regulatory facts carry `asOf` and authoritative-source provenance.
3. **One compliance-review kernel**: coverage and evidence/effectiveness assessment reuse `two-axis-compliance-review`.
4. **One risk lifecycle**: hazards, risk controls, residual risk and post-production risk updates reuse `medical-device-risk-management-iso14971`.
5. **One CAPA/RCA lifecycle**: regulatory findings may trigger `medical-device-capa` / `evidence-based-causal-investigation`; new regulatory skills do not embed a second CAPA engine.
6. **One document-control lifecycle**: controlled artifacts flow to `controlled-quality-documentation` when approval/effective-state/supersession matters.
7. **No dead-end producer**: every non-terminal output must have an existing or planned consumer. Legitimate terminal outputs must be explicitly identified as decision/evidence packages rather than inferred as pipeline artifacts.
8. **Front doors stay broad; workers stay narrow**: EU/FDA/QMS specialists decide which specialist is needed and aggregate results. Narrow skills must not independently re-run the complete market-access assessment.
9. **Regulatory authority is never simulated**: classification, clearance, approval, certification or legal determinations remain evidence-backed assessments until the required human/authority decision exists.
10. **Invocation defaults**: specialist evidence workers may be implicit when their trigger is unambiguous; pathway selection, irreversible regulatory strategy and external submission/commitment skills default to explicit invocation.

## Shared flow

```text
regulated-product-context
        |
        +--> research-to-evidence-note / MDCG-FDA source discovery
        |
        +--> EU front door -------------------------+
        |       |                                   |
        |       +--> IVDR classification            |
        |       +--> performance-evaluation stack   |
        |       +--> PMS/PMPF                       |
        |       +--> EUDAMED/UDI                    |
        |                                           |
        +--> FDA front door ------------------------+
        |       |
        |       +--> classification/product code
        |       +--> 510(k) predicate -> SE
        |       +--> De Novo -> special controls
        |       +--> Q-Sub/eSTAR/review response
        |       +--> CLIA/QMSR/inspection
        |
        +--> QMS front door
                +--> design-control traceability
                +--> design-change regulatory impact
                +--> supplier/process/measurement controls

specialist outputs
        +--> two-axis-compliance-review
        +--> medical-device-risk-management-iso14971
        +--> controlled-quality-documentation
        +--> medical-device-capa / causal investigation when triggered
        +--> decision-record for high-impact strategy decisions
```

## Wave 1 — foundation and highest-value IVD/FDA gaps

Wave 1 establishes reusable regulatory evidence contracts. These skills should be implemented before downstream submission/report builders.

| Skill | Boundary / unique state transition | Requires | Outputs | Primary consumers | Implicit invocation | Upstream inspiration |
|---|---|---|---|---|---|---|
| `regulatory-evidence-traceability` | Turns regulatory obligations and source-bound interpretations into stable requirement→evidence→status links; does not perform compliance review itself. | `regulated-product-context`, `research-to-evidence-note` | `regulatory-evidence-map.json`, `regulatory-evidence-gaps.json` | EU/FDA specialists, `two-axis-compliance-review`, document builders | true | Existing `compliance-traceability-v1`; K-Dense provenance patterns |
| `mdcg-guidance-navigator` | Finds current applicable MDCG guidance, revision/status and scope; does not decide compliance. | `regulated-product-context`, `research-to-evidence-note` | `mdcg-guidance-set.json`, `mdcg-guidance-changes.json` | EU front door and all IVDR workers | true | European Commission MDCG guidance index |
| `ivdr-device-classification` | IVD qualification/classification hypothesis under Annex VIII with explicit rule rationale and uncertainty. | `regulated-product-context`, `mdcg-guidance-navigator`, `regulatory-evidence-traceability` | `ivdr-classification-assessment.json`, `ivdr-classification-rationale.md` | EU front door, performance evaluation, conformity-route planning | false | IVDR Annex VIII; MDCG 2020-16 rev.4; MDCG 2024-11 |
| `ivdr-scientific-validity` | Converts analyte/measurand–clinical-condition evidence into a scientific-validity evidence package. | `regulated-product-context`, `research-to-evidence-note`, `regulatory-evidence-traceability` | `scientific-validity-assessment.json`, `scientific-validity-report.md` | `ivdr-performance-evaluation` | true | IVDR performance-evaluation framework; scientific literature workflows |
| `ivdr-analytical-performance` | Plans/evaluates analytical-performance characteristics without duplicating risk or generic compliance review. | `regulated-product-context`, `regulatory-evidence-traceability` | `analytical-performance-plan.json`, `analytical-performance-assessment.json`, `analytical-performance-report.md` | `ivdr-performance-evaluation`, design-change impact | true | CLSI EP-series; K-Dense analytical-method-validation patterns |
| `ivdr-clinical-performance-study` | Defines/performs regulatory planning and evidence structuring for IVD performance studies; not generic clinical study management. | `regulated-product-context`, `mdcg-guidance-navigator`, `regulatory-evidence-traceability`, `medical-device-risk-management-iso14971` | `clinical-performance-study-plan.json`, `clinical-performance-evidence.json`, `performance-study-gaps.json` | `ivdr-performance-evaluation`, PMS/PMPF | false | IVDR; ISO 20916; MDCG 2025-5, 2024-4, 2022-19/20 |
| `ivdr-performance-evaluation` | Orchestrates the three IVDR evidence pillars and identifies evidence gaps; does not redo their analyses. | `ivdr-scientific-validity`, `ivdr-analytical-performance`, `regulatory-evidence-traceability` | `ivdr-performance-evaluation.json`, `ivdr-performance-evaluation-gaps.json` | EU front door, PER builder, PMPF | true | IVDR performance evaluation |
| `fda-device-classification-product-code` | Produces evidence-backed US classification/product-code/regulation-number assessment; no pathway submission strategy beyond classification facts. | `regulated-product-context`, `research-to-evidence-note`, `regulatory-evidence-traceability` | `fda-device-classification.json`, `fda-product-code-evidence.json` | FDA front door, 510(k), De Novo, CLIA | true | FDA Classification Database / official FDA sources |
| `fda-510k-predicate-strategy` | Finds and screens legally marketed predicates/reference devices against intended use and technology; stops before SE conclusion. | `fda-device-classification-product-code`, `regulated-product-context`, `research-to-evidence-note` | `predicate-candidate-set.json`, `predicate-strategy.md` | `fda-510k-substantial-equivalence`, Q-Sub | false | FDA 510(k) databases; public FDA consultant patterns |
| `fda-510k-substantial-equivalence` | Builds explicit SE reasoning from intended use, technological characteristics and performance evidence. | `fda-510k-predicate-strategy`, `regulatory-evidence-traceability`, `medical-device-risk-management-iso14971` | `substantial-equivalence-assessment.json`, `substantial-equivalence-matrix.md`, `se-evidence-gaps.json` | eSTAR builder, Q-Sub, FDA front door | false | FDA 510(k) framework |
| `fda-de-novo-strategy` | Converts absence of suitable predicate plus risk/control evidence into a De Novo strategy hypothesis. | `fda-device-classification-product-code`, `regulated-product-context`, `medical-device-risk-management-iso14971`, `regulatory-evidence-traceability` | `de-novo-strategy.json`, `de-novo-evidence-gaps.json` | special-controls skill, Q-Sub, eSTAR builder | false | FDA De Novo pathway |
| `fda-qsub-strategy` | Converts unresolved FDA questions into a bounded Q-Sub interaction package and records requested feedback; not a generic meeting skill. | `fda-medical-device-ivd-regulatory-specialist`, `regulatory-evidence-traceability`, `decision-record` | `qsub-question-set.json`, `qsub-briefing-package.md`, `qsub-commitments.json` | 510(k), De Novo, CLIA, follow-up tracker | false | FDA Q-Submission final guidance May 2025 |
| `fda-qmsr-iso13485-gap` | Separates ISO 13485 evidence from current US QMSR-specific obligations and gaps; does not duplicate QMS process mapping. | `medical-device-qms-iso13485`, `two-axis-compliance-review`, `regulatory-evidence-traceability` | `qmsr-iso13485-delta.json`, `qmsr-gap-assessment.md` | FDA front door, inspection readiness, controlled docs | true | FDA QMSR effective 2026-02-02 |
| `design-change-regulatory-impact` | Converts a confirmed product/design change into market-specific regulatory, V&V, risk and documentation impact decisions. | `regulated-product-context`, `medical-device-risk-management-iso14971`, `two-axis-compliance-review`, `decision-record` | `design-change-impact.json`, `regulatory-change-decisions.json`, `change-verification-needs.json` | EU/FDA front doors, controlled docs, implementation planning | false | FDA change-to-510(k) reasoning; EU significant-change principles |

## Wave 2 — submission/report assembly and lifecycle closure

Wave 2 consumes Wave-1 evidence. These skills are deliberately downstream so they cannot become isolated document generators.

| Skill | Requires | Outputs | Consumer / closure | Implicit |
|---|---|---|---|---|
| `ivdr-performance-evaluation-report` | `ivdr-performance-evaluation`, `ivdr-clinical-performance-study`, `regulatory-evidence-traceability` | `performance-evaluation-report.md`, `per-traceability.json` | EU front door, controlled docs, PMPF | true |
| `ivdr-pmpf` | `ivdr-performance-evaluation`, `medical-device-risk-management-iso14971` | `pmpf-plan.json`, `pmpf-evaluation-report.md`, `pmpf-signals.json` | PMS/vigilance, PER refresh, CAPA if triggered | true |
| `ivdr-pms-vigilance` | `regulated-product-context`, `medical-device-risk-management-iso14971`, `two-axis-compliance-review` | `ivdr-pms-assessment.json`, `vigilance-decision-log.json`, `trend-signal-set.json` | PMPF/PER refresh, CAPA, controlled docs | false |
| `ivdr-class-d-conformity` | `ivdr-device-classification`, `regulatory-evidence-traceability` | `class-d-conformity-plan.json`, `class-d-external-dependencies.json` | EU front door, NB/EURL human procedures | false |
| `eudamed-udi-ivd` | `regulated-product-context`, `ivdr-device-classification`, `regulatory-evidence-traceability` | `ivd-udi-data-set.json`, `eudamed-readiness.json` | `human-procedure-wizard`, controlled docs | false |
| `fda-estar-submission-builder` | 510(k) SE or De Novo strategy plus `regulatory-evidence-traceability` | `estar-content-map.json`, `submission-readiness.json` | human submission procedure, FDA review response | false |
| `fda-de-novo-special-controls` | `fda-de-novo-strategy`, `medical-device-risk-management-iso14971`, `regulatory-evidence-traceability` | `special-controls-matrix.json`, `de-novo-risk-control-rationale.md` | eSTAR, Q-Sub, later 510(k) reference strategy | false |
| `fda-acceptance-readiness` | eSTAR map plus pathway-specific evidence | `fda-acceptance-preflight.json`, `acceptance-gaps.json` | human submission gate | true |
| `fda-additional-information-response` | submission evidence plus FDA request source | `fda-request-issue-map.json`, `fda-response-package.md`, `response-evidence-matrix.json` | controlled docs, follow-up tracker, new investigations | false |
| `fda-ivd-clia-waiver` | `fda-device-classification-product-code`, `regulated-product-context`, `medical-device-risk-management-iso14971` | `clia-waiver-strategy.json`, `flex-study-needs.json`, `clia-evidence-gaps.json` | Q-Sub/eSTAR/Dual planning | false |
| `fda-qmsr-inspection-readiness` | `fda-qmsr-iso13485-gap`, `iso13485-qms-audit`, `two-axis-compliance-review` | `qmsr-inspection-readiness.json`, `inspection-evidence-index.json` | controlled docs, CAPA, human-procedure-wizard | false |
| `fda-complaint-mdr-reportability` | complaint facts, `medical-device-risk-management-iso14971`, regulatory evidence | `mdr-reportability-assessment.json`, `complaint-regulatory-actions.json` | CAPA, PMS, human reporting procedure | false |
| `design-control-traceability` | `regulated-product-context`, `medical-device-risk-management-iso14971`, `two-axis-compliance-review` | `design-control-traceability.json`, `design-evidence-gaps.json` | QMS, design-change impact, submission builders | true |
| `iec62304-software-lifecycle` | `regulated-product-context`, `medical-device-risk-management-iso14971`, `design-control-traceability` | `software-lifecycle-assessment.json`, `software-safety-classification.json`, `software-evidence-gaps.json` | FDA/EU submission evidence, design changes | true |
| `iec62366-usability-engineering` | `regulated-product-context`, `medical-device-risk-management-iso14971`, `design-control-traceability` | `usability-engineering-assessment.json`, `use-related-risk-evidence.json` | submission evidence, risk file, design changes | true |

## Wave 3 — specialized market/lifecycle capabilities

Implement only when a concrete project needs them; each already has a route into existing or Wave-1/2 consumers.

| Skill | Primary upstream | Primary downstream / closure | Default invocation |
|---|---|---|---|
| `ivdr-companion-diagnostic` | EU front door + performance evaluation | PER, conformity strategy, authority interaction | false |
| `ivdr-in-house-device-article-5-5` | product context + QMS + evidence traceability | compliance review, controlled docs | false |
| `fda-dual-510k-clia-waiver` | SE + CLIA waiver | eSTAR/Q-Sub | false |
| `fda-breakthrough-device-assessment` | FDA classification + evidence traceability | Q-Sub/decision record | false |
| `fda-pccp-change-control` | software lifecycle + risk + design change | FDA submission/change control | false |
| `medical-device-cybersecurity-lifecycle` | risk + software lifecycle | FDA/EU evidence, PMS, CAPA | true |
| `fda-recall-corrections-removals` | complaint/PMS + risk | CAPA, human-procedure-wizard, controlled docs | false |
| `fda-registration-listing-udi` | FDA classification + product context | human-procedure-wizard | false |
| `supplier-quality-medical-device` | QMS + risk + compliance review | CAPA/SCAR, controlled docs | true |
| `process-validation-iq-oq-pq` | QMS + risk + design controls | controlled docs, change impact | true |
| `measurement-system-validation` | QMS + analytical performance | analytical evidence, controlled docs | true |
| `nonconformance-mrb-disposition` | QMS + risk | CAPA, controlled docs | true |
| `quality-record-integrity` | controlled docs + compliance review | QMSR/ISO audit readiness | true |
| `medical-device-labeling-ifu` | product context + risk + regulatory evidence | EU/FDA submission builders, controlled docs | true |
| `regulatory-claims-consistency` | product context + labeling + submission/PER evidence | design change, CAPA, controlled docs | true |

## Candidates intentionally not created as standalone skills

The following ideas are absorbed into existing skills or the roadmap above because a new top-level skill would duplicate state transitions:

- generic ISO 13485 gap analysis → `medical-device-qms-iso13485`
- generic ISO 13485 audit → `iso13485-qms-audit`
- generic CAPA / supplier CAPA engine → `medical-device-capa` plus supplier-specific evidence when needed
- generic root-cause analysis → `evidence-based-causal-investigation`
- generic risk management / FMEA → `medical-device-risk-management-iso14971`
- generic document control → `controlled-quality-documentation`
- generic management review → `qms-management-review-governance`
- generic FDA consultant / MDR specialist monoliths → retain as external inspiration only; broad scope conflicts with the repo's composable architecture
- separate `fda-510k-special-abbreviated-traditional` skill → selection belongs in the FDA front door / eSTAR planning unless repeated evidence shows a distinct workflow boundary
- separate `fda-submission-commitment-tracker` → use `decision-and-follow-up-tracker` with regulatory commitment records
- separate `fda-openfda-device-intelligence` → prefer a data/tool adapter feeding `research-to-evidence-note` and FDA specialists, not a reasoning skill

## Front-door changes when waves are implemented

### `eu-mdr-ivdr-regulatory-specialist`

Remain user-facing. Reduce detailed IVD worker logic over time and route to:

- classification → `ivdr-device-classification`
- scientific/analytical/clinical evidence → performance-evaluation stack
- performance studies → `ivdr-clinical-performance-study`
- post-market → `ivdr-pms-vigilance` / `ivdr-pmpf`
- guidance freshness → `mdcg-guidance-navigator`
- Class D / CDx / in-house only when applicable

Its output remains the **aggregated market-access assessment**, not copies of specialist evidence.

### `fda-medical-device-ivd-regulatory-specialist`

Remain user-facing. Route to:

- classification/product code → `fda-device-classification-product-code`
- 510(k) → predicate → SE → eSTAR
- De Novo → strategy → special controls → eSTAR
- unresolved authority questions → Q-Sub
- CLIA context → CLIA waiver / Dual
- QMSR → ISO13485 delta → inspection readiness

Its output remains the **pathway/readiness assessment**.

### `medical-device-qms-iso13485`

Remain QMS front door. Delegate specialized evidence generation to design-control, supplier, process-validation, measurement-system and QMSR-delta skills. Continue to own process map and QMS-level gap prioritization.

## No-dead-end acceptance test for every future regulatory skill

A candidate may enter the repository only when all are true:

1. It has a trigger not already owned by an existing skill.
2. It performs a distinct state transition or produces a distinct regulatory evidence contract.
3. Its `requires` reuse shared product/evidence/risk/QMS foundations where applicable.
4. Every non-terminal output names at least one real consumer.
5. A terminal artifact is explicitly marked as such and has a human/authority decision boundary where needed.
6. It has happy, edge and failure evaluation cases.
7. Its `agents/openai.yaml` invocation policy reflects surprise/authority risk.
8. It does not copy legal or standards text into the skill; volatile rules are resolved from current authoritative sources.
9. It cannot claim clearance, certification, classification confirmation or compliance merely because its own checks pass.
10. The broad EU/FDA/QMS front door can aggregate the result without re-performing the specialist analysis.

## External sources used for architecture inspiration

Prefer concepts and workflow patterns, not blind installation.

- European Commission MDCG guidance index, including current IVDR classification, performance-study and PMS guidance.
- FDA De Novo and eSTAR pages; De Novo eSTAR is required for most De Novo submissions since 2025-10-01.
- FDA Q-Submission final guidance (May 2025).
- FDA QMSR material; QMSR became effective 2026-02-02 and FDA moved from QSIT to Compliance Program 7382.850.
- K-Dense-AI `scientific-agent-skills`: standards-readiness, analytical-method-validation, evidence provenance and assurance-lane separation.
- `alirezarezvani/claude-skills` FDA consultant and MDR specialist: useful content inventory, but too monolithic for direct adoption.
- `a5c-ai/babysitter` IEC 62304 lifecycle skill: useful lifecycle decomposition reference.

## Recommended implementation order

Do not add all candidates at once. Implement in vertical chains so every new output has a consumer immediately:

1. `regulatory-evidence-traceability` → `mdcg-guidance-navigator` → `ivdr-device-classification`.
2. `ivdr-scientific-validity` + `ivdr-analytical-performance` → `ivdr-performance-evaluation`; then add clinical-performance-study and PER/PMPF.
3. `fda-device-classification-product-code` → `fda-510k-predicate-strategy` → `fda-510k-substantial-equivalence`.
4. `fda-de-novo-strategy` → `fda-de-novo-special-controls`.
5. `fda-qsub-strategy` and `fda-estar-submission-builder` consume both FDA pathways.
6. `fda-qmsr-iso13485-gap` → `fda-qmsr-inspection-readiness`.
7. `design-control-traceability` → `design-change-regulatory-impact` → IEC 62304 / IEC 62366 as project demand justifies.

This sequence keeps the capability graph connected throughout the expansion rather than creating a catalogue of isolated regulatory experts.
