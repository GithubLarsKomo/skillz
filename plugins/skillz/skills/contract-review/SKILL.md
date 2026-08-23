---
name: contract-review
description: Bewertet einen hochgeladenen oder als Text bereitgestellten privaten oder beruflichen Vertrag einschließlich Anlagen und AGB gegen bestätigte Requirements, Rechtsgrundlagen und wirtschaftlich-operative Risiken und erzeugt eine priorisierte Issue-Liste mit Verhandlungspositionen. Verwenden für Vertragsprüfung, Risikoanalyse und Redline-Vorbereitung, nicht für die initiale Vertragserzeugung.
---

# Contract Review

## Zweck und Grenze

Dieser Skill bewertet einen **vorhandenen Vertrag oder Vertragsset**. Er trennt juristische, wirtschaftliche, operative und redaktionelle Findings und priorisiert sie für Entscheidung und Verhandlung.

Er erzeugt keine definitive Aussage wie „rechtswirksam“ oder „gerichtsfest“, wenn Rechtsgrundlage, Sachverhalt oder Rechtsprechung dies nicht belastbar erlauben. Er ersetzt kein erforderliches qualifiziertes Legal Review.

## Dokumentaufnahme

Akzeptiere insbesondere DOCX, PDF, Text und mehrere zusammengehörige Dokumente. Bei mehreren Dateien:

1. Hauptvertrag bestimmen.
2. Anlagen, SOW, SLA, Preislisten, AGB, DPA, Policies und referenzierte Dokumente zuordnen.
3. Rangfolgeklauseln und Incorporation-by-reference erfassen.
4. Fehlende referenzierte Dokumente als `missingReferencedDocument` markieren.
5. Originale unverändert lassen und für jede Quelle soweit möglich Version/Hash/Dateiname erfassen.

Wenn Inhalte unlesbar oder unvollständig sind, keine Lücken erfinden. Bei Scan-/Parsing-Problemen konkrete Seiten oder Abschnitte als nicht verifizierbar kennzeichnen.

## Voraussetzung

Ein aktuelles `contract-legal-context.json` muss vorliegen oder erzeugt werden. Außerdem müssen Zweck, Vertragsrolle des Nutzers und wesentliche Must-haves bekannt sein; fehlende fachliche Entscheidungen gehen über `contract-workflow` zu Grilling zurück.

## Review-Dimensionen

Prüfe mindestens, soweit einschlägig:

- Parteien, Vertretung, Präambel und Vertragsgegenstand,
- Scope, Deliverables, Abhängigkeiten, Leistungsort, Termine und Change Control,
- Preis, Steuern, Währung, Zahlungsbedingungen und Preisanpassung,
- Abnahme, Gewährleistung, Garantien, Service Levels und Remedies,
- Laufzeit, Verlängerung, Kündigung, Suspendierung und Exit/Transition,
- Haftung, Haftungsdeckel, Ausschlüsse, Freistellungen und Versicherungen,
- Vertraulichkeit und Veröffentlichungsrechte,
- IP, Background/Foreground IP, Nutzungsrechte, Lizenzumfang und Drittanbieterrechte,
- Datenschutz, Datennutzung, Security, Unterauftragnehmer und internationale Transfers,
- Compliance, Audit, Dokumentation und regulatorische Pflichten,
- Exklusivität, Wettbewerbsverbote, Mindestabnahmen und Lock-in,
- Assignment, Change of Control, Subcontracting,
- Force Majeure / Hardship,
- Rechtswahl, Gerichtsstand, Schiedsverfahren und Streitbeilegung,
- Form, Notices, Entire Agreement, Severability und Survival,
- Definitionen, Querverweise, Anlagen, Rangfolge, Widersprüche und offene Platzhalter.

## Klauselbewertung

Jedes materielle Finding erhält:

- `issueId`, `location`, `clauseTopic`,
- `findingType`: `legal | commercial | operational | drafting | missing-term | cross-document-conflict`,
- `riskLevel`: `critical | high | medium | low | note`,
- `userImpact`,
- `legalBasis` nur soweit verifiziert,
- `whyItMatters`,
- `recommendedAction`: `must-fix | negotiate | accept-or-monitor | verify-facts | counsel-review`,
- `preferredPosition`, `fallbackPosition`, `redLine` soweit ableitbar,
- `proposedChange` als präzise Änderungsanweisung oder Klauselvorschlag,
- `confidence` und `openFacts`.

Risiko wird nicht allein aus „ungewöhnlicher“ Formulierung abgeleitet. Berücksichtige Wahrscheinlichkeit, Schadenshöhe, Kontrollierbarkeit, Reversibilität, operative Eintrittswahrscheinlichkeit und Verhandlungskontext.

## Cross-Clause Review

Nach Einzelklauseln zwingend einen zweiten Pass durchführen auf:

- widersprüchliche Definitionen,
- Haftung versus Freistellung versus Versicherung,
- Laufzeit versus Kündigung versus Preisbindung,
- IP versus Vertraulichkeit versus Datennutzung,
- Leistungspflichten versus SLA/Abnahme/Remedies,
- Hauptvertrag versus Anlagen/AGB,
- Rechtswahl versus Gerichtsstand/Arbitration,
- Rangfolgen und Survival.

## AGB-/Formularvertrag-Gate

Wenn vorformulierte Bedingungen vorliegen, markiere die AGB-Relevanz aus dem Legal Context. Unterscheide B2C und B2B; behandle Individualabreden und tatsächlich ausgehandelte Klauseln gesondert. Keine pauschale Gleichsetzung von B2B mit „AGB-Kontrolle irrelevant“.

## Ausgabe

`contract-review.json` enthält Summary, Dokumentset, Legal-Context-Version, Gesamtrisiko, Findings, Cross-Clause-Findings, Missing Documents, Material Unknowns und Escalations.

`contract-review.md` enthält:

1. Executive Summary,
2. Top-Risiken,
3. Klausel-für-Klausel-Bewertung,
4. fehlende oder schwache Regelungen,
5. Verhandlungsplan,
6. Final-Gate-Status.

`contract-issue-list.json` ist die kompakte, sortierbare Arbeitsliste für Revision/Verhandlung.

## Prüfungen

Pass nur wenn das gesamte relevante Dokumentset berücksichtigt wurde; Findings konkrete Fundstellen besitzen; Recht, Wirtschaft und Operations getrennt werden; B2C/B2B und AGB-Kontext korrekt geroutet sind; keine unlesbaren Passagen erfunden werden; Cross-Clause-Konflikte geprüft werden; Top-Risiken priorisiert und konkrete nächste Aktionen angegeben werden; Material Unknowns und Counsel-Eskalationen sichtbar bleiben.

## Abschluss

Der Skill endet mit einer nachvollziehbaren, priorisierten Vertragsbewertung, die direkt in Verhandlung, Revision oder qualifiziertes Legal Review übergeben werden kann.
