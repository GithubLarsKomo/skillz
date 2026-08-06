---
name: evidence-based-causal-investigation
description: Untersucht Qualitäts-, Prozess-, Produkt-, Herstellungs-, Human-Factor- und Systemprobleme evidenzbasiert mit konkurrierenden Kausalhypothesen und verifiziertem oder ausdrücklich unbestätigtem Root Cause.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: 
  - research-to-evidence-note
outputs: 
  - causal-investigation.json
  - causal-investigation.md
lastEvaluated: 2026-08-04
implicitInvocation: true
---

# evidence-based-causal-investigation

## Zweck

Überträgt die Evidenzdisziplin von Softwarediagnosen auf nicht-softwarezentrierte Nonconformities, Complaints, Audit Findings und Prozessabweichungen.

## Trigger

Verwenden, wenn eine CAPA-, Nonconformity-, Complaint- oder Audit-Ursache untersucht werden muss und 5-Why/Fishbone/FMEA/FTA nicht als bloße Ritualmethoden genügen.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- Symptom, unmittelbare Ursache, beitragende Bedingung und Root Cause sind getrennte Begriffe.
- Eine Root-Cause-Behauptung benötigt unterscheidende Evidenz gegenüber plausiblen Alternativhypothesen.
- 5-Why, Ishikawa, FTA, FMEA, Fault Isolation oder Human-Factors-Methoden sind Werkzeuge, keine Beweise.
- Human error ist ohne Prüfung von System-, Prozess-, Training-, Interface-, Workload- und Kontrollbedingungen kein hinreichender Endpunkt.
- Containment, Correction, Corrective Action und Preventive/Systemic Action bleiben getrennt.
- Fehlende oder widersprüchliche Evidenz führt zu rootCause.status=unverified statt zu einer plausiblen Geschichte.

## Workflow

1. Problem und objektive Evidenz zeitlich und sachlich eingrenzen.
2. Konkurrierende Kausalhypothesen mit erwarteten Beobachtungen formulieren.
3. Mit unterscheidenden Nachweisen Hypothesen bestätigen, widerlegen oder offen lassen.
4. Root Cause und beitragende Bedingungen abgrenzen.
5. Nur evidenzgestützte Action Targets an CAPA/Risk/QMS übergeben.
6. Restrisiko und offene Untersuchungen dokumentieren.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

## Grenzen

- Keine automatische CAPA-Eröffnung oder Closure.
- Keine Schuldzuweisung an Personen.
- Keine Methode erzwingt eine bestimmte Anzahl von Why-Schritten oder Ursachen.

## Qualitätsgate

Pass nur, wenn Facts/Interpretations getrennt, Freshness sichtbar, zentrale Claims rückverfolgbar, Unknowns nicht positiv umgedeutet, Cross-Skill-Grenzen respektiert und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.
