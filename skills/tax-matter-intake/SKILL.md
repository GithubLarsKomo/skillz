---
name: tax-matter-intake
description: Strukturiert steuerliche Matters auf Steuerpflichtigen-/Entity-, Zeitraum-, Jurisdiktions-, Steuerarten-, Fristen-, Facts- und Dokumentebene und trennt bestätigte Tatsachen, Annahmen, fehlende Belege und Legal-/Accounting-/Valuation-Abhängigkeiten vor materieller Tax-Analyse.
userFacing: true
implicitInvocation: true
category: analysis
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - tax-matter.json
  - tax-fact-gaps.json
  - tax-dependency-map.json
lastEvaluated: 2026-08-30
---

# Tax Matter Intake

## Zweck

Erzeuge einen belastbaren Tax-Matter-State, bevor Fachanalyse oder Gestaltung beginnt.

## Mindestinhalt

Erfasse mindestens `taxpayer`, `clientContext`, `entities`, `beneficialOwners`, `jurisdictions`, `taxTypes`, `assessmentPeriods`, `matterObjective`, `facts`, `assumptions`, `documents`, `deadlines`, `cashFlows`, `transactions`, `existingPositions`, `filings`, `notices`, `audits`, `legalDependencies`, `accountingDependencies`, `valuationDependencies` und `professionalRepresentation`.

## Kernregeln

- Steuerpflichtigen-, Mandanten- und Entity-Rolle nicht gleichsetzen.
- Zeitraum und Stichtag jeder materiellen Frage explizit machen.
- Tatsachen, steuerliche Qualifikation und Empfehlung getrennt halten.
- Fehlende Unterlagen als Fact Gap kennzeichnen, nicht günstig interpretieren.
- Erklärungs-, Einspruchs-, Änderungs- und Zahlungsfristen als eigenständige Objekte behandeln.
- Bei unklarer Zielstellung vorhandenes `round-based-requirements-grilling` wiederverwenden.

## Qualitätsgate

Pass nur, wenn die steuerlich entscheidungsrelevanten Personen/Entities, Perioden, Jurisdiktionen, Steuerarten, Fristen, Facts, Belege und offenen Abhängigkeiten sichtbar sind.