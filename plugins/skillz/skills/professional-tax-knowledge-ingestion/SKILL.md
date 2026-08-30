---
name: professional-tax-knowledge-ingestion
description: Extrahiert aus professionellen Tax-Quellen strukturierte Konzepte, Regeln, Strukturmuster, Practitioner-Heuristiken, Failure Patterns und Fallbeispiele, klassifiziert Evidenzqualität und Freshness und routet materielle Regeln zur Primärquellenverifikation, statt Kanzlei-, Video- oder Marketingcontent ungeprüft als Tax Authority zu speichern.
---

# Professional Tax Knowledge Ingestion

## Zweck

Professionelles Praxiswissen in eine verifizierbare Tax Knowledge Base überführen.

## Knowledge Types

- `tax-concept`
- `tax-rule`
- `tax-structure-pattern`
- `tax-practitioner-heuristic`
- `tax-failure-pattern`
- `tax-case-example`

## JUHN Seed Corpus

JUHN Website und der Kanal `@juhnsteuerberater` sind als priorisierte Practitioner-Seed-Quellen vorgesehen, insbesondere für Holding/Konzern, Umwandlung, M&A, International Tax, Betriebsprüfung/Einspruch, Unternehmensbesteuerung, ErbSt/SchenkSt und Immobilien. Website und Video werden thematisch verknüpft; Videos dienen besonders zur Extraktion von Beratungsheuristiken, typischen Mandantensituationen, Optionsvergleichen, Warnungen und Umsetzungssequenzen.

## Ingestion Workflow

1. Quelle und Veröffentlichungsdatum erfassen.
2. Content in fachlich kohärente Claims/Patterns segmentieren.
3. Knowledge Type und Tax Domains klassifizieren.
4. Normen, Entscheidungen, Behördenmaterial und externe Verweise extrahieren.
5. Marketingaussage, Interpretation, Fallbeschreibung und Rechtsregel trennen.
6. T3/T4-Claims mit materieller Relevanz in `tax-source-verification-queue.json` überführen.
7. Nur nach `current-tax-context`-Verifikation einen `tax-rule` als bestätigt behandeln.
8. Freshness und Supersession speichern.

## Qualitätsgate

Pass nur, wenn Source Tier, Knowledge Type, Zeitpunkt, fachliche Domain, Claim/Interpretation-Grenze und notwendige Primärquellenverifikation nachvollziehbar sind.
