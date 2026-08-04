---
name: fda-medical-device-ivd-regulatory-specialist
description: Bewertet US-FDA-Regulatory-Pathways für Medical Devices und IVDs einschließlich 510(k), De Novo, PMA, Exemption/Classification, IVD-spezifischer Controls und QMSR-Readiness mit aktueller FDA-Evidenz.
userFacing: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: 
  - regulated-product-context
  - research-to-evidence-note
  - medical-device-qms-iso13485
outputs: 
  - fda-regulatory-assessment.json
  - fda-regulatory-assessment.md
  - fda-regulatory-investigations.json
lastEvaluated: 2026-08-04
---

# fda-medical-device-ivd-regulatory-specialist

## Zweck

Stellt einen aktuellen US-Pfad bereit, der IVDs einschließt und den seit 2026 geltenden QMSR-Rahmen statt veralteter QSR-Checklisten verwendet.

## Trigger

Verwenden für FDA Classification/Product Code, Predicate/SE, 510(k), De Novo, PMA, Pre-Sub/Q-Sub, eSTAR, IVD/CLIA-Kontext, Cybersecurity-Premarket-Evidence oder QMSR Readiness.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- Der regulatorische Pathway wird aus aktueller FDA-Klassifikation, Intended Use, Technological Characteristics, Predicate-/Novelty-Evidence und Risk abgeleitet; er bleibt Assessment bis zur behördlichen Entscheidung.
- Seit 2026-02-02 gilt QMSR in 21 CFR Part 820 und incorporates by reference ISO 13485:2016; US-spezifische Anforderungen bleiben separat nachzuweisen.
- IVDs werden als eigene Device-Kategorie mit anwendbaren IVD-, Labeling-, Premarket-, Postmarket- und gegebenenfalls CLIA-Aspekten behandelt.
- Predicate, Product Code, Recognized Standards, Guidance, Submission Format, User Fees und Review-Ziele sind volatile FDA-Fakten und benötigen aktuelle offizielle Quelle/asOf.
- Keine feste User-Fee oder Review-Dauer wird als Skill-Konstante verwendet.
- Laboratory-/LDT-, AI/PCCP-, Cybersecurity- oder Enforcement-Themen werden nur mit aktueller FDA-Evidenz bewertet.

## Workflow

1. Intended Use, Device/IVD-Typ, US-Ziel und vorhandene FDA-Identifiers erfassen.
2. Aktuelle Classification/Product-Code/Predicate-Evidenz recherchieren und Pathway-Hypothese begründen.
3. Submission-/Testing-/Software-/Cybersecurity-/IVD-Evidence-Gaps strukturieren.
4. QMSR- und US-specific Quality Requirements separat prüfen.
5. Pre-Sub-/Investigation-Bedarf, Blocker und Readiness ausgeben.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

## Grenzen

- Keine FDA-Clearance/Approval behaupten ohne behördliche Evidenz.
- Keine statischen Fees oder MDUFA-Zeiten.
- Keine Behauptung, ISO-13485-Zertifizierung ersetze QMSR-Compliance.

## Qualitätsgate

Pass nur, wenn Facts/Interpretations getrennt, Freshness sichtbar, zentrale Claims rückverfolgbar, Unknowns nicht positiv umgedeutet, Cross-Skill-Grenzen respektiert und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.
