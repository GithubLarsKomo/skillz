---
name: legal-compliance-office
description: Orchestriert unternehmerische und private Legal-/Compliance-Matters von Intake und Mandantenstrategie über aktuelle Rechtsgrundlage, Wayfinding, Specialist Routing und Risiko bis zum Final Gate und verbindet Einzelmatters mit Legal Change Monitoring, Compliance Management und Executive Governance, ohne Fachlogik der Specialists zu duplizieren.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.3.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - legal-matter-intake
  - legal-client-strategy
  - current-law-context
  - privilege-and-counsel-routing
  - legal-matter-wayfinder
  - legal-specialist-router
  - legal-compliance-risk-assessment
  - legal-matter-final-gate
outputs:
  - legal-matter-status.json
  - legal-matter-plan.md
  - legal-matter-handoff.json
lastEvaluated: 2026-08-28
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

## Operating-System Routing

- Verträge → kompatibler `contract-workflow` / kanonischer Contract Matter Stack.
- Compliance-System/Control Framework → `compliance-management-workflow` mit Obligation→Control→Evidence Lineage.
- Rechtsänderungen außerhalb des Medical-Device-Spezialmonitorings → `legal-change-monitoring` → `legal-change-impact-orchestrator`.
- Medical-Device-/IVD-Regulatory Changes → bestehendes `regulatory-change-monitoring` und `regulatory-change-impact-orchestrator`; nicht in ein generisches Legal-Monitoring umdeuten.
- Executive-/Vorstandsreview, Decision Queue und Residual-Risk-Governance → `executive-legal-compliance-governance`.
- Whistleblowing oder interne Untersuchung → `whistleblowing-law-specialist` und `internal-investigation-workflow`.
- Sport-/Vereinsmatters → `german-association-law-specialist`, `german-sports-law-specialist`, bei Rudern zusätzlich `german-rowing-sport-law-specialist`; Investigations bleiben ein separater Verfahrenslayer.

## Specialist Routing Examples

- Employment/Labor → `german-employment-labor-law-specialist`.
- Privacy/Data → `privacy-data-law-specialist`; regulierte IVD/Medical-Device-Privacy zusätzlich beim vorhandenen Fach-Skill.
- Corporate Governance → `corporate-governance-law-specialist`.
- M&A/Transactions → `corporate-transactions-ma-specialist`.
- IP/Licensing → `ip-licensing-law-specialist` plus vorhandene Patent/Biopatent/FTO-Skills.
- Competition/Antitrust → `competition-antitrust-law-specialist`.
- Trade/Sanctions/Export → `trade-sanctions-export-control-specialist`.
- Product Liability/Safety → `product-liability-safety-law-specialist` plus vorhandene Regulatory/Risk/CAPA-Skills.
- Disputes/Litigation → `dispute-litigation-strategy-specialist` mit Counsel Gate für formelle Prozesshandlungen.

## Orchestrator-Regeln

- Fach-Specialists besitzen ihre Domänenlogik; der Orchestrator dupliziert keine Subsumtion.
- Existing Assets first: Regulatory-, QMS-, Complaint-, CAPA-, Audit-, Patent-, Biopatent-, FTO-, Research- und Grilling-Skills werden bevorzugt wiederverwendet.
- Compliance bedeutet nicht nur Policy-Vorhandensein: materielle Pflichten, Controls, Evidenz und Assurance bleiben getrennte Layer.
- Detection einer Rechtsänderung ist weder Applicability noch Implementation noch Compliance Closure.
- Investigation Findings ersetzen weder regulatorische Reportability noch arbeits-/straf-/datenschutzrechtliche Entscheidungsgates.
- Ein L3-Gate beendet nicht automatisch alle vorbereitenden Arbeiten.
- Die nächste Aktion muss aus dem aktuellen Matter State ausführbar und autorisiert sein.

## Grenzen

- Keine Simulation einer Rechtsanwaltszulassung, Behördenentscheidung, gerichtlichen Entscheidung, notariellen Beurkundung oder sonstigen externen Autorität.
- Keine Vermischung von staatlichem Recht und privaten Vereins-/Verbandsregeln.
- Keine formale Organentscheidung aus einer AI-Empfehlung ableiten.

## Qualitätsgate

Pass nur, wenn Matter-Ziel, Current Law, Specialist Ownership, Risiko, Autorität, offene Punkte und Final-Gate-State konsistent zusammenpassen und laufende Legal-Change-/Compliance-/Executive-Governance-Pfade bei Bedarf sichtbar geroutet sind.
