# EUROIMMUN De-Novo Corporate Report Master

Status: **DESIGN_APPROVED / CONTROLLED_MASTER_PENDING**

Approval date: **2026-08-28**

This record defines the approved visual baseline for the de-novo EUROIMMUN DOCX/PDF report master. It is not a substitute for controlled-template certification. The visual system is approved; the final binary master remains pending until controlled corporate assets and document-control inputs are integrated and the complete Level-2 gate is rerun.

## 1. Provenance

The design was created de novo from:

- `docs/corporate/euroimmun/DESIGN.md`;
- authoritative `euroimmun-corporate@1.0.0` color tokens;
- the established EUROIMMUN/Revvity corporate hierarchy;
- the DOCX/PDF render and parity requirements in the report workflow.

The Public-Reference DOCX was **not** promoted or treated as the source master.

The user explicitly approved the rendered v0.1 PDF visual direction on 2026-08-28. Version 0.2 preserves that visual direction and extends production behavior only.

## 2. Approved page grammar

- format: A4;
- left margin: 20 mm;
- right margin: 20 mm;
- top margin: 22 mm;
- bottom margin: 18 mm;
- cover separated from body section;
- restrained white body pages;
- thin Forest rule below body header;
- quiet operational footer;
- no decorative card-grid grammar;
- no independent PDF styling.

## 3. Approved color roles

- Forest `#218529`: primary corporate hierarchy, Heading 1, primary tables, decision accents;
- Sea `#148087`: secondary hierarchy, Heading 3 and evidence semantics;
- Orange `#FA7E33`: warning/risk only;
- neutral grays: metadata, captions, sources, borders and non-semantic surfaces.

Do not broaden the palette decoratively.

## 4. Typography hierarchy

Design-approved hierarchy:

- title: strong black display, Hanken-Grotesk-oriented;
- Heading 1: Forest;
- Heading 2: dark neutral;
- Heading 3: Sea;
- body: current implementation uses Arial-compatible office-safe text metrics;
- caption/source/metadata: smaller neutral text with preserved readability.

The final controlled Word font policy remains a governance item. No font files are stored or redistributed.

## 5. Semantic content patterns

The approved system supports:

- executive lead paragraph;
- decision callout;
- evidence callout;
- warning/risk callout;
- neutral template/control callout;
- decision-oriented management table;
- evidence-status table;
- bullet list;
- numbered sequence;
- figure/chart area with caption;
- source list;
- document-control appendix.

Semantic callouts MUST remain whole across page breaks. Table rows MUST NOT split when this would impair interpretation. Repeating table-header rows are required for multi-page tables.

## 6. Template insertion contract

The v0.2 design-approved binary uses both:

- bookmark: `REPORT_BODY_START`;
- Word content-control tag: `EI_REPORT_BODY`.

Arbitrary-position insertion is forbidden.

A renderer MAY use a versioned adapter/profile to bind content to the controlled master. The controlled master itself MUST NOT be destructively modified merely to add Skillz-specific placeholder syntax.

## 7. Approved v0.2 identities

- `EUROIMMUN_Corporate_Report_Master_v0.2.docx`
  - SHA-256: `320e1a291aaf8639f05844bb7cff24cfc42e1f8c59618bb90059d6a9861afacb`
- `EUROIMMUN_Corporate_Report_Master_v0.2.dotx`
  - SHA-256: `102254f2ee792e2660eebd67f26adda7b4ffad2ee1dcfc7821e72e1db5386215`
- `EUROIMMUN_Corporate_Report_Master_v0.2_specimen.docx`
  - SHA-256: `2e7971c067afd8d0bc36ebf2da4cc348ec4ed88b833934c9ffce9e66cbe330a6`
- `EUROIMMUN_Corporate_Report_Master_v0.2_specimen.pdf`
  - SHA-256: `e5efc95c12a05efa10483f3f15cf45b823dc88a21de643780fd265d723221276`

These hashes identify the approved design run. They do not by themselves establish `approved-controlled` status.

## 8. Render evidence

Final v0.2 verification:

- blank master DOCX: `2/2 PASS`;
- specimen DOCX: `4/4 PASS`;
- derived specimen PDF: `4/4 PASS`;
- DOCX/PDF page-count parity: `PASS`;
- visible-layout parity: `PASS`;
- clipping/overlap: none;
- broken tables: none;
- split semantic callouts: none after final correction;
- missing glyphs: none observed;
- unresolved Critical: `0`;
- unresolved Major: `0`.

A blue inherited `Title` style border and a page-splitting callout were detected during v0.2 development, corrected, and the complete artifact set was rerendered before this record was established.

## 9. Remaining blockers before controlled Level 2

The design MUST remain `CONTROLLED_MASTER_PENDING` until all of the following are resolved:

1. approved EUROIMMUN / From Revvity logo asset is embedded without reconstruction;
2. authoritative classification, legal/entity and document-control wording/fields are supplied;
3. final controlled Word typography policy is locked;
4. final binary master SHA-256 is recorded after those changes;
5. Section/page geometry, Named Styles, headers/footers, fields/content controls, assets and fonts are fingerprinted;
6. complete DOCX render inspection is repeated;
7. complete DOCX -> PDF render/parity inspection is repeated;
8. unresolved Critical = 0;
9. unresolved Major = 0;
10. Corporate Design Gate = `PASS`;
11. report Golden Reference = `LEVEL_2_PASS`.

## 10. Status semantics

`DESIGN_APPROVED` means the visual grammar may be treated as normative for continuing the de-novo master development.

It does **not** mean:

- `approved-controlled`;
- `template-derived` from an approved internal Word master;
- `LEVEL_2_PASS`;
- approved legal/document-control wording;
- approved logo asset provenance.

That distinction is mandatory until the controlled-master blockers are closed.
