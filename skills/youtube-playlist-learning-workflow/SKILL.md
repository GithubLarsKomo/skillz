---
name: youtube-playlist-learning-workflow
description: Orchestriert mehrere YouTube-Videos oder eine Playlist zu einem gemeinsamen evidenzgebundenen Lernpaket: Einzelanalyse je Video, Quellenarbitration, Deduplication, Konflikterkennung, konsolidiertes Wissensmodell und Ausgabe als Landingpage, Präsentation oder DOCX/PDF unter DESIGN.md. Verwenden für Playlist-Learner, Multi-Video-Tutorials, Kurs-Synthesen und konsolidierte SOP-Entwürfe.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - youtube-learning-workflow
  - learning-source-arbitration
  - multi-source-learning-synthesis
  - learning-delivery-workflow
outputs:
  - youtube-playlist-learning-run.json
lastEvaluated: 2026-08-28
---

# YouTube Playlist Learning Workflow

## Ziel

Die Multi-Source-Arbitration und Synthese bleiben in diesem Skill. Sobald `multi-source-learning-model.json` fixiert ist, wird die gemeinsame Design-, Visual-, Render- und Cross-Format-QA-Schicht über `learning-delivery-workflow` ausgeführt.

Mehrere Videos werden zunächst **einzeln evidenzgebunden analysiert** und erst danach zu einer gemeinsamen Lernbasis synthetisiert. Die Ausgabe folgt der Lernlogik und nicht der Video-Reihenfolge.

```text
playlist / video set
  -> per-video youtube-learning analysis
  -> source registry
  -> learning-source-arbitration
  -> multi-source-learning-synthesis
  -> multi-source-learning-model.json
  -> visual plan + DESIGN authority
  -> HTML | PPTX | DOCX -> PDF
  -> cross-format + cross-source QA
```

## Eingabe

Akzeptiert:

- Playlist-URL;
- Liste von YouTube-URLs;
- bestehende Einzelvideo-Learning-Modelle;
- Mischung aus bereits analysierten und neu zu analysierenden Videos.

Nutzeroptionen:

- `mode`: `summary | tutorial | sop | full`;
- `formats`: `html | pptx | docx | pdf`;
- `language`;
- `audience`;
- `depth`;
- optionaler Fokus/Fragestellung;
- Design-/Corporate-/Template-Kontext.

## 1. Source Set Lock

Video-IDs, URLs, Titel, Reihenfolge der Playlist und tatsächlich analysierte Quellen fixieren. Nicht zugängliche Videos bleiben als `unavailable` dokumentiert und dürfen nicht stillschweigend als analysiert gelten.

## 2. Einzelanalyse

Für jedes zugängliche Video den bestehenden `youtube-learning-workflow` bis zum kanonischen Einzelmodell ausführen. Renderer sind in dieser Phase optional; entscheidend sind Evidence Map und Learning Model.

Jedes Einzelmodell behält einen eigenen Fingerprint.

## 3. Quellenarbitration

`learning-source-arbitration` ausführen:

- Autorität und Evidenznähe;
- echte Quellenunabhängigkeit;
- methodische/zeitliche Unterschiede;
- Claim-Support und Widersprüche;
- zulässige Formulierungsstärke.

Kein Mehrheitsvotum als Wahrheitsersatz.

## 4. Multi-Source-Synthese

`multi-source-learning-synthesis` erzeugt und besitzt:

- `multi-source-learning-model.json`;
- deduplizierte Claim-Cluster;
- Consensus Core;
- qualifizierte Aussagen;
- Konflikte und offene Fragen;
- Coverage Map;
- optionale Prozess-/SOP-Varianten;
- lernlogische Kapitelstruktur.

Der Playlist-Orchestrator referenziert dieses Modell im Run-Manifest, beansprucht aber nicht selbst dessen Artifact-Ownership.

## 5. Canonical Model Lock

Das von `multi-source-learning-synthesis` erzeugte `multi-source-learning-model.json` wird zur einzigen Source of Truth für alle finalen Renderer. Es referenziert die Einzelmodell-Fingerprints und Arbitration-Artefakte.

## 6. Delivery und Cross-Source QA

`learning-delivery-workflow` mit dem kanonischen `multi-source-learning-model.json`, den angeforderten Formaten und dem Design-/Corporate-/Template-Kontext ausführen. Visualplanung, Assets, HTML/PPTX/DOCX/PDF, Render-/Parity-Gates und Cross-Format-QA gehören ausschließlich in diese gemeinsame Delivery-Schicht.

Der Playlist-Orchestrator ergänzt darauf nur die **Multi-Source-spezifischen** Prüfungen:

- alle finalen Claims bleiben auf Source-Cluster rückführbar;
- `independentSourceCount` ist korrekt;
- ungelöste Konflikte bleiben sichtbar;
- Single-Source-Aussagen werden nicht als Konsens dargestellt;
- Zahlen/Einheiten/Parameter werden nicht unzulässig gemittelt;
- keine Hybrid-SOP entsteht aus inkompatiblen Protokollen;
- alle ausgelieferten Formate referenzieren denselben Multi-Source-Fingerprint.

`youtube-playlist-learning-run.json` referenziert das `learning-delivery-bundle.json` und den zugehörigen Delivery-Run, ohne Worker-Artefakte selbst zu besitzen.

## Playlist-Skalierung

- kleine Sets: alle Videos tief analysieren;
- große Playlists: zunächst Metadaten/Chapters clustern, dann relevante Videos priorisieren;
- Sampling muss im Run-Manifest sichtbar sein;
- kein `complete-playlist`-Status, wenn Teile nicht analysiert wurden.

## Grenzen

- Zugriffsschutz wird nicht umgangen.
- Nicht zugängliche Videos werden nicht halluziniert.
- Wiederholungen desselben Ursprungs werden nicht als unabhängige Bestätigung gezählt.
- Konflikte werden nicht durch sprachliches Glätten entfernt.
- Ein konsolidierter SOP-Entwurf ist ohne fachliche/Quality-Freigabe kein kontrolliertes Dokument.

## Output-Manifest

`youtube-playlist-learning-run.json` dokumentiert Source Set, Einzelmodell-Fingerprints, Referenz auf das kanonische `multi-source-learning-model.json`, Arbitration, Synthese-Fingerprint, Sampling/Exclusions, Design Authority, Render Coverage, Konflikte/Warnings und finalen QA-Status.

## Abschluss

PASS nur bei 0 offenen Critical/Major Findings, vollständiger Renderabdeckung der angeforderten Formate und nachweisbarer Source-/Conflict-Traceability.
