# EUROIMMUN Corporate Design Golden Reference

This document defines the reproducible Golden Reference hierarchy for `docs/corporate/euroimmun/DESIGN.md`. It is intentionally **artifact-free** in the repository: proprietary PowerPoint masters and generated business binaries are not committed. Instead, fixtures define the required source evidence, acceptance state and regression invariants.

## Mandatory two-level model

EUROIMMUN presentation verification uses two explicit Golden Reference levels.

### Level 1 — Shared Design / Fallback Golden Reference

Level 1 verifies the shared corporate design, language, structural QA, complete rendering and source/PDF parity behavior when the proprietary PowerPoint binary master is not available.

It is mandatory for the fallback path and is allowed to pass as `template-compatible` when all findings are disclosed and the Corporate Design Gate passes.

Level 1 MUST NOT be used to claim:

- `template-derived` output;
- controlled-template or master parity;
- pixel-level parity with a proprietary PowerPoint source;
- verified inheritance of master-owned logos, footers, confidentiality fields or layout behavior.

Fixture: `tests/fixtures/euroimmun/corporate-design-24h-neuro.json`.

### Level 2 — Controlled Master Golden Reference

Level 2 is the higher-fidelity presentation certification against the **real controlled or confirmed PowerPoint binary master available at run time**.

Level 2 is mandatory whenever any of the following is true:

- a controlled or confirmed EUROIMMUN PowerPoint binary master is available in the execution context;
- the presentation is described as `template-derived`;
- controlled master/layout/theme/logo/footer behavior is claimed to be preserved;
- pixel/template parity or controlled-template verification is claimed.

Fixture: `tests/fixtures/euroimmun/corporate-design-controlled-master-level2.json`.

**Hard rule:** Level 2 MUST NOT report `PASS` without the actual binary master. A reconstructed template, copied logo, manually recreated footer, textual template specification or screenshot is not an acceptable substitute.

If the master is unavailable, Level 2 status is `NOT_RUN`. Level 1 may still pass, but the artifact remains `template-compatible` and no controlled-master parity claim is permitted.

## Level 2 source lock

Before authoring or verification, the Level 2 run MUST record:

- exact runtime source filename/identity;
- SHA-256 of the actual PPTX binary;
- template status (`approved-controlled` or `confirmed-reference-binary`);
- slide size;
- master and layout inventory;
- theme/color inventory;
- logo/footer/confidentiality geometry or stable fingerprint;
- font inventory and fallback disposition.

The currently confirmed reference deck is `260610 Innovation Topics.pptx`, SHA-256 `a85871bbe60a795436982e08bfce4a7efbc85b57471cb0c837062362844395e2`. This hash is recorded as confirmed reference provenance; it MUST NOT be silently promoted to an approved controlled master identity if a different controlled template is supplied at run time.

## Level 2 representative archetypes

A controlled-master certification run MUST exercise the master/layout grammar, not only one easy slide. The test deck MUST cover, where the source template supports them:

1. corporate cover;
2. section header;
3. standard analytical content slide;
4. two-column comparison slide;
5. figure + bullets + conclusion slide;
6. table or portfolio comparison slide;
7. visual-heavy/custom diagram slide.

If a listed archetype does not exist in the supplied master, record that fact rather than inventing it.

## Level 2 parity checks

The run MUST verify at least:

- source SHA-256 and template identity;
- slide-size parity;
- master/layout inheritance;
- theme color behavior;
- logo geometry and aspect ratio;
- footer/confidentiality geometry and content behavior;
- slide-number behavior;
- primary font family and fallback disposition;
- placeholder geometry;
- safe areas and overflow;
- complete rendering of every generated slide;
- complete rendering of the presentation PDF/print representation;
- source/PDF content and visible-layout parity;
- visual-difference assessment for master-owned regions;
- language/content checks from the Corporate Design Gate.

Master-owned regions SHOULD be compared by geometry/fingerprint and rendered visual difference rather than by manually reconstructed coordinates alone.

## Level 2 acceptance

Level 2 is `LEVEL_2_PASS` only when all of the following are true:

- derivation is `template-derived`;
- source binary and SHA-256 are recorded;
- no required master-owned element was reconstructed;
- unresolved Critical findings = `0`;
- unresolved Major findings = `0`;
- every applicable slide is rendered and inspected;
- every presentation-PDF page is rendered and inspected;
- source/PDF parity = `PASS`;
- Corporate Design Gate = `PASS`.

If any of these conditions is missing, the Level 2 result is `FAIL` or `NOT_RUN`; it is never downgraded silently to a warning.

## Supersession and rerun rules

Level 1 remains the permanent fallback regression because it proves that Skillz behaves correctly without proprietary template binaries.

A successful Level 2 run supersedes Level 1 **for controlled-presentation fidelity claims**, but does not delete Level 1.

Level 2 MUST be rerun when materially relevant source state changes, including:

- approved/confirmed master SHA-256 changes;
- master/layout/theme/logo/footer structure changes;
- the shared corporate presentation design contract changes materially;
- the rendering stack changes materially enough to affect slide output.

## Level 1 reference run — 2026-08-28

- Date: 2026-08-28
- Content window: 2026-08-27 through 2026-08-28
- Fixture: `tests/fixtures/euroimmun/corporate-design-24h-neuro.json`
- Brand profile: `euroimmun-corporate` v1.0.0
- Corporate Design Gate: `PASS`
- Unresolved Critical findings: `0`
- Unresolved Major findings: `0`

The generated test set contained:

- a 7-slide management presentation plus PDF derivative;
- a 3-page management DOCX plus PDF derivative;
- full render inspection for every slide/page;
- explicit source/parity evidence and warning disposition.

Generated binary artifacts are deliberately not committed. The fixture describes the reference run and the regression test protects the contract expected from future runs.

### Content used

The Level 1 Golden Reference intentionally uses recent, decision-relevant scientific content rather than lorem ipsum:

1. Fujirebio FDA 510(k) clearance for the Lumipulse G pTau217/beta-Amyloid 1-42 Plasma Ratio on 2025-05-16 (`K242706`).
2. Fujirebio IVDR CE milestones for Lumipulse G NfL Blood on 2026-03-17 and Lumipulse G pTau217 Plasma on 2026-05-11.
3. FDA Class II recall/product-correction evidence for affected Lumipulse pTau217/beta-Amyloid 1-42 Plasma Ratio lots as a robustness/specificity communication stress case.
4. The internal pTau217 working epitope model `P216-pT217-P218-P219-T220-R221`, explicitly presented as a hypothesis requiring assay-specific confirmation.
5. The current EUROIMMUN neurodegeneration portfolio working set around pTau217, GFAP, NfL and amyloid biomarkers.

The reference therefore exercises regulated external facts, internal hypotheses, portfolio strategy, risk language, scientific notation, tables, decision gates and management-level recommendations in one compact test.

### Presentation reference state

The confirmed proprietary PowerPoint master was not available in the execution context. The presentation was therefore correctly classified as:

- template status: `confirmed-reference`;
- derivation: `template-compatible`, not `template-derived`;
- geometry: 16:9, 13.333 x 7.5 in;
- typography: Lato runtime fallback because Hanken Grotesk was unavailable;
- render coverage: `7/7` slides;
- presentation PDF parity: `PASS`.

This remains the deliberate Level 1 fallback test. A successful Level 2 run with the real binary master becomes the higher-fidelity controlled presentation reference.

### DOCX/PDF reference state

The report used the documented Public-Reference fallback behavior:

- A4 layout;
- 20 mm left/right margins;
- Liberation Sans runtime fallback;
- render coverage: `3/3` pages;
- DOCX-to-PDF parity: `PASS`.

It MUST NOT be represented as an approved internal controlled DOCX template.

### Expected Level 1 warnings

- `PPT-FONT-001`: Hanken Grotesk unavailable; verified Lato fallback used.
- `PPT-TEMPLATE-001`: presentation is template-compatible because the binary master was unavailable.
- `DOCX-TEMPLATE-001`: report uses a public-reference working format.
- `SCOPE-001`: the run validates shared design/language/render behavior, not pixel parity with the unavailable controlled PowerPoint master.

Any future Level 1 run that silently removes these warnings without changing the underlying source state is suspicious. Any run with unresolved Critical or Major findings MUST fail.

## Repository regression

The regression test `tests/test_euroimmun_corporate_design_golden_reference.py` validates both levels:

- Level 1 remains a strict, reproducible fallback PASS;
- Level 2 cannot pass without the runtime binary master and required parity evidence;
- `template-derived` and controlled-master claims are reserved for Level 2;
- the proprietary master itself is never required to be stored in the repository.
