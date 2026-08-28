---
name: legal-specialist-router
description: Routet präzise Legal-Work-Orders an passende Rechtsgebiets-, Compliance-, Regulatory-, IP- oder Sports-Law-Specialists und integriert deren Ergebnisse, ohne deren Fachlogik zu duplizieren. Verwenden, wenn ein Matter mehrere Rechts- oder Regelwerksschichten berührt.
---

# Legal Specialist Router

## Zweck

Der Router entscheidet **wer welche Frage beantwortet**, nicht die materielle Rechtsfrage selbst.

## Routing Domains

Unterstütze insbesondere:

- Commercial Contract Law
- Employment/Labor
- Corporate Governance
- Corporate Transactions/M&A
- Privacy/Data
- IP/Licensing sowie bestehende Patent-/FTO-Skills
- Competition/Antitrust
- Corporate Compliance
- Trade/Sanctions/Export
- Product Liability/Safety
- Disputes/Litigation
- Tax Legal Interface
- Real Estate
- deutsches Vereinsrecht
- deutsches Sportrecht einschließlich DOSB-Strukturen
- Rudersportrecht/DRV als sportartspezifisches Overlay
- bestehende MDR/IVDR/FDA/QMS/Risk-Specialists bei regulierten Produkten.

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
- Bestehende Regulatory-/IP-Skills werden wiederverwendet, nicht neu implementiert.
- Mehrere Specialists dürfen dieselben Facts konsumieren; ihre Schlussfolgerungen werden nicht automatisch harmonisiert.
- Widersprüche werden im `legal-specialist-integration-status.json` sichtbar und an Risk/Decision Routing übergeben.
- Fehlender Specialist erzeugt einen offenen Capability Gap statt improvisierter Rechtsberatung.

## Qualitätsgate

Pass nur, wenn jede materielle Frage einen Owner besitzt, bestehende Fach-Skills bevorzugt werden und Widersprüche/fehlende Outputs offen bleiben.
