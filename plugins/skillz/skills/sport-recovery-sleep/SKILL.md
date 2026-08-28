---
name: sport-recovery-sleep
description: Interpretiert Schlaf, Ermüdung, passive physiologische Signale und Erholung longitudinal gegen individuelle Baselines und leitet konkrete Recovery-Optionen ab. Verwenden bei kumulierter Müdigkeit, Schlafproblemen, Reise, Wettkampfbelastung oder Health Drift; keinen opaken Readiness-Score und keine HRV-/Vendor-Score-Alleinsteuerung erzeugen.
---

# Sport Recovery Sleep

Bewerte Erholung als mehrdimensionalen Verlauf aus Athletenbericht, Schlaf, Trainingskontext und geeigneten passiven Signalen. Schlafbedarf und Response sind individuell; ein einzelner schlechter Morgen oder Wearable-Ausreißer ist weder Diagnose noch automatische Deload-Anweisung.

## Ablauf

1. **Datenklassen prüfen.** Direkte Sensorwerte, manuelle/reference Messungen, Sports-Journal-Ableitungen und proprietäre Provider-Scores unterscheiden. Provider-Scores bleiben Kontext und werden nicht wie Rohsignale behandelt.
2. **Baseline bilden.** Bei ausreichender Coverage robuste individuelle Referenzen für Schlafdauer/-qualität, Müdigkeit, Muskelkater, Stress, Motivation sowie – soweit methodisch vergleichbar – resting HR, HRV, Respiration, Hauttemperaturtrend und ausgewählte SpO₂-Summaries verwenden.
3. **Akut vs. Trend trennen.** Einzeltag, 3–7-Tage-Verlauf und längere Entwicklung getrennt beschreiben. Device-, Firmware- oder Methodenwechsel als potenzielle Serienbrüche markieren.
4. **Physiological Stability bewerten.** Abweichungen mehrerer geeigneter Baseline-Marker zusammenführen, ohne einen universellen Health Score zu erzeugen. Datenqualität und Persistenz bleiben sichtbar.
5. **Health Drift bestimmen.** `normal | elevated | persistent | resolving | unknown` nur aus nachvollziehbaren Baselineabweichungen ableiten. Ein isolierter HRV-, Temperatur- oder SpO₂-Wert reicht nicht für relevante Eskalation.
6. **Belastungskontext koppeln.** Trainingslast, Standardbelastungsreaktion, Reise, Wettkampf, Krankheit, Lebensstress, Umwelt und zeitliche Schlafgelegenheit zuordnen.
7. **Subjektiv/objektiv abgleichen.** Konflikte zwischen Wearable und Athletenbericht explizit erhalten und bei ungeklärtem Widerspruch Confidence reduzieren.
8. **Schlafproblem spezifizieren.** Zu wenig Gelegenheit, Einschlaf-/Durchschlafproblem, verschobene Zeiten oder subjektiv schlechte Qualität nicht vermischen.
9. **Recovery-Maßnahme proportional wählen.** Schlafgelegenheit, Tagesstruktur, Nap-Option, leichte Recovery, Sessionverschiebung oder reduzierte Last nur bei passender Gesamtevidenz vorschlagen.
10. **Re-Evaluation terminieren.** Kurzfristige Maßnahmen mit nächstem Checkpoint verbinden.

## Provider-Scores

Garmin Training Readiness, Body Battery, Sleep Score, Training Status, Fitness Age und analoge proprietäre Outputs dürfen in `provider_score_context` dokumentiert werden. Sie dürfen weder Health Drift definieren noch allein eine Recovery- oder Trainingsentscheidung auslösen. Biological Age, Pace of Aging, Lifespan-/„days gained“-Angaben und Metabolic Capacity/Momentum sind keine autoritativen Recovery-Konstrukte.

## Keine Scheingenauigkeit

Kein zusammengesetzter Wert wie `Readiness 72%` oder ein universeller Health-/Longevity-Score darf als physiologische Wahrheit ausgegeben werden. Traffic-Light-States sind nur zulässig, wenn die verantwortlichen Signale, Datenqualität und Unsicherheit sichtbar bleiben. HRV ist ein Signal und kein autonomer Regler.

## 50+ und Geschlecht

Bei 50+ kann Recovery variabler sein, wird aber gemessen statt vorausgesetzt. Peri-/Menopause-, Zyklus- oder thermoregulatorische Symptome dürfen freiwillig als Erklärungskontext eingehen, nicht als starre Trainingsphase.

## Safety

Anhaltende ausgeprägte Schlafstörung, extreme Tagesmüdigkeit, mögliche schlafbezogene Atmungsstörung, depressive/psychiatrische Warnzeichen, systemische Erkrankung oder andere Red Flags werden an geeignete professionelle Abklärung geroutet. Ein günstiger Wearable-Score kann solche Signale nicht überstimmen; der Skill diagnostiziert nicht.

## Übergabe

`recovery-state.json` enthält Baselinefenster, aktuelle Signale, `physiological_stability`, `baseline_deviations`, `health_drift`, `health_drift_signals`, `provider_score_context`, Trend, plausible Kontextfaktoren, Maßnahmen, Confidence, nächste Re-Evaluation und Safety Flags gemäß P1-Contract.

## Evidenzanker

Athleten-Schlafkonsensus betont individuelle Schlafbedürfnisse und sport-/reisebedingte Störungen statt einer universellen Einheitszahl. Wearable-Metriken werden entsprechend ihrer Mess- und Ableitungsebene als longitudinale Kontextsignale behandelt.

## Abschlusskriterien

Erholung ist als erklärbarer Zustand mit individueller Baseline, physiologischer Stabilität, subjektivem Kontext, proportionaler Intervention und nächstem Checkpoint beschrieben; proprietäre Vendor-Scores bleiben erkennbar sekundär.
