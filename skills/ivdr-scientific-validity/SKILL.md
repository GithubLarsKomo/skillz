---
name: ivdr-scientific-validity
description: Bewertet die wissenschaftliche Validität eines IVD evidenzgebunden und trennt Association, Claim, Evidenzstärke und Gap.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - regulated-product-context
  - research-to-evidence-note
  - regulatory-evidence-traceability
outputs:
  - scientific-validity-assessment.json
  - scientific-validity-report.md
lastEvaluated: 2026-08-07
---

# IVDR Scientific Validity

## Zweck und Grenze

Dieser Skill bewertet, ob die Beziehung zwischen Analyte/Measurand bzw. Target und dem klinischen Zustand oder physiologischen Prozess für den konkreten Intended Purpose wissenschaftlich ausreichend begründet ist. Er strukturiert die Evidenz und ihre Grenzen, führt aber keine analytische Leistungsbewertung, klinische Performance-Studie oder Gesamt-Performance-Evaluation durch.

Er ersetzt weder `research-to-evidence-note` noch `ivdr-analytical-performance`, `ivdr-clinical-performance-study` oder `ivdr-performance-evaluation`.

## Kernprinzipien

- Intended Purpose, Population, Specimen, Target und klinischer Use Case stammen aus `regulated-product-context`.
- Biologische Plausibilität, klinische Association und konkrete Produkt-Claims werden getrennt bewertet.
- Evidenz wird nicht nach Publikationsanzahl, sondern nach Relevanz, Qualität, Konsistenz, Direktheit und Applicability beurteilt.
- Sekundärquellen dürfen Discovery unterstützen; tragende Claims benötigen nachvollziehbare Primär- oder autoritative Evidenz.
- Ein fehlender direkter Nachweis wird als Gap oder begrenzte Transferierbarkeit sichtbar, nicht durch Analogie geschlossen.
- Wissenschaftliche Validität ist eine Evidenzsäule und beweist weder analytische noch klinische Leistungsfähigkeit des konkreten Produkts.

## Workflow

### 1. Claim-Scope fixieren

Formuliere pro Intended-Purpose-Claim die zu belegende Beziehung zwischen Target/Measurand, klinischem Zustand/Prozess, Population, Specimen und Verwendungszweck.

### 2. Evidenzinventar aufbauen

Übernimm Research Notes und verknüpfe jede tragende Quelle über `regulatory-evidence-traceability`. Trenne mindestens Leitlinien/Consensus, systematische Reviews, Primärstudien, Referenzdatenbanken und begründete mechanistische Evidenz.

### 3. Applicability prüfen

Bewerte für jede Evidenzquelle mindestens Population, Erkrankungsstadium, Specimen/Matrix, Targetdefinition, Referenzstandard, Setting und Claim-Nähe. Nicht übertragbare Evidenz bleibt sichtbar.

### 4. Evidenzstärke und Widersprüche bewerten

Klassifiziere die Evidenz pro Claim als `strong|moderate|limited|insufficient|conflicting|unknown` und dokumentiere Widersprüche, Bias-/Generalisierbarkeitsrisiken und fehlende direkte Evidenz.

### 5. Gap-to-Action ableiten

Jeder relevante Gap erhält einen nächsten Evidenzschritt, z. B. fokussierte Literaturrecherche, Claim-Eingrenzung, zusätzliche klinische Evidenz oder Eskalation an `ivdr-clinical-performance-study`.

## Output-Verträge

`scientific-validity-assessment.json` enthält mindestens `asOf`, Product-Context-Referenz, Claims, Evidence Links, Applicability, Evidenzstärke, Widersprüche, Gaps und eine klare `assessmentState`-Kennzeichnung.

`scientific-validity-report.md` fasst Scope, Methodik, Claim-by-Claim-Bewertung, Evidenzstärke, Gaps und Schlussfolgerungen nachvollziehbar zusammen, ohne fehlende Evidenz zu kaschieren.

## Downstream

Primärer Consumer ist `ivdr-performance-evaluation`. Gaps können an `research-to-evidence-note`, `ivdr-clinical-performance-study`, Claim-/Labeling-Arbeit oder `decision-record` übergeben werden.

## Memory Path

Persistenzwürdig sind bestätigte, wiederverwendbare Association-Muster, stabile projektspezifische Claim-Grenzen und validierte Applicability-Heuristiken. Einzelne neue Publikationen, aktuelle Suchresultate, offene Evidenzkonflikte und vorläufige Evidenzstärken bleiben run-only. Kandidaten benötigen `sourceRefs`; zeitabhängige Aussagen tragen `asOf` und bei erwartbarer Änderung `reviewAfter`. Übergib nur geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- jeder bewertete Claim auf fixierten Produktkontext verweist,
- Association, Produkt-Claim und Produktleistung getrennt bleiben,
- tragende Evidenz nachvollziehbare Source References besitzt,
- Applicability und Widersprüche sichtbar bewertet sind,
- unzureichende Evidenz nicht positiv umgedeutet wird,
- Gaps einen klaren nächsten Evidenzschritt besitzen,
- Memory Candidates keine vorläufige Evidenzbewertung zu einem zeitlosen Fakt hochstufen.
