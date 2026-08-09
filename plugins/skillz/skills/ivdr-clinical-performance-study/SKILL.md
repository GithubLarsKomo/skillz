---
name: ivdr-clinical-performance-study
description: Plant klinische IVD-Performance-Evidenz nach IVDR/ISO 20916 mit Risiko-, Bias-, Endpunkt- und Gap-Kontrolle.
---

# IVDR Clinical Performance Study

## Zweck und Grenze

Dieser Skill strukturiert die regulatorische Planung und Bewertung klinischer IVD-Performance-Evidenz. Er entscheidet zuerst, ob bestehende klinische Evidenz für den konkreten Claim ausreicht oder ob eine zusätzliche Performance Study erforderlich ist. Wird eine Studie benötigt, definiert er ein evidenz- und risikogebundenes Design nach IVDR und anwendbaren aktuellen Guidance-/ISO-20916-Prinzipien.

Er ist kein generisches Studienmanagement, ersetzt keine Ethik-/Behörden-/Sponsorentscheidung und führt keine Patientenrekrutierung oder operative Studienhandlung autonom aus.

## Kernprinzipien

- Die Frage lautet zuerst `welche klinische Performance muss für welchen Claim belegt werden?`, nicht `welche Studie wollen wir durchführen?`.
- Existing Evidence wird vor einer neuen Studie bewertet.
- Intended Purpose, Population, Specimen, Setting, Comparator/Reference Method, Endpunkte und Entscheidungsgrenzen werden explizit fixiert.
- Selection-, Spectrum-, Verification-, Review- und Handling-Bias werden aktiv gesucht und nicht erst nach Ergebnisabweichungen diskutiert.
- Sample Size und statistisches Design werden aus Endpunkten, erwarteter Performance, Präzisionsziel, Subgruppen und Decision Rules abgeleitet.
- Klinische Risiken und potenzielle Fehlklassifikationen werden an `medical-device-risk-management-iso14971` gekoppelt, nicht in einem separaten Risiko-Register dupliziert.
- Aktuelle MDCG-/EC-Guidance wird über `mdcg-guidance-navigator` geprüft; statische Versionsannahmen sind unzulässig.

## Workflow

### 1. Evidence Need fixieren

Übernimm Product Context und Performance Claims. Definiere pro Claim die klinische Performance-Frage sowie die minimal erforderliche Evidenz.

### 2. Existing Evidence bewerten

Inventarisiere vorhandene klinische Performance-Daten, frühere Studien, Routine-/Archivdaten, Literatur und externe Datensätze. Klassifiziere `sufficient|potentially-sufficient|insufficient|not-applicable|unknown` mit Begründung.

### 3. Study-Need-Entscheidung

Wenn bestehende Evidenz genügt, erzeuge trotzdem `clinical-performance-evidence.json` mit Traceability und dokumentiere `studyNeed: no-new-study`. Bei Lücken wird `studyNeed: new-study|additional-study|targeted-study` begründet. Eine neue Studie ist kein automatischer Default.

### 4. Design definieren

Falls Studie erforderlich, dokumentiere mindestens:

- Objective/Hypothesis,
- Intended-Purpose-Claim,
- Population und Ein-/Ausschlusskriterien,
- Specimen und Handling,
- Setting/Sites,
- Index Test und Comparator/Reference Standard,
- Endpunkte und Analysepopulationen,
- Blinding/Randomisierung soweit relevant,
- Bias Controls,
- Sample-Size-/Präzisionslogik,
- Subgruppen,
- Missing-/Invalid-Data-Regeln,
- statistischen Analyseplan,
- Safety/Risk-Verknüpfungen,
- Abweichungs- und Stop-Regeln.

### 5. Regulatorische und operative Voraussetzungen trennen

Kennzeichne Sponsor-/Ethik-/Behörden-/Site-/Consent-/Datenschutz-/Registrierungs- oder sonstige Human-only-Schritte als externe Voraussetzungen. Nutze bei Bedarf `human-procedure-wizard`; der Skill simuliert keine Freigabe.

### 6. Evidenz nach Durchführung strukturieren

Ordne Ergebnisse, Deviations, Missing Data, Subgruppen, Bias-/Generalizability-Limitationen und Claim Coverage in `clinical-performance-evidence.json` ein. Ungeklärte Findings bleiben Gaps.

## Output-Verträge

`clinical-performance-study-plan.json` enthält Study Need, Objectives, Claims, Design, Endpunkte, Population, Comparator, Bias Controls, Statistik, Risk/Evidence References, externe Freigaben und Decision Rules.

`clinical-performance-evidence.json` enthält bestehende und/oder neu erzeugte klinische Performance-Evidenz mit Source/Study References, Applicability, Ergebnisstatus, Limitationen und Claim Coverage.

`performance-study-gaps.json` enthält offene Evidenz-, Bias-, Design-, Freigabe-, Statistik- oder Generalisierbarkeitslücken mit nächstem Schritt und Stop Condition.

## Downstream

Primärer Consumer ist `ivdr-performance-evaluation`. Operative/regulatorische Voraussetzungen können an `human-procedure-wizard`, controlled documentation, Risk Management oder Decision Records gehen.

## Memory Path

Persistenzwürdig sind validierte produktspezifische Study-Design-Constraints, wiederverwendbare Bias-/Endpoint-Muster und bestätigte Hinweise zur Evidenzübertragbarkeit. Personenbezogene Studiendaten, Rekrutierungs-/Site-Status, einzelne Patientendaten, offene Deviations, laufende Freigaben und vorläufige Resultate bleiben strikt run-only. Kandidaten benötigen `sourceRefs`; guidance-/regelabhängige Aussagen zusätzlich `asOf` und `reviewAfter`. Übergib nur abstrahierte, nicht-sensitive `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- Study Need explizit gegen Existing Evidence begründet ist,
- Claim, Population, Specimen, Comparator und Endpunkte eindeutig sind,
- Bias und Generalisierbarkeit aktiv bewertet werden,
- Sample-Size-/Statistiklogik nachvollziehbar ist,
- Risk Management verknüpft statt dupliziert wird,
- Human-/Authority-Freigaben nicht simuliert werden,
- personenbezogene Studiendaten nicht in Memory Candidates gelangen,
- Downstream die Evidenz ohne implizite Annahmen übernehmen kann.
