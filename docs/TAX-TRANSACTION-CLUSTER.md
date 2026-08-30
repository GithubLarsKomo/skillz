# Tax Transaction Cluster

## Purpose

The Tax Advisory Office transaction layer consists of three peer Tax Specialists:

- `reorganization-tax-specialist`
- `ma-tax-specialist`
- `transfer-pricing-specialist`

They extend the foundation without turning `tax-advisory-office` or `tax-specialist-router` into substantive tax engines.

## Ownership model

- Reorganization Tax owns tax treatment of transformations, contributions, value approaches, lock-up periods and tax sequence constraints.
- M&A Tax owns Tax DD, buyer/seller deal-tax economics, Share-vs-Asset comparison, tax attributes and tax-related deal constraints.
- Transfer Pricing owns arm's-length analysis, functional/risk analysis, method selection, benchmarking requirements and TP documentation.
- Legal owns contracts, corporate-law mechanics, transaction documents and legal effectiveness.
- Accounting owns accounting facts.
- Valuation owns valuations and valuation methodology where a separate valuation opinion is required.
- Authorized Tax Professionals own reserved individualized professional acts and sign-offs through `tax-professional-routing`.

## Cross-routing

Typical integrated flow:

`tax-advisory-office` -> `tax-specialist-router` -> M&A Tax + Reorganization Tax + Transfer Pricing as needed -> `tax-position-register` / `tax-structure-pattern-library` -> `tax-legal-interface-specialist` -> Legal mechanism -> `tax-matter-final-gate`.

Specialists may run in parallel. Shared facts, periods and entity maps must reconcile before integrated advice is marked resolved.

## JUHN role

JUHN website and `@juhnsteuerberater` remain prioritized Practitioner/Discovery seed sources for Holding, Reorganization, M&A and Transfer-Pricing patterns, case sequences, warnings and practitioner heuristics. They are not authority for a material rule, benchmark or individualized Tax Position. Material claims are verified through `current-tax-context` against current primary/authoritative sources.

## Current authority examples

The cluster is designed to use current official sources rather than hard-code transient rules. For Transfer Pricing this includes the current German arm's-length rule, current BMF transfer-pricing guidance and applicable OECD material. Reorganization and M&A rules are likewise resolved by period through current law, administration and case law.

## Remaining explicit capability gaps

- `real-estate-tax-specialist`
- `employment-payroll-tax-specialist`
- `partnership-tax-specialist`
- `nonprofit-association-tax-specialist`

These remain explicit work orders/gaps until their own specialists exist.