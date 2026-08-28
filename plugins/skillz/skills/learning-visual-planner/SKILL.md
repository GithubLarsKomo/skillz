---
name: learning-visual-planner
description: Plant für evidenzgebundene Lerninhalte die jeweils informationsstärkste Visualisierung und entscheidet zwischen Quellframe, Diagramm/SVG, Chart, annotiertem Screenshot oder generierter Illustration. Verwenden vor Grafik- oder Bilderzeugung; nicht zum Erzeugen dekorativer Assets oder zum Verändern fachlicher Claims.
---

# Learning Visual Planner

## Grundsatz

**Message first, visual second.** Ein Visual ist nur gerechtfertigt, wenn es Verständnis, Orientierung, Erinnerung oder sichere Ausführung verbessert.

## Repräsentationswahl

Bevorzugte Zuordnung:

| Lernproblem | Darstellung |
|---|---|
| Prozess / Reihenfolge | Flow, Step Diagram, Timeline |
| Ursache/Wirkung | Causal Diagram |
| Systemaufbau | Architecture / annotated schematic |
| Entscheidung | Decision Tree |
| Vergleich | Matrix / comparison table |
| Messdaten | Chart, nur bei echten Daten |
| UI-Handlung | gezielter Screenshot + Annotation |
| räumliche/physische Handlung | Illustration oder selektierter Quellframe |
| abstraktes Konzept | explanatory illustration |
| Wissensbeziehungen | Concept Map |

SVG/Diagramm wird bevorzugt, wenn Geometrie, Labels und Logik wichtiger sind als Fotorealismus.

## `learning-visual-plan.json`

Jedes Asset enthält mindestens:

```json
{
  "id": "V-01",
  "message": "...",
  "sourceClaims": ["C-01"],
  "timestamps": ["00:12:14"],
  "visualType": "process-diagram",
  "assetMode": "generated-svg",
  "labels": [],
  "altTextIntent": "...",
  "targetSurfaces": ["html", "pptx", "docx", "pdf"],
  "designRequirements": [],
  "evidenceRole": "explanatory"
}
```

## Source-Frame-Regel

Originalframes sind **Evidenzanker**, nicht Default-Illustrationen. Nutze sie nur, wenn der reale Zustand selbst relevant ist. Für übertragbare Lernlogik bevorzuge neu gezeichnete, sachlich abgeleitete Visuals.

## Anti-Slop

Nicht planen:

- dekorative Stock-/AI-Bilder ohne Lernfunktion;
- beliebige Hero-Illustrationen, die keinen Claim transportieren;
- 3D-/Glassmorphism-Effekte ohne Informationswert;
- Text, der eigentlich HTML/SVG sein sollte, als Rasterbild;
- komplexe Diagramme nur um Fläche zu füllen;
- Farbvielfalt ohne semantische Rolle.

## Qualitätsgate

- jedes Visual besitzt eine klare Lernbotschaft;
- jeder fachliche Bestandteil ist auf Claims/Evidenz zurückführbar;
- geeigneter Asset-Typ ist begründet;
- `evidenceRole` trennt `source`, `explanatory` und `illustrative-only`;
- target surfaces und DESIGN.md-Anforderungen sind vor Rendering bekannt.

## Abschluss

Abgeschlossen, wenn SVG- und Bildgeneratoren ein eindeutiges, evidenzgebundenes Briefing erhalten, ohne eigene fachliche Entscheidungen treffen zu müssen.
