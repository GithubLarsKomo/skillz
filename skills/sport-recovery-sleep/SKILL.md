---
name: sport-recovery-sleep
description: Interpretiert Schlaf, Ermüdung und Erholung longitudinal gegen die individuelle Baseline und leitet konkrete Recovery-Optionen ab. Verwenden bei kumulierter Müdigkeit, Schlafproblemen, Reise, Wettkampfbelastung oder passiven Wearable-Abweichungen; keinen opaken Readiness-Score und keine HRV-Alleinsteuerung erzeugen.
userFacing: true
implicitInvocation: true
category: analysis
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-athlete-profile
  - sport-daily-athlete-monitoring
outputs:
  - recovery-state.json
lastEvaluated: 2026-08-28
---

# Sport Recovery Sleep

Bewerte Erholung als mehrdimensionalen Verlauf. Schlafbedarf und Response sind individuell; ein einzelner schlechter Morgen oder Wearable-Ausreißer ist weder Diagnose noch automatische Deload-Anweisung.

## Ablauf

1. **Vergleichbare Baselines bilden.** Bei ausreichenden Daten robuste individuelle Referenzen für Schlafdauer/-qualität, Müdigkeit, Muskelkater, Stress, Motivation sowie optional Ruhe-HF, HRV, Atemfrequenz, Hauttemperatur und SpO₂ verwenden. Nur methodisch vergleichbare Serien zusammenführen.
2. **Akut vs. Trend trennen.** Einzeltag, 3–7-Tage-Verlauf und längere Entwicklung getrennt beschreiben.
3. **Physiological Stability bewerten.** Mehrere passive Biomarker gemeinsam gegen die persönliche Baseline betrachten. Abweichungen als `normal`, `elevated`, `persistent`, `resolving` oder `unknown` beschreiben; keine Krankheitsdiagnose ableiten.
4. **Health Drift nur multisignal-basiert eskalieren.** Ein einzelner HRV-, Temperatur- oder SpO₂-Wert reicht nicht. Persistenz, unabhängige Signale, Datenqualität, Symptome und Belastungskontext bestimmen die Relevanz.
5. **Belastungskontext koppeln.** Trainingslast, Reise, Wettkampf, Krankheit, Lebensstress und zeitliche Schlafgelegenheit zuordnen.
6. **Vendor-Scores dekomponieren.** Garmin Body Battery, Sleep Score, Training Readiness oder ähnliche Scores dürfen als Provider-Kontext gezeigt werden, aber ihre zugrunde liegenden Messgrößen und Journal-Daten bleiben entscheidungsnäher.
7. **Schlafproblem spezifizieren.** Zu wenig Gelegenheit, Einschlaf-/Durchschlafproblem, verschobene Zeiten oder subjektiv schlechte Qualität nicht vermischen.
8. **Recovery-Maßnahme proportional wählen.** Schlafgelegenheit, Tagesstruktur, Nap-Option, leichte Recovery, Sessionverschiebung oder reduzierte Last nur bei passender Evidenz vorschlagen.
9. **Re-Evaluation terminieren.** Kurzfristige Maßnahmen mit nächstem Checkpoint verbinden.

## Baseline-Regeln

- Baselines sind individuell und robust; Population-Normen dienen nur als Kontext.
- Ein Geräte-, Firmware- oder Messmethodenwechsel kann eine neue Vergleichsserie erfordern.
- Fehlende Daten reduzieren Confidence; sie werden nicht als „normal“ imputiert.
- Schlafphasen und Consumer-SpO₂ werden schwächer gewichtet als stabilere Trends, sofern keine bessere Validierung für das konkrete Gerät vorliegt.
- Health Drift ist eine Beobachtung physiologischer Instabilität, keine Diagnose oder Clearance-Entscheidung.

## Keine Scheingenauigkeit

Kein zusammengesetzter Wert wie `Readiness 72%`, „Biological Age“, „Pace of Aging“, „Metabolic Capacity“ oder „gewonnene Lebenstage“ darf als physiologische Wahrheit ausgegeben werden. Traffic-Light-States sind nur zulässig, wenn die verantwortlichen Signale sichtbar bleiben. HRV ist Kontext und kein autonomer Regler.

## 50+ und Geschlecht

Bei 50+ kann Recovery variabler sein, wird aber gemessen statt vorausgesetzt. Peri-/Menopause-, Zyklus- oder thermoregulatorische Symptome dürfen freiwillig als Erklärungskontext eingehen, nicht als starre Trainingsphase.

## Safety

Anhaltende ausgeprägte Schlafstörung, extreme Tagesmüdigkeit, mögliche schlafbezogene Atmungsstörung, persistierende multisignal-physiologische Abweichung zusammen mit Symptomen, depressive/psychiatrische Warnzeichen oder systemische Erkrankung werden an geeignete professionelle Abklärung geroutet; der Skill diagnostiziert nicht.

## Übergabe

`recovery-state.json` enthält Baselinefenster, aktuelle subjektive und passive Signale, Physiological Stability, Health Drift, Provider-Kontext, Trend, plausible Kontextfaktoren, Maßnahmen, Confidence, nächste Re-Evaluation und Safety Flags.

## Evidenzanker

Athleten-Schlafkonsensus betont individuelle Schlafbedürfnisse und sport-/reisebedingte Störungen statt einer universellen Einheitszahl. Wearable-Daten werden geräte- und claim-spezifisch bewertet; Provider-Algorithmen werden nicht automatisch als validierte physiologische Konstrukte behandelt.

## Abschlusskriterien

Erholung ist als erklärbarer Zustand mit Trend, Baseline, Datenqualität, Kontext, proportionaler Intervention und nächstem Checkpoint beschrieben.
