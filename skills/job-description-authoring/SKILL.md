---
name: job-description-authoring
description: Erzeugt aus einer freigegebenen Role Architecture zielgruppengerechte interne Stellenbeschreibungen, Executive-Search-Briefs und öffentliche Ausschreibungen, ohne Mandat, Anforderungen oder Auswahlkriterien neu zu erfinden. Verwenden, wenn ein normatives Rollenmodell kommunikativ übersetzt werden soll.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
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

## Qualitätsprüfung

Prüfe:

- stimmt der Zweck mit der Role Architecture überein,
- fehlen oder entstehen keine Entscheidungsrechte,
- wurden Must-haves nicht durch attraktive Wunschmerkmale erweitert,
- sind Outcomes konkreter als Aktivitätslisten,
- sind Anforderungen inklusiv und funktionsbezogen,
- sind vertrauliche Inhalte angemessen abstrahiert,
- bleibt die öffentliche Fassung realistisch statt werblicher Überhöhung.

## Übergabe

Die Job Description ist **kein Bewertungsmaßstab für Kandidaten**, wenn sie aus Kommunikationsgründen verkürzt ist. `candidate-role-fit-assessment` verwendet immer die zugrunde liegende `role-architecture.json` und `role-scorecard.json` als normative Basis.

## Abschluss

Abgeschlossen ist der Skill, wenn alle erzeugten Fassungen denselben Rollenauftrag korrekt projizieren, zielgruppengerecht differenziert sind und keine neuen Auswahlkriterien einführen.
