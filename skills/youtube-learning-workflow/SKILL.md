---
name: youtube-learning-workflow
description: Orchestriert die tiefgehende Analyse eines YouTube-Videos zu evidenzgebundenen Key Take-Home Messages und optionalen derived SOPs, plant passende Diagramme/SVGs/Bilder, bindet alles an DESIGN.md und erzeugt wahlweise Landingpage-HTML, Präsentation und DOCX/PDF mit Cross-Format-QA. Verwenden für YouTube-Learner, Video-to-SOP, Video-to-Study-Guide oder Video-to-Presentation; nicht zum Umgehen von YouTube-Zugriffsschutz oder zur ungeprüften Freigabe regulierter SOPs.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - youtube-video-ingestion
  - multimodal-learning-analysis
  - learning-summary-synthesis
  - procedure-sop-extractor
  - learning-visual-planner
  - learning-content-design-system
  - learning-svg-generator
  - learning-image-generator
  - learning-landingpage-renderer
  - learning-document-delivery
  - learning-artifact-qa
  - template-presentation-workflow
outputs:
  - learning-content-model.json
  - youtube-learning-run.json
lastEvaluated: 2026-08-28
---

# YouTube Learning Workflow

## Ziel

Ein einzelnes Video wird einmal fachlich analysiert und anschließend aus **derselben kanonischen Learning-Basis** in mehrere Medien projiziert.

```text
YouTube source
  -> ingestion
  -> multimodal evidence
  -> summary / optional SOP
  -> learning-content-model.json
  -> visual plan
  -> DESIGN.md authority
  -> SVG / image assets
  -> HTML | PPTX | DOCX -> PDF
  -> cross-format QA
```

## Nutzeroptionen

Wenn nicht anders angegeben, leite pragmatisch ab:

- `mode`: `summary | sop | full`;
- `formats`: eine oder mehrere aus `html | pptx | docx | pdf`;
- `language`: Quellsprache oder gewünschte Ausgabesprache;
- `audience`: general | professional | expert | management | training;
- `depth`: concise | standard | deep;
- Design-/Corporate-/Template-Kontext.

Keine unnötige Abfrage, wenn Ziel und Format aus dem Auftrag klar sind.

## Workflow

### 1. Source Lock

`youtube-video-ingestion` ausführen. Video-ID, URL, Transcript-Herkunft und Zugriffseinschränkungen fixieren.

### 2. Multimodale Evidence Map

`multimodal-learning-analysis` ausführen. Transcript + visuelle Demonstrationen + Metadaten gemeinsam auswerten.

### 3. Lernkern

`learning-summary-synthesis` erzeugt Key Takeaways und Mental Model.

Wenn `mode=sop|full` oder das Video klar einen Prozess demonstriert, `procedure-sop-extractor` ausführen. Fehlende kritische Parameter dürfen die SOP-Ausgabe auf einen Entwurf begrenzen.

### 4. Kanonisches Learning-Modell assemblieren

`learning-content-model.json` referenziert, ohne Subskill-Ownership zu duplizieren:

- Source/Video;
- Evidence Map;
- Summary;
- optional Procedure;
- Lernziele;
- Kapitel;
- Terminologie;
- Timestamp Map;
- offene Evidenzlücken;
- angeforderte Ausgabeformate.

Dies ist die inhaltliche Source of Truth für alle Renderer.

### 5. Visuals planen

`learning-visual-planner` entscheidet je Botschaft, ob Quellframe, SVG/Diagramm oder generierte Illustration geeignet ist.

### 6. DESIGN.md Authority Lock

`learning-content-design-system` ausführen.

- Bei neutralem Lernartefakt gelten Projekt-DESIGN.md + `docs/learning-content/DESIGN.md`.
- Bei Corporate Content gewinnt der entsprechende Corporate-Vertrag.
- Für EUROIMMUN gilt zusätzlich zwingend `docs/corporate/euroimmun/DESIGN.md` einschließlich Corporate Design Gate.

### 7. Visual Assets erzeugen

- strukturierte Diagramme/Schematics -> `learning-svg-generator`;
- erklärende/realistische Illustration -> `learning-image-generator`;
- Originalframe nur wenn inhaltlich nötig und provenance-/rights-seitig zulässig.

Visuals dürfen keine neuen fachlichen Claims einführen.

### 8. Ausgabe erzeugen

**HTML** -> `learning-landingpage-renderer`.

**PPTX** -> `template-presentation-workflow`. Educational Storyline als Default:

`why it matters -> mental model -> key concepts -> how it works -> demonstrated procedure -> critical details -> mistakes -> takeaways`

Bei bestätigtem EUROIMMUN-Kontext ist der EUROIMMUN-Corporate-Wrapper/Template-Kontext zu verwenden und der Corporate Design Gate nachzuweisen.

**DOCX/PDF** -> `learning-document-delivery`.

### 9. Cross-Format QA

`learning-artifact-qa` ausführen. Nach jeder materiellen Korrektur neu rendern und erneut prüfen.

## Ausgabe-Manifest

`youtube-learning-run.json` dokumentiert:

- Video/source identity;
- Zugriffsmodus;
- Output mode/formats;
- Content-model fingerprint;
- Design authority chain;
- erzeugte Subskill-Artefakte;
- Render coverage;
- offene Warnings;
- finalen QA-Status.

Der Orchestrator erklärt Subskill-Artefakte nicht zusätzlich als eigene Outputs; er referenziert sie im Manifest.

## Grenzen

- v1 verarbeitet ein Video pro Run. Playlists werden als getrennte Runs behandelt; eine Multi-Video-Synthese ist ein eigener späterer Workflow.
- Kein Zugriffsschutz umgehen.
- Keine langen Transcript-Reproduktionen.
- Keine generierten Visuals als Quellbeweis.
- Keine regulierte SOP ohne externe fachliche/Quality-Freigabe.
- Kein `final`-Status ohne vollständige QA der tatsächlich ausgelieferten Formate.

## Qualitätsfälle

**Happy Path:** öffentlich zugängliches Video mit gutem Transcript und relevanten visuellen Demonstrationen -> evidenzgebundene Summary, passende Visuals und mehrere konsistente Ausgabeformate.

**Edge Case:** Transcript vorhanden, aber visuelle Demonstration teilweise unlesbar -> Summary möglich, Prozessdetails bleiben `unknown`/niedrige Confidence, SOP ggf. unvollständig.

**Failure Case:** Workflow versucht fehlende Parameter zu erfinden, Originalframes massenhaft zu reproduzieren oder Corporate-Design ohne Gate zu liefern -> stoppen und korrigieren.

## Abschluss

Abgeschlossen, wenn alle angeforderten Artefakte dieselbe Learning-Basis verwenden, Visuals und Designautorität nachvollziehbar sind und `learning-artifact-qa` für die finale Revision PASS meldet.
