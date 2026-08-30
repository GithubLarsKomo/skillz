---
name: tax-structure-pattern-library
description: Modelliert wiederkehrende steuerliche Gestaltungs- und Strukturmuster wie Holding, Einbringung, Umwandlung, Nachfolge oder Cross-Border-Struktur als vergleichbare Patterns mit Voraussetzungen, Steuerwirkungen, Sperrfristen, Kosten, Risiken, Legal Dependencies und einfacheren Alternativen, ohne Pattern automatisch als Empfehlung auszugeben.
userFacing: true
implicitInvocation: true
category: tax-specialist
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-tax-context
outputs:
  - tax-structure-pattern.json
  - tax-structure-options.json
  - tax-structure-risk-map.json
lastEvaluated: 2026-08-30
---

# Tax Structure Pattern Library

## Zweck

Strukturwissen aus Praxisfällen und Fachquellen wiederverwendbar machen, ohne Beratung auf Marketing- oder Musterlogik zu reduzieren.

## Pattern Contract

Erfasse mindestens `name`, `objective`, `startingStructure`, `targetStructure`, `steps`, `legalTransactions`, `taxRegimes`, `requirements`, `blockingConditions`, `sperrfristen`, `taxEffects`, `legalEffects`, `cashEffects`, `setupCost`, `operatingCost`, `complexityCost`, `exitConstraints`, `alternatives`, `failureModes`, `authorityRefs`, `practitionerRefs`, `lawAsOf` und `professionalReviewRequired`.

## Practitioner Sources

JUHN und vergleichbare Kanzleiquellen sind besonders geeignet, um Patterns, typische Sequenzen, Warnungen und Beratungsheuristiken zu entdecken. Sie bestätigen aber weder Tatbestandsvoraussetzungen noch individuelle Eignung. Materielle Regeln müssen über `current-tax-context` gegen höhere Evidence Tiers verifiziert werden.

## Comparison Gate

Komplexe Struktur immer mindestens gegen eine einfachere Alternative und den Status quo vergleichen. Steuerquote allein ist kein ausreichendes Entscheidungskriterium; Liquidität, Transaktionskosten, laufende Compliance, Flexibilität, Exit und Legal Constraints mitführen.

## Qualitätsgate

Pass nur, wenn Nutzenbedingungen, Nicht-Eignungsbedingungen, Voraussetzungen, Risiken, Kosten, Alternativen und aktuelle Authority getrennt dokumentiert sind.