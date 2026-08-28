---
name: workflow-benchmark-authoring
description: Erstellt ausführbare, domänenübergreifende Workflow-Benchmarks aus kanonischen Skill-Orchestratoren, Dependency Closure, Artifact Ownership, Lifecycle/Discoverability und Evaluationsevidenz. Verwenden als internen Governance-Worker, wenn neue End-to-End-Architekturpfade als versionierte Regression Contracts abgesichert werden sollen.
userFacing: false
implicitInvocation: false
category: internal
version: 0.1.0
status: candidate
discoverability: internal
owners:
  - GithubLarsKomo
requires:
  - skill-evaluation-suite-authoring
  - artifact-contract-normalizer
outputs:
  - workflow-benchmark-spec.json
  - workflow-benchmark-regression.py
  - workflow-benchmark-authoring-report.md
lastEvaluated: 2026-08-28
---

# Workflow Benchmark Authoring

## Zweck

Erzeuge einen versionierten, maschinenprüfbaren Benchmark für einen **realen Workflowpfad** im Skillz-Capability-System. Ein Benchmark schützt Architektur- und Verhaltensgrenzen über mehrere Skills hinweg; er ist kein Ersatz für die Evaluation einzelner Skills und darf keine Ausführung behaupten, die tatsächlich nur strukturell geprüft wurde.

Der Worker arbeitet auf dem kanonischen Capability Index, Dependency Graph, den aktuellen `SKILL.md`-Verträgen und aufgezeichneten Evaluationsergebnissen.

## Verbindliche Benchmark-Grenze

Ein Contract-Level-E2E-Benchmark darf nur behaupten, dass:

- der kanonische Entrypoint existiert und aktiv discoverable ist,
- die erwarteten Worker über den `requires`-Closure erreichbar sind,
- die beteiligten Skills nicht deprecated/compatibility-only sind, sofern der Benchmark nicht ausdrücklich eine Compatibility-Migration testet,
- die beteiligten Skills aktuelle Evaluationen besitzen und diese PASS sind,
- zentrale `mustPreserve`- und `mustNotDo`-Grenzen als überprüfbare Regression Contracts festgehalten sind,
- Artifact Ownership und Delegationsgrenzen nicht durch doppelte Producer oder direkte Worker-Bypässe unterlaufen werden.

**Contract-Level ≠ echte Artifact-Ausführung.** Render-, Browser-, Compiler-, Runtime-, API- oder Dokument-Parität darf nur als ausgeführt bezeichnet werden, wenn ein entsprechender executable Test diese Artefakte wirklich erzeugt bzw. prüft.

## Authoring-Ablauf

### 1. Kanonischen Entrypoint wählen

Beginne mit einem realen user-facing Orchestrator. Prüfe:

- `userFacing: true`,
- `discoverability` ist `public` oder `advanced`,
- `status` ist nicht `deprecated`,
- Evaluation ist vorhanden und PASS,
- der Entrypoint besitzt mindestens einen klaren Output.

Interne Worker oder Compatibility-Fassaden werden nicht zum normalen Benchmark-Entrypoint erklärt.

### 2. Dependency Closure statt Wunschsequenz

Leite die zulässige Sequenz aus dem transitiven `requires`-Closure des Entrypoints ab. Jeder in `sequence` genannte Skill muss tatsächlich über diesen Closure erreichbar sein.

Verboten:

- Worker nur wegen thematischer Nähe in die Sequenz schreiben,
- eine frühere Legacy-Fassade reaktivieren, weil sie einmal der Einstieg war,
- direkte Renderer/Delivery-Worker auf Top-Level ziehen, wenn ein Shared Delivery Orchestrator diese Grenze besitzt.

### 3. Semantische Invarianten binden

Formuliere pro Szenario mindestens:

- zwei konkrete `mustPreserve`-Invarianten,
- mindestens ein `mustNotDo`,
- eine klare Intent-Beschreibung,
- eine eindeutige Domain und Scenario-ID.

Die Invarianten müssen aus aktuellen normativen Skill-Verträgen stammen. Vage Aussagen wie „gute Qualität“ oder „korrekt arbeiten“ sind keine belastbaren Benchmark-Gates.

### 4. Artifact Ownership prüfen

Nutze `artifact-contract-normalizer`, wenn Producer/Consumer-Grenzen unklar sind. Der Benchmark darf keine zweite Ownership etablieren. Shared Delivery, generische Template-Cores und Compatibility-Fassaden werden entsprechend ihrer aktuellen Architekturgrenze geprüft.

### 5. Evaluationsevidenz prüfen

Nutze `skill-evaluation-suite-authoring`, wenn ein beteiligter Skill keine aktuelle Evaluation besitzt oder die Suite die relevante Grenze nicht abdeckt. Der Benchmark wird nicht durch eine erfundene PASS-Annahme geschlossen.

**Kein grüner Benchmark auf roter oder fehlender Skill-Evaluation.**

### 6. Regressionstest erzeugen

`workflow-benchmark-regression.py` prüft mindestens:

1. Schema-Konformität des Benchmarks.
2. Eindeutige Scenario-IDs.
3. Aktive user-facing Entrypoints.
4. Reachability aller Sequenz-Skills über den `requires`-Closure.
5. Keine unbeabsichtigten deprecated/compatibility Skills in der aktiven Sequenz.
6. PASS-Evaluation aller beteiligten Skills.
7. Nichtleere fachliche Preserve-/Forbidden-Grenzen.
8. Domänenspezifische Architekturgrenzen, wenn der Benchmark genau eine Migration oder Delegation absichern soll.

### 7. Repository-Gate

Vor Abschluss müssen mindestens laufen:

- Metadata-/Schema-Validator,
- der neue Workflow-Benchmark-Test,
- Repository-Validator,
- Unified Evaluation Runner.

Wenn der Benchmark einen echten Render-/Runtime-/Artifact-Pfad berührt und dafür bereits ein spezialisiertes CI-Gate existiert, muss dieses zusätzlich grün sein.

## Output Contract

### `workflow-benchmark-spec.json`

Schema-konforme Benchmarkdefinition mit `schemaVersion`, `suite` und Szenarien aus `id`, `domain`, `entrypoint`, `intent`, `sequence`, `mustPreserve`, `mustNotDo`.

### `workflow-benchmark-regression.py`

Deterministischer Offline-Regressionscheck gegen den aktuellen Capability Index und die kanonischen Repository-Artefakte.

### `workflow-benchmark-authoring-report.md`

Dokumentiert:

- Benchmark-Level und Scope,
- ausgewählte Entrypoints,
- geprüfte Closure-/Ownership-Grenzen,
- echte executable Gates versus nur Contract-Level-Gates,
- offene Lücken und nicht behauptete Evidenz.

## Failure Conditions

FAIL, wenn:

- ein Sequenz-Skill außerhalb des Entrypoint-Closures liegt,
- ein aktiver Pfad auf eine deprecated/compatibility-only Fassade zurückfällt,
- fehlende oder rote Evaluationen ignoriert werden,
- ein Contract-Level-Test als tatsächliche Artifact-Ausführung ausgegeben wird,
- Invarianten frei erfunden statt aus normativen Verträgen abgeleitet werden,
- ein Benchmark Ownership dupliziert oder Shared-Delivery-Grenzen umgeht.
