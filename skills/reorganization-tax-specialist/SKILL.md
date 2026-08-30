---
name: reorganization-tax-specialist
description: Analysiert deutsche Umwandlungs- und Einbringungssteuer-Matters einschließlich Verschmelzung, Spaltung, Formwechsel, Einbringung, Anteilstausch, Wertansätzen, Sperrfristen und Nachversteuerungsrisiken und hält Legal-, VAT-, RETT-, Verlust-, Organschafts- und internationale Abhängigkeiten getrennt.
userFacing: true
implicitInvocation: true
category: tax-specialist
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-tax-context
  - tax-position-register
  - tax-structure-pattern-library
outputs:
  - reorganization-tax-assessment.json
  - reorganization-tax-structure-options.json
  - reorganization-tax-step-plan.json
  - reorganization-tax-open-issues.json
lastEvaluated: 2026-08-31
---

# Reorganization Tax Specialist

## Zweck

Strukturiere deutsche Reorganization-Tax-Fragen als steuerliche Fachschicht. Der Skill entscheidet nicht den gesellschaftsrechtlichen Umwandlungsmechanismus; Legal und Tax bleiben getrennte Owner.

## Scope

Behandle insbesondere:

- Verschmelzung, Spaltung, Abspaltung, Ausgliederung und Formwechsel,
- Einbringung von Betrieben, Teilbetrieben, Mitunternehmeranteilen oder Anteilen,
- Anteilstausch und mehrstufige Holding-/Reorganization-Sequenzen,
- Buchwert-, Zwischenwert- und gemeiner-Wert-Szenarien,
- Sperrfristen, Nachversteuerung und schädliche Folgetransaktionen,
- Steuerbilanz-/Übertragungsstichtage und Sequenzabhängigkeiten,
- Reorganization-Schritte vor oder nach M&A-/Nachfolge-/Finanzierungsmaßnahmen.

## Reorganization Model

Für jede Option mindestens dokumentieren:

1. Ausgangs- und Zielstruktur,
2. beteiligte Rechtsträger, Beteiligungen und Wirtschaftsgüter,
3. gewünschtes wirtschaftliches Ziel,
4. steuerlich relevanten Reorganization-Tatbestand und Zeitraum,
5. mögliche Wertansätze und deren Voraussetzungen,
6. Sperrfristen, Haltebedingungen und Nachversteuerungsrisiken,
7. Schrittfolge und Abhängigkeiten,
8. unmittelbare und spätere Steuerfolgen,
9. offene Legal-, Accounting-, Valuation- und andere Tax-Interfaces,
10. einfachere Alternative und Status quo.

## Current Authority Gate

Konkrete Voraussetzungen, Wertansatzwahl, Fristen und Rechtsfolgen immer über `current-tax-context` gegen die für den Zeitraum geltende Fassung des UmwStG, einschlägige Steuer-/Umwandlungsnormen, aktuelle BMF-Verwaltung und Rechtsprechung prüfen. Practitioner Patterns ersetzen diese Prüfung nicht.

## Cross-Tax Interfaces

Nicht im Reorganization Skill improvisieren:

- Verlustnutzung/Organschaft/Corporate Tax -> `german-corporate-tax-specialist`,
- Cross-border/DBA/EU/Exit Tax -> `international-tax-specialist`,
- VAT -> `vat-indirect-tax-specialist`,
- M&A Deal Economics -> `ma-tax-specialist`,
- Transfer Pricing/Funktionsverlagerung -> `transfer-pricing-specialist`,
- Grunderwerbsteuer, Erb-/SchenkSt oder andere noch nicht abgedeckte Spezialthemen -> strukturierte Work Order bzw. Capability Gap.

## Legal Interface

Verschmelzungsvertrag, Spaltungsplan, Einbringungsvertrag, gesellschaftsrechtliche Wirksamkeit, Register-/Notarfragen, Gewährleistungen und Closing Mechanics bleiben beim Legal Owner. Übergib steuerliche Constraints über `tax-legal-interface-specialist`; Tax bestimmt nicht den Legal Mechanism.

## Practitioner Knowledge

JUHN und vergleichbare Kanzleiquellen sind Seed Sources für typische Holding-, Einbringungs-, Spaltungs- und Sequenzmuster sowie Failure Patterns. Kennzeichne sie als Practitioner/Discovery Evidence und verifiziere materielle Voraussetzungen über höhere Evidence Tiers.

## Professional Gate

Materielle individuelle Reorganization-Tax-Positionen, Wahlrechtsausübungen, steuerliche Erklärungen oder Vertretung benötigen bei entsprechender berufsrechtlicher Reserved Work `tax-professional-routing`. Vorbereitung, Variantenvergleich und Evidence Package laufen bis zum Gate weiter.

## Qualitätsgate

Pass nur, wenn Ausgangs-/Zielstruktur, Wertansatzoptionen, Sequenz, Sperrfristen, aktuelle Authority, Cross-Tax-/Legal-Dependencies, Alternativen und Professional Gate sichtbar und voneinander getrennt sind.