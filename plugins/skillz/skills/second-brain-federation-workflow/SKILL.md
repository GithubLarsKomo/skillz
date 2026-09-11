---
name: second-brain-federation-workflow
description: Verbindet mehrere Project Second Brains mit einem privaten Super Second Brain als verifizierten Registry-, Routing- und Discoverability-Layer. Verwendet Project-Memory-Zustände als Quellen, prüft Repository-Verfügbarkeit und Freshness, registriert nur Metadaten und Links statt fachliche Inhalte zu duplizieren und unterstützt sowohl einzelne Projekt-Repositories als auch Collection-Repositories mit mehreren Matters oder Projekten.
---

# Second Brain Federation Workflow

## Zweck

Dieser Workflow verbindet mehrere eigenständige `project-second-brain`-Instanzen mit einem **Super Second Brain**. Das Super Second Brain ist kein weiterer fachlicher Speicher und keine Kopie der Child Brains. Es ist ein privater, versionierter **Index-, Routing- und Discoverability-Layer**.

Seine Kernfrage lautet:

**Welcher Second Brain besitzt den relevanten Kontext, ist er erreichbar und wo befindet sich sein aktueller kanonischer Einstiegspunkt?**

Die fachliche Wahrheit bleibt immer im jeweiligen Child Brain und dessen kanonischen Producer-Artefakten.

## Trigger

Verwenden:

- wenn ein neuer Project Second Brain oder ein neues Collection-Repository angelegt wurde,
- wenn ein bestehender Second Brain umbenannt, verschoben, archiviert oder wieder aktiviert wurde,
- wenn Workflow-Familien oder Scope eines Second Brains wesentlich geändert wurden,
- wenn der Nutzer eine Gesamtsicht, einen globalen Einstieg oder ein Routing über mehrere Second Brains verlangt,
- für einen expliziten Refresh der Verfügbarkeit oder Freshness registrierter Brains,
- beim Bootstrap eines Super Second Brains aus bereits vorhandenen Child Brains.

Nicht bei jedem einzelnen Project-Memory-Event einen Cross-Repository-Write erzwingen. Normale fachliche Ereignisse bleiben lokal. Der Federation State wird bei strukturellen Änderungen, Handoffs, expliziten Refreshes oder bewusst gewählten Meilensteinen aktualisiert.

## Architektur

```text
                         Super Second Brain
                    registry / routing / index
                               |
          +--------------------+--------------------+
          |                    |                    |
          v                    v                    v
   Project Second Brain   Collection Brain    Project Second Brain
      project A            domain / matters       project B
          |                    |                    |
          v                    v                    v
 canonical artifacts     projects/<id>/...    canonical artifacts
```

### Child Brain

Ein Child Brain bleibt autonome Source of Truth für:

- Projektzustand,
- Decisions,
- Timeline und Events,
- fachliche Evidence,
- externe Asset-Referenzen,
- lokale nächste Aktionen.

### Super Brain

Das Super Brain besitzt ausschließlich:

- Registry der bekannten Second Brains,
- verifizierte Repository- und Root-Referenzen,
- Scope und Workflow-Familien,
- Availability/Freshness,
- kurze nicht-sensitive Routing-Zusammenfassungen,
- Federation Events wie Register, Move, Archive, Reactivate oder Refresh,
- Links zum kanonischen Child Brain.

Es besitzt **keine Kopie** von SPECs, Vertragsinhalten, Coaching-Notizen, Trainingsdaten, Investigation Evidence, Manuskripten oder anderen fachlichen Child-Inhalten.

## Private-by-default Gate

Ein Super Second Brain aggregiert Metadaten über mehrere Lebens- und Arbeitsbereiche. Dadurch kann bereits die Existenz oder Benennung einzelner Child Brains sensibel sein.

Daher gilt:

1. Das kanonische Super-Brain-Repository ist standardmäßig **privat**.
2. Eine reale Registry mit privaten Repository-Namen wird nicht in ein öffentliches Framework-Repository wie `skillz` geschrieben.
3. Öffentliche Skills enthalten nur Schema, Workflow und Beispiele mit neutralen Platzhaltern.
4. Child-Brain-Sichtbarkeit wird beobachtet und dokumentiert, nicht erraten.
5. Inhalte eines privaten Child Brains werden niemals in einen weniger geschützten Super Brain kopiert.

Wenn kein ausreichend geschütztes Super-Brain-Repository verfügbar ist, bleibt Federation `pending`.

## Super-Brain-Struktur

Empfohlene Struktur:

```text
README.md
docs/super-memory/
├── INDEX.md
├── REGISTRY.md
├── registry.json
├── state.json
├── brains/
│   ├── <brain-id>.md
│   └── ...
├── domains/
│   └── <domain>.md
└── events/
    └── FED-YYYYMMDD-HHMMSS-<slug>.md
```

- `INDEX.md` ist der globale Einstieg für Mensch, GitHub und Obsidian.
- `REGISTRY.md` ist die lesbare Registry.
- `registry.json` ist die maschinenlesbare Source of Truth der Federation.
- `state.json` hält letzten Sync, bekannte offene Probleme und nächste Federation-Aktion.
- `brains/` enthält pro Child Brain genau eine Routing-Note.
- `domains/` ist optional und gruppiert Brains nach Domäne oder Workflow-Familie.
- `events/` dokumentiert strukturelle Federation-Änderungen append-orientiert.

## Child-Brain-Modi

### `project`

Ein Repository repräsentiert primär ein einzelnes langlebiges Projekt. Standard-Root:

```text
docs/project-memory/INDEX.md
```

### `collection`

Ein Repository repräsentiert eine Domäne mit mehreren Matters oder Projekten. Der Domain-Level-Root darf weiterhin unter `docs/project-memory/` liegen; einzelne Cases liegen bevorzugt unter:

```text
projects/<project-or-matter-id>/docs/project-memory/
```

Das Super Brain registriert das Collection-Repository als Einheit und darf zusätzlich aktive Child Roots referenzieren. Es kopiert deren Inhalt nicht.

## Registry Contract

Jeder Registry-Eintrag enthält mindestens:

```json
{
  "brainId": "stable-brain-id",
  "label": "Human-readable label",
  "mode": "project",
  "scope": "short routing scope",
  "repository": "owner/repository",
  "repositoryVisibility": "private",
  "projectMemoryRoot": "docs/project-memory/INDEX.md",
  "status": "available",
  "workflowFamilies": ["example-workflow"],
  "tags": ["example-domain"],
  "lastVerifiedAt": "2026-09-11T17:00:00+02:00",
  "latestEventRef": null
}
```

Zulässige `status`-Werte:

- `available` – Repository und deklarierter Einstieg wurden verifiziert,
- `bootstrap-needed` – Repository existiert, Project-Memory-Struktur fehlt noch,
- `pending` – erwarteter Brain ist konfiguriert, aber nicht vollständig prüfbar,
- `unavailable` – zuvor bekannter Brain ist aktuell nicht erreichbar,
- `archived` – bewusst historisiert und nicht mehr aktives Routingziel.

Repository-Verfügbarkeit und Project-Memory-Verfügbarkeit sind getrennt zu behandeln. Ein erreichbares leeres Repository ist `bootstrap-needed`, nicht bereits ein vollständig verfügbarer Project Brain.

## Initial Bootstrap

Wenn ein Super Second Brain erstmals angelegt wird:

1. Kandidatenliste der bereits bekannten Second Brains bestimmen.
2. Jedes Repository einzeln auf Existenz, Zugriff, Sichtbarkeit und Default Branch prüfen.
3. Project-Memory-Root oder äquivalente bestehende Struktur prüfen.
4. `mode`, `scope`, `workflowFamilies` und Tags aus bestätigtem Kontext bestimmen; keine sensiblen Inhalte ableiten.
5. Für jeden Brain eine Routing-Note unter `brains/` erzeugen.
6. `registry.json`, `REGISTRY.md` und `INDEX.md` konsistent erzeugen.
7. einen Federation-Bootstrap-Event schreiben.
8. read-back-verifizieren, dass alle erwarteten Brains entweder registriert oder explizit als `pending`, `bootstrap-needed` oder `unavailable` markiert sind.

Der Bootstrap ist erst abgeschlossen, wenn **kein Kandidat stillschweigend verloren ging**.

## Federation Sync

### 1. Child identifizieren

Nutze stabile `brainId` und den zuletzt verifizierten Repository-Identifier. Namen allein sind bei Rename oder Migration nicht ausreichend.

### 2. Availability prüfen

Verifiziere mindestens:

- Repository erreichbar,
- beobachtete Sichtbarkeit,
- Default Branch,
- deklarierter Project-Memory-Root oder Bootstrap-Bedarf,
- soweit verfügbar letzter verifizierter Child-Event oder Child-State.

### 3. Delta bestimmen

Klassifiziere:

- neu,
- unverändert,
- metadata-changed,
- moved/renamed,
- bootstrap-needed,
- unavailable,
- archived/reactivated.

### 4. Registry aktualisieren

Nur Federation-Metadaten ändern. Keine fachlichen Child-Artefakte spiegeln.

### 5. Federation Event schreiben

Ein Event ist erforderlich bei Register, Rename/Move, Scope-Änderung, Archive/Reactivate, Availability-Transition oder strukturellem Bootstrap. Reine bestätigte Unverändertheit braucht keinen Event.

### 6. Read-back

Nach Writes Registry und betroffene Routing-Notes erneut lesen. Keine erfolgreiche Synchronisierung behaupten, wenn der Zielzustand nicht beobachtet wurde.

## Routing

Wenn ein Auftrag Kontext aus einem Second Brain benötigt:

1. Super Registry lesen.
2. Kandidaten anhand `scope`, `workflowFamilies`, Tags und Status auswählen.
3. Nur `available` oder bewusst akzeptierte `bootstrap-needed` Kandidaten routen.
4. Bei mehreren plausiblen Brains deren Scope vergleichen; keine Inhalte raten.
5. kanonischen Child Root lesen.
6. ab dort normalen `project-second-brain`- und Fachworkflow verwenden.

Das Super Brain beantwortet keine fachliche Frage aus seinem eigenen Kurzabstract, wenn der Child Brain erreichbar ist.

## Cross-Brain-Verknüpfungen

Verbindungen zwischen Projekten werden im Super Brain als **Relationen**, nicht als zusammenkopierte Inhalte, dokumentiert. Beispiele:

- `supports`,
- `depends-on`,
- `shares-evidence-with`,
- `supersedes`,
- `related-domain`,
- `derived-from`.

Jede Relation nennt beide `brainId`-Werte und einen kurzen, nicht-sensitiven Grund. Bei fachlich sensitiver Relation genügt ein neutraler Relationstyp ohne Detailtext.

## Failure Handling

- **Super Brain fehlt:** Bootstrap-Manifest vorbereiten, Federation `pending`; Child Brains funktionieren weiter.
- **Child Repo existiert, Memory fehlt:** `bootstrap-needed`; nicht `available` vortäuschen.
- **Child vorübergehend nicht erreichbar:** letzten bekannten Registry-Eintrag behalten, Status `unavailable`, Freshness markieren.
- **Rename/Move:** stabile `brainId` beibehalten und Repository-Referenz aktualisieren; Historie nicht als neuen Brain duplizieren.
- **Privacy-Konflikt:** keinen Inhalt in weniger geschützte Ebene kopieren; Sync abbrechen oder Metadaten weiter minimieren.
- **Widersprüchliche Registry-Daten:** kein stilles Überschreiben; als Reconciliation-Bedarf markieren.

## Handoff

Nach erfolgreicher Federation kann ein Handoff enthalten:

```json
{
  "superSecondBrain": {
    "repository": "owner/private-super-brain",
    "index": "docs/super-memory/INDEX.md",
    "registry": "docs/super-memory/registry.json",
    "lastVerifiedAt": "observed timestamp"
  },
  "projectMemory": {
    "brainId": "stable-brain-id",
    "root": "docs/project-memory/INDEX.md"
  }
}
```

Alle Werte müssen beobachtet oder aus kanonischer Registry gelesen sein.

## Abschlusskriterien

Der Workflow ist abgeschlossen, wenn:

- das Super-Brain-Repository geschützt und erreichbar ist oder explizit `pending` bleibt,
- alle bekannten Child-Brain-Kandidaten klassifiziert wurden,
- jeder registrierte Brain einen stabilen `brainId`, Scope, Modus und Repository-Status besitzt,
- keine fachliche Wahrheit aus Child Brains dupliziert wurde,
- reale private Repository-Namen nicht in öffentliche Framework-Artefakte gelangt sind,
- Registry, Human Index und Routing-Notes konsistent und read-back-verifiziert sind,
- ein Agent vom Super Brain deterministisch zum kanonischen Child Brain routen kann.
