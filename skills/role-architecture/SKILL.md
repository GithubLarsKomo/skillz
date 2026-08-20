---
name: role-architecture
description: Überführt bestätigte Rollenanforderungen in ein normatives Rollenmodell mit Zweck, Outcomes, Verantwortungs- und Entscheidungsrechten, Scope, Schnittstellen, Erfolgskriterien und begründeten Capability-Anforderungen. Verwenden, wenn definiert werden soll, welche Rolle die Organisation tatsächlich braucht, bevor Ausschreibung oder Kandidatenbewertung beginnen.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
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

Erforderlich ist entweder ein `role-requirements-handoff.json` oder äquivalente bestätigte Evidenz, die Zweck, Outcomes, Mandat, Scope, Capability-Anforderungen und offene Entscheidungen ausreichend trägt. `role-requirements-grilling` ist der bevorzugte Klärungspfad, aber keine technische Zwangsvoraussetzung.

Blockierende Widersprüche zu Mandat, Scope oder Entscheidungsrechten verhindern `status=approved` der betroffenen Role Architecture. Fehlt eine echte Stakeholder-Entscheidung, zurück zu `role-requirements-grilling`; fehlende bloße Dokumentform ist dagegen kein Grund für künstliches Re-Grilling.

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

## Normativer Artefaktvertrag

`role-architecture.json` enthält mindestens:

- `roleArchitectureId`,
- `version`,
- `status: draft | review | approved | superseded`,
- `sourceHandoffId` und `sourceHandoffVersion`, falls ein Requirements-Handoff verwendet wurde,
- `purpose`, `outcomes`, `accountabilities`, `decisionRights`, `scope`, `interfaces`, `context`,
- `capabilities`, `experienceEvidence`, `successMeasures`, `nonGoals`, `risksAndTensions`,
- `approvedAt` und `approvalAuthority`, wenn `status=approved`.

Nur `status=approved` ist eine normative Freigabe für `job-description-authoring` und `candidate-role-fit-assessment`.

## Capability-Logik

Trenne strikt:

- **Capability**: tatsächlich benötigte Fähigkeit,
- **Evidence proxy**: mögliche Erfahrung, die diese Fähigkeit belegt,
- **Credential**: formaler Nachweis, nur wenn fachlich oder rechtlich erforderlich.

Ein früherer Titel, eine bestimmte Unternehmensgröße, Branche oder Ausbildung darf nicht automatisch als Must-have gelten. Harte Kriterien benötigen eine nachvollziehbare Verbindung zu Outcome, Risiko oder zwingender Rahmenbedingung.

## Role Scorecard

`role-scorecard.json` gehört immer zu genau einer Role-Architecture-Version und enthält mindestens:

- `roleArchitectureId`,
- `roleArchitectureVersion`,
- `scoringModelVersion`,
- `status: draft | approved | superseded`,
- gewichtete, rollenbezogene Dimensionen mit stabiler ID, Definition, Gewicht, beobachtbarer Evidenz, Mindestniveau und optionalem Knockout,
- Rationale für jedes `knockout: true`.

Invarianten:

- Summe der aktiven Gewichte = `1.0`.
- Dimension-IDs sind eindeutig.
- Jede Dimension verweist nachvollziehbar auf Capability, Outcome oder zwingende Rollenanforderung.
- Knockouts benötigen eine begründete zwingende Voraussetzung.
- Gewichte und Knockouts werden **vor Sichtung eines konkreten Kandidaten** freigegeben und dürfen nicht kandidatenbezogen nachjustiert werden.
- `roleArchitectureId` und `roleArchitectureVersion` müssen zwischen Architektur und Scorecard exakt übereinstimmen.

Gewichte und Knockouts dürfen keine sachfremden oder geschützten Merkmale kodieren.

## Übergaben

Nach Freigabe kann dieselbe Role Architecture parallel an zwei Verbraucher gehen:

- `job-description-authoring` für interne/externe Kommunikationsfassungen,
- `candidate-role-fit-assessment` für eine evidenzbasierte Kandidatenbewertung.

Eine `draft`- oder `review`-Architektur darf nicht als freigegebene normative Basis an diese Verbraucher übergeben werden.

## Versionierung und Invalidierung

Ändert sich der Rollenauftrag, die Capability-Logik, ein Knockout, ein Gewicht oder ein anderer normativer Bestandteil, entsteht eine neue Role-Architecture-/Scorecard-Version. Die vorherige Version wird `superseded`.

Alle Job Descriptions, Search Briefs, öffentlichen Ausschreibungen und Candidate-Fit-Assessments, die auf einer superseded Version beruhen, gelten ab diesem Zeitpunkt als `stale`. Sie bleiben auditierbar, dürfen aber nicht als aktueller Rollen- oder Auswahlstand verwendet werden und müssen gegen die neue freigegebene Version neu erzeugt bzw. neu bewertet werden.

Kandidatenevidenz darf niemals als Begründung dienen, die Role Architecture oder Scorecard so zu verändern, dass ein bestimmter Kandidat besser passt. Eine echte Rollenänderung braucht rollenbezogene Stakeholder-/Organisationsgründe unabhängig vom betrachteten Kandidaten.

## Abschluss

Abgeschlossen ist die Role Architecture, wenn Auftrag, Outcome, Mandat, Scope, Capability-Modell und Scorecard konsistent, versioniert, rückverfolgbar und als normative Basis für Kommunikation und Auswahl ausdrücklich freigegeben sind.
