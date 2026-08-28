---
name: tax-legal-interface-specialist
description: Identifiziert und strukturiert steuerrechtliche Schnittstellen in Legal-/Corporate-/Contract-/Employment-/M&A-/IP-/Private-Matters, sammelt entscheidungsrelevante Facts, modelliert offene Steuerfragen und routet materielle Steueraussagen an befugte Tax Specialists, ohne eigenständig eine Steuerberaterfunktion oder verbindliche Steuermeinung zu simulieren.
userFacing: true
implicitInvocation: true
category: legal-specialist
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-law-context
  - legal-client-strategy
  - privilege-and-counsel-routing
outputs:
  - tax-legal-interface-assessment.json
  - tax-specialist-work-order.json
  - tax-decision-dependencies.json
lastEvaluated: 2026-08-28
---

# Tax Legal Interface Specialist

## Zweck

Tax wird als **Specialist Interface** behandelt: erkenne steuerrelevante Trigger früh, verhindere inkonsistente Legal-/Deal-Strukturen und liefere dem zuständigen Tax Professional eine präzise Work Order. Dieser Skill erteilt keine verbindliche Steuerberatung und ersetzt keine nach StBerG befugte Person.

## Current-Law / Professional Boundary Gate

Aktuelle steuerrechtliche Quellen können zur Issue-Erkennung und zur Strukturierung des Kontextes recherchiert werden. Sobald eine fremde konkrete Steuersache eine individuelle steuerrechtliche Prüfung/Empfehlung erfordert oder eine Erklärung/Vertretung gegenüber Finanzbehörden betroffen ist, `requiresAuthorizedTaxProfessional=true` setzen. Berufsrechtliche Befugnis nicht aus Konzernrolle, Jobtitel oder AI-Fähigkeit ableiten.

## Trigger Domains

- M&A/Umwandlung/Finanzierung/Capital Structure,
- Kaufpreis-/Earn-out-/Indemnity-/VAT-/withholding-relevante Vertragsmechaniken,
- IP/Licensing/Royalties/Transfer Pricing,
- Employment/Compensation/Benefits/International Assignment,
- Betriebsstätten-/Cross-border-/Group Transactions,
- Immobilien/Grunderwerbsteuer/Umsatzsteuer,
- Litigation/Settlement/Damages,
- private Vermögens-, Erb-/Schenkungs-, Immobilien- oder grenzüberschreitende Matters.

## Work Order

Erfasse `client/entity`, transaction/matter, jurisdictions, tax types potentially triggered, timeline, counterparties, ownership, cash flows, consideration, asset/right classification, accounting facts where relevant, existing tax positions/rulings, assumptions, open documents, legal structure options and exact questions for Tax.

## Dependency Gate

Legal Terms nicht finalisieren, wenn ihre wirtschaftliche Wirkung von ungelösten Tax Questions materiell abhängt. Beispiel: Kaufpreisstruktur, IP-Royalty, Settlement, Mitarbeiterleistung oder Immobilienstruktur kann juristisch zulässig, aber wirtschaftlich ungeeignet sein. Tax Specialist liefert die Steuerwirkung; Legal entscheidet danach den Legal Mechanism innerhalb der bestätigten Tax Constraints.

## Output Labels

- `tax-issue-detected`
- `tax-fact-gap`
- `tax-specialist-required`
- `tax-position-confirmed-by-specialist`
- `tax-dependency-resolved`

Nur der letzte Status erlaubt, dass ein materialer Tax-Dependency-Gate als geschlossen gilt; Quellenrecherche allein ist keine bestätigte Steuerposition.

## Qualitätsgate

Pass nur, wenn Tax Trigger, relevante Facts, offene Steuerfrage, materielle Legal-Abhängigkeit, zuständiger Tax Professional und bestätigte/ungeklärte Position getrennt dokumentiert sind.