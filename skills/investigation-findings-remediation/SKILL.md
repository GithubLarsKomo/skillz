---
name: investigation-findings-remediation
description: Übersetzt Untersuchungsevidenz in nachvollziehbare Findings, trennt Fakt, Inferenz und Rechtsbewertung und entwickelt Remediation-, Disziplinar-, Reporting-, CAPA-/Control- und Retest-Pfade. Verwenden am Ende oder bei Zwischenfeststellungen einer internen Investigation.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - legal-compliance-risk-assessment
  - compliance-control-mapping
outputs:
  - investigation-findings.json
  - investigation-remediation-plan.json
  - investigation-reporting-decisions.json
lastEvaluated: 2026-08-28
---

# Investigation Findings and Remediation

## Findings Discipline

Jede Allegation wird elementweise gegen die gesicherte Evidenz bewertet. Trenne ausdrücklich:

- `verified-fact`,
- `disputed-fact`,
- `inference`,
- `credibility-assessment`,
- `policy-rule-assessment`,
- `legal-assessment` nur mit verifiziertem Specialist/Current-Law-Kontext.

Ein evidentiary threshold wird nicht frei erfunden. Nutze den durch anwendbares Recht, verbindliches Regelwerk oder bestätigte Investigation Charter vorgegebenen Standard; fehlt er, markiere die Entscheidung als Governance Open Point.

## Outcome Status

Zulässige Outcome-Kategorien: `substantiated`, `partly-substantiated`, `unsubstantiated`, `inconclusive`, `outside-scope`, jeweils mit Evidenzreferenzen, Gegenargumenten, offenen Fakten und Confidence.

`unsubstantiated` bedeutet nicht automatisch „falsch gemeldet“; absichtliche oder grob fahrlässige Falschmeldung wird nur bei eigener belastbarer Evidenz und anwendbarem Recht bewertet.

## Remediation Layers

Je Finding prüfen:

1. Immediate containment / Schutzmaßnahmen.
2. Individual action oder Disziplinarmaßnahme – nur durch zuständige Authority und mit Employment/Counsel Gate.
3. Prozess-/Control-Remediation → `compliance-control-mapping` und Retest.
4. Produkt-/QMS-Folge → bestehende Complaint-, CAPA-, Vigilance-, Risk- oder Audit-Skills.
5. Policy/Training/Governance-Änderungen.
6. Restitution/Vertrags-/Business-Maßnahmen.
7. Behördliche, strafrechtliche, regulatorische oder sonstige externe Meldung – Entscheidung und Frist separat quellenbasiert prüfen.
8. Retaliation-/Safeguarding-Monitoring soweit relevant.

## Reporting Decision Gate

Eine externe Meldung wird weder automatisch aus einem substantiated Finding noch automatisch aus Managementinteresse ausgelöst. Erfasse `authority`, `trigger`, `deadline`, `decisionOwner`, `counselStatus`, `factsToReport`, `preservationStatus` und `decisionRationale`.

## Closure Gate

Ein Matter wird nicht geschlossen, solange kritische Safety-/Retaliation-Risiken, gesetzliche Reporting-Fristen, Evidence Holds, überfällige Remediation oder erforderliche Retests offen sind.

## Qualitätsgate

Pass nur, wenn Findings evidenzverknüpft sind, Fakt/Inferenz/Rechtsbewertung getrennt bleiben, Disziplinar-/Reporting-Entscheidungen einen Owner und Rechtsgate besitzen und systemische Ursachen in Controls/CAPA statt nur Individualmaßnahmen überführt werden.
