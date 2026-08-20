---
name: round-based-requirements-grilling
description: Führt Requirements Engineering als datengetriebenen, rundenbasierten Grilling-Prozess durch. Die konkrete Grilling-Engine, Runtime, Authentifizierung, Statuslogik, Rundensemantik und Deploymentregeln werden ausschließlich aus dem aktuellen main-Stand von GithubLarsKomo/grilling bezogen. Bei Softwareprojekten ist KI-/ML-Readiness verpflichtender Bestandteil des Grillings.
version: 1.1.0
status: stable
owners:
  - GithubLarsKomo
requires: []
outputs:
  - GRILL-REPORT.md
  - approved SPEC.md
lastEvaluated: 2026-08-20
implicitInvocation: false
---

# Round-based Requirements Grilling

## Rolle dieses Skillz-Eintrags

Dieser Skill ist ausschließlich der **Capability-, Discovery-, Trigger- und Contract-Entry-Point** für Grilling innerhalb von `GithubLarsKomo/skillz`.

Er enthält bewusst **keine eigene Implementierung** der Grilling-Plattform und keine duplizierten Regeln zu Runtime, Authentifizierung, Deployment, globalem App-Status, Tokenmechanismen, Rundenspeicherung oder Produktübergabe.

## Autoritative Quelle

Vor jeder Ausführung dieses Skills müssen aus `GithubLarsKomo/grilling` auf dem aktuellen `main`-Stand mindestens gelesen werden:

1. `SKILL.md` – autoritative Prozess-, Runtime-, Auth-, Deployment-, Status- und Handoff-Semantik.
2. `site/catalog.json` – aktuelle, parallele, historische und freigegebene Grillings sowie aktive Runden.
3. Bei Fortsetzung eines bestehenden Grillings die darin referenzierten `site/rounds/*.json` und vorhandenen Reports/Handoff-Metadaten, soweit für die nächste Runde erforderlich.

Falls dieser Skillz-Eintrag und `GithubLarsKomo/grilling/SKILL.md` voneinander abweichen, **hat `GithubLarsKomo/grilling/SKILL.md` Vorrang**. Abweichungen sind als Synchronisationsfehler zu behandeln und dürfen nicht durch eine zweite Implementierungslogik kompensiert werden.

## Trigger

Diesen Skill verwenden, wenn Anforderungen iterativ geklärt, Zielkonflikte aufgelöst, offene Entscheidungen durch fokussierte Fragerunden reduziert oder aus mehreren Runden eine freigabefähige `SPEC.md` abgeleitet werden soll.

Bei Software-, WebApp-, API-, Datenplattform-, Automatisierungs- oder sonstigen digitalen Produktvorhaben gehört die in der autoritativen Grilling-Definition festgelegte **KI-/ML-Readiness** verpflichtend zum Requirements Engineering.

## Ausführungsvertrag

1. Aktuellen `main`-Stand von `GithubLarsKomo/grilling/SKILL.md` lesen.
2. Aktuellen `site/catalog.json` lesen und klären, ob ein bestehendes Grilling fortgesetzt oder ein neues angelegt wird.
3. Den dort festgelegten Grilling-Ablauf unverändert anwenden.
4. Neue oder geänderte Rundendefinitionen ausschließlich im `GithubLarsKomo/grilling`-Repository pflegen.
5. Finale Produkt-`SPEC.md` nicht im Grilling-Repository speichern; Produktübergabe gemäß autoritativer Grilling-Definition durchführen.
6. Keine Runtime-, Auth-, Deployment- oder Statusregeln aus diesem Repository erfinden oder kopieren.

## Outputs

- `GRILL-REPORT.md` gemäß autoritativer Grilling-Definition.
- Eine im Chat geprüfte und vom Nutzer freigegebene `SPEC.md`.
- Aktualisierte Grilling-/Rundenmetadaten ausschließlich in `GithubLarsKomo/grilling`, wenn der Prozess dies verlangt.

## Abschluss

Der Skillz-Eintrag ist erfüllt, wenn er zuverlässig in die aktuelle autoritative Grilling-Engine delegiert und der dort definierte Prozess ohne lokalen Parallelstrang ausgeführt wurde.
