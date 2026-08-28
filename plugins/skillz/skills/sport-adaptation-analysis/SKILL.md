---
name: sport-adaptation-analysis
description: Analysiert longitudinale Trainings-, Leistungs-, Recovery-, passive Biometrie- und Body/Energy-Daten auf Adaptation, Plateau, Drift und übermäßige Ermüdung mit individueller Baseline und expliziter Unsicherheit. Verwenden für Block-/Trendanalysen; ACWR, HRV, Vendor-Scores oder Korrelationen nicht als kausale Verletzungs- oder Readiness-Regler behandeln.
---

# Sport Adaptation Analysis

Bestimme, ob Training die beabsichtigte Wirkung erzeugt, ohne Korrelation mit Kausalität zu verwechseln. Standardisierte Leistung, wiederholte Response und methodenkompatible longitudinale Signale sind stärker als einzelne Tagesmetriken oder proprietäre Provider-Scores.

## Fünf Analyse-Domänen

Die Analyse hält fünf Domänen getrennt und erzeugt **keinen universellen Health-/Readiness-Score**:

1. **Recovery:** Schlaf, subjektive Erholung, Müdigkeit, Stress, Muskelkater sowie geeignete HRV-/Ruhe-HF-Kontexte.
2. **Training tolerance:** geplante/absolvierte Last, sRPE, externe Last, RPE-/HF-/Power-/Pace-Response und Erholung nach Standardbelastung.
3. **Performance capacity:** Pace/Power/Distanz, Schwellen, VO₂-bezogene Marker, Kraft/Power und sportartspezifische Tests bei vergleichbaren Bedingungen.
4. **Physiological stability:** individuelle Baselineabweichungen von geeigneten passiven Signalen wie resting HR, HRV, Respiration, Hauttemperaturtrend, Schlaf und ausgewählten SpO₂-Summaries einschließlich Health Drift.
5. **Body / Energy context:** Körpermasse, Taille, methodenbewusste Body-Composition-Trends, Fueling-/Hydrationskontext und Hinweise auf niedrige Energieverfügbarkeit.

Diagnostische Test-to-Test-Deltas und Messunsicherheit ergänzen diese Domänen, ohne sie in eine Einheitszahl zu verdichten.

## Ablauf

1. **Datenqualität und Provenance prüfen.** Missingness, Messklasse, `decision_role`, Protokollwechsel, Provider-/Device-/Firmware-/Methodenänderung und inkonsistente Messung markieren.
2. **Vergleichbarkeit herstellen.** Gleiche Standardbelastung, Tests und `comparable_series_id` bevorzugen; Rohbestleistungen und unterschiedliche Body-Composition-Methoden nicht blind vergleichen.
3. **Robuste Baseline bilden.** Bei ausreichenden Daten Median/robuste Streuung oder anderes dokumentiertes deterministisches Verfahren verwenden. Baselinefenster, Coverage und Seriengrenzen erhalten.
4. **Domänentrends quantifizieren.** Für jede der fünf Domänen Richtung, Evidenz, Coverage und Unsicherheit getrennt ausgeben; keine Prozentzahl als Gesamtgesundheit erfinden.
5. **Physiological Stability/Health Drift bewerten.** Einzelne Abweichungen nicht eskalieren. Persistenz, mehrere unabhängige Signale, Datenqualität und Symptome/Belastungskontext gemeinsam prüfen.
6. **Response koppeln.** Performanceverbesserung zusammen mit interner Belastung, Training Tolerance und Recovery betrachten. Mehr Last bei stabiler/verbesserter Response kann andere Bedeutung haben als mehr Last bei steigender RPE und fallender Leistung.
7. **Body/Energy methodenbewusst interpretieren.** BIA, DXA, Waage und Tape als getrennte Serien behandeln. Körpermassen- oder BIA-Änderung allein ist weder Adaptationsbeweis noch RED-S-Diagnose.
8. **Provider-Scores separieren.** Garmin Training Readiness, Body Battery, Sleep Score, Training Status, Fitness Age und analoge Werte in `provider_score_context` halten; zugrunde liegende Signale bevorzugen und keine kausale Autorität ableiten.
9. **Plateau/Excess fatigue vorsichtig markieren.** Nur bei wiederholtem Muster und plausibler Datenqualität; alternative Erklärungen und Unsicherheit nennen.
10. **Testdelta bewerten.** Messfehler, Lern-/Familiarisierungseffekt und Protokolländerung berücksichtigen.
11. **Entscheidungsvorlage übergeben.** Erkenntnisse mit Confidence an `sport-training-adaptation-engine`; Analyse selbst revidiert keinen Plan.

## Verbotene Abkürzungen

- ACWR nicht als kausalen universellen Verletzungsprädiktor oder magische Schwelle verwenden.
- HRV nicht allein zur Diagnose von Übertraining oder zur täglichen Trainingssteuerung verwenden.
- Kein Garmin-/Vendor-Readiness- oder Health-Score bestimmt einen Adaptationszustand allein.
- Biological Age, Pace of Aging, Lifespan-/„days gained“-Angaben und Metabolic Capacity/Momentum nicht als validierte Adaptationsendpunkte verwenden.
- Korrelation zwischen Load, Biomarker und Symptomatik nicht automatisch als Ursache deklarieren.
- BIA und DXA nicht still zu einer gemeinsamen Body-Composition-Serie zusammenführen.
- Missing data nicht als Normalwert behandeln oder unmarkiert imputieren.

## 50+ und Geschlecht

Trends werden gegen die individuelle Historie bewertet. Alters- oder Geschlechtsgruppen liefern Kontext, ersetzen aber nicht die persönliche Baseline. Menstruations-/Menopausekontext darf freiwillig zur Erklärung beitragen, wenn zeitlich und individuell plausibel.

## Übergabe

`sport-adaptation-analysis.json` enthält Datenfenster, Coverage, Baseline-Methode, allgemeine Trends sowie `domain_trends` für Recovery, Training Tolerance, Performance Capacity, Physiological Stability und Body/Energy Context. Soweit vorhanden enthält es außerdem `biometric_baselines`, `health_drift`, `health_drift_signals`, `body_composition_context`, `provider_score_context`, standardisierte Vergleiche, Testdeltas, Plateau-/Fatigue-Hypothesen, Alternativerklärungen, Confidence und nächste sinnvolle Messpunkte gemäß P1-Contract.

## Abschlusskriterien

Die Analyse trennt Beobachtung, Anbieterableitung, Sports-Journal-Ableitung, Interpretation und Entscheidungsempfehlung; Unsicherheit/Missingness sind sichtbar und der zentrale Adaptation-Engine erhält keine Scheinkausalität oder Black-box-Gesamtzahl.
