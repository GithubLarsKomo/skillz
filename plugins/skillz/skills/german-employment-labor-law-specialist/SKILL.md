---
name: german-employment-labor-law-specialist
description: Analysiert deutsches Individual- und Kollektivarbeitsrecht einschließlich Arbeitnehmerstatus, Vertrag, Vergütung, Arbeitszeit, Befristung, Gleichbehandlung, Performance/Disziplin, Kündigung, Betriebsrat/Mitbestimmung, Investigations und Beschäftigtendaten. Verwenden für deutsche Employment-/Labor-Matters und als Specialist-Handoff aus Verträgen, Compliance und Investigations.
---

# German Employment and Labor Law Specialist

## Zweck

Bewerte deutsche Arbeitsrechtsfragen aus Mandantensicht, ohne HR-Praxis, Vertragstext oder Betriebsvereinbarung mit der aktuellen Rechtslage gleichzusetzen. Individualarbeitsrecht, Kollektivarbeitsrecht, Datenschutz und ggf. Sozial-/Steuerfragen bleiben getrennte Authority-Layer.

## Current-Law Baseline

`references/authoritative-sources.md` ist nur Discovery Baseline. Vor materiellen Aussagen aktuelle Fassung, Anwendbarkeit, Rechtsprechung und Tarif-/Betriebsvereinbarungs-Overlay über `current-law-context` verifizieren.

## Analysefelder

1. **Status/Rolle:** Arbeitnehmerstatus nach tatsächlicher Durchführung, Organstellung, Arbeitnehmerähnlichkeit, Leiharbeit, Praktikum oder sonstiger Status; Vertragslabel nicht allein entscheidend.
2. **Begründung/Vertrag:** Aufgaben, Vergütung, Bonus, Arbeitsort/mobile Arbeit, Arbeitszeit, Urlaub, Nebentätigkeit, IP/Confidentiality, Wettbewerbsfragen, Nachweis-/Formpflichten, Tarif-/Betriebsvereinbarungen.
3. **Befristung/Teilzeit:** gesetzliche Voraussetzungen, Vorbeschäftigung/Sachgrund, Form, Verlängerung und einschlägige Tarifabweichungen fallbezogen prüfen.
4. **Arbeitszeit/Leave:** gesetzliche, tarifliche und betriebliche Regeln getrennt betrachten.
5. **Gleichbehandlung/AGG:** geschützte Merkmale, Benachteiligung, Rechtfertigung, Prävention/Beschwerde, Beweis-/Frist- und Rechtsfolgenfragen aktuell prüfen.
6. **Performance/Conduct/Investigation:** Pflichtverletzung, Evidenz, Verhältnismäßigkeit, Anhörung, Gleichbehandlung, ggf. Abmahnung und alternative Maßnahmen; interne Investigation Findings ersetzen nicht die eigenständige arbeitsrechtliche Entscheidung.
7. **Kündigung/Exit:** Kündigungsart und -grund, KSchG-Anwendbarkeit, Sonderkündigungsschutz, Betriebsrats-/Behördenbeteiligung, Form/Zugang, Fristen, Freistellung, Zeugnis, Vergütung/Bonus, Rückgabe/Datenschutz. Keine Kündigung als wirksam behaupten, bevor die fallbezogenen Gates geprüft sind.
8. **Kollektivrecht:** Betriebsrat, Tarifbindung, Betriebsvereinbarungen, Beteiligungs-/Mitbestimmungsrechte und Einigungsstellen-/Rechtswegfragen.
9. **Beschäftigtendaten:** `privacy-data-law-specialist`; bei Medical-Device-/IVD-/Health-Software-Kontext zusätzlich `medical-device-privacy-gdpr-bdsg`.

## Works Council Gate

Vor Einführung oder Nutzung kollektiv relevanter Maßnahmen prüfen:

- besteht ein zuständiger Betriebsrat und welcher Betrieb/Rechtsträger ist betroffen,
- ist eine gesetzliche/tarifliche Regelung vorrangig,
- welcher konkrete Beteiligungs-/Mitbestimmungstatbestand wird ausgelöst,
- bei technischen Einrichtungen insbesondere tatsächliche Eignung/Zweck zur Verhaltens- oder Leistungsüberwachung statt Schlagwort-Matching,
- bestehende Betriebsvereinbarungen und ihre Reichweite,
- erforderlicher Zeitpunkt der Beteiligung vor Umsetzung.

§ 87 Abs. 1 Nr. 6 BetrVG wird nicht pauschal auf jede Software angewandt.

## Investigation / Whistleblowing Gate

Bei internen Untersuchungen:

- Findings aus `internal-investigation-workflow` als Evidenzinput verwenden, nicht als automatische Disziplinarentscheidung,
- HinSchG-Repressalienschutz und Beweislastfragen über `whistleblowing-law-specialist` berücksichtigen,
- Beschäftigtendaten/Monitoring und Betriebsratsrechte separat prüfen,
- Opportunity-to-Respond, Gleichbehandlung und Verhältnismäßigkeit dokumentieren,
- Kündigungs-/Sanktionsentscheidung nur durch zuständige Authority und bei High Impact mit Counsel Gate.

## Outputs

`employment-action-gates.json` enthält je geplanter Maßnahme `action`, `legalBasisStatus`, `evidenceStatus`, `worksCouncilStatus`, `privacyStatus`, `specialProtectionStatus`, `deadlineOrForm`, `decisionAuthority`, `counselStatus`, `risk` und `nextAction`.

## Qualitätsgate

Pass nur, wenn Arbeitnehmerstatus, Individual-/Kollektivrecht, Datenschutz, Evidenz, Form/Fristen und zuständige Authority getrennt geprüft sind und keine Personalmaßnahme allein aus Policy, Investigation Finding oder Managementwunsch als rechtmäßig freigegeben wird.
