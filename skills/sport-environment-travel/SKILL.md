---
name: sport-environment-travel
description: Plant sportliche Anpassungen an Hitze, Kälte, Höhe/Hypoxie, Reisebelastung und Jetlag mit Kontext-, Akklimatisations-, Schlaf-/Circadian- und Safety-Regeln. Verwenden für Trainingslager, Wettkampfreisen oder extreme Umweltbedingungen; nicht als pauschale Lastsenkung oder medizinische Höhenfreigabe.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-athlete-profile
  - sport-microcycle-planning
  - sport-recovery-sleep
outputs:
  - environment-adjustment.json
lastEvaluated: 2026-08-22
---

# Sport Environment & Travel

Behandle Umwelt und Reise als planbare Kontextbelastung. Hitze, Kälte, Höhe, Travel Fatigue und Jetlag sind unterschiedliche Probleme mit unterschiedlichen Mechanismen und dürfen nicht in einem generischen „Recovery Score“ verschwinden.

## Trigger

Nutze diesen Skill bei Trainings-/Wettkampfexposition in Hitze/Kälte, Höhen- oder Hypoxieblöcken, Langstreckenreisen, Zeitzonenwechsel oder wenn Reiseplanung Schlüsseltrainings und Wettkampfleistung beeinflussen kann.

## Voraussetzungen

Zielort, Zeitraum, Zeitverschiebung, Klima/Umwelt, Höhe, Wettkampf-/Trainingszeit, Reiseplan und relevante Health Constraints erfassen. Fehlende Wetter-/Höheninformationen als Unsicherheit markieren statt erfinden.

## Ablauf

1. **Exposition klassifizieren.** `heat`, `cold`, `altitude_hypoxia`, `travel_fatigue`, `jet_lag` oder Kombinationen getrennt erfassen.
2. **Risiko und Leistungsziel trennen.** Safety-/medizinische Grenzen vor Performance-Optimierung behandeln.
3. **Akklimatisation planen.** Bei Hitze wiederholte sportartspezifische Wärmeexposition über einen geeigneten Vorbereitungszeitraum vorsehen; Hydration/Cooling und realistische Intensitätsanpassung ergänzen.
4. **Höhe individualisieren.** Expositionshöhe/-dauer, Trainingsqualität, Eisen-/Gesundheitskontext und Ziel des Camps dokumentieren. LHTL/Hypoxie ist eine Option mit variabler Response, kein Pflichtmodell.
5. **Travel Fatigue und Jetlag trennen.** Reisedauer/Logistik von circadianer Fehlanpassung unterscheiden.
6. **Circadiane Strategie bauen.** Ziel-Schlaf-/Wachzeit, Licht/Dunkelheit, Mahlzeiten, Bewegung und Training zeitlich auf Zielzeitzone/Wettkampfzeit ausrichten; keine universelle Ost-/West-Formel ohne Reisedaten.
7. **Mikrozyklus anpassen.** Schlüsselreize um Reise/Akklimatisation platzieren und nur so viel Last verschieben wie nötig.
8. **Response prüfen.** Schlaf, subjektive Müdigkeit, Leistung bei Standardbelastung, Hitze-/Höhenverträglichkeit und Krankheitssignale beobachten.

## Hitze

Hitzeakklimatisation ist eine der wichtigsten leistungs- und belastungsrelevanten Interventionen für Wettkampf in heißer Umgebung. Hydration und Cooling ergänzen sie, ersetzen aber keine Akklimatisation. Individuelle Schweißrate/Verträglichkeit kann die Strategie präzisieren; keine pauschale Maximierung der Flüssigkeitsaufnahme.

## Höhe / Hypoxie

Höhenkonzepte können bei Ausdauerathleten physiologische/leistungsbezogene Vorteile bieten, die Response ist heterogen. Trainingsqualität und individuelle Toleranz müssen erhalten bleiben. Akute relevante Höhenkrankheitssymptome oder medizinische Risiken werden nicht als normales Trainingsproblem behandelt.

## Reise / Jetlag

Travel Fatigue kann auch ohne Zeitzonenwechsel auftreten; Jetlag beruht auf circadianer Fehlanpassung nach Zeitzonenwechsel. Interventionen richten sich an den konkreten Reiseweg, Zeitplan und Zielwettkampf. Schlafmittel/Medikamente werden nicht autonom empfohlen.

## Alters-/Geschlechtsmodifier

Keine pauschalen Regeln „Masters brauchen mehr Tage“ oder geschlechtsbasierte Hitze-/Höhenverbote. Individuelle Response, Health Constraints, Hydrations-/Thermoregulationskontext und Reiseerfahrung sind primär.

## Safety

Synkope, Brustschmerz, schwere Dyspnoe, neurologische Symptome, deutliche Hitzeerkrankung, akute Höhenkrankheit oder andere medizinische Red Flags verlassen normale Performance-Planung und benötigen geeignete medizinische Abklärung/Versorgung.

## Prüfungen

- Sind Umweltart und Mechanismus getrennt?
- Ist die Strategie zeitlich konkret statt „mehr Erholung“?
- Sind Zielwettkampf und Schlüsselreize berücksichtigt?
- Werden Hitze-/Höhen-/Circadian-Interventionen nicht als universelle Rezepte dargestellt?
- Gibt es klare Safety-/Re-Evaluation-Regeln?

## Fehlerbehandlung

- **Reisedaten unvollständig:** keine Jetlag-Zeitplanung erfinden; fehlende Zeiten anfordern/markieren.
- **Keine Akklimatisationszeit:** konservative Expositions-/Cooling-/Pacing-Strategie mit Unsicherheit statt fiktiver Anpassung.
- **Red Flag:** normale Trainingsoptimierung beenden und medizinisch routen.

## Übergabe

`environment-adjustment.json` enthält Version, Exposition(en), Reise-/Umweltdaten, Zielereignis, Akklimatisations-/Circadian-Strategie, Mikrozyklusänderungen, Hydration/Cooling-Kontext, Monitoring, Safety Flags, Unsicherheiten und nächste Re-Evaluation.

## Abschlusskriterien

Die Umwelt-/Reisestrategie ist mechanistisch passend, zeitlich ausführbar, minimal invasiv für den Trainingsplan und besitzt klare Safety-/Monitoring-Grenzen.
