---
name: fda-de-novo-special-controls
description: Entwickelt vorgeschlagene FDA-De-Novo-Special-Controls aus Risiko- und Evidenzlücken und trennt interne Control-Hypothesen strikt von später von FDA etablierten Controls.
userFacing: true
implicitInvocation: false
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - fda-de-novo-strategy
  - medical-device-risk-management-iso14971
  - regulatory-evidence-traceability
outputs:
  - special-controls-matrix.json
  - de-novo-risk-control-rationale.md
lastEvaluated: 2026-08-07
---

# FDA De Novo Special Controls

## Zweck und Grenze

Dieser Skill entwickelt **vorgeschlagene** Special Controls für eine De-Novo-Strategie aus Risks, Failure Modes, Claims, vorhandenen General Controls und Evidenzlücken. Er strukturiert, welche zusätzlichen Controls eine reasonable assurance of safety and effectiveness für einen vorgeschlagenen Class-II-Device-Type unterstützen könnten.

Er etabliert keine regulatorisch gültigen Special Controls. Solche Controls entstehen erst durch FDA-Entscheidung/Classification Regulation bzw. andere autoritative FDA-Aktion. Der Skill ersetzt weder Risk Management noch Standardsauswahl oder Submission Assembly.

## Kernprinzipien

- Jeder proposed Special Control besitzt einen konkreten Risk-/Failure-/Performance-Link.
- Controls sind Anforderungen/Mechanismen, nicht bloße Testnamen oder Dokumenttitel.
- Für jeden Control werden Verification/Evidence, Pass-/Decision Logic und residuale Unsicherheit beschrieben.
- Bestehende General Controls, Standards, Labeling, Performance Testing, Software/Cybersecurity-, Usability-, Clinical- oder Postmarket-Controls werden nur soweit relevant als Mechanismen genutzt.
- Ein vorgeschlagener Control wird nie als „FDA required special control“ bezeichnet, solange keine passende autoritative FDA-Quelle dies für den Device Type etabliert.
- Wenn ein Risk trotz plausiblem Control-Set nicht ausreichend beherrschbar erscheint, wird die De-Novo-Class-II-Hypothese zurück an Strategy eskaliert.

## Workflow

### 1. Risk-/Control-Baseline übernehmen

Übernimm Hazards, harms, Failure Modes, bestehende Risk Controls und De-Novo-Gaps aus `fda-de-novo-strategy` und `medical-device-risk-management-iso14971`.

### 2. Regulatory-Control-Layer trennen

Unterscheide:

- bereits anwendbare General Controls,
- vorhandene device-type-spezifische FDA-Anforderungen/Standards,
- interne vorgeschlagene Special Controls,
- Evidenz-/Verification-Aktivitäten,
- Postmarket-/Labeling-/Training-Mechanismen.

Diese Kategorien dürfen nicht miteinander vermischt werden.

### 3. Proposed Special Controls formulieren

Jeder Vorschlag enthält mindestens:

- Control ID,
- Risk/Failure/Claim Link,
- Control Objective,
- normative oder funktionale Control Formulierung,
- Verification/Evidence Method,
- Acceptance/Decision Logic,
- Residual Uncertainty,
- Applicable Device Scope,
- Source/Supporting Evidence.

### 4. Sufficiency prüfen

Bewerte, ob das gesamte proposed Control Set die zentralen identifizierten Risks nachvollziehbar adressiert. Status mindestens `plausibly-sufficient|partial|insufficient|unknown`. Eine positive interne Bewertung ist keine FDA-Controls-Entscheidung.

### 5. Redundanz und Übersteuerung prüfen

Entferne doppelte Controls, die denselben Risk Mechanism ohne zusätzlichen Nutzen abbilden. Vermeide unnötig produktspezifische Anforderungen, wenn ein funktionaler Control Objective die Device-Type-Ebene besser beschreibt.

### 6. Feedback-/Evidence-Gaps routen

Unklare Control-Akzeptanz oder Device-Type-Ebene → `fda-qsub-strategy`.
Fehlende Verification-/Performance-Evidence → zuständiger Engineering-/Clinical-Skill.
Unbeherrschte Risk Story → `fda-de-novo-strategy` und Risk Management.

## Output-Verträge

`special-controls-matrix.json` enthält Control IDs, Risk/Claim Links, Control Objectives, proposed Requirements, Evidence/Verification, Decision Logic, Residual Uncertainty, Scope, Status und Source References.

`de-novo-risk-control-rationale.md` erklärt, wie General Controls und proposed Special Controls gemeinsam die interne Class-II-/De-Novo-Hypothese tragen oder warum sie dies noch nicht tun.

## Downstream

Primäre Consumer sind `fda-de-novo-strategy`, `fda-qsub-strategy` und später `fda-estar-submission-builder`. Nach einem tatsächlichen FDA-De-Novo-Grant müssen die etablierten Classification-/Special-Control-Texte als neue autoritative Evidenz zurückgeführt und interne Vorschläge entsprechend superseded werden.

## Memory Path

Persistenzwürdig sind validierte Risk-to-Control-Mappings, wiederverwendbare funktionale Control-Patterns und bestätigte Verification-Heuristiken. Aktuelle proposed Special Controls, momentane Sufficiency-Bewertungen und unbestätigte FDA-Akzeptanzannahmen bleiben run-only. Nach FDA-Grant darf ein tatsächlich etablierter Control nur mit autoritativer Source Reference, `asOf` und Scope als Memory Candidate betrachtet werden. Übergib geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- jeder proposed Control auf Risk/Failure/Claim zurückgeführt ist,
- General Controls, proposed Special Controls und Verification getrennt bleiben,
- interne Vorschläge nicht als FDA-etablierte Special Controls ausgegeben werden,
- Control Sufficiency samt residualer Unsicherheit bewertet wird,
- fehlende Evidence/Feedback-Fragen an vorhandene Skills geroutet werden,
- unzureichende Control-Story die De-Novo-Hypothese zurückstellt statt sie zu kaschieren,
- aktuelle Control-Vorschläge nicht als dauerhaftes FDA-Faktum gespeichert werden.
