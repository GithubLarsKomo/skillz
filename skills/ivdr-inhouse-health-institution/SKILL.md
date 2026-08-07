---
name: ivdr-inhouse-health-institution
description: Bewertet in Gesundheitseinrichtungen hergestellte und verwendete IVDs gegen die IVDR-Health-Institution-Exception nach Artikel 5(5), inklusive aktueller Übergangsfristen, GSPR-, QMS-, Dokumentations- und Marktäquivalenz-Gates.
userFacing: true
implicitInvocation: false
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - regulated-product-context
  - medical-device-qms-iso13485
  - medical-device-risk-management-iso14971
  - regulatory-evidence-traceability
  - decision-record
outputs:
  - inhouse-ivd-eligibility.json
  - inhouse-ivd-condition-map.json
  - inhouse-ivd-transition-readiness.json
lastEvaluated: 2026-08-07
---

# IVDR In-house Health Institution

## Zweck und Grenze

Dieser Skill bewertet IVDs, die ausschließlich innerhalb einer in der Union ansässigen Gesundheitseinrichtung hergestellt und verwendet werden, gegen die Health-Institution-Exception nach Artikel 5(5) IVDR und die aktuelle MDCG-Guidance. Er bildet Eligibility, anwendbare Bedingungen, Übergangsfristen, Annex-I-GSPR-, QMS-, Dokumentations- und Behörden-Informationspflichten ab.

Er erklärt ein Produkt nicht pauschal für „IVDR-exempt“, ersetzt keine nationale Rechtsprüfung und darf einen kommerziell bereitgestellten oder außerhalb der Gesundheitseinrichtung übertragenen IVD nicht in den Article-5(5)-Pfad hineininterpretieren.

## Kernprinzipien

- **Health institution scope first:** Organisation, Union-Sitz, primärer Zweck und ausschließliche interne Herstellung/Verwendung müssen belegt sein.
- **Article 5(5) is conditional, not a blanket exemption:** Annex-I-GSPR und alle aktuell anwendbaren Bedingungen bleiben verpflichtend.
- **No industrial scale or external transfer:** industrielle Herstellung oder Übertragung an eine andere juristische Person beendet den privilegierten In-house-Scope.
- **Transition dates are condition-specific:** jede Article-5(5)-Bedingung wird gegen ihren aktuellen IVDR-Anwendungszeitpunkt geprüft.
- **Market-equivalence justification is deferred for IVDs:** die Bedingung aus Artikel 5(5)(d), dass spezifische Bedürfnisse nicht durch ein gleichwertiges CE-gekennzeichnetes IVD am Markt erfüllt werden können, wird für IVDs erst ab 31. Dezember 2030 als zwingendes Gate behandelt, sofern das Recht nicht erneut geändert wird.

## Workflow

### 1. Health-Institution- und Device-Scope fixieren

Erfasse Organisation/Rechtsträger, Union-Sitz, Health-Institution-Rolle, Herstellungsort, Verwendungsort/-personen, Device/Intended Use, Scale, Transfers/Distribution, externe Leistungen und `asOf`.

### 2. Eligibility prüfen

Klassifiziere `eligible-inhouse|not-eligible|borderline|evidence-missing`. Prüfe insbesondere ausschließliche interne Herstellung/Verwendung, keine Übertragung an andere juristische Personen und nicht-industriellen Maßstab.

### 3. Condition-by-condition Applicability

Mappe die Bedingungen aus Artikel 5(5) einzeln auf `applicable-now|future-applicable|met|gap|not-applicable|uncertain`, einschließlich GSPR, QMS, Labor-/Akkreditierungsbezug soweit einschlägig, Dokumentation, öffentliche Erklärung, Behördeninformationen, Experience Review und corrective actions.

### 4. Market-Availability Condition zeitlich behandeln

Artikel 5(5)(d) wird separat mit Effective Date geführt. Vor dem 31.12.2030 kann Market-Availability-Evidence als vorausschauende Readiness vorbereitet werden, darf aber nicht als bereits geltende IVDR-Bedingung ausgegeben werden. Ab Anwendbarkeit muss die Begründung evidenzgebunden auf spezifische Patientengruppenbedürfnisse und gleichwertige CE-IVDs bezogen sein.

### 5. GSPR/QMS/Evidence Routing

- Annex-I-GSPR/Risk → bestehender Risk-/Evidence-Pfad.
- QMS/quality evidence → `medical-device-qms-iso13485` bzw. anwendbarer institutioneller Quality Owner.
- Performance Evidence → bestehende IVDR Performance Skills.
- externe Behörde/Publikation/Portal → verifizierter Human-/External-Action-Pfad.

### 6. Change-/Loss-of-Eligibility Trigger

Definiere Trigger wie External Transfer, Industrial Scale, geänderte Organisation/Rechtsträger, CE-Marktverfügbarkeit ab relevantem Datum, Intended-Use-/Performance-Änderung oder neue nationale Anforderungen. Bei Verlust der Eligibility → normaler IVDR Regulatory-/Conformity-Pfad.

## Output-Verträge

`inhouse-ivd-eligibility.json` enthält Health-Institution/Device Scope, Eligibility State, Legal/Guidance Sources, `asOf`, evidence und boundary rationale.

`inhouse-ivd-condition-map.json` enthält Article-5(5)-Condition, effective/applicability date, current state, evidence, gap, owner und next action.

`inhouse-ivd-transition-readiness.json` enthält future-applicable conditions, especially 5(5)(d), readiness evidence, trigger dates, monitoring owner und loss-of-eligibility routing.

## Memory Path

Persistenzwürdig sind nur abstrahierte validierte Article-5(5)-Eligibility-/Condition-/Transition-Muster mit Provenance/Freshness. Konkrete Patientengruppen, interne Testprotokolle, institutionelle Behördenkommunikation, nicht veröffentlichte Performance-Daten und volatile nationale/transition states bleiben run-only oder kontrollierte Health-Institution/Quality/Regulatory Records. Geeignete Kandidaten gehen ausschließlich an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- Health-Institution-, Union-, Internal-Use-, Transfer- und Scale-Scope belegt oder als Gap markiert sind,
- Article 5(5) nicht als pauschale IVDR-Befreiung dargestellt wird,
- jede Bedingung mit ihrem aktuellen Anwendungsdatum geführt wird,
- Article 5(5)(d) für IVDs vor dem 31.12.2030 nicht als bereits zwingendes Marktäquivalenz-Gate behandelt wird,
- Loss-of-Eligibility in den normalen IVDR-Pfad routet,
- externe Behörden-/Publikationszustände nicht simuliert werden,
- konkrete institutionelle/patientenbezogene Zustände nicht in globales dauerhaftes Memory gelangen.
