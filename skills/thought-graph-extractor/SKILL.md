---
name: thought-graph-extractor
description: Analysiert ein normalisiertes Thought Journal, extrahiert Themen, Aussagen, Ziele, Fragen, Widersprüche und belastbar begründete Beziehungen und erzeugt daraus einen nachvollziehbaren semantischen Graphen mit Confidence und Provenance. Verwenden, wenn unstrukturierte Gedanken zu einem Obsidian-, Mermaid- oder Mindmap-fähigen Wissensgraphen verdichtet werden sollen; finale Zielkonzepte gehören nachgelagert in thought-to-concept-flow.
userFacing: true
implicitInvocation: true
category: research-knowledge
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - thought-capture-journal
  - structured-knowledge-artifact
outputs:
  - thought-graph.json
  - thought-graph-summary.md
  - structured thought artifacts
lastEvaluated: 2026-08-23
---

# Thought Graph Extractor

## Zweck

Verdichte rohe Gedanken zu einer expliziten, prüfbaren Bedeutungsstruktur. Anders als `knowledge-map-generator`, der vorhandene explizite Relationen lediglich projiziert, darf dieser Skill Beziehungen aus dem Thought Journal **ableiten**, muss jede Ableitung aber mit Herkunft, Begründung und Confidence kennzeichnen.

## Knotentypen

Mindestens zulässig:

- `goal` – gewünschter Zustand oder Wirkung,
- `idea` – Vorschlag, Ansatz oder Hypothese,
- `claim` – Aussage über die Welt,
- `constraint` – Grenze, Muss oder Nicht-Ziel,
- `question` – offene Frage,
- `evidence` – angeführter Beleg oder Beobachtung,
- `risk` – mögliches negatives Ereignis,
- `action` – konkrete Aktivität,
- `stakeholder` – relevante Rolle oder Gruppe,
- `theme` – abstrahierendes Cluster,
- `decision` – ausdrücklich getroffene Festlegung.

## Relationstypen

Bevorzuge ein kleines kontrolliertes Vokabular:

- `supports`, `contradicts`, `depends_on`, `causes`, `enables`,
- `refines`, `example_of`, `part_of`, `related_to`,
- `answers`, `raises`, `mitigates`, `blocks`, `serves_goal`.

## Workflow

1. Alle Journal-Einträge mit IDs und Zeitbezug laden.
2. Atomare semantische Einheiten extrahieren, ohne den Rohtext zu verlieren.
3. Doppelte oder nahezu identische Einheiten zusammenführen; Original-SourceRefs erhalten.
4. Knotentypen bestimmen und Unsicherheit sichtbar halten.
5. Beziehungen nur anlegen, wenn sie explizit genannt oder aus dem Kontext plausibel ableitbar sind.
6. Jede inferierte Edge mit `inference=true`, Confidence zwischen 0 und 1 und kurzer Begründung versehen.
7. Widersprüche nicht glätten. Gegenläufige Aussagen durch `contradicts` verbinden oder als unresolved markieren.
8. Cluster/Themen aus hoher semantischer Nähe bilden; Cluster sind Projektionen und ersetzen keine Originalknoten.
9. Lücken als `question`-Knoten oder offene Relationshypothesen ausgeben.
10. Relevante Einheiten zusätzlich als `structured-knowledge-artifact` verpacken und danach an `knowledge-map-generator` übergeben.

## Graph-Vertrag

```json
{
  "schemaVersion": 1,
  "nodes": [
    {
      "id": "idea-001",
      "type": "idea",
      "label": "...",
      "summary": "...",
      "sourceRefs": ["thought-20260823-2217-001"],
      "confidence": 0.96
    }
  ],
  "edges": [
    {
      "id": "edge-001",
      "from": "idea-001",
      "to": "goal-001",
      "type": "serves_goal",
      "sourceRefs": ["thought-20260823-2217-001"],
      "inference": true,
      "confidence": 0.82,
      "rationale": "Der Gedanke beschreibt den Ansatz ausdrücklich als Mittel für das Ziel."
    }
  ],
  "clusters": [],
  "openQuestions": [],
  "contradictions": []
}
```

## Confidence-Regeln

- `>=0.90`: explizit im Text oder mehrfach unabhängig gestützt,
- `0.70–0.89`: starke kontextuelle Ableitung,
- `0.50–0.69`: plausible, aber prüfbedürftige Hypothese,
- `<0.50`: nicht als reguläre Edge übernehmen; als Kandidat/offene Frage ausgeben.

## Qualitätsgate

- Jeder Knoten besitzt mindestens einen SourceRef oder ist klar als abstraktes Cluster markiert.
- Jede inferierte Edge besitzt Rationale und Confidence.
- Keine widersprüchlichen Gedanken werden zu einer scheinbaren Konsensposition verschmolzen.
- Zeitliche Entwicklung bleibt rekonstruierbar.
- Graph enthält nicht nur Themen, sondern auch Ziele, Abhängigkeiten, offene Fragen und Konflikte, sofern vorhanden.

## Abschluss

Der Skill endet mit einem referenziell konsistenten Thought Graph, der sowohl an `knowledge-map-generator`/`obsidian-adapter` als auch an `mermaid-knowledge-map-renderer` und `thought-to-concept-flow` übergeben werden kann.
