---
name: legal-specialist-router
description: Routet präzise Legal-Work-Orders an passende Rechtsgebiets-, Compliance-, Regulatory-, IP- oder Sports-Law-Specialists und integriert deren Ergebnisse, ohne deren Fachlogik zu duplizieren. Verwenden, wenn ein Matter mehrere Rechts- oder Regelwerksschichten berührt.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.7.0
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
- Finance/Insolvency/Restructuring → `finance-insolvency-restructuring-law-specialist`
- Corporate Compliance/Integrity/Anti-Corruption → `corporate-compliance-law-specialist` plus Obligation/Control/Investigation-Systeme
- ESG/Supply Chain/Environmental → `esg-supply-chain-environmental-law-specialist` plus Supplier-/Control-Systeme
- Public Procurement/Healthcare → `public-procurement-healthcare-law-specialist` plus Contract/Antitrust/Compliance/Regulatory
- Digital/AI/Cyber/Data → `digital-ai-cyber-law-specialist`; technische Cybersecurity/ISMS und Medical-Device-Cybersecurity bleiben bei den vorhandenen Fach-Skills
- allgemeines Privacy/Data Law → `privacy-data-law-specialist`; Medical-Device-/IVD-Privacy zusätzlich zum vorhandenen `medical-device-privacy-gdpr-bdsg`
- IP/Licensing → `ip-licensing-law-specialist`; Patentlandschaft/Biopatent/FTO bleiben bei den vorhandenen Fach-Skills
- Competition/Antitrust/Merger Control → `competition-antitrust-law-specialist`
- Whistleblowing/HinSchG und `internal-investigation-workflow`
- Trade/Sanctions/Export → `trade-sanctions-export-control-specialist`
- Product Liability/Safety → `product-liability-safety-law-specialist`; Medical-Device-/IVD-Sicherheitsentscheidungen bleiben bei den vorhandenen Regulatory/Risk/CAPA Specialists
- Disputes/Litigation → `dispute-litigation-strategy-specialist`
- Tax-relevante Legal Dependencies → `tax-legal-interface-specialist`; materielle Steuerpositionen an befugte Tax Professionals
- Real Estate → `real-estate-law-specialist`
- private Matters → zuerst `private-legal-matter-router`, danach insbesondere `german-family-law-specialist`, `german-inheritance-succession-law-specialist`, `german-consumer-insurance-private-contract-law-specialist`, `german-criminal-administrative-offence-procedure-specialist` oder `german-administrative-social-traffic-law-specialist`
- deutsches Vereinsrecht → `german-association-law-specialist`
- deutsches Sportrecht einschließlich DOSB-Strukturen und Safe-Sport-Verfahren → `german-sports-law-specialist`
- Rudersportrecht/DRV → `german-rowing-sport-law-specialist`
- bestehende MDR/IVDR/FDA/QMS/Risk/Complaint/CAPA-Specialists bei regulierten Produkten.

## Cross-Domain Examples

- M&A mit Finanzierung, Betriebsübergang, IP und Fusionskontrolle erzeugt getrennte Work Orders an M&A, Finance/Insolvency, Employment, IP und Antitrust.
- Distress bei reguliertem Hersteller erzeugt Finance/Insolvency-, Governance-, Employment-, Supplier-, Regulatory- und ggf. Litigation/Counsel-Work Orders.
- Öffentliche IVD-Ausschreibung erzeugt Procurement/Healthcare-, Contract-, Competition-, Corporate-Compliance- und Regulatory-Work Orders.
- Lieferkettenvorwurf bei kritischem Reagenzlieferanten erzeugt ESG/Supply-Chain-, Supplier-Quality-, Contract-, Investigation- und Governance-Work Orders.
- IP-Lizenz mit Exklusivität erzeugt getrennte Work Orders an IP/Licensing und Antitrust; Patent-/FTO-Analyse bleibt technisch/rechtlich separat.
- Investigation mit möglicher Kündigung und Beschäftigtendaten erzeugt getrennte Work Orders an Investigation, Employment und Privacy sowie bei Bedarf Whistleblowing/Counsel.
- Board-Entscheidung über material risk erzeugt Governance/Risk/Decision Work Orders; eine AI-Empfehlung wird nicht als Organbeschluss behandelt.
- Internationale Technology- oder Materialtransfers erzeugen Trade/Export-Control Work Orders zusätzlich zu IP, Contract, Regulatory oder Scientific Specialists.
- Produktschaden erzeugt getrennte Work Orders für Regulatory/Vigilance, Risk/CAPA, Product Liability und bei Streitdrohung Litigation/Preservation.
- AI-gestützte HR-Entscheidung erzeugt Digital/AI-, Employment-, Privacy- und ggf. Works-Council-/Governance-Work Orders statt einer monolithischen „AI-Compliance“-Antwort.
- Korruptionsverdacht bei Distributor erzeugt Corporate-Compliance-, Investigation-, Employment-, Trade/Sanctions- und ggf. Criminal/Counsel-Work Orders.
- Immobilientransaktion erzeugt Real-Estate-, Tax- und je nach Struktur M&A/Governance/Notary Work Orders.
- Private Angelegenheit wird zunächst im Private Router auf Mandant, Frist, Conflict und Vertretung geprüft; Unternehmensannahmen werden nicht übernommen.

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
- Corporate Compliance definiert materielle Integrity-/Organisationsfragen; Obligation Register, Controls und Investigation bleiben getrennte Systeme.
- ESG/Supply-Chain Legal definiert materielle Scope-/Due-Diligence-Pflichten; Supplier Quality, technische Umweltbewertung und Reporting bleiben eigene Layer.
- Procurement/Healthcare trennt Vergabe, Integrity, Competition, Contract und Regulatory statt eines monolithischen Tender-Checks.
- Finance/Insolvency verarbeitet bestätigte Finance-Facts; Accounting, Tax und Valuation bleiben bei ihren Fach-Owners.
- Digital/AI/Cyber Legal klassifiziert Rechtsregime/Rollen; technische Security-, Privacy- und Regulatory-Ownership bleibt bei den Fach-Specialists.
- Whistleblowing-Rechtsanalyse und Investigation Fact-Finding sind getrennte Work Orders, können aber denselben Matter State nutzen.
- Tax wird als Specialist Interface geroutet; eine Legal-Analyse wird nicht zur behaupteten Steuerberatermeinung hochgestuft.
- Private und Corporate Matter States werden nicht vermischt.
- Mehrere Specialists dürfen dieselben Facts konsumieren; ihre Schlussfolgerungen werden nicht automatisch harmonisiert.
- Widersprüche werden im `legal-specialist-integration-status.json` sichtbar und an Risk/Decision Routing übergeben.
- Fehlender Specialist erzeugt einen offenen Capability Gap statt improvisierter Rechtsberatung.

## Qualitätsgate

Pass nur, wenn jede materielle Frage einen Owner besitzt, bestehende Fach-Skills bevorzugt werden und Widersprüche/fehlende Outputs offen bleiben.
