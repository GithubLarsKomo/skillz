# EUROIMMUN Corporate Design Golden Reference

This document defines the reproducible Golden Reference hierarchy for `docs/corporate/euroimmun/DESIGN.md`. Proprietary PowerPoint binaries are not committed; identity hashes, fixtures and QA records provide the repository evidence.

The active presentation-reference pointer is `docs/corporate/euroimmun/ACTIVE_PRESENTATION_REFERENCE.md`.

## Mandatory two-level model

### Level 1 — Shared Design / Fallback Golden Reference

Level 1 verifies shared corporate design, language, structural QA, complete rendering and source/PDF parity when the preferred binary reference is unavailable. It may pass as `template-compatible`, but MUST NOT be used to claim `template-derived`, controlled-template/master parity, or verified inheritance of master-owned regions.

Fixture: `tests/fixtures/euroimmun/corporate-design-24h-neuro.json`.

The permanent Level-1 stress set uses the 27–28 Aug 2026 neurodegeneration content and remains a reproducible fallback regression. Its presentation render coverage is `7/7`, report coverage is `3/3`, unresolved Critical/Major findings are `0`, and Corporate Design Gate is `PASS`.

### Level 2 — Controlled Master Golden Reference

Level 2 certifies presentation fidelity against a **real controlled or confirmed PowerPoint binary available at runtime**. It is mandatory when a binary master is available, `template-derived` is claimed, controlled master/layout/logo/footer preservation is claimed, or pixel/template parity is claimed.

Fixture: `tests/fixtures/euroimmun/corporate-design-controlled-master-level2.json`.

**Hard rule:** Level 2 MUST NOT report `PASS` without the actual binary master. A reconstructed template, copied logo, manually recreated footer, textual specification or screenshot is not a substitute.

Before Level-2 authoring or verification, record:

- runtime source filename/identity;
- SHA-256 of the actual PPTX binary;
- template status (`approved-controlled` or `confirmed-reference-binary`);
- slide size and master/layout inventory;
- theme/color and font inventory;
- logo/footer/confidentiality geometry or stable fingerprints.

## Preferred current Level-2 reference

The preferred current confirmed binary reference is:

- `260828 NDD Review.pptx`
- SHA-256 `349e5599ee0c1876a474057ec659244e0f37dd39d65636d2042b7eee46bab02e`
- status `confirmed-reference-binary`
- certified `LEVEL_2_PASS` on 2026-08-28
- source: 12 slides, 3 slide masters, 51 visible PowerPoint layouts, 4 themes
- primary theme: `Hanken Grotesk Light` / `Hanken Grotesk`
- active green theme accent: `#208528`

The certification record is `docs/corporate/euroimmun/GOLDEN_REFERENCE_LEVEL2_20260828.md`.

`260610 Innovation Topics.pptx`, SHA-256 `a85871bbe60a795436982e08bfce4a7efbc85b57471cb0c837062362844395e2`, is a **historical confirmed reference**. It remains valid provenance for earlier template observations but MUST NOT silently displace the preferred current reference.

## Level 2 representative archetypes

A certification run MUST exercise the available master/layout grammar, including where supported:

1. corporate cover;
2. section header;
3. standard analytical content slide;
4. two-column comparison slide;
5. figure + bullets + conclusion behavior;
6. table/portfolio comparison;
7. visual-heavy/custom diagram behavior.

If an archetype is unavailable in the runtime master, record that fact rather than inventing it.

## Level 2 required parity checks

At minimum verify:

- source SHA-256 and identity;
- slide-size parity;
- master/layout inheritance;
- theme color behavior;
- logo geometry and aspect ratio;
- footer/confidentiality geometry and behavior;
- slide-number behavior;
- font family and fallback disposition;
- placeholder geometry, safe areas and overflow;
- every generated slide rendered and inspected;
- every presentation-PDF page rendered and inspected;
- source/PDF visible-layout parity;
- visual-difference assessment for master-owned regions;
- Corporate Design Gate language/content checks.

Master-owned regions SHOULD be checked by geometry/fingerprint and rendered visual comparison, not by manually reconstructed coordinates alone.

## Level 2 acceptance

`LEVEL_2_PASS` requires:

- derivation `template-derived`;
- source binary and SHA-256 recorded;
- no required master-owned element reconstructed;
- unresolved Critical findings = `0`;
- unresolved Major findings = `0`;
- complete slide and presentation-PDF render coverage;
- PDF parity = `PASS`;
- Corporate Design Gate = `PASS`.

If any required condition is missing, Level 2 is `FAIL` or `NOT_RUN`; missing source evidence is never downgraded silently to a warning.

## Current certified run

The 2026-08-28 run using `260828 NDD Review.pptx` produced a 7-slide `template-derived` Golden Reference with `7/7` slide and `7/7` PDF-page inspection. Master-owned cover logo, lower Revvity branding, right-side cover artwork and standard content-footer regions/rule were `100%` pixel-identical in matched render comparisons. Critical = `0`, Major = `0`, PDF parity = `PASS`, Corporate Design Gate = `PASS`, final status = `LEVEL_2_PASS`.

The known warnings are preserved in the detailed record: runtime Hanken-Grotesk substitution, `confirmed-reference-binary` rather than `approved-controlled`, and PowerPoint-theme `accent1 #208528` versus cross-format corporate `forest #218529` with template precedence for template-derived elements.

## Supersession and rerun

Level 1 remains the permanent fallback regression. The successful Level 2 run supersedes Level 1 only for controlled-presentation fidelity claims tied to the certified source identity.

Rerun Level 2 when the preferred approved/confirmed source SHA-256 changes, master/layout/theme/logo/footer structure changes, the corporate presentation design contract changes materially, or the rendering stack changes materially enough to affect output.

The repository regression test `tests/test_euroimmun_corporate_design_golden_reference.py` validates these invariants.
