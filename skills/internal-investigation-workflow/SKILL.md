---
name: internal-investigation-workflow
description: Orchestriert interne Untersuchungen von Allegation-Triage, Independence/Privilege und rechtmäßiger Beweissicherung über Interview-/Fact-Finding bis Findings, Reporting, Remediation, Repressalienschutz und Final Gate. Verwenden für Whistleblowing-, Compliance-, Audit-, Safe-Sport- oder Management-Untersuchungen.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - whistleblowing-law-specialist
  - investigation-evidence-preservation
  - investigation-findings-remediation
  - legal-matter-final-gate
outputs:
  - investigation-charter.json
  - investigation-workplan.json
  - investigation-status.json
  - investigation-handoff.json
lastEvaluated: 2026-08-28
---

# Internal Investigation Workflow

## Zweck

Führe eine faire, beweisorientierte und rechtlich geroutete interne Untersuchung. Der Workflow darf Whistleblowing-Recht, Arbeitsrecht, Strafrecht, Datenschutz, Safe Sport oder regulatorische Fachlogik nicht durch generische Investigation-Praxis ersetzen.

## 1. Triage and Immediate-Risk Gate

Erfasse Allegation, Quelle, betroffene Personen/Einheiten, Zeitraum und bekannte Evidenz. Prüfe sofort:

- laufende Gefahr für Personen/Safety,
- Repressalien- oder Beeinflussungsrisiko,
- drohenden Evidence Loss,
- mögliche gesetzliche/regulatorische Meldefristen,
- Interessenkonflikte im vorgesehenen Investigation Team,
- Straf-/Litigation-/Privilege-Nähe.

Schutz-/Containment-Maßnahmen dürfen die Untersuchung nicht unnötig vorwegnehmen und benötigen zuständige Authority.

## 2. Legal/Rule Scope

- Whistleblowing-Fall → `whistleblowing-law-specialist`.
- Nicht jede interne Beschwerde fällt unter HinSchG; der Workflow bleibt auch für außerhalb liegende Untersuchungen nutzbar.
- Safe-Sport-/Vereins-/Verbandsfall → deutscher Sport-/Vereins-Specialist plus tatsächlich bindendes Regelwerk.
- Produkt-/QMS-Fall → Complaint/Vigilance/CAPA/Audit Routing parallel aktivieren.
- Employment, Criminal, Privacy/Data, Antitrust oder andere Specialists über `legal-specialist-router` einbinden.

## 3. Investigation Charter

Dokumentiere `mandate`, `decisionOwner`, Investigator, Unabhängigkeit/Conflict Check, Allegations/Elements, Scope/Out-of-Scope, Jurisdictions, Evidentiary Standard falls verifiziert, Data/Privilege Rules, Reporting Lines, Milestones und Change-Control für Scope-Erweiterungen.

## 4. Evidence First

Vor breiten Interviews `investigation-evidence-preservation` durchführen. Erstelle Timeline und Evidence Map. Hypothesen bleiben ausdrücklich vorläufig; suche sowohl belastende als auch entlastende Evidenz.

## 5. Interviews

Interviewplan priorisiert Wissensnähe, Evidence Dependencies und Manipulationsrisiko. Für jedes Interview:

- Rolle und Themen/Elements,
- anwendbare Information-, Vertretungs-/Begleit- oder Mitbestimmungsfragen vorab prüfen,
- offene Fragen vor konfrontativen Detailfragen,
- Fact vs. hearsay vs. inference markieren,
- relevante Dokumente kontrolliert vorhalten,
- Protokollform, Review/Bestätigung und Datenzugriff rechtlich passend festlegen,
- keine Drohung, Täuschung über Rechte oder erzwungene Selbstbelastungsannahmen erfinden.

Betroffenen Personen wird vor einem nachteiligen Finding eine sachgerechte Möglichkeit zur Stellungnahme gegeben, soweit Recht/Regelwerk/Verfahrensfairness dies verlangen und keine zulässige Ausnahme greift.

## 6. Findings and Remediation

→ `investigation-findings-remediation`.

Separate Entscheidungen für Individualmaßnahmen, systemische Controls/CAPA, Behörden-/Regulatory Reporting, Litigation Strategy und Retaliation Monitoring. Das Investigation Team empfiehlt nur innerhalb seiner Authority.

## 7. Communication and Confidentiality

Need-to-know statt pauschaler Geheimhaltung. Whistleblower-, Beschuldigten-, Zeugen- und Drittidentitäten werden nach jeweils anwendbarem Recht geschützt. Statuskommunikation darf Evidence Collection, Rechte Betroffener oder regulatorische Pflichten nicht beeinträchtigen.

## 8. Closure / Final Gate

`legal-matter-final-gate` prüft offene High-Risk-Findings, Reporting Deadlines, Evidence Holds, Retaliation/Safety, Remediation/Retest und erforderliche Counsel-/Authority-Entscheidungen. Erst danach `closed`, `closed-with-monitoring` oder `escalated`.

## Qualitätsgate

Pass nur, wenn Investigator-Unabhängigkeit, Current-Law/Rule Scope, Evidence Integrity, Datenschutz, Fairness, Repressalienschutz, Findings-Lineage und Remediation/Reporting sauber getrennt und versioniert sind.
