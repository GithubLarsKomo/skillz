---
name: job-description-authoring
description: Erzeugt aus einer freigegebenen Role Architecture zielgruppengerechte interne Stellenbeschreibungen, Executive-Search-Briefs und öffentliche Ausschreibungen, übernimmt bei Bedarf bestätigte Corporate-Templates und Organisationsmetadaten und sichert semantische Konsistenz über alle Fassungen. Verwenden, wenn ein normatives Rollenmodell kommunikativ übersetzt werden soll.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.4.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - role-architecture
consumes:
  - role-architecture.json
  - role-scorecard.json
outputs:
  - job-description.md
  - executive-search-brief.md
  - public-job-posting.md
lastEvaluated: 2026-08-24
---

# Job Description Authoring

## Trigger

Verwenden, wenn eine bereits freigegebene Role Architecture kommunikativ in interne Stellenbeschreibung, Executive-Search-Brief oder öffentliche Ausschreibung übersetzt werden soll. Dieser Skill beantwortet: **Wie beschreiben wir eine bereits definierte Rolle korrekt, verständlich, corporate-kompatibel und über alle Fassungen konsistent?**

Die freigegebene `role-architecture` ist normativ. Dieser Skill darf **keine neuen Must-haves** erfinden und weder Mandat, Entscheidungsrechte, Scorecard noch Scope verändern.

Vorhandene Corporate-Postings, HR-Briefings, Organigramme, freigegebene Search-Strategien, Package-/Job-Family-Angaben, Sprachfassungen oder Layout-Vorgaben dürfen als ergänzende Evidenz verwendet werden. Sie steuern Darstellung und konkrete Organisationsbezeichnungen, besitzen aber **keinen Vorrang vor Role Architecture und Scorecard**.

## Voraussetzungen

Erforderlich sind:

- `role-architecture.json` mit `status=approved`,
- zugehörige `role-scorecard.json` mit `status=approved`,
- identische `roleArchitectureId` und `roleArchitectureVersion`,
- kein bekannter normativer Widerspruch zwischen Architektur und Scorecard.

Optional können zusätzlich vorliegen:

- bestätigte Executive-Search-/Sourcing-Strategie,
- Corporate-Template oder bisherige Ausschreibung als Stil-/Strukturreferenz,
- Organigramm bzw. bestätigte Organisationsdarstellung,
- HR-/Package-/Job-Family-Metadaten,
- gewünschte Sprachfassungen,
- Branding-, Vertraulichkeits- und Dokumentformatvorgaben.

Eine `draft`-, `review`- oder `superseded`-Architektur darf nicht als aktuelle Basis verwendet werden. Stimmen ID oder Version der Scorecard nicht überein, wird die Autorenerstellung blockiert.

## Quellenhierarchie

Bei mehreren Quellen gilt folgende Priorität:

1. **freigegebene Role Architecture** – normativer Rollenauftrag, Scope, Constraints, Capabilities und Entscheidungsrechte;
2. **freigegebene Role Scorecard** – normative Auswahl- und Knockout-Logik;
3. **separat freigegebene Search-/Sourcing-Strategie** – nur für Suchpriorisierung, Target Pools und Search Governance;
4. **bestätigte Organisations-/HR-Metadaten** – z. B. Reporting Line, Package, Job Family, Start-/Setup-Zeitpunkt, Organigramm;
5. **Corporate-Template / bestehende Ausschreibung** – Struktur, Ton, wiederkehrende Labels, Branding und Format;
6. **redaktionelle Formulierung** – nur dort, wo die höheren Ebenen nichts festlegen.

Konflikte zwischen Ebenen werden nicht durch Mittelung oder weichere Formulierungen verborgen. Eine alte Ausschreibung darf ein bestätigtes Must-have nicht zu einer Präferenz abschwächen und darf bekannte Organisationsfakten nicht wieder in Platzhalter zurückverwandeln.

## Ablauf

### 1. Source Reconciliation

Vor dem Schreiben eine kurze interne Quellenmatrix bilden:

- Welche Aussagen sind normativ?
- Welche sind nur Search-/Sourcing-Regeln?
- Welche sind bestätigte Organisations-/HR-Fakten?
- Welche Elemente des Templates sind reine Form/Stil?
- Welche historischen Inhalte widersprechen der aktuellen Rollenarchitektur?
- Welche Felder sind tatsächlich noch unbekannt?

Bekannte Werte ersetzen vorhandene Platzhalter. Unbekannte Werte werden **nicht erfunden**. Wenn ein Template beispielsweise `[Budget]`, `[Headcount]`, `[Travel]` oder `[Hybrid model]` enthält, obwohl einzelne Werte bereits bestätigt sind, werden nur die echten Unbekannten als offene Felder erhalten.

### 2. Corporate-Template-Inheritance

Wenn ein freigegebenes oder vom Nutzer gewünschtes Corporate-Template vorliegt, übernimm soweit sinnvoll:

- Dokumentdramaturgie und Abschnittsfolge,
- Corporate-Headings und Terminologie,
- organisationseigene Funktionsnamen,
- tabellarische Executive-/Organisational-Set-up-Blöcke,
- Organigramm als visuelles Kontextobjekt,
- Proprietary-/Confidential-Kennzeichnung,
- Tonalität, Typografie- und Layoutlogik,
- gewünschte Reihenfolge von Aufgaben, Besonderheiten und Profil.

**Nicht ungeprüft übernehmen:** alte Must-haves, weiche Präferenzformulierungen, historische Scope-Aussagen, veraltete Reporting-Lines, Platzhalter oder frühere Zielunternehmen. Form darf geerbt werden; Inhalt muss gegen die aktuelle Quellenhierarchie validiert werden.

### 3. Drei Projektionen

#### Interne Stellenbeschreibung

`job-description.md` enthält mindestens Zweck, organisatorische Einordnung, Accountabilities, Entscheidungsrechte, Scope, Schnittstellen, Erfolgsmaßstäbe und Capability-Anforderungen. Sie darf intern präziser sein als die öffentliche Fassung.

Für Executive-Rollen ist ein kompakter **Organisational set-up** am Dokumentanfang bevorzugt, wenn die Daten bestätigt sind: Reporting Line, Standort/Mobilität, funktionaler Scope und Kerninterfaces; Package/Level/Job Family nur, wenn als HR-Metadaten bestätigt.

#### Executive-Search-Brief

`executive-search-brief.md` ergänzt Suchkontext, Veränderungsauftrag, kritische Erfolgsfaktoren, Must-have-Capabilities, plausible Evidence-Proxys, bewusst offene Karrierepfade, Interview-Schwerpunkte und bekannte Fehlbesetzungsrisiken. **Vertrauliche Inhalte** nur im zulässigen internen Rahmen.

Für Executive Search ist folgende Informationsarchitektur ein bewährter Default, sofern das Corporate-Template nichts Besseres vorgibt:

1. Executive Role / Organisational set-up,
2. Search mandate,
3. Search principle,
4. zentrale Responsibilities,
5. What makes this position special / Veränderungsauftrag,
6. priorisierte Outcomes mit Zeithorizont,
7. What sets you apart / Capability-Profil,
8. Executive-search guidance,
9. Target-/Sourcing-Pools aus freigegebener Search-Strategie,
10. Evidence required before longlist,
11. Early red flags / mis-hire risks,
12. Interview focus areas,
13. Longlist prioritisation and governance.

Target-Company-Tiers oder Arbeitgebernamen dürfen **nur** aus einer separat bestätigten Search-/Sourcing-Strategie stammen. Arbeitgeberherkunft erhöht niemals den Kandidatenscore.

#### Öffentliche Ausschreibung

`public-job-posting.md` übersetzt die Architektur in klare, inklusive und attraktive Sprache. Sie trennt Verantwortungen von Anforderungen, reduziert unnötige Credentials und vermeidet interne vertrauliche Details. **Keine diskriminierenden oder sachfremden Kriterien.**

Die öffentliche Fassung darf kürzer und weniger vertraulich sein, aber sie darf keine normative Anforderung widersprechen oder bewusst abschwächen. Ein hartes Branchen-/Capability-Must-have darf beispielsweise nicht als „preferably“ oder durch eine breitere Alternativbranche formuliert werden, wenn diese Alternative normativ nicht zulässig ist.

### 4. Semantische Entdopplung

Vor Finalisierung ähnliche Aussagen zusammenführen. Ziel ist **eine Aussage pro semantischem Zweck**, nicht dieselbe Botschaft in mehreren Varianten.

- Rollenauftrag einmal klar im Search Mandate/Purpose.
- Dauerhafte Verantwortungen einmal unter Responsibilities/Accountabilities.
- Veränderungscharakter einmal unter „What makes this position special“ bzw. Context.
- Zeitgebundene Resultate einmal unter Outcomes/Priorities.
- Anforderungen einmal unter „What sets you apart“ bzw. Requirements.
- Im Search-Anhang dieselben Anforderungen nicht erneut beschreiben, sondern **operationalisieren**: Evidenz, Red Flags, Interviewfragen, Scoring-Governance.

Wiederholung ist nur zulässig, wenn sich die Funktion der Aussage ändert, z. B. von „Requirement“ zu „konkrete Evidenzfrage“.

### 5. Cross-Projection Consistency

Alle erzeugten Fassungen werden gegeneinander geprüft. Dabei gilt:

- Ein `knockout` bleibt in jeder Fassung, in der er erwähnt wird, ein hartes Kriterium.
- Ein Must-have darf nicht in einer anderen Fassung zu „preferred“, „nice to have“ oder einer fachlich breiteren Alternative werden.
- Bestätigte Reporting-, Standort-, Hybrid-, Reise-, Scope- und Sprachangaben dürfen in keiner Fassung widersprüchlich oder wieder als Platzhalter erscheinen.
- Nicht bestätigte Headcount-, Budget- oder Grade-Angaben dürfen nicht erfunden werden.
- Search-spezifische Target Companies erscheinen nicht als öffentliche Kandidatenanforderung.
- Öffentliche Kürzung ist zulässig; **Widerspruch ist nicht zulässig**.

### 6. Bilinguale / mehrsprachige Fassungen

Wenn mehrere Sprachfassungen erzeugt oder aus einem bestehenden Dokument übernommen werden, müssen sie **semantisch äquivalent** sein.

Besonders prüfen:

- Muss vs. bevorzugt,
- erforderliche Jahre/Erfahrungstiefe,
- Branchen- und Technologiefokus,
- Reporting Line und Scope,
- Standort/Präsenz/Reise,
- Sprachvoraussetzungen,
- Entscheidungs- und Eskalationsrechte.

Eine Übersetzung darf weder Auswahlkriterien verschärfen noch abschwächen. Abweichungen zwischen bestehenden Sprachfassungen werden explizit bereinigt statt einfach gemeinsam weitergeführt.

### 7. Traceability

**Jede harte Anforderung** muss auf Capability, Outcome, Risiko oder zwingende Rahmenbedingung der Role Architecture zurückführbar sein. Formulierungsfreiheit darf die **normative Bedeutung** nicht verschieben.

Kennzeichne Unterschiede zwischen interner und öffentlicher Darstellung als **Kommunikationsentscheidung**, nicht als Änderung der Rolle. Jede erzeugte Fassung hält `roleArchitectureId` und `roleArchitectureVersion` im Dokumentkopf oder in maschinenlesbaren Begleitmetadaten fest.

Search-spezifische Sourcing-Artefakte referenzieren zusätzlich ihre freigegebene Search-/Sourcing-Strategie, falls eine solche verwendet wurde.

### 8. Human-Review-Feedback als Skill-Kalibrierung

Eine menschlich gereviewte Endfassung darf genutzt werden, um den Authoring-Skill zu verbessern. Dabei strikt trennen:

- **projektspezifische redaktionelle Entscheidung** → bleibt im Projekt;
- **wiederverwendbare Workflow-Erkenntnis** → darf als generische Skill-Regel oder Evaluation übernommen werden.

Keine unternehmens-, rollen- oder kandidatenbezogenen Details aus einem Einzelreview in den generischen Skill hardcoden.

## Versionierung und Staleness

Wird Role Architecture oder Scorecard durch eine neue freigegebene Version ersetzt, **werden alle aus der alten Version abgeleiteten Fassungen `stale`**. Sie dürfen archiviert und nachvollzogen, aber nicht als aktuelle Ausschreibungs- oder Search-Basis weiterverwendet werden. Die drei Projektionen werden gegen die neue Version neu erzeugt oder explizit revalidiert.

Ändern sich nur Corporate-Layout, Branding, Dokumentstruktur, Package/Job Family oder Übersetzung ohne normative Bedeutungsänderung, bleibt die Role-Architecture-Version unverändert. Die Kommunikationsartefakte erhalten bei Bedarf eine eigene Dokumentversion.

## Prüfungen

Prüfe vor Abschluss:

- Zweck und Outcomes stimmen mit der Role Architecture überein.
- Es fehlen oder entstehen keine Entscheidungsrechte.
- Must-haves wurden weder erweitert noch abgeschwächt.
- Scorecard-Knockouts sind in Search Brief und öffentlicher Fassung widerspruchsfrei dargestellt.
- Outcomes bleiben konkreter als Aktivitätslisten.
- Anforderungen sind inklusiv und funktionsbezogen.
- Vertrauliche Inhalte sind angemessen abstrahiert.
- Öffentliche Fassung bleibt realistisch statt werblicher Überhöhung.
- Corporate-Struktur wurde übernommen, ohne historischen Inhalt ungeprüft zu erben.
- Bekannte Organisations-/HR-Angaben ersetzen entsprechende Template-Platzhalter.
- Verbleibende Platzhalter betreffen tatsächlich unbekannte Werte und sind sichtbar als offen markiert.
- Interne, Search- und öffentliche Fassungen widersprechen sich nicht in Must-have/Preferred, Scope, Reporting, Standort, Reise, Sprache oder Entscheidungskompetenz.
- Mehrsprachige Fassungen sind semantisch äquivalent.
- Redundante Aussagen wurden zusammengeführt; Search-Guidance operationalisiert Anforderungen statt sie nur zu wiederholen.
- Target Companies oder Sourcing-Tiers stammen nur aus bestätigter Search-/Sourcing-Evidenz und beeinflussen die Bewertung nicht.
- Alle Fassungen referenzieren dieselbe freigegebene normative Version.

## Fehlerbehandlung

Bei echtem inhaltlichem Änderungsbedarf **zurück zu `role-architecture`**; keine normative Änderung im Authoring verstecken. Ist die Architektur nicht approved oder die Scorecard-Version inkonsistent, die Ausgabe blockieren statt auf einer vermeintlich aktuellen Fassung weiterzuarbeiten.

Widerspricht eine bestehende Ausschreibung oder eine Übersetzung der Role Architecture, korrigiere die Kommunikationsfassung. Ist unklar, ob der Unterschied eine echte Rollenänderung darstellt, blockiere die betroffene Aussage und route zur Role Architecture zurück.

Bei widersprüchlichen Template-Platzhaltern und bestätigten Fakten gilt der bestätigte Fakt. Bei unbekanntem Headcount, Budget, Package oder ähnlichen HR-Daten nichts erfinden; offen markieren oder den nicht benötigten Platzhalter aus der kommunizierten Fassung entfernen.

### Verbotene Übergänge

- Kein direkter Einstieg aus `role-requirements-grilling`; zuerst muss eine freigegebene `role-architecture` entstehen.
- Keine Änderung der normativen Rolle innerhalb dieses Skills.
- `public-job-posting.md`, `job-description.md` und `executive-search-brief.md` sind keine normative Bewertungsbasis für `candidate-role-fit-assessment`.
- Keine Übernahme alter Template-Anforderungen ohne Abgleich mit Role Architecture und Scorecard.
- Keine sprachspezifische Abschwächung oder Verschärfung harter Kriterien.

## Übergabe

Die Job Description ist **kein Bewertungsmaßstab für Kandidaten**, wenn sie aus Kommunikationsgründen verkürzt ist. `candidate-role-fit-assessment` verwendet immer `role-architecture.json` und `role-scorecard.json` als normative Basis; die Kommunikationsartefakte dürfen nur ergänzender Kontext sein.

Der Executive-Search-Brief darf dem Search-Partner zusätzlich freigegebene Sourcing-Prioritäten, Evidence Requirements, Red Flags und Interviewfokus bereitstellen. Diese Informationen steuern Suche und Evidenzerhebung, ersetzen aber niemals die normative Scorecard.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn alle erzeugten Fassungen denselben Rollenauftrag korrekt projizieren, die verwendete normative Version referenzieren, Corporate-Form und bestätigte Organisationsmetadaten korrekt übernehmen, semantisch entdoppelt sind, mehrsprachig konsistent bleiben und keine neuen oder abgeschwächten Auswahlkriterien enthalten.