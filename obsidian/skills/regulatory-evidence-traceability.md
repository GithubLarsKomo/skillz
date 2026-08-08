---
type: skill
generated: true
name: "regulatory-evidence-traceability"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/regulatory-evidence-traceability/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# regulatory-evidence-traceability

Verwandelt regulatorische Quellen, Verpflichtungen und ausdrücklich markierte Interpretationen in stabile Requirement-to-Evidence-Verknüpfungen mit Provenance, Freshness und Gap-Status. Verwenden als gemeinsamen Evidence-Kern für EU-/FDA-/QMS-Spezialisten; der Skill entscheidet selbst weder Compliance noch Klassifikation oder Zulassung.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/research-to-evidence-note|research-to-evidence-note]]

## Required by

- [[skills/audit-inspection-finding-response|audit-inspection-finding-response]]
- [[skills/clinical-evidence-update-impact|clinical-evidence-update-impact]]
- [[skills/design-change-regulatory-impact|design-change-regulatory-impact]]
- [[skills/eudamed-udi-ivd|eudamed-udi-ivd]]
- [[skills/fda-510k-predicate-strategy|fda-510k-predicate-strategy]]
- [[skills/fda-510k-substantial-equivalence|fda-510k-substantial-equivalence]]
- [[skills/fda-acceptance-readiness|fda-acceptance-readiness]]
- [[skills/fda-additional-information-response|fda-additional-information-response]]
- [[skills/fda-complaint-mdr-reportability|fda-complaint-mdr-reportability]]
- [[skills/fda-de-novo-special-controls|fda-de-novo-special-controls]]
- [[skills/fda-de-novo-strategy|fda-de-novo-strategy]]
- [[skills/fda-device-classification-product-code|fda-device-classification-product-code]]
- [[skills/fda-dual-510k-clia-waiver|fda-dual-510k-clia-waiver]]
- [[skills/fda-estar-submission-builder|fda-estar-submission-builder]]
- [[skills/fda-ivd-clia-waiver|fda-ivd-clia-waiver]]
- [[skills/fda-pccp-change-control|fda-pccp-change-control]]
- [[skills/fda-qmsr-iso13485-gap|fda-qmsr-iso13485-gap]]
- [[skills/fda-qsub-strategy|fda-qsub-strategy]]
- [[skills/fda-recall-status-termination|fda-recall-status-termination]]
- [[skills/fda-registration-listing-udi|fda-registration-listing-udi]]
- [[skills/ivdr-analytical-performance|ivdr-analytical-performance]]
- [[skills/ivdr-class-d-conformity|ivdr-class-d-conformity]]
- [[skills/ivdr-clinical-performance-study|ivdr-clinical-performance-study]]
- [[skills/ivdr-companion-diagnostic-consultation|ivdr-companion-diagnostic-consultation]]
- [[skills/ivdr-device-classification|ivdr-device-classification]]
- [[skills/ivdr-economic-operator-postmarket-propagation|ivdr-economic-operator-postmarket-propagation]]
- [[skills/ivdr-field-safety-corrective-action|ivdr-field-safety-corrective-action]]
- [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]
- [[skills/ivdr-inhouse-health-institution|ivdr-inhouse-health-institution]]
- [[skills/ivdr-performance-evaluation|ivdr-performance-evaluation]]
- [[skills/ivdr-performance-evaluation-report|ivdr-performance-evaluation-report]]
- [[skills/ivdr-pmpf|ivdr-pmpf]]
- [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
- [[skills/ivdr-scientific-validity|ivdr-scientific-validity]]
- [[skills/mdcg-guidance-navigator|mdcg-guidance-navigator]]
- [[skills/mdsap-audit-readiness|mdsap-audit-readiness]]
- [[skills/medical-device-adverse-event-coding|medical-device-adverse-event-coding]]
- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]
- [[skills/medical-device-labeling-ifu|medical-device-labeling-ifu]]
- [[skills/medical-device-pms-system|medical-device-pms-system]]
- [[skills/regulatory-change-impact-orchestrator|regulatory-change-impact-orchestrator]]
- [[skills/regulatory-change-monitoring|regulatory-change-monitoring]]
- [[skills/regulatory-claims-consistency|regulatory-claims-consistency]]

## Outputs

- `regulatory-evidence-gaps.json`
- `regulatory-evidence-map.json`

## Output consumers

### `regulatory-evidence-gaps.json`

- [[skills/audit-inspection-finding-response|audit-inspection-finding-response]]
- [[skills/clinical-evidence-update-impact|clinical-evidence-update-impact]]
- [[skills/design-change-regulatory-impact|design-change-regulatory-impact]]
- [[skills/eudamed-udi-ivd|eudamed-udi-ivd]]
- [[skills/fda-510k-predicate-strategy|fda-510k-predicate-strategy]]
- [[skills/fda-510k-substantial-equivalence|fda-510k-substantial-equivalence]]
- [[skills/fda-acceptance-readiness|fda-acceptance-readiness]]
- [[skills/fda-additional-information-response|fda-additional-information-response]]
- [[skills/fda-complaint-mdr-reportability|fda-complaint-mdr-reportability]]
- [[skills/fda-de-novo-special-controls|fda-de-novo-special-controls]]
- [[skills/fda-de-novo-strategy|fda-de-novo-strategy]]
- [[skills/fda-device-classification-product-code|fda-device-classification-product-code]]
- [[skills/fda-dual-510k-clia-waiver|fda-dual-510k-clia-waiver]]
- [[skills/fda-estar-submission-builder|fda-estar-submission-builder]]
- [[skills/fda-ivd-clia-waiver|fda-ivd-clia-waiver]]
- [[skills/fda-pccp-change-control|fda-pccp-change-control]]
- [[skills/fda-qmsr-iso13485-gap|fda-qmsr-iso13485-gap]]
- [[skills/fda-qsub-strategy|fda-qsub-strategy]]
- [[skills/fda-recall-status-termination|fda-recall-status-termination]]
- [[skills/fda-registration-listing-udi|fda-registration-listing-udi]]
- [[skills/ivdr-analytical-performance|ivdr-analytical-performance]]
- [[skills/ivdr-class-d-conformity|ivdr-class-d-conformity]]
- [[skills/ivdr-clinical-performance-study|ivdr-clinical-performance-study]]
- [[skills/ivdr-companion-diagnostic-consultation|ivdr-companion-diagnostic-consultation]]
- [[skills/ivdr-device-classification|ivdr-device-classification]]
- [[skills/ivdr-economic-operator-postmarket-propagation|ivdr-economic-operator-postmarket-propagation]]
- [[skills/ivdr-field-safety-corrective-action|ivdr-field-safety-corrective-action]]
- [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]
- [[skills/ivdr-inhouse-health-institution|ivdr-inhouse-health-institution]]
- [[skills/ivdr-performance-evaluation|ivdr-performance-evaluation]]
- [[skills/ivdr-performance-evaluation-report|ivdr-performance-evaluation-report]]
- [[skills/ivdr-pmpf|ivdr-pmpf]]
- [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
- [[skills/ivdr-scientific-validity|ivdr-scientific-validity]]
- [[skills/mdcg-guidance-navigator|mdcg-guidance-navigator]]
- [[skills/mdsap-audit-readiness|mdsap-audit-readiness]]
- [[skills/medical-device-adverse-event-coding|medical-device-adverse-event-coding]]
- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]
- [[skills/medical-device-labeling-ifu|medical-device-labeling-ifu]]
- [[skills/medical-device-pms-system|medical-device-pms-system]]
- [[skills/regulatory-change-impact-orchestrator|regulatory-change-impact-orchestrator]]
- [[skills/regulatory-change-monitoring|regulatory-change-monitoring]]
- [[skills/regulatory-claims-consistency|regulatory-claims-consistency]]

### `regulatory-evidence-map.json`

- [[skills/audit-inspection-finding-response|audit-inspection-finding-response]]
- [[skills/clinical-evidence-update-impact|clinical-evidence-update-impact]]
- [[skills/design-change-regulatory-impact|design-change-regulatory-impact]]
- [[skills/eudamed-udi-ivd|eudamed-udi-ivd]]
- [[skills/fda-510k-predicate-strategy|fda-510k-predicate-strategy]]
- [[skills/fda-510k-substantial-equivalence|fda-510k-substantial-equivalence]]
- [[skills/fda-acceptance-readiness|fda-acceptance-readiness]]
- [[skills/fda-additional-information-response|fda-additional-information-response]]
- [[skills/fda-complaint-mdr-reportability|fda-complaint-mdr-reportability]]
- [[skills/fda-de-novo-special-controls|fda-de-novo-special-controls]]
- [[skills/fda-de-novo-strategy|fda-de-novo-strategy]]
- [[skills/fda-device-classification-product-code|fda-device-classification-product-code]]
- [[skills/fda-dual-510k-clia-waiver|fda-dual-510k-clia-waiver]]
- [[skills/fda-estar-submission-builder|fda-estar-submission-builder]]
- [[skills/fda-ivd-clia-waiver|fda-ivd-clia-waiver]]
- [[skills/fda-pccp-change-control|fda-pccp-change-control]]
- [[skills/fda-qmsr-iso13485-gap|fda-qmsr-iso13485-gap]]
- [[skills/fda-qsub-strategy|fda-qsub-strategy]]
- [[skills/fda-recall-status-termination|fda-recall-status-termination]]
- [[skills/fda-registration-listing-udi|fda-registration-listing-udi]]
- [[skills/ivdr-analytical-performance|ivdr-analytical-performance]]
- [[skills/ivdr-class-d-conformity|ivdr-class-d-conformity]]
- [[skills/ivdr-clinical-performance-study|ivdr-clinical-performance-study]]
- [[skills/ivdr-companion-diagnostic-consultation|ivdr-companion-diagnostic-consultation]]
- [[skills/ivdr-device-classification|ivdr-device-classification]]
- [[skills/ivdr-economic-operator-postmarket-propagation|ivdr-economic-operator-postmarket-propagation]]
- [[skills/ivdr-field-safety-corrective-action|ivdr-field-safety-corrective-action]]
- [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]
- [[skills/ivdr-inhouse-health-institution|ivdr-inhouse-health-institution]]
- [[skills/ivdr-performance-evaluation|ivdr-performance-evaluation]]
- [[skills/ivdr-performance-evaluation-report|ivdr-performance-evaluation-report]]
- [[skills/ivdr-pmpf|ivdr-pmpf]]
- [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]
- [[skills/ivdr-scientific-validity|ivdr-scientific-validity]]
- [[skills/mdcg-guidance-navigator|mdcg-guidance-navigator]]
- [[skills/mdsap-audit-readiness|mdsap-audit-readiness]]
- [[skills/medical-device-adverse-event-coding|medical-device-adverse-event-coding]]
- [[skills/medical-device-complaint-regulatory-routing|medical-device-complaint-regulatory-routing]]
- [[skills/medical-device-labeling-ifu|medical-device-labeling-ifu]]
- [[skills/medical-device-pms-system|medical-device-pms-system]]
- [[skills/regulatory-change-impact-orchestrator|regulatory-change-impact-orchestrator]]
- [[skills/regulatory-change-monitoring|regulatory-change-monitoring]]
- [[skills/regulatory-claims-consistency|regulatory-claims-consistency]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/regulatory-evidence-traceability/SKILL.md`
