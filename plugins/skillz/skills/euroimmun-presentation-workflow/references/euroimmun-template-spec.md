# EUROIMMUN PowerPoint Template Specification

Current preferred reference derived from user-supplied `260828 NDD Review.pptx` and certified on 2026-08-28. Historical observations from `260610 Innovation Topics.pptx` remain documented where still useful.

## Normative status

This file is a **format-specific observed template specification**, not the company-wide design authority. For every EUROIMMUN corporate presentation, `docs/corporate/euroimmun/DESIGN.md` is the mandatory shared design/QA contract, `docs/corporate/euroimmun/ACTIVE_PRESENTATION_REFERENCE.md` identifies the preferred current binary reference, and `docs/corporate/euroimmun/GOLDEN_REFERENCE.md` governs Level-1/Level-2 certification.

When a verified PowerPoint binary reference is available, its master/theme/layout values are authoritative for template-owned elements. For `template-derived` work, template-owned theme values take precedence over cross-format palette tokens for roles the template explicitly defines.

## Preferred current reference identity

- Source: `260828 NDD Review.pptx`
- SHA-256: `349e5599ee0c1876a474057ec659244e0f37dd39d65636d2042b7eee46bab02e`
- Status: `confirmed-reference-binary`
- Golden Reference: `LEVEL_2_PASS` on 2026-08-28
- Slide size: 16:9 widescreen, 13.333 × 7.5 in
- Slides in source: 12
- Slide masters: 3
- Visible PowerPoint layouts: 51
- Themes: 4
- Primary theme major font: `Hanken Grotesk Light`
- Primary theme minor font: `Hanken Grotesk`

Primary active theme colors observed in the preferred reference:

| Theme role | Hex |
|---|---|
| dk1 | `#000000` |
| lt1 | `#FFFFFF` |
| dk2 | `#7F7F7F` |
| lt2 | `#FFEB0F` |
| accent1 | `#208528` |
| accent2 | `#7F03B0` |
| accent3 | `#148087` |
| accent4 | `#C94D00` |
| accent5 | `#9E306E` |
| accent6 | `#000000` |

`accent1 #208528` is therefore the correct green for new elements that intentionally follow this PowerPoint theme. The cross-format corporate palette still contains forest `#218529`; do not normalize template-owned PowerPoint elements from `#208528` to `#218529`.

## Historical reference

`260610 Innovation Topics.pptx`, SHA-256 `a85871bbe60a795436982e08bfce4a7efbc85b57471cb0c837062362844395e2`, is retained as a **historical confirmed reference**. It was the basis of the first template characterization and remains useful for compatible layout observations. It is no longer the preferred current binary reference.

Approximate rendered greens previously observed around `#158A38` to `#179B43` remain non-normative observations only and MUST NOT override either the active PowerPoint theme or the authoritative cross-format corporate palette.

## Brand behavior confirmed

- EUROIMMUN/Revvity identity is predominantly light/white and restrained on standard content slides.
- Cover uses EUROIMMUN branding in the upper-left area, Revvity branding in the lower-left area and master-owned visual artwork on the right.
- Content slides use master-owned Revvity/footer elements and a fine lower rule.
- Proprietary/confidentiality text is master/layout controlled and must be inherited rather than recreated.
- Section headers use high-contrast Revvity-family color fields and large minimal titles.
- Corporate greens and Revvity-family purple, teal, orange, fuchsia and yellow are theme-defined; use selectively rather than as a rainbow palette.

## Core layout archetypes

The preferred reference supports a broad layout inventory. The Level-2 Golden Reference exercised these native layouts successfully:

- `Title Slide 05` — corporate cover
- `Section Header 03` — chapter divider
- `Title + 2 Column Content` — paired comparison
- `Titel und Inhalt` — standard title/content slide
- `Charts: Title and Content 02` — chart/analytical content
- `Content 02 Euroimmun` — EUROIMMUN content layout
- `Title Only` — flexible analytical/custom visual slide

Historical/compatible layouts including `Section Header 04`, `1_Abbildung mit Stichpunkten und Fazit`, `1_Leere Folie` and `Blank` may still be used when present in the supplied binary template.

## Typography hierarchy

Use the active template hierarchy first. Typical ranges remain:

- cover title: approximately 28–36 pt;
- section title: approximately 32–45 pt;
- standard slide title: approximately 20–24 pt;
- body: approximately 12–16 pt;
- table/body-small: approximately 9–12 pt when necessary;
- sources/footnotes: approximately 7–9 pt.

Do not shrink text repeatedly to force fit. Split, shorten or redesign instead.

## Composition rules

1. Keep standard content slides predominantly white/light.
2. Prefer one clear visual anchor and one primary message per slide.
3. Use table/header/chart colors from the active PowerPoint theme when the template defines them.
4. Avoid dense decorative card systems foreign to the master grammar.
5. Use section-color slides sparingly as narrative separators.
6. Retain generous margins and master safe areas.
7. Use photographs/scientific visuals only when they carry evidence or context.
8. Use charts with restrained palette and direct labels where practical.
9. Put citations/sources in a consistent lower band above the corporate footer.
10. Keep logos, footer, Proprietary/Confidential labels and slide numbers master-controlled wherever possible.

## Level-2 parity evidence

The 2026-08-28 certification using `260828 NDD Review.pptx` produced a `template-derived` 7-slide Golden Reference and achieved:

- full PPTX render coverage: `7/7`;
- full presentation-PDF coverage: `7/7`;
- source/PDF parity: `PASS`;
- unresolved Critical findings: `0`;
- unresolved Major findings: `0`;
- master-owned cover logo region: `100% exact` pixel comparison;
- master-owned cover Revvity region: `100% exact`;
- master-owned cover artwork region: `100% exact`;
- master-owned standard content footer regions/rule: `100% exact`.

This certification establishes `260828 NDD Review.pptx` as the preferred current confirmed binary reference. It does not promote it to `approved-controlled` without separate approval evidence.

## Management-deck adaptation

For Board/R&D/portfolio presentations:

- use statement-led titles;
- fewer words per slide than technical reports;
- prefer portfolio matrices, timelines, staged investment diagrams and decision structures;
- explicitly label `Decision`, `Risk`, `Gate` and `Assumption` when useful;
- distinguish modeled assumptions from externally confirmed facts;
- end with a specific requested decision/next gate when appropriate.

## Confidentiality / repository rule

The reference decks contain proprietary and confidential business/scientific content. Therefore:

- do not store the binary source decks in Skillz;
- do not copy scientific/business content from a reference deck into unrelated presentations;
- persist only non-confidential design grammar, identity hashes and QA evidence;
- when the verified preferred binary is available at runtime, use it directly as source of truth for template-owned behavior;
- always apply `docs/corporate/euroimmun/DESIGN.md` and the relevant Golden Reference level before final delivery.
