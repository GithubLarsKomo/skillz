---
name: creative-writing-workflow
description: Orchestriert Creative Writing nach vorgelagertem Grilling von Ziel, Publikum, Autor-Modus und Format über Craft-Analyse und den passenden Science-Storytelling- oder Fiction-Series-Pfad bis zur optionalen EPUB3-Ausgabe für TTS-Reader wie ElevenReader. Verwenden als Haupteinstieg für populärwissenschaftliche Langform und Science-/Fantasy-Fiction; Fachlogik der Worker, Evidence Claims, Story Bible und EPUB-Rendering nicht duplizieren.
---

# Creative Writing Workflow

## Zweck

Ein gemeinsamer Einstieg in zwei unterschiedliche Wahrheitsmodelle:

- **Science Storytelling:** Evidenz muss erhalten bleiben.
- **Fiction Series:** Canon und Knowledge States müssen konsistent bleiben.

Der Orchestrator routet und dokumentiert; er übernimmt nicht die Fachlogik der Worker.

## Harte Vorbedingung: Grilling

Vor einem substantiellen Lauf `round-based-requirements-grilling` verwenden beziehungsweise einen bestätigten Handoff wiederverwenden.

Mindestens klären:

- Mission `science|fiction`;
- Zielpublikum;
- gewünschte Wirkung;
- Sprache;
- Umfang/Format;
- Autor-Modus `coach|coauthor|writer|editor`;
- vorhandenes Material;
- gewünschte Ausgabe;
- bei EPUB: TTS-/ElevenReader-Ziel und gewünschte Voice-Charakteristik;
- Erfolgskriterien und Nicht-Ziele.

Bereits geklärte Entscheidungen nicht erneut abfragen.

## Optionaler Idea Capture

Wenn das Projekt aus längerfristig gesammelten Gedanken entsteht, `thought-to-concept-flow` nutzen. Rohideen bleiben dort zunächst Ideen; eine Übernahme in Science Claims oder Fiction Canon erfolgt nur durch den zuständigen Domain-Pfad.

## Craft Context

`mentor-text-craft-analysis` verwenden, wenn Referenzwerke oder gezielte Handwerksfragen vorliegen. Das Craft Model bleibt abstrakt und darf keine Autorenstimme kopieren.

## Routing

### Science

`science-storytelling-workflow`:

```text
evidence
 -> audience/explanation model
 -> narrative draft
 -> workshop
 -> creative revision
 -> scientific fidelity recheck
 -> science-story.md
```

### Fiction

`fiction-series-writing-workflow`:

```text
world + ensemble + series architecture
 -> story bible
 -> draft contract
 -> draft
 -> workshop
 -> revision
 -> continuity
 -> canon promotion
 -> fiction-manuscript.md
```

## Project Second Brain

Bei langfristigen Projekten wesentliche Zustandsänderungen ab dem Grilling über `project-second-brain` dokumentieren.

Science Evidence bzw. Fiction Story Bible bleiben kanonische Fachartefakte und werden nicht in Project Memory dupliziert.

## EPUB Delivery

Wenn EPUB/TTS gewünscht ist, nach dem jeweiligen Domain Gate `creative-writing-epub-delivery` ausführen.

Der Creative-Writing-Orchestrator **besitzt das EPUB nicht**. Er verweist in `creative-writing-run.json` auf das vom Delivery-Skill erzeugte `creative-writing.epub`.

## Run Manifest

```json
{
  "schemaVersion": 1,
  "grillingHandoffRef": "...",
  "mission": "science|fiction",
  "authorMode": "coach|coauthor|writer|editor",
  "domainRunRef": "...",
  "projectMemory": null,
  "deliveryRequested": true,
  "deliveryRunRef": "...",
  "status": "pass|review|fail",
  "nextAction": "..."
}
```

## Qualitätsgate

- **Grilling vor Produktion.**
- **Science Claims und Fiction Canon haben getrennte Eigentümer.**
- Kein One-shot-Langformdraft als Default bei ungeklärter Architektur.
- Autor-Modus wird respektiert.
- Kein finaler EPUB-Handoff vor Domain-, Listener- und EPUB-Gates.
- Project Second Brain und Story Bible nicht vermischen.
- Alternative Science-/Fiction-Routen werden im Manifest explizit, nicht als statische Doppelpflicht behandelt.

## Abschluss

Abgeschlossen, wenn der Auftrag über den richtigen Domain-Pfad geführt, die relevanten Gates bestanden, der Projektzustand nachvollziehbar dokumentiert und bei gewünschter Audio-/Reader-Ausgabe ein geprüfter Delivery-Handoff erzeugt wurde.
