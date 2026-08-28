# EUROIMMUN Active DOCX/PDF Report Reference

Status: **normative pointer** for the preferred current EUROIMMUN report template used by `euroimmun-docx-report-renderer` and `euroimmun-pdf-report-renderer`.

## Current state

As of 2026-08-28, **no internally approved or otherwise confirmed EUROIMMUN DOCX/DOTX binary template has been registered as the preferred Level-2 report reference**.

A de-novo Word/PDF report design has, however, been visually approved and render-verified. This creates a binding **design baseline** without falsely promoting the current binary to an `approved-controlled` Level-2 template.

Therefore:

- preferred current Level-2 binary reference: `NONE_REGISTERED`;
- current Level-2 certification record: `NONE`;
- approved visual design baseline: `EUROIMMUN Corporate Report Master v0.2`;
- design-baseline lifecycle: `DESIGN_APPROVED / CONTROLLED_MASTER_PENDING`;
- DOCX Level 2: `NOT_RUN` until the final controlled binary is completed and verified;
- PDF Level 2: `NOT_RUN` unless its source DOCX has Level-2 PASS;
- bundled Public-Reference template remains the Level-1 fallback only;
- Public-Reference output may pass the Corporate Design Gate for its declared fallback scope, but is never `template-derived`, `approved-controlled`, or a certified internal corporate document.

## Approved de-novo visual baseline

Normative design record: `docs/corporate/euroimmun/DE_NOVO_REPORT_MASTER.md`

Approved baseline properties:

- provenance: `de-novo`;
- visual approval date: `2026-08-28`;
- page format: A4;
- margins: 20 mm left/right, 22 mm top, 18 mm bottom;
- primary accent: Forest `#218529`;
- secondary semantic accent: Sea `#148087`;
- safe bookmark: `REPORT_BODY_START`;
- Word content-control tag: `EI_REPORT_BODY`;
- full master DOCX render: `2/2 PASS`;
- full specimen DOCX render: `4/4 PASS`;
- full specimen PDF render: `4/4 PASS`;
- DOCX/PDF visible-layout parity: `PASS`;
- Critical findings: `0`;
- Major findings: `0`.

Current v0.2 binary identities from the approved design run:

- DOCX master SHA-256: `320e1a291aaf8639f05844bb7cff24cfc42e1f8c59618bb90059d6a9861afacb`;
- DOTX master SHA-256: `102254f2ee792e2660eebd67f26adda7b4ffad2ee1dcfc7821e72e1db5386215`;
- DOCX specimen SHA-256: `2e7971c067afd8d0bc36ebf2da4cc348ec4ed88b833934c9ffce9e66cbe330a6`;
- PDF specimen SHA-256: `e5efc95c12a05efa10483f3f15cf45b823dc88a21de643780fd265d723221276`.

These hashes identify the design-approved v0.2 artifacts. They **do not constitute Level-2 controlled-template certification**.

Remaining blockers before promotion to `approved-controlled` / `LEVEL_2_PASS`:

1. approved EUROIMMUN / From Revvity logo asset embedded without reconstruction;
2. authoritative classification, entity and document-control wording/fields;
3. final controlled Word typography policy;
4. final binary SHA lock after those controlled changes;
5. repeat of all Level-2 structural, render and DOCX -> PDF parity checks.

## Current Level-1 fallback

- representation: `skills/euroimmun-docx-report-renderer/assets/euroimmun-report-template.docx.b64`
- generator: `skills/euroimmun-docx-report-renderer/scripts/build_template.py`
- theme metadata: `skills/euroimmun-docx-report-renderer/assets/report-theme.json`
- status: `public-reference-fallback`
- derivation claim allowed: `template-compatible`
- Level-2 claim allowed: **no**

The Level-1 fallback is retained for operational compatibility. It MUST NOT override the approved de-novo visual grammar when the v0.2 design baseline is being developed or reproduced.

## Promotion criteria for a preferred Level-2 reference

A DOCX/DOTX may become the preferred current Level-2 report reference only after all of the following are recorded and verified:

1. exact runtime/source filename;
2. SHA-256 of the unmodified binary;
3. template status: preferably `approved-controlled`; `confirmed-reference-binary` is acceptable only when approval evidence is unavailable and that limitation is explicit;
4. document/page geometry and Section inventory;
5. Named Style inventory and hierarchy;
6. Header/Footer relationships and controlled content by Section;
7. logo/image identities or stable fingerprints in controlled regions;
8. fields, page numbering and relevant document properties/content controls;
9. font inventory and fallback disposition;
10. a safe content insertion adapter/profile that does not require destructive modification of the template;
11. complete DOCX render inspection;
12. generated DOCX -> PDF full-page parity inspection;
13. unresolved Critical = 0;
14. unresolved Major = 0;
15. `Corporate Design Gate: PASS`;
16. report Golden Reference = `LEVEL_2_PASS`.

The binary template itself does not need to be committed to Skillz. For confidential/proprietary templates, Skillz should retain only non-confidential identity, profile, fingerprints and QA evidence.

## Runtime precedence

1. task-specific `approved-controlled` DOCX/DOTX supplied for the current document;
2. preferred current Level-2 binary reference registered here, once one exists;
3. approved de-novo report design baseline when explicitly generating or completing the future controlled master;
4. another explicitly supplied confirmed Corporate DOCX/DOTX with documented provenance;
5. Public-Reference Level-1 fallback.

A lower-priority source must never silently replace a higher-priority one.

## Supersession

When a Level-2 reference is certified, update this file with its filename, SHA-256, status, certification date and record path. Retain the v0.2 approved design record as provenance even after the controlled master supersedes it operationally.

Rerun Level 2 when the source SHA-256, Section/page geometry, styles, Header/Footer/logo/field structure, template adapter, corporate design contract, or rendering stack changes materially.
