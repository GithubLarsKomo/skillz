---
name: sport-endurance-programming
description: Erstellt sportartspezifische Ausdauerprescriptions aus Diagnostik, Ziel, Saisonphase und Mikrozyklus für niedrige Intensität, Schwelle, VO2-orientierte Intervalle und anaerobe Reize. Verwenden für konkrete Pace-/Power-/HF-/RPE-Ziele; HRV oder starre Zonen nicht als alleinige Regler verwenden.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-athlete-profile
  - sport-performance-diagnostics
  - sport-goal-performance-model
  - sport-mesocycle-planning
  - sport-microcycle-planning
outputs:
  - endurance-plan.json
lastEvaluated: 2026-08-22
---

# Sport Endurance Programming

Übersetze valide Diagnostik und Periodisierungsziele in ausführbare Ausdauerarbeit. Zonen sind Arbeitsbereiche mit Unsicherheit, keine biologischen Schalter.

## Ablauf

1. **Referenzmodell wählen.** LT1/LT2, kritische Leistung/Tempo, sportartspezifische Tests und RPE gemeinsam einordnen; Quelle und Confidence der Schwellen erhalten.
2. **Primärreiz bestimmen.** Low intensity, Threshold, VO2-orientiert, Sprint/anaerob oder Erhaltung passend zum Mesoziel wählen.
3. **Dosis setzen.** Dauer, Wiederholungen, Arbeits-/Pausenzeit, Ziel-Power/Pace/HF/RPE und Abbruch-/Anpassungsregel angeben.
4. **Intensitätsverteilung begründen.** Polarisiert, pyramidal oder andere Verteilung nur als Ergebnis von Sport, Phase, Trainingshistorie und Ziel verwenden; kein Dogma.
5. **Externe und interne Last trennen.** Power/Pace/Distanz als externe Leistung, HF/RPE als interne Reaktion behandeln.
6. **Drift und Kontext nutzen.** Standardbelastungen, Hitze, Schlaf, Fueling und Ermüdung bei ungewöhnlicher HF/RPE berücksichtigen.
7. **Mikrozyklus schützen.** Harte Ausdauerreize gegen Kraft/Power und sportliche Schlüsseltermine sequenzieren.
8. **Progression klein halten.** Volumen, Dichte oder Intensität nicht gleichzeitig unnötig erhöhen.

## HRV und Readiness

HRV/resting HR sind optionale Kontexteingaben. Ein einzelner HRV-Wert darf keine geplante harte Einheit automatisch hoch- oder herunterregeln. Wiederholte individuelle Abweichungen können zusammen mit subjektiver und leistungsbezogener Evidenz einen Checkpoint auslösen.

## Alters-/Geschlechtsmodifier

20–30 und 50+ unterscheiden sich nicht durch starre Intensitätsverbote. Bei Masters-Athleten werden beobachtete Recovery, Trainingshistorie und funktionelle Reserve stärker explizit gemacht. Weibliche Athleten erhalten keine fixe Zyklus-Zonenplanung; Symptome und individuelle Response können die Tagesentscheidung beeinflussen.

## Safety

Akute Krankheit, Brustschmerz, Synkope, ungewöhnliche Belastungsdyspnoe oder dokumentierte medizinische Restriktionen werden nicht als Trainingsproblem wegprogrammiert.

## Übergabe

`endurance-plan.json` enthält Reiztyp, Referenzmodell, Zonen/Targets mit Confidence, Sessions, Dosis, Intensitätsverteilung, Progressions- und Stop-Regeln sowie Interferenzhinweise.

## Abschlusskriterien

Jede Session hat einen klaren physiologischen Zweck, konkrete Targets und eine nachvollziehbare Anpassungsregel; Schwellenunsicherheit und Safety Flags bleiben sichtbar.