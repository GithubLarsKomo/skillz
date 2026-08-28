# EUROIMMUN Active DOCX/PDF Report Reference

Status: **normative pointer** for the preferred current EUROIMMUN report template used by `euroimmun-docx-report-renderer` and `euroimmun-pdf-report-renderer`.

## Current state

As of 2026-08-28, **no internally approved or otherwise confirmed EUROIMMUN DOCX/DOTX binary template has been registered as the preferred Level-2 report reference**.

Therefore:

- preferred current Level-2 binary reference: `NONE_REGISTERED`;
- current Level-2 certification record: `NONE`;
- DOCX Level 2: `NOT_RUN` unless an eligible runtime binary is explicitly supplied and verified;
- PDF Level 2: `NOT_RUN` unless its source DOCX has Level-2 PASS;
- bundled Public-Reference template remains the Level-1 fallback only;
- Public-Reference output may pass the Corporate Design Gate for its declared fallback scope, but is never `template-derived`, `approved-controlled`, or a certified internal corporate document.

## Current Level-1 fallback

- representation: `skills/euroimmun-docx-report-renderer/assets/euroimmun-report-template.docx.b64`
- generator: `skills/euroimmun-docx-report-renderer/scripts/build_template.py`
- theme metadata: `skills/euroimmun-docx-report-renderer/assets/report-theme.json`
- status: `public-reference-fallback`
- derivation claim allowed: `template-compatible`
- Level-2 claim allowed: **no**

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
3. another explicitly supplied confirmed Corporate DOCX/DOTX with documented provenance;
4. Public-Reference Level-1 fallback.

A lower-priority source must never silently replace a higher-priority one.

## Supersession

When a Level-2 reference is certified, update this file with its filename, SHA-256, status, certification date and record path. Retain prior identities as historical references rather than deleting provenance.

Rerun Level 2 when the source SHA-256, Section/page geometry, styles, Header/Footer/logo/field structure, template adapter, corporate design contract, or rendering stack changes materially.
