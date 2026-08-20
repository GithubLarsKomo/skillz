---
name: role-architecture
description: Überführt bestätigte Rollenanforderungen in ein normatives Rollenmodell mit Zweck, Outcomes, Verantwortungs- und Entscheidungsrechten, Scope, Schnittstellen, Erfolgskriterien und begründeten Capability-Anforderungen. Verwenden, wenn definiert werden soll, welche Rolle die Organisation tatsächlich braucht, bevor Ausschreibung oder Kandidatenbewertung beginnen.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - role-requirements-grilling
outputs:
  - role-architecture.json
  - role-architecture.md
  - role-scorecard.json
lastEvaluated: 2026-08-20
---

# Role Architecture

## Zweck

`role-architecture` ist das **normative Modell der Stelle**. Es beantwortet: **Welche Rolle braucht die Organisation tatsächlich?**

Die Role Architecture ist nicht die Stellenanzeige. Sie darf deshalb Anforderungen enthalten, die intern präzise sein müssen, aber in einer öffentlichen Ausschreibung anders formuliert oder aus Vertraulichkeitsgründen abstrahiert werden.

## Eintritt

Erforderlich ist ein ausreichend geklärter `role-requirements-handoff.json` oder äquivalente bestätigte Evidenz. Blockierende Widersprüche zu Mandat, Scope oder Entscheidungsrechten verhindern die Freigabe der betroffenen Teile.

## Modell

Definiere mindestens:

1. Rollenbezeichnung als Arbeitslabel, ohne den Inhalt aus dem Titel abzuleiten.
2. `purpose`: warum die Rolle existiert.
3. `outcomes`: drei bis sieben beobachtbare Ergebnisse mit Zeithorizont.
4. `accountabilities`: dauerhafte Ergebnisverantwortungen.
5. `decisionRights`: selbständig, gemeinsam, empfehlend oder eskalierend.
6. `scope`: Team, Budget, Produkte, Regionen, Systeme oder Prozesse.
7. `interfaces`: zentrale interne und externe Abhängigkeiten.
8. `context`: Build, Scale, Transformation, Turnaround, Integration oder Betrieb.
9. `capabilities`: kausal notwendige Fähigkeiten, getrennt nach Must-have und entwickelbar.
10. `experienceEvidence`: welche Erfahrung eine Capability belegen kann, ohne einen einzigen Karrierepfad vorzuschreiben.
11. `successMeasures`: beobachtbare Scorecard statt Aktivitätsliste.
12. `nonGoals`: was ausdrücklich nicht zur Rolle gehört.
13. `risksAndTensions`: strukturelle Zielkonflikte und Fehlbesetzungsrisiken.

## Capability-Logik

Trenne strikt:

- **Capability**: tatsächlich benötigte Fähigkeit,
- **Evidence proxy**: mögliche Erfahrung, die diese Fähigkeit belegt,
- **Credential**: formaler Nachweis, nur wenn fachlich oder rechtlich erforderlich.

Ein früherer Titel, eine bestimmte Unternehmensgröße, Branche oder Ausbildung darf nicht automatisch als Must-have gelten. Harte Kriterien benötigen eine nachvollziehbare Verbindung zu Outcome, Risiko oder zwingender Rahmenbedingung.

## Role Scorecard

`role-scorecard.json` enthält gewichtete, rollenbezogene Dimensionen. Jede Dimension braucht:

- stabile ID,
- Definition,
- Gewicht,
- beobachtbare Evidenz,
- Mindestniveau, falls wirklich erforderlich,
- `knockout: true` nur bei begründeter zwingender Voraussetzung.

Gewichte und Knockouts dürfen keine sachfremden oder geschützten Merkmale kodieren.

## Übergaben

Nach Freigabe kann dieselbe Role Architecture parallel an zwei Verbraucher gehen:

- `job-description-authoring` für interne/externe Kommunikationsfassungen,
- `candidate-role-fit-assessment` für eine evidenzbasierte Kandidatenbewertung.

Ändert sich später der Rollenauftrag, wird zuerst die Role Architecture versioniert; Job Description und Kandidatenbewertung werden danach gegen die neue Version aktualisiert.

## Abschluss

Abgeschlossen ist die Role Architecture, wenn Auftrag, Outcome, Mandat, Scope, Capability-Modell und Scorecard konsistent, rückverfolgbar und als normative Basis für Kommunikation und Auswahl freigegeben sind.
