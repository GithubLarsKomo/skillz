# Legal & Compliance Office – Coverage and Migration Map

Status: 2026-08-28  
Branch: `feat/legal-compliance-office-foundation`

## Repository health at this checkpoint

- Canonical skills: **251**
- User-facing entrypoints: **220**
- Evaluation suites: **245**
- Legal/Compliance skills added or materially migrated in this branch: all have evaluation suites and recorded Happy/Edge/Failure baselines.
- The six remaining repository-wide evaluation gaps are presentation-workflow capabilities and are outside the Legal/Compliance scope.
- Final Legal/Compliance validation passed dependency-contract tests, metadata-schema tests, OpenAI metadata materialisation, repository metadata generation, OpenAI plugin build, reproducibility checks, Obsidian generation, repository validation and all skill evaluation suites.

## Migration policy

The Legal & Compliance Office is a **thin orchestration and specialist-routing layer**. Existing deep capabilities are reused instead of copied. A skill is only replaced when its original abstraction is materially wrong; otherwise migration is performed through `upgrade`, `alias/compatibility`, or `keep/reuse`.

### KEEP / REUSE

The following existing capability families remain authoritative in their domain and are consumed or routed to by the Legal Office:

- MDR/IVDR/FDA regulatory specialists and regulatory strategy.
- Regulatory change monitoring and impact orchestration for Medical-Device/IVD-specific change.
- QMS, ISO 13485, CAPA, complaint, vigilance, field action, supplier quality and risk-management specialists.
- ISMS, ISO 27001, medical-device cybersecurity and software/product technical specialists.
- Patent landscape, biopatent deep analysis and FTO assessment.
- `research-to-evidence-note` and evidence/traceability primitives.
- `round-based-requirements-grilling` for decision/fact uncertainty.
- controlled documentation, precision writing and fidelity verification.
- generic project, engineering, knowledge, learning, presentation and sport capabilities unless a Legal work order explicitly consumes their output.

These skills are **not absorbed into Legal**. Legal owns the legal question; the domain specialist retains the technical/regulatory/quality/scientific question.

### UPGRADE

Existing capabilities materially upgraded or integrated into the Legal architecture:

- `contract-workflow` → compatibility entrypoint into the new Contract Matter architecture.
- `contract-legal-context` → compatibility/legal-context layer aligned with `current-law-context`.
- `contract-review` → client-objective, risk, specialist-overlay and negotiation-aware review.
- `contract-drafting` → deal-model/clause-coverage based drafting with current-law and final-gate integration.
- `legal-specialist-router` → expanded from core corporate fields to complete enterprise/private routing.
- `legal-compliance-office` → expanded from matter orchestration to ongoing Legal/Compliance operating system.
- `private-legal-matter-router` → now routes to dedicated private-law specialists instead of broad capability gaps.
- `decision-record` integration → significant Legal/Compliance decisions preserve authority, evidence, alternatives and supersession rather than being hidden inside narrative advice.

### ALIAS / COMPATIBILITY

Compatibility is preferred over deletion where existing user prompts or dependent skills may still call legacy names.

- `contract-workflow` remains a supported front door; the canonical architecture is the Contract Matter / Legal Matter stack.
- `contract-legal-context` remains available for contract-specific callers while broader matters use `current-law-context`.
- Medical-Device/IVD privacy, regulatory change, cybersecurity and quality specialists remain sector overlays instead of being renamed into generic Legal skills.

### NEW – Core Legal Office

- `legal-compliance-office`
- `legal-matter-intake`
- `legal-client-strategy`
- `legal-matter-wayfinder`
- `current-law-context`
- `legal-specialist-router`
- `legal-compliance-risk-assessment`
- `privilege-and-counsel-routing`
- `legal-matter-final-gate`
- `executive-legal-compliance-governance`
- `legal-change-monitoring`
- `legal-change-impact-orchestrator`

### NEW – Contract / Deal System

- `contract-matter-workflow`
- `agreement-type-analysis`
- `legal-negotiation-strategy`
- `legal-redline-review-loop`
- agreement overlays for confidentiality/NDA, MTA, DTA/DUA, IP licensing, R&D/collaboration, supply/manufacturing and quality/regulatory contexts.

### NEW – Compliance / Investigation System

- `compliance-obligation-register`
- `compliance-control-mapping`
- `compliance-control-assurance`
- `compliance-management-workflow`
- `whistleblowing-law-specialist`
- `investigation-evidence-preservation`
- `internal-investigation-workflow`
- `investigation-findings-remediation`

### NEW – Enterprise Legal Specialists

- `german-employment-labor-law-specialist`
- `corporate-governance-law-specialist`
- `corporate-transactions-ma-specialist`
- `finance-insolvency-restructuring-law-specialist`
- `corporate-compliance-law-specialist`
- `public-procurement-healthcare-law-specialist`
- `esg-supply-chain-environmental-law-specialist`
- `digital-ai-cyber-law-specialist`
- `privacy-data-law-specialist`
- `ip-licensing-law-specialist`
- `competition-antitrust-law-specialist`
- `trade-sanctions-export-control-specialist`
- `product-liability-safety-law-specialist`
- `dispute-litigation-strategy-specialist`
- `tax-legal-interface-specialist`
- `real-estate-law-specialist`
- `german-association-law-specialist`
- `german-sports-law-specialist`
- `german-rowing-sport-law-specialist`

### NEW – Private Matter Specialists

- `private-legal-matter-router`
- `german-family-law-specialist`
- `german-inheritance-succession-law-specialist`
- `german-consumer-insurance-private-contract-law-specialist`
- `german-criminal-administrative-offence-procedure-specialist`
- `german-administrative-social-traffic-law-specialist`

## Coverage matrix

| Matter domain | Primary owner | Required overlays / handoffs | Coverage state |
|---|---|---|---|
| Commercial contracts | Contract Matter Stack | Current Law, risk, negotiation, relevant domain specialist | covered |
| Employment / labour / works council | `german-employment-labor-law-specialist` | Privacy, investigations, corporate, tax/social interfaces | covered |
| Corporate governance / board / authority | `corporate-governance-law-specialist` | Decision Record, risk, M&A/finance as triggered | covered |
| M&A / transactions | `corporate-transactions-ma-specialist` | Antitrust, employment, IP, privacy, regulatory, tax, finance | covered |
| Finance / security / distress / insolvency | `finance-insolvency-restructuring-law-specialist` | Governance, Tax, finance/accounting/valuation, counsel | covered |
| IP ownership / licensing | `ip-licensing-law-specialist` | Patent landscape, biopatent, FTO, antitrust | covered |
| Privacy / data | `privacy-data-law-specialist` | Medical-device privacy overlay, digital/cyber, employment | covered |
| Digital / AI / cyber / Data Act / NIS2 | `digital-ai-cyber-law-specialist` | Privacy, ISMS, cyber technical, regulatory, contract | covered |
| Competition / merger control | `competition-antitrust-law-specialist` | M&A, IP, procurement, contracts | covered |
| Integrity / anti-corruption / third parties | `corporate-compliance-law-specialist` | Obligation/control, investigation, employment, criminal/counsel | covered |
| Whistleblowing / investigations | Whistleblowing + Investigation stack | Employment, privacy, compliance, privilege/counsel | covered |
| Trade / sanctions / export | `trade-sanctions-export-control-specialist` | Contract, IP, regulatory, scientific/technical classification | covered |
| Public procurement / healthcare tenders | `public-procurement-healthcare-law-specialist` | Antitrust, compliance, contract, regulatory | covered |
| ESG / supply chain / environment | `esg-supply-chain-environmental-law-specialist` | Supplier quality, controls, reporting, contract | covered |
| Product liability / safety | `product-liability-safety-law-specialist` | Regulatory/vigilance, risk/CAPA, litigation | covered |
| Litigation / disputes | `dispute-litigation-strategy-specialist` | Matter specialist, preservation, counsel | covered for strategy/preparation; representation gated |
| Tax legal dependencies | `tax-legal-interface-specialist` | authorised Tax Professional for substantive tax position | covered as interface; reserved professional work gated |
| Real estate | `real-estate-law-specialist` | Tax, notary, finance, corporate | covered; notarial acts gated |
| Regulatory / IVDR / FDA | existing regulatory specialist system | Legal specialist only for horizontal legal questions | covered by reuse |
| QMS / CAPA / complaints / vigilance | existing quality/regulatory system | Legal only for liability/enforcement/contract overlays | covered by reuse |
| Family | `german-family-law-specialist` | Real estate, tax, professional/court gate | covered |
| Inheritance / succession | `german-inheritance-succession-law-specialist` | Corporate, real estate, tax, notary/probate | covered |
| Consumer / insurance / private contracts | `german-consumer-insurance-private-contract-law-specialist` | Litigation, privacy, real estate, product liability | covered |
| Criminal / OWi / investigation procedure | `german-criminal-administrative-offence-procedure-specialist` | Evidence preservation, privilege/counsel, employment/corporate if relevant | covered for analysis/preparation; defence/representation gated |
| Administrative / social / traffic public law | `german-administrative-social-traffic-law-specialist` | Expert evidence, criminal/OWi, professional/court gate | covered |
| Association / sport / rowing | association + sports-law overlays | Investigation, employment, privacy as triggered | covered |

## External-authority boundaries

The target is **operational replacement of routine Legal/Compliance work**, not fictional replacement of legally reserved or external authority functions.

- L0 – autonomous preparation: intake, research, evidence mapping, drafting, review, monitoring, control mapping, issue spotting and work-order generation.
- L1 – internal executive authority: material commercial/risk acceptance and management decisions.
- L2 – specialist validation: deep internal Regulatory/IP/Tax/technical or other specialised expertise.
- L3 – qualified external authority/professional: court/authority representation, notarial acts, formal criminal defence, reserved tax advice, foreign-law opinions where required, high-critical privilege or specialist opinions.

An L3 gate does **not** stop preparatory work. The Legal Office should continue to build the evidence package, issue tree, draft, options, risk analysis and tightly scoped professional brief.

## Current-law principle

No legal specialist treats remembered law, old checklists or static thresholds as authoritative. Every material conclusion is bound to jurisdiction, source class, effective/applicable date and `asOf`. Time-sensitive regimes are routed through `legal-change-monitoring` and current official/primary sources.

## Remaining non-Legal repository gaps

The generated repository health report currently identifies six evaluation-suite gaps, all in presentation/template presentation capabilities. They are not Legal/Compliance coverage gaps and are intentionally not repaired in this Legal branch.

## Merge gate

Before merge into `main`:

1. reconcile branch with current `main`,
2. resolve generated-artifact conflicts by regenerating from canonical skills rather than hand-merging generated files,
3. rerun the complete metadata/plugin/Obsidian/repository/evaluation pipeline,
4. confirm no Legal/Compliance evaluation gaps,
5. update PR scope/status and only then mark ready for merge.
