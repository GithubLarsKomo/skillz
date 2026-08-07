---
name: ivdr-pms-vigilance
description: Bewertet IVDR-Post-Market-Signale und Vigilance-Fragen evidenzgebunden, zeitkritisch und mit klarer Rückkopplung in Risk, CAPA, PMPF und Performance Evaluation.
userFacing: true
implicitInvocation: false
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - regulated-product-context
  - medical-device-risk-management-iso14971
  - two-axis-compliance-review
  - regulatory-evidence-traceability
  - mdcg-guidance-navigator
outputs:
  - ivdr-pms-assessment.json
  - vigilance-decision-log.json
  - trend-signal-set.json
lastEvaluated: 2026-08-07
---

# IVDR PMS and Vigilance

## Zweck und Grenze

Dieser Skill strukturiert IVDR-Post-Market-Surveillance-Signale und Vigilance-/Reportability-Fragen. Er verbindet Feldinformationen mit Product Context, Risk Management, regulatorischer Evidenz und aktuellen Melde-/Guidance-Anforderungen und erzeugt nachvollziehbare Entscheidungen, Gaps und Eskalationen.

Er führt **keine externe Behördenmeldung autonom aus**, ersetzt keine CAPA/Ursachenanalyse und ist kein generischer Complaint-Handling-Skill. Wegen potenziell zeitkritischer regulatorischer Entscheidungen ist die automatische implizite Invocation deaktiviert.

## Kernprinzipien

- Melde-/Vigilance-Fragen werden fallbezogen gegen aktuelle offizielle Anforderungen geprüft; Fristen und Definitionen werden nicht als statische Zahlen im Skill konserviert.
- Unvollständige Fakten sind kein Grund, potenziell zeitkritische regulatorische Bewertung aufzuschieben: Unsicherheit und nächste sichere Aktion werden explizit dokumentiert.
- Complaint, Incident, Serious-Incident-Hypothese, Trend, FSCA-/Field-Action-Frage, Nonconformity und Performance Signal bleiben getrennte Klassifikationen, bis Evidenz eine Verbindung trägt.
- PMS aggregiert Datenquellen; Risk Management, PMPF, Performance Evaluation und CAPA behalten ihre jeweilige Fachlogik.
- Jede regulatorisch relevante Entscheidung besitzt Source/Requirement References, `asOf`, Facts/Unknowns und eine Authority/Human Boundary.

## Workflow

### 1. Signal Intake normalisieren

Erfasse Quelle, Zeitpunkt, Produkt/Version/Lot soweit relevant, Markt, Nutzungskontext, Ereignisbeschreibung, Outcome/Impact, bekannte Patient-/User-Auswirkungen, technische Fakten und Unknowns. Personenbezogene Daten werden minimiert und nicht unnötig in Artefakte kopiert.

### 2. Current Requirements laden

Nutze `mdcg-guidance-navigator` und autoritative Rechtsquellen für die zum Fallzeitpunkt anwendbaren Definitionen, Meldewege, Fristen, Trend-/Vigilance-Regeln und Übergangsbedingungen. Historische Guidance wird nur verwendet, wenn sie für den Ereigniszeitpunkt relevant ist.

### 3. Signal klassifizieren

Bewerte getrennt:

- Complaint/Feedback,
- Performance- oder Safety-Signal,
- Incident-/Serious-Incident-Potenzial,
- Trend-Hypothese,
- Field-Safety-/Corrective-Action-Frage,
- bekannte Nonconformity/Systemursache,
- fehlende Fakten/Verification Need.

Status mindestens `not-indicated|possible|likely|confirmed|not-reportable-on-current-evidence|reportability-unresolved|human-authority-action-required`.

### 4. Zeitkritik und Stop Conditions bestimmen

Bei möglicher Meldepflicht oder anderer zeitkritischer Pflicht wird der relevante Human/Regulatory Owner sofort sichtbar gemacht. Fehlende Detailinformationen dürfen notwendige Eskalation nicht still blockieren. Der Skill behauptet keine Meldung, solange externe Ausführung nicht verifiziert ist.

### 5. Evidence/Risk-Linkage

Verknüpfe die Entscheidung über `regulatory-evidence-traceability` mit aktuellen Requirements und aktualisiere bei Bedarf `medical-device-risk-management-iso14971`. Eine neue Gefahr/Risikohöhe oder ein neuer Failure Mode wird nicht nur im Vigilance-Log belassen.

### 6. Lifecycle-Routing

- Performance-Frage → `ivdr-performance-evaluation` / `ivdr-pmpf`
- Trend-/PMS-Überwachung → fortgesetztes PMS mit definiertem Trigger
- systemische Nonconformity → `medical-device-capa`
- unklare Ursache → `evidence-based-causal-investigation`
- externe Human-/Authority-Aktion → `human-procedure-wizard` bzw. verantwortliche Regulatory-Funktion
- kontrollierte Records → `controlled-quality-documentation`

## Output-Verträge

`ivdr-pms-assessment.json` enthält Scope, Datenquellen, Signalübersicht, Product/Risk Context, Trend-/Performance-Bewertung, offene Gaps, Re-evaluation Trigger und `asOf`.

`vigilance-decision-log.json` enthält pro Fall/Entscheidung Facts, Unknowns, Current Requirement References, Klassifikation, Reportability State, Time-Criticality, Human Owner, Decision Evidence, externe Action State und Follow-up Trigger.

`trend-signal-set.json` enthält normalisierte Signaldefinition, Baseline/Denominator soweit verfügbar, Beobachtungen, Unsicherheit, Trigger/Threshold-Logik, Confidence und Next Action. Ein statistischer Trend wird nicht behauptet, wenn Datenbasis oder Nenner unzureichend sind.

## Memory Path

Persistenzwürdig sind validierte produktspezifische Signaldefinitionen, stabile Surveillance-Grenzen und bestätigte wiederverwendbare Entscheidungsheuristiken. Einzelne Beschwerden, Patienten-/Anwenderdaten, laufende Reportability-Fälle, aktuelle Meldefrist-Snapshots, momentane Trendwerte und offene Investigation-Fakten bleiben run-only. Kandidaten benötigen `sourceRefs`; regulatorische Learnings zusätzlich `asOf` und `reviewAfter`. Übergib nur abstrahierte, nicht-sensitive `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- aktuelle Requirements statt erinnerter Fristen/Definitionen verwendet werden,
- Facts, Unknowns und regulatorische Interpretation getrennt sind,
- potenziell zeitkritische Fälle nicht auf vollständige Ursachenklärung warten,
- externe Meldung/Behördenaktion nicht simuliert wird,
- Risk/PMPF/Performance/CAPA-Rückkopplung korrekt geroutet ist,
- Trends ohne ausreichende Datenbasis nicht behauptet werden,
- einzelne Fälle oder personenbezogene Daten nicht in dauerhaftes Memory gelangen.
