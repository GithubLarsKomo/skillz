---
name: learning-path-planner
description: Plant aus einem Course-Concept-Graph eine didaktisch begründete Modul- und Lektionenreihenfolge mit Voraussetzungen, Einstiegspunkten, optionalen Abkürzungen und Abschlusskompetenzen. Verwenden für Course Builder und Learning Paths nach Multi-Source-Synthese.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - course-concept-graph
outputs:
  - learning-path.json
lastEvaluated: 2026-08-28
---

# Learning Path Planner

## Ziel

Aus dem Konzeptgraphen wird ein lernbarer Kurs, nicht bloß eine sortierte Playlist.

## Planungsprinzipien

1. Voraussetzungen vor abhängigen Kompetenzen;
2. gemeinsamer Kern vor Spezialvarianten;
3. ein Modul hat ein klares Kompetenzversprechen;
4. neue Begriffe pro Lektion begrenzen;
5. Erklärung -> geführte Anwendung -> selbständige Anwendung;
6. Wiederholung wird als Spacing/Practice eingesetzt, nicht als Inhaltsduplikat;
7. Konflikte und Varianten werden an der Stelle behandelt, an der Lernende den gemeinsamen Kern bereits verstehen.

## Kursstruktur

Default:

`orientation -> foundations -> mental model -> mechanisms -> guided application -> variants/conflicts -> independent application -> consolidation/assessment`

Ein Kurs kann davon abweichen, wenn Zielgruppe oder Stofflogik es verlangen.

## Module

Jedes Modul enthält mindestens:

- `moduleId`, Titel, Kompetenzversprechen;
- Eingangsvoraussetzungen;
- Lernziele mit beobachtbaren Verben;
- zugeordnete Concepts/Claims/Source-IDs;
- Lektionen in begründeter Reihenfolge;
- geplante Visuals/Übungen;
- Checkpoint;
- Exit Criteria;
- geschätzte qualitative Belastung `light | medium | heavy`.

Zeitangaben dürfen nur als Planungsschätzung ausgewiesen werden, nicht als aus der Video-Länge abgeleitete Lernzeit.

## Lernpfad-Varianten

Optional:

- `standard` — vollständiger Kernpfad;
- `fast-track` — überspringt nachweislich beherrschte Grundlagen;
- `deep-dive` — enthält zusätzliche Varianten, Konflikte und Quellen;
- `role-specific` — priorisiert Anwendungen für eine definierte Zielgruppe.

Abkürzungen dürfen keine echte fachliche Voraussetzung umgehen.

## Eintrittsdiagnostik

Wenn sinnvoll, definiere kleine Entry Checks für angenommene Voraussetzungen. Ein bestandener Check darf einen Fast-Track freischalten; er darf keine unbekannte Kompetenz unterstellen.

## Output

`learning-path.json` enthält:

- Kursziel und Zielgruppe;
- `modules[]` und `lessons[]`;
- prerequisite map;
- standard path;
- optionale alternative paths;
- entry checks;
- checkpoints;
- completion criteria;
- open planning assumptions.

## Qualitätsfälle

**Happy Path:** Lernende erwerben erst PCR-Grundprinzip und Zykluslogik, danach quantitative/qPCR-Erweiterungen.

**Edge Case:** Expertenzielgruppe bringt Grundlagen mit -> Entry Check + Fast-Track statt erzwungener Basismodul-Wiederholung.

**Failure Case:** Ein Spezialthema wird früh platziert, obwohl zentrale Begriffe erst später erklärt werden -> Reihenfolge korrigieren.
