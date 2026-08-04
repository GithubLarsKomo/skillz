---
name: medical-device-isms-governance
description: Strukturiert ISO-27001-orientierte ISMS-Governance für MedTech/IVD-Organisationen und koppelt Informationssicherheitsrisiken, Controls, Supplier/Cloud, Incidents und Product-Cybersecurity-Schnittstellen ohne technische Security-Tests zu duplizieren.
userFacing: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: 
  - regulated-product-context
  - two-axis-compliance-review
outputs: 
  - isms-governance-assessment.json
  - isms-risk-treatment-context.json
  - isms-governance.md
lastEvaluated: 2026-08-04
---

# medical-device-isms-governance

## Zweck

Trennt organisatorisches ISMS von Product Security Engineering und schafft eine gemeinsame Evidenz-/Audit-Grundlage.

## Trigger

Verwenden für ISMS Scope, Risk Treatment, Statement-of-Applicability-Kontext, Security Policies/Controls, Supplier/Cloud Governance, Security Incident Governance oder Medical-Device-Cybersecurity-Schnittstellen.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- ISMS Scope, Assets/Information, Interested Parties, Risk Method und Control Applicability werden organisationsspezifisch und evidenzbasiert festgelegt.
- ISO 27001/27002 Controls werden nicht als blind vollständige Checkliste behandelt; Applicability und Evidence bleiben getrennt.
- Organisatorisches ISMS, Product Cybersecurity Risk Management und technische Security Testing/Penetration Testing sind getrennte Verantwortungsbereiche mit expliziten Interfaces.
- Supplier/Cloud/SaaS-Risiken erhalten Ownership, Vertrags-/Assurance-Evidenz und Monitoring statt implizites Vertrauen.
- Security Incidents können Privacy, Product Risk, CAPA und Regulatory Reporting triggern; diese Downstream-Entscheidungen werden nicht vom ISMS-Skill erfunden.

## Workflow

1. ISMS-Scope und kritische Information/Services fixieren.
2. Risks und vorhandene Controls/Evidence inventarisieren.
3. Applicability, Treatment und Residual Risk Context prüfen.
4. Supplier/Cloud/Product-Cybersecurity-Interfaces dokumentieren.
5. Audit-/Improvement-/Incident-Investigations ausgeben.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

## Grenzen

- Keine Penetration Tests oder Vulnerability Scans durchführen.
- Keine ISO-27001-Zertifizierung behaupten.
- Keine automatische Control-Wirksamkeit aus Policy-Vorhandensein ableiten.

## Qualitätsgate

Pass nur, wenn Facts/Interpretations getrennt, Freshness sichtbar, zentrale Claims rückverfolgbar, Unknowns nicht positiv umgedeutet, Cross-Skill-Grenzen respektiert und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.
