---
name: performance-baseline
description: Erzeugt vor Software-Optimierungen eine reproduzierbare Performance-Baseline mit repräsentativem Workload, relevanten Laufzeit-, Ressourcen-, Datenbank-, I/O- und Netzwerkmetriken sowie Messunsicherheit. Verwenden, wenn Code oder ein System beschleunigt, skaliert oder ressourceneffizienter gemacht werden soll; nicht als Ersatz für funktionale Fehlerdiagnose.
userFacing: true
implicitInvocation: true
category: engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - iterate-software-projects
outputs:
  - performance-baseline.json
  - performance-baseline.md
  - benchmark-reproduction.md
lastEvaluated: 2026-08-26
---

# Performance Baseline

Stelle vor jeder Optimierung einen reproduzierbaren Ausgangszustand her. Keine Geschwindigkeits- oder Effizienzbehauptung ohne Messbasis.

## Eingang

- Repository-/Build-/Runtime-Zustand einschließlich Commit oder eindeutigem Snapshot
- repräsentativer Workload oder reale Nutzeraktion
- gewünschte Optimierungsdimension, falls vorgegeben
- funktionale Invarianten und Kompatibilitätsgrenzen

Fehlt ein explizites Performance-Ziel, ermittle zunächst die relevante Engpassdimension und dokumentiere sie als reversible Annahme. Funktionale Fehler zuerst mit `disciplined-diagnosis` behandeln.

## Ablauf

1. Reproduzierbaren Build und funktionalen Ausgangszustand bestätigen.
2. Workload so festlegen, dass Eingabedaten, Warm-/Cold-State, Parallelität, Cache-Zustand und externe Abhängigkeiten beschrieben sind.
3. Nur relevante Metriken erfassen, mindestens Wall Time plus die für den vermuteten Engpass aussagekräftigen Größen, z. B. CPU, Peak Memory, Query Count/Duration, I/O, Netzwerkaufrufe, Cache Hit Rate, Zeilen/Objekte oder Build-Dauer.
4. Mehrere Läufe verwenden, wenn Messrauschen die Aussage beeinflussen kann. Median oder robuste Perzentile bevorzugen; Einzelmessungen als solche kennzeichnen.
5. Messwerkzeuge und deren Overhead dokumentieren. Produktionsnahe Daten niemals unnötig kopieren oder persistieren.
6. Baseline als unveränderlichen Vergleichspunkt ausgeben.

## Qualitätsregeln

- Keine synthetische Mikrobenchmark als alleinigen Ersatz für den realen Zielpfad verwenden.
- Warm- und Cold-Cache nicht vermischen.
- Externe Latenz getrennt vom eigenen Code ausweisen, wenn sie die Messung dominiert.
- Benchmark-Daten müssen dieselbe Semantik vor und nach der Optimierung erlauben.
- Nicht gemessene Größen als `unknown`, nicht als Null oder bestanden ausgeben.

## Ausgabe

`performance-baseline.json` enthält mindestens: `revision`, `workload`, `environment`, `metrics`, `sampleCount`, `measurementMethod`, `noiseOrVariance`, `functionalInvariants`, `constraints` und `knownLimitations`.

`performance-baseline.md` fasst die wichtigsten Werte menschenlesbar zusammen. `benchmark-reproduction.md` enthält die minimalen Schritte, Kommandos und Voraussetzungen zur Wiederholung.

## Abschluss

Der Skill endet, wenn ein anderer Agent denselben Workload auf demselben Codezustand reproduzieren und die Baseline mit denselben Metriken erneut bestimmen kann.