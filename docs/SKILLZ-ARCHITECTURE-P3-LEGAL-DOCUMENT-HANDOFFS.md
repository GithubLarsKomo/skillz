# Skillz Architecture Consolidation — P3 Legal and Document Handoffs

Status: implemented on `feat/skillz-architecture-p3-legal-document-handoffs`.

## Goal

Continue the evidence-led typed-artifact migration where the normative contracts already identify a clear canonical source and a machine-readable downstream state.

This tranche deliberately avoids flattening branded DOCX renderers into the generic document core. The EUROIMMUN DOCX renderer still owns real Corporate template identity, adapter, block, image/table and Level-2 parity logic and therefore remains a domain renderer.

## EUROIMMUN DOCX -> PDF source contract

`euroimmun-pdf-report-renderer` now explicitly consumes only:

- `euroimmun-report.docx`

This encodes the existing architecture rule that the PDF is a distribution representation of the canonical DOCX and must not re-author content or layout.

The branded DOCX renderer remains the canonical producer of `euroimmun-report.docx` and retains Corporate Design / controlled-template ownership.

## Contract negotiation state spine

`legal-negotiation-strategy` now explicitly consumes:

- `client-strategy.json`
- `legal-decision-boundaries.json`
- `legal-risk-register.json`
- `commercial-exposure-analysis.json`
- `legal-risk-decision-handoff.json`

This makes the negotiation model depend on explicit client authority and risk state rather than every output of its required skills.

## Contract redline state spine

`legal-redline-review-loop` now explicitly consumes:

- `contract-review.json`
- `contract-issue-list.json`
- `negotiation-positions.json`

The loop therefore carries forward issue lineage and machine-readable negotiation positions without treating `contract-review.md` or `negotiation-playbook.md` as hidden state dependencies.

## Legal final gate state spine

`legal-matter-final-gate` now explicitly consumes:

- `legal-risk-register.json`
- `legal-risk-decision-handoff.json`
- `privilege-routing.json`
- `counsel-scope.json`

This reflects the gate's normative checks for residual-risk authorization, privilege/confidentiality routing and external-counsel/authority requirements.

## Canonical contract matter state machine

`contract-matter-workflow` now consumes the explicit work products required to maintain the versioned contract Matter state:

- agreement deal model / clause coverage / specialist routes;
- contract review, issue list and risk handoff;
- contract draft, drafting report and open points;
- negotiation positions;
- redline delta and negotiation state;
- final legal gate and final open points.

Human-oriented review/playbook/redline narrative files are deliberately not included when the corresponding structured state exists. This keeps the orchestrator state-oriented and avoids broad legacy coupling.

## Regression protection

Added:

- `tests/test_architecture_consolidation_p3_legal_document_handoffs.py`

Extended:

- `.github/workflows/artifact-contract-regression.yml`

The regression verifies:

1. exact `consumes` lists;
2. one canonical producer for every consumed artifact;
3. generated consumer edges are present and unambiguous;
4. EUROIMMUN PDF has exactly the canonical DOCX source contract;
5. Contract Matter prefers structured state artifacts over redundant human views;
6. Redline Review consumes issue lineage and machine negotiation positions;
7. repository-wide ambiguous outputs remain zero.

## Validation

The one-time materialization run passed:

- dependency graph tests;
- metadata schema validation;
- role-selection contracts;
- legal/document handoff migration;
- repository metadata generation;
- legal/document handoff regression;
- prior typed-artifact regression;
- cross-domain workflow E2E;
- OpenAI plugin build;
- metadata reproducibility;
- Obsidian generation;
- repository contract validation;
- all **281** skill evaluation suites.

The temporary Python migration helper was removed and the normal metadata-sync workflow was restored to the canonical `main` configuration.

## Health after this tranche

- skills: **281**
- user-facing entrypoints: **231**
- evaluation coverage: **281/281**
- executed evaluation suites: **PASS**
- ambiguous outputs: **0**
- outputs without inferred consumers: **274**

The increase of the final metric is intentional. Explicit `consumes` removed false broad-inference edges. It is a review queue, not a KPI to minimize.

## Document-core conclusion

The generic core (`document-template-profiler -> document-layout-qa -> document-render-verifier -> template-document-workflow`) is already internally typed.

Do not replace `euroimmun-docx-report-renderer` merely to reduce skill count. It still owns domain-specific Corporate template and parity behavior that the generic workflow intentionally does not own.

Future document consolidation should target orchestration duplication or simple derived-delivery adapters, not brand-specific rendering semantics.

## Remaining P3 candidates

1. higher-level person-research orchestration contracts;
2. selected frontend context/shaping/review artifact handoffs;
3. evidence-based discoverability review of explicit/advanced entrypoints;
4. only then selective domain-document-wrapper thinning where no ownership is lost;
5. branch protection / required-CI policy once the final gate set is stable.
