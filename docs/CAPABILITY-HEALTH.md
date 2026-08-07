# Capability Health

Generated from the canonical skill capability index. Do not edit manually.

## Summary

- Skills: **78**
- User-facing entrypoints: **60**
- Evaluation suites: **78**
- Skills without evaluation suite: **0**
- User-facing entrypoints without evaluation suite: **0**
- Ambiguous outputs (multiple producers): **0**
- Outputs without inferred hard-requires consumers: **89**

## Evaluation gaps

None.

### User-facing evaluation gaps

None.

## Ambiguous outputs

None.

## Outputs without inferred consumers

These are **not automatically defects**. The dependency graph infers consumers only from hard `requires` edges. User-facing reports, installed artifacts, runbooks, exported notes and other terminal products are expected to appear here. Treat this list as a review queue, not as an orphan verdict.

- `GRILL-REPORT.md` — producer: `round-based-requirements-grilling`
- `acceptance-gaps.json` — producer: `fda-acceptance-readiness`
- `approved SPEC.md` — producer: `round-based-requirements-grilling`
- `beta-readiness.json` — producer: `project-beta-readiness`
- `beta-readiness.md` — producer: `project-beta-readiness`
- `beta-runbook.md` — producer: `project-beta-readiness`
- `change-impact-assessment.json` — producer: `controlled-quality-documentation`
- `change-verification-needs.json` — producer: `design-change-regulatory-impact`
- `communication-profile.merged.json` — producer: `memory-sync-reconciliation`
- `conflict-residual-risk-handoff.json` — producer: `merge-conflict-resolution`
- `conflict-resolution-evidence.json` — producer: `merge-conflict-resolution`
- `controlled-document-plan.md` — producer: `controlled-quality-documentation`
- `de-novo-risk-control-rationale.md` — producer: `fda-de-novo-special-controls`
- `decision-follow-up-register.json` — producer: `decision-and-follow-up-tracker`
- `decision-follow-up-register.md` — producer: `decision-and-follow-up-tracker`
- `design-change-impact.json` — producer: `design-change-regulatory-impact`
- `docs/agents/CONFIG.md` — producer: `repository-skill-bootstrap`
- `docs/agents/CONTEXT.md` — producer: `repository-skill-bootstrap`
- `docs/agents/DECISIONS.md` — producer: `repository-skill-bootstrap`
- `document-control-assessment.json` — producer: `controlled-quality-documentation`
- `domain-change-plan.md` — producer: `domain-model-maintenance`
- `domain-model-map.json` — producer: `domain-model-maintenance`
- `domain-validation.json` — producer: `domain-model-maintenance`
- `dpia-decision.json` — producer: `medical-device-privacy-gdpr-bdsg`
- `execution plan` — producer: `synapse-orchestrator`
- `expert handoff` — producer: `synapse-orchestrator`
- `fda-acceptance-preflight.json` — producer: `fda-acceptance-readiness`
- `fda-request-issue-map.json` — producer: `fda-additional-information-response`
- `fda-response-package.md` — producer: `fda-additional-information-response`
- `human-procedure-plan.md` — producer: `human-procedure-wizard`
- `human-procedure-result.json` — producer: `human-procedure-wizard`
- `import verification` — producer: `openasr-offline-model-import`
- `inspection-evidence-index.json` — producer: `fda-qmsr-inspection-readiness`
- `installed OpenASR model` — producer: `openasr-offline-model-import`
- `isms-audit-findings.json` — producer: `iso27001-isms-audit`
- `isms-audit-plan.json` — producer: `iso27001-isms-audit`
- `isms-audit-report.md` — producer: `iso27001-isms-audit`
- `ivdr-classification-assessment.json` — producer: `ivdr-device-classification`
- `ivdr-classification-rationale.md` — producer: `ivdr-device-classification`
- `ivdr-pms-assessment.json` — producer: `ivdr-pms-vigilance`
- `management-review-actions.json` — producer: `qms-management-review-governance`
- `management-review-brief.json` — producer: `qms-management-review-governance`
- `management-review-brief.md` — producer: `qms-management-review-governance`
- `memory-ledger.merged.json` — producer: `memory-sync-reconciliation`
- `memory-reconciliation-plan.json` — producer: `memory-sync-reconciliation`
- `obsidian-candidate.json` — producer: `obsidian-adapter`
- `obsidian-map.canvas` — producer: `obsidian-adapter`
- `obsidian-note.md` — producer: `obsidian-adapter`
- `obsidian-view.base` — producer: `obsidian-adapter`
- `opaque-analysis-evidence.md` — producer: `opaque-system-analysis`
- `per-traceability.json` — producer: `ivdr-performance-evaluation-report`
- `performance-evaluation-report.md` — producer: `ivdr-performance-evaluation-report`
- `pmpf-evaluation-report.md` — producer: `ivdr-pmpf`
- `pmpf-plan.json` — producer: `ivdr-pmpf`
- `pmpf-signals.json` — producer: `ivdr-pmpf`
- `privacy-assessment.json` — producer: `medical-device-privacy-gdpr-bdsg`
- `privacy-governance.md` — producer: `medical-device-privacy-gdpr-bdsg`
- `process-validation-assessment.json` — producer: `process-validation-iq-oq-pq`
- `process-validation-protocol.md` — producer: `process-validation-iq-oq-pq`
- `process-validation-strategy.json` — producer: `process-validation-iq-oq-pq`
- `progress summary` — producer: `synapse-orchestrator`
- `qmsr-inspection-readiness.json` — producer: `fda-qmsr-inspection-readiness`
- `qsub-briefing-package.md` — producer: `fda-qsub-strategy`
- `qsub-commitments.json` — producer: `fda-qsub-strategy`
- `qsub-question-set.json` — producer: `fda-qsub-strategy`
- `recovered-system-model.json` — producer: `opaque-system-analysis`
- `regulatory-change-decisions.json` — producer: `design-change-regulatory-impact`
- `regulatory-strategy.json` — producer: `medical-device-regulatory-strategy`
- `regulatory-strategy.md` — producer: `medical-device-regulatory-strategy`
- `regulatory-wayfinding-handoff.json` — producer: `medical-device-regulatory-strategy`
- `remaining-unknowns.json` — producer: `opaque-system-analysis`
- `resolved-change-brief.md` — producer: `merge-conflict-resolution`
- `response-evidence-matrix.json` — producer: `fda-additional-information-response`
- `se-evidence-gaps.json` — producer: `fda-510k-substantial-equivalence`
- `source-context.json` — producer: `source-to-context`
- `source-context.md` — producer: `source-to-context`
- `special-controls-matrix.json` — producer: `fda-de-novo-special-controls`
- `stakeholder-questionnaire.json` — producer: `external-stakeholder-questionnaire`
- `stakeholder-questionnaire.md` — producer: `external-stakeholder-questionnaire`
- `substantial-equivalence-assessment.json` — producer: `fda-510k-substantial-equivalence`
- `substantial-equivalence-matrix.md` — producer: `fda-510k-substantial-equivalence`
- `supplier-control-plan.json` — producer: `supplier-quality-medical-device`
- `supplier-quality-assessment.json` — producer: `supplier-quality-medical-device`
- `supplier-signal-set.json` — producer: `supplier-quality-medical-device`
- `synchronization manifest` — producer: `central-skill-repository-curation`
- `trend-signal-set.json` — producer: `ivdr-pms-vigilance`
- `ui-prototype-plan.md` — producer: `project-beta-readiness`
- `updated skill repository` — producer: `central-skill-repository-curation`
- `vigilance-decision-log.json` — producer: `ivdr-pms-vigilance`

## Interpretation

A true orphan requires additional evidence that an output was intended for downstream machine consumption but has no valid consumer. Absence of a hard dependency alone is insufficient to make that claim.
