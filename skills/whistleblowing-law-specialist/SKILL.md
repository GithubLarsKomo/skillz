---
name: whistleblowing-law-specialist
description: Analysiert Hinweisgeber- und Meldestellenrecht mit Schwerpunkt Deutschland/EU, insbesondere HinSchG, Vertraulichkeit, Meldekanäle, Verfahrensfristen, Datenschutz, Repressalienschutz und Folgemaßnahmen. Verwenden für Whistleblowing-Systeme und einzelne Meldungen vor einer internen Untersuchung.
userFacing: true
implicitInvocation: true
category: legal-specialist
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-law-context
  - privilege-and-counsel-routing
outputs:
  - whistleblowing-law-assessment.json
  - reporting-office-obligations.json
  - whistleblowing-source-note.md
lastEvaluated: 2026-08-28
---

# Whistleblowing Law Specialist

## Zweck

Bestimme für eine Organisation oder konkrete Meldung, welche Hinweisgeberregeln tatsächlich gelten und welche Verfahrens-, Vertraulichkeits-, Datenschutz- und Schutzpflichten daraus folgen. Schwerpunkt ist Deutschland/EU; grenzüberschreitende Konzernsysteme benötigen zusätzlich das jeweilige lokale Recht.

## Current-Law Gate

`references/authoritative-sources.md` dient nur als Discovery Baseline. Vor jeder materiellen Aussage muss `current-law-context` die aktuelle Fassung und den relevanten Zeitraum verifizieren.

Für Deutschland prüfe insbesondere:

- persönlichen und sachlichen Anwendungsbereich,
- Pflicht zur internen Meldestelle und etwaige sektorale Sonderregeln,
- Organisationsform, Unabhängigkeit/Fachkunde und Interessenkonflikte,
- zulässige Meldekanäle und tatsächliche Zugriffsberechtigungen,
- Eingangsbestätigung, Stichhaltigkeitsprüfung, Folgemaßnahmen und Rückmeldung,
- Vertraulichkeit und zulässige Identitätsweitergabe,
- personenbezogene Daten und besondere Kategorien,
- Dokumentation, Aufbewahrung/Löschung,
- Repressalien, Beweislast, Schadensersatz und Sanktionen,
- Verhältnis zu spezifischeren Meldeverfahren.

## Wichtige Deutschland-Gates

- Beschäftigtenzahl und Sondersektor werden nicht geschätzt; § 12 HinSchG wird fallbezogen geprüft.
- Anonyme Meldungen sollen bearbeitet werden; eine generelle Pflicht, anonyme Abgabe technisch zu ermöglichen, wird nicht erfunden.
- Die HinSchG-Dokumentationsfrist wird nur auf tatsächlich vom Gesetz erfasste Meldestellen-Dokumentation angewandt; andere Investigation Records können andere Rechtsgrundlagen und Retention Periods haben.
- Eine zentrale Konzernstelle ersetzt nicht automatisch sämtliche Rechtsträgerpflichten; Entity-, Rollen- und lokale Rechtslage bleiben sichtbar.
- Repressalien werden als eigenes Schutz- und Monitoring-Risiko behandelt.

## Data/Employment/Works-Council Gate

Bei Beschäftigtendaten aktuelle DSGVO/BDSG-Rechtsgrundlagen, Erforderlichkeit, Zweckbindung, Datenminimierung, besondere Kategorien, Transparenz-/Betroffenenrechte, Security und Retention prüfen. Technische Überwachungsmaßnahmen oder andere mitbestimmungsrelevante Gestaltungen werden an deutsches Arbeits-/Betriebsverfassungsrecht geroutet; § 87 Abs. 1 Nr. 6 BetrVG wird nur bei tatsächlichem Trigger angewandt.

## Output

`whistleblowing-law-assessment.json` enthält mindestens `asOf`, `entities`, `jurisdictions`, `scopeStatus`, `reportingOfficeDuty`, `channelRequirements`, `confidentialityRules`, `procedureDeadlines`, `dataProtectionRoutes`, `retaliationProtections`, `retentionRules`, `externalReportingRoutes`, `materialUnknowns` und `counselEscalations`.

## Qualitätsgate

Pass nur, wenn Fassung/AsOf, Entity Scope, Vertraulichkeit, Deadlines, Datenschutz und Repressalienschutz quellenbelegt sind und aus HinSchG/EU-Richtlinie keine nicht verifizierte pauschale Konzern- oder Fremdrechtslösung abgeleitet wird.
