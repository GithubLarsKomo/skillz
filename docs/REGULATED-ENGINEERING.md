# Regulated Engineering Extension

This extension adds a clean-room Medical Device & Quality domain layer to the existing engineering skill graph. The donor repository `borghei/Claude-Skills` was used only as a workflow inventory; no donor scripts or skill text are copied.

## Architecture

`round-based-requirements-grilling -> regulated-product-context -> domain specialists -> compliance traceability -> large-work-wayfinder/conversation-to-spec -> engineering -> domain review/audit -> causal investigation/CAPA -> risk/QMS feedback`.

Wayfinder remains the owner of exploration, dependencies and sequencing. Grilling remains the owner of iterative requirements elicitation. Domain skills own only their regulated semantics.

## Regulated Product Grilling pack

The reusable six-round source pack is maintained in `GithubLarsKomo/grilling` at `site/packs/regulated-product-baseline-v1/`. It is deliberately not registered as an active grilling. A concrete project can instantiate immutable round definitions with:

```bash
python scripts/instantiate_regulated_product_pack.py \
  --project-id my-device \
  --project-title "My Device" \
  --output-dir /tmp/my-device-rounds
```

Instantiation verifies the committed template hashes and produces project-specific round IDs and definition hashes, but never mutates `site/catalog.json`. Catalog registration remains a separate explicit project action. The pack covers Product/Intended Purpose, markets and classification hypotheses, QMS/design/production/suppliers, risk/post-market, clinical/performance evidence, and software/cybersecurity/privacy/AI. Its AI section supplements rather than replaces the generic AI/ML-readiness rules in `round-based-requirements-grilling`.

The pack's output groups map to `contracts/regulated-product-baseline-v1.schema.json`; `regulated-product-context` then normalizes confirmed results for downstream domain skills.

## Current regulatory anchors (as of 2026-08-04)

- FDA QMSR: https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr — effective 2026-02-02; Part 820 incorporates ISO 13485:2016 by reference.
- FDA IVD overview: https://www.fda.gov/medical-devices/ivd-regulatory-assistance/overview-ivd-regulation
- EU MDR 2017/745: https://eur-lex.europa.eu/eli/reg/2017/745/oj
- EU IVDR 2017/746: https://eur-lex.europa.eu/eli/reg/2017/746/oj
- ISO 13485:2016 overview: https://www.iso.org/standard/59752.html
- ISO 14971:2019 overview: https://www.iso.org/standard/72704.html (reviewed/confirmed in 2025).

Volatile fees, review targets, transition rules, EUDAMED implementation, guidance revisions and authority policy are never stored as timeless skill constants.

## Foundation

- `regulated-product-context`
- `evidence-based-causal-investigation`
- `two-axis-compliance-review`
- `regulatory-source-evidence-v1`
- `compliance-traceability-v1`
- `regulated-product-baseline-v1`

## Domain skills

1. `medical-device-risk-management-iso14971`
2. `medical-device-qms-iso13485`
3. `controlled-quality-documentation`
4. `medical-device-capa`
5. `eu-mdr-ivdr-regulatory-specialist`
6. `fda-medical-device-ivd-regulatory-specialist`
7. `medical-device-isms-governance`
8. `medical-device-privacy-gdpr-bdsg`
9. `iso13485-qms-audit`
10. `iso27001-isms-audit`
11. `qms-management-review-governance`
12. `medical-device-regulatory-strategy`

## Non-negotiable constraints

No checklist-only compliance claim; no agent-created authority decision; no mandatory 5x5/RPN/ALARP method unless organizationally adopted; no universal audit sample/frequency/finding class; no universal CAPA recurrence threshold; no fixed document numbering; no static FDA fees/review times; no silent MDR/IVDR mixing; no regex-derived privacy compliance score.
