---
name: sport-season-periodization
description: Plant die Saison- und Makrostruktur aus priorisierten Wettkämpfen, Performance-Zielen, Trainingshistorie und verfügbarem Kalender. Verwenden für A/B/C-Wettkämpfe, Peak-Timing, Vorbereitungs-, Wettkampf-, Taper- und Übergangsphasen; nicht für konkrete Tages- oder Wochenbelastungen.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-goal-performance-model
consumes:
  - sport-performance-model.json
outputs:
  - sport-season-plan.json
lastEvaluated: 2026-08-22
---

# Sport Season Periodization

Erzeuge eine robuste Saisonarchitektur, die Peaks und Entwicklungsphasen plant, ohne eine einzelne Periodisierungsideologie zu erzwingen.

## Trigger

Nutze diesen Skill für Saison-, Jahres- oder Makroplanung mit einem oder mehreren Zielwettkämpfen.

## Voraussetzungen

Benötigt `sport-performance-model.json`, Athletenprofil, Wettkampfkalender, Trainingshistorie, verfügbare Zeit und bekannte Belastungsgrenzen.

## Ablauf

1. **Wettkämpfe klassifizieren.** A/B/C-Priorität, Zielleistung und notwendige Frische festlegen.
2. **Peaks begrenzen.** Hauptpeaks auf realistische Fenster verteilen und Zielkonflikte kennzeichnen.
3. **Makrozyklen schneiden.** Allgemeine Vorbereitung, spezifische Vorbereitung, Wettkampf/Taper und Transition nach Bedarf planen.
4. **Adaptationsreihenfolge wählen.** Limiter und Zielanforderungen in eine nachvollziehbare Reihenfolge überführen.
5. **Retests platzieren.** Tests nur dort einplanen, wo sie eine Planentscheidung verändern können.
6. **Puffer einbauen.** Krankheit, Reise, Wettkampfverschiebung und variable Adaptation durch Revisionspunkte abfangen.
7. **Taper-Fenster definieren.** Volumenreduktion und Erhalt spezifischer Intensität als Ziel festlegen; Details bleiben nachgelagert.

## Periodisierungsregel

Linear, undulierend, Block- oder Mischformen sind Werkzeuge. Die Wahl wird aus Sportart, Kalender, Trainingsalter, Wettkampfdichte und beobachteter Reaktion begründet; keine Form gilt pauschal als überlegen.

## Alters- und Geschlechtsregeln

50+ kann größere Bedeutung von Kraft-/Power-Erhalt, funktioneller Reserve und adaptiven Erholungsfenstern haben, ohne Intensität pauschal zu reduzieren. Sex-spezifische Symptome können Kalenderentscheidungen beeinflussen, starre zyklusphasengesteuerte Makroplanung ist unzulässig.

## Prüfungen

- Passen Phasen und Wettkampfprioritäten zeitlich zusammen?
- Gibt es ausreichend Entwicklungs- und Taperzeit vor A-Wettkämpfen?
- Sind Retests entscheidungsrelevant?
- Sind Puffer und Revisionspunkte vorhanden?
- Wurde keine Periodisierungsform dogmatisch gewählt?

## Fehlerbehandlung

- **Zu viele A-Wettkämpfe:** Konflikt offenlegen und Priorisierung erzwingen.
- **Kurzer Horizont:** reduzierte Peak-/Taperlogik statt künstlichem Voll-Makrozyklus verwenden.
- **Unsichere Termine:** Zeitfenster und Triggerpunkte statt falscher Kalenderpräzision nutzen.

## Übergabe

Output ist `sport-season-plan.json` gemäß `$defs.seasonPlan`. `sport-mesocycle-planning` übernimmt jeweils den aktiven Makro-/Phasenkontext.

## Abschlusskriterien

Der Skill endet mit einer kalenderkonsistenten Saisonstruktur aus Wettkampfprioritäten, Phasen, Makrozyklen, Retests, Puffern und Revisionspunkten.
