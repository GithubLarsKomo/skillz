---
name: sport-adaptation-analysis
description: Analysiert longitudinale Trainings- und Leistungsdaten auf Adaptation, Plateau, Drift und übermäßige Ermüdung mit individueller Baseline und expliziter Unsicherheit. Verwenden für Block-/Trendanalysen; ACWR, HRV oder Korrelationen nicht als kausale Verletzungsvorhersage behandeln.
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
lastEvaluated: 2026-08-22
---

# Sport Adaptation Analysis

Bestimme, ob Training die beabsichtigte Wirkung erzeugt, ohne Korrelation mit Kausalität zu verwechseln. Standardisierte Leistung und wiederholte Response sind stärker als eine einzelne Tagesmetrik.

## Analyseebenen

- **Load:** geplante/absolvierte Dauer, sRPE, externe Last und Verteilung.
- **Performance:** Pace/Power/Distanz/Kraft/Power bei vergleichbaren Bedingungen.
- **Internal response:** RPE, HF, Drift und Erholung bei Standardlast.
- **Recovery:** Schlaf, Müdigkeit, Muskelkater, Stress, Motivation und optionale HRV/resting HR.
- **Diagnostics:** Test-to-Test-Delta mit Messunsicherheit und Protokollvergleich.

## Ablauf

1. **Datenqualität prüfen.** Missingness, Protokollwechsel, Geräte-/Umweltänderung und inkonsistente Messung markieren.
2. **Vergleichbarkeit herstellen.** Gleiche Standardbelastung/Tests bevorzugen; rohe Bestleistungen nicht blind vergleichen.
3. **Robuste Baseline bilden.** Bei ausreichenden Daten Median/robuste Streuung oder anderes dokumentiertes deterministisches Verfahren verwenden.
4. **Trend quantifizieren.** Zeitfenster und Richtung explizit nennen; Einzeltage nicht als Plateau deklarieren.
5. **Response koppeln.** Performanceverbesserung zusammen mit interner Belastung und Recovery betrachten.
6. **Plateau/Excess fatigue vorsichtig markieren.** Nur bei wiederholtem Muster und plausibler Datenqualität; alternative Erklärungen und Unsicherheit nennen.
7. **Testdelta bewerten.** Messfehler, Lern-/Familiarisierungseffekt und Protokolländerung berücksichtigen.
8. **Entscheidungsvorlage übergeben.** Erkenntnisse mit Confidence an `sport-training-adaptation-engine`; Analyse selbst revidiert keinen Plan.

## Verbotene Abkürzungen

- ACWR nicht als kausalen universellen Verletzungsprädiktor oder magische Schwelle verwenden.
- HRV nicht allein zur Diagnose von Übertraining oder zur täglichen Trainingssteuerung verwenden.
- Korrelation zwischen Load und Symptomatik nicht automatisch als Ursache deklarieren.
- Missing data nicht imputieren, wenn die Methode nicht begründet und gekennzeichnet ist.

## 50+ und Geschlecht

Trends werden gegen die individuelle Historie bewertet. Alters- oder Geschlechtsgruppen liefern Kontext, ersetzen aber nicht die persönliche Baseline. Menstruations-/Menopausekontext darf freiwillig zur Erklärung beitragen, wenn zeitlich und individuell plausibel.

## Übergabe

`sport-adaptation-analysis.json` enthält Datenfenster, Coverage, Baseline-Methode, Load-/Performance-/Recovery-Trends, standardisierte Vergleiche, Testdeltas, Plateau-/Fatigue-Hypothesen, Alternativerklärungen, Confidence und nächste sinnvolle Messpunkte.

## Abschlusskriterien

Die Analyse trennt Beobachtung, Interpretation und Entscheidungsempfehlung; Unsicherheit/Missingness sind sichtbar und der zentrale Adaptation-Engine erhält keine Scheinkausalität.