---
name: executive-legal-compliance-governance
description: Konsolidiert Legal-/Compliance-Matters, Rechtsänderungen, Control Gaps, Investigations, Verträge, Litigation, Specialist Escalations und Residual Risks in einen entscheidungsorientierten Vorstand-/Executive-Cockpit-Workflow mit Authority, Informationsbasis, Deadlines und Follow-up, ohne Fachentscheidungen neu zu treffen.
---

# Executive Legal & Compliance Governance

## Zweck

Verdichte fachlich bereits analysierte Legal-/Compliance-Informationen zu einer **entscheidungsfähigen Management- und Organperspektive**. Dieser Skill ersetzt keine Specialist Opinion und keine formale Organentscheidung; er stellt sicher, dass Entscheidungsträger die richtige Frage, Informationsbasis, Risiken, Zuständigkeit und Frist sehen.

## Governance Baseline

Für eine deutsche AG ist die aktuelle Organ-/Risikobaseline insbesondere über `corporate-governance-law-specialist` und `current-law-context` zu verifizieren. AktG § 93 verlangt bei unternehmerischen Entscheidungen eine angemessene Informationsgrundlage und Handeln zum Wohl der Gesellschaft; AktG § 91 Abs. 2 verlangt geeignete Maßnahmen einschließlich eines Überwachungssystems zur Früherkennung bestandsgefährdender Entwicklungen. Diese Baseline wird fallbezogen und mit aktuellem `asOf` angewandt.

## Cockpit Domains

Mindestens:

- Critical/High Legal Matters und persönliche Organ-Exposure,
- Rechtsänderungen mit naher Effective Date oder hohem Implementierungsaufwand,
- offene Compliance Obligations ohne ausreichenden Control/Evidence Status,
- ineffektive Controls und überfällige Remediation,
- Whistleblowing/Internal Investigations und retaliation/confidentiality risks,
- material Contracts/Negotiations und ungeklärte Red Lines,
- IP/FTO/License Blocker,
- Competition/Trade/Sanctions Exposure,
- Product Liability/Safety und Litigation/Claims,
- externe Counsel-/Authority-Abhängigkeiten,
- offene Entscheidungen und akzeptierte Residual Risks.

## Decision Queue

Jede Executive Decision enthält:

```json
{
  "decisionId": "ED-...",
  "matterOrChangeId": "...",
  "decisionQuestion": "...",
  "decisionOwner": "...",
  "requiredAuthority": "...",
  "deadline": "...",
  "recommendedOption": "...",
  "alternatives": [],
  "facts": [],
  "assumptions": [],
  "specialistConclusions": [],
  "contradictions": [],
  "legalConstraints": [],
  "riskIfAct": [],
  "riskIfNoAct": [],
  "financialOperationalExposure": "...",
  "reversibility": "...",
  "openEvidence": [],
  "confidence": "...",
  "followUp": []
}
```

## Information Sufficiency Gate

Vor einer materiellen Entscheidung prüfen:

- sind zentrale Facts und Unsicherheiten getrennt?
- sind relevante Specialist Conclusions vorhanden und Widersprüche sichtbar?
- ist aktuelle Rechtslage/fachliche Baseline ausreichend frisch?
- sind wirtschaftliche, operative, regulatorische und persönliche Exposure sichtbar?
- ist die Entscheidung reversibel und welche Deadlines/External Dependencies bestehen?
- ist die zuständige Authority bestimmt?

Fehlt eine entscheidungskritische Information, Status `not-ready` statt künstlicher Entscheidungssicherheit.

## Authority Gate

Unterscheide `recommendation`, `legal/specialist assessment`, `management approval`, `Vorstand/Geschäftsführer decision`, `Aufsichtsratszustimmung`, `Gesellschafter-/Hauptversammlungsbeschluss`, `external counsel/authority action`. Kein Upstream-Artefakt wird automatisch zur formalen Entscheidung.

## Residual Risk Acceptance

Residual Risk darf nur von der dafür zuständigen Authority akzeptiert werden. Dokumentiere Scope, Dauer, Begründung, Alternativen, Mitigations, Trigger zur Neubewertung, persönliche/regulatorische Exposure und Review Date. Ein überfälliger Control Gap wird nicht durch bloße Risikoakzeptanz als „compliant“ umklassifiziert.

## Review Cadence

Unterstütze ad hoc Critical Review sowie regelmäßige Executive Reviews. Priorisiere nach Deadline, Risk Velocity, Enforcement/Personal Exposure, Irreversibility, Control Failure, External Dependency und Decision Lead Time. Keine reine Heatmap ohne zugrunde liegende Matter-/Evidence-Referenzen.

## Decision Record / Follow-up

Materiale Entscheidungen an `decision-record` übergeben. Danach Follow-up mit Owner, Due Date, Evidence of Completion, Effectiveness/Outcome und Reopen Trigger. Beschlussfassung ohne Umsetzung ist kein geschlossenes Matter.

## Qualitätsgate

Pass nur, wenn alle Critical/High Items einen Owner, Status, Deadline, Specialist Source, Risk/Exposure, Decision/Authority Need und nächsten verifizierbaren Schritt besitzen; `not-ready`, Widersprüche und überfällige Punkte bleiben sichtbar.
