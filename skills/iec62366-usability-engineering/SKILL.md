---
name: iec62366-usability-engineering
description: Bewertet Use-Related-Risk- und Usability-Evidence für Medical Devices entlang IEC 62366-1 ohne Risk oder Design zu duplizieren.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - regulated-product-context
  - medical-device-risk-management-iso14971
  - design-control-traceability
  - medical-device-labeling-ifu
outputs:
  - usability-engineering-assessment.json
  - use-related-risk-evidence.json
  - usability-evidence-gaps.json
lastEvaluated: 2026-08-07
---

# IEC 62366-1 Usability Engineering

## Zweck und Grenze

Dieser Skill strukturiert sicherheitsbezogene Usability-/Human-Factors-Evidence für Medical Devices/IVDs auf Basis der autorisierten aktuellen IEC-62366-1-Ausgabe und aktueller marktbezogener Guidance. Er besitzt weder ein zweites Risk Register noch ersetzt er Design Control, Labeling oder regulatorische Submission-Strategie.

## Kernprinzipien

- **Users uses environments first:** Intended Users, Use Environments, User Interface, Use Scenarios und Training/Labeling Context müssen vor Evaluation fixiert sein.
- **Use-related risk stays linked:** Use Errors, hazardous situations and use-related risk controls verweisen auf den bestehenden ISO14971-Lifecycle.
- **Formative and summative serve different decisions:** formative Evidence dient Design-Lernen; summative/validation Evidence dient der abschließenden sicherheitsbezogenen Use-Evaluation im definierten Scope.
- **Critical tasks are evidence-backed:** Critical-Task-/High-Risk-Use-Szenarien entstehen aus Risk/Use Analysis, nicht aus einer pauschalen Checkliste.
- **Representative context matters:** User, Environment, Training, Interface/Baseline und Tasks müssen zur intended real-world use situation passen.
- **Submission content is market-specific:** FDA-/EU-/anderer Submission Content wird current-source-basiert abgeleitet; Usability-Evidence bleibt die gemeinsame Basis.

## Workflow

### 1. Use Specification fixieren

Erfasse Intended Users, User Characteristics, Use Environment, Operating Principle, User Interface Elements, Use Scenarios, Training/Labeling Assumptions, Variants und Baseline.

### 2. Current Standard/Market Context laden

Verifiziere aktuelle IEC-62366-1-Ausgabe/Amendments sowie marktbezogene Human-Factors-/Usability-Guidance und Submission-Information mit `asOf`. Normtext wird nur aus autorisierter Quelle angewendet.

### 3. Use-Related Risk Map

Mappe User Tasks/Interactions auf Use Errors, hazardous situations, Harm/Risk References, Risk Controls, Information for Safety und Evidence. Abnormal-use observations können erfasst werden, werden aber nicht still in die normale Use-Risk-Methodik gepresst.

### 4. Formative Evidence bewerten

Dokumentiere Design Questions, Participants/Context, Findings, Design Changes, Risk/Requirement Links und Closure Evidence. Formative Erfolgsmuster ersetzen keine erforderliche abschließende Evaluation.

### 5. Summative-/Validation Need ableiten

Definiere Critical Tasks/Scenarios, Representative Users/Environment/Training, Device/UI Baseline, Success/Failure Criteria, Data Capture und Analysis Rationale **vor** Ergebnisbewertung. Prüfe, ob bestehende Evidence wiederverwendbar ist oder zusätzliche Evaluation nötig ist.

### 6. Routing

- Use-related Risk → `medical-device-risk-management-iso14971`
- UI/Design Change → `design-control-traceability` / `design-change-regulatory-impact`
- Software UI → `iec62304-software-lifecycle`
- Labeling/Training → `medical-device-labeling-ifu`
- FDA Submission Content → FDA Front Door/eSTAR nach aktuellem Guidance Scope
- Claims Conflict → `regulatory-claims-consistency`
- Postmarket Use Signal → `fda-complaint-mdr-reportability` / `ivdr-pms-vigilance`.

## Output-Verträge

`usability-engineering-assessment.json` enthält Use Specification, Current Standard/Guidance Context, UI/Baseline, Formative/Summative Evidence State, Critical Tasks, Representative Context, Design/Risk Links und `asOf`.

`use-related-risk-evidence.json` enthält Task/Scenario, Use Error/Hazard/Risk Reference, Control, Design/Labeling Implementation, Verification/Validation Evidence und Residual Gap.

`usability-evidence-gaps.json` enthält Gap ID, Use Scenario/Task, Risk/Requirement Link, Missing Evidence/Decision, Impact, Next Skill und Closure Evidence.

## Memory Path

Persistenzwürdig sind validierte Use-Specification-/Critical-Task-Heuristiken, abstrahierte formative/summative Designmuster und wiederverwendbare Representative-Context-Prüfregeln. Konkrete Participant-/User-Daten, unreleased UI Designs, Testaufzeichnungen, aktuelle Critical-Task Decisions, offene Use Errors und aktuelle Submission States bleiben run-only bzw. in kontrollierten Study/Engineering/Quality Records. Norm-/Guidance-Kandidaten benötigen `sourceRefs`, `asOf` und `reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- **Users uses environments first** umgesetzt ist,
- Use-related Risk auf ISO14971 referenziert statt dupliziert wird,
- **Formative and summative serve different decisions** eingehalten wird,
- Critical Tasks/Risk Scenarios evidenzbasiert sind,
- Representative Users/Environment/Baseline geprüft werden,
- Evaluation Criteria nicht post-hoc angepasst werden,
- marktbezogene Submission-Anforderungen current-source-basiert sind,
- konkrete Participant/UI/Test-/Submission-Zustände nicht in globales dauerhaftes Memory gelangen.
