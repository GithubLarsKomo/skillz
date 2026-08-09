---
name: medical-device-privacy-gdpr-bdsg
description: Bewertet Datenschutz für Medical-Device-/IVD- und Health-Software-Kontexte unter GDPR/DSGVO und deutschem BDSG mit Data Inventory, Rollen, Legal Basis, Art.-9-Kontext, DPIA, Rights, Retention, Transfers und Breach Governance.
---

# medical-device-privacy-gdpr-bdsg

## Zweck

Verbindet Privacy-Anforderungen mit Engineering-Datenflüssen, ohne Regex-Scanner oder Prozentwerte als Rechtskonformität auszugeben.

## Trigger

Verwenden für personenbezogene/gesundheitsbezogene Daten, Controller/Processor-Rollen, Legal Basis, Special Categories, DPIA, Data Subject Rights, Retention/Deletion, Transfers, Processor Governance oder Breach Assessment.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- Data Inventory und Datenflüsse gehen der Compliance-Bewertung voraus; Code-/Pattern-Scanner liefern nur potentielle Privacy-Signale.
- Controller/Processor/Joint-Controller-Rollen, Zwecke, Kategorien, Empfänger, Transfers, Retention und Löschung werden explizit dokumentiert.
- Legal Basis nach Art. 6 und gegebenenfalls Special-Category-Bedingung nach Art. 9 werden getrennt betrachtet; keine Basis wird aus technischer Notwendigkeit erfunden.
- DPIA-Notwendigkeit wird aus aktueller rechtlicher/aufsichtlicher Evidenz und Verarbeitungskontext abgeleitet; Ergebnis kann required, not-required oder unresolved sein.
- Data Subject Rights und Breach Fristen/Prozesse werden nicht als erledigt markiert, solange externe organisatorische Evidenz fehlt.
- Ein Compliance Score aus Pattern Matching ist kein GDPR-Nachweis.

## Workflow

1. Processing Activities und Datenflüsse erfassen.
2. Rollen, Zwecke, Legal Basis/Special Categories, Empfänger/Transfers und Retention prüfen.
3. DPIA Threshold/Scope evidenzbasiert bewerten.
4. Rights, Security/Incident und Processor Controls auf Evidence prüfen.
5. Gaps, Investigations, Engineering Requirements und Governance Actions ausgeben.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

## Grenzen

- Keine Rechtsberatung oder behördliche Entscheidung vortäuschen.
- Keine personenbezogenen Beispieldaten unnötig persistieren.
- Keine Compliance-Prozentbewertung aus Code-Scanning.

## Qualitätsgate

Pass nur, wenn Facts/Interpretations getrennt, Freshness sichtbar, zentrale Claims rückverfolgbar, Unknowns nicht positiv umgedeutet, Cross-Skill-Grenzen respektiert und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.
