---
name: learning-delivery-workflow
description: Orchestriert die formatübergreifende Auslieferung eines bereits kanonischen Learning-Content-, Multi-Source- oder Course-Modells über DESIGN.md, Visualplanung, SVG/Bild-Assets, Landingpage, Präsentation, DOCX/PDF und finales Cross-Format-QA, ohne fachliche Learning-Semantik neu zu autorieren. Verwenden als interne gemeinsame Delivery-Schicht für Learning-Orchestratoren.
---

# Learning Delivery Workflow

## Zweck und Grenze

`learning-delivery-workflow` ist die gemeinsame **Delivery-Schicht** für bereits fachlich bestimmte Learning-Modelle. Er koordiniert Designautorität, Visuals, Ausgabeformate und Cross-Format-QA, besitzt aber weder die fachlichen Claims noch die Lernlogik der vorgelagerten Single-Video-, Multi-Source- oder Course-Orchestratoren.

Der Skill verhindert, dass jeder Learning-Orchestrator denselben Render-/QA-Stack erneut als eigene Ablaufverantwortung verdrahtet.

## Trigger

Intern verwenden, wenn mindestens eines der folgenden kanonischen Modelle final genug für eine Medienprojektion vorliegt:

- `learning-content-model.json` für ein einzelnes Lernobjekt oder Video;
- `multi-source-learning-model.json` für konsolidierte Mehrquelleninhalte;
- `course-learning-model.json` für einen didaktisch strukturierten Kurs.

Nicht verwenden, um Rohquellen zu analysieren, Konflikte zwischen Quellen zu entscheiden, Claims zu erfinden, Lernziele neu zu strukturieren oder einen regulierten SOP-Entwurf fachlich freizugeben.

## Voraussetzungen

Vor Delivery müssen vorliegen:

1. genau ein autoritatives kanonisches Inhaltsmodell für den aktuellen Run;
2. angeforderte Zielformate `html|pptx|docx|pdf`;
3. Zielgruppe, Sprache und Darstellungszweck;
4. verfügbarer Corporate-/Template-/DESIGN.md-Kontext oder ein ausdrücklich zulässiger Learning-Default;
5. nachvollziehbarer Content-Fingerprint und Source-/Claim-Provenance des vorgelagerten Modells.

Liegen mehrere Inhaltsmodelle vor, muss der aufrufende Orchestrator eindeutig festlegen, welches Modell für diesen Delivery-Run autoritativ ist. Der Delivery-Skill synthetisiert sie nicht selbst.

## Ablauf

### 1. Canonical Model Lock

Das gewählte Learning-Modell als einzige fachliche Source of Truth für diesen Delivery-Run fixieren. Content-Fingerprint, Modelltyp und Provenance in `learning-delivery-run.json` übernehmen.

### 2. Design Authority auflösen

`learning-content-design-system` ausführen und `learning-design-context.json` übernehmen. Corporate-/Template-Autorität hat Vorrang vor generischen Learning-Defaults. Fehlende verbindliche Designautorität darf nicht durch erfundene Markenregeln ersetzt werden.

### 3. Visualplan bestimmen

`learning-visual-planner` verwenden. Visuals müssen einen fachlichen oder didaktischen Zweck haben. Bereits ausreichende Quellframes oder vorhandene Evidenzvisuals werden nicht allein aus Stilgründen durch generierte Bilder ersetzt.

### 4. Assets erzeugen

Nur die im Visualplan geforderten Worker aufrufen:

- `learning-svg-generator` für Diagramme, Flows, Timelines, Matrizen und Schematics;
- `learning-image-generator` für erklärende Illustrationen oder realistische Lernbilder.

Manifest und Provenance der Assets erhalten. Illustrative Bilder bleiben als Illustration gekennzeichnet und werden nicht zu experimenteller Evidenz hochgestuft.

### 5. Angeforderte Formate rendern

- HTML über `learning-landingpage-renderer`;
- PPTX/PDF-Präsentation über `template-presentation-workflow`;
- DOCX/PDF-Handout über `learning-document-delivery`.

Nicht angeforderte Formate müssen nicht erzeugt werden. Renderer besitzen ihre nativen Dateien und formatbezogenen QA-Artefakte; dieser Orchestrator deklariert diese Worker-Artefakte nicht erneut als eigene Outputs.

### 6. Cross-Format-QA

`learning-artifact-qa` über alle tatsächlich erzeugten Formate und Assets ausführen. Prüfen:

- alle Kernaussagen bleiben auf das kanonische Modell rückführbar;
- Zahlen, Einheiten, Prozessreihenfolge und Einschränkungen stimmen formatübergreifend überein;
- Source-/Timestamp-/Claim-Traceability bleibt erhalten, soweit im Modell vorhanden;
- DESIGN.md wird in allen Formaten konsistent angewendet;
- alle angeforderten Render-/Parity-Gates wurden tatsächlich ausgeführt;
- kein Renderer hat Inhalte fachlich neu autoriert.

### 7. Bundle und Run Manifest erzeugen

`learning-delivery-bundle.json` referenziert die tatsächlich erzeugten Worker-Artefakte, ohne deren Ownership zu übernehmen.

Minimaler Vertrag:

```json
{
  "schemaVersion": 1,
  "modelType": "single|multi-source|course",
  "modelRef": "...",
  "contentFingerprint": "...",
  "designContextRef": "...",
  "visualPlanRef": "...",
  "requestedFormats": ["html", "pptx", "docx", "pdf"],
  "artifacts": [
    {"format": "html", "ref": "...", "producer": "learning-landingpage-renderer"},
    {"format": "pptx", "ref": "...", "producer": "template-presentation-workflow"}
  ],
  "assetManifests": [],
  "qaRef": "learning-artifact-qa.json",
  "status": "pass|review|fail"
}
```

`learning-delivery-run.json` dokumentiert Routing, ausgeführte Worker, ausgelassene Formate, Warnings, Render-Coverage und Abschlussstatus.

## Prüfungen

Vor PASS prüfen:

- genau ein autoritatives Inhaltsmodell pro Run;
- jedes angeforderte Format besitzt einen tatsächlichen Worker-Output oder einen expliziten Fehlerstatus;
- Bundle-Referenzen nennen den tatsächlichen Producer;
- keine Worker-Datei wird vom Orchestrator als neu produziert ausgegeben;
- kein Critical/Major Finding aus `learning-artifact-qa` bleibt offen;
- ein visueller PASS wird nur bei tatsächlich geprüften Rendern vergeben;
- Corporate-/Template-Gates bleiben erhalten und werden nicht durch Learning-Defaults überschrieben.

## Fehlerbehandlung

- **Kein kanonisches Modell:** Delivery abbrechen; keine Inhalte aus Rohquellen improvisieren.
- **Mehrere konkurrierende Modelle ohne Authority:** an den aufrufenden Orchestrator zurückgeben; keine Synthese durchführen.
- **Renderer nicht verfügbar:** betroffenes Format als nicht geliefert markieren; keine Ersatzdatei mit falscher Extension erzeugen.
- **Asset-Fehler:** wenn semantisch verzichtbar, dokumentiert ohne Asset fortfahren; wenn für Verständnis oder Traceability erforderlich, Delivery auf `review|fail` setzen.
- **QA-Finding:** betroffenen Worker korrigieren lassen und danach erneut rendern/prüfen.
- **Designkonflikt:** verbindliche Corporate-/Template-Autorität respektieren; keine lokale Designabweichung als Fix erfinden.

## Übergabe

Primäre Outputs sind ausschließlich:

- `learning-delivery-bundle.json` als Referenzpaket auf die tatsächlichen Delivery-Artefakte;
- `learning-delivery-run.json` als auditierbarer Ausführungs- und QA-Status.

Die eigentlichen HTML-, PPTX-, DOCX-, PDF-, SVG- und Bildartefakte verbleiben im Ownership ihrer spezialisierten Producer.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn das autoritative Learning-Modell unverändert als fachliche Basis erhalten blieb, die angeforderten Formate über die zuständigen Worker erzeugt wurden, alle erzeugten Assets und Formate über echte Producer-Referenzen im Bundle verknüpft sind, Cross-Format-QA abgeschlossen ist und `learning-delivery-run.json` den finalen Status ohne simulierte Render-, Delivery- oder Freigabeerfolge dokumentiert.
