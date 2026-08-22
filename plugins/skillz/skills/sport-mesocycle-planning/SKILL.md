---
name: sport-mesocycle-planning
description: Übersetzt eine Saisonphase in einen 3–8-wöchigen Adaptationsblock mit Primärziel, Erhaltungsqualitäten, Laststrategie, Entry-/Exit-Kriterien und Re-Evaluation. Verwenden für Blockplanung zwischen Saisonarchitektur und konkreter Wochenplanung; nicht für die Detaildosierung einzelner Übungen.
---

# Sport Mesocycle Planning

Baue einen begrenzten Trainingsblock um eine primäre Adaptation und klar definierte Revisionskriterien.

## Trigger

Nutze diesen Skill für 3–8-wöchige Blöcke innerhalb einer aktiven Saisonphase.

## Voraussetzungen

Benötigt Saison-/Makrokontext, Performance-Modell, jüngste Trainings- und Testdaten, verfügbare Trainingstage sowie aktuelle Restriktionen.

## Ablauf

1. **Primäradaptation wählen.** Genau einen dominanten Entwicklungsfokus benennen.
2. **Erhaltungsqualitäten festlegen.** Sekundäre Qualitäten mit minimal wirksamer Dosis schützen.
3. **Belastungsstrategie formulieren.** Umfang, Intensitätscharakter und erwartete Progression als Zielkorridor beschreiben.
4. **Entry-Kriterien prüfen.** Nur starten, wenn gesundheitliche, technische und zeitliche Voraussetzungen passen.
5. **Recovery-Logik definieren.** Belastungs-/Entlastungsverhältnis reaktionsbasiert planen; Deload nicht nur kalenderbasiert.
6. **Exit-Kriterien setzen.** Performance-, Qualitäts-, Toleranz- oder Zeitkriterien definieren.
7. **Re-Evaluation planen.** Test oder Standard-Session nur dann einbauen, wenn daraus eine Blockentscheidung folgt.

## Alters- und Geschlechtsregeln

Bei 50+ Power und Maxkraft nicht aus Vorsicht automatisch streichen; Exposition, Technik, Vorverletzung und Recovery-Verlauf entscheiden. Bei weiblichen Athleten symptom-informed statt kalenderphasengesteuert planen.

## Prüfungen

- Gibt es genau eine Primäradaptation?
- Sind Sekundärqualitäten und deren Erhaltungsdosis benannt?
- Sind Entry-/Exit-Kriterien messbar oder beobachtbar?
- Ist Progression an Reaktion und Qualität gebunden?
- Gibt es ein klares Verhalten bei ausbleibender oder negativer Adaptation?

## Fehlerbehandlung

- **Mehrere Primärziele:** priorisieren oder getrennte Blöcke bilden.
- **Fehlende Baseline:** konservativen Start und frühen Standardtest einplanen.
- **Health constraint:** nur freigegebene Belastungsmuster einplanen und ggf. Health-Routing auslösen.

## Übergabe

Output ist `sport-mesocycle.json` gemäß `$defs.mesocycle`. `sport-microcycle-planning` konkretisiert daraus die nächste kurze Lastverteilung.

## Abschlusskriterien

Der Skill endet, wenn Primäradaptation, Erhaltungsziele, Lastkorridor, Entry-/Exit-Kriterien, Recovery-Logik und Re-Evaluation eindeutig vorliegen.
