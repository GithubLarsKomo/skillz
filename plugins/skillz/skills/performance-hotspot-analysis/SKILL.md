---
name: performance-hotspot-analysis
description: Analysiert eine belastbare Performance-Baseline zusammen mit Profiling-, Query-, Trace- oder Laufzeitevidenz, lokalisiert dominierende Hotspots und klassifiziert Root Causes nach Algorithmus, unnötiger Arbeit, Datenbank, I/O, Netzwerk, Serialisierung, Cache, Parallelisierung, Runtime, Speicher, Architektur oder Build-Tooling. Verwenden vor einer Performance-Optimierung, um Mikrooptimierung nach Bauchgefühl zu vermeiden.
---

# Performance Hotspot Analysis

Bestimme zuerst, wo Zeit oder Ressourcen tatsächlich verloren gehen. Der Skill verändert keinen Produktivcode.

## Eingang

- `performance-baseline.json`
- Quellcode und relevante Architektur-/Runtime-Evidenz
- Profiling, Tracing, Query-Pläne, Logs oder gleichwertige Messdaten, soweit verfügbar

## Root-Cause-Taxonomie

Klassifiziere Hotspots bevorzugt als:

- `algorithm-data-structure`
- `unnecessary-work`
- `database`
- `disk-io`
- `network-api`
- `serialization`
- `cache`
- `parallelism-concurrency`
- `runtime-process-overhead`
- `memory-allocation`
- `architecture-boundary`
- `build-tooling`

Mehrfachzuordnung ist zulässig, wenn die Evidenz mehrere Ursachen trägt.

## Ablauf

1. Prüfen, ob Baseline und Workload für die Fragestellung repräsentativ sind. Bei unbrauchbarer Baseline an `performance-baseline` zurückgeben.
2. Gesamtzeit/-ressource in dominante Anteile zerlegen. Pareto-Prinzip als Heuristik, nicht als Beweis verwenden.
3. Für jeden relevanten Hotspot konkrete Evidenz auf Datei/Funktion/Query/Service/Call-Path beziehen.
4. Ursache von Symptom trennen. Beispiel: eine langsame Schleife kann durch N+1-Datenbankzugriffe und nicht durch die Schleifenlogik selbst verursacht sein.
5. Optimierungshebel in dieser Reihenfolge prüfen: Arbeit vermeiden; algorithmische Komplexität reduzieren; Datenstruktur ändern; Query/Index/Batching; Lazy/Streaming; Cache; Parallelisierung; Architektur/Runtime; erst danach Mikrooptimierung.
6. Kandidaten mit `expectedImpact`, `confidence`, `implementationEffort`, `correctnessRisk`, `operationalRisk` und `evidence` bewerten.
7. Kandidaten ohne ausreichende Evidenz explizit als Hypothese kennzeichnen.

## Priorisierung

Bevorzuge hohe erwartete Gesamtwirkung bei hoher Evidenz und begrenztem Risiko. Kleine lokale Gewinne dürfen keinen dominanten Systemengpass verdrängen. Vermeide Parallelisierung, Cache oder Infrastrukturwechsel, wenn einfachere Arbeitseinsparung denselben Engpass sicherer löst.

## Ausgabe

`hotspot-map.json` enthält mindestens Anteil/Impact, Ursache, Evidenz, betroffenen Pfad und Confidence. `optimization-candidates.json` enthält priorisierte Kandidaten einschließlich verworfener Alternativen und Begründung. `hotspot-analysis.md` erläutert die wichtigsten Kausalzusammenhänge.

## Abschluss

Der Skill endet, wenn die wichtigsten Optimierungskandidaten nach messbarer Wirkung, Evidenz und Risiko priorisiert sind und kein Kandidat allein aufgrund stilistischer Präferenz empfohlen wird.
