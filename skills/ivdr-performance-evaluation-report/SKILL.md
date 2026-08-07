---
name: ivdr-performance-evaluation-report
description: Erstellt aus einer abgeschlossenen IVDR-Performance-Evaluation einen rückverfolgbaren Performance Evaluation Report, ohne die Evidenzsäulen neu zu bewerten.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - ivdr-performance-evaluation
  - regulatory-evidence-traceability
  - mdcg-guidance-navigator
outputs:
  - performance-evaluation-report.md
  - per-traceability.json
lastEvaluated: 2026-08-07
---

# IVDR Performance Evaluation Report

## Zweck und Grenze

Dieser Skill assembliert eine bereits fachlich abgeschlossene IVDR-Performance-Evaluation zu einem nachvollziehbaren Performance Evaluation Report (PER). Er übernimmt Status, Claims, Evidenz, Limitationen und Gaps aus `ivdr-performance-evaluation` und erzeugt daraus ein prüfbares Dokument mit Requirement-/Evidence-Traceability.

Er bewertet Scientific Validity, Analytical Performance oder Clinical Performance **nicht erneut**, ändert keine Claims und simuliert weder Notified-Body- noch Behördenakzeptanz. Die jeweils aktuelle regulatorische bzw. MDCG-Struktur wird vor der Dokumentassembly über `mdcg-guidance-navigator` verifiziert statt als statische Template-Version eingebrannt.

## Kernprinzipien

- **Assembly statt Re-Assessment:** fachliche Bewertungen bleiben Eigentum der Upstream-Skills.
- **Claim-Level Traceability:** jede wesentliche Aussage muss auf Performance-Evaluation, Evidenz oder klar gekennzeichnete Interpretation zurückführbar sein.
- **Keine Gap-Kosmetik:** offene oder blockierende Gaps bleiben im Bericht sichtbar.
- **Current Guidance:** Struktur- und Inhaltsanforderungen werden gegen aktuelle offizielle Quellen geprüft.
- **Controlled-State getrennt:** Freigabe, Effective Date, Signaturen und Supersession gehören zu `controlled-quality-documentation`.

## Workflow

### 1. Inputs fixieren

Prüfe `asOf`, Product Context, Claim-Matrix, Gesamtstatus, Cross-Pillar-Konflikte, Limitationen und offene Gaps aus `ivdr-performance-evaluation` sowie die aktuelle Guidance-Auswahl.

### 2. Berichtstruktur ableiten

Erzeuge die aktuelle erforderliche bzw. begründete Struktur aus IVDR und anwendbarer Guidance. Statische Abschnittsnummern oder historische Templates dürfen nicht ungeprüft als verbindlich gelten.

### 3. Evidenzsäulen referenzieren

Stelle Scientific Validity, Analytical Performance und Clinical Performance getrennt dar. Übernimm ihre Schlussfolgerungen und Source References; führe keine neue unabhängige Evidenzbewertung im Reporting-Skill durch.

### 4. Claim Coverage und Konsistenz darstellen

Für jeden Claim dokumentiere die drei Evidenzsäulen, den Unterstützungsstatus, Limitationen und verbleibende Gaps. Cross-Pillar-Widersprüche bleiben explizit.

### 5. Traceability erzeugen

`per-traceability.json` verknüpft Berichtsaussagen mit Requirements, Claims, Performance-Evaluation-Elementen und Source References über `regulatory-evidence-traceability`.

### 6. Übergabe

Übergib den Report an `controlled-quality-documentation` für Freigabe/Versionierung. Evidenzlücken gehen an den jeweiligen Performance-Skill zurück; neue Post-Market-Fragen an `ivdr-pmpf` bzw. `ivdr-pms-vigilance`.

## Output-Verträge

`performance-evaluation-report.md` enthält mindestens Scope, Intended Purpose/Claims, Methodik, Scientific Validity, Analytical Performance, Clinical Performance, integrierte Claim Coverage, Limitationen, offene Gaps, Schlussfolgerung, `asOf` und Source References.

`per-traceability.json` enthält Statement-/Section-IDs, Claim-/Requirement-Links, Evidence References, Source References, Freshness und Gap-Referenzen.

## Memory Path

Persistenzwürdig sind bestätigte, wiederverwendbare Reporting-/Traceability-Muster und stabile organisations- oder projektfamilienspezifische Strukturentscheidungen. Aktuelle PER-Schlussfolgerungen, offene Gaps, konkrete Freigabestände und momentane Guidance-Versionen bleiben run-only. Kandidaten benötigen `sourceRefs`; guidanceabhängige Learnings zusätzlich `asOf` und `reviewAfter`. Übergib nur geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- die drei Evidenzsäulen nicht neu bewertet werden,
- jede wesentliche Berichtsaussage rückverfolgbar ist,
- Gaps und Widersprüche sichtbar bleiben,
- aktuelle Guidance vor der Strukturentscheidung geprüft wurde,
- Controlled-Document-Freigabe nicht simuliert wird,
- Downstream den Report ohne implizite Gesprächsannahmen übernehmen kann,
- aktuelle PER-Schlussfolgerungen nicht als dauerhaftes Memory-Faktum gespeichert werden.
