---
name: sport-goal-performance-model
description: Übersetzt ein sportliches Ziel in Outcome-, Performance- und Prozessziele sowie eine priorisierte KPI- und Limiter-Struktur. Verwenden vor Saison- oder Blockplanung, wenn Zieltermin, Wettkampfpriorität und messbare Leistungsanforderungen geklärt werden müssen; nicht für die konkrete Wochenprogrammierung.
---

# Sport Goal Performance Model

Formuliere aus einem breiten Ziel eine überprüfbare Zielhierarchie und ein sportartspezifisches Performance-Modell.

## Trigger

Nutze diesen Skill bei Wettkampf-, Leistungs- oder Entwicklungszielen, bevor Saison-, Meso- oder Mikroplanung beginnt.

## Voraussetzungen

Benötigt ein `athlete-profile.json`, Zielbeschreibung, Zieltermin soweit bekannt, Wettkampf-/Disziplinkontext und vorhandene Leistungsdiagnostik oder Benchmarks.

## Ablauf

1. **Outcome-Ziel klären.** Ergebnis, Termin und Priorität A/B/C festhalten.
2. **Performance-Ziele ableiten.** Messbare physiologische, technische oder kraftbezogene Leistungsmarker formulieren.
3. **Prozessziele definieren.** Beeinflussbare Verhaltens- und Trainingsziele festlegen.
4. **Limiter modellieren.** Belegte Limiter, plausible Hypothesen und Unbekanntes getrennt führen.
5. **KPI-Baum bauen.** Nur Metriken aufnehmen, die eine Trainings- oder Testentscheidung unterstützen.
6. **Trade-offs explizit machen.** Bei konkurrierenden Qualitäten festlegen, was priorisiert, erhalten oder bewusst nachrangig behandelt wird.
7. **Erfolgskriterien setzen.** Zielwerte als Bereiche oder Schwellen mit Messmethode, Datum und Unsicherheit dokumentieren.

## Alters- und Geschlechtsregeln

Zielambition nicht allein wegen 50+ absenken. Alters- oder sex-spezifische Normwerte dürfen Kontext liefern, ersetzen aber keine individuellen Baselines. Zyklus-/Menopausenkontext nur berücksichtigen, wenn individuelle Symptome oder Daten die Zielumsetzung tatsächlich beeinflussen.

## Prüfungen

- Sind Outcome-, Performance- und Prozessziele sauber getrennt?
- Hat jeder KPI eine konkrete Entscheidung oder Testfunktion?
- Sind Limiter evidenzgraduiert statt behauptet?
- Sind Zielwerte mit Datum, Einheit und Messmethode versehen?
- Werden Alters-/Geschlechtsannahmen nicht als unbelegte Limiter verwendet?

## Fehlerbehandlung

- **Kein Zieltermin:** offenen Entwicklungszeitraum mit Re-Evaluation definieren.
- **Keine Diagnostik:** Performance-Hypothesen kennzeichnen und Testbedarf ableiten.
- **Mehrere Hauptziele:** Prioritäten und Konflikte sichtbar machen, nicht alle gleichzeitig zu A-Zielen erklären.

## Übergabe

Output ist `sport-performance-model.json` gemäß `$defs.performanceModel` in `schemas/sport-athlete-management-v1.schema.json`. `sport-season-periodization` konsumiert Zielhierarchie, Wettkampfprioritäten und KPI-Baum.

## Abschlusskriterien

Der Skill endet, wenn ein messbares, priorisiertes und evidenzgraduiertes Performance-Modell vorliegt, das Saisonplanung ermöglicht ohne bereits konkrete Wochenlasten vorwegzunehmen.
