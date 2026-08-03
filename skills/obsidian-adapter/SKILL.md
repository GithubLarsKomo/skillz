---
name: obsidian-adapter
description: Rendert provider-neutrale Knowledge Artifacts, Views und Maps in Obsidian-kompatible Markdown-, Bases- und JSON-Canvas-Artefakte und liest optional editierte Obsidian-Artefakte ausschließlich als nicht-kanonische Kandidaten zurück. Verwenden, wenn der bestehende Knowledge-Layer in einen Obsidian Vault projiziert oder aus Obsidian sicher zur vorgelagerten Governance/Reconciliation zurückgeführt werden soll; Obsidian bleibt Adapter, nicht semantische Quelle.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - structured-knowledge-artifact
  - knowledge-view
  - knowledge-map-generator
outputs:
  - obsidian-note.md
  - obsidian-view.base
  - obsidian-map.canvas
  - obsidian-candidate.json
lastEvaluated: 2026-08-03
---

# Obsidian Adapter

## Zweck

Dieser Skill bildet den provider-neutralen Knowledge-Layer auf Obsidian-spezifische Formate ab. Er übernimmt keine fachliche Semantik und verändert keine kanonischen Quellenzustände.

## Unterstützte Richtungen

### Export

- `structured-knowledge-artifact` -> Markdown Note mit Frontmatter und optionalen Wikilinks
- `knowledge-view` -> Obsidian Bases Definition oder statische Tabellenprojektion
- `knowledge-map-generator` -> JSON Canvas

### Kandidaten-Import

Ein editierter Obsidian-Stand darf höchstens in `obsidian-candidate.json` übersetzt werden. Dieser Kandidat ist ausdrücklich nicht kanonisch und muss bei Memory-Inhalten durch Governance, Reconciliation, optionales Approval und den kanonischen Apply-Pfad laufen.

## Nicht-Ziele

- keine Memory-Aktivierung,
- keine Conflict Resolution,
- kein Last-write-wins,
- keine automatische Übernahme manuell gezeichneter Canvas-Edges als Domainrelation,
- keine semantische Interpretation von Dateinamen, Foldern, Farben oder Canvas-Positionen,
- keine direkte kanonische Schreiboperation aus Obsidian heraus.

## Markdown Export

Erhalte mindestens:

- stabile `id`,
- `artifactType`,
- Lifecycle-State,
- Provenance/SourceRefs,
- explizite Relationstypen,
- fachlichen Inhalt.

Obsidian-Dateiname und Note-Titel sind Presentation Metadata und nicht die kanonische Identität. Renames oder Folder Moves dürfen daher die `id` nicht verändern.

Wikilinks sind Renderings vorhandener Relationen. Ein Wikilink darf keine neue Relation erzeugen, wenn der Quellvertrag diese nicht bereits enthält.

## Bases Export

Eine `.base`-Definition darf ausschließlich eine `knowledge-view` darstellen. Filter, Sortierung, Gruppierung und Formeln dürfen Präsentation und Auswahl beeinflussen, aber niemals Lifecycle, Konflikte oder Quellartefakte mutieren.

Offene Konflikte müssen sichtbar bleiben; eine View darf sie nicht so filtern, dass eine scheinbar eindeutige Wahrheit entsteht.

## JSON Canvas Export

- Node-IDs referenzieren stabile Artifact-IDs.
- Edges stammen ausschließlich aus `knowledge-map-generator`.
- Layout, Farbe, Größe, Gruppen und Position sind nicht-kanonisch.
- Manuell hinzugefügte lokale Edges werden bei Rückimport nur als untrusted candidate relations gekennzeichnet.

## Kandidaten-Import

Beim Import editierter Obsidian-Artefakte:

1. stabile IDs und bekannte SourceRefs prüfen,
2. Unterschiede zum letzten exportierten Snapshot bestimmen,
3. Darstellungseffekte von semantisch möglichen Änderungen trennen,
4. unbekannte/manuelle Relationen als Kandidaten markieren,
5. gelöschte oder fehlende Notes niemals automatisch als Forget interpretieren,
6. stale Notes dürfen superseded/rejected/expired/removed Zustände nicht reaktivieren,
7. Ergebnis ausschließlich als `obsidian-candidate.json` ausgeben.

Beispiel:

```json
{
  "schemaVersion": 1,
  "source": "obsidian",
  "baseSnapshotRef": "...",
  "changes": [],
  "candidateRelations": [],
  "warnings": [],
  "canonicalWriteAllowed": false
}
```

## CLI-Grenze

Ein Obsidian CLI oder Plugin darf als Execution Backend verwendet werden, um Notes, Bases oder Canvas-Dateien zu schreiben/lesen. CLI-Kommandos sind Implementierungsdetails und gehören nicht in den semantischen Vertrag.

Der Adapter muss auch ohne CLI durch normale Dateiarbeit implementierbar bleiben.

## Qualitätsgate

Bestanden nur wenn:

- IDs und Relationstypen beim Export erhalten bleiben,
- Markdown/Bases/Canvas keine kanonische Semantik hinzufügen,
- manuelle Obsidian-Änderungen nicht direkt kanonisch schreiben,
- stale Projektionen keine gelöschten oder superseded Zustände wiederbeleben,
- Konflikte und Lifecycle nicht durch UI-/View-Logik verborgen werden,
- Kandidaten-Import klar zwischen Presentation- und Semantic-Diff unterscheidet.

## Abschluss

Die Aufgabe endet, wenn eine Obsidian-kompatible Projektion oder ein nicht-kanonischer Kandidatenstand erzeugt wurde und der kanonische Knowledge-/Memory-Vertrag unverändert bleibt.