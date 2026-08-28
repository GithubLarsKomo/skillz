# YouTube Course Builder — Specification

Status: candidate  
Version: 0.1  
Date: 2026-08-28

## Goal

Extend the YouTube learning stack from multi-video synthesis to curriculum construction. The Course Builder turns a playlist, URL set or existing `multi-source-learning-model.json` into a modular learning path with prerequisites, measurable learning objectives, formative activities and consistent HTML/PPTX/DOCX/PDF projections.

## Architecture

```text
YouTube videos / playlist
 -> youtube-playlist-learning-workflow
 -> multi-source-learning-model.json
 -> course-concept-graph
 -> learning-path-planner
 -> learning-activity-generator
 -> course-learning-model.json
 -> visual/design/render stack
 -> course QA
```

The Course Builder does not replace the single-video or multi-video workflows. It composes them.

## Course model

`course-learning-model.json` is the canonical semantic source of truth. Suggested top-level fields:

```json
{
  "schemaVersion": 1,
  "courseId": "...",
  "title": "...",
  "audience": "professional",
  "language": "de",
  "courseDepth": "standard",
  "multiSourceFingerprint": "...",
  "courseFingerprint": "...",
  "assumedPrerequisites": [],
  "modules": [],
  "learningObjectives": [],
  "activitiesArtifact": "course-activities.json",
  "knowledgeChecksArtifact": "course-knowledge-checks.json",
  "sourceMap": [],
  "openEvidenceGaps": [],
  "requestedFormats": ["html", "pptx", "docx", "pdf"]
}
```

## Prerequisite semantics

The graph distinguishes:

- `prerequisite-of`: required knowledge/competence;
- `helps-before`: pedagogically useful but skippable;
- `part-of`: hierarchy;
- `variant-of`: alternative branch;
- `contrasts-with`: comparison;
- `applies-to`: application relation.

Mandatory prerequisite edges must form a DAG. Playlist order is not evidence of prerequisite order.

## Module design

A required module has:

- module ID and competence promise;
- entry prerequisites;
- observable learning objectives;
- lessons mapped to concept/claim IDs;
- active practice;
- formative checkpoint;
- exit criteria;
- source/evidence map.

Modules are built around competence boundaries, not source-video boundaries.

## Learning objectives

Objectives use observable verbs and must map to one or more concepts/claims. Vague statements such as “understand PCR” should be refined to e.g. “explain the role of denaturation, annealing and extension in a PCR cycle”.

## Learning path variants

Supported modes:

- `standard` — complete core path;
- `fast-track` — skips only verified/checked prerequisites;
- `deep-dive` — adds advanced variants, conflicts and source critique;
- `role-specific` — adapts applications and optional branches to a defined role while preserving the common core.

## Formative assessment

Knowledge checks are evidence-bound. Each item carries:

- objective ID;
- claim/evidence IDs;
- expected answer;
- rationale;
- misconception feedback;
- difficulty and cognitive level.

No psychometric validity, certification status or pass mark is implied. In regulated/safety-critical contexts, pass thresholds require an explicit validated assessment process.

## Conflict handling

An unresolved material conflict cannot become a single-answer knowledge-check fact. The course may instead ask learners to distinguish positions, scopes or evidence strengths.

Protocol variants remain separate. The Course Builder must never synthesize incompatible parameters into a new hybrid procedure.

## Course outputs

### HTML

Primary self-study surface: course overview, course map, prerequisites, module navigation, lessons, practice/checks, source map and print support.

### PPTX

Instructor/workshop mode or course overview + module decks. Module IDs/objective IDs remain stable.

### DOCX/PDF

Study Guide or Trainer Guide. PDF derives from canonical DOCX and is parity-checked.

## DESIGN authority

`docs/learning-content/course/DESIGN.md` extends the shared learning design contract. Corporate/project contracts remain higher authority.

## QA

Course PASS requires at minimum:

1. prerequisite DAG valid;
2. every required module has measurable objectives and exit criteria;
3. every required concept is covered or explicitly open;
4. every knowledge check maps to objective and source evidence;
5. conflicts/qualified claims are not flattened into false certainty;
6. no invented mastery/progress data;
7. same Course-Fingerprint across all renderers;
8. complete format-specific render inspection;
9. unresolved Critical/Major findings = 0.

## v1 non-goals

- SCORM/xAPI packaging;
- LMS hosting;
- learner accounts/progress persistence;
- adaptive Bayesian mastery models;
- psychometric calibration;
- certification;
- automatic controlled-procedure qualification.

## Future extension

The same model can later support:

- SCORM/xAPI export;
- spaced-repetition schedules;
- adaptive branching from validated entry/checkpoint results;
- instructor facilitation packs;
- course versioning/change impact when source videos change;
- local video/webinar/document mixtures through provider-neutral source adapters.
