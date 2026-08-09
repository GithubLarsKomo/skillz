---
name: two-axis-compliance-review
description: Prüft regulierte Anforderungen getrennt nach Anwendbarkeit/Abdeckung und nach Evidenz/Wirksamkeit, damit fehlende Nachweise nicht als Compliance und grüne Checklisten nicht als effektive Controls gelten.
---

# two-axis-compliance-review

## Zweck

Stellt einen gemeinsamen Review-Kern für QMS-, ISMS-, Regulatory- und Privacy-Assessments bereit.

## Trigger

Verwenden, wenn eine Gap Analysis, Audit-Readiness, technische Dokumentation, Control-Implementierung oder regulatorische Anforderung bewertet wird.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- Achse 1 bewertet requirement applicability und coverage; Achse 2 bewertet evidence sufficiency und control/process effectiveness.
- Jede normative Aussage verweist auf eine regulatorische Quelle, einen Standard, Guidance, Organisationspolicy oder ausdrücklich markierte Interpretation.
- Missing evidence ist unknown oder gap, niemals compliant.
- Ein Compliance-Prozentscore darf höchstens als organisationsdefinierter Indikator erscheinen und ersetzt keine Einzelbefunde.
- Audit-Finding-Schweregrade, Samplegrößen und Fristen werden nicht als universelle Normvorgaben erfunden.
- Eine positive Gesamtentscheidung setzt voraus, dass keine entscheidende Anforderung oder Evidenzlücke verborgen bleibt.

## Workflow

1. Scope, Jurisdiktion, Kriterien und asOf fixieren.
2. Anforderungen inventarisieren und Anwendbarkeit mit Evidenzstatus bestimmen.
3. Coverage unabhängig von Evidenzqualität bewerten.
4. Nachweise, Stichprobenlogik und Wirksamkeit getrennt prüfen.
5. Widersprüche, unknowns und Finding-Kandidaten ableiten.
6. Review-Entscheidung mit Restrisiken und nächstem verifizierbaren Schritt erzeugen.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

## Grenzen

- Kein Ersatz für Zertifizierer, Benannte Stelle, Behörde oder Rechtsberatung.
- Keine automatische Freigabe nur wegen vollständiger Dokumentenliste.
- Keine universellen Audit-Samplegrößen oder Finding-Klassen erfinden.

## Qualitätsgate

Pass nur, wenn Facts/Interpretations getrennt, Freshness sichtbar, zentrale Claims rückverfolgbar, Unknowns nicht positiv umgedeutet, Cross-Skill-Grenzen respektiert und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.
