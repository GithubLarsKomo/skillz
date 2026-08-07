# Capability Health

Generated from the canonical skill capability index. Do not edit manually.

## Summary

- Skills: **102**
- User-facing entrypoints: **84**
- Evaluation suites: **102**
- Skills without evaluation suite: **0**
- User-facing entrypoints without evaluation suite: **0**
- Ambiguous outputs (multiple producers): **0**
- Outputs without inferred hard-requires consumers: **130**

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
- `audit-finding-response-map.json` — producer: `audit-inspection-finding-response`
- `beta-readiness.json` — producer: `project-beta-readiness`
- `beta-readiness.md` — producer: `project-beta-readiness`
- `beta-runbook.md` — producer: `project-beta-readiness`
- `cdx-consultation-readiness.json` — producer: `ivdr-companion-diagnostic-consultation`
- `cdx-medicinal-product-linkage.json` — producer: `ivdr-companion-diagnostic-consultation`
- `cdx-scope-assessment.json` — producer: `ivdr-companion-diagnostic-consultation`
- `change-integration-status.json` — producer: `regulatory-change-impact-orchestrator`
- `claim-conflicts.json` — producer: `regulatory-claims-consistency`
- `claims-consistency-map.json` — producer: `regulatory-claims-consistency`
- `claims-remediation-plan.md` — producer: `regulatory-claims-consistency`
- `class-d-conformity-plan.json` — producer: `ivdr-class-d-conformity`
- `class-d-external-dependencies.json` — producer: `ivdr-class-d-conformity`
- `clinical-evidence-actions.json` — producer: `clinical-evidence-update-impact`
- `clinical-evidence-delta.json` — producer: `clinical-evidence-update-impact`
- `clinical-evidence-impact-map.json` — producer: `clinical-evidence-update-impact`
- `communication-profile.merged.json` — producer: `memory-sync-reconciliation`
- `conflict-residual-risk-handoff.json` — producer: `merge-conflict-resolution`
- `conflict-resolution-evidence.json` — producer: `merge-conflict-resolution`
- `containment-actions.json` — producer: `nonconformance-mrb-disposition`
- `correction-removal-action-plan.json` — producer: `fda-corrections-removals`
- `correction-removal-assessment.json` — producer: `fda-corrections-removals`
- `correction-removal-reporting-state.json` — producer: `fda-corrections-removals`
- `cybersecurity-evidence-map.json` — producer: `medical-device-cybersecurity-lifecycle`
- `cybersecurity-lifecycle-assessment.json` — producer: `medical-device-cybersecurity-lifecycle`
- `cybersecurity-postmarket-actions.json` — producer: `medical-device-cybersecurity-lifecycle`
- `de-novo-risk-control-rationale.md` — producer: `fda-de-novo-special-controls`
- `decision-follow-up-register.json` — producer: `decision-and-follow-up-tracker`
- `decision-follow-up-register.md` — producer: `decision-and-follow-up-tracker`
- `docs/agents/CONFIG.md` — producer: `repository-skill-bootstrap`
- `docs/agents/CONTEXT.md` — producer: `repository-skill-bootstrap`
- `docs/agents/DECISIONS.md` — producer: `repository-skill-bootstrap`
- `domain-change-plan.md` — producer: `domain-model-maintenance`
- `domain-model-map.json` — producer: `domain-model-maintenance`
- `domain-validation.json` — producer: `domain-model-maintenance`
- `dpia-decision.json` — producer: `medical-device-privacy-gdpr-bdsg`
- `dual-510k-clia-strategy.json` — producer: `fda-dual-510k-clia-waiver`
- `dual-evidence-package.json` — producer: `fda-dual-510k-clia-waiver`
- `dual-study-evidence-map.json` — producer: `fda-dual-510k-clia-waiver`
- `eudamed-readiness.json` — producer: `eudamed-udi-ivd`
- `execution plan` — producer: `synapse-orchestrator`
- `expert handoff` — producer: `synapse-orchestrator`
- `fda-acceptance-preflight.json` — producer: `fda-acceptance-readiness`
- `fda-device-listing-readiness.json` — producer: `fda-registration-listing-udi`
- `fda-registration-readiness.json` — producer: `fda-registration-listing-udi`
- `fda-request-issue-map.json` — producer: `fda-additional-information-response`
- `fda-response-package.md` — producer: `fda-additional-information-response`
- `finding-action-plan.json` — producer: `audit-inspection-finding-response`
- `finding-closure-status.json` — producer: `audit-inspection-finding-response`
- `gudid-udi-readiness.json` — producer: `fda-registration-listing-udi`
- `human-procedure-plan.md` — producer: `human-procedure-wizard`
- `human-procedure-result.json` — producer: `human-procedure-wizard`
- `import verification` — producer: `openasr-offline-model-import`
- `inhouse-ivd-condition-map.json` — producer: `ivdr-inhouse-health-institution`
- `inhouse-ivd-eligibility.json` — producer: `ivdr-inhouse-health-institution`
- `inhouse-ivd-transition-readiness.json` — producer: `ivdr-inhouse-health-institution`
- `inspection-evidence-index.json` — producer: `fda-qmsr-inspection-readiness`
- `installed OpenASR model` — producer: `openasr-offline-model-import`
- `isms-audit-findings.json` — producer: `iso27001-isms-audit`
- `isms-audit-plan.json` — producer: `iso27001-isms-audit`
- `isms-audit-report.md` — producer: `iso27001-isms-audit`
- `ivd-udi-data-set.json` — producer: `eudamed-udi-ivd`
- `ivdr-pms-assessment.json` — producer: `ivdr-pms-vigilance`
- `lifecycle-impact-gates.json` — producer: `regulatory-change-impact-orchestrator`
- `management-review-actions.json` — producer: `qms-management-review-governance`
- `management-review-brief.json` — producer: `qms-management-review-governance`
- `management-review-brief.md` — producer: `qms-management-review-governance`
- `mdsap-audit-scope.json` — producer: `mdsap-audit-readiness`
- `mdsap-evidence-gaps.json` — producer: `mdsap-audit-readiness`
- `mdsap-task-readiness.json` — producer: `mdsap-audit-readiness`
- `measurement-capability-study.json` — producer: `measurement-system-validation`
- `measurement-evidence-gaps.json` — producer: `measurement-system-validation`
- `measurement-system-assessment.json` — producer: `measurement-system-validation`
- `memory-ledger.merged.json` — producer: `memory-sync-reconciliation`
- `memory-reconciliation-plan.json` — producer: `memory-sync-reconciliation`
- `mrb-disposition-decision.json` — producer: `nonconformance-mrb-disposition`
- `nonconformance-assessment.json` — producer: `nonconformance-mrb-disposition`
- `obsidian-candidate.json` — producer: `obsidian-adapter`
- `obsidian-map.canvas` — producer: `obsidian-adapter`
- `obsidian-note.md` — producer: `obsidian-adapter`
- `obsidian-view.base` — producer: `obsidian-adapter`
- `opaque-analysis-evidence.md` — producer: `opaque-system-analysis`
- `pccp-applicability.json` — producer: `fda-pccp-change-control`
- `pccp-change-evidence.json` — producer: `fda-pccp-change-control`
- `pccp-deviation-routing.json` — producer: `fda-pccp-change-control`
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
- `regulatory-change-events.json` — producer: `regulatory-change-monitoring`
- `regulatory-change-route-map.json` — producer: `regulatory-change-impact-orchestrator`
- `regulatory-change-watch-status.json` — producer: `regulatory-change-monitoring`
- `regulatory-source-register.json` — producer: `regulatory-change-monitoring`
- `regulatory-strategy.json` — producer: `medical-device-regulatory-strategy`
- `regulatory-strategy.md` — producer: `medical-device-regulatory-strategy`
- `regulatory-wayfinding-handoff.json` — producer: `medical-device-regulatory-strategy`
- `remaining-unknowns.json` — producer: `opaque-system-analysis`
- `resolved-change-brief.md` — producer: `merge-conflict-resolution`
- `response-evidence-matrix.json` — producer: `fda-additional-information-response`
- `source-context.json` — producer: `source-to-context`
- `source-context.md` — producer: `source-to-context`
- `special-controls-matrix.json` — producer: `fda-de-novo-special-controls`
- `stakeholder-questionnaire.json` — producer: `external-stakeholder-questionnaire`
- `stakeholder-questionnaire.md` — producer: `external-stakeholder-questionnaire`
- `supplier-control-plan.json` — producer: `supplier-quality-medical-device`
- `supplier-quality-assessment.json` — producer: `supplier-quality-medical-device`
- `supplier-signal-set.json` — producer: `supplier-quality-medical-device`
- `synchronization manifest` — producer: `central-skill-repository-curation`
- `trend-signal-set.json` — producer: `ivdr-pms-vigilance`
- `ui-prototype-plan.md` — producer: `project-beta-readiness`
- `updated skill repository` — producer: `central-skill-repository-curation`
- `usability-engineering-assessment.json` — producer: `iec62366-usability-engineering`
- `usability-evidence-gaps.json` — producer: `iec62366-usability-engineering`
- `use-related-risk-evidence.json` — producer: `iec62366-usability-engineering`
- `vigilance-decision-log.json` — producer: `ivdr-pms-vigilance`

## Interpretation

A true orphan requires additional evidence that an output was intended for downstream machine consumption but has no valid consumer. Absence of a hard dependency alone is insufficient to make that claim.
