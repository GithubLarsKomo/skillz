---
name: regulated-product-context
description: Normalisiert bestätigten Produkt-, Intended-Purpose-, Markt-, Lifecycle-, QMS-, Risiko-, Software-, AI-, Privacy- und Evidenzkontext für regulierte Medizinprodukte und IVDs, ohne Klassifikation oder Zulassung zu erfinden.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs: 
  - regulated-product-context.json
  - regulated-product-context.md
lastEvaluated: 2026-08-04
implicitInvocation: true
---

# regulated-product-context

## Zweck

Ein gemeinsamer, zeitpunktbezogener Produktkontext verhindert, dass nachgelagerte RA/QM-Skills dieselben Basisfragen erneut stellen oder widersprüchliche Annahmen verwenden.

## Trigger

Verwenden, wenn Grilling-Reports, Specs, technische Dokumentation oder Evidenz in eine gemeinsame Ausgangslage für Medical Device/IVD Engineering überführt werden sollen.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- Trenne Fakten, bestätigte Entscheidungen, Annahmen, Hypothesen, Unbekannte und Konflikte sichtbar.
- Kennzeichne Produktart mindestens als medical-device, ivd, samd, accessory, combination, other oder unknown.
- Behandle Intended Purpose, Claims, Zielpopulation, Anwender, Use Environment, Märkte und Lifecycle-Phase als explizite Felder.
- Bei IVD zusätzlich mindestens Specimen, Analyte/Measurand, Untersuchungsprinzip und qualitative/quantitative Nutzung erfassen, soweit bekannt.
- Regulatorische Klassifikation besitzt einen Evidenzstatus confirmed, hypothesis oder unknown; eine bloße Ableitung wird nie als behördlich bestätigt dargestellt.
- Jeder zeitabhängige regulatorische Fakt erhält asOf und Source-Referenz oder bleibt unknown.
- Software, Connectivity, AI/ML, personenbezogene Daten, besondere Kategorien personenbezogener Daten und Cybersecurity-Relevanz werden als eigener Kontext geführt.

## Workflow

1. Bestätigte Grilling-/Spec-/Repository- und Evidenzquellen inventarisieren.
2. Produkt, Intended Purpose/Claims, Märkte, Lifecycle, QMS, klinische bzw. Performance-Evidenz, Herstell-/Supplier-, Software/AI-, Security- und Privacy-Kontext normalisieren.
3. Widersprüche und fehlende entscheidungsrelevante Angaben markieren.
4. Stabile JSON-Sicht plus lesbares Markdown erzeugen.
5. Nur offene, entscheidungsrelevante Unsicherheiten als Investigations an large-work-wayfinder übergeben.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

## Grenzen

- Kein eigener regulatorischer Klassifizierer oder Zulassungsentscheid.
- Keine erneute Requirements-Befragung für bereits bestätigte Grilling-Inhalte.
- Keine Speicherung von Secrets oder unnötigen personenbezogenen Rohdaten.

## Qualitätsgate

Pass nur, wenn Facts/Interpretations getrennt, Freshness sichtbar, zentrale Claims rückverfolgbar, Unknowns nicht positiv umgedeutet, Cross-Skill-Grenzen respektiert und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.
