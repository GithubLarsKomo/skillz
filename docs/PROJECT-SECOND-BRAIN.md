# Project Second Brain

Status: active capability  
Date: 2026-09-10  
Canonical skill: [`project-second-brain`](../skills/project-second-brain/SKILL.md)

## Ziel

Skillz führt projektbezogene Arbeit ab dem Requirements-Grilling als GitHub-versionierten, Obsidian-kompatiblen Projektgraphen fort. Der Graph macht Entscheidungen, Evidenz, Artefakte, Iterationen und Übergaben nachvollziehbar, ohne eine zweite fachliche Wahrheit neben den kanonischen Producer-Artefakten zu erzeugen.

Nicht-textuelle Projekt-, Referenz-, Review- und Delivery-Artefakte werden ergänzend in einem pro Projekt dokumentierten Google-Drive-Ordner geführt, sofern sie nicht für Build, Test, Runtime oder Source Control des Repositories benötigt werden. GitHub bleibt die dokumentarische und verlinkende Ebene; Drive ist der externe Artifact Store.

## Lifecycle

```text
round-based-requirements-grilling
        |
        v
project-second-brain bootstrap
        |
        +--> large-work-wayfinder --------+
        |                                  |
        +----------------------------------v
                               conversation-to-spec
                                         |
                                         v
                              spec-to-vertical-issues
                                         |
                                         v
                              iterate-software-projects
                                | implementation
                                | review
                                | delivery / closure
                                v
                                  next iteration
                                         |
                                         v
                                    agent-handoff
```

`project-second-brain` ist ein Querschnittsvertrag. Die fachlichen Skills behalten ihre Artefaktverantwortung; Project Memory erzeugt nur verlinkte Ereignis- und Zustandsprojektionen. Alle Workflows, die `project-second-brain` verwenden, erben auch die Drive-Artifact-Regel und verwenden denselben dokumentierten Projektordner statt parallele Ablagen anzulegen.

## Zielstruktur im Projekt-Repository

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

### `INDEX.md`

Map of Content für Mensch und Obsidian. Enthält Projektziel, aktuellen Status, normative Artefakte, wichtige Decisions, letzte Events, offene Schleifen, den nächsten Schritt und bei vorhandenen externen Artefakten den Link auf `ASSETS.md`.

### `TIMELINE.md`

Append-orientierter chronologischer Index auf Event-Notes. Alte Zustände werden nicht gelöscht, sondern durch Folgeevents oder Supersession weitergeführt.

### `ASSETS.md`

Human-readable Manifest des externen Artifact Stores. Die Datei wird erst materialisiert, wenn ein Projekt einen externen Artifact Store oder ein externes nicht-textuelles Artefakt besitzt. Sie dokumentiert mindestens:

- Provider (`Google Drive`),
- beobachtete Folder-ID und Drive-URL des kanonischen Projektordners,
- Zeitpunkt der letzten Verifikation,
- stabile lokale Asset-ID,
- Rolle/Zweck,
- Dateiname und Typ,
- beobachtete Drive-Datei-ID und URL,
- Lifecycle-Status,
- Producer/Quelle,
- zugehörigen Project-Memory-Event,
- Verifikationsstand beziehungsweise Revision/Checksum/Modified-Time, soweit sinnvoll verfügbar.

### `state.json`

Kompakte maschinenlesbare Projektion für Skill-Handoffs. Enthält `latestEvent`, `currentStage`, kanonische Artefakte, Decision-Referenzen, offene Schleifen, verifizierten Repositoryzustand und nächste Aktion.

Ohne externen Artifact Store kann das bestehende `schemaVersion: 1` verwendet werden. Beim ersten materialisierten Drive-Store wird additiv auf `schemaVersion: 2` erweitert um:

```json
{
  "artifactStore": {
    "provider": "google-drive",
    "folderId": "observed-folder-id",
    "folderUrl": "observed-folder-url",
    "folderName": "project-id",
    "lastVerifiedAt": "2026-09-10T12:00:00+02:00"
  },
  "externalArtifacts": []
}
```

Bestehende v1-Events werden dafür nicht rückwirkend umgeschrieben.

### `events/`

Atomare Ereignisnotizen mit YAML-Frontmatter und normalen relativen Markdown-Links. Dadurch funktionieren dieselben Dateien in GitHub, Obsidian Properties, Dataview und Graph View. Externe Artefakte werden über stabile Asset-IDs plus verifizierte Drive-Referenzen eingebunden, nicht als Kopie des Binärinhalts.

## Storage Boundary: GitHub oder Drive?

### Im Repository bleiben

Nicht-textuelle Dateien bleiben im Repository, wenn sie dort funktional gebraucht werden, zum Beispiel:

- Build-, Test-, Runtime- oder Deployment-Abhängigkeiten,
- Repository-native Icons, Fixtures oder eingebettete Assets,
- Modelle oder Binärdateien, die Bestandteil des Produkts sind,
- Artefakte, für die das Repository bereits der autoritative Producer-Ort ist.

Die neue Drive-Regel darf Software- oder Design-Repositories nicht dadurch beschädigen, dass erforderliche Binärassets allein wegen ihres Dateiformats ausgelagert werden.

### In den dokumentierten Drive-Ordner

Nicht-textuelle dokumentarische oder distributive Artefakte werden grundsätzlich im Projekt-Drive geführt, sofern keine andere autoritative externe Quelle existiert. Typische Beispiele:

- PPT/PPTX, DOC/DOCX, XLS/XLSX,
- PDF,
- PNG/JPEG/TIFF und andere Review-/Exportbilder,
- EPUB,
- Audio und Video,
- ZIP-/Handoff-Pakete,
- Google Docs, Sheets und Slides als kanonische externe Artefakte.

Eine bereits autoritative externe Datei wird nur registriert und verlinkt; sie wird nicht unnötig erneut in Drive kopiert.

Der normative Detailvertrag liegt unter [`skills/project-second-brain/references/drive-artifact-contract.md`](../skills/project-second-brain/references/drive-artifact-contract.md).

## Kanonischer Google-Drive-Projektordner

Jeder Project Memory besitzt höchstens einen kanonischen Google-Drive-Projektordner für externe Artefakte. Die Auflösung erfolgt in dieser Reihenfolge:

1. bereits in `state.json` dokumentierte Folder-ID wiederverwenden,
2. explizit im Projekt/Handoff festgelegten Drive-Ordner wiederverwenden,
3. vorhandenen passenden Projektordner nur nach Identitätsprüfung übernehmen,
4. andernfalls unter einem konfigurierten Parent oder als Fallback unter `Skillz Projects/<projectId>` in My Drive einen privaten Projektordner anlegen.

Sobald der Ordner materialisiert ist, wird er über seine beobachtete Folder-ID identifiziert, nicht durch erneute Namenssuche. Vorhandene Sharing-Rechte werden erhalten; neue Ordner werden nicht automatisch freigegeben.

## Drive-Write-Vertrag

Bei jedem externen Artifact Write:

1. Storage Boundary prüfen.
2. Kanonischen Projektordner per ID auflösen.
3. Datei hochladen oder die bestehende kanonische Datei nur dann in-place aktualisieren, wenn sie bewusst mutable ist.
4. Nach dem Write Metadaten read-back-verifizieren.
5. Nur beobachtete IDs, URLs, MIME-Typen, Parents und Modifikationsdaten dokumentieren.
6. `ASSETS.md`, `state.json` und den auslösenden Event konsistent aktualisieren.
7. Freigegebene/frozen Deliverables nicht still überschreiben; Version oder Supersession nachvollziehbar machen.

Ist Google Drive nicht erreichbar oder nicht schreibbar, bleibt der Zustand `pending`. Eine Ablage darf nicht als abgeschlossen dokumentiert werden, bevor sie verifiziert ist.

## Verlinkungsprinzip

Project Memory kopiert keine `SPEC.md`, Wayfinding-Artefakte, Review-Evidenz oder Delivery-Daten. Es verweist auf die kanonischen Artefakte und dokumentiert ihren Status.

Die folgende Darstellung zeigt nur die beabsichtigten relativen Ziele; in einer realen Project-Memory-Datei werden daraus normale Markdown-Links, sobald die referenzierten Dateien existieren:

```text
Inputs:
- Requirements Handoff -> ../../requirements-handoff.json
- Wayfinding Brief -> ../../wayfinding-brief.md

Outputs:
- SPEC v1 -> ../../SPEC.md
- DEC-004 -> ../decisions/DEC-004.md
- ASSET-004 -> ../ASSETS.md + beobachteter Google-Drive-Link
```

Relative Markdown-Links sind bewusst die Standardform, weil sie sowohl GitHub als auch Obsidian verstehen. Für externe Dateien dient `ASSETS.md` als stabiler lokaler Einstiegspunkt; der eigentliche Drive-Link bleibt die kanonische Dateireferenz.

## Event-Grenzen

Ein neuer Event entsteht bei semantischer Zustandsänderung, insbesondere:

- Grilling abgeschlossen oder wieder geöffnet,
- Wayfinding-/Research-Ergebnis,
- SPEC erstellt, geändert oder freigegeben,
- wesentliche Decision erstellt oder supersediert,
- Backlog erzeugt oder neu geschnitten,
- Engineering-Inkrement erreicht einen neuen verifizierbaren Zustand,
- Review-Entscheidung für einen fixierten SHA,
- Materialisierung oder Wechsel des kanonischen Drive-Artifact-Stores,
- Release, Supersession oder wesentliche Übergabe eines externen Artefakts,
- Merge/Deployment/Requirement-Closure,
- Handoff oder Projektabschluss.

Keine Event-Flut für Low-Level-Kommandos, reine Lesezugriffe, jeden Working-File-Save oder unveränderte Status-Polls.

## Handoff

Der bestehende Handoff bleibt gültig:

```json
{
  "projectMemory": {
    "root": "docs/project-memory/INDEX.md",
    "state": "docs/project-memory/state.json",
    "latestEvent": "docs/project-memory/events/EVT-....md"
  }
}
```

Sobald ein externer Artifact Store existiert, wird er erweitert:

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

Nachgelagerte Skills lesen `state.json`, den letzten relevanten Event und bei externen Assets `ASSETS.md`. Sie verwenden den dokumentierten Store weiter und erzeugen keinen eigenen parallelen Drive-Projektordner.

## Historie und Auditierbarkeit

- Event-Notes sind nach Abschluss inhaltlich stabil.
- Substantielle Korrekturen erzeugen Folgeevents und Links auf den ersetzten Zustand.
- `INDEX.md`, `TIMELINE.md`, `ASSETS.md` und `state.json` sind aktualisierbare Projektionen.
- Git-Commits und immutable SHAs gehören zur Evidenz.
- Drive-Folder-/File-IDs und beobachtete Metadaten gehören zur Evidenz externer Artefakte.
- Force-Rewrites werden nicht verwendet, um Projektgeschichte zu glätten.
- Freigegebene externe Artefakte werden nicht still überschrieben.

## Datenschutz und Reasoning-Grenze

Persistiert werden nachvollziehbare Rationale, Alternativen, Entscheidungen, Annahmen, Evidenz und Ergebnisse. Nicht persistiert werden private Chain-of-Thought, Scratchpads, Secrets, unnötige personenbezogene Informationen oder vollständige Logs ohne dokumentarischen Mehrwert.

Google Drive wird nicht implizit öffentlich freigegeben. Bestehende Sharing-Rechte werden erhalten; neue Projektordner bleiben standardmäßig privat.

## Obsidian-Nutzung

Der Projekt-Repository-Root kann direkt als Vault geöffnet werden; alternativ kann nur `docs/project-memory/` in einen bestehenden Vault gespiegelt werden. Für den Graphen sind keine speziellen Plugins erforderlich. Dataview kann später auf YAML-Felder wie `stage`, `status`, `source_skill`, `previous_event`, `external_outputs` und `tags` zugreifen. `ASSETS.md` verbindet den lokalen Wissensgraphen mit den externen Drive-Artefakten.

## Integrationspunkte in Skillz

Die Capability ist direkt in folgende Lifecycle-Entrypoints eingebunden:

- `round-based-requirements-grilling` — Bootstrap des ersten Project-Memory-Events,
- `large-work-wayfinder` — technische Evidenz und Routing,
- `conversation-to-spec` — normative Spezifikation und Freigabe,
- `spec-to-vertical-issues` — Backlog und Requirement-Traceability,
- `iterate-software-projects` — Implementation, Review, Delivery und nächste Iteration,
- `agent-handoff` — Fortsetzung ohne erneute Vollanalyse,
- weitere Workflows mit `project-second-brain` als Abhängigkeit — einschließlich Creative-Writing- und Release-Flows.

Die tieferen Producer-Skills behalten ihre bisherigen Output-Verträge. `project-second-brain` entscheidet nicht über den fachlichen Inhalt der Datei, sondern stellt sicher, dass nicht-textuelle dokumentarische Artefakte im gemeinsamen Projekt-Drive auffindbar, verifiziert und mit dem Projektgraphen verbunden sind.