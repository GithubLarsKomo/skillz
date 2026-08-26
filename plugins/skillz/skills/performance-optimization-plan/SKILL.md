---
name: performance-optimization-plan
description: Überführt gemessene Hotspots und priorisierte Optimierungskandidaten in ein belastbares Performance-Konzept und eine agententaugliche TASK.md mit Performance-Budget, funktionalen Invarianten, kleinen Umsetzungsslices, Messplan, Rollback und ausdrücklich verworfenen Alternativen. Verwenden nach Profiling/Hotspot-Analyse und vor Codeänderungen.
---

# Performance Optimization Plan

Wandle Messdaten in einen begrenzten, ausführbaren Optimierungsauftrag um. Plane keine spekulativen Rewrites und keine Änderung ohne überprüfbare Erfolgsbedingung.

## Eingang

- `performance-baseline.json`
- `hotspot-map.json`
- `optimization-candidates.json`
- Architektur-, Kompatibilitäts- und Betriebsgrenzen
- funktionale Invarianten

Wenn der Kandidat Modulgrenzen, Persistenzmodell oder Infrastruktur wesentlich verändert, nutze `architecture-deepening-review` für den kleinsten gerechtfertigten Architektur-Schritt.

## Ablauf

1. Optimierungsziel als beobachtbares Budget formulieren, z. B. p95-Latenz, Batch-Laufzeit, Query-Anzahl, Peak Memory, Build-Zeit oder Ressourcenverbrauch.
2. Die kleinste Kombination von Kandidaten wählen, die das Ziel plausibel erreicht.
3. Alternativen mit erwarteter Wirkung, Risiko und Ablehnungsgrund dokumentieren, damit spätere Iterationen sie nicht ohne neue Evidenz wiederholen.
4. Änderung in kleine, unabhängig prüfbare Slices schneiden. Jeder Slice muss einen Hotspot adressieren und einen eigenen funktionalen sowie Performance-Nachweis besitzen.
5. Reihenfolge nach Abhängigkeiten und Informationsgewinn bestimmen: risikoarme, hochwirksame Ursachenbehebung vor komplexen Optimierungen.
6. Für Cache, Parallelisierung, asynchrone Verarbeitung, Index-/Schemaänderungen oder Architekturänderungen spezifische Korrektheitsrisiken festhalten, z. B. Staleness, Invalidierung, Race Conditions, Locking, Ordering, Transaktionen und Rollback.
7. Rollback- und Messstrategie festlegen.

## PERFORMANCE_PLAN.md

Enthält mindestens:

- Problem und Ziel
- Baseline und relevante Hotspots
- Root Causes
- ausgewählte Optimierungen
- verworfene Alternativen mit Grund
- erwarteten Effekt und Confidence
- betroffene Komponenten
- funktionale Invarianten
- Kompatibilitäts-/Betriebsgrenzen
- Risiken
- Mess- und Benchmarkplan
- Rollback
- Definition of Done

## TASK.md

`TASK.md` ist unmittelbar für Coding-Agenten ausführbar und enthält mindestens:

- `Objective`
- `Baseline`
- `Performance Gate`
- `Functional Gate`
- `Scope`
- `Out of Scope`
- `Constraints`
- geordnete Checkbox-Tasks
- pro Task betroffene Komponente/Datei soweit bekannt
- geforderte Tests und Benchmark-Wiederholung
- erwartete Abschlussdokumentation

Keine vagen Tasks wie `optimize application`. Formuliere z. B. `N+1 supplier lookup durch Bulk Lookup ersetzen und Query-Anzahl für 50k-Import von ~50k auf <50 reduzieren`.

## Abschluss

Der Skill endet, wenn `PERFORMANCE_PLAN.md` die Entscheidung begründet und `TASK.md` ohne weitere Produktentscheidung implementierbar ist. Offene irreversible Entscheidungen bleiben Blocker und dürfen nicht als Annahme versteckt werden.
