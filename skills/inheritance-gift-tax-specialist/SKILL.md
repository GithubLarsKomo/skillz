---
name: inheritance-gift-tax-specialist
description: Analysiert deutsche Erbschaft- und Schenkungsteuer-Matters aus Erwerb, Bewertung, persönlichen Freibeträgen, Steuerklassen, Begünstigungen, Vorerwerben, Unternehmens-/Immobilienvermögen, Erklärung und Gestaltungsoptionen und hält zivilrechtliche Nachfolge-, Gesellschafts-, Bewertungs- und Notarfragen als eigene Interfaces.
userFacing: true
implicitInvocation: true
category: tax-specialist
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-tax-context
  - tax-position-register
  - tax-structure-pattern-library
outputs:
  - inheritance-gift-tax-assessment.json
  - inheritance-gift-tax-scenarios.json
  - inheritance-gift-tax-open-issues.json
lastEvaluated: 2026-08-30
---

# Inheritance & Gift Tax Specialist

## Scope

Erwerbstatbestand, persönliche Steuerpflicht, Steuerklasse/Freibeträge, Vorerwerbe, Bewertung, Nachlassverbindlichkeiten, Unternehmens- und Immobilienvermögen, Verschonungsregeln, Erklärung und Gestaltungsalternativen.

## Interfaces

- Erbfolge/Testament/Pflichtteil -> `german-inheritance-succession-law-specialist`.
- Gesellschaftsrechtliche Nachfolge -> Legal Office.
- Bewertung -> Valuation Owner.
- Notar/Nachlassgericht -> externe Professional/Authority Route.

## Qualitätsgate

Pass nur, wenn Erwerb, Beteiligte, Vorerwerbe, Vermögens-/Bewertungsbasis, Begünstigungen, zivilrechtliche Vorfragen, aktuelle Authority und Professional Gate getrennt dokumentiert sind.