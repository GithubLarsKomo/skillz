---
name: ivdr-performance-evaluation
description: Orchestriert wissenschaftliche Validität, analytische und klinische Performance zu einer IVDR-Gesamtbewertung mit Gaps.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - ivdr-scientific-validity
  - ivdr-analytical-performance
  - ivdr-clinical-performance-study
  - regulatory-evidence-traceability
outputs:
  - ivdr-performance-evaluation.json
  - ivdr-performance-evaluation-gaps.json
lastEvaluated: 2026-08-07
---

# IVDR Performance Evaluation

## Zweck und Grenze

Dieser Skill ist der Orchestrator der IVDR-Performance-Evaluation. Er führt die bereits erzeugten Evidenzpakete zu wissenschaftlicher Validität, analytischer Performance und klinischer Performance zusammen, bewertet Claim Coverage, Konsistenz und offene Evidenzlücken und erzeugt eine nachvollziehbare Gesamtbewertung.

Er führt die drei Evidenzsäulen nicht erneut aus, ersetzt keinen Performance Evaluation Report und simuliert keine Notified-Body-/Behördenentscheidung.

## Kernprinzipien

- Die drei Evidenzsäulen bleiben getrennte fachliche Inputs mit eigener Provenance und eigener Unsicherheit.
- Eine starke Säule kompensiert eine fehlende andere Säule nicht automatisch.
- Claim Coverage wird claim-by-claim bewertet; globale Aussagen wie „Performance ausreichend“ ohne Rückverfolgbarkeit sind unzulässig.
- Widersprüche zwischen Scientific Validity, Analytical Performance und Clinical Performance werden sichtbar gemacht und nicht durch Mittelung geglättet.
- Gaps werden nach regulatorischer Relevanz, Claim-Auswirkung und Downstream-Entscheidung priorisiert.
- Produktkontext- oder Claim-Änderungen invalidieren betroffene Teilbewertungen gezielt statt die gesamte Historie still zu überschreiben.

## Workflow

### 1. Input-Freshness prüfen

Verifiziere Product Context, `asOf`, Source/Evidence References und Status der drei Eingangsartefakte. Stale oder unvollständige Inputs werden als Blocker/Gaps markiert.

### 2. Claim Coverage normalisieren

Baue eine gemeinsame Claim-Matrix. Für jeden Claim erfasse:

- Scientific-Validity-Status,
- analytische Performance Coverage,
- klinische Performance Coverage,
- relevante Risk-/Evidence References,
- Limitationen,
- offene Gaps.

### 3. Konsistenz prüfen

Suche insbesondere nach:

- Claims ohne wissenschaftliche Validität,
- analytischer Range/Matrix, die den klinisch verwendeten Bereich nicht abdeckt,
- klinischer Evidenz außerhalb des Intended Purpose,
- widersprüchlichen Populationen/Specimens/Comparators,
- post-hoc Claim-Ausweitungen,
- Risk Controls ohne ausreichende Performance-Evidenz.

### 4. Gesamtstatus ableiten

Pro Claim und insgesamt sind mindestens `supported|partially-supported|unsupported|inconclusive|blocked` zulässig. Der Gesamtstatus ist keine arithmetische Mittelung; ein kritischer Gap kann die Gesamtbewertung blockieren.

### 5. Gaps routen

Jeder Gap geht an den fachlich richtigen Owner zurück:

- Association/Claim → `ivdr-scientific-validity`,
- analytische Evidenz → `ivdr-analytical-performance`,
- klinische Evidenz/Study Need → `ivdr-clinical-performance-study`,
- Provenance → `regulatory-evidence-traceability`,
- Risk-Auswirkung → `medical-device-risk-management-iso14971`.

### 6. Abschlussartefakte erzeugen

Erzeuge eine maschinenlesbare Gesamtbewertung plus Gap-Liste. Der spätere `ivdr-performance-evaluation-report` konsumiert diese Artefakte und übernimmt Dokumentassembly/Controlled-Documentation-Aspekte.

## Output-Verträge

`ivdr-performance-evaluation.json` enthält mindestens `asOf`, Product Context, Claims, Referenzen auf alle drei Evidenzsäulen, Claim-Coverage-Matrix, Cross-Pillar-Conflicts, Gesamtstatus, Limitationen und Authority Boundary.

`ivdr-performance-evaluation-gaps.json` enthält Gap-ID, Claim, betroffene Säule, Impact, Priority, benötigte Evidenz, Owner/Next Skill, Stop Condition und Re-evaluation Trigger.

## Downstream

Primäre Consumers sind `eu-mdr-ivdr-regulatory-specialist`, der geplante `ivdr-performance-evaluation-report`, PMPF/PMS, Design-Change-Regulatory-Impact und controlled documentation.

## Memory Path

Persistenzwürdig sind bestätigte, wiederverwendbare Cross-Pillar-Konsistenzmuster, stabile projektspezifische Claim-Coverage-Regeln und validierte Gap-Routing-Heuristiken. Aktuelle Gesamtstatus, offene Gaps, momentane Evidenzstände und vorläufige Claim-Bewertungen bleiben run-only. Kandidaten benötigen `sourceRefs`; zeitabhängige regulatorische Aussagen tragen `asOf` und gegebenenfalls `reviewAfter`. Übergib nur geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- alle drei Evidenzsäulen explizit referenziert sind,
- Claim Coverage statt pauschaler Gesamtbehauptung bewertet wird,
- Cross-Pillar-Widersprüche sichtbar bleiben,
- kritische Gaps nicht durch starke andere Säulen kompensiert werden,
- jeder Gap einen fachlich richtigen Rückweg besitzt,
- kein Report-/Authority-Schritt simuliert wird,
- Memory Candidates keine aktuelle Gesamtbewertung zu dauerhaftem Regulatory Fact machen.
