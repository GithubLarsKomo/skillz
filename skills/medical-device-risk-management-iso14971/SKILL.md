---
name: medical-device-risk-management-iso14971
description: Führt Medical-Device- und IVD-Risikomanagement nach dem Prozessmodell von ISO 14971 evidenzbasiert durch, ohne eine bestimmte Risikomatrix, RPN-Schwelle oder ALARP-Regel als Normvorgabe zu erfinden.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: 
  - regulated-product-context
  - research-to-evidence-note
outputs: 
  - risk-management-analysis.json
  - risk-management-analysis.md
  - risk-wayfinding-handoff.json
lastEvaluated: 2026-08-04
---

# medical-device-risk-management-iso14971

## Zweck

Verbindet Produktkontext, Hazard Analysis, Risk Controls, Residual Risk und Produktions-/Postproduktionsinformationen mit Engineering und regulatorischer Traceability.

## Trigger

Verwenden für Risk Management Plan/File, Hazard Analysis, FMEA/FTA/Use Error Analysis, Residual Risk, Benefit-Risk oder Post-Market-Risk-Updates bei Medical Devices und IVDs.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- ISO 14971:2019 bleibt der fachliche Referenzrahmen, aber konkrete Normanforderungen werden nur aus zugänglicher autoritativer Evidenz behauptet.
- Risikokriterien und Akzeptanzgrenzen sind organisationsdefiniert; 5x5-Matrix, RPN und ALARP sind optionale Methoden, keine universelle Normvorgabe.
- Trenne Hazard, Sequence of Events, Hazardous Situation, Harm, Probability und Severity nachvollziehbar.
- Risk Controls werden mit Implementierungs- und Wirksamkeitsverifikation verknüpft; ein niedriger Score ersetzt die Verification nicht.
- Residual Risk, Overall Residual Risk und Benefit-Risk werden nur dort bewertet, wo Kontext und Kriterien dies tragen.
- Produktions- und Postproduktionsinformationen können neue Hazards, Wahrscheinlichkeiten, Controls oder CAPA-Investigations auslösen.
- AI/ML- und Cybersecurity-Risiken werden in denselben Lifecycle-Prozess integriert, ohne Security Engineering zu duplizieren.

## Workflow

1. Scope, Intended Purpose, Lifecycle und organisationsdefinierte Akzeptanzkriterien fixieren.
2. Hazards und vorhersehbare Ereignisfolgen evidenzbasiert identifizieren.
3. Risiken nach bestätigter Organisationsmethodik evaluieren.
4. Risk Controls priorisieren, implementierungs- und wirksamkeitsbezogene Verification planen.
5. Residual/Overall Residual Risk und erforderliche Benefit-Risk-Rationale dokumentieren.
6. Production/Post-production Signals, offene Investigations und Traceability übergeben.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

## Grenzen

- Keine erfundene Zertifizierungs- oder Regulatory-Acceptance-Aussage.
- Keine FMEA-RPN-Schwelle als Ersatz für Risk Acceptability.
- Keine Penetration Tests, klinischen Studien oder CAPA-RCA selbst ausführen.

## Qualitätsgate

Pass nur, wenn Facts/Interpretations getrennt, Freshness sichtbar, zentrale Claims rückverfolgbar, Unknowns nicht positiv umgedeutet, Cross-Skill-Grenzen respektiert und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.
