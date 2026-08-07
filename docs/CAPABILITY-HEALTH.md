# Capability Health

Generated from the canonical skill capability index. Do not edit manually.

## Summary

- Skills: **60**
- User-facing entrypoints: **42**
- Evaluation suites: **60**
- Skills without evaluation suite: **0**
- User-facing entrypoints without evaluation suite: **0**
- Ambiguous outputs (multiple producers): **0**
- Outputs without inferred hard-requires consumers: **59**

## Evaluation gaps

None.

### User-facing evaluation gaps

None.

## Ambiguous outputs

None.

## Outputs without inferred consumers

These are **not automatically defects**. The dependency graph infers consumers only from hard `requires` edges. User-facing reports, installed artifacts, runbooks, exported notes and other terminal products are expected to appear here. Treat this list as a review queue, not as an orphan verdict.

- `GRILL-REPORT.md` — producer: `round-based-requirements-grilling`
- `approved SPEC.md` — producer: `round-based-requirements-grilling`
- `beta-readiness.json` — producer: `project-beta-readiness`
- `beta-readiness.md` — producer: `project-beta-readiness`
- `beta-runbook.md` — producer: `project-beta-readiness`
- `change-impact-assessment.json` — producer: `controlled-quality-documentation`
- `communication-profile.merged.json` — producer: `memory-sync-reconciliation`
- `conflict-residual-risk-handoff.json` — producer: `merge-conflict-resolution`
- `conflict-resolution-evidence.json` — producer: `merge-conflict-resolution`
- `controlled-document-plan.md` — producer: `controlled-quality-documentation`
- `decision-follow-up-register.json` — producer: `decision-and-follow-up-tracker`
- `decision-follow-up-register.md` — producer: `decision-and-follow-up-tracker`
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
- `human-procedure-plan.md` — producer: `human-procedure-wizard`
- `human-procedure-result.json` — producer: `human-procedure-wizard`
- `import verification` — producer: `openasr-offline-model-import`
- `installed OpenASR model` — producer: `openasr-offline-model-import`
- `isms-audit-findings.json` — producer: `iso27001-isms-audit`
- `isms-audit-plan.json` — producer: `iso27001-isms-audit`
- `isms-audit-report.md` — producer: `iso27001-isms-audit`
- `ivdr-classification-assessment.json` — producer: `ivdr-device-classification`
- `ivdr-classification-rationale.md` — producer: `ivdr-device-classification`
- `ivdr-performance-evaluation-gaps.json` — producer: `ivdr-performance-evaluation`
- `ivdr-performance-evaluation.json` — producer: `ivdr-performance-evaluation`
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
- `privacy-assessment.json` — producer: `medical-device-privacy-gdpr-bdsg`
- `privacy-governance.md` — producer: `medical-device-privacy-gdpr-bdsg`
- `progress summary` — producer: `synapse-orchestrator`
- `recovered-system-model.json` — producer: `opaque-system-analysis`
- `regulatory-strategy.json` — producer: `medical-device-regulatory-strategy`
- `regulatory-strategy.md` — producer: `medical-device-regulatory-strategy`
- `regulatory-wayfinding-handoff.json` — producer: `medical-device-regulatory-strategy`
- `remaining-unknowns.json` — producer: `opaque-system-analysis`
- `resolved-change-brief.md` — producer: `merge-conflict-resolution`
- `source-context.json` — producer: `source-to-context`
- `source-context.md` — producer: `source-to-context`
- `stakeholder-questionnaire.json` — producer: `external-stakeholder-questionnaire`
- `stakeholder-questionnaire.md` — producer: `external-stakeholder-questionnaire`
- `synchronization manifest` — producer: `central-skill-repository-curation`
- `ui-prototype-plan.md` — producer: `project-beta-readiness`
- `updated skill repository` — producer: `central-skill-repository-curation`

## Interpretation

A true orphan requires additional evidence that an output was intended for downstream machine consumption but has no valid consumer. Absence of a hard dependency alone is insufficient to make that claim.
