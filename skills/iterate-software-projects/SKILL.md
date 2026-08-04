---
name: iterate-software-projects
description: Iterative Weiterentwicklung bestehender Softwareprojekte durch den wiederkehrenden Zyklus aus Bestandsanalyse, Klärung kritischer Produktentscheidungen, Auswahl des nächsten kleinen Inkrements, präzisem Copilot- oder Coding-Agent-Prompt und evidenzbasiertem Review. Verwenden, wenn ein Repository schrittweise fortgeführt, ein Plan vor der Umsetzung geschärft, ein nächster Implementierungsauftrag formuliert, ein Agentenergebnis geprüft, ein Docker-/KI-Service diagnostiziert oder nach einem Review die nächste Iteration geplant werden soll.
userFacing: true
category: engineering
version: 1.0.0
status: stable
owners:
  - GithubLarsKomo
requires: []
outputs:
  - review findings
  - next increment
  - verification evidence
lastEvaluated: 2026-07-31
---

# Softwareprojekte iterativ entwickeln

Arbeite als technischer Orchestrator. Halte Analyse, Implementierungsauftrag und Review als getrennte Phasen, aber führe ihre Erkenntnisse in einer fortlaufenden Projektschleife zusammen.

## Arbeitsmodus bestimmen

Ermittle zuerst, welche Phase der Nutzer verlangt:

- **Analyse:** Repository und Laufzeitstatus untersuchen und das nächste sinnvolle Inkrement empfehlen.
- **Copilot-Prompt:** Einen unmittelbar ausführbaren Auftrag für Copilot oder einen anderen Coding-Agenten erzeugen.
- **Review:** Umsetzung, Diff, Tests und Laufzeitnachweise gegen den Auftrag prüfen.
- **Weiterentwicklung:** Alle drei Phasen nacheinander durchführen, soweit Zugriff und Auftrag dies erlauben.

Bei Formulierungen wie „wie bisher“, „prüfe und mache weiter“ oder „nächster Prompt“ den letzten nachweisbaren Stand rekonstruieren. Keine vermeintliche Projektkontinuität erfinden.

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

1. Projektregeln und vorhandene Spezifikationen lesen.
2. Branch, Status, letzte relevante Commits und aktuelle Änderungen prüfen.
3. Architektur, Services, Schnittstellen, Datenhaltung und Deployment erfassen.
4. Offene TODOs, fehlgeschlagene Tests, Logs, Review-Kommentare und provisorische Fixes sammeln.
5. Behauptungen in drei Klassen trennen: durch Quelltext belegt, durch Laufzeittest belegt, noch unbestätigt.

Bei Docker-/KI-Projekten zuerst den realen Fehlerweg verfolgen: Servicezustand, Logs, Ports, Health-Endpunkt, interne und externe URLs, Abhängigkeiten und Netzwerkgrenzen. Lokale Proxy-Sonderfälle berücksichtigen; für lokale Tests bei Bedarf `--noproxy "*"` verwenden.

## 2. Nächstes Inkrement wählen

Das kleinste Inkrement wählen, das eigenständig Wert liefert und überprüfbar abgeschlossen werden kann. In dieser Reihenfolge priorisieren:

1. Regressionen und Restfehler der letzten Iteration
2. Reproduzierbarkeit eines bereits bewiesenen provisorischen Fixes
3. Fehlende Tests, Migrationen, Dokumentation oder Betriebsnachweise
4. Nächster fachlich kohärenter MVP-Baustein
5. Härtung, Automatisierung und Komfortfunktionen

Bestehende Architektur und Infrastruktur bevorzugen. Neue Komponenten nur einführen, wenn ihr Nutzen und ihre Integrationsgrenze klar sind. Größere Vorhaben phasenweise schneiden, beispielsweise isolierter MVP → Integration → Schnittstelle → Synchronisation → Härtung.

Vor Festlegung des Inkrements einen kurzen Entscheidungscheck durchführen:

1. Ist das Nutzerziel beobachtbar formuliert?
2. Sind In-Scope und Nicht-im-Scope widerspruchsfrei?
3. Sind irreversible Architektur-, Daten- oder Deployment-Entscheidungen geklärt?
4. Lassen sich Abnahmekriterien ausführen oder beobachten?

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

## 5. Schleife schließen

Nach dem Review genau einen Status vergeben:

- **Abnahmefähig:** Definition of Done erfüllt; nächstes Inkrement vorschlagen.
- **Korrekturschleife:** Begrenzte Restfehler; einen fokussierten Fix-Prompt erzeugen.
- **Neu schneiden:** Ansatz oder Scope ist fehlerhaft; Inkrement neu definieren.

Den Projektstand kompakt fortschreiben: bestätigter Stand, offene Risiken, nächster Schritt und benötigte Nachweise. Keine abgeschlossene Arbeit erneut beauftragen.

Zusätzlich ein schlankes Entscheidungsprotokoll fortschreiben:

- **Entschieden:** Wahl und wichtigste Folge
- **Angenommen:** reversible Vorgabe, die bei neuen Fakten geändert werden darf
- **Offen:** nur Entscheidungen, die eine spätere Iteration tatsächlich blockieren

## Qualitätsprinzipien

- Evidence first: Logs, Tests, API-Antworten und Diffs höher gewichten als Beschreibungen.
- Kleine, reversible Änderungen mit klarer Abnahmegrenze bevorzugen.
- Quellengebundene Systeme dürfen keine unbelegten Inhalte als Fakten speichern oder ausgeben.
- Generierte Inhalte und verifizierte Quellen getrennt halten; Audit Trail und Versionierung vorsehen, wenn Wissen weiterverwendet wird.
- Diagnose und dauerhafte Behebung ausdrücklich unterscheiden.
- Nutzeränderungen und fremde Worktree-Änderungen schützen.
- Nur den nächsten sinnvollen Schritt detaillieren; spätere Phasen als Orientierung knapp halten.
- Bei Rückfragen eine konkrete Empfehlung geben, statt lediglich Optionen aufzuzählen.
- Nicht um Bestätigung bereits belegter Fakten bitten.

## Ausgabeformate

Bei **Analyse** liefern: Statusbild, Belege, Risiken, empfohlenes Inkrement und Abnahmekriterien.

Bei **Entscheidungsklärung** liefern: genau eine Frage, die empfohlene Antwort mit Begründung und die wesentlichen Folgen der realistischen Alternativen. Danach auf die Nutzerentscheidung warten.

Bei **Copilot-Prompt** liefern: einen kopierbaren, in sich geschlossenen Prompt ohne zusätzliche Ausführungskommentare im Promptblock.

Bei **Review** liefern: Befunde zuerst, nach Schwere sortiert und mit Datei-/Stellenbezug; danach Testnachweise, Restunsicherheiten und klare Entscheidung.
