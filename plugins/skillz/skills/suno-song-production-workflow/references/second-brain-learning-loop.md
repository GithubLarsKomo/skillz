# Suno Second Brain Learning Loop

## Purpose

The Suno workflow should improve from real generations without confusing taste, one-off randomness, and model behavior. This reference defines how observations are stored and promoted.

## Observation classes

Every learning note must identify one of four classes:

1. `user_preference` — a confirmed preference about music, output format, or workflow.
2. `project_observation` — something observed in one specific song or album.
3. `model_behavior` — a behavior plausibly tied to a named Suno model/version and prompt pattern.
4. `cross_project_learning` — a pattern supported across multiple projects or repeated controlled observations.

Never promote a single surprising take directly to `cross_project_learning`.

## Minimum fields

A `suno-model-learning.md` or equivalent structured note should capture:

- date;
- project and track;
- Suno model/version if known;
- capability-snapshot reference;
- prompt/package version;
- observation class;
- observation;
- user feedback, if any;
- actual output duration if duration is relevant;
- comparison candidate(s), if any;
- confidence: `tentative`, `supported`, or `stable-within-model`;
- scope: track / genre / model / user workflow / cross-project;
- action taken;
- revalidation trigger.

## Model changes

When Suno changes model families or materially changes Create/Edit behavior:

- retain historical notes;
- do not rewrite them as if they were wrong;
- mark affected heuristics `revalidation_required`;
- record new tests under the new model;
- only re-promote a rule after fresh evidence.

## Distinguishing preference from behavior

Examples:

- “The user prefers not to use Extend when a clean full regeneration is easier” -> `user_preference`.
- “This trance prompt produced 2:42 despite a 6:00 target” -> `project_observation`.
- “Three vX generations with this structure consistently undershot target duration” -> `model_behavior`.
- “Across three trance projects, explicit repeated hook blocks improved long-form duration without harming style” -> possible `cross_project_learning`.

## Promotion back into Skillz

Project-specific material remains in the project Second Brain. A learning should be proposed for the reusable Skillz workflow only when:

- it is not merely a personal title/lyric preference;
- it has repeated evidence or a clear platform-contract basis;
- its scope is explicit;
- it remains valid under the current Suno model/capability snapshot;
- it improves a decision rule, gate, or prompt contract rather than bloating the skill with anecdotes.

## Non-text assets

Audio generations, stems, artwork and exports are external assets under `project-second-brain` storage rules. GitHub stores identifiers, links, status, hashes when available, and concise evidence — not a parallel binary archive.
