# Capability Health

Generated from the canonical skill capability index. Do not edit manually.

## Summary

- Skills: **198**
- User-facing entrypoints: **168**
- Evaluation suites: **192**
- Skills without evaluation suite: **6**
- User-facing entrypoints without evaluation suite: **6**
- Ambiguous outputs (multiple producers): **8**
- Outputs without inferred hard-requires consumers: **184**

## Evaluation gaps

- `euroimmun-presentation-workflow`
- `presentation-language-rewriter`
- `presentation-layout-qa`
- `presentation-render-verifier`
- `presentation-template-profiler`
- `template-presentation-workflow`

### User-facing evaluation gaps

- `euroimmun-presentation-workflow`
- `presentation-language-rewriter`
- `presentation-layout-qa`
- `presentation-render-verifier`
- `presentation-template-profiler`
- `template-presentation-workflow`

## Ambiguous outputs

- `PERFORMANCE_PLAN.md` — producers: `optimize-software-performance`, `performance-optimization-plan`
- `TASK.md` — producers: `optimize-software-performance`, `performance-optimization-plan`
- `learning-mission.json` — producers: `learning-mission`, `teach`
- `learning-next-step.json` — producers: `learning-next-step`, `teach`
- `learning-state.json` — producers: `learning-state`, `teach`
- `performance-result.json` — producers: `optimize-software-performance`, `performance-regression-verification`
- `presentation-qa.md` — producers: `euroimmun-presentation-workflow`, `template-presentation-workflow`
- `presentation-template-profile.json` — producers: `euroimmun-presentation-workflow`, `presentation-template-profiler`, `template-presentation-workflow`

## Outputs without inferred consumers

These are **not automatically defects**. The dependency graph infers consumers only from hard `requires` edges. User-facing reports, installed artifacts, runbooks, exported notes and other terminal products are expected to appear here. Treat this list as a review queue, not as an orphan verdict.

- `acceptance-gaps.json` — producer: `fda-acceptance-readiness`
- `adverse-event-code-set.json` — producer: `medical-device-adverse-event-coding`
- `adverse-event-coding-delta.json` — producer: `medical-device-adverse-event-coding`
- `adverse-event-coding-rationale.json` — producer: `medical-device-adverse-event-coding`
- `athlete-management-state.json` — producer: `sport-athlete-management`
- `audit-finding-response-map.json` — producer: `audit-inspection-finding-response`
- `beta-readiness.json` — producer: `project-beta-readiness`
- `beta-readiness.md` — producer: `project-beta-readiness`
- `beta-runbook.md` — producer: `project-beta-readiness`
- `candidate-interview-question-set.md` — producer: `candidate-role-fit-assessment`
- `candidate-role-fit.json` — producer: `candidate-role-fit-assessment`
- `candidate-role-fit.md` — producer: `candidate-role-fit-assessment`
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
- `complaint-regulatory-routing.json` — producer: `medical-device-complaint-regulatory-routing`
- `concept-handoff.json` — producer: `thought-to-concept-flow`
- `concept.md` — producer: `thought-to-concept-flow`
- `conflict-residual-risk-handoff.json` — producer: `merge-conflict-resolution`
- `conflict-resolution-evidence.json` — producer: `merge-conflict-resolution`
- `containment-actions.json` — producer: `nonconformance-mrb-disposition`
- `contract-case.json` — producer: `contract-workflow`
- `contract-handoff.json` — producer: `contract-workflow`
- `contract-plan.md` — producer: `contract-workflow`
- `cybersecurity-evidence-map.json` — producer: `medical-device-cybersecurity-lifecycle`
- `cybersecurity-lifecycle-assessment.json` — producer: `medical-device-cybersecurity-lifecycle`
- `cybersecurity-postmarket-actions.json` — producer: `medical-device-cybersecurity-lifecycle`
- `de-novo-risk-control-rationale.md` — producer: `fda-de-novo-special-controls`
- `docs/agents/CONFIG.md` — producer: `repository-skill-bootstrap`
- `docs/agents/CONTEXT.md` — producer: `repository-skill-bootstrap`
- `docs/agents/DECISIONS.md` — producer: `repository-skill-bootstrap`
- `domain-change-plan.md` — producer: `domain-model-maintenance`
- `domain-model-map.json` — producer: `domain-model-maintenance`
- `domain-validation.json` — producer: `domain-model-maintenance`
- `dpia-decision.json` — producer: `medical-device-privacy-gdpr-bdsg`
- `dr-komorowski-report.pdf` — producer: `dr-komorowski-sport-report-renderer`
- `dual-510k-clia-strategy.json` — producer: `fda-dual-510k-clia-waiver`
- `dual-evidence-package.json` — producer: `fda-dual-510k-clia-waiver`
- `dual-study-evidence-map.json` — producer: `fda-dual-510k-clia-waiver`
- `due-diligence-handoff.json` — producer: `technology-due-diligence`
- `engineering-closure-gaps.json` — producer: `engineering-delivery-followup`
- `engineering-delivery-status.json` — producer: `engineering-delivery-followup`
- `engineering-iteration-return-input.json` — producer: `engineering-delivery-followup`
- `eudamed-readiness.json` — producer: `eudamed-udi-ivd`
- `euroimmun-presentation.pdf` — producer: `euroimmun-presentation-workflow`
- `euroimmun-presentation.pptx` — producer: `euroimmun-presentation-workflow`
- `euroimmun-report.pdf` — producer: `euroimmun-pdf-report-renderer`
- `execution plan` — producer: `synapse-orchestrator`
- `executive-search-brief.md` — producer: `job-description-authoring`
- `expert handoff` — producer: `synapse-orchestrator`
- `fda-acceptance-preflight.json` — producer: `fda-acceptance-readiness`
- `fda-device-listing-readiness.json` — producer: `fda-registration-listing-udi`
- `fda-recall-authority-state.json` — producer: `fda-recall-status-termination`
- `fda-recall-status-report.json` — producer: `fda-recall-status-termination`
- `fda-recall-termination-request.json` — producer: `fda-recall-status-termination`
- `fda-registration-readiness.json` — producer: `fda-registration-listing-udi`
- `fda-request-issue-map.json` — producer: `fda-additional-information-response`
- `fda-response-package.md` — producer: `fda-additional-information-response`
- `finding-action-plan.json` — producer: `audit-inspection-finding-response`
- `finding-closure-status.json` — producer: `audit-inspection-finding-response`
- `frontend-design-handoff.md` — producer: `frontend-design-director`
- `frontend-design-routing.json` — producer: `frontend-design-director`
- `fto-claim-map.json` — producer: `freedom-to-operate-assessment`
- `fto-design-around-options.json` — producer: `freedom-to-operate-assessment`
- `fto-risk-heatmap.md` — producer: `freedom-to-operate-assessment`
- `fto-scope.json` — producer: `freedom-to-operate-assessment`
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
- `ivdr-authority-state.json` — producer: `ivdr-fsca-status-final-reporting`
- `ivdr-economic-operator-escalation-log.json` — producer: `ivdr-economic-operator-postmarket-propagation`
- `ivdr-economic-operator-obligation-map.json` — producer: `ivdr-economic-operator-postmarket-propagation`
- `ivdr-economic-operator-propagation-state.json` — producer: `ivdr-economic-operator-postmarket-propagation`
- `ivdr-fsca-authority-followup.json` — producer: `ivdr-fsca-status-final-reporting`
- `ivdr-vigilance-final-report-package.json` — producer: `ivdr-fsca-status-final-reporting`
- `job-description.md` — producer: `job-description-authoring`
- `knowledge-map.md` — producer: `mermaid-knowledge-map-renderer`
- `knowledge-map.mmd` — producer: `mermaid-knowledge-map-renderer`
- `learning-practice-request.json` — producer: `teach`
- `lifecycle-impact-gates.json` — producer: `regulatory-change-impact-orchestrator`
- `management-review-effectiveness-gaps.json` — producer: `qms-management-review-action-followup`
- `management-review-follow-up-status.json` — producer: `qms-management-review-action-followup`
- `management-review-return-input.json` — producer: `qms-management-review-action-followup`
- `mdsap-audit-scope.json` — producer: `mdsap-audit-readiness`
- `mdsap-evidence-gaps.json` — producer: `mdsap-audit-readiness`
- `mdsap-task-readiness.json` — producer: `mdsap-audit-readiness`
- `measurement-capability-study.json` — producer: `measurement-system-validation`
- `measurement-evidence-gaps.json` — producer: `measurement-system-validation`
- `measurement-system-assessment.json` — producer: `measurement-system-validation`
- `memory-ledger.merged.json` — producer: `memory-sync-reconciliation`
- `memory-reconciliation-plan.json` — producer: `memory-sync-reconciliation`
- `mrb-disposition-decision.json` — producer: `nonconformance-mrb-disposition`
- `next-training-decision.json` — producer: `sport-athlete-management`
- `nonconformance-assessment.json` — producer: `nonconformance-mrb-disposition`
- `obsidian-candidate.json` — producer: `obsidian-adapter`
- `obsidian-map.canvas` — producer: `obsidian-adapter`
- `obsidian-note.md` — producer: `obsidian-adapter`
- `obsidian-view.base` — producer: `obsidian-adapter`
- `opaque-analysis-evidence.md` — producer: `opaque-system-analysis`
- `optimization-closure.md` — producer: `optimize-software-performance`
- `optional Mermaid map` — producer: `thought-to-concept-flow`
- `optional Obsidian vault projection` — producer: `thought-to-concept-flow`
- `patent-landscape.json` — producer: `patent-landscape-analysis`
- `patent-landscape.md` — producer: `patent-landscape-analysis`
- `patent-search-log.json` — producer: `patent-landscape-analysis`
- `pccp-applicability.json` — producer: `fda-pccp-change-control`
- `pccp-change-evidence.json` — producer: `fda-pccp-change-control`
- `pccp-deviation-routing.json` — producer: `fda-pccp-change-control`
- `per-traceability.json` — producer: `ivdr-performance-evaluation-report`
- `performance-evaluation-report.md` — producer: `ivdr-performance-evaluation-report`
- `person-research-workflow-result.json` — producer: `person-research-report-workflow`
- `plan-revision.json` — producer: `sport-athlete-management`
- `pmpf-evaluation-report.md` — producer: `ivdr-pmpf`
- `pmpf-plan.json` — producer: `ivdr-pmpf`
- `pmpf-signals.json` — producer: `ivdr-pmpf`
- `privacy-assessment.json` — producer: `medical-device-privacy-gdpr-bdsg`
- `privacy-governance.md` — producer: `medical-device-privacy-gdpr-bdsg`
- `process-validation-assessment.json` — producer: `process-validation-iq-oq-pq`
- `process-validation-protocol.md` — producer: `process-validation-iq-oq-pq`
- `process-validation-strategy.json` — producer: `process-validation-iq-oq-pq`
- `progress summary` — producer: `synapse-orchestrator`
- `public-job-posting.md` — producer: `job-description-authoring`
- `purchase-plan.json` — producer: `purchase-decision-planner`
- `purchase-plan.md` — producer: `purchase-decision-planner`
- `purchase-shortlist.json` — producer: `purchase-decision-planner`
- `qmsr-inspection-readiness.json` — producer: `fda-qmsr-inspection-readiness`
- `qsub-briefing-package.md` — producer: `fda-qsub-strategy`
- `qsub-commitments.json` — producer: `fda-qsub-strategy`
- `qsub-question-set.json` — producer: `fda-qsub-strategy`
- `recovered-system-model.json` — producer: `opaque-system-analysis`
- `regulatory-awareness-timeline.json` — producer: `medical-device-complaint-regulatory-routing`
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
- `role-architecture.md` — producer: `role-architecture`
- `role-requirements-report.md` — producer: `role-requirements-grilling`
- `service-complaint-handoff.json` — producer: `medical-device-service-report-quality-routing`
- `service-event-quality-record.json` — producer: `medical-device-service-report-quality-routing`
- `service-quality-routing.json` — producer: `medical-device-service-report-quality-routing`
- `source-context.json` — producer: `source-to-context`
- `source-context.md` — producer: `source-to-context`
- `special-controls-matrix.json` — producer: `fda-de-novo-special-controls`
- `sport-report-package` — producer: `sport-diagnostics-training-report-workflow`
- `stakeholder-questionnaire.json` — producer: `external-stakeholder-questionnaire`
- `stakeholder-questionnaire.md` — producer: `external-stakeholder-questionnaire`
- `supplier-control-plan.json` — producer: `supplier-quality-medical-device`
- `supplier-quality-assessment.json` — producer: `supplier-quality-medical-device`
- `supplier-signal-set.json` — producer: `supplier-quality-medical-device`
- `synchronization manifest` — producer: `central-skill-repository-curation`
- `technology-due-diligence.json` — producer: `technology-due-diligence`
- `technology-due-diligence.md` — producer: `technology-due-diligence`
- `ui-prototype-plan.md` — producer: `project-beta-readiness`
- `updated skill repository` — producer: `central-skill-repository-curation`
- `usability-engineering-assessment.json` — producer: `iec62366-usability-engineering`
- `usability-evidence-gaps.json` — producer: `iec62366-usability-engineering`
- `use-related-risk-evidence.json` — producer: `iec62366-usability-engineering`
- `vigilance-entry-handoff.json` — producer: `medical-device-complaint-regulatory-routing`

## Interpretation

A true orphan requires additional evidence that an output was intended for downstream machine consumption but has no valid consumer. Absence of a hard dependency alone is insufficient to make that claim.
