---
name: role-architecture
description: Überführt bestätigte Rollenanforderungen in ein normatives Rollenmodell mit Zweck, Outcomes, Verantwortungs- und Entscheidungsrechten, Scope, Schnittstellen, Erfolgskriterien und begründeten Capability-Anforderungen. Verwenden, wenn definiert werden soll, welche Rolle die Organisation tatsächlich braucht, bevor Ausschreibung oder Kandidatenbewertung beginnen.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.3.2
status: candidate
owners:
  - GithubLarsKomo
requires: []
consumes:
  - role-requirements-handoff.json
outputs:
  - role-architecture.json
  - role-architecture.md
  - role-scorecard.json
lastEvaluated: 2026-08-24
---

# Role Architecture

## Trigger

Verwenden, wenn aus bestätigten Rollenanforderungen oder äquivalenter bestätigter Evidenz ein **normatives Modell der Stelle** erzeugt werden soll. Die Role Architecture beantwortet: **Welche Rolle braucht die Organisation tatsächlich?**

Sie ist nicht die Stellenanzeige. Intern notwendige Präzision darf in späteren Kommunikationsfassungen abstrahiert werden, ohne die normative Bedeutung zu verändern.

## Voraussetzungen

Erforderlich ist entweder ein `role-requirements-handoff.json` oder äquivalente bestätigte Evidenz, die Zweck, Outcomes, Mandat, Scope, Capability-Anforderungen und offene Entscheidungen ausreichend trägt. `role-requirements-grilling` ist der bevorzugte Klärungspfad, aber keine technische Zwangsvoraussetzung; deshalb bleibt `requires: []` und der optionale Artefaktverbrauch wird separat über `consumes` modelliert.

Blockierende Widersprüche zu Mandat, Scope oder Entscheidungsrechten verhindern `status=approved`. Fehlt eine echte Stakeholder-Entscheidung, zurück zu `role-requirements-grilling`; fehlende bloße Dokumentform ist kein Grund für künstliches Re-Grilling.

Vorhandene HR-/Posting-/Template-Evidenz wird vor Modellierung klassifiziert:

- **rollenbestimmend und normativ**, wenn sie die tatsächliche Ausübung der Rolle verändert, etwa Reporting Line, funktionaler Scope, Standort-/Mobilitätsmodell, zwingende Sprache, Entscheidungsrechte oder reale Organisationsschnittstellen;
- **kommunikativ/administrativ**, wenn sie nur Darstellung oder HR-Abwicklung betrifft, etwa Package, Bonus, Job Family, Corporate-Layout, Branding oder Publikationssprache;
- **historisch**, wenn sie aus einer alten Stellenbeschreibung stammt und noch gegen die bestätigten Requirements geprüft werden muss.

## Ablauf

### Modell

Definiere mindestens:

1. Rollenbezeichnung als Arbeitslabel, **ohne den Inhalt aus dem Titel abzuleiten**.
2. `purpose`: warum die Rolle existiert.
3. `outcomes`: drei bis sieben **beobachtbare Ergebnisse** mit Zeithorizont.
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

### Organisationsfakten und Kommunikationsmetadaten

Bestätigte Organisationsfakten, die für die Wirksamkeit der Rolle kausal sind, gehören in die Role Architecture und dürfen später nicht zu unverbindlichen Copy-Optionen abgeschwächt werden. Dazu können gehören:

- Reporting- und Matrix-Linien,
- Standort, Hybrid-/Präsenzmodell und notwendige Mobilität,
- reale funktionale Einheiten und organisationseigene Funktionsbezeichnungen,
- interne/externe Kerninterfaces,
- operative Sprachfähigkeit, wenn sie für Führung, Behörden- oder Stakeholderarbeit tatsächlich erforderlich ist,
- geplantes Organisationsmodell oder Start-/Transformationskontext, soweit rollenrelevant.

Reine HR-/Kommunikationsmetadaten wie Vergütungsband, Bonus, Job Family, Corporate-Dokumentstil oder gewünschte Sprachfassung werden **nicht künstlich in `capabilities`, `scope` oder Scorecard kodiert**. Sie können als separate Authoring-Evidenz weitergegeben werden.

Wenn ein vorhandenes Organigramm oder Posting organisationseigene Bezeichnungen enthält, sollen bestätigte Bezeichnungen in `scope` und `interfaces` möglichst erhalten bleiben. Historische Inhalte mit abweichender Rollenlogik werden nicht übernommen, nur weil ihr Wording corporate-konform ist.

### Normativer Artefaktvertrag

`role-architecture.json` folgt `schemas/role-architecture-v1.schema.json` und enthält mindestens:

- `schemaVersion: 1`,
- `roleArchitectureId`,
- `version`,
- `status: draft | review | approved | superseded`,
- `sourceHandoffId` und `sourceHandoffVersion`, falls ein Requirements-Handoff verwendet wurde,
- `purpose`, `outcomes`, `accountabilities`, `decisionRights`, `scope`, `interfaces`, `context`,
- `capabilities`, `experienceEvidence`, `successMeasures`, `nonGoals`, `risksAndTensions`,
- `approvedAt` und `approvalAuthority`, wenn `status=approved`.

Nur `status=approved` ist eine normative Freigabe für `job-description-authoring` und `candidate-role-fit-assessment`.

### Capability-Logik

Trenne strikt:

- **Capability**: tatsächlich benötigte Fähigkeit,
- **Evidence proxy**: mögliche Erfahrung, die diese Fähigkeit belegt,
- **Credential**: formaler Nachweis, nur wenn fachlich oder rechtlich erforderlich.

Ein früherer Titel, eine bestimmte Unternehmensgröße, Branche oder Ausbildung darf **nicht automatisch als Must-have** gelten. Harte Kriterien benötigen eine nachvollziehbare Verbindung zu Outcome, Risiko oder zwingender Rahmenbedingung.

Ebenso darf eine harte, bestätigte Anforderung nicht für kommunikative Attraktivität in eine weichere Präferenz umgedeutet werden. Die spätere öffentliche Ausschreibung darf kürzer sein, aber nicht der normativen Role Architecture widersprechen.

### Role Scorecard

`role-scorecard.json` folgt `schemas/role-scorecard-v1.schema.json`, gehört immer zu genau einer Role-Architecture-Version und enthält mindestens:

- `schemaVersion: 1`,
- `roleArchitectureId`,
- `roleArchitectureVersion`,
- `scoringModelVersion`,
- `status: draft | approved | superseded`,
- `approvedBeforeCandidateReview`,
- gewichtete, rollenbezogene Dimensionen mit stabiler ID, Definition, Gewicht, beobachtbarer Evidenz, Mindestniveau und optionalem Knockout,
- Rationale für jedes `knockout: true`.

### Versionierung und Invalidierung

Ändert sich Rollenauftrag, Capability-Logik, Knockout, Gewicht oder ein anderer normativer Bestandteil, entsteht eine neue Role-Architecture-/Scorecard-Version. Die vorherige Version wird `superseded`.

Alle Job Descriptions, Search Briefs, öffentlichen Ausschreibungen und Candidate-Fit-Assessments, die auf einer superseded Version beruhen, **gelten ab diesem Zeitpunkt als `stale`**. Sie bleiben auditierbar, dürfen aber nicht als aktueller Rollen- oder Auswahlstand verwendet werden und müssen gegen die neue freigegebene Version neu erzeugt bzw. neu bewertet werden.

Reine Änderungen an Corporate-Layout, Dokumentstruktur, Package/Bonus/Job Family oder Übersetzung erzeugen **keine neue Role-Architecture-Version**, solange die normative Bedeutung unverändert bleibt.

Kandidatenevidenz darf niemals als Begründung dienen, Role Architecture oder Scorecard so zu verändern, dass ein bestimmter Kandidat besser passt. Eine echte Rollenänderung braucht rollenbezogene Stakeholder-/Organisationsgründe unabhängig vom betrachteten Kandidaten.

## Prüfungen

Vor einer Freigabe prüfen:

- `role-architecture.json` und `role-scorecard.json` validieren gegen ihre v1-Schemas.
- Summe der aktiven Gewichte = `1.0`.
- Dimension-IDs sind eindeutig.
- Jede Dimension verweist auf Capability, Outcome oder zwingende Rollenanforderung.
- Jedes `knockout: true` besitzt eine dokumentierte zwingende Rationale.
- Gewichte, Mindestniveaus und Knockouts wurden **vor Sichtung eines konkreten Kandidaten** freigegeben.
- `roleArchitectureId` und `roleArchitectureVersion` stimmen zwischen Architektur und Scorecard exakt überein.
- Gewichte und Knockouts kodieren keine sachfremden oder geschützten Merkmale.
- Ausgangsevidenz und ggf. `sourceHandoffId`/`sourceHandoffVersion` sind rückverfolgbar.
- Rollenbestimmende Reporting-, Scope-, Standort-/Mobilitäts-, Sprach- und Schnittstellenfakten sind nicht versehentlich als bloße Kommunikationsmetadaten ausgelagert.
- Reine HR-/Darstellungsmetadaten wurden nicht zu normativen Auswahlkriterien hochgestuft.
- Keine harte Anforderung ist nur deshalb abgeschwächt, weil eine historische oder öffentliche Formulierung weicher klingt.

## Fehlerbehandlung

Bei blockierenden fachlichen Entscheidungen zurück zu `role-requirements-grilling`. Bei widersprüchlicher oder unvollständiger Evidenz keinen normativen Zustand vortäuschen; die betroffenen Teile bleiben `draft` oder `review`.

Widerspricht ein Corporate-Template oder eine bestehende Ausschreibung der bestätigten Role Architecture, wird **nicht gemittelt**. Die Role Architecture bleibt normativ; `job-description-authoring` muss die Kommunikationsfassung korrigieren oder die Differenz als nicht zulässigen Konflikt melden.

Wenn eine spätere Job Description oder Kandidatenbewertung einen echten Rollenfehler sichtbar macht, zuerst die Role Architecture unabhängig vom konkreten Kandidaten korrigieren und neu freigeben. Downstream-Artefakte werden danach invalidiert und neu erzeugt.

## Übergabe

Nach ausdrücklicher Freigabe kann dieselbe Role Architecture parallel an zwei Verbraucher gehen:

- `job-description-authoring` für interne/externe Kommunikationsfassungen,
- `candidate-role-fit-assessment` für evidenzbasierte Kandidatenbewertung.

An `job-description-authoring` darf zusätzlich separat bestätigter Kommunikationskontext übergeben werden, etwa Corporate-Template, Organigramm, Package/Job Family, Branding, Dokumentstruktur oder gewünschte Sprachfassungen. Diese ergänzende Evidenz besitzt **keinen Vorrang** vor Role Architecture und Scorecard.

Eine `draft`-, `review`- oder `superseded`-Architektur darf nicht als aktuelle normative Basis übergeben werden.

## Abschlusskriterien

Abgeschlossen ist die Role Architecture, wenn Auftrag, Outcomes, Mandat, Scope, Capability-Modell und **Role Scorecard** konsistent, schema-validiert, versioniert, rückverfolgbar und als normative Basis für Kommunikation und Auswahl ausdrücklich freigegeben sind und die Grenze zwischen normativen Rollenfakten und nicht-normativen HR-/Kommunikationsmetadaten eindeutig ist.