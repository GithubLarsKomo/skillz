---
name: ivdr-field-safety-corrective-action
description: Überführt eine IVDR-Vigilance-/Field-Action-Frage in eine evidenzgebundene FSCA-Entscheidung, behördliche Sequenz, Field-Safety-Notice-Anforderungen und kontrollierte Execution-Handoffs, ohne Authority- oder Customer-Aktionen zu simulieren.
userFacing: true
implicitInvocation: false
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - ivdr-pms-vigilance
  - medical-device-risk-management-iso14971
  - medical-device-capa
  - regulatory-evidence-traceability
  - mdcg-guidance-navigator
  - controlled-quality-documentation
outputs:
  - ivdr-fsca-assessment.json
  - ivdr-fsca-regulatory-plan.json
  - field-safety-notice-content.json
lastEvaluated: 2026-08-08
---

# IVDR Field Safety Corrective Action

## Zweck und Grenze

Dieser Skill besitzt den **EU-/IVDR-spezifischen Übergang von einer Vigilance-/Field-Action-Frage zu einer kontrollierten Field Safety Corrective Action (FSCA)**. Er bewertet, ob die geplante oder bereits eingeleitete Feldmaßnahme eine FSCA darstellt, fixiert Scope und regulatorische Sequenz, strukturiert die behördliche Reporting-/Coordination-Evidence und erzeugt einen kontrollierten Content-Input für die Field Safety Notice (FSN).

Er ersetzt weder `ivdr-pms-vigilance`, CAPA/RCA, Risk Management, Customer-/Distributor-Kommunikation noch die physische Durchführung der Maßnahme. Er reicht **keine** Meldung autonom ein, sendet **keine** FSN und behauptet keine Zustimmung, Koordination oder Closure durch eine Behörde ohne verifizierte externe Evidenz.

## Regulatorischer Rahmen

Aktuelle offizielle Quellen werden pro Fall über `mdcg-guidance-navigator` und `regulatory-evidence-traceability` aufgelöst. Besonders relevant sind die jeweils geltende konsolidierte IVDR-Fassung, aktuelle MDCG-Vigilance-Guidance und die aktuellen PMSV-Reporting-Forms/Templates.

Der Skill konserviert keine veraltbaren Portal-, Formularversions- oder Verfahrensannahmen als harte Wahrheit. Zeitabhängige Requirements erhalten `sourceRef`, `asOf` und gegebenenfalls `reviewAfter`.

## Kernprinzipien

- **FSCA ≠ CAPA:** eine CAPA kann Ursache und systemische Korrektur adressieren; die FSCA ist die konkrete Feldmaßnahme zur Verhinderung oder Reduktion des Risikos eines Serious Incident bei bereits bereitgestellten Devices.
- **FSCA ≠ Serious Incident:** eine FSCA kann eine eigene Vigilance-Pflicht sein und wird nicht aus dem Incident-State abgeleitet oder mit ihm verschmolzen.
- **Field action facts first:** geplante/tatsächliche Maßnahme, betroffene Devices, technischer/medizinischer Grund, Markt-/Distributionsscope und Initiation-/Decision-Timeline müssen getrennt von Interpretation dokumentiert werden.
- **Advance reporting unless urgency:** soweit die aktuelle IVDR-Anforderung dies verlangt, wird eine nicht dringliche FSCA vor ihrer Durchführung an die zuständige Behörde berichtet; bei Dringlichkeit wird notwendige Safety Action nicht blockiert und die Abweichung/Sequenz evidenzgebunden dokumentiert.
- **Third-country action can matter in EU:** eine Feldmaßnahme in einem Drittland wird auf EU-FSCA-Relevanz geprüft, wenn dasselbe Device rechtmäßig im Unionsmarkt bereitgestellt wird und der Grund nicht ausschließlich die Drittland-Ausführung betrifft.
- **FSN is a safety control, not marketing copy:** Inhalt darf Risiko nicht herunterspielen, muss Device/Manufacturer eindeutig identifizieren und klar sagen, welche Handlungen Nutzer ausführen müssen.
- **Authority comment state is explicit:** `drafted|submitted-for-comment|comments-received|approved-by-internal-owner|released|unknown` werden getrennt; kein State wird ohne Evidence hochgestuft.
- **Country consistency by default:** unterschiedliche nationale FSN-Inhalte benötigen dokumentierte rechtliche/behördliche oder sachliche Begründung; Übersetzungen sind keine Gelegenheit zur Risikoveränderung.
- **No closure by communication:** Versand einer FSN schließt weder FSCA, Vigilance, CAPA noch Risk/PMS.
- **New facts reopen scope:** neue Lots, Länder, Varianten, Failure Modes, Outcomes oder Distributionsdaten können die FSCA-Version, den Regulatory Scope und die Notice Population erweitern.

## Trigger

Nutze den Skill, wenn `ivdr-pms-vigilance` eine `Field-Safety-/Corrective-Action-Frage` als `possible|likely|confirmed|human-authority-action-required` markiert oder wenn bereits eine technische/medizinische Feldmaßnahme für ein in der EU bereitgestelltes IVD geplant/eingeleitet wurde.

Eine bereits ausgeführte dringliche Maßnahme ist kein Grund, den Skill zu überspringen; sie erzeugt vielmehr einen expliziten retrospective/urgent regulatory sequencing state.

## Workflow

### 1. Vigilance- und Action-Provenance fixieren

Konsumiere soweit vorhanden:

- `vigilance-decision-log.json`,
- `ivdr-pms-assessment.json`,
- Risk-/CAPA-/Investigation-References,
- geplante oder bereits ausgeführte Field Action,
- betroffene Device-/UDI-/Lot-/Serial-/Version-Scope-Daten,
- Distribution/Market Scope,
- Third-Country-Action-Information,
- Decision-/Initiation-/Execution-Timestamps,
- Prior FSCA/FSN Versions.

Trenne strikt `facts`, `unknowns`, `riskInterpretation`, `regulatoryInterpretation`, `externalActionState`.

### 2. FSCA-Qualifikation bewerten

Bewerte die Feldmaßnahme current-source-basiert als mindestens:

- `not-a-field-action`,
- `field-action-not-fsca-on-current-evidence`,
- `possible-fsca`,
- `fsca-confirmed`,
- `fsca-scope-uncertain`,
- `urgent-fsca-action`,
- `human-regulatory-decision-required`.

Dokumentiere technische/medizinische Gründe, Risikobezug und Device-Market-Bezug. Eine interne Bezeichnung wie `service campaign`, `quality improvement`, `customer advisory`, `software patch` oder `voluntary action` entscheidet die FSCA-Qualifikation nicht.

### 3. Scope versionieren

Erzeuge eine versionierte Scope-Sicht mit:

- Device/Variant/Software/Firmware,
- Basic UDI-DI/UDI soweit anwendbar/verfügbar,
- Lots/Serials/Batches,
- Länder/Member States,
- Direct/Indirect Distribution Population,
- bereits korrigierte/entfernte Devices,
- Known Downstream Distribution,
- Third-Country Parallel Actions,
- Scope Unknowns.

Scope-Erweiterungen überschreiben keine frühere Version. Jede Erweiterung erhält `newMaterialFacts`, `effectiveFrom`, `sourceRefs` und Regulatory-Reassessment-State.

### 4. Urgency und regulatorische Sequenz bestimmen

Bestimme getrennt:

- `safetyActionUrgency`,
- `authorityReportingState`,
- `reportBeforeExecutionExpected`,
- `executionAlreadyStarted`,
- `urgentExceptionRationale`,
- `authorityCommentRequiredBeforeFSNRelease`,
- `currentSubmissionProcessRef`.

Eine dringliche Maßnahme darf nicht auf Root Cause, vollständige Distribution Data, finale CAPA oder administrative Vollständigkeit warten. Umgekehrt darf nicht dringliche Ausführung eine erforderliche behördliche Vorabsequenz nicht still umgehen.

### 5. FSN-Content Package erzeugen

`field-safety-notice-content.json` enthält mindestens:

- eindeutige Herstelleridentifikation einschließlich SRN soweit vorhanden/anwendbar,
- eindeutige Device-Identifikation einschließlich relevanter UDI-Daten soweit anwendbar,
- betroffenen Scope,
- klare technische/medizinische Begründung,
- zugehöriges Risiko für Patient/User/andere Personen ohne Verharmlosung,
- konkrete erforderliche Handlungen des Empfängers,
- Fristen/Stop-Use/Quarantine/Return/Correction Instructions soweit aus dem freigegebenen Action Plan abgeleitet,
- Weiterleitungs-/Downstream-Instruktionen soweit erforderlich,
- Kontakt-/Response-Anforderung soweit kontrolliert definiert,
- Master-Language-Version und Translation-Control-State,
- Authority-Comment-/Release-State.

Der Skill erzeugt **Content**, aber kein behauptetes Senden/Empfangen.

### 6. Multi-Member-State-Konsistenz kontrollieren

Für jede nationale Version dokumentiere:

- Sprache,
- Master Content Version,
- Übersetzungs-/Review-Evidence,
- landesspezifische Pflichtabweichung,
- Authority Comment Reference,
- Release Version.

Risikoaussage, Device Scope und User Action dürfen nicht aus kommerziellen Gründen abgeschwächt oder widersprüchlich lokalisiert werden.

### 7. Execution-Handoff erzeugen

Übergib freigegebene/zulässige Kommunikations- und Scope-Daten an `medical-device-field-action-communication`.

Der Handoff enthält:

- `fieldActionId`,
- Jurisdiction = `EU-IVDR`,
- FSCA Decision Version,
- Authority/FSN Release Preconditions,
- Recipient Scope Basis,
- Master Notice Content Reference,
- Required Languages,
- Due/urgency states,
- Distribution unknowns,
- Evidence requirements.

Externe Aktionen werden anschließend über autorisierte Systeme/Menschen und bei Bedarf `human-procedure-wizard` ausgeführt und verifiziert.

### 8. Rückkopplung offen halten

Neue Incident-/Complaint-/Distribution-/Execution-Fakten können zurück routen zu:

- `ivdr-pms-vigilance` für Reportability/Reassessment,
- `medical-device-risk-management-iso14971`,
- `medical-device-capa`,
- `medical-device-pms-system`,
- Performance Evaluation/PMPF soweit betroffen.

Eine bereits freigegebene FSN immunisiert die Entscheidung nicht gegen neue Evidenz.

## Output-Verträge

`ivdr-fsca-assessment.json` enthält Source References, Vigilance Decision Reference, Action Facts, FSCA State, Scope Version, Urgency, Third-Country-Relevance, Facts/Unknowns, Requirement References, Human Owner und `asOf`.

`ivdr-fsca-regulatory-plan.json` enthält Authority Reporting Sequence, required pre-/post-action states, current submission/process references, Member-State Coordination State, FSN Authority-Comment State, execution stop/bypass conditions und follow-up triggers.

`field-safety-notice-content.json` enthält kontrollierten Master Content, Device/Manufacturer Identity, Risk Statement, Required User Actions, Translation/Member-State Versions, Authority-Comment/Release State und Source References. Es enthält keinen erfundenen `sent|delivered`-State.

## Memory Path

Persistenzwürdig sind abstrahierte FSCA-Qualifikationsheuristiken, stabile Scope-/FSN-Content-Patterns und validierte EU-Field-Action-Handoff-Muster. Konkrete Incident-/Complaint-/Patient-/Customer-/Device-/UDI-/Lot-/Country-Daten, Authority-Kommunikation, aktuelle Deadlines, Notice-Versionen, Recipient Lists und offene FSCA-Stati bleiben run-only oder kontrollierte Regulatory/Quality Records.

Regulatorische Memory Candidates benötigen `sourceRefs`, `asOf` und bei veränderlichen Verfahren `reviewAfter`; Übergabe ausschließlich als abstrahierter `memory-candidate-handoff-v1` an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- FSCA, Serious Incident, CAPA und allgemeine Field Action getrennte Zustände bleiben,
- aktuelle offizielle Requirements/Forms/Processes statt erinnerter Workflowdetails verwendet werden,
- eine dringliche Safety Action nicht auf administrative Vollständigkeit oder Root Cause wartet,
- eine nicht dringliche FSCA eine erforderliche Vorabmeldung/-koordination nicht still umgeht,
- Drittlandmaßnahmen auf EU-Relevanz geprüft werden,
- Device/Manufacturer/Scope in der FSN eindeutig und evidenzgebunden sind,
- Risiko nicht verharmlost und User Actions eindeutig beschrieben werden,
- Member-State-/Sprachversionen auf kontrollierten Master Content zurückführbar sind,
- Authority Comment/Submission/Acceptance/Closure niemals ohne externe Evidence behauptet wird,
- FSN Release nicht als FSCA-/Vigilance-/CAPA-Closure gilt,
- Scope-Erweiterungen und neue materielle Fakten versioniert Reassessment auslösen,
- konkrete Fall-/Recipient-/Authority-Daten nicht in globales dauerhaftes Memory gelangen.
