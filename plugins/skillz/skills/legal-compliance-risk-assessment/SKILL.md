---
name: legal-compliance-risk-assessment
description: Konsolidiert Legal-, Compliance-, Regulatory- und Specialist-Findings in ein priorisiertes Risiko- und Exposure-Modell mit Probability, Impact, Velocity, Reversibility, Mitigation, Residual Risk und Entscheidungsautorität. Verwenden vor wesentlichen Legal-Entscheidungen, Verhandlungen und Final Gates.
---

# Legal Compliance Risk Assessment

## Zweck

Priorisiere Risiken nach tatsächlicher Entscheidungsrelevanz statt nach bloßer Anzahl roter Findings.

## Risikodimensionen

Erfasse mindestens:

- probability,
- legal/financial/regulatory/reputational/personal impact,
- velocity und deadline sensitivity,
- detectability und controllability,
- reversibility,
- quantitative oder qualitative exposure,
- mitigation und mitigation cost,
- residual risk,
- risk owner und decision authority.

## Kernregeln

- Evidenzqualität und Risikoschwere getrennt bewerten.
- Unknown ist weder `low risk` noch `no issue`.
- Mehrere kleine Klauselprobleme dürfen ein Systemrisiko bilden; ein formal auffälliger Punkt muss nicht materiell hoch sein.
- Accepted Risk benötigt dokumentierte Autorität aus `legal-decision-boundaries.json`.
- Specialist-Widersprüche werden als Risk/Decision Uncertainty weitergeführt.

## Workflow

1. Findings und Specialist Outputs normalisieren.
2. Gemeinsame Ursachen und kumulative Exposures clustern.
3. Inherent Risk und Evidenzqualität bewerten.
4. Mitigation Options und Kosten/Reversibilität erfassen.
5. Residual Risk und erforderliche Autorität bestimmen.
6. Priorisierten Risk Register und Decision Handoff ausgeben.

## Qualitätsgate

Pass nur, wenn High-Risk-Prioritäten aus Exposure und Entscheidungswirkung erklärbar sind, Unknowns sichtbar bleiben und Risk Acceptance eine benannte Autorität besitzt.
