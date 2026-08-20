# Teach Integration Specification

Status: draft architecture specification  
Scope: `GithubLarsKomo/skillz`, `GithubLarsKomo/exam-trainer-framework`, `GithubLarsKomo/grilling`, deployment through GitHub/Coolify/Hetzner  
Primary user entrypoint: `/teach`  

## 1. Purpose

Integrate the strongest ideas from Matt Pocock's `teach` skill into `skillz` without copying its monolithic workspace model. The resulting system shall provide persistent, evidence-grounded, stateful learning across sessions while reusing the existing Skillz knowledge/evidence layer and `exam-trainer-framework` (ETF) as the shared learning, retrieval and assessment runtime.

The core learning loop is:

```text
Mission
  -> trusted evidence
  -> KnowledgeItems
  -> lessons / guided explanation
  -> spaced retrieval and practice in ETF
  -> ReviewEvents
  -> learning assessment
  -> learning state
  -> next challenge in the learner's zone of proximal development
```

The system optimizes for durable learning rather than mere coverage or conversational fluency.

## 2. Architectural decision

### 2.1 `/teach` is an orchestrator

`/teach` owns pedagogical orchestration. It decides what should be learned next, why, and at what level of challenge. It does not duplicate domain logic from FDA, IVDR, engineering, research, patent, writing or other Skillz capabilities.

Initial invocation metadata:

```yaml
name: teach
userFacing: true
implicitInvocation: false
category: productivity
```

The command is explicit by default. A normal request such as "explain X" must not silently create a persistent learning workspace.

### 2.2 ETF is the shared learning and assessment runtime

`GithubLarsKomo/exam-trainer-framework` is not only an examination runtime. For Teach integration it is the authoritative runtime for:

- spaced-repetition scheduling;
- adaptive learning queues;
- learning sessions;
- question rendering;
- learner self-grading and structured grading assistance;
- immutable ReviewEvents;
- diagnostics such as repeated failure, uncertainty, slow recall and leeches;
- examination simulation;
- local/offline learner-state persistence;
- backup and restore.

ETF SHALL NOT be forked for Teach.

Teach-specific capabilities are added to ETF through additive, general-purpose interfaces. ETF remains independently usable for existing catalogs such as Fügetechnik.

### 2.3 Anki is an inbound content capability, not a second runtime

ETF's existing safe `.apkg` import remains authoritative for Anki content ingestion. Imported note fields, tags, deck hierarchy, cloze semantics and supported media may become ETF content.

Anki scheduling and review history remain intentionally excluded from import. Teach does not introduce Anki as a second scheduler or learner-state owner.

Conceptually:

```text
Anki .apkg -----\
Teach evidence ---+--> ETF KnowledgeItem --> QuestionVariants --> ETF learning/exam runtime
Skillz skill -----/
```

### 2.4 FSRS policy remains controlled by ETF

ETF currently keeps the classic five-stage scheduler authoritative while FSRS runs in shadow mode. Teach MUST NOT bypass ETF's activation policy or make FSRS authoritative implicitly.

Any future switch to FSRS is an ETF product decision based on the existing controlled Classic-vs-FSRS evaluation and activation policy.

## 3. Separation of responsibilities

### Skillz `/teach`

Owns:

- learning mission;
- success criteria and scope;
- prerequisite/competency interpretation;
- evidence acquisition and selection;
- pedagogical sequencing;
- zone-of-proximal-development selection;
- decisions between explanation, retrieval, application and transfer;
- interpretation of ETF evidence into semantic learning state;
- creation of learning records only after demonstrated understanding;
- selection of the next challenge.

Does not own:

- domain truth already owned by specialist Skillz skills;
- browser persistence;
- spaced-repetition scheduling mechanics;
- question UI/runtime;
- exam session mechanics;
- ETF deployment internals.

### `exam-trainer-framework`

Owns:

- KnowledgeItem / QuestionVariant runtime model;
- ReviewEvent persistence;
- learning/exam session mechanics;
- classic scheduler and FSRS shadow state;
- adaptive queue;
- question types and renderers;
- catalog validation/versioning;
- local learner state;
- PWA/offline behavior;
- backup/export.

ETF does not decide the learner's overall mission or pedagogical roadmap.

### Specialist Skillz capabilities

Examples: `fda-510k-predicate-strategy`, `research-to-evidence-note`, `large-work-wayfinder`, regulatory skills, engineering skills.

They remain authoritative for their domain semantics and may supply:

- concepts;
- workflows;
- evidence claims;
- evaluation cases;
- domain constraints;
- realistic exercises.

They MUST NOT acquire a dependency on `teach`.

### `research-to-evidence-note`

Owns claim/source separation, source quality, conflicts, confidence and freshness. Teach consumes its evidence output rather than reproducing research-evidence logic.

### Knowledge layer

`structured-knowledge-artifact`, `knowledge-view` and `knowledge-map-generator` may package and project learning artifacts. Teach-specific learning semantics remain owned by Teach rather than these generic knowledge tools.

### Grilling

Requirements Grilling remains authoritative for requirements decisions. Teach may reuse the generic questioning approach for mission clarification but MUST NOT reinterpret `requirements-handoff.json` as a learning contract.

A future refactor MAY separate a generic round-based grilling runtime from concrete requirements-grilling semantics. This refactor is useful but not a prerequisite for Teach v0.1.

## 4. Canonical learning objects

### 4.1 Learning Mission

Portable output:

- `learning-mission.json`
- optional Markdown mirror

Minimum contract:

```json
{
  "schemaVersion": 1,
  "id": "mission-id",
  "topic": "...",
  "why": "concrete real-world outcome",
  "successCriteria": ["observable capability"],
  "constraints": [],
  "outOfScope": [],
  "sourceRefs": [],
  "state": "active"
}
```

One active mission should represent one coherent learning goal. Mission changes are explicit and create a learning-state event rather than silently rewriting history.

### 4.2 Learning State

Portable output:

- `learning-state.json`

It records semantic competence, not every UI event.

```json
{
  "schemaVersion": 1,
  "missionId": "...",
  "competencies": [
    {
      "id": "...",
      "statement": "...",
      "level": "introduced|retrieval-demonstrated|application-demonstrated|transfer-demonstrated",
      "evidenceRefs": [],
      "lastDemonstratedAt": "...",
      "state": "active"
    }
  ],
  "misconceptions": [],
  "priorKnowledge": [],
  "openGaps": [],
  "nextCandidateCompetencies": []
}
```

Material merely presented in a lesson MUST NOT be promoted to demonstrated competence.

### 4.3 Learning Record

A learning record is created only when one of the following is evidenced:

- non-trivial understanding has been demonstrated;
- prior knowledge has been established sufficiently to alter future teaching;
- a misconception has been corrected;
- the mission changed because of new learning.

Learning records are concise semantic records, not session logs.

### 4.4 Review evidence

ETF `ReviewEvent` remains the low-level immutable evidence stream for actual learner interactions. Teach references ETF ReviewEvents; it does not copy the full raw event history into each learning record.

ETF already distinguishes the source of a review as `learning` or `exam`. Teach SHALL preserve this distinction.

## 5. KnowledgeItem as the integration pivot

ETF's existing separation between `KnowledgeItem` and `QuestionVariant` becomes the central Teach/ETF contract.

A KnowledgeItem represents one durable semantic object. QuestionVariants provide different retrieval or application surfaces for the same underlying item.

Example:

```text
KnowledgeItem: 510(k) predicate suitability
  |- free-text recall variant
  |- matching variant
  |- single-choice edge case
  |- comparative application case
  `- novel transfer case
```

Teach should prefer multiple high-quality variants over producing many duplicated cards that create fragmented learner state.

### Proposed additive ETF metadata

ETF should support optional metadata such as:

```json
{
  "learningObjective": "Evaluate whether a candidate is suitable as a predicate",
  "competencyClass": "knowledge|application|transfer",
  "origin": {
    "type": "skillz-teach|anki|manual|other",
    "missionId": "...",
    "sourceSkill": "...",
    "sourceRefs": [],
    "sourceCommit": "..."
  }
}
```

Exact field placement shall be resolved during ETF implementation so existing catalogs and migrations remain backward compatible.

## 6. Teach capabilities

The target capability split is intentionally composable.

### 6.1 `teach` — user-facing orchestrator

Inputs:

- topic or Skillz skill;
- optional existing mission/workspace;
- explicit command mode.

Outputs:

- updated learning mission/state;
- next lesson/practice action;
- links or handoffs to ETF learning/exam sessions when required.

Suggested command surface:

```text
/teach <topic>
/teach skill <skill-name>
/teach status
/teach review
```

### 6.2 `learning-mission`

Owns mission definition and revision.

### 6.3 `learning-resource-curation`

Selects and annotates high-trust resources appropriate to the mission. Evidence synthesis is delegated to `research-to-evidence-note` where multiple claims/sources must be reconciled.

### 6.4 `learning-state`

Transforms demonstrated evidence into semantic competence records, misconceptions and gaps.

### 6.5 `learning-next-step`

Chooses the next pedagogical move using mission, prerequisites, learning state, due review evidence and current difficulty.

Possible outcomes:

- explanation;
- worked example;
- guided exercise;
- retrieval practice;
- application case;
- transfer case;
- ETF learning session;
- ETF examination;
- real-world/practitioner exercise.

### 6.6 `learning-assessment-spec`

Defines what evidence is needed to justify a competence transition. It is provider-neutral and does not emit ETF-specific cards directly.

### 6.7 `learning-assessment`

Interprets learner evidence, including ETF ReviewEvents and exam results, into semantic competence conclusions.

### 6.8 `learning-review-queue`

Provides a portable semantic view of competencies that require revisit, reinforcement or transfer checks. ETF remains the scheduler of individual review items.

### 6.9 ETF adapter capabilities

Internal adapter functions/skills may include:

- `exam-trainer-catalog-builder`;
- `exam-trainer-validator`;
- `exam-trainer-publisher`;
- `exam-trainer-result-import`.

These adapters translate contracts; they MUST NOT reproduce ETF's scheduling or rendering logic.

## 7. Assessment hierarchy

Teach shall distinguish at least:

1. exposure — material was presented;
2. retrieval — learner can recall/use the concept without immediate support;
3. application — learner can apply it in a representative problem;
4. transfer — learner can apply it to a sufficiently novel problem.

An overall percentage MUST NOT be treated automatically as a competence state. A learner may have strong recall and weak transfer.

Learning-state transitions therefore depend on the required evidence for the specific competence.

## 8. Anki integration

### Existing ETF behavior to preserve

- safe APKG parsing;
- note fields/tags/deck hierarchy/template identity/cloze semantics preserved where supported;
- media imported through the ETF asset pipeline;
- imported templates never executed;
- imported content treated as untrusted input;
- Anki scheduling/review history ignored;
- imported content committed into a new ETF catalog.

### Teach enrichment after Anki import

Teach MAY use imported ETF KnowledgeItems as starting material to:

- map items to a learning mission;
- identify duplicates or overly fragmented concepts;
- add trusted evidence/provenance;
- generate better explanations;
- create additional QuestionVariants;
- add application and transfer cases;
- identify weak or ambiguous cards for review;
- associate concepts with Skillz skills and prerequisite relations.

Teach MUST NOT silently mark imported cards as authoritative domain knowledge merely because they came from Anki.

## 9. Hosted catalogs and deployment

### 9.1 Runtime deployment

ETF shall gain a first-class GitHub -> Coolify -> Hetzner deployment path analogous to other hosted project runtimes.

Target path:

```text
GitHub main
  -> CI: tests + production build
  -> Coolify deployment trigger
  -> Hetzner container/runtime
  -> HTTPS PWA
```

Netlify may remain supported but is not the canonical Teach integration target.

### 9.2 One runtime, multiple catalogs

Do not deploy one container per learning mission or exam.

Use one ETF runtime capable of discovering/importing multiple hosted catalogs while keeping learner state local.

### 9.3 Hosted Catalog Registry

ETF should support a read-only hosted registry whose entries identify published catalogs and immutable content versions/hashes.

Conceptual contract:

```json
{
  "schemaVersion": 1,
  "catalogs": [
    {
      "id": "skillz-large-work-wayfinder",
      "version": "1.0.0",
      "title": "Large Work Wayfinder",
      "manifestUrl": "/catalogs/skillz-large-work-wayfinder/catalog.json",
      "contentHash": "...",
      "status": "released"
    }
  ]
}
```

Downloaded/selected catalogs are copied into local ETF storage for offline learning. Hosted content must not create a server-side learner profile.

### 9.4 Runtime/content lifecycle separation

Longer-term target:

- `exam-trainer-framework`: runtime/application lifecycle;
- hosted catalog repository or build input: content lifecycle.

A catalog-only change SHOULD eventually be publishable without rebuilding unrelated runtime code. This separation may be implemented after the first integrated deployment.

## 10. Publication and trust

Teach-generated personal learning material may pass through an automated personal validation path, but it must not be confused with externally approved training content.

For reusable or formally released catalogs, preserve ETF's controlled content lifecycle:

```text
draft -> in_review -> approved -> released -> retired
```

Released content remains immutable. New revisions create new versions.

For regulated or organizational training, Teach/ETF evidence MUST NOT by itself claim formal qualification, authorization, certification or QMS training completion. Such claims require a separate governed training-record workflow with appropriate authority.

## 11. Privacy and persistence

Default model:

- learner progress remains local in ETF IndexedDB;
- hosted servers publish application and catalog content, not learner history;
- raw private connector payloads are not persisted into catalogs;
- secrets/tokens never enter learning artifacts;
- durable global user preferences are governed separately by `communication-memory-governance`;
- mission-specific competence remains inside the learning workspace/state unless explicitly packaged as a portable artifact.

Cross-device learner synchronization remains out of scope for Teach v0.1 unless separately specified.

## 12. `/teach skill <skill-name>`

A Skillz skill can itself become a learning target.

Teach may use:

- the current canonical `SKILL.md`;
- declared dependencies and dependents;
- output contracts;
- evaluation fixtures/cases;
- referenced evidence and domain sources;
- the capability index for exact skill identity and discovery metadata.

The result is a competency path rather than a prose walkthrough.

Example:

```text
/teach skill large-work-wayfinder

1. distinguish technical from product uncertainty
2. separate facts, assumptions and hypotheses
3. define investigation issues
4. define stop conditions
5. build dependency evidence
6. route between Grilling, Wayfinder and Spec
7. solve realistic case
8. solve novel transfer case
```

ETF may then provide spaced practice and exam/transfer variants derived from this path.

## 13. Implementation sequence

### Phase 0 — architecture contracts

- [x] Decide against ETF fork.
- [x] Define ETF as shared learning + assessment runtime.
- [x] Keep Anki as inbound content source.
- [x] Keep FSRS activation under ETF governance.
- [ ] Review and approve this specification.

### Phase 1 — Skillz learning-state foundation

- [ ] Create `teach` user-facing orchestrator.
- [ ] Define `learning-mission` contract.
- [ ] Define `learning-state` and learning-record contract.
- [ ] Define `learning-next-step`.
- [ ] Define `learning-assessment-spec` and `learning-assessment`.
- [ ] Define routing to `research-to-evidence-note` and knowledge artifacts.

### Phase 2 — ETF interoperability

In `exam-trainer-framework`:

- [ ] Add backward-compatible Teach/origin metadata to KnowledgeItems/QuestionVariants/catalogs as necessary.
- [ ] Define portable catalog import/build contract for Teach-generated content.
- [ ] Define machine-readable export of relevant ReviewEvents/assessment summaries without exposing unrelated local state.
- [ ] Add tests proving existing Fügetechnik and imported catalogs remain compatible.

### Phase 3 — Learning integration

- [ ] Teach can create a small ETF learning catalog from an evidence-backed concept set.
- [ ] ETF can schedule and run spaced learning for that catalog.
- [ ] ReviewEvents can be returned to Teach.
- [ ] Teach can update semantic learning state from demonstrated evidence.
- [ ] Teach can select a corrective or harder next step.

### Phase 4 — Anki enrichment

- [ ] Import an APKG through ETF's existing safe path.
- [ ] Expose imported KnowledgeItems to Teach.
- [ ] Add provenance and learning-objective mapping.
- [ ] Generate additional variants only where pedagogically justified.
- [ ] Validate no Anki scheduling/runtime semantics leak into ETF.

### Phase 5 — hosted runtime

- [ ] Add Docker/production hosting support to ETF.
- [ ] Add GitHub CI gate for production deployment.
- [ ] Configure Coolify/Hetzner HTTPS runtime.
- [ ] Add Hosted Catalog Registry.
- [ ] Verify PWA install/update/offline behavior on hosted runtime.
- [ ] Keep learner state local and verify server receives no learner history.

### Phase 6 — Skillz self-teaching

- [ ] Implement `/teach skill <skill-name>`.
- [ ] Generate prerequisite/competency paths from canonical Skillz metadata.
- [ ] Use evaluation fixtures as candidate application/transfer material.
- [ ] Pilot on at least one engineering and one regulated/research skill.

## 14. Acceptance criteria

The integration is acceptable when all of the following are true:

1. A user can explicitly start `/teach <topic>` and receive a mission-grounded learning path.
2. Domain claims used for teaching remain traceable to specialist Skillz/evidence sources.
3. Material exposure alone never creates demonstrated competence.
4. ETF can receive Teach-generated KnowledgeItems/QuestionVariants without a fork.
5. ETF can provide both learning sessions and examinations for the same semantic KnowledgeItems.
6. ETF ReviewEvents can support Teach learning-state transitions.
7. APKG content can enter through ETF's existing safe importer and later be enriched by Teach.
8. Anki scheduler/history does not become a second learner-state authority.
9. FSRS remains governed by ETF's existing activation policy.
10. Existing ETF catalogs and learner-state migrations remain backward compatible.
11. A hosted ETF instance can be automatically deployed from GitHub to Hetzner through Coolify.
12. Hosted catalogs remain usable offline after local import/cache while learner history stays local by default.
13. `/teach skill <skill-name>` can teach at least one real Skillz capability through retrieval, application and transfer rather than prose-only explanation.

## 15. Non-goals for v0.1

- replacing ETF with Anki;
- importing Anki review history;
- enabling FSRS automatically;
- creating a container per course/exam;
- server-side learner accounts;
- cross-device progress synchronization;
- formal certification or regulated training qualification;
- implicit Teach invocation from ordinary explanation requests;
- duplicating domain skill logic inside Teach;
- duplicating ETF runtime logic inside Skillz.

## 16. Key design principle

The semantic ownership chain is:

```text
Specialist Skill / trusted evidence
              |
              v
        Skillz /teach
      pedagogical intent
              |
              v
       ETF KnowledgeItem
              |
              v
      QuestionVariants
              |
              v
 ETF learning + exam runtime
              |
              v
        ReviewEvents
              |
              v
    learning-assessment
              |
              v
       learning-state
              |
              `----> next challenge
```

This chain is the normative integration model. Any implementation that creates a second scheduler, a second domain truth, or a parallel Teach-specific ETF runtime should be treated as an architectural regression.
