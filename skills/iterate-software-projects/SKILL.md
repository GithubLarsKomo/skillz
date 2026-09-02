---
name: iterate-software-projects
description: Iterative Weiterentwicklung bestehender Softwareprojekte durch den wiederkehrenden Zyklus aus Bestandsanalyse, Klärung kritischer Produktentscheidungen, Auswahl des nächsten kleinen Inkrements, präzisem Copilot- oder Coding-Agent-Prompt und evidenzbasiertem Review. Verwenden, wenn ein Repository schrittweise fortgeführt, ein Plan vor der Umsetzung geschärft, ein nächster Implementierungsauftrag formuliert, ein Agentenergebnis geprüft, ein Docker-/KI-Service diagnostiziert oder nach einem Review die nächste Iteration geplant werden soll.
userFacing: true
implicitInvocation: true
category: engineering
version: 1.1.0
status: stable
owners:
  - GithubLarsKomo
requires:
  - project-second-brain
outputs:
  - review findings
  - next increment
  - verification evidence
  - engineering-iteration-state.json
lastEvaluated: 2026-09-02
---

# Softwareprojekte iterativ entwickeln

Arbeite als technischer Orchestrator. Halte Analyse, Implementierungsauftrag, Review und Delivery-Closure als getrennte Phasen, aber führe ihre Erkenntnisse in einer fortlaufenden Projektschleife zusammen.

## Arbeitsmodus bestimmen

Ermittle zuerst, welche Phase der Nutzer verlangt:

- **Analyse:** Repository und Laufzeitstatus untersuchen und das nächste sinnvolle Inkrement empfehlen.
- **Copilot-Prompt:** Einen unmittelbar ausführbaren Auftrag für Copilot oder einen anderen Coding-Agenten erzeugen.
- **Review:** Umsetzung, Diff, Tests und Laufzeitnachweise gegen den Auftrag prüfen.
- **Weiterentwicklung:** Alle Phasen nacheinander durchführen, soweit Zugriff und Auftrag dies erlauben.

Bei Formulierungen wie „wie bisher“, „prüfe und mache weiter“ oder „nächster Prompt“ den letzten **verifizierten Delivery-Zustand** rekonstruieren. Keine vermeintliche Projektkontinuität erfinden und eine reviewte, aber noch nicht gemergte beziehungsweise extern verifizierte Änderung nicht als bereits erledigte Iteration behandeln.

Wenn ein `projectMemory`-Verweis vorhanden ist, zuerst `docs/project-memory/state.json` und die letzten relevanten Events lesen. Diese ersetzen nicht Repository- oder Delivery-Evidenz, verhindern aber unnötige Wiederholung bereits dokumentierter Entscheidungen, erledigter Arbeit und verworfener Ansätze.

## Temporal Feedback Contract

Wenn für die vorherige Iteration `engineering-iteration-return-input.json` aus `engineering-delivery-followup` vorliegt, ist er ein expliziter Eingang der nächsten Iteration. Ein technischer Hard-Dependency-Zyklus wird bewusst vermieden.

Wenn aus Repository-/PR-/Issue-Evidenz erkennbar ist, dass eine vorherige Iteration reviewt oder zur Delivery übergeben wurde, aber kein belastbarer Return Input beziehungsweise gleichwertiger verifizierter Delivery-Zustand vorliegt:

- Status nicht als abgeschlossen erfinden,
- `deliveryContinuityGap` markieren,
- zuerst Review-Freshness, Required Checks, Merge/Deployment soweit relevant und Issue-/Requirement-Closure auflösen,
- erst danach ein unabhängiges neues Inkrement starten.

Trenne mindestens `implemented`, `review-approved`, `merge-ready`, `merged`, `deployed/released` soweit anwendbar, `issue-closed` und `requirement-verified`. Kein späterer Tracker- oder PR-Status ersetzt einen fehlenden fachlichen Nachweis.

## Fakten und Entscheidungen trennen

Vor jeder Rückfrage feststellen, ob die fehlende Information recherchierbar oder eine echte Nutzerentscheidung ist.

- **Fakten selbst ermitteln:** Repository, Projektregeln, bestehende Architektur, Tests, Logs, Schnittstellen, Versionen und bereits dokumentierte Präferenzen untersuchen. Den Nutzer nicht nach Dingen fragen, die durch verfügbare Quellen feststellbar sind.
- **Entscheidungen explizit machen:** Nur fragen, wenn mehrere plausible Wege Ziel, Scope, Architektur, Risiko oder späteren Aufwand wesentlich unterschiedlich beeinflussen und keine etablierte Präferenz die Wahl bereits bestimmt.
- **Abhängigkeiten ordnen:** Zuerst die Entscheidung klären, von der weitere Entscheidungen abhängen. Noch nicht über nachgelagerte Details diskutieren.
- **Einzeln fragen:** Pro Runde genau eine entscheidungsreife Frage stellen, die Folgen der Optionen knapp benennen und eine begründete Empfehlung als Standard anbieten.
- **Verständnis festhalten:** Nach jeder Antwort die Entscheidung mit ihrer Konsequenz in einem Satz fortschreiben. Widersprüche mit früheren Entscheidungen sofort sichtbar machen.

Keine Rückfrage stellen, wenn Faktenlage, Nutzerziel und etablierter Projektmodus eine risikoarme Wahl eindeutig nahelegen. Dann die Annahme nennen und fortfahren.

Bei einer noch offenen, irreversiblen oder weitreichenden Entscheidung weder Implementierung noch finalen Coding-Prompt erzeugen. Zuerst ein gemeinsames, widerspruchsfreies Verständnis von Ziel, Scope und Abnahmekriterien erreichen. Reversible Detailentscheidungen dürfen mit der empfohlenen Vorgabe in den Prompt aufgenommen werden.

## 1. Projektzustand rekonstruieren

1. Project-Memory-State und letzte relevante Events lesen, sofern vorhanden.
2. Projektregeln und vorhandene Spezifikationen lesen.
3. Branch, Status, letzte relevante Commits und aktuelle Änderungen prüfen.
4. Architektur, Services, Schnittstellen, Datenhaltung und Deployment erfassen.
5. Offene TODOs, fehlgeschlagene Tests, Logs, Review-Kommentare und provisorische Fixes sammeln.
6. Vorherigen Iterations-/Delivery-Status rekonstruieren: Issue/Requirement, Implementierungs-Head, `reviewedHeadSha`, aktuelle PR-/Branch-SHA, Required Checks, Merge State, Deployment/Release soweit Done-relevant, Tracker-/Requirement-Closure und undispositionierte Follow-ups.
7. Behauptungen in drei Klassen trennen: durch Quelltext belegt, durch Laufzeit-/Delivery-Evidenz belegt, noch unbestätigt.

Bei Docker-/KI-Projekten zuerst den realen Fehlerweg verfolgen: Servicezustand, Logs, Ports, Health-Endpunkt, interne und externe URLs, Abhängigkeiten und Netzwerkgrenzen. Lokale Proxy-Sonderfälle berücksichtigen; für lokale Tests bei Bedarf `--noproxy "*"` verwenden.

## 2. Nächstes Inkrement wählen

Bevor ein neues Inkrement gewählt wird, muss die vorherige Iteration dispositioniert sein:

- `closed`: darf als erledigt in `doNotRepeat` übernommen werden,
- `closed-with-followups`: Kernissue abgeschlossen, Follow-ups bleiben sichtbar und werden nur bei echter Priorität als neues Inkrement gewählt,
- `review-stale|blocked|pending|unknown`: zuerst die früheste Delivery-/Verification-Lücke schließen; kein unabhängiges neues Feature vorziehen, wenn dadurch ein unsicherer Integrationszustand verborgen würde.

Danach das kleinste Inkrement wählen, das eigenständig Wert liefert und überprüfbar abgeschlossen werden kann. In dieser Reihenfolge priorisieren:

1. Regressionen und Restfehler der letzten Iteration
2. offene Delivery-/Closure-Gaps der letzten Iteration
3. Reproduzierbarkeit eines bereits bewiesenen provisorischen Fixes
4. fehlende Tests, Migrationen, Dokumentation oder Betriebsnachweise
5. nächster fachlich kohärenter MVP-Baustein
6. Härtung, Automatisierung und Komfortfunktionen

Bestehende Architektur und Infrastruktur bevorzugen. Neue Komponenten nur einführen, wenn ihr Nutzen und ihre Integrationsgrenze klar sind. Größere Vorhaben phasenweise schneiden, beispielsweise isolierter MVP → Integration → Schnittstelle → Synchronisation → Härtung.

Vor Festlegung des Inkrements einen kurzen Entscheidungscheck durchführen:

1. Ist das Nutzerziel beobachtbar formuliert?
2. Sind In-Scope und Nicht-im-Scope widerspruchsfrei?
3. Sind irreversible Architektur-, Daten- oder Deployment-Entscheidungen geklärt?
4. Lassen sich Abnahmekriterien ausführen oder beobachten?
5. Ist die vorherige Iteration wirklich geschlossen oder ihr offener Delivery-Zustand explizit der nächste Schritt?

Nur offene Punkte klären, die das gewählte Inkrement tatsächlich verändern würden.

## 3. Implementierungsauftrag erzeugen

Für einen ausführbaren Copilot-Prompt die Schablone in [references/copilot-prompt.md](references/copilot-prompt.md) verwenden. Der Prompt muss ohne Rückfrage arbeitsfähig sein und mindestens enthalten:

- Rolle, Ziel und belegten Ausgangsstand
- ausdrücklich in und außerhalb des Scopes liegende Punkte
- konkrete Dateien oder Komponenten, soweit bekannt
- funktionale und nichtfunktionale Anforderungen
- Kompatibilitäts- und Architekturgrenzen
- erforderliche Tests und reale Funktionsnachweise
- Dokumentations- und Migrationspflichten
- Definition of Done
- bestätigte Nutzerentscheidungen sowie bewusst gesetzte reversible Annahmen
- Abschlussbericht mit geänderten Dateien, Tests, Risiken und Restpunkten

Nur dann Commit und Push verlangen, wenn der Nutzer dies beauftragt oder sein etablierter Projektmodus dies ausdrücklich vorsieht. Vor dem Commit Änderungen und Tests prüfen; keine fremden Änderungen einbeziehen.

## 4. Umsetzung reviewen

Den ursprünglichen Auftrag als Prüfbasis verwenden. Nicht nur prüfen, ob Dateien existieren, sondern ob das Verhalten nachgewiesen ist.

1. Diff und geänderte Dateien auf Scope-Treue prüfen.
2. Funktionale Anforderungen einzeln gegen Code und Tests abgleichen.
3. Relevante Tests, Linter, Builds und `git diff --check` ausführen.
4. Bei Services Health-/API-Aufrufe, Logs und einen echten Ende-zu-Ende-Fall prüfen.
5. Provisorische Änderungen im laufenden Container nur als Diagnosebeweis werten; dauerhafte Lösung in Dockerfile, Abhängigkeiten, Compose oder Quellcode verlangen.
6. Befunde nach Schwere ordnen: Blocker, funktionaler Fehler, Betriebs-/Sicherheitsrisiko, Wartbarkeit, Stil.
7. Für jeden Befund Beleg, Auswirkung und konkrete Korrektur nennen.

Wenn Tests wegen Umgebung oder fehlender Zugänge nicht ausführbar sind, dies als unbestätigten Nachweis ausweisen; nicht als Erfolg behandeln.

Ein Code Review kann eine Änderung `review-approved` machen, aber nicht eigenständig `merged`, `deployed`, `issue-closed` oder `requirement-verified`. Für die Delivery-/Closure-Phase an `engineering-delivery-followup` übergeben.

## 5. Schleife schließen

Nach Review und soweit erforderlich Delivery-Follow-up genau einen Iterationsstatus vergeben:

- **Abnahmefähig/geschlossen:** Definition of Done inklusive der vereinbarten Delivery-Gates erfüllt; nächstes Inkrement vorschlagen.
- **Korrekturschleife:** Begrenzte Restfehler oder Review-Findings; fokussierten Fix-Auftrag erzeugen.
- **Delivery offen:** Review abgeschlossen, aber CI/Merge/Deployment/Issue-/Requirement-Closure noch pending, stale oder unbestätigt; zuerst `engineering-delivery-followup` fortsetzen.
- **Neu schneiden:** Ansatz oder Scope ist fehlerhaft; Inkrement neu definieren.

Den Projektstand kompakt fortschreiben: bestätigter Stand, Delivery-/Verification-Status, offene Risiken, `doNotRepeat`, nächster Schritt und benötigte Nachweise. Keine abgeschlossene Arbeit erneut beauftragen.

Zusätzlich ein schlankes Entscheidungsprotokoll fortschreiben:

- **Entschieden:** Wahl und wichtigste Folge
- **Angenommen:** reversible Vorgabe, die bei neuen Fakten geändert werden darf
- **Offen:** nur Entscheidungen, die eine spätere Iteration tatsächlich blockieren

`engineering-iteration-state.json` enthält mindestens Repository/Head, letzte Issue-/Requirement-IDs, Review/Delivery State, Return-Input-Referenz sofern vorhanden, `doNotRepeat`, offene Gaps/Risks, `projectMemory`-Referenz und genau das nächste Inkrement beziehungsweise die früheste Closure-Aktion.

## Project-Memory-Contract

Die Engineering-Schleife ist kein einzelner undurchsichtiger Event. `project-second-brain` wird an **semantischen Phasengrenzen** fortgeschrieben:

- `stage: implementation` nach einem abgegrenzten Implementierungsstand oder verworfenen Implementierungsversuch mit neuer Evidenz,
- `stage: review` nach einer Review-Entscheidung für einen fixierten `reviewedHeadSha`,
- `stage: delivery` nach verifiziertem Merge, Deployment/Release oder Issue-/Requirement-Closure beziehungsweise wenn ein externer Zustand bewusst pending bleibt,
- `stage: implementation` oder `handoff` bei einer Korrekturschleife oder Übergabe an einen neuen Agenten.

Jeder Event verlinkt statt dupliziert die kanonischen Artefakte des jeweiligen Skills, insbesondere Issue/Requirement, Commit/PR, Test- und Review-Evidenz, Delivery-Status und relevante Decision Records.

Ein Low-Level-Kommando, ein unveränderter CI-Poll oder ein reiner Lesezugriff erzeugt keinen Event. Ein neuer überprüfbarer Projektzustand, eine neue Entscheidung, ein gescheiterter Ansatz mit relevantem `doNotRepeat` oder ein Routingwechsel dagegen schon.

Vor dem Start eines unabhängigen neuen Inkrements muss der vorherige wesentliche Zustand im Project Memory verankert sein. `state.json` wird mit `currentStage`, `latestEvent`, offenen Schleifen und genau der nächsten Aktion aktualisiert.

## Qualitätsprinzipien

- Evidence first: Logs, Tests, API-Antworten, Diffs und verifizierte Delivery-Zustände höher gewichten als Beschreibungen.
- Kleine, reversible Änderungen mit klarer Abnahmegrenze bevorzugen.
- Quellengebundene Systeme dürfen keine unbelegten Inhalte als Fakten speichern oder ausgeben.
- Generierte Inhalte und verifizierte Quellen getrennt halten; Audit Trail und Versionierung vorsehen, wenn Wissen weiterverwendet wird.
- Diagnose und dauerhafte Behebung ausdrücklich unterscheiden.
- Nutzeränderungen und fremde Worktree-Änderungen schützen.
- Nur den nächsten sinnvollen Schritt detaillieren; spätere Phasen als Orientierung knapp halten.
- Bei Rückfragen eine konkrete Empfehlung geben, statt lediglich Optionen aufzuzählen.
- Nicht um Bestätigung bereits belegter Fakten bitten.
- Weder PR-Closed noch Merge noch Tracker-Done allein als vollständige Engineering-Closure behandeln.
- Project Memory hält Rationale, Evidenz und Links fest, aber keine private Chain-of-Thought oder Secrets.

## Memory Path

Persistenzwürdig sind abstrahierte Iterations-, Priorisierungs-, Verification- und Delivery-Governance-Muster. Konkrete Repository-/PR-/Issue-Namen, SHAs, aktuelle CI-/Deployment-Zustände, unveröffentlichte Implementierungsdetails und offene Findings bleiben Run-/Project-State und werden bei aktivem Project Memory dort verlinkt dokumentiert. Übergib nur validierte `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; dieser Skill persistiert keine globalen Nutzererinnerungen selbst.

## Ausgabeformate

Bei **Analyse** liefern: Statusbild, Belege, Risiken, Delivery-Continuity-Status, empfohlenes Inkrement und Abnahmekriterien.

Bei **Entscheidungsklärung** liefern: genau eine Frage, die empfohlene Antwort mit Begründung und die wesentlichen Folgen der realistischen Alternativen. Danach auf die Nutzerentscheidung warten.

Bei **Copilot-Prompt** liefern: einen kopierbaren, in sich geschlossenen Prompt ohne zusätzliche Ausführungskommentare im Promptblock.

Bei **Review** liefern: Befunde zuerst, nach Schwere sortiert und mit Datei-/Stellenbezug; danach Testnachweise, Delivery-/Closure-Status, Restunsicherheiten und klare Entscheidung.
