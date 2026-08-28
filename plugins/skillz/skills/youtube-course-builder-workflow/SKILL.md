---
name: youtube-course-builder-workflow
description: Baut aus mehreren YouTube-Videos oder einem Multi-Source-Learning-Modell einen modularen Learning Path mit Voraussetzungen, Lernzielen, Übungen, Wissenchecks und konsistenten Kursartefakten in HTML/PPTX/DOCX/PDF. Verwenden für Course Builder, Curriculum aus Videoquellen oder strukturierte Learning Paths; nicht als psychometrisch validierte Prüfung oder automatische Zertifizierung.
---

# YouTube Course Builder Workflow

## Ziel

Course Concept, Learning Path und Activities bleiben in diesem Skill. Nach dem Lock von `course-learning-model.json` wird die gemeinsame Design-, Visual-, Render- und Cross-Format-QA-Schicht über `learning-delivery-workflow` ausgeführt.

Aus einer Playlist, einem URL-Set oder einem bestehenden `multi-source-learning-model.json` wird ein **didaktisch strukturierter Kurs**. Die Reihenfolge folgt fachlichen Voraussetzungen und Lernzielen, nicht der Reihenfolge der Videos.

```text
videos / playlist / multi-source model
 -> multi-source synthesis
 -> course concept graph
 -> learning path
 -> activities + knowledge checks
 -> course-learning-model.json
 -> visual plan + DESIGN authority
 -> course landing page | presentation | DOCX -> PDF
 -> course QA
```

## Nutzeroptionen

Pragmatisch ableiten, wenn nicht explizit gesetzt:

- `audience`: general | professional | expert | management | training;
- `courseDepth`: essentials | standard | deep;
- `pathMode`: standard | fast-track | deep-dive | role-specific;
- `formats`: html | pptx | docx | pdf;
- `assessment`: none | checkpoints | full-formative;
- Sprache und Corporate-/Template-Kontext.

## Workflow

### 1. Quellenbasis

Wenn URLs/Playlist geliefert werden, `youtube-playlist-learning-workflow` ausführen. Liegt bereits ein valides `multi-source-learning-model.json` vor, dieses als Source of Truth verwenden.

### 2. Course Concept Graph

`course-concept-graph` erzeugt fachliche Concepts, Kompetenzen und Voraussetzungskanten. `prerequisite-of` muss azyklisch sein.

### 3. Learning Path

`learning-path-planner` erzeugt Module, Lektionen, Entry Checks, Checkpoints und Exit Criteria. Playlist-Reihenfolge ist ausdrücklich nicht bindend.

### 4. Aktivitäten

`learning-activity-generator` erzeugt formative Übungen und Knowledge Checks. Jede Aufgabe verweist auf Lernziel und Evidence/Claim-IDs.

### 5. Kanonisches Kursmodell

`course-learning-model.json` ist die einzige semantische Rendering-Basis und enthält mindestens:

- Source- und Multi-Source-Fingerprints;
- Zielgruppe, Kursziel, Annahmen;
- Concept Graph Reference;
- Module/Lektionen und prerequisite map;
- learning objectives;
- activities / knowledge checks;
- consensus/conflict/open states;
- source map;
- visual plan references;
- requested formats;
- Design authority chain.

Alle Renderer verwenden denselben unveränderlichen Course-Fingerprint.

### 6. Delivery und Course-QA

`learning-delivery-workflow` mit `course-learning-model.json`, angeforderten Formaten und dem kombinierten Learning-/Course-/Corporate-Designkontext ausführen. Visualplanung, Assets, HTML/PPTX/DOCX/PDF sowie Cross-Format- und Render-QA gehören ausschließlich in diese Delivery-Schicht.

Der Course Builder besitzt nur die **kurssemantischen** Gates:

- prerequisite graph ist azyklisch;
- jedes Pflichtmodul besitzt Lernziel und Exit Criteria;
- jede formative Frage ist auf Claim/Evidence rückführbar;
- ungelöste materielle Konflikte werden nicht zu eindeutigen Prüfungsantworten;
- keine erfundenen Bestehensgrenzen;
- keine Formatausgabe verwendet eine abweichende Modulreihenfolge ohne dokumentierten Grund;
- Delivery-Run und Course-Fingerprint sind im `youtube-course-builder-run.json` referenziert.

## Grenzen

- Kein SCORM/LMS-Paket in v1.
- Keine Lernfortschrittsspeicherung oder Benutzerkonten.
- Keine psychometrische Kalibrierung.
- Keine Zertifizierung/Kompetenzfreigabe.
- Kein automatisches Überspringen echter Voraussetzungen.

## Qualitätsfälle

**Happy Path:** 10–50 fachlich verwandte Videos -> deduplizierter Kurs mit Grundlagen, Anwendungen, Varianten und formativen Checks.

**Edge Case:** Expertenkurs -> Entry Checks erlauben Fast-Track, ohne erforderliches Vorwissen zu erfinden.

**Failure Case:** Course Builder kopiert Playlist-Reihenfolge und generiert dazu Trivia-Fragen ohne Lernziel-/Evidenzbindung -> stoppen und neu planen.

## Abschluss

Abgeschlossen, wenn Course Graph, Learning Path, Aktivitäten und alle ausgelieferten Formate denselben Course-Fingerprint verwenden und die finale Course-QA PASS meldet.
