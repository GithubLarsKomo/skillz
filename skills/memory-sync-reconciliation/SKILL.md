---
name: memory-sync-reconciliation
description: Gleicht mehrere bereits governance-konforme Kommunikationsprofile und Memory-Ledger deterministisch ab, propagiert Forget/Supersession/Expiry sicher und legt echte Konflikte zur Auflösung vor. Verwenden, wenn Memory-Stände aus unterschiedlichen Sitzungen, Clients oder Persistenzkanälen konvergieren sollen, ohne neue Memories zu erfinden.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - communication-memory-governance
outputs:
  - memory-reconciliation-plan.json
  - communication-profile.merged.json
  - memory-ledger.merged.json
lastEvaluated: 2026-08-02
implicitInvocation: true
---

# Memory Sync Reconciliation

## Zweck und Grenze

Dieser Skill reconciliert zwei oder mehr bereits durch `communication-memory-governance` erzeugte Zustände. Er entscheidet **nicht**, welche neue Information zu Memory werden darf, und extrahiert keine neuen Erinnerungen aus Gesprächen.

Die Zuständigkeiten bleiben getrennt:
- `communication-memory-governance`: Aktivierung, Sensitivität, Scope und Memory-Lebenszyklus,
- `memory-sync-reconciliation`: Vergleich und Konvergenz bereits governance-konformer Snapshots,
- `chatgpt-communication`: Persistenz-/Channel-Layer,
- andere Skills: Projekt-, Session-, Entscheidungs- und Follow-up-Zustände.

## Voraussetzungen

Mindestens zwei Snapshot-Paare mit:
- `communication-profile.json`,
- `memory-ledger.json`,
- stabiler Snapshot-/Source-ID,
- `asOf`-Zeitpunkt,
- unveränderten Ledger-IDs und Lineage-Referenzen.

Fehlen Identitäten oder Lineage, darf nicht durch Textähnlichkeit so getan werden, als seien Einträge sicher identisch.

## Reconciliation-Klassen

Jeder Vergleich fällt in genau eine Klasse:

### 1. Identical
Gleiche Ledger-ID und semantisch gleiche governance-relevante Felder. Keine Änderung.

### 2. Compatible additive
Unabhängige Einträge mit verschiedenen IDs und nicht widersprechendem Scope/Inhalt. Beide bleiben erhalten.

### 3. Lineage update
Explizite `supersedes`/`supersededBy`-Beziehung oder identische Ledger-ID mit nachvollziehbarer Lifecycle-Fortschreibung. Neuere Lifecycle-Wirkung wird übernommen, ohne Historie zu löschen.

### 4. Tombstone propagation
Forget/Removal, `rejected`, `expired` oder explizite Deaktivierung darf durch eine stale aktive Kopie nicht rückgängig gemacht werden. Der deaktivierende Zustand wird an alle Merge-Ausgaben propagiert.

### 5. Hard conflict
Zwei aktive, nicht durch Lineage verbundene Aussagen widersprechen sich im gleichen Scope. Beide bleiben sichtbar; keine wird automatisch aktiv bevorzugt.

### 6. Unresolved identity ambiguity
Ähnliche Aussagen ohne stabile IDs/Lineage oder widersprüchliche Metadaten. Kein Auto-Merge.

## Präzedenzregeln

### Explizite Lifecycle-Semantik vor Zeitstempel
`superseded`, Forget/Removal, `rejected` und `expired` sind semantische Zustände. Ein später geschriebener Snapshot mit älterem fachlichem Zustand darf sie nicht durch Last-write-wins reaktivieren.

### Explizite User-Korrektur vor unbestätigter Kopie
Wenn Provenance eindeutig eine explizite User-Korrektur bzw. Forget-Anweisung belegt und die andere Seite nur einen älteren aktiven Zustand enthält, wird die Korrektur propagiert.

### Kein generelles Last-write-wins
`asOf`, Dateimodifikation oder Sync-Zeit allein entscheiden keinen semantischen Konflikt.

### Keine synthetischen Memories
Der Merge darf keine neue Aussage formulieren, die in keinem Input als governance-konformer Eintrag existiert.

## Ablauf

1. **Snapshots fixieren** – IDs, `asOf`, Source und Hash/Version soweit verfügbar erfassen.
2. **Schema-/Governance-Kompatibilität prüfen** – nicht-governance-konforme Inputs stoppen oder isolieren.
3. **Ledger-IDs indexieren** – gleiche IDs zuerst vergleichen.
4. **Lineage-Graph bilden** – `supersedes`/`supersededBy` deterministisch auflösen; Zyklen sind Blocker.
5. **Lifecycle propagieren** – Tombstones, Forget, Rejection, Expiry und Supersession anwenden.
6. **Scope-Konflikte prüfen** – aktive konkurrierende Aussagen mit gleichem Geltungsbereich markieren.
7. **Communication Profile ableiten** – ausschließlich aus konfliktfreien aktiven Communication-Preference-Einträgen.
8. **Plan erzeugen** – jede Änderung mit Ursache, Quell-ID und Aktion dokumentieren.
9. **Merged Outputs erzeugen** – deterministisch sortiert, ohne Persistenzmutation.
10. **Idempotenz prüfen** – erneute Reconciliation der konvergierten Outputs muss `no-op` ergeben.

## Konfliktbehandlung

Ein Hard Conflict wird nicht durch Confidence, Aktualität oder Mehrheit allein entschieden. `memory-reconciliation-plan.json` enthält mindestens:
- Konflikt-ID,
- betroffene Ledger-IDs,
- Scope,
- konkurrierende Statements,
- Provenance/Confirmation-Metadaten,
- Grund, warum keine deterministische Präzedenz zulässig ist,
- `resolutionState: human-required`.

Solange der Konflikt offen ist, darf keine konkurrierende Preference in `communication-profile.merged.json` als konfliktfrei aktiv erscheinen.

## Forget- und Removal-Semantik

Forget ist eine Sicherheitsinvariante. Wenn ein Snapshot einen Eintrag als entfernt/rejected bzw. durch eine explizite Forget-Aktion nicht mehr nutzbar markiert und diese Lifecycle-Aktion governance-konform belegt ist:
- darf kein stale Snapshot den Inhalt wieder aktivieren,
- muss der aktive Profilbezug entfernt bleiben,
- darf Persistenz-Historie nur so weit erhalten werden, wie der zugrunde liegende Storage-/Privacy-Vertrag es erlaubt,
- enthält der Reconciliation-Plan keine unnötige Wiederholung des vergessenen Statements.

## Output-Verträge

### `memory-reconciliation-plan.json`

```json
{
  "schemaVersion": 1,
  "inputs": [],
  "classificationCounts": {},
  "actions": [],
  "conflicts": [],
  "blocked": false,
  "idempotenceExpected": true
}
```

Aktionen sind z. B. `keep`, `add`, `propagate-lifecycle`, `deactivate`, `mark-conflict`, `no-op`. Keine Aktion bedeutet externe Persistenz sei bereits erfolgt.

### `memory-ledger.merged.json`

Enthält die unionierte, deterministisch sortierte Ledger-Historie mit korrektem Lifecycle und vollständiger Provenance/Lineage. Bestehende IDs werden nicht neu vergeben.

### `communication-profile.merged.json`

Enthält nur aktive, konfliktfreie, zulässige Kommunikationspräferenzen plus sichtbare Konfliktreferenzen. Es wird ausschließlich aus dem gemergten Ledger abgeleitet.

## Determinismus

Bei denselben kanonischen Inputs muss Byte-/Semantik-relevant dieselbe Sortierung und Entscheidung entstehen. Input-Reihenfolge darf das Ergebnis nicht verändern.

Empfohlene stabile Sortierung:
1. Scope,
2. Kind,
3. Ledger-ID.

## Datenschutzgrenzen

Die Datenschutzregeln von `communication-memory-governance` gelten unverändert. Reconciliation darf verbotene Inhalte nicht durch Zusammenführung neu persistierbar machen. Keine Secrets, Roh-Connector-Payloads oder Transkripte in Plan oder Merged Outputs kopieren.

## Qualitätsgate

Bestanden nur wenn:
- keine neuen Memory-Statements erfunden werden,
- Forget/Removal nicht durch stale aktive Kopien reaktiviert werden,
- Supersession über Lineage statt Last-write-wins erfolgt,
- echte Konflikte sichtbar und human-required bleiben,
- IDs, Provenance, Scope und Lifecycle erhalten bleiben,
- Input-Reihenfolge das Ergebnis nicht beeinflusst,
- erneute Reconciliation der konvergierten Outputs semantisch ein No-op ist,
- keine externe Persistenz als ausgeführt behauptet wird.
