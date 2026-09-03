---
name: round-based-requirements-grilling
description: Führt Requirements Engineering als datengetriebenen, rundenbasierten Grilling-Prozess durch. Die konkrete Grilling-Engine, v1-/v2-Runtime, Authentifizierung, Statuslogik, Rundensemantik und Deploymentregeln werden ausschließlich aus dem aktuellen main-Stand von GithubLarsKomo/grilling bezogen. Grilling klärt fachliche Entscheidungen; die normative SPEC.md wird anschließend durch conversation-to-spec erzeugt.
---

# Round-based Requirements Grilling

## Rolle dieses Skillz-Eintrags

Dieser Skill ist ausschließlich der **Capability-, Discovery-, Trigger- und Contract-Entry-Point** für Grilling innerhalb von `GithubLarsKomo/skillz`.

Er enthält bewusst keine eigene Implementierung der Grilling-Plattform und keine duplizierten Regeln zu Runtime, Authentifizierung, Deployment, globalem App-Status, Rundenspeicherung, progressiver Sessionlogik oder Produktübergabe.

## Autoritative Quelle

Vor jeder Ausführung dieses Skills muss aus `GithubLarsKomo/grilling` auf dem aktuellen `main`-Stand mindestens `SKILL.md` gelesen werden. Danach ist die verwendete Runtime zu bestimmen:

- **v1 / legacy:** `site/catalog.json`, referenzierte `site/rounds/*.json` und vorhandene Reports/Handoff-Metadaten lesen.
- **v2 / DB-backed:** `docs/RUNTIME-SOURCE-OF-TRUTH.md`, `docs/API-v2.md`, `schemas/grilling-definition-v2.schema.json` und bei Bedarf die aktuelle v2-Runtime unter `src/v2/` berücksichtigen. Definitionen und Sessions werden in der v2-Datenbank geführt; `site/catalog.json` ist kein v2-Session-Register.
- **progressive v2 session:** den aktuellen Session-State und letzten `grilling-round-handoff` verwenden. Bereits beantwortete Fragen nicht wiederholen und den `nextRoundContract` respektieren.

Falls dieser Skillz-Eintrag und `GithubLarsKomo/grilling/SKILL.md` voneinander abweichen, hat `GithubLarsKomo/grilling/SKILL.md` Vorrang. Abweichungen sind Synchronisationsfehler und dürfen nicht durch eine zweite Implementierungslogik kompensiert werden.

## Trigger

Diesen Skill verwenden, wenn Anforderungen iterativ geklärt, Zielkonflikte aufgelöst, offene Präferenz-, Scope-, Rollen-, Prozess- oder Produktentscheidungen durch fokussierte Fragerunden reduziert oder bestätigte Requirements für eine spätere Spezifikation vorbereitet werden sollen.

Bei Software-, WebApp-, API-, Datenplattform-, Automatisierungs- oder sonstigen digitalen Produktvorhaben gehört die in der autoritativen Grilling-Definition festgelegte KI-/ML-Readiness verpflichtend zum Requirements Engineering.

## Routing und Abgrenzung

Grilling reduziert **fachliche Entscheidungsunsicherheit**. Seine Kernfrage lautet: **Was wollen oder entscheiden Nutzer und Stakeholder?**

- Fehlende fachliche Präferenz-, Scope-, Rollen-, Prozess- oder Produktentscheidung → Grilling.
- Fehlende technische Evidenz, unbekannte Abhängigkeit, Migrations- oder Architekturtragfähigkeit → `large-work-wayfinder`.
- Fachliche Entscheidungen ausreichend geklärt und technische Evidenz ausreichend → `conversation-to-spec`.
- Wayfinder entdeckt eine neue fachliche Entscheidung → zurück zum betreffenden Grilling.
- `spec-to-vertical-issues` ist kein direkter Grilling-Nachfolger; eine freigegebene normative SPEC aus `conversation-to-spec` ist zwingende Zwischenstufe.

Grilling erzeugt nicht selbst die normative Produkt-`SPEC.md`.

## Ausführungsvertrag

1. Aktuellen `main`-Stand von `GithubLarsKomo/grilling/SKILL.md` lesen.
2. Runtime v1 oder v2 bestimmen; niemals v1-Katalogsemantik auf eine v2-Session übertragen.
3. Bei v1 die dort festgelegten Katalog-/Rundenregeln anwenden.
4. Bei v2 Definition, Session und progressive Round-/Handoff-Semantik der aktuellen Runtime verwenden.
5. Neue oder geänderte portable Grilling-Definitionen ausschließlich im `GithubLarsKomo/grilling`-Kontext pflegen bzw. über dessen v2-Importweg verwenden.
6. Bei technischer statt fachlicher Unsicherheit an Wayfinder routen.
7. Nach ausreichender fachlicher Klärung bestätigte Requirements und Reports an `conversation-to-spec` übergeben.
8. Finale Produkt-`SPEC.md` nicht im Grilling-Repository speichern oder innerhalb dieses Capability-Eintrags selbst erzeugen.
9. Keine Runtime-, Auth-, Deployment-, DB- oder Statusregeln aus diesem Repository erfinden oder kopieren.

## Progressive v2

Progressive v2-Grillings dürfen mit einer kleinen initialen Definition starten. Nach Abschluss einer Runde entsteht ein `grilling-round-handoff` mit Ziel, Antworten, vorherigen Runden und `nextRoundContract`. Eine weitere Runde wird nur erzeugt, wenn relevante fachliche Unsicherheit verbleibt.

Question IDs sind sessionweit eindeutig. Bereits gelöste Fragen werden nicht erneut gestellt. Nach Reopen/Truncation dürfen downstream erzeugte Runden und Handoffs nicht weiter als gültiger aktueller Stand behandelt werden.

## Outputs

- `GRILL-REPORT.md` bzw. äquivalente lesbare Konsolidierung gemäß autoritativer Grilling-Definition.
- `requirements-handoff.json` mit bestätigten Entscheidungen, offenen Punkten, Quellen, Nicht-Zielen, Risiken und Routinghinweisen, wenn der Workflow in Richtung Produktspezifikation geht.
- v2 Round-Handoffs bleiben Runtime-Artefakte des Grilling-Systems und sind nicht mit dem finalen Requirements-Handoff gleichzusetzen.

## Project-Memory-Hook

Ein abgeschlossenes **projektbezogenes** Grilling kann Startpunkt der persistenten Projektdokumentation über `project-second-brain` sein. Das gilt nur, wenn ein Projekt-Repository bzw. geeigneter persistenter Projektkontext existiert und die Daten dafür geeignet sind.

Vertrauliche Coaching-, HR-, Health-, Investigation- oder vergleichbar sensible Grillings werden **nicht automatisch** in Project Second Brain persistiert. Dafür ist eine ausdrückliche, geeignete Persistenzentscheidung erforderlich.

Bei normalem projektbezogenem Handoff:

1. `project-second-brain` aufrufen.
2. bestehenden Project-Memory-Root wiederverwenden oder `docs/project-memory/` initialisieren.
3. Grilling-Event mit bestätigten Zielen, Nicht-Zielen, Entscheidungen, offenen Punkten und Routingziel verlinken.
4. den resultierenden `projectMemory`-Verweis im nachgelagerten Handoff mitführen.

## Abschluss

Der Skillz-Eintrag ist erfüllt, wenn er zuverlässig in die aktuelle autoritative Grilling-Engine delegiert, v1 und v2 korrekt unterscheidet, fachliche von technischer Unsicherheit trennt und den passenden Handoff erzeugt, ohne einen lokalen Parallelstrang oder eine zweite Runtime-/SPEC-Semantik einzuführen.
