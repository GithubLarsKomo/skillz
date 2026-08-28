---
name: sport-recovery-sleep
description: Interpretiert Schlaf, Ermüdung und Erholung longitudinal gegen die individuelle Baseline und leitet konkrete Recovery-Optionen ab. Verwenden bei kumulierter Müdigkeit, Schlafproblemen, Reise oder Wettkampfbelastung; keinen opaken Readiness-Score und keine HRV-Alleinsteuerung erzeugen.
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
lastEvaluated: 2026-08-22
---

# Sport Recovery Sleep

Bewerte Erholung als mehrdimensionalen Verlauf. Schlafbedarf und Response sind individuell; ein einzelner schlechter Morgen ist weder Diagnose noch automatische Deload-Anweisung.

## Ablauf

1. **Baseline bilden.** Wenn ausreichend Daten vorliegen, robuste individuelle Referenzen für Schlafdauer/-qualität, Müdigkeit, Muskelkater, Stress, Motivation sowie optional resting HR/HRV verwenden.
2. **Akut vs. Trend trennen.** Einzeltag, 3–7-Tage-Verlauf und längere Entwicklung getrennt beschreiben.
3. **Belastungskontext koppeln.** Trainingslast, Reise, Wettkampf, Krankheit, Lebensstress und zeitliche Schlafgelegenheit zuordnen.
4. **Schlafproblem spezifizieren.** Zu wenig Gelegenheit, Einschlaf-/Durchschlafproblem, verschobene Zeiten oder subjektiv schlechte Qualität nicht vermischen.
5. **Recovery-Maßnahme proportional wählen.** Schlafgelegenheit, Tagesstruktur, Nap-Option, leichte Recovery, Sessionverschiebung oder reduzierte Last nur bei passender Evidenz vorschlagen.
6. **Re-Evaluation terminieren.** Kurzfristige Maßnahmen mit nächstem Checkpoint verbinden.

## Keine Scheingenauigkeit

Kein zusammengesetzter Wert wie `Readiness 72%` darf als Wahrheit ausgegeben werden. Traffic-Light-States sind nur zulässig, wenn die verantwortlichen Signale sichtbar bleiben. HRV ist Kontext und kein autonomer Regler.

## 50+ und Geschlecht

Bei 50+ kann Recovery variabler sein, wird aber gemessen statt vorausgesetzt. Peri-/Menopause-, Zyklus- oder thermoregulatorische Symptome dürfen freiwillig als Erklärungskontext eingehen, nicht als starre Trainingsphase.

## Safety

Anhaltende ausgeprägte Schlafstörung, extreme Tagesmüdigkeit, mögliche schlafbezogene Atmungsstörung, depressive/psychiatrische Warnzeichen oder systemische Erkrankung werden an geeignete professionelle Abklärung geroutet; der Skill diagnostiziert nicht.

## Übergabe

`recovery-state.json` enthält Baselinefenster, aktuelle Signale, Trend, plausible Kontextfaktoren, Maßnahmen, Confidence, nächste Re-Evaluation und Safety Flags.

## Evidenzanker

Athleten-Schlafkonsensus betont individuelle Schlafbedürfnisse und sport-/reisebedingte Störungen statt einer universellen Einheitszahl.

## Abschlusskriterien

Erholung ist als erklärbarer Zustand mit Trend, Kontext, proportionaler Intervention und nächstem Checkpoint beschrieben.