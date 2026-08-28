# EUROIMMUN Corporate Content Design System

Status: **normative** for Skillz-generated EUROIMMUN company presentations, DOCX reports and their PDF derivatives.

This file is the shared design contract for corporate content. It plays the same role for company artifacts that an authoritative `DESIGN.md` plays for an Impeccable product: it fixes visual identity, format behavior, language expectations, allowed variation and the acceptance gate. Format-specific skills may add stricter rules, but they MUST NOT weaken this contract.

## 1. Scope and mandatory use

Apply this contract whenever Skillz creates, materially edits or re-renders:

- an EUROIMMUN corporate presentation or a presentation using the confirmed EUROIMMUN/Revvity PowerPoint template;
- an EUROIMMUN DOCX report, management paper, technical/scientific report or comparable company document;
- a PDF derived from one of those DOCX artifacts;
- a corporate artifact that reuses EUROIMMUN brand assets, corporate colors, master layouts, headers, footers or confidentiality markings.

For standalone Revvity corporate material, use a verified Revvity source template when available. Do not infer a complete Revvity design system from EUROIMMUN co-branding alone.

**Mandatory gate:** an applicable artifact MUST NOT be described or delivered as final/verified until the Corporate Design Gate in section 13 has passed. If this file is unavailable, the corporate workflow stops instead of silently improvising a design.

## 2. Normative language

- **MUST / MUST NOT**: hard acceptance rule.
- **SHOULD / SHOULD NOT**: default rule; an exception requires a documented reason.
- **MAY**: permitted option within the contract.

## 3. Source-of-truth hierarchy

Use the following precedence. Never blend contradictory sources by intuition.

1. **Current approved/supplied controlled template for the specific artifact.** Preserve its master, theme, logo system, header/footer, legal fields and controlled styles.
2. **Authoritative EUROIMMUN corporate palette:** `skills/frontend-design-system-context/references/brand-profiles/euroimmun.json`, profile `euroimmun-corporate`, currently v1.0.0, derived from the user-supplied `EI_color_palette_RGB.ase` without changing RGB values.
3. **This `DESIGN.md`** for shared content, composition, typography, imagery, accessibility and verification rules.
4. **Confirmed format references:**
   - PowerPoint: `skills/euroimmun-presentation-workflow/references/euroimmun-template-spec.md`, derived from confirmed deck `260610 Innovation Topics.pptx` (SHA-256 `a85871bbe60a795436982e08bfce4a7efbc85b57471cb0c837062362844395e2`).
   - DOCX fallback: the versioned Public-Reference template/theme in `skills/euroimmun-docx-report-renderer/assets/`.
5. **Generic renderer defaults** only where none of the sources above defines the property.

If an approved controlled template conflicts with the corporate palette, do not restyle existing controlled template elements. Preserve them, use the template/theme for additions on that artifact and record the discrepancy in QA. Never invent a third variant.

## 4. Brand identity and asset integrity

- Preserve the EUROIMMUN/From Revvity logo relationship exactly as defined by the active template or approved asset.
- Do not redraw, stretch, recolor, crop, re-typeset or reconstruct the logo from text.
- Do not replace a supplied controlled logo/header/footer with a Public-Reference asset.
- Keep logo clear space and visual hierarchy consistent with the source template.
- Do not claim that a Public-Reference fallback is an internally approved corporate template.
- Do not package or redistribute font files as part of Skillz outputs.
- Do not infer document IDs, approvals, authors, confidentiality classes or legal status.

### Authoritative corporate colors

The exact RGB tokens from `euroimmun-corporate` are:

| Token | Hex |
|---|---|
| black | `#000000` |
| white | `#FFFFFF` |
| forest | `#218529` |
| clover | `#73C054` |
| orchid | `#7F03B0` |
| purple | `#B985D9` |
| sea | `#148087` |
| turquoise | `#3DD4CC` |
| flame | `#C94D00` |
| orange | `#FA7E33` |
| fuchsia | `#9E306E` |
| pink | `#FF8ECF` |
| yellow | `#FFEB0F` |

Rules:

- Newly created brand-colored elements MUST use exact template/theme values or exact authoritative tokens, not visually estimated substitutes.
- Approximate colors observed in a reference deck are descriptive evidence only and MUST NOT override the authoritative palette.
- Derived tints/shades MAY be used for accessible surfaces or data visualization only when their parent token and derivation are traceable in QA.
- Do not use the entire palette on one page/slide. Use restrained semantic roles and let the active template determine the dominant accent family.
- Text/background combinations MUST remain legible. Prefer the foreground mapping in the authoritative brand profile and verify contrast for small text and data labels.

## 5. Typography

Typography follows the active approved template first.

### Presentations

When the confirmed EUROIMMUN PowerPoint template is used:

- primary family: `Hanken Grotesk`;
- strong hierarchy: `Hanken Grotesk SemiBold`;
- legacy/imported Arial or Lato is not a reason to introduce it as a new primary style;
- fallback fonts are allowed only when the intended font is technically unavailable and the rendered result is re-verified.

Reference hierarchy:

- cover title: approximately 28–36 pt;
- section title: approximately 32–45 pt;
- standard slide title: approximately 20–24 pt;
- body: approximately 12–16 pt;
- table/small body: approximately 9–12 pt when necessary;
- sources/footnotes: approximately 7–9 pt.

Do not solve density by shrinking text below readable size. Split, shorten or redesign the slide first.

### DOCX / PDF

- Use named styles and typography from the approved DOCX template.
- The bundled Public-Reference template may use its documented Arial/Aptos/Liberation Sans fallback chain; this is a fallback implementation, not a universal corporate-font rule.
- Heading levels MUST be visually and semantically consistent.
- Body, captions, footnotes and table text MUST remain readable after PDF conversion and at 100% page view.
- Font substitution that changes line breaks, pagination or hierarchy is a QA finding and requires re-rendering.

## 6. Content and language design

Language quality is part of design acceptance.

- Preserve facts, numbers, claims, evidence levels, uncertainty and management decisions.
- German and English MUST be optimized independently and idiomatically; do not translate word-for-word when a native business/scientific formulation is clearer.
- Avoid generic LLM phrasing, repetitive framing, inflated adjectives and unnecessary meta-language.
- Maintain terminology consistently across title, body, charts, tables, notes and captions.
- Distinguish confirmed facts, modeled assumptions, risks, recommendations and decisions visually and linguistically.

### Presentation language

Use presentation-specific rewriting (`presentation-language-rewriter` in the presentation workflow): concise, scannable and element-aware. Report prose MUST NOT simply be pasted onto slides. For management decks, prefer statement-led titles that communicate the slide's conclusion.

### Report language

Reports use professional continuous prose with explicit reasoning, evidence and qualification. Apply the appropriate report/precision writing revision before rendering when content is editable. If the user requires verbatim preservation, do not rewrite the text; record that language QA was limited to layout-safe corrections.

## 7. Presentation composition contract

Default canvas: 16:9 widescreen, 13.333 × 7.5 in, when using the confirmed template.

- Reuse native master layouts and placeholders before creating custom geometry.
- Content slides SHOULD remain predominantly white/light and restrained.
- Each slide MUST have one primary message and one clear visual anchor.
- Section-header color fields are narrative punctuation, not decoration.
- Keep generous margins; do not fill every available area.
- Prefer diagrams, charts, timelines, portfolio matrices, stage gates and decision structures over long prose.
- Tables are for genuine comparison; reduce them to decision-relevant rows/columns.
- Sources belong in a consistent lower source band above the corporate footer.
- Footer, confidentiality and slide number SHOULD remain master-controlled.
- For executive/management decks, the decision, recommendation or key implication MUST be understandable without reading a companion report.

### Presentation anti-patterns

Do not:

- create decorative card grids foreign to the template grammar;
- use rainbow charts or unrelated accent colors;
- place multiple independent messages on one slide;
- reduce font size repeatedly to force content into a box;
- introduce decorative stock photography without informational value;
- flatten editable charts/tables/diagrams to screenshots unless the source itself is raster and editability is impossible or explicitly undesired.

## 8. DOCX composition contract

- Use A4 and the page geometry of the active approved template. The Public-Reference fallback uses approximately 20 mm side margins and its defined header/footer geometry.
- Preserve corporate header/footer, legal/entity information, document metadata fields and classification behavior from the chosen template.
- Use named paragraph/table styles rather than ad-hoc formatting wherever practical.
- Keep heading hierarchy stable; avoid orphaned headings and isolated single lines where the renderer allows control.
- Tables MUST fit the printable width. Prefer wrapping, column rebalancing, logical splitting or landscape only when justified; never make text unreadably small.
- Images MUST preserve aspect ratio, remain sharp at intended size and include captions/source/provenance when required.
- Callouts are semantic (`info`, `warning`, `decision`, `neutral`), not decorative containers.
- Page breaks SHOULD follow document logic; accidental blank pages, clipped footers and split visual elements are defects.

## 9. PDF contract

PDF is a verified distribution representation, not an independent design surface.

`Report-Spec -> approved/fallback EUROIMMUN DOCX template -> canonical DOCX -> PDF`

- Do not independently restyle or repair the PDF.
- Fix conversion/reflow problems in the source DOCX/template and regenerate.
- The PDF MUST retain the source artifact's template status, classification and content order.
- Page count, visible content, logo/header/footer, tables, images and pagination MUST be checked for parity with the canonical source.

For presentation PDFs, export from the final PPTX and verify the PDF/render separately from the editable deck.

## 10. Charts, tables, scientific visuals and imagery

- Every visual MUST support a message, evidence item, decision or orientation task.
- Use the smallest palette that communicates the distinction.
- Prefer direct labels over legends when this improves comprehension.
- Encode critical distinctions by more than hue where feasible (label, line style, marker, pattern or annotation).
- Axis scales, units, denominators, cohorts, time points and uncertainty MUST be explicit where materially relevant.
- Do not distort scientific images, assay outputs, microscopy, plots or product screenshots for decoration.
- Images and externally sourced figures require provenance; confidential/internal figures must be distinguished from public sources.
- Generated illustrations MUST NOT be presented as experimental/scientific evidence.

## 11. Confidentiality, provenance and governance

Before finalization verify:

- correct company/entity and template status;
- correct confidentiality/classification wording;
- no invented approval, signature, document ID or author;
- sources/citations are retained where required;
- internal/proprietary information is not copied from a reference deck merely because it was used as a design source;
- template/reference identity and fallback status are recorded in QA.

## 12. Accessibility and robustness

- Ensure sufficient contrast for body text, table text, chart labels and callouts.
- Do not use color as the sole carrier of a critical meaning.
- Use meaningful reading order and semantic headings in DOCX where tooling permits.
- Add alternative text for material images/figures when the output workflow supports it and the description can be factual.
- Avoid tiny footnotes that are technically present but practically unreadable.
- Keep key content inside printable/safe areas.
- Missing glyphs, unsupported symbols and visibly disruptive font substitution are hard defects.

## 13. Corporate Design Gate

The gate is mandatory for every applicable final artifact.

### Gate A — Design-source lock

Record and verify:

- artifact type: `pptx | docx | pdf`;
- active approved/source template and its identity if available;
- template status: `approved-controlled | confirmed-reference | public-reference-fallback`;
- corporate brand profile ID/version;
- language and target audience;
- confidentiality/classification source.

**FAIL** if no valid design source can be established or the workflow silently substitutes a different template.

### Gate B — Structural design QA

Verify before rendering:

- correct page/slide size and master/template use;
- logo/header/footer integrity;
- corporate color/token integrity;
- typography hierarchy and minimum readability;
- alignment, margins, safe areas and grid consistency;
- no text-box overflow, shape clipping or off-canvas objects;
- table width/row behavior;
- image aspect ratio/resolution;
- chart labels, units and visual semantics;
- metadata/classification consistency.

Presentation workflows MUST use `presentation-layout-qa` for the dedicated structural checks.

### Gate C — Language/content QA

Verify:

- language is idiomatic for `de` or `en` and suitable for the artifact type;
- presentation copy is presentation-specific rather than report prose;
- terminology, values and units are consistent;
- facts, assumptions, recommendations, risks and decisions are not accidentally conflated;
- design editing did not alter material claims or evidence.

### Gate D — Full render QA

A structural inspection is not enough.

**PPTX:** render every slide, visually inspect every slide, export PDF/print representation, render/inspect that output too.

**DOCX:** render the complete document to page images (or equivalent faithful page rendering) and inspect every page at 100% for clipping, overlaps, bad page breaks, tables, images, headers/footers and glyphs.

**PDF:** render every page and compare visible layout/content with the canonical DOCX or PPTX source.

After any material correction, repeat the affected structural checks and render again. A previous render does not validate a modified artifact.

### Gate E — Severity and disposition

Use these severities:

- **Critical:** wrong template/brand, missing or altered mandatory logo/footer/classification, missing content, unreadable/clipped content, broken render, materially altered claim/data, unverified final artifact.
- **Major:** layout inconsistency that harms comprehension, poor table/chart readability, significant font substitution/reflow, inconsistent terminology, incorrect color role or hierarchy.
- **Warning:** non-material visual deviation, documented fallback, minor stylistic inconsistency that does not impair use.

Final status is **PASS** only when:

- unresolved Critical findings = 0;
- unresolved Major findings = 0;
- every applicable slide/page has been rendered and inspected;
- any Warning is documented with rationale;
- the final output is the same revision that passed the render check.

### Gate F — QA evidence

The workflow MUST retain or report enough evidence to reconstruct the gate:

- `design_contract`: `docs/corporate/euroimmun/DESIGN.md`;
- design/template source and status;
- brand profile ID/version;
- font/fallback information when relevant;
- structural checks performed;
- render coverage (`checked/total` pages or slides);
- PDF/source parity result where applicable;
- findings by severity and disposition;
- final `Corporate Design Gate: PASS | FAIL`.

For presentations, include this evidence in `presentation-qa.md`. DOCX/PDF workflows MAY keep the detailed QA artifact internal unless requested, but MUST communicate the final gate result and MUST NOT call an unchecked artifact final.

## 14. Forbidden shortcuts

A corporate artifact is not verified when any of the following occurred:

- guessed or eye-matched brand colors were used although authoritative values were available;
- a new corporate design was invented instead of using the active template;
- text was shrunk until it technically fit;
- a single screenshot or first page was inspected instead of the full artifact;
- PDF conversion was assumed to preserve layout without checking it;
- a corrected artifact was delivered without re-rendering;
- a Public-Reference fallback was described as an approved internal template;
- content from a confidential reference artifact leaked into unrelated output;
- design QA was claimed without actual structural and visual verification.

## 15. Change control

This file is the canonical shared policy. Format-specific implementation details belong in their skills/reference specs, but changes that alter company-wide palette usage, brand hierarchy, verification requirements or shared typography/content principles MUST be made here first.

A format-specific skill MAY be stricter. It MUST NOT silently weaken this contract.

When an updated approved corporate template or brand guideline conflicts materially with this file, record the new provenance, update this contract and then update downstream skills. Until that update is deliberate, do not normalize the discrepancy by guesswork.

## 16. Completion rule

Corporate content work is complete only when the requested artifact is content-correct, template-correct, linguistically appropriate for its medium, visually coherent, fully rendered and inspected, and the **Corporate Design Gate reports PASS**.