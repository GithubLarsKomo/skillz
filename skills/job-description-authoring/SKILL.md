---
name: job-description-authoring
description: Erzeugt aus einer freigegebenen Role Architecture zielgruppengerechte interne Stellenbeschreibungen, Executive-Search-Briefs und öffentliche Ausschreibungen, ohne Mandat, Anforderungen oder Auswahlkriterien neu zu erfinden. Verwenden, wenn ein normatives Rollenmodell kommunikativ übersetzt werden soll.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - role-architecture
outputs:
  - job-description.md
  - executive-search-brief.md
  - public-job-posting.md
lastEvaluated: 2026-08-20
---

# Job Description Authoring

## Zweck und Abgrenzung

Dieser Skill beantwortet: **Wie beschreiben wir eine bereits definierte Rolle korrekt, verständlich und zielgruppengerecht?**

Die freigegebene `role-architecture` ist normativ. Dieser Skill darf weder neue Must-haves erfinden noch Mandat, Entscheidungsrechte, Scorecard oder Scope verändern. Bei einem echten inhaltlichen Änderungsbedarf zurück zu `role-architecture`.

## Eintritt und Freigabe-Gate

Erforderlich sind:

- `role-architecture.json` mit `status=approved`,
- die zugehörige `role-scorecard.json` mit derselben `roleArchitectureId` und `roleArchitectureVersion`,
- kein bekannter normativer Widerspruch zwischen Architektur und Scorecard.

Eine `draft`-, `review`- oder `superseded`-Architektur darf nicht als aktuelle Basis verwendet werden. Stimmen ID oder Version der Scorecard nicht überein, wird die Autorenerstellung blockiert, bis der normative Satz konsistent ist.

## Drei Projektionen

### Interne Stellenbeschreibung

`job-description.md` enthält mindestens Zweck, organisatorische Einordnung, Accountabilities, Entscheidungsrechte, Scope, Schnittstellen, Erfolgsmaßstäbe und Capability-Anforderungen. Sie darf intern präziser sein als die öffentliche Fassung.

### Executive-Search-Brief

`executive-search-brief.md` ergänzt Suchkontext, Veränderungsauftrag, kritische Erfolgsfaktoren, Must-have-Capabilities, plausible Evidence-Proxys, bewusst offene Karrierepfade, Interview-Schwerpunkte und bekannte Fehlbesetzungsrisiken. Vertrauliche Inhalte nur im zulässigen internen Rahmen.

### Öffentliche Ausschreibung

`public-job-posting.md` übersetzt die Architektur in klare, inklusive und attraktive Sprache. Sie trennt Verantwortungen von Anforderungen, reduziert unnötige Credentials und vermeidet interne vertrauliche Details. Keine diskriminierenden oder sachfremden Kriterien.

## Traceability

Jede harte Anforderung muss auf eine Capability, ein Outcome, ein Risiko oder eine zwingende Rahmenbedingung der Role Architecture zurückführbar sein. Formulierungsfreiheit darf die normative Bedeutung nicht verschieben.

Kennzeichne Unterschiede zwischen interner und öffentlicher Darstellung als Kommunikationsentscheidung, nicht als Änderung der Rolle.

Jede erzeugte Fassung muss die verwendete `roleArchitectureId` und `roleArchitectureVersion` im Dokumentkopf oder in maschinenlesbarer Begleitmetadaten festhalten.

## Qualitätsprüfung

Prüfe:

- stimmt der Zweck mit der Role Architecture überein,
- fehlen oder entstehen keine Entscheidungsrechte,
- wurden Must-haves nicht durch attraktive Wunschmerkmale erweitert,
- sind Outcomes konkreter als Aktivitätslisten,
- sind Anforderungen inklusiv und funktionsbezogen,
- sind vertrauliche Inhalte angemessen abstrahiert,
- bleibt die öffentliche Fassung realistisch statt werblicher Überhöhung.

## Verbotene Übergänge

- Kein direkter Einstieg aus `role-requirements-grilling`; zuerst muss eine freigegebene `role-architecture` entstehen.
- Keine Änderung der normativen Rolle innerhalb dieses Skills; echte Rollenänderungen gehen zurück zu `role-architecture`.
- `public-job-posting.md`, `job-description.md` und `executive-search-brief.md` sind keine normative Bewertungsbasis für `candidate-role-fit-assessment`.

## Versionierung und Staleness

Wird die zugrunde liegende Role Architecture oder Scorecard durch eine neue freigegebene Version ersetzt, werden alle aus der alten Version abgeleiteten Fassungen `stale`. Sie dürfen archiviert und nachvollzogen, aber nicht als aktuelle Ausschreibungs- oder Search-Basis weiterverwendet werden. Die drei Projektionen müssen gegen die neue freigegebene Version neu erzeugt oder explizit als unverändert revalidiert werden.

## Übergabe

Die Job Description ist **kein Bewertungsmaßstab für Kandidaten**, wenn sie aus Kommunikationsgründen verkürzt ist. `candidate-role-fit-assessment` verwendet immer die zugrunde liegende `role-architecture.json` und `role-scorecard.json` als normative Basis.

## Abschluss

Abgeschlossen ist der Skill, wenn alle erzeugten Fassungen denselben Rollenauftrag korrekt projizieren, die verwendete normative Version referenzieren, zielgruppengerecht differenziert sind und keine neuen Auswahlkriterien einführen.
