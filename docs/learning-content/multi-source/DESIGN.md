# Multi-Source Learning Design Contract

Status: **normative extension** to `docs/learning-content/DESIGN.md` for learning artifacts synthesized from multiple videos or instructional sources.

This file adds multi-source visual and information-design rules. A stricter project/corporate `DESIGN.md` remains higher authority.

## 1. Core principle

A multi-source artifact must make **agreement, qualification, disagreement and coverage** visually understandable without turning source count into a popularity contest.

The learner should be able to answer:

1. What is the shared core?
2. What is source-/context-specific?
3. Where do sources materially disagree?
4. Which claims are supported by one source only?
5. What remains unknown?

## 2. Information hierarchy

Default order:

`shared mental model -> consensus core -> qualified variants -> conflicts/open questions -> practical synthesis -> source map`

Do not structure the final artifact as `Video 1 summary -> Video 2 summary -> Video 3 summary` unless the user's goal is explicitly comparative review.

## 3. Source identity

Each source receives a stable short identifier such as `S1`, `S2`, `S3` plus human-readable title/creator in the source map.

Rules:

- Source IDs must remain stable across HTML/PPTX/DOCX/PDF.
- Do not encode source identity by color alone.
- Source badges may use restrained accent variations, but labels/text remain primary.
- Dependent/reused sources may be grouped visually.
- Generated visuals never receive a source badge implying evidence.

## 4. Consensus states

Use consistent semantic states across all formats:

- **Consensus** — independent relevant sources converge;
- **Qualified** — core agrees but scope/conditions differ;
- **Single source** — only one material source supports the claim;
- **Conflict** — unresolved material disagreement;
- **Open** — insufficient evidence.

Visual encoding must use label + shape/icon/pattern where practical, not hue alone.

## 5. Conflict presentation

A conflict is a first-class learning object, not a footnote to hide.

For material conflicts show:

- the disputed question;
- Position A/B/... in parallel;
- source IDs;
- scope/method/version qualifiers;
- resolution status;
- safe learner takeaway.

Never use a visual that implies a winner unless arbitration supports that conclusion.

## 6. Coverage map

For three or more sources, a coverage visualization is recommended when it materially helps orientation.

Preferred forms:

- matrix: learning objectives x sources;
- concept map with source badges;
- small multiples for source-specific extensions.

Avoid dense heatmaps without labels. Absence of coverage is not evidence against a claim.

## 7. Process and SOP variants

When sources show different procedures:

- shared steps form the common spine;
- incompatible variants branch explicitly;
- source-/condition-specific parameters stay attached to their branch;
- do not average temperatures, times, concentrations, thresholds or settings;
- unresolved critical differences receive visible warning treatment;
- a merged process diagram must not imply that all steps can be combined in one protocol.

## 8. Visual grammar

Recommended multi-source patterns:

- **Consensus spine:** central flow for common mechanism, side branches for variants;
- **Conflict matrix:** disputed dimension as rows, source positions as columns;
- **Evidence fan-in:** multiple source nodes converging on one canonical claim;
- **Coverage matrix:** source IDs across columns, learning objectives across rows;
- **Variant tree:** shared prerequisite -> branch by context/method/version.

Arrows represent logical/process relations, not mere source association.

## 9. Landingpage

Default IA extension:

`Hero/source-set summary -> learning objectives -> consensus core -> shared mental model -> source navigator -> deeper synthesis -> variants -> conflicts/open questions -> optional SOP variants -> self-check -> complete source map`

Requirements:

- source navigator can filter/locate source references without hiding the canonical synthesis;
- conflict blocks remain readable on narrow screens;
- source links use meaningful labels;
- print view preserves source IDs and conflict states.

## 10. Presentation

Default storyline:

`problem -> shared mental model -> consensus core -> deeper mechanism -> relevant variants -> conflicts/open questions -> practical synthesis -> takeaways`

Slides should not become bibliography tables. Use source IDs in compact provenance areas and reserve full citations/source map for appendix or dedicated source slide.

A conflict slide should compare positions directly rather than serially describing each video.

## 11. DOCX/PDF

- source IDs and full source registry must be recoverable;
- consensus/qualified/conflict labels survive PDF conversion;
- variant tables do not split in ways that detach conditions from values;
- conflicts may use tables only if printable width remains readable;
- complete source map and model fingerprint appear in provenance/appendix.

## 12. Accessibility

- do not use green = agreement / red = conflict as the only distinction;
- every state has textual wording;
- matrix cells require accessible text equivalents where possible;
- source badge contrast must remain sufficient;
- conflict/variant diagrams need alt-text describing the actual relationship, not merely visual appearance.

## 13. Anti-patterns

Reject:

- one color per video across an entire deck/page when source identity is not the learning point;
- majority-vote charts implying truth by bar height;
- decorative source logos as evidence strength;
- blended protocol values;
- hiding a conflict in tiny citation text;
- representing unavailable videos as analyzed;
- duplicated creator videos shown as independent corroboration;
- source-by-source summaries with no actual synthesis.

## 14. Completion gate

PASS only when:

- every consensus claim is traceable to its independent source support;
- every unresolved material conflict is visible in final outputs;
- source IDs are stable across formats;
- single-source claims are not visually elevated to consensus;
- process variants remain condition-bound;
- all requested formats share the same multi-source model fingerprint;
- base Learning Content DESIGN.md and any applicable corporate DESIGN.md also PASS.
