---
name: sport-testing-battery
description: Wählt eine minimale, sport- und zielbezogene Leistungsdiagnostik-Batterie aus und legt Protokoll, Zeitpunkt, Wiederholbarkeit und Entscheidungsnutzen fest. Verwenden zur Testplanung über Saisonphasen; nicht für unnötige Maximaltests kurz vor Wettkämpfen oder medizinische Diagnostik.
---

# Sport Testing Battery

Teste nur, wenn ein Ergebnis eine Entscheidung verändert. Die beste Batterie ist nicht die größte, sondern die kleinste valide Menge von Messungen für Ziel, Sport und Saisonphase.

## Ablauf

1. **Entscheidungsfrage formulieren.** Welche Trainings-/Leistungsentscheidung soll der Test ermöglichen?
2. **KPI koppeln.** Test direkt einem Performance-Ziel oder Limiter zuordnen.
3. **Messdomäne wählen.** Je nach Bedarf aerobe/anaerobe Schwellen, VO2-nahe Feld-/Ergotests, Sprintleistung, Maximalkraft/e1RM, Isometrie, Sprung/Power, sportartspezifische Leistung oder funktionelle Reserve auswählen.
4. **Minimalbatterie bauen.** Redundante Tests entfernen und Belastung der Tests gegen Trainingswert abwägen.
5. **Protokoll standardisieren.** Gerät, Warm-up, Stufen-/Pausenstruktur, Tageszeit, Fueling, Umwelt und Auswertungsversion dokumentieren.
6. **Reliabilität sichern.** Gleiche Kernbedingungen bei Retests; technische/methodische Änderung separat kennzeichnen.
7. **Zeitpunkt wählen.** Baseline, Blockende, strategische Retests und Wettkampfproximity berücksichtigen.
8. **Interpretation routen.** Messdaten an `sport-performance-diagnostics`; dieser Skill erfindet keine Schwelle aus der Testauswahl.

## 50+ und Geschlecht

Bei Masters kann funktionelle Reserve, Kraft und Power zusätzlich wertvoll sein, ohne dass dies sportartspezifische Leistungstests ersetzt. Alter allein verbietet keinen Maximaltest; Safety, Erfahrung, Technik und Nutzen entscheiden. Geschlecht bestimmt nicht automatisch andere Testprotokolle; physiologisch relevante Kontexte werden dokumentiert, wenn sie die Vergleichbarkeit beeinflussen.

## Safety

Bei medizinischen Red Flags oder fehlender Belastungsfreigabe keine maximalen Feld-/Ergotests anordnen. Kurz vor einem A-Wettkampf keine ermüdende Testbatterie ohne klaren Entscheidungsnutzen.

## Prüfungen

- Ändert jedes Testergebnis potenziell eine Entscheidung?
- Ist der Test valide für Sport/Ziel und wiederholbar?
- Sind Vergleichsbedingungen dokumentiert?
- Wird Testlast im Mikro-/Taperkontext berücksichtigt?

## Übergabe

`sport-testing-plan.json` enthält Testfragen, KPI-Mapping, Protokolle, Timing, Standardisierungsbedingungen, erwartete Outputs, Abbruchregeln und Retestplan.

## Abschlusskriterien

Eine minimale, sichere und wiederholbare Testbatterie mit klarer Entscheidungsverknüpfung und Übergabe an die Diagnostik liegt vor.
