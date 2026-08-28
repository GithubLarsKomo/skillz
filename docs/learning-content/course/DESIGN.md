# Course Learning Design System

Status: **normative extension** of `docs/learning-content/DESIGN.md` for modular courses and learning paths.

This contract governs course maps, module navigation, prerequisite visualization, exercises, knowledge checks and cross-format course projections. Stricter project/corporate design contracts remain authoritative.

## 1. Design hierarchy

1. approved target template / corporate DESIGN.md;
2. project DESIGN.md;
3. `docs/learning-content/DESIGN.md`;
4. this Course DESIGN extension;
5. renderer defaults.

This file adds course-specific semantics and must not weaken corporate or learning-content gates.

## 2. Core visual objects

A course package should use a consistent family of:

- **Course Map** — modules and progression;
- **Prerequisite Graph** — only real prerequisite relationships;
- **Module Header** — competence promise + prerequisites + exit criteria;
- **Lesson Unit** — one primary concept/action;
- **Checkpoint** — formative retrieval/application;
- **Variant/Conflict Panel** — preserves qualified/conflicting knowledge;
- **Source Map** — provenance and evidence navigation.

## 3. Course Map grammar

- Default progression reads left-to-right on wide layouts, top-to-bottom on narrow/print.
- Module order must match `learning-path.json` unless a format-specific split is explicitly documented.
- Required modules are visually primary; optional deep dives are secondary.
- Fast-track skips must be visible as alternate paths, never silently remove prerequisites.
- Avoid game-like progress bars unless actual learner progress data exists.
- Do not fabricate completion percentages, scores or mastery indicators.

## 4. Module states

Use semantic states, not arbitrary colors:

- `foundation` — prerequisite/base;
- `core` — required central content;
- `application` — guided/independent use;
- `variant` — alternative/specialized branch;
- `conflict/open` — unresolved or qualified knowledge;
- `optional` — enrichment/deep dive.

Color may reinforce states but labels/shape/text must preserve meaning in grayscale.

## 5. Learning objective presentation

Learning objectives should be short, observable and action-oriented.

Prefer:

- explain;
- distinguish;
- sequence;
- interpret;
- apply;
- diagnose;
- compare;
- justify.

Avoid vague objectives such as “understand” when a more observable verb is available.

## 6. Activities and checks

- Distinguish **Learn**, **Practice**, **Check**, and **Reflect** visually.
- Feedback/explanations should be adjacent or directly reachable.
- Correct-answer styling must not rely on color only.
- MC distractors must remain readable and not visually privilege the correct answer before interaction/reveal.
- In static PPTX/DOCX/PDF, answers belong in a clearly separated solution/review area where appropriate.
- Conflict-dependent questions must visibly preserve the qualification rather than forcing a false binary answer.

## 7. Course Landingpage

Default information architecture:

`Hero -> Course Goal -> What you need -> Course Map -> Module 1..N -> Practice/Checks -> Consolidation -> Source Map`

Each module should support:

- competence promise;
- prerequisites;
- learning objectives;
- lesson navigation;
- mental model / dominant visual;
- activities;
- checkpoint;
- exit criteria;
- source/evidence links.

Responsive navigation must remain usable without horizontal course maps overflowing the viewport.

## 8. Presentation

Two valid presentation modes:

1. **Instructor/Workshop Deck** — teaching flow through modules;
2. **Course Overview Deck** — architecture, goals, module map, selected learning content.

For large courses, prefer one overview deck plus module decks rather than one excessively long deck.

Every module deck preserves the same module ID, objective IDs and Course-Fingerprint as the canonical model.

## 9. DOCX / PDF

Default structures:

### Study Guide
`course overview -> module map -> modules/lessons -> activities -> checkpoints -> answer rationale -> sources`

### Trainer Guide
Adds facilitation notes, expected misconceptions and suggested discussion prompts, clearly separated from learner-facing content.

Do not independently reorder modules during pagination/layout repair.

## 10. Visual density

- Course Map: overview only, not every claim.
- Module page/slide: one primary learning message.
- Exercise page: task first, evidence/explanation second.
- Do not shrink typography to fit an entire curriculum into one visual.
- Split large concept graphs into overview + focused subgraphs.

## 11. Accessibility

In addition to base learning DESIGN:

- path direction must be recoverable from text/numbering;
- optional vs required must not rely on color;
- prerequisite relationships need textual equivalents;
- question feedback is keyboard/read-order friendly in HTML;
- printable activities leave sufficient space for learner response when that is the intended use.

## 12. Provenance

Every final format must be able to reconstruct:

- Course-Fingerprint;
- Multi-Source-Fingerprint(s);
- module and objective IDs;
- claim/evidence IDs for checks;
- design authority chain;
- renderer/QA revision.

## 13. Course Design Gate

PASS requires:

- module order matches canonical Learning Path;
- required/optional/variant semantics are preserved;
- prerequisite graph has no misleading visual edges;
- no fake progress/mastery metrics;
- every knowledge check remains linked to its learning objective;
- solution rationale does not introduce unsupported claims;
- all delivered formats use the same Course-Fingerprint;
- unresolved Critical/Major findings = 0.

## 14. Anti-patterns

Reject:

- playlist thumbnails presented as curriculum architecture;
- identical card grid for every module regardless of content;
- gamification decoration without learning function;
- progress percentages with no learner-state data;
- hidden prerequisite skips;
- quiz trivia unrelated to learning objectives;
- conflicting scientific claims turned into single-answer questions;
- module order drifting between HTML, PPTX and DOCX/PDF.
