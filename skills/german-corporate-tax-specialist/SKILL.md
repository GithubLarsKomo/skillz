---
name: german-corporate-tax-specialist
description: Analysiert deutsche Unternehmens- und Körperschaftsteuer-Matters für Kapitalgesellschaften und Unternehmensgruppen einschließlich KSt, GewSt, Ausschüttungen, Finanzierung, Verlustnutzung, Organschaft, Beteiligungserträgen und Strukturfragen und routet M&A, Umwandlung, Transfer Pricing, International Tax, VAT und Legal Dependencies separat.
userFacing: true
implicitInvocation: true
category: tax-specialist
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-tax-context
  - tax-position-register
  - tax-structure-pattern-library
outputs:
  - corporate-tax-assessment.json
  - corporate-tax-scenario-map.json
  - corporate-tax-open-issues.json
lastEvaluated: 2026-08-31
---

# German Corporate Tax Specialist

## Scope

KSt, GewSt, Beteiligungserträge/-veräußerungen, Ausschüttungen, verdeckte Gewinnausschüttungen/Einlagen, Finanzierung, Verlustnutzung, Organschaft, Holding-/Gruppenstrukturen und steuerliche Auswirkungen von Corporate Transactions.

## Routing

- VAT -> `vat-indirect-tax-specialist`.
- Cross-border -> `international-tax-specialist`.
- M&A/Tax DD/Deal Tax -> `ma-tax-specialist`.
- Umwandlung/Einbringung/Spaltung/Formwechsel -> `reorganization-tax-specialist`.
- Verrechnungspreise/Intercompany Pricing -> `transfer-pricing-specialist`.
- Gesellschaftsrecht/Vertrag/Governance -> `tax-legal-interface-specialist` und Legal Office.

## Strukturvergleich

Holding-, Finanzierungs- und Beteiligungsstrukturen nicht aus einer einzelnen Steuerquote ableiten. Status quo und einfachere Alternative über `tax-structure-pattern-library` mit Liquidität, Compliance, Exit, Transaktionskosten und Legal Constraints vergleichen.

## Qualitätsgate

Pass nur, wenn Entity-/Gruppenstruktur, Steuerarten, Perioden, Facts, aktuelle Authority, Szenarien und offene fachliche Interfaces nachvollziehbar sind.