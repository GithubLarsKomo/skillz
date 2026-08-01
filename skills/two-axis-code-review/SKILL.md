---
name: two-axis-code-review
description: Prüft eine Änderung unabhängig auf Anforderungsabdeckung und auf Implementierungs- sowie Lieferqualität. Verwendet zwei getrennte Evidenzachsen für Spezifikationstreue, Codequalität, Architektur, Tests, Sicherheit, Migrationen und Betriebsrisiken und liefert priorisierte, kleinste sichere Abhilfen ohne stilgetriebene Blocker oder spekulative Neuschreibung.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - implement-from-issue
  - architecture-deepening-review
  - disciplined-diagnosis
  - agent-handoff
outputs:
  - requirement-coverage.json
  - quality-review.json
  - review-decision.md
lastEvaluated: 2026-08-01
---

# Two-Axis Code Review

## Trigger

Diesen Skill verwenden, wenn ein klar abgegrenzter Commit, Branch oder Pull Request gegen sein Issue beziehungsweise seine Spezifikation und unabhängig davon gegen technische Lieferqualität geprüft werden soll.

## Voraussetzungen

Benötigt werden unveränderlicher Repositoryzustand, Base- und Head-SHA, Diff, zugehöriges Issue oder Spezifikation mit Akzeptanzkriterien, relevante Tests, Migrationsartefakte, Sicherheitsgrenzen und Betriebsbedingungen. Fehlt die Anforderungsgrundlage, darf Achse 1 nicht als bestanden gelten.

## Ablauf

### 1. Prüfobjekt fixieren

Verifiziere Repository, Base, Head, Head-SHA, Diff und bereits vorliegende CI- oder Testevidenz. Prüfe keine bewegliche Referenz und verwechsle grüne CI nicht mit vollständiger Korrektheit.

### 2. Achse 1: Anforderungskorrektheit

Ordne jedes Akzeptanzkriterium genau einer der Kategorien `erfüllt`, `teilweise`, `nicht erfüllt` oder `nicht verifizierbar` zu. Belege die Einstufung mit beobachtbarem Verhalten, Tests, Diffstellen oder fehlender Evidenz. Ein fehlendes oder falsch umgesetztes Kriterium bleibt blockierend, auch wenn der Code technisch sauber ist.

### 3. Achse 2: Implementierungs- und Lieferqualität

Prüfe unabhängig davon Codeverständlichkeit, Fehlerbehandlung, Dateninvarianten, Tests, Architekturgrenzen, Sicherheit, Migrationen, Kompatibilität, Rollback und Betriebsrisiken. Nutze `architecture-deepening-review` nur bei belegter Kopplung oder duplizierten Regeln und `disciplined-diagnosis` bei unklaren Fehlerursachen.

### 4. Befunde priorisieren

Jeder Befund enthält Achse, Schweregrad, konkrete Evidenz, Auswirkung, kleinste sichere Abhilfe und Verifikation. Blockierend sind nur nachgewiesene Anforderungsverstöße oder erhebliche Qualitäts-, Sicherheits-, Migrations- oder Betriebsrisiken. Stilpräferenzen, spekulative Architektur und Duplikate sind nicht blockierend.

### 5. Entscheidung ableiten

Bewerte beide Achsen getrennt als `pass`, `pass-with-notes`, `block` oder `unknown`. Die Gesamtentscheidung darf nur freigeben, wenn keine Achse blockiert und keine entscheidende Unsicherheit verborgen ist. Grüne CI allein ist niemals hinreichend.

### 6. Handoff erzeugen

Gib unveränderlichen Head-SHA, Anforderungsabdeckung, Qualitätsbefunde, Restrisiken und genau den nächsten Schritt aus. Für Korrekturen verweise auf `implement-from-issue`; bei verbleibender Unsicherheit oder externer Prüfung auf den passenden Diagnose- oder Handoff-Skill.

## Prüfungen

Vor Abschluss müssen alle Akzeptanzkriterien sichtbar abgedeckt, beide Achsen getrennt bewertet, Befunde dedupliziert, Schweregrade begründet, Abhilfen eng begrenzt und Sicherheits-, Migrations-, Kompatibilitäts- sowie Betriebswirkungen explizit behandelt sein.

## Fehlerbehandlung

Stoppe und korrigiere den Review, wenn persönliche Stilvorlieben als Blocker erscheinen, eine breite Neuschreibung empfohlen wird, identische Befunde mehrfach auftauchen, Achsen vermischt werden oder Freigabe allein aus grüner CI abgeleitet wird.

## Übergabe

```json
{
  "repository": {"name": "...", "base": "...", "head": "...", "headSha": "..."},
  "axis1": {"status": "pass|pass-with-notes|block|unknown", "criteria": [{"id": "...", "status": "fulfilled|partial|missing|unverified", "evidence": ["..."]}]},
  "axis2": {"status": "pass|pass-with-notes|block|unknown", "findings": [{"severity": "blocking|high|medium|low|note", "evidence": "...", "impact": "...", "remediation": "...", "verification": "..."}]},
  "decision": "approve|approve-with-notes|request-changes|insufficient-evidence",
  "residualRisks": ["..."],
  "nextSkill": "implement-from-issue|disciplined-diagnosis|agent-handoff"
}
```

## Abschlusskriterien

Abgeschlossen ist der Review, wenn Anforderungskorrektheit und Lieferqualität unabhängig, vollständig und evidenzbasiert bewertet, blockierende Befunde der richtigen Achse zugeordnet und eine enge, ausführbare nächste Aktion mit unveränderlichem Repositoryzustand übergeben wurde.
