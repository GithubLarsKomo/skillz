---
name: role-architecture
description: Überführt bestätigte Rollenanforderungen in ein normatives Rollenmodell mit Zweck, Outcomes, Verantwortungs- und Entscheidungsrechten, Scope, Schnittstellen, Erfolgskriterien und begründeten Capability-Anforderungen. Verwenden, wenn definiert werden soll, welche Rolle die Organisation tatsächlich braucht, bevor Ausschreibung oder Kandidatenbewertung beginnen.
---

# Role Architecture

## Trigger

Verwenden, wenn aus bestätigten Rollenanforderungen oder äquivalenter bestätigter Evidenz ein **normatives Modell der Stelle** erzeugt werden soll. Die Role Architecture beantwortet: **Welche Rolle braucht die Organisation tatsächlich?**

Sie ist nicht die Stellenanzeige. Intern notwendige Präzision darf in späteren Kommunikationsfassungen abstrahiert werden, ohne die normative Bedeutung zu verändern.

## Voraussetzungen

Erforderlich ist ein `role-requirements-handoff.json` oder äquivalente bestätigte Evidenz mit Zweck, Outcomes, Mandat, Scope, Capability-Anforderungen und offenen Entscheidungen. Blockierende Widersprüche verhindern `status=approved`.

Vorhandene HR-/Posting-/Template-Evidenz wird klassifiziert als:

- **rollenbestimmend und normativ**, wenn sie die tatsächliche Ausübung verändert, etwa Reporting Line, funktionaler Scope, Standort-/Mobilitätsmodell, zwingende Sprache, Entscheidungsrechte oder reale Organisationsschnittstellen;
- **kommunikativ/administrativ**, wenn sie nur Darstellung oder HR-Abwicklung betrifft, etwa Package, Bonus, Job Family, Corporate-Layout, Branding oder Publikationssprache;
- **historisch**, wenn sie aus einer alten Stellenbeschreibung stammt und noch gegen die bestätigten Requirements geprüft werden muss.

## Ablauf

### Modell

Definiere mindestens Rollenlabel, `purpose`, beobachtbare `outcomes`, `accountabilities`, `decisionRights`, `scope`, `interfaces`, `context`, kausal notwendige `capabilities`, `experienceEvidence`, `successMeasures`, `nonGoals` und `risksAndTensions`.

### Organisationsfakten und Kommunikationsmetadaten

Bestätigte Organisationsfakten, die für die Wirksamkeit der Rolle kausal sind, gehören in die Role Architecture und dürfen später nicht zu unverbindlichen Copy-Optionen abgeschwächt werden. Dazu können Reporting-/Matrix-Linien, Standort/Hybrid/Mobilität, reale funktionale Einheiten, Kerninterfaces, operative Sprachfähigkeit oder ein rollenrelevantes geplantes Organisationsmodell gehören.

Reine HR-/Kommunikationsmetadaten wie Vergütungsband, Bonus, Job Family, Corporate-Dokumentstil oder gewünschte Sprachfassung werden **nicht künstlich in Capabilities, Scope oder Scorecard kodiert**. Sie können als separate Authoring-Evidenz weitergegeben werden.

Wenn ein Organigramm oder Posting organisationseigene Bezeichnungen enthält, sollen bestätigte Bezeichnungen in Scope und Interfaces möglichst erhalten bleiben. Historische Inhalte mit abweichender Rollenlogik werden nicht übernommen, nur weil ihr Wording corporate-konform ist.

### Capability-Logik

Trenne Capability, Evidence Proxy und Credential strikt. Titel, Unternehmensgröße, Branche oder Ausbildung sind nicht automatisch Must-haves. Harte Kriterien benötigen eine Verbindung zu Outcome, Risiko oder zwingender Rahmenbedingung.

Eine harte, bestätigte Anforderung darf nicht für kommunikative Attraktivität in eine weichere Präferenz umgedeutet werden. Die spätere öffentliche Ausschreibung darf kürzer sein, aber nicht der normativen Role Architecture widersprechen.

### Role Scorecard

Die Scorecard gehört genau zu einer Role-Architecture-Version, hat gewichtete Dimensionen, beobachtbare Evidenz, Mindestniveaus und begründete Knockouts. Gewichte und Knockouts werden vor Kandidatenreview freigegeben.

### Versionierung

Normative Änderungen erzeugen eine neue Architecture-/Scorecard-Version und machen abgeleitete Kommunikations- und Assessment-Artefakte stale. Reine Änderungen an Corporate-Layout, Dokumentstruktur, Package/Bonus/Job Family oder Übersetzung erzeugen **keine neue Role-Architecture-Version**, solange die normative Bedeutung unverändert bleibt.

## Prüfungen

Vor Freigabe insbesondere prüfen:

- Gewichte = 1.0, IDs eindeutig, Knockouts begründet.
- Rollenbestimmende Reporting-, Scope-, Standort-/Mobilitäts-, Sprach- und Schnittstellenfakten sind nicht versehentlich als bloße Kommunikationsmetadaten ausgelagert.
- Reine HR-/Darstellungsmetadaten wurden nicht zu normativen Auswahlkriterien hochgestuft.
- Keine harte Anforderung ist nur deshalb abgeschwächt, weil eine historische oder öffentliche Formulierung weicher klingt.

## Fehlerbehandlung

Widerspricht ein Corporate-Template oder eine bestehende Ausschreibung der bestätigten Role Architecture, wird **nicht gemittelt**. Die Role Architecture bleibt normativ; `job-description-authoring` muss die Kommunikationsfassung korrigieren oder die Differenz als Konflikt melden.

## Übergabe

Nach Freigabe an `job-description-authoring` und `candidate-role-fit-assessment`. An `job-description-authoring` darf zusätzlich separat bestätigter Kommunikationskontext übergeben werden, etwa Corporate-Template, Organigramm, Package/Job Family, Branding, Dokumentstruktur oder gewünschte Sprachfassungen. Diese ergänzende Evidenz besitzt **keinen Vorrang** vor Role Architecture und Scorecard.

## Abschlusskriterien

Abgeschlossen ist die Role Architecture, wenn Auftrag, Outcomes, Mandat, Scope, Capability-Modell und Scorecard konsistent und freigegeben sind und die Grenze zwischen normativen Rollenfakten und nicht-normativen HR-/Kommunikationsmetadaten eindeutig ist.