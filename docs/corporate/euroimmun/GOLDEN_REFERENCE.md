# EUROIMMUN Corporate Design Golden Reference

This document defines a reproducible **artifact-free Golden Reference** for `docs/corporate/euroimmun/DESIGN.md`. It records the inputs, expected evidence and acceptance state of a real content stress test without checking proprietary PowerPoint masters or generated binary business artifacts into the repository.

## Reference run

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

## Content used

The Golden Reference intentionally uses recent, decision-relevant scientific content rather than lorem ipsum:

1. Fujirebio FDA 510(k) clearance for the Lumipulse G pTau217/beta-Amyloid 1-42 Plasma Ratio on 2025-05-16 (`K242706`).
2. Fujirebio IVDR CE milestones for Lumipulse G NfL Blood on 2026-03-17 and Lumipulse G pTau217 Plasma on 2026-05-11.
3. FDA Class II recall/product-correction evidence for affected Lumipulse pTau217/beta-Amyloid 1-42 Plasma Ratio lots as a robustness/specificity communication stress case.
4. The internal pTau217 working epitope model `P216-pT217-P218-P219-T220-R221`, explicitly presented as a hypothesis requiring assay-specific confirmation.
5. The current EUROIMMUN neurodegeneration portfolio working set around pTau217, GFAP, NfL and amyloid biomarkers.

The reference therefore exercises regulated external facts, internal hypotheses, portfolio strategy, risk language, scientific notation, tables, decision gates and management-level recommendations in one compact test.

## Presentation reference state

The confirmed proprietary PowerPoint master was not available in the execution context. The presentation was therefore correctly classified as:

- template status: `confirmed-reference`;
- derivation: `template-compatible`, not `template-derived`;
- geometry: 16:9, 13.333 x 7.5 in;
- typography: Lato runtime fallback because Hanken Grotesk was unavailable;
- render coverage: `7/7` slides;
- presentation PDF parity: `PASS`.

This is a deliberate fallback test. A later run with the controlled/confirmed PowerPoint binary master should supersede it as the higher-fidelity `template-derived` presentation reference.

## DOCX/PDF reference state

The report used the documented Public-Reference fallback behavior:

- A4 layout;
- 20 mm left/right margins;
- Liberation Sans runtime fallback;
- render coverage: `3/3` pages;
- DOCX-to-PDF parity: `PASS`.

It MUST NOT be represented as an approved internal controlled DOCX template.

## Expected warnings

The Golden Reference is expected to pass with these documented non-material warnings:

- `PPT-FONT-001`: Hanken Grotesk unavailable; verified Lato fallback used.
- `PPT-TEMPLATE-001`: presentation is template-compatible because the binary master was unavailable.
- `DOCX-TEMPLATE-001`: report uses a public-reference working format.
- `SCOPE-001`: the run validates shared design/language/render behavior, not pixel parity with the unavailable controlled PowerPoint master.

Any future run that silently removes these warnings without changing the underlying source state is suspicious. Any future run with unresolved Critical or Major findings MUST fail.

## Golden-reference acceptance checks

A conforming rerun MUST prove all of the following:

- canonical `DESIGN.md` is the declared design contract;
- `euroimmun-corporate` is the declared brand profile;
- template/fallback state is explicit rather than inferred;
- externally verified facts and internal hypotheses remain distinguishable;
- all presentation slides are structurally checked and rendered;
- all DOCX/PDF pages are rendered and inspected;
- source/PDF parity is checked;
- unresolved Critical findings = `0`;
- unresolved Major findings = `0`;
- final status is exactly `Corporate Design Gate: PASS`.

The regression test `tests/test_euroimmun_corporate_design_golden_reference.py` validates these repository-level invariants.
