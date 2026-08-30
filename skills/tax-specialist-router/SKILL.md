---
name: tax-specialist-router
description: Zerlegt Tax Matters in fachlich kohärente Work Orders für passende Tax Specialists und integriert deren Ergebnisse, ohne deren Fachlogik zu duplizieren; Legal, Accounting, Valuation und Counsel bleiben eigene Ownership-Layer.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-tax-context
outputs:
  - tax-specialist-work-orders.json
  - tax-specialist-route-map.json
  - tax-specialist-integration-status.json
lastEvaluated: 2026-08-30
---

# Tax Specialist Router

## Zweck

Der Router entscheidet, welcher Specialist welche Tax-Frage beantwortet. Er beantwortet die materielle Tax-Frage nicht selbst.

## Routing Domains

Unterstütze insbesondere:

- persönliche Einkommensteuer -> `german-personal-income-tax-specialist`
- Unternehmens-/Körperschaftsteuer -> `german-corporate-tax-specialist`
- Umsatzsteuer/VAT -> `vat-indirect-tax-specialist`
- Erbschaft-/Schenkungsteuer -> `inheritance-gift-tax-specialist`
- internationales Steuerrecht -> `international-tax-specialist`
- Betriebsprüfung/Bescheid/Einspruch/Verfahren -> `tax-procedure-matter-workflow`
- Umwandlung/M&A/Transfer Pricing/Real Estate/Payroll bis zur späteren eigenen Specialist-Abdeckung als explizite Capability Gaps bzw. strukturierte Work Orders.

## Interfaces

- Legal Dependencies -> `tax-legal-interface-specialist` / `legal-compliance-office`.
- Accounting Facts bleiben beim Accounting Owner.
- Unternehmens-/Anteils-/Immobilienbewertung bleibt beim Valuation Owner.
- Reserved Professional Work -> `tax-professional-routing`.

## Work Order Contract

```json
{
  "specialist": "...",
  "question": "...",
  "matterId": "TM-...",
  "taxpayer": "...",
  "taxTypes": [],
  "periods": [],
  "jurisdictions": [],
  "facts": [],
  "assumptions": [],
  "sourceRefs": [],
  "dependencies": [],
  "expectedOutput": "specialist-specific artifact"
}
```

## Qualitätsgate

Pass nur, wenn jede materielle Steuerfrage einen fachlichen Owner besitzt, Capability Gaps offen bleiben und widersprüchliche Specialist Outputs nicht stillschweigend harmonisiert werden.