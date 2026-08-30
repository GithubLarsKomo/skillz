# Tax Advisory Office – Universe Foundation

Status: 2026-08-30  
Branch: `feat/tax-advisory-office-foundation`

## Architectural intent

The Tax Advisory Office is a peer of the existing Legal & Compliance Office, not a Legal submodule and not a second monolithic professional-services stack. Shared Skillz primitives remain authoritative for research, evidence, grilling, decisions, controlled documents and handoffs. Tax-specific ownership is added only where the domain requires it.

```text
                         SKILLZ UNIVERSE
                                |
           +--------------------+--------------------+
           |          Shared Primitives              |
           | Research · Evidence · Grilling ·        |
           | Decision · Documents · Handoffs         |
           +--------------------+--------------------+
                                |
              +-----------------+-----------------+
              |                                   |
       LEGAL & COMPLIANCE                   TAX ADVISORY
             OFFICE                             OFFICE
              |                                   |
       Legal Specialists                  Tax Specialists
              |                                   |
              +----------- INTERFACE -------------+
                                |
              +-----------------+-----------------+
              |                                   |
       Tax Position Register             Structure Library
              |                                   |
              +-----------------+-----------------+
                                |
                       Tax Knowledge Layer
```

## Core Tax Office

- `tax-advisory-office` – thin matter orchestrator.
- `tax-matter-intake` – taxpayer/entity, period, jurisdiction, tax types, deadlines, evidence and dependencies.
- `current-tax-context` – current authority, evidence tiers and freshness.
- `tax-specialist-router` – coherent work-order routing.
- `tax-position-register` – versioned material tax positions.
- `tax-structure-pattern-library` – reusable structure/transaction patterns with alternatives and failure modes.
- `professional-tax-knowledge-ingestion` – controlled ingestion of professional secondary/practitioner sources.
- `tax-professional-routing` – StBerG/professional/authority boundary gate.
- `tax-matter-final-gate` – filing/implementation/closure readiness.

## Initial Specialists

- `german-personal-income-tax-specialist`
- `german-corporate-tax-specialist`
- `vat-indirect-tax-specialist`
- `inheritance-gift-tax-specialist`
- `international-tax-specialist`
- `tax-procedure-matter-workflow`

## Planned specialist extensions

Priority next wave:

- `reorganization-tax-specialist`
- `ma-tax-specialist`
- `transfer-pricing-specialist`
- `real-estate-tax-specialist`
- `employment-payroll-tax-specialist`
- `partnership-tax-specialist`
- `nonprofit-association-tax-specialist`

These remain explicit capability gaps until implemented; the router must not silently simulate them.

## Legal <-> Tax contract

The existing `tax-legal-interface-specialist` remains the compatibility and adapter layer.

Legal -> Tax:

- factual/transaction context,
- jurisdictions and periods,
- tax types potentially triggered,
- legal structure options,
- cash flows/consideration,
- exact questions,
- material legal terms that depend on tax outcome.

Tax -> Legal:

- tax position references and review state,
- tax consequences/constraints,
- tax structure options where relevant,
- unresolved professional/authority gates.

Tax decides tax treatment/economic tax effect within its authority model; Legal decides the legal mechanism within confirmed or explicitly open tax constraints.

## Knowledge architecture

### Evidence tiers

1. **T1 Primary Authority** – statutes, EU law, BFH/BVerfG/EuGH/FG, BMF, BZSt, competent tax administration.
2. **T2 Authoritative Professional Interpretation** – leading commentary, journals, academic literature, OECD where relevant.
3. **T3 Practitioner Knowledge** – high-quality law/tax-firm publications and professional practice material.
4. **T4 Discovery/Explanation** – YouTube, podcasts, social media and other explanatory formats.

T3/T4 may create hypotheses, patterns, case models and research triggers. They cannot alone mark a material `tax-rule` or individual `tax-position` as confirmed.

### JUHN role

`juhn.com` and `@juhnsteuerberater` are seed practitioner sources, especially for:

- holding/group structures,
- reorganization,
- M&A,
- international tax/exit tax,
- tax procedure/audit/objection,
- corporate taxation,
- inheritance/gift tax,
- real estate.

Website and video should be linked by topic. Website content is primarily useful for structured concepts/patterns; video transcripts are especially useful for practitioner heuristics, typical client situations, option comparisons, warnings and implementation sequences.

### Knowledge types

- `tax-concept`
- `tax-rule`
- `tax-structure-pattern`
- `tax-practitioner-heuristic`
- `tax-failure-pattern`
- `tax-case-example`

### Freshness

Material records should preserve `publishedAt`, `effectiveFrom`, `effectiveUntil`, `lawAsOf`, `verifiedAt` and `supersededBy` where applicable.

## Matter lifecycle

```text
Tax Matter Intake
      -> Current Tax Context
      -> Fact/Evidence Completion
      -> Specialist Routing
      -> Tax Positions / Calculations / Scenarios
      -> Legal / Accounting / Valuation Interfaces
      -> Professional Review Gate
      -> Decision / Filing / Implementation
      -> Assessment / Reconciliation / Objection
      -> Final Gate / Monitoring
```

## Tax procedure lifecycle

```text
Return / Position
      -> Assessment
      -> Reconciliation
      -> Difference classification
      -> Correction / Objection
      -> Audit / Negotiation
      -> Litigation interface
      -> Closure
```

## Professional authority model

- **T0** – autonomous preparation: facts, research, calculations, scenarios, drafts, reconciliation.
- **T1** – client/management authority: objective, option and risk decision.
- **T2** – authorised Tax Professional validation/action where required.
- **T3** – tax authority/court/external authority.

A T2/T3 gate does not end safe preparatory work.

## Universe relationships

Primary edges expected after repository generation:

- `tax-advisory-office` -> requires core Tax Office skills.
- `tax-specialist-router` -> routes to initial Tax Specialists.
- `tax-position-register` -> consumes `current-tax-context` and `decision-record`.
- `tax-structure-pattern-library` -> consumes `current-tax-context`.
- `professional-tax-knowledge-ingestion` -> consumes `research-to-evidence-note` and `current-tax-context`.
- `tax-legal-interface-specialist` -> requires `tax-advisory-office` and remains visible under Legal Specialist routing.
- `inheritance-gift-tax-specialist` <-> `german-inheritance-succession-law-specialist` through explicit Legal/Tax work orders, not shared ownership.

## Validation / generation note

Canonical source skills are added on the feature branch. Derived repository artifacts such as `docs/skill-capability-index.json`, OpenAI plugin materialisations and Obsidian `Skill Universe`/category pages must be regenerated using the repository's normal generators before merge. Generated artifacts should not be hand-maintained as the authoritative source.
