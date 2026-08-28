# EUROIMMUN Corporate Design Golden Reference

This document defines the reproducible Golden Reference hierarchy for `docs/corporate/euroimmun/DESIGN.md`. Proprietary corporate binaries are not committed; identity hashes, fixtures and QA records provide repository evidence.

Active pointers:

- presentation: `docs/corporate/euroimmun/ACTIVE_PRESENTATION_REFERENCE.md`
- DOCX/PDF reports: `docs/corporate/euroimmun/ACTIVE_REPORT_REFERENCE.md`

## Mandatory two-level model

### Level 1 — Shared Design / Fallback Golden Reference

Level 1 verifies shared corporate design, language, structural QA, complete rendering and source/PDF parity when the preferred binary reference is unavailable. It may pass as `template-compatible`, but MUST NOT be used to claim `template-derived`, controlled-template/master parity, or verified inheritance of controlled binary-template regions.

Fixture: `tests/fixtures/euroimmun/corporate-design-24h-neuro.json`.

The permanent Level-1 stress set uses the 27–28 Aug 2026 neurodegeneration content and remains a reproducible fallback regression. Its presentation render coverage is `7/7`, report coverage is `3/3`, unresolved Critical/Major findings are `0`, and Corporate Design Gate is `PASS`.

For DOCX/PDF, the bundled Public-Reference template is explicitly Level 1 only.

### Level 2 — Real Binary Template Golden Reference

For presentations, this retains the established **Level 2 — Controlled Master Golden Reference** semantics while extending the same rigor to reports.

Level 2 certifies fidelity against a **real controlled or confirmed corporate binary available at runtime**. It is artifact-family specific:

- Presentation Level 2: real PPTX binary master/reference.
- Report Level 2: real DOCX/DOTX binary template/reference.

Level 2 is mandatory when a qualifying binary is available, `template-derived` is claimed, controlled master/template preservation is claimed, or pixel/template parity is claimed.

Presentation fixture: `tests/fixtures/euroimmun/corporate-design-controlled-master-level2.json`.
Report fixture: `tests/fixtures/euroimmun/corporate-design-controlled-report-level2.json`.

**Hard rule:** Presentation Level 2 MUST NOT report `PASS` without the actual binary master; Report Level 2 MUST NOT report `PASS` without the actual DOCX/DOTX binary template. A reconstructed template, copied logo, manually recreated footer, textual specification, Base64 Public-Reference fallback or screenshot is not a substitute.

## Presentation Level 2

### Source lock

Before Presentation-Level-2 authoring or verification, record:

- runtime source filename/identity;
- SHA-256 of the actual PPTX binary;
- template status (`approved-controlled` or `confirmed-reference-binary`);
- slide size and master/layout inventory;
- theme/color and font inventory;
- logo geometry and aspect ratio, footer/confidentiality geometry, or stable fingerprints.

### Preferred current presentation reference

- `260828 NDD Review.pptx`
- SHA-256 `349e5599ee0c1876a474057ec659244e0f37dd39d65636d2042b7eee46bab02e`
- status `confirmed-reference-binary`
- certified `LEVEL_2_PASS` on 2026-08-28
- source: 12 slides, 3 slide masters, 51 visible PowerPoint layouts, 4 themes
- primary theme: `Hanken Grotesk Light` / `Hanken Grotesk`
- active green theme accent: `#208528`

Certification record: `docs/corporate/euroimmun/GOLDEN_REFERENCE_LEVEL2_20260828.md`.

`260610 Innovation Topics.pptx`, SHA-256 `a85871bbe60a795436982e08bfce4a7efbc85b57471cb0c837062362844395e2`, is a **historical confirmed reference** and MUST NOT silently displace the preferred current reference.

### Presentation representative archetypes

A certification run MUST exercise the available master/layout grammar, including where supported:

1. corporate cover;
2. section header;
3. standard analytical content slide;
4. two-column comparison slide;
5. figure + bullets + conclusion behavior;
6. table/portfolio comparison;
7. visual-heavy/custom diagram behavior.

### Presentation required parity checks

At minimum verify source SHA-256 and identity, slide-size parity, master/layout inheritance, theme color behavior, logo/footer/confidentiality behavior, slide numbers, font/fallback disposition, placeholder geometry/safe areas/overflow, every slide render, every presentation-PDF page render, source/PDF visible-layout parity, master-owned visual difference assessment, and Corporate Design Gate language/content checks.

### Presentation Level-2 acceptance

`LEVEL_2_PASS` requires derivation `template-derived`, source binary/SHA recorded, no required master-owned element reconstructed, Critical = 0, Major = 0, complete slide/PDF coverage, PDF parity = `PASS`, and Corporate Design Gate = `PASS`.

The 2026-08-28 certified run using `260828 NDD Review.pptx` achieved these conditions with `7/7` slide and `7/7` PDF inspection and 100% pixel-identical matched master-owned regions.

## DOCX/PDF Report Level 2

### Current state

As of 2026-08-28, **no eligible internally approved or confirmed EUROIMMUN DOCX/DOTX binary has been registered as the preferred report Level-2 reference**. Therefore Report Level 2 is currently `NOT_RUN`.

The existing Public-Reference Word template remains Level 1. This is intentional and prevents a public-style working format from being mislabeled as a controlled internal corporate template.

Authoritative pointer: `docs/corporate/euroimmun/ACTIVE_REPORT_REFERENCE.md`.

### Report source lock

Before DOCX-Level-2 authoring or verification, record:

- exact source filename;
- SHA-256 of the unmodified DOCX/DOTX binary;
- template status (`approved-controlled` preferred; otherwise explicit `confirmed-reference-binary`);
- Sections, page size, margins and orientation inventory;
- Named Styles and hierarchy;
- Header/Footer relationships by Section;
- logos/images in controlled regions and stable identities/fingerprints;
- fields, page numbering, document properties, bookmarks/content controls where relevant;
- font inventory/fallback disposition;
- safe body insertion adapter/profile.

The binary template itself need not be stored in Skillz.

### Report adapter rule

A real internal Word template MUST NOT be modified merely to add Skillz-specific `{{...}}` placeholders. Binary source and template adapter are separate concerns. The adapter must identify a safe content insertion point and map body elements to existing approved styles/structures without reconstructing controlled template regions.

If no safe adapter exists, Level 2 is `NOT_RUN` or `FAIL`.

### DOCX required parity checks

At minimum verify:

- source binary identity and SHA-256;
- Section/page-geometry parity;
- style inheritance and hierarchy;
- Header/Footer/logo/field preservation;
- page numbering behavior;
- fonts/fallbacks;
- body insertion does not overwrite controlled regions;
- tables/images/captions/callouts remain inside printable geometry;
- every generated DOCX page rendered and inspected;
- controlled-region geometry/fingerprints/render comparison;
- no required controlled template element reconstructed;
- Corporate Design Gate language/content checks.

### DOCX Level-2 acceptance

DOCX `LEVEL_2_PASS` requires:

- real DOCX/DOTX binary available;
- source SHA-256/status recorded;
- derivation `template-derived`;
- valid adapter/profile;
- no required controlled template element reconstructed;
- Sections/Page Setup and controlled regions preserved;
- complete DOCX page render coverage;
- unresolved Critical = `0`;
- unresolved Major = `0`;
- Corporate Design Gate = `PASS`.

Missing binary evidence is never downgraded to a warning.

### PDF Level-2 inheritance and parity

PDF is never independently promoted. It inherits the DOCX report level.

PDF `LEVEL_2_PASS` additionally requires:

- source DOCX already has Report `LEVEL_2_PASS`;
- final source-DOCX SHA-256 recorded;
- PDF generated from that exact DOCX revision;
- every PDF page rendered and inspected;
- page count/content order parity;
- Header/Footer/logo/field/Page-Setup visible behavior preserved;
- no PDF-specific repair/reconstruction;
- DOCX/PDF source parity = `PASS`;
- Critical = `0`, Major = `0`;
- Corporate Design Gate = `PASS`.

If DOCX Level 2 is `NOT_RUN`, PDF Level 2 MUST also be `NOT_RUN`.

## Supersession and rerun

Level 1 remains the permanent fallback regression for each artifact family. A Level-2 PASS supersedes Level 1 only for fidelity claims tied to the certified source identity.

Rerun Presentation Level 2 when the approved/confirmed PPTX SHA, master/layout/theme/logo/footer structure, presentation design contract, or relevant rendering stack changes materially.

Rerun Report Level 2 when the approved/confirmed DOCX/DOTX SHA, Section/page geometry, styles, Header/Footer/logo/field structure, adapter/profile, report design contract, or relevant rendering/conversion stack changes materially.

The repository regression tests `tests/test_euroimmun_corporate_design_golden_reference.py` and `tests/test_euroimmun_docx_pdf_level2_reference.py` validate these invariants.
