---
name: legal-change-monitoring
description: Überwacht Rechtsänderungen außerhalb des spezialisierten Medical-Device-Regulatory-Monitorings über versionierte Primärquellen-Snapshots, trennt echte normative Änderungen von Metadaten-/Guidance-Änderungen und erzeugt belastbare Legal-Change-Events mit asOf, Effective Date und betroffenen Rechtsgebieten.
---

# Legal Change Monitoring

## Zweck

Erkenne belastbar, **dass** sich eine relevante Rechtsquelle geändert hat. Dieser Skill entscheidet noch nicht, wie das Unternehmen darauf reagieren muss. Detection und Impact Assessment bleiben getrennt.

## Scope

Insbesondere Corporate/Governance, Employment/Labor, Privacy/Data, AI/Cyber, Competition/Antitrust, IP, Whistleblowing, Trade/Sanctions/Export, Product Liability/Safety, Litigation/Procedure, Commercial Law, Real Estate und sonstige Legal Domains. Medical-Device-/IVD-Regulatory-Quellen verbleiben primär beim bestehenden `regulatory-change-monitoring`; bestätigte Events können später gemeinsam geroutet werden.

## Source Hierarchy

1. Gesetz-/Verordnungsblatt, amtliche konsolidierte Norm, EUR-Lex oder andere zuständige Primärquelle.
2. Gericht/Behörde für Entscheidungen, verbindliche Akte und offizielle Bekanntmachungen.
3. Offizielle Guidance/FAQ/Leitlinie als eigene `guidance`-Klasse.
4. Sekundärquellen nur für Discovery; sie erzeugen allein kein bestätigtes Change Event.

## Snapshot Model

Jeder Watch-Eintrag enthält `sourceId`, `authority`, `jurisdiction`, `domain`, `sourceType`, `officialUrl`, `retrievedAt`, `publishedAt`, `effectiveFrom`, `versionId`, `status`, `contentFingerprint`, `previousSnapshot`, `watchFrequency` und `owner`.

## Change Event

Ein bestätigtes Event enthält mindestens:

```json
{
  "changeId": "LC-...",
  "sourceId": "...",
  "jurisdiction": "DE|EU|...",
  "domain": "...",
  "changeType": "new|amended|repealed|effective-date|judgment|guidance|correction",
  "publishedAt": "...",
  "effectiveFrom": "...",
  "asOf": "...",
  "oldStateRef": "...",
  "newStateRef": "...",
  "verifiedDelta": [],
  "unknownDelta": [],
  "status": "detected|verified|superseded"
}
```

## Delta Gate

- Geänderte `lastModified`-/Webseitenmetadaten sind kein materieller Rechtsdelta.
- Konsolidierte Fassungen, Änderungsgesetz und Inkrafttretensregel gemeinsam prüfen, wenn für den Delta erforderlich.
- Draft, political agreement, adopted, published, in force und applicable nicht vermischen.
- Ist der Inhalt nicht zuverlässig vergleichbar, `unknownDelta` statt erfundener Änderung ausgeben.

## Judgment / Guidance Gate

Gerichtsentscheidungen und Guidance werden nicht automatisch wie Gesetzesänderungen behandelt. Erfasse zuständiges Gericht/Behörde, Verfahrensstand, Bindungs-/Präzedenzwirkung soweit relevant, betroffene Norm und mögliche Interpretationsänderung. Materielle Bedeutung wird erst downstream bewertet.

## Handoff

Nur verifizierte oder ausdrücklich als vorläufig markierte Events an `legal-change-impact-orchestrator` übergeben. Jede Übergabe enthält Quelle, Delta, Effective Date, Unsicherheiten und betroffene Domains; keine voreilige Unternehmensmaßnahme.

## Qualitätsgate

Pass nur, wenn Primärquelle, Version/Freshness, Veröffentlichungs-/Wirksamkeitsstatus, alter/neuer Zustand, Delta-Evidenz und Unsicherheiten nachvollziehbar sind und Detection nicht als Impact Assessment ausgegeben wird.
