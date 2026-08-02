---
name: knowledge-view
description: Erzeugt deterministische, schreibgeschützte Sichten auf strukturierte Wissensartefakte anhand expliziter Filter, Sortierungen, Gruppierungen und abgeleiteter Felder. Verwenden, wenn aktive Entscheidungen, offene Fragen, Memory-Einträge, Projektartefakte oder andere Knowledge Artifacts selektiv als Kontext oder Übersicht projiziert werden sollen; verändert weder Quellen noch löst der Skill Konflikte.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - structured-knowledge-artifact
outputs:
  - knowledge-view.json
lastEvaluated: 2026-08-02
---

# Knowledge View

## Zweck

Eine Knowledge View ist ein reproduzierbares Read Model über Knowledge Artifacts. Das Prinzip entspricht einer Datenbankansicht: Auswahl und Darstellung ändern die Quelle nicht.

## Vertrag

Eine View-Spezifikation enthält mindestens:
- `id`
- `sourceScopes`
- `filters`
- optionale `sort`, `groupBy`, `fields`, `derivedFields`
- `includeStates` (standardmäßig nur `active`, sofern der aufrufende Fach-Skill nichts anderes verlangt)

Der Output enthält:
- die angewandte View-Spezifikation,
- referenzierte Artifact-IDs,
- projizierte Felder,
- `asOf` bzw. den Snapshot-Bezug.

## Workflow

1. Lade ausschließlich bereits zulässige Artefakte aus dem angegebenen Scope.
2. Wende Lifecycle-Filter vor inhaltlichen Filtern an.
3. Filtere und sortiere deterministisch.
4. Berechne abgeleitete Felder ausschließlich aus vorhandenen Werten; keine neuen fachlichen Claims.
5. Erhalte Artifact-IDs und SourceRefs für Drill-down und Audit.
6. Gib die View ohne Mutation der Quellen zurück.

## Grenzen

- Kein Last-write-wins oder Conflict Resolution.
- Keine Memory-Aktivierung.
- Keine automatische Speicherung der View als neues Memory.
- Keine stillen Joins über Scopes, die der Aufrufer nicht freigegeben hat.

## Qualitätsgate

Die gleiche View-Spezifikation auf demselben Snapshot muss dasselbe Ergebnis liefern. Jede Zeile muss auf ihre Quellartefakte zurückführbar sein. Offene Konflikte dürfen nicht durch Filterung als scheinbar eindeutige Wahrheit präsentiert werden.
