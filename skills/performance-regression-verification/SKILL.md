---
name: performance-regression-verification
description: Verifiziert nach einer Software-Optimierung funktionale Gleichwertigkeit und messbare Performance-Verbesserung gegen eine unveränderte Baseline, bewertet Rauschen und Trade-offs und erzeugt dauerhafte Performance-Gates oder Regression-Guards, wenn sie stabil genug sind. Verwenden nach Implementierung eines Performance-TASK.md; nicht für reine Code-Ästhetik oder ungemessene Optimierungsbehauptungen.
userFacing: true
implicitInvocation: true
category: engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - performance-baseline
  - test-driven-vertical-slice
  - two-axis-code-review
outputs:
  - performance-result.json
  - performance-result.md
  - performance-regression-guard.md
lastEvaluated: 2026-08-26
---

# Performance Regression Verification

Beweise, dass die Änderung funktional korrekt ist und den beabsichtigten Engpass messbar verbessert. Eine scheinbar schnellere Implementierung ohne vergleichbaren Benchmark gilt nicht als verifiziert.

## Eingang

- unveränderte `performance-baseline.json`
- `TASK.md`/Performance Gate und funktionale Invarianten
- implementierter Codezustand
- funktionale Testnachweise
- identischer oder kontrolliert äquivalenter Benchmark-Workload

## Ablauf

1. Prüfen, dass Baseline und Candidate hinsichtlich Workload, Datenmenge, Cache-Zustand, Umgebung und relevanter Parallelität vergleichbar sind.
2. Funktionale Regressionstests zuerst ausführen. Bei fachlicher Abweichung `FAIL_FUNCTIONAL`; Performance-Gewinn darf dies nicht überstimmen.
3. Benchmark mit derselben Messmethode wiederholen. Bei Messrauschen ausreichende Stichprobe/robuste Statistik verwenden.
4. Vorher/Nachher für jede vereinbarte Metrik sowie relative und absolute Änderung berechnen.
5. Neben dem Zielmetrikwert Sekundärregressionen prüfen: CPU, RAM, Query Count, I/O, Netzwerk, Locking, Error Rate oder Kosten soweit relevant.
6. Adversarial Review durchführen: Cache-Invalidierung, stale data, Race Conditions, unbounded concurrency, Memory Leaks, Lock Contention, Query Explosion, Ordering- und Transaktionsänderungen gezielt prüfen.
7. Ergebnis als `PASS`, `PASS_WITH_TRADEOFF`, `FAIL_FUNCTIONAL`, `FAIL_PERFORMANCE` oder `INCONCLUSIVE` klassifizieren.
8. Nur stabile, ausreichend reproduzierbare Metriken in einen dauerhaften Regression-Guard überführen. Flaky Wall-Clock-Grenzen vermeiden; Toleranz/Warning/Fail-Band dokumentieren.

## Simplification Pass

Nach bestandenem Kernnachweis prüfen, ob durch die Optimierung alte Workarounds, doppelte Helper, redundante Konvertierungen, veraltete Fallbacks, temporäre Instrumentierung oder unnötige Abstraktionen entfallen können. Cleanup nur übernehmen, wenn Funktion und Performance erneut verifiziert werden. Ziel ist nicht minimale Zeilenzahl, sondern geringere unnötige Komplexität.

## Ausgabe

`performance-result.json` enthält mindestens Baseline/Candidate-Revision, Workload-Fingerprint, Metriken vorher/nachher, Delta, Functional Test State, Trade-offs, Ergebnisstatus und Restunsicherheiten.

`performance-result.md` liefert verständliche Before/After-Evidenz. `performance-regression-guard.md` beschreibt den CI-/Benchmark-Guard oder begründet, warum kein stabiler automatischer Guard sinnvoll ist.

## Abschluss

Abgeschlossen ist die Optimierung nur bei funktionalem Nachweis plus erreichtem Performance Gate oder explizit akzeptiertem Trade-off. `INCONCLUSIVE` darf nie als Erfolg dargestellt werden.