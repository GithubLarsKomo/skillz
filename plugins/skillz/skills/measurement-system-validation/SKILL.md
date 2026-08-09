---
name: measurement-system-validation
description: Bewertet Medical-Device-Mess- und Prüfsysteme risikobasiert auf Eignung, Kalibrierung, Auflösung, Bias, Stabilität und Wiederhol-/Reproduzierbarkeit.
---

# Measurement System Validation for Medical Devices

## Zweck und Grenze

Dieser Skill bewertet, ob Mess-, Prüf-, Inspektions- oder Monitoring-Systeme in Medical-Device-/IVD-Prozessen für ihren vorgesehenen Entscheidungszweck geeignet sind. Er verbindet Messaufgabe, Toleranz/Decision Limit, Risiko, Kalibrier-/Traceability-Evidenz, Auflösung, Bias/Agreement, Stabilität sowie Wiederhol- und Reproduzierbarkeit zu einer belastbaren Eignungsentscheidung.

Er ersetzt **nicht** die analytische Performance Evaluation eines IVD, keine Produkt-Verifikation/-Validierung und kein allgemeines Kalibrierprogramm. Produktbezogene analytische Leistungsmerkmale bleiben bei `ivdr-analytical-performance`; QMS-Kalibrier-/Equipment-Prozesse bleiben bei `medical-device-qms-iso13485`.

## Kernprinzipien

- **Calibration ≠ fitness for use:** gültige Kalibrierung belegt Rückführung/Status, aber nicht automatisch ausreichende Messfähigkeit für die konkrete Toleranz oder Entscheidung.
- **Decision context first:** Messgröße, Einheit, Range, Toleranz/Decision Limit, Fehlklassifikationsrisiko und Einsatzbedingungen werden vor der Study fixiert.
- **Risk-based MSA:** Tiefe der Untersuchung folgt Produkt-/Prozess-/Patient-/Compliance-Risiko und der Kritikalität der Messentscheidung.
- **Fit-for-purpose characteristics:** Auflösung/Discrimination, Bias/Agreement, Linearität, Stabilität, Repeatability/Reproducibility und Unsicherheit werden nur soweit für das konkrete System relevant bewertet; keine dogmatische Kennzahlenliste.
- **Representative variation:** Operatoren, Instrumente, Lots, Fixtures, Software, Umgebungsbedingungen, Range und reale Prozessvariation werden risikobasiert berücksichtigt.
- **Method and system stay distinct:** unzureichende Prüfmethode, ungeeignete Proben/Referenzen oder instabile Software dürfen nicht als reines Geräteproblem maskiert werden.

## Workflow

### 1. Measurement Decision fixieren

Erfasse Measurement System ID/Version, Messgröße/Resultat, Intended Use der Messung, Product/Process Scope, Toleranz-/Specification-/Decision Limits, relevante Range, erwartete Variation und Konsequenz einer falschen Accept/Reject-Entscheidung.

### 2. Existing Evidence indexieren

Referenziere Calibration/Traceability, Equipment Qualification, Method/Software Version, Reference Standards/Materials, Maintenance, Environmental Controls, historische QC/Monitoring-Daten und bekannte Deviations. Ein Calibration Certificate schließt keine Eignungsprüfung.

### 3. Measurement-Risk und Study Need ableiten

Bewerte, welche Fehlerquellen die Entscheidung beeinflussen können: Resolution, Bias, Drift, Operator, Instrument, Fixture, Sample Preparation, Lot, Environment, Software/Algorithm, Range/Linearity und Method Agreement. Leite daraus `existing-evidence-sufficient|targeted-study|required-study|method-redesign-needed|unknown` ab.

### 4. Study Design

Definiere vor Durchführung geeignete Samples/References, Range, Operators/Instruments/Runs, Repeats, Randomization/Order soweit relevant, Environmental/Use Conditions, Acceptance Criteria und Analysis Plan. Kriterien werden nicht nach Ergebnislage verschoben.

Mögliche Evidence Patterns umfassen je nach Messaufgabe beispielsweise:
- Resolution/Discrimination Check,
- Bias oder Method Agreement,
- Linearity/Range,
- Stability/Drift,
- Repeatability/Reproducibility bzw. Varianzkomponenten,
- Classification/Attribute Agreement,
- Measurement Uncertainty oder Guard-Band-/Decision-Rule-Analyse.

Nicht jede Messaufgabe benötigt alle Patterns.

### 5. Evidence auswerten

Bewerte Ergebnisse gegen vorab definierte Criteria und die tatsächliche Messentscheidung. Trenne statistische Signifikanz von praktischer Eignung. Berücksichtige, ob Measurement Variation im Verhältnis zur relevanten Produkt-/Prozessvariation bzw. Toleranz akzeptabel ist.

### 6. Gap und Routing

- QMS-/Calibration-/Maintenance-Gap → `medical-device-qms-iso13485`
- Process Validation Impact → `process-validation-iq-oq-pq`
- analytische IVD-Performance → `ivdr-analytical-performance`
- Design-/Regulatory Change → `design-change-regulatory-impact`
- systemische Ursache/CAPA → `medical-device-capa` / `evidence-based-causal-investigation`
- kontrollierte Protocols/Reports/Records → `controlled-quality-documentation`.

## Output-Verträge

`measurement-system-assessment.json` enthält Measurement Decision Context, System/Method Version, Calibration/Traceability Evidence, Risk Factors, Needed Characteristics, Overall Fitness State, Gaps und Routing.

`measurement-capability-study.json` enthält Study Design, Samples/References, Factors/Runs/Repeats, Acceptance Criteria, Analysis Plan, Result References und Interpretation.

`measurement-evidence-gaps.json` enthält Gap ID, Failure Mode/Decision Impact, Missing Evidence, Owner/Next Skill, Stop Condition und Re-evaluation Trigger.

## Memory Path

Persistenzwürdig sind validierte Measurement-System-Heuristiken, wiederverwendbare Study-Design-/Acceptance-Prinzipien und abstrahierte MSA-/Decision-Rule-Patterns. Konkrete Instrument IDs, Calibration Results, Produktions-/Patientendaten, aktuelle Bias-/R&R-/Uncertainty-Ergebnisse, offene Deviations/CAPA und vertrauliche Spezifikationsgrenzen bleiben run-only bzw. in kontrollierten Quality/Lab/Manufacturing Records. Kandidaten benötigen `sourceRefs`; technologie-/prozessabhängige Learnings zusätzlich `asOf`/`reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- Measurement Decision und relevante Toleranz/Range vor der Eignungsbewertung fixiert sind,
- Kalibrierung nicht mit Fitness for Use gleichgesetzt wird,
- Study Tiefe und Variation risikobasiert statt schematisch gewählt werden,
- Acceptance Criteria vor der Auswertung definiert sind,
- praktische Entscheidungsfähigkeit statt nur statistischer Signifikanz bewertet wird,
- Produkt-Analytical-Performance und Measurement-System-Eignung nicht vermischt werden,
- konkrete Mess-/Produktionszustände nicht in globales dauerhaftes Memory gelangen.
