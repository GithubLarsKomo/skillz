---
name: travel-context-builder
description: Normalisiert bestätigte Reiseanforderungen, Präferenzen, Zeitfenster, Reisende, Budget und harte Constraints in einen kanonischen Travel Context ohne fehlende Entscheidungen zu erfinden.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
discoverability: internal
owners:
  - GithubLarsKomo
requires: []
outputs:
  - travel-context.json
lastEvaluated: 2026-08-30
---
# Travel Context Builder

## Zweck und Grenze

Überführe bestätigte Reiseanforderungen in genau einen kanonischen `travel-context.json`. Der Skill normalisiert bereits bekannte Entscheidungen, Präferenzen, Constraints und offene Punkte; er recherchiert keine Reiseziele, Preise oder Verfügbarkeiten und erfindet keine fehlenden Anforderungen.

## Trigger

Verwenden, sobald eine Reiseidee oder ein `requirements-handoff.json` so weit geklärt ist, dass Zielzustand, Reisende, Zeitrahmen und wesentliche Constraints strukturiert an Travel-Worker übergeben werden können.

Wenn eine entscheidungsrelevante Präferenz fehlt, markiere sie unter `openQuestions` und route über den Orchestrator bei Bedarf an `round-based-requirements-grilling`.

## Voraussetzungen

Soweit für die konkrete Reise relevant:

- Reisende und bekannte Mobilitäts-/Zugänglichkeitsconstraints,
- Startregion oder Startpunkt,
- Zielstatus `open | candidate | fixed`,
- Zeitraum `fixed | window | flexible`,
- Budgetstatus `hard | target | open`,
- Must-haves, Präferenzen und Ausschlüsse,
- Transport- und Unterkunftspräferenzen,
- Interessen, Reisetempo und Entscheidungskriterien.

Nicht relevante Felder dürfen leer bleiben. Fehlende Werte werden nicht durch typische Reiseannahmen ersetzt.

## Ablauf

1. Reiseauftrag als `destination-discovery`, `trip-planning` oder `trip-operations` klassifizieren.
2. Fakten, harte Constraints, Präferenzen und offene Fragen trennen.
3. Zeit- und Budgetangaben mit explizitem Status normalisieren.
4. Must-haves mit stabilen IDs erfassen, soweit spätere Hard Gates darauf referenzieren.
5. Entscheidungskriterien nur mit bestätigten Gewichten übernehmen; unbestätigte Kriterien bleiben ungewichtet.
6. Quellen- oder Handoff-Referenzen erhalten.
7. `travel-context.json` erzeugen.

## Output Contract

`travel-context.json` enthält mindestens:

- `schemaVersion`, `tripId`, `asOf`, `mode`,
- `travellers`, `origin`, `destination`, `dates`, `budget`,
- `mustHaves`, `preferences`, `exclusions`,
- `transport`, `stay`, `interests`, `pace`,
- `decisionCriteria`, `openQuestions`, `sourceRefs`.

Budget und Datum tragen immer den jeweiligen Klärungsstatus. Ein leeres Feld ist kein stillschweigend bestätigter Default.

## Prüfungen

Bestanden nur wenn:

- Must-haves und Präferenzen getrennt bleiben,
- ein `hard` Budget tatsächlich explizit bestätigt ist,
- flexible Daten nicht zu festen Daten werden,
- keine Präferenzgewichte erfunden werden,
- offene entscheidungsrelevante Fragen sichtbar bleiben,
- bereits beantwortete Anforderungen nicht erneut als offen markiert werden.

## Fehlerbehandlung

Wenn Ziel, Zeitfenster, Reisende oder andere für den nächsten Schritt zwingende Informationen fehlen, Status `requirements-incomplete` an den Orchestrator zurückgeben. Keine Destination-, Preis- oder Buchungsannahme erzeugen.

## Übergabe

Normalpfad: `travel-destination-research`, `travel-transport-research` und `travel-stay-research` konsumieren denselben Travel Context.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn ein widerspruchsfreier kanonischer Travel Context vorliegt, alle übernommenen Entscheidungen auf bestätigte Angaben zurückgehen und jede noch entscheidungsrelevante Unsicherheit explizit markiert ist.
