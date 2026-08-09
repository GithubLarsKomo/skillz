---
name: merge-conflict-resolution
description: Löst Git-Merge-Konflikte semantisch, rekonstruiert die Änderungsabsichten beider Seiten, bewahrt akzeptiertes Verhalten und Repository-Invarianten und erzeugt einen überprüfbaren Auflösungsstand mit Tests, Rollback und Restrisiken. Verwenden, wenn Konfliktmarker allein nicht zeigen, welche fachliche oder technische Kombination korrekt ist.
---

# Merge Conflict Resolution

## Trigger

Diesen Skill verwenden, wenn ein Merge, Rebase oder Cherry-pick Konflikte erzeugt und die korrekte Auflösung nicht durch blindes Übernehmen von `ours` oder `theirs` bestimmt werden darf.

## Voraussetzungen

Benötigt werden Repository, Operation, Base-, Ours- und Theirs-SHA, Konfliktdateien, zugehörige Issues oder Spezifikationen, Tests, Invarianten, Migrationen, Sicherheitsgrenzen und Betriebsbedingungen. Bewegliche Referenzen werden vor der Analyse in unveränderliche SHAs aufgelöst.

## Ablauf

### 1. Konfliktzustand fixieren

Dokumentiere Operation, Base, Ours, Theirs, Konfliktmarker, betroffene Dateien und bereits ausgeführte Git-Schritte. Verändere keine weiteren Dateien, bevor die Konfliktmenge und der Rückweg feststehen.

### 2. Beide Änderungsabsichten rekonstruieren

Lies Commits, Issues, Spezifikationen, Tests und angrenzenden Code beider Seiten. Beschreibe pro Konflikt, welches Verhalten jede Seite einführen, erhalten oder entfernen wollte. Unterscheide Textüberlappung, kompatible Absichten, konkurrierende Absichten und obsoletes Verhalten.

### 3. Semantische Entscheidung treffen

Erhalte akzeptiertes Verhalten beider Seiten, wenn die Absichten kompatibel sind. Bei konkurrierenden Produkt-, Daten- oder Architekturentscheidungen blockiere und fordere eine autorisierte Entscheidung an, statt stillschweigend eine Seite zu wählen. Begründe jede verworfene Alternative.

### 4. Kleinste Auflösung implementieren

Entferne Konfliktmarker und ändere nur die für die semantische Kombination nötigen Dateien. Unzulässig sind unabhängige Refactorings, breite Dependency-Upgrades, abgeschwächte Tests, geänderte Sicherheitskontrollen oder ungeplante Migrationen.

### 5. Verhalten verifizieren

Führe konfliktnahe Tests, relevante Regressionen, Typ-, Lint-, Build-, Schema-, Migrations- und Sicherheitsprüfungen aus. Nutze `test-driven-vertical-slice` für fehlende Akzeptanztests und `disciplined-diagnosis` bei unklaren Fehlerursachen.

### 6. Zwei-Achsen-Review durchführen

Nutze `two-axis-code-review`, um getrennt zu prüfen, ob beide akzeptierten Änderungsabsichten erfüllt sind und ob die Auflösung technisch, betrieblich und migrationsseitig sicher ist.

### 7. Reviewbaren Zustand übergeben

Dokumentiere pro Konflikt Absichten, Entscheidung, geänderte Dateien, Evidenz, Rollback und Restrisiken. Erzeuge einen überprüfbaren Commit oder PR mit exaktem resolved Head-SHA. Nicht verfügbare CI-, Deployment- oder Dienstprüfungen werden mit `deferred-external-action-verification` getrennt überwacht.

## Prüfungen

Vor Abschluss müssen alle Konfliktmarker entfernt, beide Absichten nachvollziehbar rekonstruiert, jede Entscheidung evidenzbasiert, akzeptiertes Verhalten getestet, Migrationen und Sicherheit geprüft, Rollback beschrieben und der unveränderliche Auflösungsstand festgehalten sein.

## Fehlerbehandlung

Stoppe und stelle den begrenzten Konfliktzustand wieder her, wenn `ours` oder `theirs` blind gewählt, eine Absicht ohne Begründung gelöscht, nur Marker statt Verhalten geprüft, Tests oder Sicherheitskontrollen geschwächt, unabhängiger Scope ergänzt oder externer Erfolg angenommen wird.

## Übergabe

```json
{
  "repository": {"name": "...", "operation": "merge|rebase|cherry-pick", "baseSha": "...", "oursSha": "...", "theirsSha": "...", "resolvedHeadSha": "..."},
  "conflicts": [{"path": "...", "classification": "textual|compatible|competing|obsolete", "oursIntent": "...", "theirsIntent": "...", "decision": "...", "discardedAlternatives": ["..."], "evidence": ["..."]}],
  "changedFiles": [{"path": "...", "rationale": "..."}],
  "verification": {"focused": ["..."], "regression": ["..."], "migration": ["..."], "security": ["..."], "external": ["..."]},
  "rollback": "...",
  "residualRisks": ["..."],
  "status": "locally-verified|externally-pending|blocked|complete",
  "nextSkill": "two-axis-code-review|disciplined-diagnosis|agent-handoff|deferred-external-action-verification"
}
```

## Abschlusskriterien

Abgeschlossen ist die Auflösung, wenn beide Änderungsabsichten und alle Invarianten semantisch berücksichtigt, jede Konfliktentscheidung geprüft, der reviewbare Head-SHA festgehalten und verbleibende externe oder autorisierungsbedürftige Punkte ehrlich übergeben wurden.
