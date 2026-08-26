---
name: optimize-software-performance
description: Orchestriert die messbare Optimierung und Beschleunigung bestehenden oder iterativ erzeugten Codes von Ziel/Guardrails über Baseline, Profiling, Hotspot- und Architekturprüfung, PERFORMANCE_PLAN.md und TASK.md bis zu kleinen Implementierungsslices, funktionalen Tests, Performance-Verifikation, Simplification Pass und Regression Guard. Verwenden, wenn funktionierender Code am Ende eines Entwicklungszyklus unnötig langsam, ressourcenintensiv oder strukturell aufgebläht ist oder gezielt auf Performance optimiert werden soll.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - iterate-software-projects
  - performance-baseline
  - performance-hotspot-analysis
  - performance-optimization-plan
  - implement-from-issue
  - test-driven-vertical-slice
  - two-axis-code-review
  - performance-regression-verification
outputs:
  - optimization-closure.md
lastEvaluated: 2026-08-26
---

# Optimize Software Performance

Arbeite als Performance-Orchestrator. Ziel ist nicht möglichst viel Refactoring, sondern der kleinste belegte Änderungssatz, der den dominanten Engpass beseitigt und Funktion, Kompatibilität und Wartbarkeit erhält oder verbessert.

## Wann verwenden

Nutze den Flow insbesondere wenn:

- iterativ erzeugter Code zwar funktioniert, aber unnötig langsam oder kompliziert geworden ist,
- selbst geschriebener Code nachträglich auf Durchsatz, Latenz, RAM, Datenbanklast, I/O, Netzwerk, Build-Zeit oder Kosten optimiert werden soll,
- mehrere lokale Optimierungen entstanden sind und ein systemischer End-to-End-Pass fehlt,
- vor einem Release oder größeren Rollout messbare Performance-Gates benötigt werden.

Bei primären Fehlfunktionen zuerst `disciplined-diagnosis`. Bei rein stilistischer Codebereinigung ohne messbares Effizienzziel andere Review-/Refactoring-Skills verwenden.

## Phase 0: Ziel und Guardrails

Definiere oder rekonstruiere:

- beobachtbares Performance-Ziel oder zu untersuchende Engpassdimension,
- funktionale Invarianten,
- Kompatibilitätsgrenzen,
- repräsentativen Workload,
- erlaubte Trade-offs,
- No-Regression-Kriterien.

Beispiel: `p95 API latency 780 ms -> <300 ms; Ergebnisse identisch; Peak Memory +<10 %; bestehende Tests grün`.

## Phase 1: Baseline

Rufe `performance-baseline` auf. Ohne reproduzierbare Baseline keine Optimierung beginnen, außer der Nutzer verlangt ausdrücklich nur eine Hypothesenanalyse. Dann Ergebnis als ungemessen kennzeichnen.

Gate: Baseline reproduzierbar und funktionaler Ausgangszustand bestätigt.

## Phase 2: Hotspots und Ursachen

Rufe `performance-hotspot-analysis` auf. Priorisiere systemische Engpässe statt sichtbarer Mikroineffizienzen. Dominierende Zeit-/Ressourcenanteile und Root Causes müssen mit Evidenz verbunden sein.

Gate: priorisierte Kandidaten mit Impact, Confidence, Aufwand und Risiko.

## Phase 3: Architektur- und Lösungscheck

Für strukturelle Kandidaten `architecture-deepening-review` verwenden. Prüfreihenfolge:

1. Arbeit vermeiden
2. algorithmische Komplexität reduzieren
3. Datenstruktur verbessern
4. Queries/Index/Batching verbessern
5. Lazy Loading/Streaming
6. Cache
7. Parallelisierung/Asynchronität
8. Architektur-/Runtime-Wechsel
9. Mikrooptimierung

Neue Infrastruktur nur einführen, wenn einfachere Lösungen das Budget nicht plausibel erreichen.

## Phase 4: Konzept und TASK.md

Rufe `performance-optimization-plan` auf. Erzeuge `PERFORMANCE_PLAN.md` und `TASK.md`. Verworfene Alternativen mit Grund festhalten. Jeder Task adressiert einen belegten Hotspot und besitzt Functional- sowie Performance-Gate.

Gate: TASK.md ist ohne weitere reversible Detailentscheidung implementierbar.

## Phase 5: Abarbeitung

Arbeite TASK.md in kleinen vertikalen Slices ab. Nutze `implement-from-issue` bzw. `test-driven-vertical-slice` nach Projektmodus. Nach jedem wesentlichen Slice:

- funktionale Tests,
- zielgerichteten Benchmark,
- Scope-/Diff-Prüfung,
- Fortsetzen nur bei positiver Evidenz oder klar begründetem Informationsgewinn.

Nicht mehrere riskante Mechanismen gleichzeitig einführen, wenn ihr Effekt sonst nicht mehr isolierbar ist.

## Phase 6: Korrektheits- und Effizienzreview

Nutze `two-axis-code-review` mit zwei expliziten Achsen:

- Correctness: Verhalten, Daten, APIs, Transaktionen und Fehlerfälle bleiben korrekt.
- Efficiency: Zielmetrik verbessert sich tatsächlich und Sekundärmetriken regressieren nicht unvertretbar.

## Phase 7: Final Verification und Simplification

Rufe `performance-regression-verification` auf. Vergleiche identischen Workload Before/After. Danach Simplification Pass:

- tote oder obsolete Workarounds entfernen,
- doppelte Helper/Abstraktionen konsolidieren,
- redundante Queries/Konvertierungen beseitigen,
- temporäre Instrumentierung entfernen,
- unnötige Compatibility-Pfade nur entfernen, wenn ihre Entbehrlichkeit belegt ist.

Nach Cleanup Tests und Benchmark erneut ausführen.

## Phase 8: Regression Guard und Closure

Für stabile kritische Metriken Warning-/Fail-Budget in CI oder Benchmark-Suite dokumentieren. Flaky absolute Zeiten ohne kontrollierte Umgebung nicht als harte Gates verwenden.

`optimization-closure.md` enthält:

- Baseline vs. finaler Zustand,
- erreichten Performance-Gewinn,
- funktionale Testevidenz,
- relevante Trade-offs,
- entfernte Komplexität,
- Regression Guards,
- Restunsicherheiten und bewusst nicht umgesetzte Kandidaten.

## Schleifenlogik

- `FAIL_FUNCTIONAL` -> kleinsten fehlerhaften Slice zurückrollen/korrigieren.
- `FAIL_PERFORMANCE` -> zurück zu Hotspot-/Kandidatenanalyse; nicht blind weiter refactoren.
- `INCONCLUSIVE` -> Messdesign verbessern.
- Ziel erreicht, aber unnötige Komplexität verbleibt -> Simplification Pass.
- Ziel erreicht und alle Gates bestanden -> Closure; keine weiteren Optimierungen nur der Vollständigkeit halber.

## Abschluss

Der Flow endet, wenn Funktion nachgewiesen, das Performance-Ziel erreicht oder ein akzeptierter Trade-off dokumentiert, die finale Implementierung erneut gemessen und unnötige Optimierungsartefakte bereinigt wurden. Eine reine Behauptung wie `sollte schneller sein` erfüllt die Definition of Done nicht.
