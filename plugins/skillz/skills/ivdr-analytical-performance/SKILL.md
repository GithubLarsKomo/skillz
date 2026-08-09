---
name: ivdr-analytical-performance
description: Bewertet analytische IVD-Leistungsmerkmale evidenzgebunden, verknüpft Methoden, Akzeptanzkriterien, Ergebnisse und Gaps.
---

# IVDR Analytical Performance

## Zweck und Grenze

Dieser Skill plant und bewertet analytische Leistungsmerkmale eines IVD gegen den konkreten Intended Purpose. Er verbindet Merkmale, Methoden, Akzeptanzkriterien, Ergebnisse, Unsicherheiten und Gaps zu einer nachvollziehbaren Evidence-Struktur.

Er ist kein generischer Laborstatistik-Skill, kein Ersatz für produktbezogenes Risikomanagement und keine Gesamt-Performance-Evaluation. Konkrete statistische Verfahren werden passend zu Messprinzip, Datentyp, Claim und anerkannten Methoden ausgewählt; der Skill erfindet keine universelle Pflichtliste.

## Kernprinzipien

- Analytical Performance wird vom Intended Purpose und den Claims rückwärts geplant.
- Relevante Merkmale werden begründet ausgewählt; nicht jedes denkbare Merkmal ist automatisch erforderlich.
- Akzeptanzkriterien werden vor Interpretation der Ergebnisse nachvollziehbar festgelegt oder als post hoc markiert.
- Methode, Probenmaterial, Konzentrationsbereich, Replikationsstruktur, Lots/Operatoren/Instrumente/Sites und Statistik werden so dokumentiert, dass Übertragbarkeit und Limitationen prüfbar sind.
- Standards und CLSI-Dokumente dienen als methodische Evidenz, ersetzen aber nicht die produktspezifische Begründung.
- Abweichungen und unerwartete Resultate werden an Risk/CAPA/Investigation weitergegeben statt im Bericht geglättet.

## Workflow

### 1. Claim-to-Characteristic-Matrix

Leite aus Intended Purpose und Claims die analytisch zu belegenden Merkmale ab. Typische Kategorien können Präzision, Wiederholbarkeit/Reproduzierbarkeit, Bias/Trueness, Messbereich, Nachweis-/Bestimmungsgrenzen, analytische Spezifität, Interferenzen, Carryover, Stabilität und metrologische Rückführbarkeit umfassen, soweit relevant.

### 2. Evidenz und Methode festlegen

Verknüpfe für jedes Merkmal Requirement, Methode, Proben-/Panelstrategie, Akzeptanzkriterium, statistische Auswertung und Source References über `regulatory-evidence-traceability`.

### 3. Risikobezogene Priorisierung

Nutze `medical-device-risk-management-iso14971`, um kritische Claims, Grenzbereiche und Fehlermodi in Umfang und Akzeptanzkriterien einfließen zu lassen. Der Skill führt kein zweites Risk Register.

### 4. Plan bewerten oder erzeugen

`analytical-performance-plan.json` kann einen neuen Plan oder die strukturierte Rekonstruktion eines bestehenden Protokolls enthalten. Fehlende Vorabkriterien, unzureichende Range-Abdeckung oder unklare Replikationsstruktur werden als Gaps markiert.

### 5. Ergebnisse bewerten

Ordne Ergebnisse den vorab definierten Kriterien zu. Trenne `meets|does-not-meet|inconclusive|not-assessed`. Post-hoc-Akzeptanzkriterien, ausgeschlossene Daten und Abweichungen bleiben sichtbar.

### 6. Gap-to-Action schließen

Gaps erhalten einen konkreten nächsten Schritt: zusätzliche Studie, gezielte Wiederholung, Ursachenuntersuchung, Claim-Anpassung, Risk-Update oder Begründung der Nicht-Anwendbarkeit.

## Output-Verträge

`analytical-performance-plan.json` enthält Claims, Merkmale, Methoden, Designparameter, Akzeptanzkriterien, Statistik, Risk/Evidence References und geplante Stop-/Decision-Regeln.

`analytical-performance-assessment.json` enthält pro Merkmal Evidenz, Ergebnisstatus, Abweichungen, Limitationen, Gaps und `assessmentState`.

`analytical-performance-report.md` fasst Scope, Methoden, Ergebnisse, Kriterien, Limitationen und offene Gaps zusammen.

## Downstream

Primärer Consumer ist `ivdr-performance-evaluation`. Findings können `medical-device-risk-management-iso14971`, `evidence-based-causal-investigation`, `medical-device-capa`, `design-change-regulatory-impact` oder kontrollierte Dokumentation triggern.

## Memory Path

Persistenzwürdig sind bestätigte produktspezifische analytische Constraints, wiederverwendbare Study-Design-Muster und validierte Failure-/Acceptance-Heuristiken. Einzelne Resultate, aktuelle Messdaten, offene Abweichungen und unbestätigte statistische Hypothesen bleiben run-only. Kandidaten tragen `sourceRefs`; methoden- oder guidanceabhängige Aussagen zusätzlich `asOf` und bei erwartbarer Änderung `reviewAfter`. Übergib geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; dieser Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- jedes relevante Merkmal auf Claim/Intended Purpose zurückgeführt ist,
- Methode und Akzeptanzkriterium nachvollziehbar begründet sind,
- post-hoc-Kriterien und ausgeschlossene Daten sichtbar bleiben,
- Risk References genutzt werden, ohne Risk Management zu duplizieren,
- nicht erfüllte oder inkonklusive Ergebnisse als Gaps erhalten bleiben,
- Downstream die Ergebnisse ohne mündliche Zusatzannahmen übernehmen kann,
- Memory Candidates keine transienten Messresultate dauerhaft machen.
