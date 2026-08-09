---
name: knowledge-map-generator
description: Projiziert vorhandene strukturierte Wissensartefakte und explizite Relationen in einen provider-neutralen Graphen aus Nodes, Edges und optionalen Groups. Verwenden, wenn Projekt-, Architektur-, Decision-, Domain- oder Memory-Zusammenhänge visualisiert oder an JSON Canvas, Mermaid, Graphviz, Neo4j oder andere Renderer übergeben werden sollen; der Skill erfindet keine fehlenden Beziehungen.
---

# Knowledge Map Generator

## Zweck

Erzeuge aus bestehenden Knowledge Artifacts einen portablen Graphen. Rendering und Backend-spezifische Syntax sind Adapteraufgaben.

## Vertrag

```json
{
  "schemaVersion": 1,
  "nodes": [{"id": "artifact-id", "type": "...", "label": "...", "sourceRefs": []}],
  "edges": [{"id": "...", "from": "...", "to": "...", "type": "...", "sourceRefs": []}],
  "groups": []
}
```

Node-IDs sollen Artifact-IDs wiederverwenden. Edge-Typen stammen aus expliziten Links oder aus einem vorgelagerten Fachmodell.

## Workflow

1. Bestimme Scope und Snapshot.
2. Übernimm zulässige Artefakte als Nodes.
3. Übernimm nur explizite oder vom fachlichen Producer bestätigte Relationen als Edges.
4. Markiere unresolved/conflicting Relationen statt sie zu glätten.
5. Gruppiere nur nach expliziten Metadaten oder einer angegebenen Projektion.
6. Validiere referenzielle Integrität.
7. Übergib den neutralen Graphen an einen Renderer/Adapter.

## Renderer-Grenze

JSON Canvas, Mermaid, Graphviz und Neo4j dürfen aus `knowledge-map.json` erzeugt werden, sind aber nicht kanonisch. Layout-Koordinaten oder Darstellungsattribute dürfen die fachliche Semantik nicht verändern.

## Qualitätsgate

- Jede Edge besitzt nachvollziehbare Herkunft.
- Keine Halluzination fehlender Relationen.
- Keine dangling references, außer sie sind explizit als externe Targets markiert.
- Eine Render-/Round-trip-Transformation erhält IDs und Relationstypen.
