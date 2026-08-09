---
name: medical-device-qms-iso13485
description: Bewertet und strukturiert ein Medical-Device-/IVD-QMS gegen ISO 13485 sowie anwendbare regulatorische Ergänzungen, ohne Zertifizierung, FDA-Compliance oder feste Organisationsprozesse zu erfinden.
---

# medical-device-qms-iso13485

## Zweck

Stellt QMS-Scope, Prozesse, Evidence Gaps und regulatorische Schnittstellen so bereit, dass Engineering, Audit, CAPA und Management Review dieselbe Grundlage verwenden.

## Trigger

Verwenden für ISO-13485-QMS-Aufbau/Remediation, QMSR-Gap-Analyse, Supplier Quality, Process Validation, Design/Development-QMS-Integration oder digitale/eQMS-Readiness.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- ISO 13485:2016 ist der aktuelle internationale QMS-Referenzstandard; konkrete Klauselbehauptungen benötigen autoritative Evidenz.
- Für die USA gilt seit 2026-02-02 QMSR in 21 CFR Part 820 mit Incorporation by Reference von ISO 13485:2016; ISO-Zertifizierung allein beweist keine FDA-Compliance.
- QMS-Scope, regulatorische Rollen, Prozesslandschaft, Interaktionen, Records und Verantwortlichkeiten bleiben explizit.
- Supplier Controls, Process Validation, Design/Development, Complaint/CAPA, Audit und Management Review werden als verknüpfte Prozesse behandelt, nicht als isolierte Checklisten.
- Part 11/Annex 11/eQMS-Anforderungen werden nur bei anwendbarem digitalen Record-/Signature-Kontext geprüft.
- Missing evidence bleibt gap/unknown und wird nicht durch typische SOP-Listen geschlossen.

## Workflow

1. Organisations-/Produkt-/Markt-Scope und anwendbare Regulatory Requirements festlegen.
2. QMS-Prozesse und Interfaces kartieren.
3. Anforderungscoverage und Evidenzwirksamkeit über two-axis-compliance-review prüfen.
4. Process-/Supplier-/Validation-/Document-/CAPA-/Audit-Gaps priorisieren.
5. Readiness, Blocker, Investigations und sichere nächste Schritte ausgeben.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

## Grenzen

- Keine Zertifizierungszusage.
- Kein Ersatz für product-specific Design Inputs/Outputs oder Testprotokolle.
- Keine Behauptung, QMSR sei identisch mit ISO 13485 ohne US-spezifische Ergänzungen.

## Qualitätsgate

Pass nur, wenn Facts/Interpretations getrennt, Freshness sichtbar, zentrale Claims rückverfolgbar, Unknowns nicht positiv umgedeutet, Cross-Skill-Grenzen respektiert und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.
