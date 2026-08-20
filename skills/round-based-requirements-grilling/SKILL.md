---
name: round-based-requirements-grilling
description: Führt Requirements Engineering als datengetriebenen, rundenbasierten Grilling-Prozess durch. Die konkrete Grilling-Engine, Runtime, Authentifizierung, Statuslogik, Rundensemantik und Deploymentregeln werden ausschließlich aus dem aktuellen main-Stand von GithubLarsKomo/grilling bezogen. Grilling klärt fachliche Entscheidungen; die normative SPEC.md wird anschließend durch conversation-to-spec erzeugt.
version: 1.2.0
status: stable
owners:
  - GithubLarsKomo
requires: []
outputs:
  - GRILL-REPORT.md
  - requirements-handoff.json
lastEvaluated: 2026-08-20
implicitInvocation: false
---

# Round-based Requirements Grilling

## Rolle dieses Skillz-Eintrags

Dieser Skill ist ausschließlich der **Capability-, Discovery-, Trigger- und Contract-Entry-Point** für Grilling innerhalb von `GithubLarsKomo/skillz`.

Er enthält bewusst **keine eigene Implementierung** der Grilling-Plattform und keine duplizierten Regeln zu Runtime, Authentifizierung, Deployment, globalem App-Status, Tokenmechanismen, Rundenspeicherung oder Produktübergabe.

## Autoritative Quelle

Vor jeder Ausführung dieses Skills müssen aus `GithubLarsKomo/grilling` auf dem aktuellen `main`-Stand mindestens gelesen werden:

1. `SKILL.md` – autoritative Prozess-, Runtime-, Auth-, Deployment-, Status-, Routing- und Handoff-Semantik.
2. `site/catalog.json` – aktuelle, parallele, historische und freigegebene Grillings sowie aktive Runden.
3. Bei Fortsetzung eines bestehenden Grillings die darin referenzierten `site/rounds/*.json` und vorhandenen Reports/Handoff-Metadaten, soweit für die nächste Runde erforderlich.

Falls dieser Skillz-Eintrag und `GithubLarsKomo/grilling/SKILL.md` voneinander abweichen, **hat `GithubLarsKomo/grilling/SKILL.md` Vorrang**. Abweichungen sind als Synchronisationsfehler zu behandeln und dürfen nicht durch eine zweite Implementierungslogik kompensiert werden.

## Trigger

Diesen Skill verwenden, wenn Anforderungen iterativ geklärt, Zielkonflikte aufgelöst, offene Präferenz-, Scope- oder Produktentscheidungen durch fokussierte Fragerunden reduziert oder bestätigte Requirements für eine spätere Spezifikation vorbereitet werden sollen.

Bei Software-, WebApp-, API-, Datenplattform-, Automatisierungs- oder sonstigen digitalen Produktvorhaben gehört die in der autoritativen Grilling-Definition festgelegte **KI-/ML-Readiness** verpflichtend zum Requirements Engineering.

## Routing und Abgrenzung

Grilling reduziert **fachliche Entscheidungsunsicherheit**. Seine Kernfrage lautet: **Was wollen oder entscheiden Nutzer und Stakeholder?**

Grilling ist nicht für technische Exploration zuständig und erzeugt nicht selbst die normative Produkt-`SPEC.md`.

- Fehlende fachliche Präferenz-, Scope- oder Produktentscheidung → Grilling.
- Fehlende technische Evidenz, unbekannte Abhängigkeit, Migrations- oder Architekturtragfähigkeit → `large-work-wayfinder`.
- Fachliche Entscheidungen ausreichend geklärt und technische Evidenz ausreichend → `conversation-to-spec`.
- Wayfinder entdeckt eine neue fachliche Produktentscheidung → zurück zu Grilling.
- `spec-to-vertical-issues` ist kein direkter Grilling-Nachfolger; eine freigegebene normative SPEC aus `conversation-to-spec` ist zwingende Zwischenstufe.

Der Abschluss eines Grillings erzeugt deshalb einen bestätigten `requirements-handoff.json` zusätzlich zu den Reports. `conversation-to-spec` besitzt anschließend die Verantwortung, daraus gemeinsam mit Repository- und Wayfinder-Evidenz eine normative, prüfbare `SPEC.md` zu erzeugen.

## Ausführungsvertrag

1. Aktuellen `main`-Stand von `GithubLarsKomo/grilling/SKILL.md` lesen.
2. Aktuellen `site/catalog.json` lesen und klären, ob ein bestehendes Grilling fortgesetzt oder ein neues angelegt wird.
3. Den dort festgelegten Grilling-Ablauf unverändert anwenden.
4. Neue oder geänderte Rundendefinitionen ausschließlich im `GithubLarsKomo/grilling`-Repository pflegen.
5. Bei technischer statt fachlicher Unsicherheit an Wayfinder routen, statt technische Entscheidungen im Grilling zu erfinden.
6. Nach ausreichender fachlicher Klärung `GRILL-REPORT.md` und `requirements-handoff.json` an `conversation-to-spec` übergeben.
7. Finale Produkt-`SPEC.md` nicht im Grilling-Repository speichern oder innerhalb dieses Capability-Eintrags selbst erzeugen.
8. Keine Runtime-, Auth-, Deployment- oder Statusregeln aus diesem Repository erfinden oder kopieren.

## Outputs

- `GRILL-REPORT.md` gemäß autoritativer Grilling-Definition.
- `requirements-handoff.json` mit bestätigten Entscheidungen, offenen Punkten, Quellen, Nicht-Zielen, Risiken und Routinghinweisen.
- Aktualisierte Grilling-/Rundenmetadaten ausschließlich in `GithubLarsKomo/grilling`, wenn der Prozess dies verlangt.

## Abschluss

Der Skillz-Eintrag ist erfüllt, wenn er zuverlässig in die aktuelle autoritative Grilling-Engine delegiert, fachliche von technischer Unsicherheit korrekt trennt und einen bestätigten Requirements-Handoff an `conversation-to-spec` erzeugt, ohne einen lokalen Parallelstrang oder eine zweite SPEC-Erzeugung einzuführen.
