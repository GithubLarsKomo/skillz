---
name: project-second-brain
description: Führt eine GitHub-versionierte, Obsidian-kompatible Projektdokumentation als verlinkten Second Brain ab dem Requirements-Grilling. Erfasst wesentliche Workflow-Übergänge, Entscheidungen und Evidenz und dokumentiert einen kanonischen Google-Drive-Projektordner für nicht-textuelle Projekt- und Delivery-Artefakte, ohne Producer-Artefakte zu duplizieren oder private Chain-of-Thought zu speichern.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - project-memory-index.md
  - project-memory-state.json
  - project-memory-event.md
  - project-memory-assets.md
lastEvaluated: 2026-09-10
---

# Project Second Brain

## Zweck

Dieser Skill hält den vollständigen Projektweg **ab dem Grilling** als GitHub-versionierte, in Obsidian direkt nutzbare Wissensspur zusammen. Er ersetzt keine fachlichen Artefakte, keine `SPEC.md`, keine Decision Records, keine Issues, keine Review-Evidenz und keine Delivery-Zustände. Er verlinkt sie als nachvollziehbaren Projektgraphen.

Zusätzlich hält er für nicht-textuelle Projekt-, Referenz- und Delivery-Artefakte einen **kanonischen Google-Drive-Projektordner** fest. Die eigentlichen Binärdateien liegen dort, sofern sie nicht für Build, Test, Runtime oder Source Control des Repositories benötigt werden. GitHub enthält weiterhin die dokumentarische Spur, Links, IDs, Status und Evidenz.

Seine Kernfrage lautet: **Welcher verifizierbare Projektzustand entstand in diesem Schritt, worauf basiert er und wohin führt er als Nächstes?**

## Trigger

Verwenden:

- unmittelbar nach dem ersten abgeschlossenen projektbezogenen `round-based-requirements-grilling`,
- bei jedem wesentlichen Übergang zwischen Grilling, Wayfinding, Research, Spezifikation, Decision Record, Issue-Zerlegung, Implementierung, Review, Delivery und Handoff,
- wenn ein projektbezogener nicht-textueller Input oder Output erzeugt, empfangen, reviewt, freigegeben oder übergeben wird,
- wenn ein Projekt nach einer Unterbrechung aus GitHub ohne erneute Vollanalyse fortgesetzt werden soll,
- wenn der Nutzer eine Obsidian-kompatible Projektchronik, einen Projektgraphen oder einen Second-Brain-artigen Wissensstand verlangt.

Nicht für jedes Shell-Kommando, jede Toolabfrage oder jede Zwischenüberlegung einen Event erzeugen. Dokumentiert werden **semantische Zustandsänderungen und abgeschlossene Arbeitsabschnitte**.

## Voraussetzungen

- Ein projektbezogener Kontext oder ein abgeschlossener Grilling-Schritt ist vorhanden.
- Das Ziel-Repository ist bekannt oder kann als Bootstrap später eindeutig bestimmt werden.
- Kanonische Producer-Artefakte bleiben an ihren bestehenden Ablageorten und werden nicht in den Project Memory kopiert.
- Bei Repository-Arbeit wird der relevante Branch-/Commit-Zustand verifiziert, bevor er als Evidenz festgeschrieben wird.
- Für externe Binärartefakte wird Google Drive nur verwendet, wenn ein zugänglicher Drive-Kontext vorhanden ist. Nicht verfügbare Drive-Schreibfähigkeit ist ein `pending` externer Zustand und kein Grund, eine erfolgte Ablage zu behaupten.

## Kanonischer Ablageort

Die textuelle Projektdokumentation liegt im **Ziel-Repository des Projekts**, standardmäßig unter:

```text
docs/project-memory/
├── INDEX.md
├── TIMELINE.md
├── ASSETS.md
├── state.json
├── events/
├── decisions/
├── knowledge/
└── retrospectives/
```

- `INDEX.md` ist die Map of Content und der Einstieg für GitHub und Obsidian.
- `TIMELINE.md` enthält die chronologische, verlinkte Ereignisfolge.
- `ASSETS.md` dokumentiert den kanonischen externen Artifact Store und die dort registrierten nicht-textuellen Artefakte. Solange ein Projekt keine externen Artefakte besitzt, darf die Datei fehlen.
- `state.json` ist der kompakte maschinenlesbare aktuelle Zustand.
- `events/` enthält atomare, abgeschlossene Projektereignisse.
- `decisions/` ist der bevorzugte Ort für projektbezogene `decision-record`-Artefakte, sofern das Ziel-Repository keinen etablierten anderen Ort besitzt.
- `knowledge/` enthält nur wiederverwendbare, projektbezogene Erkenntnisnotizen, nicht Rohquellenkopien.
- `retrospectives/` enthält abgeschlossene Iterations- oder Meilensteinrückblicke.

Besteht bereits eine gleichwertige Projektdokumentationsstruktur, wird sie weiterverwendet. Kein zweiter paralleler Second Brain wird angelegt.

## GitHub- und Obsidian-Kompatibilität

Verwende in realen Project-Memory-Dateien normales Markdown mit relativen Links. Die folgenden Beispielziele sind nur Schema-Platzhalter und deshalb hier bewusst als Pfade statt als auflösbare Links dargestellt:

```text
DEC-004 -> ../decisions/DEC-004.md
SPEC -> ../../SPEC.md
EVT-20260902-101500-spec-created -> events/EVT-20260902-101500-spec-created.md
ASSET-004 -> ASSETS.md + beobachteter Google-Drive-Link
```

Normale Markdown-Links funktionieren in GitHub und Obsidian. Wikilinks `[[...]]` dürfen ergänzend nur verwendet werden, wenn das Repository dies bereits verbindlich nutzt; sie sind nicht die alleinige Navigation.

Jede Event-Note besitzt YAML-Frontmatter. Dadurch kann Obsidian Properties, Dataview und Graph View ohne proprietäres Zusatzformat nutzen.

## Dokumentationsvertrag ab Grilling

### 1. Bootstrap nach Grilling

Nach dem ersten projektbezogenen Grilling:

1. Ziel-Repository bestimmen.
2. Falls noch kein Ziel-Repository existiert, ein `project-memory-bootstrap` als Ausgabe vorbereiten und die Initialisierung beim ersten bestätigten Repository durchführen; Grilling-ID und Quellen bleiben referenziert.
3. `docs/project-memory/` initialisieren, sofern nicht vorhanden.
4. ersten Event mit `stage: grilling` erzeugen.
5. `GRILL-REPORT.md`, `requirements-handoff.json`, bestätigte Ziele, Nicht-Ziele, Entscheidungen, offene Punkte und Routingziel verlinken.
6. `INDEX.md`, `TIMELINE.md` und `state.json` aktualisieren.
7. Einen bereits festgelegten Projekt-Drive-Ordner in `state.json`/`ASSETS.md` registrieren; andernfalls den Drive-Artifact-Store erst beim ersten externen nicht-textuellen Artefakt materialisieren.
8. den Memory-Verweis an den nächsten Skill übergeben.

### 2. Document-on-transition Gate

Vor jedem fachlichen Handoff zum nächsten Projekt-Skill muss der abgeschlossene Schritt im Project Second Brain verankert sein.

Typische Übergänge:

```text
Grilling
  -> Wayfinding / Research
  -> conversation-to-spec
  -> spec-to-vertical-issues
  -> iterate-software-projects / implement-from-issue
  -> two-axis-code-review
  -> engineering-delivery-followup
  -> nächste Iteration oder Abschluss
```

Wenn ein Schritt keine Zustandsänderung erzeugt, darf auf einen neuen Event verzichtet werden. Der Grund muss aus bestehender Event- oder Handoff-Evidenz erkennbar sein.

### 3. Drive-Artifact Gate

Wenn ein Workflow einen nicht-textuellen Projekt-, Referenz-, Review- oder Delivery-Output erzeugt, gilt zusätzlich:

1. Zuerst prüfen, ob das Artefakt für Build, Test, Runtime oder Source Control des Repositories erforderlich ist. Falls ja, bleibt es im Repository und wird nur referenziert.
2. Andernfalls den bereits dokumentierten kanonischen Google-Drive-Projektordner wiederverwenden oder gemäß [`references/drive-artifact-contract.md`](references/drive-artifact-contract.md) einmalig auflösen bzw. anlegen.
3. Artefakt in Drive ablegen oder die bereits autoritative externe Datei registrieren.
4. Nach einem Write den Drive-Zustand read-back-verifizieren; IDs, URL, MIME-Typ, Parent und Modifikationszustand niemals erraten.
5. `ASSETS.md`, `state.json` und den zugehörigen Event konsistent aktualisieren.
6. Bei freigegebenen/frozen Deliverables keine stillen Überschreibungen vornehmen; Supersession oder Versionstransition nachvollziehbar dokumentieren.

Diese Regel gilt für **alle Workflows, die `project-second-brain` verwenden**. Nachgelagerte Skills erzeugen keinen eigenen parallelen Drive-Projektordner.

## Ablauf

1. Bestehenden Project-Memory-Root, `state.json` und letzten relevanten Event lesen oder nach dem ersten Grilling initialisieren.
2. Den kanonischen Input und den verifizierten Repository-/External-State des abgeschlossenen Arbeitsschritts bestimmen.
3. Nicht-textuelle Artefakte gegen die Storage Boundary des Drive Artifact Contract klassifizieren.
4. Falls erforderlich den kanonischen Drive-Projektordner auflösen, Datei schreiben/verifizieren und in `ASSETS.md` registrieren.
5. Nur bei einer semantischen Zustandsänderung einen neuen Event erzeugen.
6. Wesentliche Entscheidungen über `decision-record` referenzieren, statt sie als zweite Wahrheit in Event-Text zu verstecken.
7. `INDEX.md`, `TIMELINE.md`, `ASSETS.md` soweit vorhanden und `state.json` konsistent aktualisieren.
8. Genau eine nächste Aktion und das Routingziel festhalten.
9. Den `projectMemory`-Verweis an den nächsten Skill übergeben.

## Event-Modell

Event-IDs sind stabil und kollisionsarm, bevorzugt:

`EVT-YYYYMMDD-HHMMSS-<kurzer-slug>`

Beispiel:

```yaml
---
id: EVT-20260902-101500-spec-created
type: project-event
project: example-project
stage: specification
status: completed
date: 2026-09-02T10:15:00+02:00
source_skill: conversation-to-spec
repository: owner/repo
head_sha: abc123...
previous_event: EVT-20260902-094500-wayfinding-closed
inputs:
  - ../../GRILL-REPORT.md
  - ../../requirements-handoff.json
outputs:
  - ../../SPEC.md
external_outputs:
  - asset_id: ASSET-004
    drive_file_id: observed-file-id
    manifest: ../ASSETS.md
decisions:
  - ../decisions/DEC-004.md
tags:
  - project-memory
  - stage/specification
---
```

Der Event-Text enthält mindestens:

1. **Kontext** – Ziel dieses Arbeitsschritts.
2. **Inputs** – verlinkte kanonische Quellen und deren Status.
3. **Ergebnis** – beobachtbare Zustandsänderung oder erzeugtes Artefakt.
4. **Entscheidungen und Annahmen** – nur bestätigte Entscheidungen bzw. explizit markierte reversible Annahmen.
5. **Evidenz** – Tests, Commits, PRs, Issues, externe Quellen, Drive-Asset-IDs oder verifizierte Toolergebnisse.
6. **Offene Schleifen** – Blocker, Risiken, pending externe Zustände.
7. **Nächste Aktion** – genau eine priorisierte Aktion oder klarer Abschlussstatus.
8. **Links** – vorheriger Event, relevante Decisions, Repo-Artefakte, `ASSETS.md`, externe kanonische Artefakte und Folgepfad.

## Keine Chain-of-Thought-Persistenz

Nachvollziehbarkeit bedeutet **Entscheidungsrationale, Evidenz, Alternativen, Annahmen und Ergebnisse**, nicht das Speichern privater interner Gedankengänge.

Nicht persistieren:

- private Chain-of-Thought oder versteckte Scratchpads,
- Zugangsdaten, Tokens oder Secrets,
- unnötige personenbezogene Inhalte,
- vollständige Logs, wenn ein kleiner Evidenzausschnitt oder ein stabiler Link genügt,
- große Quellenkopien, die bereits kanonisch verfügbar sind.

## Umgang mit kanonischen Artefakten

Project Second Brain besitzt **keine zweite fachliche Wahrheit**.

- `SPEC.md` bleibt bei `conversation-to-spec`.
- Decision Records bleiben bei `decision-record`.
- Wayfinding-Artefakte bleiben bei `large-work-wayfinder`.
- Issues und PRs bleiben in GitHub.
- Implementierungs- und Review-Evidenz bleibt bei den Engineering-Skills.
- Delivery-Zustände bleiben bei `engineering-delivery-followup`.
- Repository-native Binärdateien, die Build/Test/Runtime benötigen, bleiben im Repository.
- Nicht-textuelle Projekt-/Review-/Delivery-Artefakte werden im dokumentierten Drive-Projektordner gespeichert, sofern sie nicht bereits eine andere autoritative externe Quelle besitzen.

Die Event-Note und `ASSETS.md` speichern Links, Status, IDs und bei Bedarf einen kurzen verifizierbaren Abstract. Keine inhaltlich divergierende Kopie anlegen.

## Drive Artifact Contract

Der vollständige Storage-, Versionierungs-, Read-back-, Manifest- und Failure-Vertrag liegt in [`references/drive-artifact-contract.md`](references/drive-artifact-contract.md) und ist normativ für diesen Skill.

Kernregeln:

- genau ein kanonischer Drive-Projektordner pro Project Memory,
- bereits dokumentierte Folder-ID wiederverwenden statt Ordner über Namen neu zu erraten,
- Standard-Fallback bei fehlender Vorgabe: private Struktur `Skillz Projects/<projectId>` in My Drive,
- bestehende Sharing-Rechte erhalten; keine implizite Freigabe,
- jeden Drive-Write read-back-verifizieren,
- `ASSETS.md` als menschenlesbares Asset-Register und `state.json` als maschinenlesbare Projektion führen,
- keine stillen Überschreibungen freigegebener/frozen Artefakte,
- externe Ausfälle als `pending` dokumentieren.

## Decision Records

Wesentliche fachliche, technische, regulatorische, rechtliche, Sicherheits-, Architektur- oder Governance-Entscheidungen werden nicht als Fließtext im Event versteckt.

1. `decision-record` verwenden, wenn dessen Trigger erfüllt ist.
2. Decision Record im Project Memory verlinken.
3. Event nennt Decision-ID, Status und Konsequenz.
4. Supersession wird als neuer Decision Record plus neuer Event dokumentiert; alte akzeptierte Records werden nicht überschrieben.

## Repository- und Commit-Bezug

Bei Repository-Arbeit enthält jeder relevante Event mindestens:

- Repository,
- Branch oder PR, soweit anwendbar,
- verifizierten Head-SHA,
- relevante Commit-/PR-/Issue-Referenzen,
- Freshness bei volatilen externen Zuständen.

Wenn Dokumentation Teil desselben Arbeitsschritts ist, wird der Event möglichst im selben Commit wie die zugehörige Änderung gespeichert. Wenn der Zustand erst extern entsteht, etwa CI, Merge, Deployment oder Drive-Upload, folgt ein eigener Dokumentations-Commit mit Referenz auf den verifizierten Zustand.

Historie nicht durch Force-Rewrite glätten. Git-Historie ist Teil der Auditierbarkeit.

## `INDEX.md`

Die Map of Content enthält mindestens:

- Projektziel und aktueller Status,
- Link auf `state.json`,
- Link auf `ASSETS.md`, wenn ein externer Artifact Store existiert,
- letzte 5 bis 10 Events,
- aktuelle normative Artefakte,
- akzeptierte Decisions,
- offene Schleifen,
- aktuellen nächsten Schritt,
- Links auf stage-bezogene Einstiegspunkte oder wichtige Wissensnotizen.

Sie ist eine **aktuelle Projektion**, keine unveränderliche Historie.

## `TIMELINE.md`

Chronologisch, append-orientiert. Beispielhafte Darstellung ohne auflösbare Repo-Links:

```text
- 2026-09-02 09:45 — EVT-...-grilling-closed -> events/EVT-...md — Requirements bestätigt; Routing zu Wayfinding.
- 2026-09-02 10:15 — EVT-...-spec-created -> events/EVT-...md — SPEC v1 erstellt; DEC-004 akzeptiert.
- 2026-09-10 12:00 — EVT-...-presentation-released -> events/EVT-...md — ASSET-004 in kanonischem Drive-Projektordner verifiziert und released.
```

In der tatsächlichen `TIMELINE.md` werden die vorhandenen Event-Dateien als relative Markdown-Links gesetzt.

Keine alten Ereignisse löschen, nur weil sie überholt sind. Stattdessen Folgeevent beziehungsweise Supersession verlinken.

## `ASSETS.md`

`ASSETS.md` wird materialisiert, sobald der erste externe Artifact Store oder externe nicht-textuelle Projektartefakt registriert wird. Die Datei enthält mindestens:

- Provider (`Google Drive`),
- beobachteten Link und die Folder-ID des kanonischen Projektordners,
- Zeitpunkt der letzten Verifikation,
- Asset-ID, Rolle, Dateiname, Drive-Link/-ID, Status, Producer, Event-Referenz und Verifikationsstand je Artefakt.

Das Register ist eine Projektion. Historische Beziehungen und Supersessions bleiben nachvollziehbar; veraltete Einträge werden nicht gelöscht, nur weil eine neue Version vorliegt.

## `state.json`

Mindestschema ohne externen Artifact Store:

```json
{
  "schemaVersion": 1,
  "projectId": "string",
  "repository": "owner/repo",
  "memoryRoot": "docs/project-memory/INDEX.md",
  "latestEvent": "docs/project-memory/events/EVT-....md",
  "currentStage": "grilling|wayfinding|research|specification|backlog|implementation|review|delivery|handoff|complete",
  "canonicalArtifacts": [
    {"type": "spec", "path": "SPEC.md", "status": "approved", "ref": "commit-or-url"}
  ],
  "decisions": [
    {"id": "DEC-004", "path": "docs/project-memory/decisions/DEC-004.md", "state": "accepted"}
  ],
  "openLoops": [
    {"id": "OPEN-001", "type": "blocker|risk|pending|question", "summary": "...", "nextAction": "..."}
  ],
  "lastVerified": {"headSha": "...", "at": "..."},
  "nextAction": {"description": "...", "skill": "..."}
}
```

Beim ersten externen Artifact Store wird additiv auf `schemaVersion: 2` erweitert:

```json
{
  "schemaVersion": 2,
  "artifactStore": {
    "provider": "google-drive",
    "folderId": "observed-folder-id",
    "folderUrl": "observed-folder-url",
    "folderName": "project-id",
    "lastVerifiedAt": "2026-09-10T12:00:00+02:00"
  },
  "externalArtifacts": [
    {
      "id": "ASSET-004",
      "role": "final-presentation",
      "name": "NDD Review.pptx",
      "mimeType": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
      "driveFileId": "observed-file-id",
      "url": "observed-drive-file-url",
      "status": "released",
      "producer": "presentation-workflow",
      "event": "docs/project-memory/events/EVT-....md",
      "verifiedAt": "2026-09-10T12:00:00+02:00"
    }
  ]
}
```

Bestehende v1-Zustände ohne externe Assets bleiben gültig. Das Upgrade auf v2 erzeugt keine rückwirkende Umschreibung historischer Event-Notes.

`state.json` ist eine Projektion und darf aktualisiert werden. Event-Notes sind die historisch stabilen Einheiten.

## Event-Frequenz

Erzeuge einen Event insbesondere bei:

- Abschluss oder Wiederöffnung eines Grillings,
- abgeschlossenem Wayfinding/Research-Schritt mit neuer Evidenz,
- neuer oder erneut freigegebener SPEC,
- neuer, akzeptierter oder supersedierter wesentlicher Entscheidung,
- erzeugtem oder wesentlich neu geschnittenem Issue-Backlog,
- Beginn/Abschluss eines Engineering-Inkrements,
- Review-Entscheidung für einen fixierten SHA,
- Materialisierung oder Wechsel des kanonischen Drive-Artifact-Stores,
- Freigabe, Supersession oder wesentlicher Übergabe eines externen nicht-textuellen Artefakts,
- Merge-/Deployment-/Requirement-Closure,
- Handoff an neue Sitzung/Agenten,
- Meilenstein oder Projektabschluss.

Keine Event-Flut für reine Lesezugriffe, jeden einzelnen Working-File-Save oder wiederholte unveränderte Statuschecks.

## Handoff-Vertrag

Nach Initialisierung wird der Project-Memory-Verweis in nachgelagerten Handoffs mitgeführt:

```json
{
  "projectMemory": {
    "root": "docs/project-memory/INDEX.md",
    "state": "docs/project-memory/state.json",
    "latestEvent": "docs/project-memory/events/EVT-....md"
  }
}
```

Sobald ein externer Artifact Store existiert, wird erweitert:

```json
{
  "projectMemory": {
    "root": "docs/project-memory/INDEX.md",
    "state": "docs/project-memory/state.json",
    "latestEvent": "docs/project-memory/events/EVT-....md",
    "assetIndex": "docs/project-memory/ASSETS.md",
    "artifactStore": {
      "provider": "google-drive",
      "folderId": "observed-folder-id",
      "folderUrl": "observed-folder-url"
    }
  }
}
```

Nachgelagerte Skills lesen zuerst `state.json` und den letzten relevanten Event; bei externen Assets zusätzlich `ASSETS.md`. Sie verwenden die dokumentierte Folder-ID weiter und erzeugen keinen parallelen Drive-Projektordner.

## Übergabe

Die Übergabe besteht mindestens aus dem `projectMemory`-Verweis, dem aktuellen Routingziel, den offenen Schleifen und genau einer nächsten Aktion. Der nachgelagerte Skill liest zuerst `state.json` und den letzten relevanten Event und folgt anschließend den verlinkten kanonischen Artefakten. Existiert ein Artifact Store, wird auch der `assetIndex`- und `artifactStore`-Verweis übergeben.

## Prüfungen

Vor jedem Handoff prüfen:

- Project-Memory-Root und `latestEvent` sind eindeutig und erreichbar,
- der neue Event beschreibt eine echte semantische Zustandsänderung,
- alle referenzierten kanonischen Artefakte und SHAs existieren beziehungsweise pending Zustände sind ausdrücklich als pending markiert,
- bei externen Assets stimmen `ASSETS.md`, `state.json`, Event und beobachtete Drive-Metadaten überein,
- Folder- und File-IDs/URLs wurden beobachtet und nicht erfunden,
- ein Repository-Build/Test/Runtime-Asset wurde nicht nur wegen seines Binärformats ausgelagert,
- `INDEX.md`, `TIMELINE.md`, `ASSETS.md` soweit vorhanden und `state.json` widersprechen dem Event nicht,
- historische Events wurden nicht still umgeschrieben,
- genau eine nächste Aktion ist benannt,
- keine private Chain-of-Thought, Secrets oder unnötige sensible Inhalte wurden persistiert.

## Fehlerbehandlung

Stoppe beziehungsweise korrigiere die Dokumentation, wenn:

- kanonische Artefakte in divergierenden Kopien dupliziert werden,
- historische Events nachträglich inhaltlich umgeschrieben werden,
- pending externe Zustände als abgeschlossen dokumentiert werden,
- Links auf bewegliche Branches als unveränderliche Evidenz ausgegeben werden, obwohl ein SHA verfügbar ist,
- Drive-Folder-/File-IDs oder URLs ohne Read-back bzw. andere Verifikation erfunden werden,
- ein neuer paralleler Drive-Projektordner neben dem bereits dokumentierten Artifact Store angelegt wird,
- Repository-native Build/Test/Runtime-Artefakte ausschließlich wegen ihres Binärformats aus GitHub entfernt werden,
- freigegebene/frozen externe Artefakte still überschrieben werden,
- Secrets oder private Chain-of-Thought gespeichert werden,
- ein neuer paralleler Projekt-Memory-Baum neben einer gleichwertigen bestehenden Struktur angelegt wird,
- ein Handoff erfolgt, obwohl der vorherige wesentliche Schritt noch nicht im Projektgraph verankert ist.

## Abschlusskriterien

Der Skill ist erfüllt, wenn:

- das Projekt ab dem Grilling einen eindeutigen GitHub-basierten Memory-Root besitzt,
- GitHub und Obsidian dieselben Markdown-Dateien sinnvoll darstellen können,
- jeder wesentliche Workflow-Übergang durch einen verlinkten Event nachvollziehbar ist,
- Entscheidungen und Evidenz auf ihre kanonischen Quellen zeigen,
- nicht-textuelle Projekt-/Review-/Delivery-Artefakte entweder im dokumentierten kanonischen Drive-Projektordner liegen oder eine andere autoritative externe Quelle verifiziert referenziert ist,
- Repository-native Binärartefakte, die Build/Test/Runtime benötigen, im Repository verbleiben,
- `INDEX.md`, `TIMELINE.md`, `ASSETS.md` soweit vorhanden und `state.json` den aktuellen Zustand konsistent abbilden,
- keine private Chain-of-Thought oder unnötige sensible Information persistiert wurde,
- ein neuer Agent oder Nutzer den aktuellen Projektstand, den kanonischen Artifact Store und genau den nächsten Schritt ohne erneute Vollanalyse rekonstruieren kann.