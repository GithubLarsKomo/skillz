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
consumes:
  - athlete-profile.json
  - sport-diagnostics.json
  - sport-performance-model.json
  - sport-mesocycle.json
  - sport-microcycle.json
outputs:
  - endurance-plan.json
lastEvaluated: 2026-08-22
---

# Sport Endurance Programming

Übersetze valide Diagnostik und Periodisierungsziele in ausführbare Ausdauerarbeit. Zonen sind Arbeitsbereiche mit Unsicherheit, keine biologischen Schalter.

## Trigger

Nutze diesen Skill, wenn ein Meso-/Mikrozyklus in konkrete Ausdauereinheiten mit sportartspezifischen Intensitäts- und Dosisvorgaben übersetzt werden soll.

## Voraussetzungen

Mindestens Ziel/Phase, aktuelle Ausdauerdiagnostik oder belastbare Leistungsreferenz, Trainingshistorie und relevante Health Constraints sollten vorliegen. Fehlende Schwellen- oder Leistungsdaten werden als Unsicherheit ausgewiesen, nicht erfunden.

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

HRV/resting HR sind optionale Kontexteingaben und **kein autonomer Regler**. Ein einzelner HRV-Wert darf keine geplante harte Einheit automatisch hoch- oder herunterregeln. Wiederholte individuelle Abweichungen können zusammen mit subjektiver und leistungsbezogener Evidenz einen Checkpoint auslösen.

## Alters-/Geschlechtsmodifier

20–30 und 50+ unterscheiden sich nicht durch starre Intensitätsverbote. Bei Masters-Athleten werden beobachtete Recovery, Trainingshistorie und funktionelle Reserve stärker explizit gemacht. Weibliche Athleten erhalten keine fixe Zyklus-Zonenplanung; Symptome und individuelle Response können die Tagesentscheidung beeinflussen.

## Safety

Akute Krankheit, Brustschmerz, Synkope, ungewöhnliche Belastungsdyspnoe oder dokumentierte medizinische Restriktionen werden nicht als Trainingsproblem wegprogrammiert.

## Prüfungen

- Sind Schwellen/Targets auf eine Quelle oder belastbare Leistungsreferenz zurückgeführt?
- Sind externe Leistung und interne Reaktion getrennt?
- Ist der Primärreiz eindeutig und die Dosis vollständig ausführbar?
- Wird HRV nur im Kontext mehrerer Signale verwendet?
- Sind Interferenz, Progression und Stop-Regeln sichtbar?

## Fehlerbehandlung

- **Diagnostik fehlt oder ist veraltet:** RPE-/Leistungsanker mit niedrigerer Confidence verwenden und Retest-Bedarf markieren.
- **Widersprüchliche Zonenmodelle:** keine Scheingenauigkeit erzeugen; überlappende Bandbreiten und Unsicherheit dokumentieren.
- **Red Flag:** normale Ausdauerprogression verlassen und Health/Medical Routing priorisieren.

## Übergabe

`endurance-plan.json` enthält Reiztyp, Referenzmodell, Zonen/Targets mit Confidence, Sessions, Dosis, Intensitätsverteilung, Progressions- und Stop-Regeln sowie Interferenzhinweise.

## Abschlusskriterien

Jede Session hat einen klaren physiologischen Zweck, konkrete Targets und eine nachvollziehbare Anpassungsregel; Schwellenunsicherheit und Safety Flags bleiben sichtbar.
