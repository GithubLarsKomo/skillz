---
name: sport-adaptation-analysis
description: Analysiert longitudinale Trainings-, Leistungs-, Recovery-, physiologische und Body-/Energy-Daten auf Adaptation, Plateau, Drift und übermäßige Ermüdung mit individueller Baseline und expliziter Unsicherheit. Verwenden für Block-/Trendanalysen; ACWR, HRV, Vendor-Scores oder Korrelationen nicht als kausale Verletzungs- oder Gesundheitsvorhersage behandeln.
userFacing: true
implicitInvocation: true
category: analysis
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-daily-athlete-monitoring
  - sport-performance-diagnostics
  - sport-microcycle-planning
outputs:
  - sport-adaptation-analysis.json
lastEvaluated: 2026-08-28
---

# Sport Adaptation Analysis

Bestimme, ob Training die beabsichtigte Wirkung erzeugt, ohne Korrelation mit Kausalität zu verwechseln. Standardisierte Leistung und wiederholte Response sind stärker als eine einzelne Tagesmetrik.

## Fünf Analysedomänen

1. **Recovery:** Schlaf, Müdigkeit, Muskelkater, Stress, Motivation, Ruhe-HF/HRV und Recovery-Verlauf.
2. **Training tolerance:** geplante/absolvierte Last, sRPE, externe Last, lokale Ermüdung, RPE-/HF-Drift und Erholung nach Standardbelastung.
3. **Performance capacity:** Pace/Power/Distanz/Kraft/Sprint/VO₂-/Schwellen- und sportartspezifische Diagnostik.
4. **Physiological stability:** Ruhe-HF, HRV, Atemfrequenz, Hauttemperatur, SpO₂ und persistente Abweichungen gegen individuelle Baselines.
5. **Body / Energy context:** Körpergewicht, Taillenumfang, methodisch gekennzeichnete Body-Composition-Daten, Fueling-/Hydrationskontext und Energieverfügbarkeitsrisiko.

Die Domänen bleiben getrennt; es wird kein Gesamt-Health- oder Longevity-Score gebildet.

## Ablauf

1. **Datenqualität und Provenance prüfen.** Missingness, Protokollwechsel, Geräte-/Firmware-/Umweltänderung, Metric Class, Decision Role und inkonsistente Messung markieren.
2. **Vergleichbarkeit herstellen.** Gleiche Standardbelastung, Tests und Messmethoden bevorzugen; BIA, DXA und manuelle Körpermaße nicht stillschweigend gleichsetzen.
3. **Robuste Baselines bilden.** Bei ausreichenden Daten Median/robuste Streuung oder anderes dokumentiertes deterministisches Verfahren verwenden.
4. **Trend pro Domäne quantifizieren.** Zeitfenster und Richtung explizit nennen; Einzeltage nicht als Plateau oder Health Drift deklarieren.
5. **Physiological Stability bewerten.** Multisignal-Abweichungen und Persistenz erfassen. `Health Drift` beschreibt eine Baselineabweichung, keine Krankheit.
6. **Response koppeln.** Performanceverbesserung zusammen mit interner Belastung, Recovery, Training tolerance und Body-/Energy-Kontext betrachten.
7. **Vendor-Scores separieren.** Garmin Training Readiness, Body Battery, Sleep Score, Training Status, Fitness Age oder vergleichbare Provider-Scores nur als `provider_score_context` behandeln; sie dürfen keine Domäne ersetzen.
8. **Plateau/Excess fatigue vorsichtig markieren.** Nur bei wiederholtem Muster und plausibler Datenqualität; alternative Erklärungen und Unsicherheit nennen.
9. **Energy-/Body-Kontext routen.** Gewichts-/Body-Composition-Verläufe nie isoliert optimieren. Relevante Kombinationen aus Gewichtsverlust, Performanceabfall, Recovery-/Health-Drift oder Symptomen an Fueling/RED-S-/medizinische Reviewpfade übergeben.
10. **Testdelta bewerten.** Messfehler, Lern-/Familiarisierungseffekt und Protokolländerung berücksichtigen.
11. **Entscheidungsvorlage übergeben.** Erkenntnisse mit Confidence an `sport-training-adaptation-engine`; Analyse selbst revidiert keinen Plan.

## Verbotene Abkürzungen

- Kein Gesamtwert `Health 91/100`, `Metabolic Capacity`, `Biological Age`, `Pace of Aging` oder „Lifespan Days“.
- ACWR nicht als kausalen universellen Verletzungsprädiktor oder magische Schwelle verwenden.
- HRV, SpO₂, Temperatur oder einen Vendor-Readiness-Score nicht allein zur Diagnose oder täglichen Trainingssteuerung verwenden.
- Korrelation zwischen Load, Body Composition und Symptomatik nicht automatisch als Ursache deklarieren.
- Missing data nicht imputieren, wenn die Methode nicht begründet und gekennzeichnet ist.

## 50+ und Geschlecht

Trends werden gegen die individuelle Historie bewertet. Alters- oder Geschlechtsgruppen liefern Kontext, ersetzen aber nicht die persönliche Baseline. Menstruations-/Menopausekontext darf freiwillig zur Erklärung beitragen, wenn zeitlich und individuell plausibel.

## Übergabe

`sport-adaptation-analysis.json` enthält Datenfenster, Coverage, Baseline-Methode, die fünf Domain-Trends, Health Drift, Body-/Energy-Kontext, Provider-Score-Kontext, standardisierte Vergleiche, Testdeltas, Plateau-/Fatigue-Hypothesen, Alternativerklärungen, Confidence und nächste sinnvolle Messpunkte.

## Abschlusskriterien

Die Analyse trennt Beobachtung, Interpretation und Entscheidungsempfehlung; Unsicherheit/Missingness sind sichtbar, Provider-Algorithmen bleiben als solche markiert und der zentrale Adaptation-Engine erhält keine Scheinkausalität.
