---
name: tax-advisory-office
description: Orchestriert steuerliche Matters als Schwesterorganisation der Legal & Compliance Office von Intake, Current Tax Context und Specialist Routing über Tax Position, Szenarien und Professional Review bis zu Filing, Bescheid, Einspruch und Follow-up, ohne Fachlogik der Tax Specialists zu duplizieren oder eine Steuerberaterzulassung zu simulieren.
---

# Tax Advisory Office

## Zweck

Dünner Tax-Orchestrator. Er hält steuerliches Ziel, Facts, Evidenz, Positionen, Specialist-Arbeit, Berechnungen, Professional-Authority und nächste Aktion zusammen. Er trifft keine zweite fachliche Steuerentscheidung neben den Specialists und ersetzt keine nach StBerG befugte Person.

Die Tax Advisory Office ist Peer der `legal-compliance-office`. Legal besitzt den rechtlichen Mechanismus; Tax besitzt die steuerliche Analyse und wirtschaftliche Steuerwirkung. Gemeinsame Matters werden über explizite Work Orders und Decision Dependencies verbunden.

## Matter-Ablauf

1. Matter mit `tax-matter-intake` strukturieren.
2. Jurisdiktion, Steuerarten, Zeitraum und Fristen festlegen.
3. `current-tax-context` ausführen und Quellenstand binden.
4. Bei fehlenden Facts vorhandenes Grilling wiederverwenden.
5. Fachfragen über `tax-specialist-router` routen.
6. Positionen im `tax-position-register` mit Evidenz, Alternativen und Status halten.
7. Strukturgestaltungen über `tax-structure-pattern-library` nur als Optionen modellieren; keine Pattern-Automatik als Empfehlung behandeln.
8. Materielle individuelle Positionen durch `tax-professional-routing` auf erforderliche Befugnis/Review routen.
9. Bei Legal Dependencies `tax-legal-interface-specialist` bzw. Legal Office anbinden.
10. Vor Filing, Einspruch, Umsetzung oder Abschluss `tax-matter-final-gate` ausführen.

## Operating Loop

`Tax Change -> Applicability -> affected Tax Positions -> Recalculation -> Risk/Opportunity -> Decision -> Filing/Amendment/Action -> Evidence -> Monitoring`.

## Shared-Primitives-Regel

Bestehende Skillz-Fähigkeiten für Research, Evidence, Grilling, Decision Records, Dokumentation, Handoffs und Monitoring werden wiederverwendet. Tax dupliziert diese Fachlogik nicht.

## Professional Boundary

- T0: AI-gestützte Vorbereitung, Facts, Research, Berechnungen, Szenarien und Entwürfe.
- T1: Mandant/Management entscheidet wirtschaftliche Ziele, Optionen und Risikotoleranz.
- T2: befugter Tax Professional validiert individuelle materielle Steuerpositionen, soweit erforderlich.
- T3: Finanzverwaltung, Gericht oder sonstige externe Authority entscheidet.

Ein T2/T3-Gate stoppt vorbereitende Arbeit nicht. Das Office erstellt ein eng umrissenes Professional Work Package.

## Qualitätsgate

Pass nur, wenn Taxpayer/Entity, Zeitraum, Jurisdiktion, Steuerarten, Facts, Quellenstand, Specialist Ownership, Positionen, offene Legal-/Accounting-/Valuation-Dependencies, Professional Authority, Fristen und nächste sichere Aktion getrennt nachvollziehbar sind.
