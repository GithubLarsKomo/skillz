---
name: two-axis-code-review
description: Prüft eine Änderung unabhängig auf Anforderungsabdeckung und auf Implementierungs- sowie Lieferqualität. Verwendet zwei getrennte Evidenzachsen für Spezifikationstreue, Codequalität, Architektur, Tests, Sicherheit, Migrationen und Betriebsrisiken und liefert priorisierte, kleinste sichere Abhilfen ohne stilgetriebene Blocker oder spekulative Neuschreibung.
userFacing: true
implicitInvocation: true
category: engineering
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
  - delivery-review-handoff.json
lastEvaluated: 2026-08-08
---

# Two-Axis Code Review

## Trigger

Diesen Skill verwenden, wenn ein klar abgegrenzter Commit, Branch oder Pull Request gegen sein Issue beziehungsweise seine Spezifikation und unabhängig davon gegen technische Lieferqualität geprüft werden soll.

## Voraussetzungen

Benötigt werden unveränderlicher Repositoryzustand, Base- und Head-SHA, Diff, zugehöriges Issue oder Spezifikation mit Akzeptanzkriterien, relevante Tests, Migrationsartefakte, Sicherheitsgrenzen und Betriebsbedingungen. Fehlt die Anforderungsgrundlage, darf Achse 1 nicht als bestanden gelten.

## Harte Review-/Delivery-Grenzen

- Jede Review-Evidenz gilt nur für den exakt fixierten `reviewedHeadSha`.
- Ein neuer Commit, Rebase, Konfliktauflösungs-, Formatierungs- oder sonstiger Head-Wechsel macht die bestehende Review-Freigabe `stale`; auch ein vermeintlich kleiner Diff wird nicht stillschweigend in die alte Freigabe aufgenommen.
- `approve` beziehungsweise `approve-with-notes` bedeutet ausschließlich **review-approved für den geprüften Head**. Es beweist weder aktuelle Required Checks noch Mergefähigkeit, Merge, Deployment, Release oder Issue-/Requirement-Closure.
- Grüne CI ist Evidenz innerhalb der Lieferqualität, aber CI-Status kann nach dem Review veralten oder sich auf einen anderen SHA beziehen. Externe Delivery-Gates werden nachgelagert durch `engineering-delivery-followup` verifiziert.
- Nicht-blockierende Notes und Residual Risks bleiben explizite Handoff-Elemente und verschwinden nicht durch eine Freigabeentscheidung.

## Ablauf

### 1. Prüfobjekt fixieren

Verifiziere Repository, Base, Head, Head-SHA, Diff und bereits vorliegende CI- oder Testevidenz. Speichere den unveränderlichen SHA als `reviewedHeadSha`. Prüfe keine bewegliche Referenz und verwechsle grüne CI nicht mit vollständiger Korrektheit.

### 2. Achse 1: Anforderungskorrektheit

Ordne jedes Akzeptanzkriterium genau einer der Kategorien `erfüllt`, `teilweise`, `nicht erfüllt` oder `nicht verifizierbar` zu. Belege die Einstufung mit beobachtbarem Verhalten, Tests, Diffstellen oder fehlender Evidenz. Ein fehlendes oder falsch umgesetztes Kriterium bleibt blockierend, auch wenn der Code technisch sauber ist.

### 3. Achse 2: Implementierungs- und Lieferqualität

Prüfe unabhängig davon Codeverständlichkeit, Fehlerbehandlung, Dateninvarianten, Tests, Architekturgrenzen, Sicherheit, Migrationen, Kompatibilität, Rollback und Betriebsrisiken. Nutze `architecture-deepening-review` nur bei belegter Kopplung oder duplizierten Regeln und `disciplined-diagnosis` bei unklaren Fehlerursachen.

### 4. Befunde priorisieren

Jeder Befund enthält Achse, Schweregrad, konkrete Evidenz, Auswirkung, kleinste sichere Abhilfe und Verifikation. Blockierend sind nur nachgewiesene Anforderungsverstöße oder erhebliche Qualitäts-, Sicherheits-, Migrations- oder Betriebsrisiken. Stilpräferenzen, spekulative Architektur und Duplikate sind nicht blockierend.

### 5. Entscheidung ableiten

Bewerte beide Achsen getrennt als `pass`, `pass-with-notes`, `block` oder `unknown`. Die Gesamtentscheidung darf nur freigeben, wenn keine Achse blockiert und keine entscheidende Unsicherheit verborgen ist. Grüne CI allein ist niemals hinreichend.

Die Gesamtentscheidung ist auf `reviewedHeadSha` beschränkt. Sie darf nicht als `merged`, `deployed`, `released`, `issue-closed` oder `requirement-closed` formuliert werden.

### 6. Delivery-Handoff erzeugen

Erzeuge zusätzlich `delivery-review-handoff.json` mit:

- Repository, Base, Branch/PR und `reviewedHeadSha`,
- Achse-1-/Achse-2-Status,
- Review Decision,
- blockierenden Findings,
- nicht-blockierenden Notes und Residual Risks,
- lokal vorliegenden Check-/Test-Referenzen,
- noch erforderlichen externen Delivery-Gates,
- `reviewFreshness: fresh|stale|unknown`,
- nächstem zulässigem Skill.

Bei freigabefähigem Review ist `nextSkill` grundsätzlich `engineering-delivery-followup`. Bei `request-changes` bleibt der Handoff bei `implement-from-issue`; bei unklarer Ursache bei `disciplined-diagnosis`.

### 7. Handoff prüfen

Verifiziere unmittelbar vor Ausgabe erneut, dass der referenzierte Head noch dem `reviewedHeadSha` entspricht, soweit der aktuelle Repositoryzustand zugänglich ist. Hat sich der Head bereits verändert, setze `reviewFreshness=stale` und gib keine aktive Review-Freigabe für den neuen Stand weiter.

## Prüfungen

Vor Abschluss müssen alle Akzeptanzkriterien sichtbar abgedeckt, beide Achsen getrennt bewertet, Befunde dedupliziert, Schweregrade begründet, Abhilfen eng begrenzt und Sicherheits-, Migrations-, Kompatibilitäts- sowie Betriebswirkungen explizit behandelt sein. Review Decision und Handoff müssen denselben `reviewedHeadSha` referenzieren.

## Fehlerbehandlung

Stoppe und korrigiere den Review, wenn persönliche Stilvorlieben als Blocker erscheinen, eine breite Neuschreibung empfohlen wird, identische Befunde mehrfach auftauchen, Achsen vermischt werden, Freigabe allein aus grüner CI abgeleitet wird oder eine Review-Freigabe nach einem Head-Wechsel ohne erneute Prüfung weiterverwendet werden soll.

## Übergabe

```json
{
  "repository": {"name": "...", "base": "...", "head": "...", "reviewedHeadSha": "..."},
  "axis1": {"status": "pass|pass-with-notes|block|unknown", "criteria": [{"id": "...", "status": "fulfilled|partial|missing|unverified", "evidence": ["..."]}]},
  "axis2": {"status": "pass|pass-with-notes|block|unknown", "findings": [{"severity": "blocking|high|medium|low|note", "evidence": "...", "impact": "...", "remediation": "...", "verification": "..."}]},
  "decision": "approve|approve-with-notes|request-changes|insufficient-evidence",
  "reviewFreshness": "fresh|stale|unknown",
  "residualRisks": ["..."],
  "externalDeliveryGates": ["..."],
  "nextSkill": "engineering-delivery-followup|implement-from-issue|disciplined-diagnosis|agent-handoff"
}
```

## Memory Path

Persistenzwürdig sind abstrahierte Review-Heuristiken wie Zwei-Achsen-Trennung, SHA-Freshness und wiederverwendbare Failure Modes. Konkrete Repository-/PR-/Issue-IDs, SHAs, aktuelle Findings, unveröffentlichter Code und volatile CI-/Merge-Zustände bleiben Run-/Project-State. Übergib nur geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; dieser Skill persistiert nichts selbst.

## Abschlusskriterien

Abgeschlossen ist der Review, wenn Anforderungskorrektheit und Lieferqualität unabhängig, vollständig und evidenzbasiert bewertet, blockierende Befunde der richtigen Achse zugeordnet und ein SHA-gebundener Delivery-Handoff mit genau der nächsten zulässigen Aktion erzeugt wurde. Eine Review-Freigabe ist ausdrücklich noch keine Delivery-/Merge-/Release-Closure.
