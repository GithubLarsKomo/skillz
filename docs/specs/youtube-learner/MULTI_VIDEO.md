# YouTube Learner — Multi-Video / Playlist Specification

Status: candidate  
Version: 0.1  
Date: 2026-08-28

## Goal

Extend the single-video YouTube Learner without replacing it. Each video remains independently evidence-bound; a second layer arbitrates and synthesizes the per-video models into one canonical multi-source learning model.

## Architecture

```text
playlist / URL set
  -> N x youtube-learning-workflow (analysis phase)
  -> N x learning-content-model.json
  -> learning-source-arbitration
  -> multi-source-learning-synthesis
  -> multi-source-learning-model.json
  -> visual plan + multi-source DESIGN.md
  -> HTML | PPTX | DOCX -> PDF
  -> learning-artifact-qa + cross-source gates
```

New composable skills:

1. `learning-source-arbitration`
2. `multi-source-learning-synthesis`
3. `youtube-playlist-learning-workflow`

Existing renderers and visual generators are reused.

## Source model

Every source keeps:

- stable source ID;
- video/source identity;
- individual model fingerprint;
- transcript/frame provenance;
- source authority context;
- dependency relationship to other sources;
- availability status.

Unavailable videos are never represented as analyzed.

## Arbitration model

Arbitration is claim-level and considers evidence proximity, authority, independence, relevant recency, specificity, internal evidence confidence and conflicts-of-interest context.

Source count is not truth. Dependent sources are grouped and do not inflate `independentSourceCount`.

Allowed convergence states:

- `convergent`
- `qualified-convergence`
- `conflicted`
- `single-source`
- `insufficient`

## Synthesis model

`multi-source-learning-model.json` owns the cross-source compilation and references all input fingerprints.

Minimum logical sections:

```json
{
  "schemaVersion": 1,
  "sources": [],
  "sourceModelFingerprints": [],
  "claimClusters": [],
  "consensusCore": [],
  "qualifiedClaims": [],
  "conflicts": [],
  "coverageMap": [],
  "procedureVariants": [],
  "sections": [],
  "sourceMap": [],
  "openEvidenceGaps": [],
  "requestedFormats": []
}
```

## Deduplication rules

- normalize terminology but preserve original labels;
- atomize claims before clustering;
- preserve scope/method/version/population qualifiers;
- cluster only semantically equivalent claims;
- do not collapse merely related claims;
- preserve every contributing source/evidence pointer.

## Conflict rules

A material disagreement is represented explicitly with positions, sources, qualifiers, resolution status and safe learner wording.

Never:

- average incompatible numerical parameters;
- hide disagreement by choosing smoother prose;
- infer a winner from views/likes/source count;
- merge different methods into one claim without qualifier.

## Procedure/SOP synthesis

Common steps may form a shared spine. Variants branch by method/context/version. Incompatible protocols are never blended into a synthetic hybrid SOP.

Critical unresolved differences force `incomplete-for-controlled-use`.

## Design

Base: `docs/learning-content/DESIGN.md`.

Additional normative contract: `docs/learning-content/multi-source/DESIGN.md`.

Corporate/project contracts remain higher authority.

Multi-source design must expose consensus, qualification, single-source support, conflict and open evidence through labels plus accessible visual semantics.

## Renderer behavior

All final formats use the same `multi-source-learning-model.json` fingerprint.

HTML adds source navigation and conflict/coverage sections.
PPTX uses a synthesis storyline rather than one-video-per-slide organization.
DOCX/PDF preserve source IDs, variants, conflicts and provenance.

## QA extensions

PASS requires:

- all consensus claims trace to independent source support;
- source dependency groups are respected;
- unresolved material conflicts remain visible;
- single-source claims are not presented as consensus;
- numerical/procedural values remain condition-bound;
- no hybrid protocol is invented;
- stable source IDs across formats;
- full requested render coverage;
- same multi-source fingerprint across outputs;
- unresolved Critical/Major findings = 0.

## Scaling

For large playlists, metadata/chapter/topic clustering may precede deep analysis. Sampling and exclusions must be explicit. A run may only claim `complete-playlist` when every intended source was actually analyzed or intentionally excluded with rationale.

## Golden reference strategy

The first multi-source fixture combines two public PCR learning videos:

- S1: `PCR explained | biology animation`, yourgenome / Wellcome Sanger Institute, video `Q2847XA-Rfk`, CC BY 4.0;
- S2: `qPCR and PCR Explained: Real-Time PCR Animation`, ClevaLab, video `rpLSvEbOmqc`.

The fixture protects the architectural invariants rather than storing copyrighted transcripts or video frames.
