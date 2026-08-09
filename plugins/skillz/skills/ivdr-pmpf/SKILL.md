---
name: ivdr-pmpf
description: Plant und bewertet IVDR-Post-Market Performance Follow-up claim-, risiko- und evidenzgebunden und führt Signale in Performance Evaluation und Risikomanagement zurück.
---

# IVDR Post-Market Performance Follow-up

## Zweck und Grenze

Dieser Skill plant und bewertet Post-Market Performance Follow-up (PMPF) als Rückkopplung zur IVDR-Performance-Evaluation. Er übersetzt bekannte Restunsicherheiten, Claims, Risikofragen und Post-Market-Datenbedarfe in nachvollziehbare PMPF-Ziele und wertet daraus entstehende Evidenz/Signale aus.

Er ersetzt weder das allgemeine PMS-System noch Vigilance-/Reportability-Entscheidungen. Ob und in welchem Umfang PMPF erforderlich bzw. begründbar ist, wird gegen aktuelle IVDR-/MDCG-Quellen geprüft; historische Templates oder Guidance-Versionen werden nicht als zeitlos verbindlich vorausgesetzt.

## Kernprinzipien

- PMPF beginnt bei offenen Performance-/Risk-Fragen, nicht bei einer generischen Aktivitätenliste.
- Objectives, Claims, Datenquellen, Methoden, Akzeptanz-/Decision Rules und Review-Zeitpunkte sind rückverfolgbar.
- Routine-PMS-Daten können Input sein, ersetzen aber eine erforderliche gezielte PMPF-Frage nicht automatisch.
- Neue Signale aktualisieren Performance Evaluation und Risk Management; sie werden nicht nur in einem PMPF-Bericht archiviert.
- Eine Begründung für reduzierten oder nicht anwendbaren Follow-up-Umfang muss evidenzgebunden und gegen aktuelle Anforderungen geprüft sein.
- PMPF ist kein zweites PMS-, CAPA- oder Risk-System.

## Workflow

### 1. PMPF-Bedarf ableiten

Übernimm Claims, Performance-Evaluation-Gaps, Limitationen, Residual-Risk-Fragen und relevante Lifecycle-Annahmen. Verifiziere aktuelle Guidance/Requirements über `mdcg-guidance-navigator`.

### 2. Ziele und Fragen definieren

Jede PMPF-Aktivität besitzt eine konkrete Frage, Claim-/Risk-Verknüpfung, erwartete Information und Decision Rule. Vermeide Aktivitäten ohne benannten Erkenntnisgewinn.

### 3. Datenquellen und Methoden festlegen

Wähle geeignete reale Nutzungs-/Post-Market-Datenquellen, z. B. Literatur, Register/Datensätze, Anwenderfeedback, gezielte Follow-up-Studien oder andere zulässige Quellen. Provenance und Applicability werden über `regulatory-evidence-traceability` gesichert.

### 4. Plan erzeugen

`pmpf-plan.json` enthält Objectives, Claims/Risks, Methoden, Population/Setting soweit relevant, Quellen, Periodizität/Event Trigger, Decision Rules, Verantwortlichkeiten, externe Abhängigkeiten und Re-evaluation Trigger.

### 5. Ergebnisse auswerten

Bewerte neue Evidenz gegenüber Baseline und Decision Rules. Klassifiziere mindestens `no-material-change|supports-current-evaluation|new-signal|evidence-gap|requires-escalation|unknown`.

### 6. Lifecycle-Rückkopplung

- Performance-/Claim-Auswirkung → `ivdr-performance-evaluation`
- neue/änderte Gefährdung oder Residual Risk → `medical-device-risk-management-iso14971`
- breiter Post-Market-/Vigilance-Signalbedarf → `ivdr-pms-vigilance`
- Nonconformity/Systemursache → `medical-device-capa` / `evidence-based-causal-investigation`
- dokumentierte PMPF-Auswertung → `controlled-quality-documentation`

## Output-Verträge

`pmpf-plan.json` enthält Scope, Baseline, Objectives, Claim-/Risk-Links, Methoden, Datenquellen, Frequenz/Trigger, Decision Rules, Verantwortlichkeit, Current-Guidance-References und Review-Zeitpunkt.

`pmpf-evaluation-report.md` dokumentiert durchgeführte Aktivitäten, neue Evidenz, Abweichungen, Signalbewertung, Auswirkungen auf Performance/Risk und offene Actions.

`pmpf-signals.json` enthält Signal-ID, Source/Evidence References, Claim/Risk-Bezug, Signalstatus, Impact, Confidence, Next Skill/Action und Re-evaluation Trigger.

## Memory Path

Persistenzwürdig sind validierte PMPF-Designmuster, stabile produktspezifische Follow-up-Fragen und bestätigte Signal-/Decision-Heuristiken. Aktuelle Feldsignale, laufende Aktivitäten, einzelne Beschwerden/Fälle, momentane Performance-Schlussfolgerungen und ungeprüfte Trendhypothesen bleiben run-only. Kandidaten benötigen `sourceRefs`; regulatorisch/guidanceabhängige Learnings zusätzlich `asOf` und `reviewAfter`. Übergib geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; PMPF persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- jede PMPF-Aktivität auf eine konkrete Performance-/Risk-Frage zurückgeht,
- aktuelle Requirements/Guidance vor Scope-Entscheidungen geprüft wurden,
- Decision Rules und Lifecycle-Rückkopplung definiert sind,
- neue Signale Performance Evaluation/Risk Management tatsächlich adressieren,
- PMS/Vigilance/CAPA nicht dupliziert werden,
- Einzelereignisse und aktuelle Signale nicht als dauerhaftes Memory-Faktum gespeichert werden.
