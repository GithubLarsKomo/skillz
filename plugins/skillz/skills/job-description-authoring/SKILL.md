---
name: job-description-authoring
description: Erzeugt aus einer freigegebenen Role Architecture zielgruppengerechte interne Stellenbeschreibungen, Executive-Search-Briefs und öffentliche Ausschreibungen, ohne Mandat, Anforderungen oder Auswahlkriterien neu zu erfinden. Verwenden, wenn ein normatives Rollenmodell kommunikativ übersetzt werden soll.
---

# Job Description Authoring

## Trigger

Verwenden, wenn eine bereits freigegebene Role Architecture kommunikativ in interne Stellenbeschreibung, Executive-Search-Brief oder öffentliche Ausschreibung übersetzt werden soll. Dieser Skill beantwortet: **Wie beschreiben wir eine bereits definierte Rolle korrekt, verständlich und zielgruppengerecht?**

Die freigegebene `role-architecture` ist normativ. Dieser Skill darf **keine neuen Must-haves** erfinden und weder Mandat, Entscheidungsrechte, Scorecard noch Scope verändern.

## Voraussetzungen

Erforderlich sind:

- `role-architecture.json` mit `status=approved`,
- zugehörige `role-scorecard.json` mit `status=approved`,
- identische `roleArchitectureId` und `roleArchitectureVersion`,
- kein bekannter normativer Widerspruch zwischen Architektur und Scorecard.

Eine `draft`-, `review`- oder `superseded`-Architektur darf nicht als aktuelle Basis verwendet werden. Stimmen ID oder Version der Scorecard nicht überein, wird die Autorenerstellung blockiert.

## Ablauf

### Drei Projektionen

#### Interne Stellenbeschreibung

`job-description.md` enthält mindestens Zweck, organisatorische Einordnung, Accountabilities, Entscheidungsrechte, Scope, Schnittstellen, Erfolgsmaßstäbe und Capability-Anforderungen. Sie darf intern präziser sein als die öffentliche Fassung.

#### Executive-Search-Brief

`executive-search-brief.md` ergänzt Suchkontext, Veränderungsauftrag, kritische Erfolgsfaktoren, Must-have-Capabilities, plausible Evidence-Proxys, bewusst offene Karrierepfade, Interview-Schwerpunkte und bekannte Fehlbesetzungsrisiken. **Vertrauliche Inhalte** nur im zulässigen internen Rahmen.

#### Öffentliche Ausschreibung

`public-job-posting.md` übersetzt die Architektur in klare, inklusive und attraktive Sprache. Sie trennt Verantwortungen von Anforderungen, reduziert unnötige Credentials und vermeidet interne vertrauliche Details. **Keine diskriminierenden oder sachfremden Kriterien.**

### Traceability

**Jede harte Anforderung** muss auf Capability, Outcome, Risiko oder zwingende Rahmenbedingung der Role Architecture zurückführbar sein. Formulierungsfreiheit darf die **normative Bedeutung** nicht verschieben.

Kennzeichne Unterschiede zwischen interner und öffentlicher Darstellung als **Kommunikationsentscheidung**, nicht als Änderung der Rolle. Jede erzeugte Fassung hält `roleArchitectureId` und `roleArchitectureVersion` im Dokumentkopf oder in maschinenlesbaren Begleitmetadaten fest.

### Versionierung und Staleness

Wird Role Architecture oder Scorecard durch eine neue freigegebene Version ersetzt, **werden alle aus der alten Version abgeleiteten Fassungen `stale`**. Sie dürfen archiviert und nachvollzogen, aber nicht als aktuelle Ausschreibungs- oder Search-Basis weiterverwendet werden. Die drei Projektionen werden gegen die neue Version neu erzeugt oder explizit revalidiert.

## Prüfungen

Prüfe vor Abschluss:

- Zweck und Outcomes stimmen mit der Role Architecture überein.
- Es fehlen oder entstehen keine Entscheidungsrechte.
- Must-haves wurden nicht durch attraktive Wunschmerkmale erweitert.
- Outcomes bleiben konkreter als Aktivitätslisten.
- Anforderungen sind inklusiv und funktionsbezogen.
- Vertrauliche Inhalte sind angemessen abstrahiert.
- Öffentliche Fassung bleibt realistisch statt werblicher Überhöhung.
- Alle Fassungen referenzieren dieselbe freigegebene normative Version.

## Fehlerbehandlung

Bei echtem inhaltlichem Änderungsbedarf **zurück zu `role-architecture`**; keine normative Änderung im Authoring verstecken. Ist die Architektur nicht approved oder die Scorecard-Version inkonsistent, die Ausgabe blockieren statt auf einer vermeintlich aktuellen Fassung weiterzuarbeiten.

### Verbotene Übergänge

- Kein direkter Einstieg aus `role-requirements-grilling`; zuerst muss eine freigegebene `role-architecture` entstehen.
- Keine Änderung der normativen Rolle innerhalb dieses Skills.
- `public-job-posting.md`, `job-description.md` und `executive-search-brief.md` sind keine normative Bewertungsbasis für `candidate-role-fit-assessment`.

## Übergabe

Die Job Description ist **kein Bewertungsmaßstab für Kandidaten**, wenn sie aus Kommunikationsgründen verkürzt ist. `candidate-role-fit-assessment` verwendet immer `role-architecture.json` und `role-scorecard.json` als normative Basis; die Kommunikationsartefakte dürfen nur ergänzender Kontext sein.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn alle erzeugten Fassungen denselben Rollenauftrag korrekt projizieren, die verwendete normative Version referenzieren, zielgruppengerecht differenziert sind und keine neuen Auswahlkriterien einführen.
