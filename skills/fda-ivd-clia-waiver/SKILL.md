---
name: fda-ivd-clia-waiver
description: Bewertet IVDs auf FDA-CLIA-Waiver-Eignung und erzeugt Flex-/User-Study- sowie Evidence-Gaps ohne Submission zu simulieren.
userFacing: true
implicitInvocation: false
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - fda-device-classification-product-code
  - regulated-product-context
  - medical-device-risk-management-iso14971
  - regulatory-evidence-traceability
outputs:
  - clia-waiver-strategy.json
  - flex-study-needs.json
  - clia-evidence-gaps.json
lastEvaluated: 2026-08-07
---

# FDA IVD CLIA Waiver

## Zweck und Grenze

Dieser Skill bewertet, ob ein IVD-Testsystem eine belastbare CLIA-Waiver-Strategie besitzt und welche zusätzliche Evidenz für die FDA-Bewertung der Waiver-Kriterien benötigt wird. Er ersetzt keine 510(k)-/De-Novo-Strategie, keine generische Analytical-/Clinical-Performance-Auswertung und keine externe CLIA-Waiver-Submission.

## Kernprinzipien

- **Waiver criteria are distinct:** Marketing Clearance/Authorization und CLIA Waiver sind getrennte Regulatory States.
- **Simple and low erroneous-result risk:** die Waiver-Argumentation adressiert die aktuellen gesetzlichen/FDA-Kriterien zur Einfachheit und zum Risiko fehlerhafter Ergebnisse.
- **Intended waived user matters:** User, Setting, Training, Workflow und Environment müssen dem geplanten waived-use context entsprechen.
- **Flex studies are risk-driven:** Flex-/Robustness-/Operator-/Environment-Challenges werden aus tatsächlichen Failure Modes, Use Errors und Process Dependencies abgeleitet, nicht aus einer starren Liste.
- **Existing evidence may be reused:** geeignete 510(k)-/Design-/Performance-/Risk-Evidenz wird referenziert; CLIA-spezifische Gaps bleiben sichtbar.
- **Waiver strategy ≠ FDA waiver:** interne Readiness oder positive Strategy ist keine FDA-Entscheidung.

## Workflow

### 1. CLIA Context fixieren

Erfasse Testsystem, Intended Use, User/Setting, Workflow, Specimen/Handling, Instrumentation, Result Interpretation, Training/Instructions und vorhandenen CLIA-Categorization-/Marketing-Status.

### 2. Current FDA Context laden

Verifiziere aktuelle FDA-CLIA-Waiver-/Categorization-Guidance, Decision Summaries soweit hilfreich, Q-Sub-/Submission-Hinweise und `asOf`. Guidance-Empfehlungen werden von gesetzlichen/regulatorischen Kriterien getrennt.

### 3. Simplicity und Error-Risk analysieren

Mappe kritische Schritte, Operator Decisions, Sample/Environmental Dependencies, Failure Modes, Risk Controls, Detection/Lockouts, Instructions/Labeling und Folgen fehlerhafter Ergebnisse. Nutze das bestehende ISO14971-Risk-System statt eines zweiten Risk Registers.

### 4. Evidence/Flex Needs ableiten

Klassifiziere Evidence als `reusable|clia-specific-needed|flex-study-needed|user-study-needed|labeling/instruction-gap|risk-control-gap|unknown`. Definiere Challenge/Population/Operator/Environment/Acceptance-Rationale **vor** Datenauswertung.

### 5. Routing

- 510(k)-SE Evidence → `fda-510k-substantial-equivalence`
- Dual Pathway → `fda-dual-510k-clia-waiver`
- FDA Feedback zu Study Design → `fda-qsub-strategy`
- Labeling/Instructions → `medical-device-labeling-ifu`
- Risk Gap → `medical-device-risk-management-iso14971`
- Design/Process Change → `design-change-regulatory-impact`
- externe Submission/Receipt → verifizierter Human-/External-Action-Path.

## Output-Verträge

`clia-waiver-strategy.json` enthält Product/User/Setting Context, Current Sources/`asOf`, Waiver Criteria Mapping, Simplicity/Error-Risk Assessment, Existing Evidence, Strategy State und FDA/Human Authority Boundary.

`flex-study-needs.json` enthält Risk/Use Step, Challenge Condition, Study/Evidence Type, Acceptance Rationale, Existing Evidence, Gap, Owner und Stop Condition.

`clia-evidence-gaps.json` enthält Gap ID, Criterion/Risk/Claim Link, Missing Evidence/Decision, Impact, Next Skill und Closure Evidence.

## Memory Path

Persistenzwürdig sind validierte CLIA-Waiver-Decision-Heuristiken, abstrahierte Flex-Study-Patterns und stabile User/Workflow-Risk-Mappings. Konkrete Study Designs, aktuelle Product/User Configurations, unpublished Results, FDA Feedback, CW/Dual IDs und Waiver Decisions bleiben run-only bzw. in kontrollierten Regulatory/Study Records. Regulatory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- **Waiver criteria are distinct** von Marketing Authorization behandelt werden,
- Simplicity und erroneous-result risk explizit evidenzgebunden bewertet werden,
- Flex-/User-Study Needs risk-driven statt checklistengetrieben sind,
- Acceptance-/Study-Rationale vor Ergebnissen festgelegt wird,
- bestehende Evidenz referenziert statt dupliziert wird,
- eine interne Strategy nicht als FDA Waiver dargestellt wird,
- konkrete CLIA-/Study-/FDA-Zustände nicht in globales dauerhaftes Memory gelangen.
