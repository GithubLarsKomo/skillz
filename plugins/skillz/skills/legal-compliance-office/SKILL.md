---
name: legal-compliance-office
description: Orchestriert unternehmerische und private Legal-/Compliance-Matters von Intake und Mandantenstrategie über aktuelle Rechtsgrundlage, Wayfinding, Specialist Routing und Risiko bis zum Final Gate und verbindet Einzelmatters mit Legal Change Monitoring, Compliance Management und Executive Governance, ohne Fachlogik der Specialists zu duplizieren.
---

# Legal Compliance Office

## Zweck

Dünner General-Counsel-/Compliance-Orchestrator. Er hält Matter-Ziel, Evidenz, Specialist-Arbeit, Risiko, Autorität und nächste Aktion zusammen, trifft aber keine zweite fachliche Entscheidung neben den Specialists. Neben Einzelmatters unterstützt er den dauerhaften Operating Loop aus **Rechtsänderung → Applicability → Obligation → Control/Evidence → Risk/Decision → Follow-up**.

## Matter-Ablauf

1. Matter mit `legal-matter-intake` strukturieren.
2. Mandantenstrategie mit `legal-client-strategy` fixieren.
3. Früh `privilege-and-counsel-routing` anwenden.
4. Rechts-/Regelwerkskontext über `current-law-context` verifizieren.
5. Bei komplexer Unsicherheit `legal-matter-wayfinder` einsetzen.
6. Fachfragen über `legal-specialist-router` routen und Ergebnisse integrieren.
7. `legal-compliance-risk-assessment` auf aktualisierte Specialist Outputs anwenden.
8. Entscheidungen/Risk Acceptance an die zuständige Autorität übergeben.
9. Vor Abschluss `legal-matter-final-gate` ausführen.
10. Status, offene Punkte und genau nächste sichere Aktion dokumentieren.

## Client Context Gate

Vor fachlichem Routing `corporate|group|private` festlegen. Private Matters zusätzlich durch `private-legal-matter-router` führen; konzerninterne Rechtsdienstleistungs-, Authority-, Privilege- oder Dokumentzugriffsannahmen werden nicht automatisch auf Privatmatters übertragen. Konflikte zwischen Unternehmens-, Organ-, Mitarbeiter- und Privatinteressen als getrennte Matter States behandeln.

## Operating-System Routing

- Verträge → kompatibler `contract-workflow` / kanonischer Contract Matter Stack.
- Corporate Integrity/Anti-Corruption/Third Parties → `corporate-compliance-law-specialist` plus Obligation/Control/Investigation-System.
- Digital/AI/Cyber/Data → `digital-ai-cyber-law-specialist` plus bestehende Privacy-/ISMS-/Cybersecurity-/Regulatory-Specialists.
- Public Procurement/Healthcare → `public-procurement-healthcare-law-specialist` plus Contract/Antitrust/Compliance/Regulatory.
- ESG/Supply Chain/Environmental → `esg-supply-chain-environmental-law-specialist` plus Supplier-/Control-/Reporting-Fachlayer.
- Finance/Insolvency/Restructuring → `finance-insolvency-restructuring-law-specialist` plus Governance/Tax/Finance/Accounting/Counsel-Schnittstellen.
- Compliance-System/Control Framework → `compliance-management-workflow` mit Obligation→Control→Evidence Lineage.
- Rechtsänderungen außerhalb des Medical-Device-Spezialmonitorings → `legal-change-monitoring` → `legal-change-impact-orchestrator`.
- Medical-Device-/IVD-Regulatory Changes → bestehendes `regulatory-change-monitoring` und `regulatory-change-impact-orchestrator`; nicht in ein generisches Legal-Monitoring umdeuten.
- Executive-/Vorstandsreview, Decision Queue und Residual-Risk-Governance → `executive-legal-compliance-governance`.
- Whistleblowing oder interne Untersuchung → `whistleblowing-law-specialist` und `internal-investigation-workflow`.
- Private Matters → `private-legal-matter-router` vor Domain Specialist/Authority Gate.
- Sport-/Vereinsmatters → `german-association-law-specialist`, `german-sports-law-specialist`, bei Rudern zusätzlich `german-rowing-sport-law-specialist`; Investigations bleiben ein separater Verfahrenslayer.

## Specialist Routing Examples

- Employment/Labor → `german-employment-labor-law-specialist`.
- Privacy/Data → `privacy-data-law-specialist`; regulierte IVD/Medical-Device-Privacy zusätzlich beim vorhandenen Fach-Skill.
- Corporate Governance → `corporate-governance-law-specialist`.
- M&A/Transactions → `corporate-transactions-ma-specialist`.
- Finance/Insolvency/Restructuring → `finance-insolvency-restructuring-law-specialist`.
- Corporate Compliance/Integrity → `corporate-compliance-law-specialist`.
- ESG/Supply Chain/Environmental → `esg-supply-chain-environmental-law-specialist`.
- Public Procurement/Healthcare → `public-procurement-healthcare-law-specialist`.
- Digital/AI/Cyber/Data → `digital-ai-cyber-law-specialist`.
- IP/Licensing → `ip-licensing-law-specialist` plus vorhandene Patent/Biopatent/FTO-Skills.
- Competition/Antitrust → `competition-antitrust-law-specialist`.
- Trade/Sanctions/Export → `trade-sanctions-export-control-specialist`.
- Product Liability/Safety → `product-liability-safety-law-specialist` plus vorhandene Regulatory/Risk/CAPA-Skills.
- Disputes/Litigation → `dispute-litigation-strategy-specialist` mit Counsel Gate für formelle Prozesshandlungen.
- Tax Dependencies → `tax-legal-interface-specialist`; bestätigte materielle Tax Position vom befugten Tax Professional.
- Real Estate → `real-estate-law-specialist`, mit Tax-/Notary-/Authority-Handoffs soweit ausgelöst.
- Family → `german-family-law-specialist`.
- Inheritance/Succession → `german-inheritance-succession-law-specialist`.
- Consumer/Insurance/Private Contracts → `german-consumer-insurance-private-contract-law-specialist`.
- Criminal/OWi/Investigation Procedure → `german-criminal-administrative-offence-procedure-specialist`.
- Administrative/Social/Traffic Public Law → `german-administrative-social-traffic-law-specialist`.

## Orchestrator-Regeln

- Fach-Specialists besitzen ihre Domänenlogik; der Orchestrator dupliziert keine Subsumtion.
- Existing Assets first: Regulatory-, QMS-, Complaint-, CAPA-, Audit-, Patent-, Biopatent-, FTO-, Research- und Grilling-Skills werden bevorzugt wiederverwendet.
- Compliance bedeutet nicht nur Policy-Vorhandensein: materielle Pflichten, Controls, Evidenz und Assurance bleiben getrennte Layer.
- Corporate Compliance Legal Analysis, Control Design und Investigation Fact-Finding sind getrennte Ownership-Layer.
- ESG-/Supply-Chain-Rechtsanalyse ersetzt weder Supplier Quality noch technische Umweltbewertung oder Reporting-Fachverantwortung.
- Public Procurement Legal ersetzt weder Tender-Fachinhalt noch Product Regulatory; Vergabe-, Competition-, Integrity- und Contract-Layer bleiben getrennt.
- Finance/Insolvency Legal verarbeitet bestätigte Finanzdaten, ersetzt aber weder Accounting/Valuation noch Tax Professional oder formelle Insolvenzberatung.
- Digital/AI/Cyber-Rechtsklassifikation ersetzt weder technische Security-Bewertung noch Privacy-, ISMS- oder Regulatory-Fachentscheidungen.
- Detection einer Rechtsänderung ist weder Applicability noch Implementation noch Compliance Closure.
- Investigation Findings ersetzen weder regulatorische Reportability noch arbeits-/straf-/datenschutzrechtliche Entscheidungsgates.
- Tax Research wird nicht als bestätigte individuelle Steuerposition ausgegeben, wenn ein Tax Professional erforderlich ist.
- Ein L3-Gate beendet nicht automatisch alle vorbereitenden Arbeiten.
- Die nächste Aktion muss aus dem aktuellen Matter State ausführbar und autorisiert sein.

## Grenzen

- Keine Simulation einer Rechtsanwaltszulassung, Steuerberaterbefugnis, Behördenentscheidung, gerichtlichen Entscheidung, notariellen Beurkundung oder sonstigen externen Autorität.
- Keine Vermischung von staatlichem Recht und privaten Vereins-/Verbandsregeln.
- Keine formale Organentscheidung aus einer AI-Empfehlung ableiten.

## Qualitätsgate

Pass nur, wenn Client Context, Matter-Ziel, Current Law, Specialist Ownership, Risiko, Autorität, offene Punkte und Final-Gate-State konsistent zusammenpassen und laufende Legal-Change-/Compliance-/Executive-Governance-Pfade bei Bedarf sichtbar geroutet sind.
