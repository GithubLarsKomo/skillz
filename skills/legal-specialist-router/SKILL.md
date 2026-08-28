---
name: legal-specialist-router
description: Routet präzise Legal-Work-Orders an passende Rechtsgebiets-, Compliance-, Regulatory-, IP- oder Sports-Law-Specialists und integriert deren Ergebnisse, ohne deren Fachlogik zu duplizieren. Verwenden, wenn ein Matter mehrere Rechts- oder Regelwerksschichten berührt.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.4.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-law-context
  - legal-client-strategy
outputs:
  - legal-specialist-work-orders.json
  - legal-specialist-route-map.json
  - legal-specialist-integration-status.json
lastEvaluated: 2026-08-28
---

# Legal Specialist Router

## Zweck

Der Router entscheidet **wer welche Frage beantwortet**, nicht die materielle Rechtsfrage selbst.

## Routing Domains

Unterstütze insbesondere:

- Commercial Contract Law / Contract Matter Stack
- deutsches Individual-/Kollektivarbeitsrecht → `german-employment-labor-law-specialist`
- Corporate Governance/Organrecht → `corporate-governance-law-specialist`
- Corporate Transactions/M&A → `corporate-transactions-ma-specialist`
- allgemeines Privacy/Data Law → `privacy-data-law-specialist`; Medical-Device-/IVD-Privacy zusätzlich zum vorhandenen `medical-device-privacy-gdpr-bdsg`
- IP/Licensing → `ip-licensing-law-specialist`; Patentlandschaft/Biopatent/FTO bleiben bei den vorhandenen Fach-Skills
- Competition/Antitrust/Merger Control → `competition-antitrust-law-specialist`
- Corporate Compliance einschließlich `compliance-obligation-register`, Control Mapping und Assurance
- Whistleblowing/HinSchG und `internal-investigation-workflow`
- Trade/Sanctions/Export → `trade-sanctions-export-control-specialist`
- Product Liability/Safety → `product-liability-safety-law-specialist`; Medical-Device-/IVD-Sicherheitsentscheidungen bleiben bei den vorhandenen Regulatory/Risk/CAPA Specialists
- Disputes/Litigation → `dispute-litigation-strategy-specialist`
- Tax Legal Interface
- Real Estate
- deutsches Vereinsrecht
- deutsches Sportrecht einschließlich DOSB-Strukturen und Safe-Sport-Verfahren
- Rudersportrecht/DRV als sportartspezifisches Overlay
- bestehende MDR/IVDR/FDA/QMS/Risk/Complaint/CAPA-Specialists bei regulierten Produkten.

## Cross-Domain Examples

- M&A mit Betriebsübergang, IP und Fusionskontrolle erzeugt getrennte Work Orders an M&A, Employment, IP und Antitrust.
- IP-Lizenz mit Exklusivität erzeugt getrennte Work Orders an IP/Licensing und Antitrust; Patent-/FTO-Analyse bleibt technisch/rechtlich separat.
- Investigation mit möglicher Kündigung und Beschäftigtendaten erzeugt getrennte Work Orders an Investigation, Employment und Privacy sowie bei Bedarf Whistleblowing/Counsel.
- Board-Entscheidung über material risk erzeugt Governance/Risk/Decision Work Orders; eine AI-Empfehlung wird nicht als Organbeschluss behandelt.
- Internationale Technology- oder Materialtransfers erzeugen Trade/Export-Control Work Orders zusätzlich zu IP, Contract, Regulatory oder Scientific Specialists.
- Produktschaden erzeugt getrennte Work Orders für Regulatory/Vigilance, Risk/CAPA, Product Liability und bei Streitdrohung Litigation/Preservation.

## Work Order Contract

```json
{
  "specialist": "...",
  "question": "...",
  "matterId": "LM-...",
  "clientObjective": "...",
  "jurisdictions": [],
  "facts": [],
  "assumptions": [],
  "sourceRefs": [],
  "priority": "critical|high|normal|low",
  "expectedOutput": "specialist-specific artifact"
}
```

## Kernregeln

- Eine Work Order enthält genau eine fachlich kohärente Frage.
- Bestehende Regulatory-/IP-/QMS-/Complaint-/CAPA-Skills werden wiederverwendet, nicht neu implementiert.
- Whistleblowing-Rechtsanalyse und Investigation Fact-Finding sind getrennte Work Orders, können aber denselben Matter State nutzen.
- Mehrere Specialists dürfen dieselben Facts konsumieren; ihre Schlussfolgerungen werden nicht automatisch harmonisiert.
- Widersprüche werden im `legal-specialist-integration-status.json` sichtbar und an Risk/Decision Routing übergeben.
- Fehlender Specialist erzeugt einen offenen Capability Gap statt improvisierter Rechtsberatung.

## Qualitätsgate

Pass nur, wenn jede materielle Frage einen Owner besitzt, bestehende Fach-Skills bevorzugt werden und Widersprüche/fehlende Outputs offen bleiben.
