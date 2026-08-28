# Learning Content Design System

Status: **normative default** for Skillz-generated learning artifacts derived from videos or other instructional sources.

This contract governs Landingpage-Style HTML, presentation projections, DOCX/PDF learning documents, explanatory SVGs/diagrams and generated learning imagery. It is intentionally format-spanning: the learning message and visual grammar must remain coherent even when the same content is rendered into different media.

A stricter approved project or corporate design contract has higher authority. This document fills only the remaining learning-specific decisions.

## 1. Scope

Apply when Skillz creates or materially edits:

- a video-derived learning page;
- a study guide or key-takeaway handout;
- a derived instructional SOP;
- an educational presentation;
- explanatory diagrams/SVGs;
- generated educational illustrations;
- DOCX/PDF learning artifacts.

This file does **not** grant a corporate identity, controlled-document status or permission to reuse copyrighted source imagery.

## 2. Source-of-truth hierarchy

Use, in order:

1. approved/supplied template or brand contract for the exact artifact;
2. applicable normative Corporate `DESIGN.md`;
3. confirmed project-local `DESIGN.md`;
4. this shared Learning Content `DESIGN.md`;
5. renderer defaults only for undefined technical details.

EUROIMMUN company content additionally uses `docs/corporate/euroimmun/DESIGN.md`. Its Corporate Design Gate cannot be weakened by this file.

## 3. Learning-first design principles

1. **One primary learning message per visual unit.**
2. **Meaning before decoration.** Every graphic must teach, orient or reduce cognitive load.
3. **Source traceability remains visible.** Important claims and process steps retain timestamp/source navigation.
4. **Observed, derived and recommended remain distinguishable.**
5. **Cross-format consistency beats per-format reinvention.**
6. **Progressive disclosure.** Start with mental model and key takeaways, then expose details, SOP steps and source evidence.
7. **Readable at real use size.** Never solve content density by shrinking typography below practical readability.
8. **Generated imagery is illustrative, never evidence.**

## 4. Visual hierarchy

Default hierarchy:

- title / core proposition;
- short learning objective;
- key takeaway or main relationship;
- visual explanation;
- supporting details;
- provenance/timestamp/source.

Use whitespace to separate conceptual groups. Avoid generic card grids when ordinary headings, a flow or a single strong visual would communicate better.

## 5. Color

If a project/corporate palette exists, use it.

Without one:

- use a restrained neutral base;
- one primary instructional accent;
- separate warning/error/success semantics only when needed;
- do not encode a critical distinction by hue alone;
- charts and diagrams use the minimum number of colors required;
- all derived tints/shades remain traceable in project `DESIGN.md`.

Do not invent company colors.

## 6. Typography

Typography follows the active template/brand first.

Learning-specific requirements:

- high legibility;
- strong title/section/body/caption hierarchy;
- short line lengths for web reading;
- labels remain readable at final PPTX/A4 size;
- source/timestamp text may be smaller but must remain practically readable;
- no font files are distributed with outputs unless the user explicitly owns/permits that workflow and system policy allows it.

Report prose and presentation copy are not interchangeable. Presentation text is compact; HTML/DOCX may explain more fully.

## 7. Diagram and SVG grammar

Default geometry:

- left-to-right for causal/process flows unless the content requires another direction;
- top-to-bottom for procedures when step sequence is primary;
- consistent arrow meaning;
- consistent line weight;
- limited shape vocabulary;
- direct labels preferred over distant legends;
- groups/containers only when they convey hierarchy;
- no decorative gradients, shadows or 3D effects by default;
- text remains editable/textual where feasible.

Every explanatory SVG must have:

- visual message;
- referenced content claims;
- readable labels;
- intended target surfaces;
- source/provenance entry;
- alt-text intent.

## 8. Images and illustrations

Use images when realism, spatial context, physical manipulation or conceptual metaphor genuinely improves learning.

Generated image family should define consistently:

- realism/stylization level;
- perspective/camera behavior;
- background treatment;
- lighting;
- human depiction;
- device/object precision;
- color relationship to the design system.

Avoid stock-like decorative imagery. An image should depict at least one central project/learning property.

Generated images are `illustrative-only`. They must not look like undocumented experimental results, clinical evidence, measured screenshots or real device states when they are not.

## 9. Source frames and screenshots

A source frame is different from a generated illustration.

- Keep timestamp and source provenance.
- Crop only to clarify the relevant region without changing meaning.
- Annotations must not hide relevant context.
- Prefer a newly drawn diagram when the original frame is only being used to explain an abstract process.
- Do not mass-republish frames merely to make the page visually dense.
- Rights/usage constraints remain part of final QA.

## 10. Landingpage-style HTML

Default information architecture:

`Hero -> learning objectives -> key takeaways -> mental model -> chapters/how it works -> optional procedure -> critical details/mistakes -> self-check/FAQ -> source map`

Requirements:

- responsive Wide + Narrow;
- semantic HTML;
- keyboard/focus support;
- no horizontal overflow;
- visible heading hierarchy;
- timestamp deep-links;
- printable stylesheet;
- portable/local assets where practical;
- no core-content dependency on JavaScript;
- avoid SaaS/dashboard clichés unless the content actually is a dashboard.

## 11. Presentation

Presentation rendering delegates to the template-based presentation workflow.

Learning-specific storyline default:

`why it matters -> mental model -> key concepts -> how it works -> demonstrated procedure -> critical details -> common mistakes -> takeaways`

Each slide:

- one primary message;
- one dominant visual or evidence structure;
- minimal prose;
- sources/timestamps when materially useful;
- no slide-specific restatement that contradicts the canonical learning model.

All existing presentation layout/render QA remains mandatory.

## 12. DOCX / PDF

Default:

`canonical learning model -> DOCX -> complete page render -> PDF -> complete parity render`

- DOCX is canonical editable document output.
- PDF is a verified representation, not an independently restyled artifact.
- Captions and timestamp/source references remain visible.
- Derived SOP classifications remain explicit.
- Tables/visuals must fit printable width.
- Do not shrink text to resolve overflow.
- Complete page-by-page QA is required.

## 13. Content labels

Use visible semantic labels where needed:

- **Observed** — directly shown/said in the source;
- **Derived** — reconstructed from source evidence;
- **Recommended** — external best-practice addition;
- **Open / needs validation** — insufficient source evidence.

These labels may be abbreviated visually but their meaning must remain recoverable.

## 14. Accessibility

- sufficient contrast;
- no color-only critical encoding;
- semantic heading order;
- useful alt text for material images;
- `<title>/<desc>` or equivalent for important SVGs where supported;
- readable captions;
- meaningful link text;
- layouts usable at narrow width and 200% zoom where practical;
- visual meaning should survive grayscale/print when possible.

## 15. Provenance

Every final artifact must be able to reconstruct:

- source video/document identity;
- timestamp/source map;
- content-model revision/fingerprint;
- visual provenance;
- generated vs source imagery;
- active design contract(s);
- template/corporate context;
- render/QA revision.

## 16. Cross-format gate

A package is PASS only when:

- claims/takeaways remain semantically aligned;
- numbers, units, warnings and procedure steps agree;
- observed/derived/recommended labels are not lost;
- visual captions and provenance agree;
- requested formats use the same canonical learning-model revision;
- every required HTML/slide/page render has been inspected;
- unresolved Critical/Major findings = 0.

## 17. Anti-patterns

Reject:

- transcript dump presented as learning summary;
- decorative hero image unrelated to the lesson;
- fake charts from qualitative statements;
- generated screenshots presented as real UI evidence;
- generic identical card grids for every section;
- tiny text to force content into one slide/page;
- multi-color diagrams without semantic need;
- different claims in HTML vs PPTX vs DOCX;
- corporate-looking artifacts without verified corporate authority;
- declaring a derived procedure an approved SOP.

## 18. Project DESIGN.md acceptance

A project-local `DESIGN.md` is ready when it records:

- design authority/provenance;
- target audience and learning purpose;
- active palette and typography;
- diagram/SVG grammar;
- imagery language;
- source-frame policy;
- target-format profiles;
- accessibility;
- QA gates;
- explicit local overrides.

For corporate material, the project contract must also point to the applicable corporate design contract and its acceptance gate.

## 19. Completion

Design work is complete only when all requested renderers and visual generators consume the same resolved design context and the final cross-format QA confirms the exact delivered revision.
