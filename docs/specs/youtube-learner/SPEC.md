# YouTube Learner — Skillz Workflow Specification

Status: candidate  
Version: 0.1  
Date: 2026-08-28

## 1. Goal

Create a reusable Skillz workflow that turns one YouTube video into an evidence-bound learning package:

- Key Take-Home Messages / Study Guide;
- optional derived instructional SOP;
- explanatory diagrams and SVGs;
- optional generated explanatory images;
- Landingpage-style static HTML;
- editable presentation through the existing template-presentation stack;
- editable DOCX and verified PDF;
- final cross-format QA.

The same semantic learning model drives every output.

## 2. Architectural decision

The workflow is split into small skills instead of one monolithic summarizer:

1. `youtube-video-ingestion`
2. `multimodal-learning-analysis`
3. `learning-summary-synthesis`
4. `procedure-sop-extractor`
5. `learning-visual-planner`
6. `learning-content-design-system`
7. `learning-svg-generator`
8. `learning-image-generator`
9. `learning-landingpage-renderer`
10. `learning-document-delivery`
11. existing `template-presentation-workflow`
12. `learning-artifact-qa`
13. `youtube-learning-workflow` as user-facing orchestration entry point.

## 3. Canonical flow

```text
YouTube URL
  |
  v
youtube-video-ingestion
  |-- youtube-video-source.json
  |-- youtube-transcript-index.json
  `-- youtube-frame-index.json
  |
  v
multimodal-learning-analysis
  |-- learning-evidence.json
  `-- learning-concept-map.json
  |
  +--> learning-summary-synthesis
  |      `-- learning-summary.*
  |
  `--> procedure-sop-extractor (optional)
         `-- derived-procedure / derived-sop
  |
  v
youtube-learning-workflow assembles
learning-content-model.json
  |
  +--> learning-visual-planner
  |       +--> learning-svg-generator
  |       `--> learning-image-generator
  |
  +--> learning-content-design-system -> resolved DESIGN.md context
  |
  +--> learning-landingpage-renderer
  +--> template-presentation-workflow
  `--> learning-document-delivery
           |
           v
     learning-artifact-qa
```

## 4. `learning-content-model.json`

The orchestrator owns this **compiled reference model**. It does not duplicate producer ownership of subskill artifacts; it references their IDs/fingerprints and assembles finalized sections for renderers.

Suggested schema:

```json
{
  "schemaVersion": 1,
  "source": {
    "provider": "youtube",
    "videoId": "...",
    "url": "...",
    "title": "...",
    "durationSeconds": 0,
    "sourceArtifact": "youtube-video-source.json"
  },
  "audience": "professional",
  "language": "en",
  "mode": "full",
  "learningObjectives": [],
  "summaryArtifact": "learning-summary.json",
  "procedureArtifact": "derived-procedure.json",
  "evidenceArtifact": "learning-evidence.json",
  "conceptMapArtifact": "learning-concept-map.json",
  "sections": [],
  "timestampMap": [],
  "terminology": [],
  "openEvidenceGaps": [],
  "requestedFormats": ["html", "pptx", "docx", "pdf"]
}
```

Renderers may receive embedded finalized content or referenced artifacts, but they must share one immutable model fingerprint for the run.

## 5. Evidence semantics

All downstream skills preserve:

- `observed`: direct source evidence;
- `derived`: reasoned reconstruction from source evidence;
- `recommended`: external best-practice addition;
- `unknown`: unresolved.

Generated visuals are not source evidence.

## 6. SOP semantics

A video-derived procedure defaults to **derived instructional SOP**.

For controlled/safety-critical contexts:

```text
derived instructional SOP
 -> domain validation
 -> controlled-quality-documentation
 -> approval/effective state
```

Missing quantities, timings, settings, tolerances or safety parameters are not inferred.

## 7. Visual architecture

### Planning first

`learning-visual-planner` chooses the representation before generation.

### SVG first for structured meaning

Prefer SVG for:

- flows;
- timelines;
- decision trees;
- concept maps;
- architecture;
- matrices;
- technical schematics.

### Generated image only when useful

Use generated imagery for:

- spatial/physical explanation;
- conceptual illustration;
- realistic but explicitly illustrative teaching scenes.

Avoid image generation for text-heavy diagrams or data that should remain editable.

## 8. DESIGN.md

Shared default: `docs/learning-content/DESIGN.md`.

Authority:

```text
approved template/brand
 > applicable corporate DESIGN.md
 > project DESIGN.md
 > learning-content DESIGN.md
 > renderer default
```

For EUROIMMUN company content:
`docs/corporate/euroimmun/DESIGN.md` remains mandatory and its Corporate Design Gate must PASS.

## 9. HTML output

A portable static page is the primary interactive learning format.

Required capabilities:

- responsive;
- source/timestamp navigation;
- key takeaways;
- mental model;
- optional SOP;
- visual assets;
- source map;
- print support;
- accessible structure.

## 10. Presentation output

Reuse existing `template-presentation-workflow`; do not create a second PPTX engine.

Educational default storyline:

`why it matters -> mental model -> key concepts -> how it works -> procedure -> critical details -> mistakes -> takeaways`

Use Corporate wrappers where applicable.

## 11. DOCX/PDF output

`learning-content-model -> canonical DOCX -> full-page QA -> PDF -> parity QA`

Corporate renderer/template takes precedence. No independent PDF re-authoring.

## 12. Copyright / platform boundary

- no bypass of access controls or DRM;
- no assumption that arbitrary YouTube media can be downloaded;
- prefer accessible captions, supplied transcripts or supplied/local media;
- avoid long verbatim transcript reproduction;
- source frames are used selectively and provenance is retained;
- explanatory visuals should generally be newly created from learned concepts rather than copied visual expression.

## 13. QA gates

Final `learning-artifact-qa` verifies:

1. source identity;
2. claim traceability;
3. timestamp validity;
4. SOP state fidelity;
5. visual semantic fit;
6. generated/source asset provenance;
7. DESIGN.md conformance;
8. HTML responsive/render quality;
9. PPTX structural + render QA;
10. DOCX full-page QA;
11. PDF parity;
12. cross-format semantic consistency;
13. applicable Corporate Design Gate.

## 14. v1 non-goals

- playlist/multi-video synthesis;
- automated LMS/SCORM packaging;
- quizzes with psychometric calibration;
- automatic controlled-SOP approval;
- video re-editing;
- copying whole transcripts or frame sequences.

These can be layered later without changing the core content model.

## 15. Extension path

Future adapters can feed the same analysis core:

- `local-video-learning-workflow`;
- webinar/meeting recordings;
- training recordings;
- lecture capture;
- multi-video course synthesis.

The analysis and semantic model stay provider-neutral even though the first ingestion adapter and user-facing entry point are YouTube.
