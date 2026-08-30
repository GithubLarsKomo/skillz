---
name: tax-procedure-matter-workflow
description: Orchestriert steuerliche Verfahrens-Matters von Erklärung und Bescheidabgleich über Betriebsprüfung, Korrektur, Einspruch und gerichtliche Eskalation, hält Fristen, Verfahrensstand, Evidence und materielle Tax Positions zusammen und routet Vertretung oder Steuerstraf-/Counsel-Fragen an befugte Professionals.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-tax-context
  - tax-position-register
  - tax-professional-routing
outputs:
  - tax-procedure-status.json
  - tax-assessment-reconciliation.json
  - tax-procedure-action-plan.json
  - tax-procedure-deadlines.json
lastEvaluated: 2026-08-30
---

# Tax Procedure Matter Workflow

## Zweck

Tax Advice bis zur tatsächlichen Umsetzung und behördlichen Reaktion verfolgen.

## Lifecycle

`Return/Position -> Assessment -> Reconciliation -> Difference Classification -> Correction/Objection -> Audit/Negotiation -> Litigation Interface -> Closure`.

## Bescheidabgleich

Vergleiche Erklärung/beantragte Positionen mit Bescheid. Jede Abweichung erhält `positionRef`, `amount`, `reason`, `authorityBasis`, `deadline`, `materiality`, `recommendedAction` und `professionalGate`.

## Betriebsprüfung

Prüfungsanordnung, Prüfungszeitraum, Themen, Informationsanforderungen, Evidence, Findings, Schlussbesprechung, Prüfungsbericht und Änderungsbescheide getrennt halten. Transfer-Pricing-, Verfahrens- oder Strafrisiken gezielt routen.

## Einspruch / Verfahren

Frist, Zulässigkeit, Beschwer, angegriffene Position, Begründung, Aussetzung/Vollziehung soweit einschlägig, Belege, Gegenargumente und Eskalationsstufe strukturiert dokumentieren. Vertretungsbefugnis über `tax-professional-routing` prüfen.

## Qualitätsgate

Pass nur, wenn Verfahrensakt, Zugang/Bekanntgabe soweit relevant, Frist, betroffene Positionen, Beträge, Evidence, nächste Aktion und Professional-/Authority-Grenze nachvollziehbar sind.