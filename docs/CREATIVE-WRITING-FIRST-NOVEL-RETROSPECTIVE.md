# Creative Writing v0.4 — first-novel retrospective benchmark

Date: 2026-09-10

## Purpose

`first-novel` is used as a **read-only empirical process case** for the reusable Creative Writing workflow. The source repository is not modified, imported, or required at Skillz runtime.

The benchmark intentionally stores only:

- immutable source provenance (repository, observed commit, artifact path, blob SHA);
- derived workflow facts;
- expected reusable policy behavior.

It does **not** copy manuscript prose into Skillz and CI does not fetch `first-novel`.

Canonical benchmark:

`benchmarks/creative-writing-first-novel-process-golden-v1.json`

Regression test:

`tests/test_creative_writing_first_novel_process_golden.py`

## Backward mapping

### 1. Reader Reality

Source pattern:

`blind reader protocol -> reader-only emotional ledger + character reconstruction -> freeze -> architecture comparison`

Reusable lesson:

A reader may reconstruct the required emotional arc and costly final choices while missing some internal architecture specificity. That mismatch is not automatically a Major defect. The gate must distinguish **reader-visible functional sufficiency** from **architecture-level exactness**.

The empirical case also validates the hard isolation rule: architecture and repository search occurred only after two reader-only artifacts were frozen. A contaminated read would be invalid rather than merely lower confidence.

Mapped worker:

`fiction-reader-reality-review`

Golden assertions:

- freeze before intent;
- frozen evidence remains immutable after architecture access;
- Critical/Major drive the gate, while genuine Minor divergence can remain a watchpoint;
- architecture mismatch alone does not establish reader failure.

### 2. Character Voice Fingerprint

Source pattern:

`voice architecture -> retrospective Act-I collision audit -> targeted repair -> prospective chapter-level voice gates`

Reusable lesson:

The same surface phrase can have different meanings for voice governance:

- a genuine signature leak when one character accidentally inherits another character's owned pragmatic pattern;
- intentional borrowing when relationship, institution, irony, provocation, or shared origin makes the overlap meaningful;
- ordinary functional crisis language that is too generic to count as a signature at all.

The Act-I case is especially useful because one Major collision blocked the gate, while two shared-language cases were deliberately preserved. After targeted voice revision the gate passed with no Canon, Reveal, or Plot change.

Mapped worker:

`character-voice-fingerprint`

Golden assertions:

- collision detection must be contextual, not lexical-only;
- open Major voice leakage blocks hardening;
- intentional shared register needs a reason, not automatic deletion;
- voice repair should stay on the smallest sufficient level and not invent Canon changes.

### 3. Creative Revision Regression

Source pattern:

`frozen blind S3 finding -> intent reconciliation -> five-chapter targeted subtractive revision -> targeted regression -> S3 closed, S2 watchpoints retained`

Observed delta:

- 5 chapters touched;
- 20,834 -> 20,503 words;
- delta: -331 words;
- event changes: 0;
- lead-decision changes: 0;
- failed-trial changes: 0;
- nonhuman/secondary agency changes: 0;
- political-consequence changes: 0;
- no fresh three-chamber blind rerun;
- frozen blind evidence retained;
- Protect List regression passed;
- residual S2 issues remained explicitly nonblocking.

Reusable lesson:

Text volume is a poor proxy for narrative impact. A revision spanning several chapters can remain an **R2 multi-scene presentation change** when causality, decisions, agency and consequences are preserved. Conversely, a one-paragraph motivation change could be R3. Gate invalidation therefore follows changed function, not file count or word count.

Mapped worker:

`creative-revision-regression`

Golden assertions:

- classify this empirical delta as R2;
- targeted regression is sufficient;
- do not discard or rewrite frozen blind evidence;
- Protect/Collateral-Damage checks remain mandatory;
- do not falsely close residual watchpoints merely because the original S3 blocker is resolved.

## Why these are fixtures rather than copied project artifacts

The project artifacts contain names, story-specific semantics and manuscript-dependent evidence. Copying them wholesale into Skillz would overfit the generic workflow to one novel and would turn an empirical precedent into an accidental schema.

The Golden fixture therefore preserves only the **decision boundary** each worker must reproduce:

1. valid versus contaminated reader evidence;
2. harmful voice collision versus justified shared language;
3. changed presentation versus changed narrative meaning.

This makes `first-novel` a regression source without making future fiction projects resemble `first-novel`.

## Source snapshot

Observed source repository state:

- repository: `GithubLarsKomo/first-novel`
- ref: `main`
- commit: `293471885152ff16373e558ea9f65e3fe6ee13dc`

Individual process artifacts are additionally pinned by blob SHA in the benchmark file.

## Maintenance rule

Do not silently update the fixture merely because `first-novel/main` changes later.

A future benchmark revision requires an explicit reason, for example:

- a new real project exposes a missing decision boundary;
- the generic worker contract changes intentionally;
- a later `first-novel` pass demonstrates that one of the current abstractions was wrong.

The benchmark is therefore historical evidence, not a live mirror of the source repository.
