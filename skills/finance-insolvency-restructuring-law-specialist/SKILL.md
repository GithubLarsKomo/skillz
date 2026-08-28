---
name: finance-insolvency-restructuring-law-specialist
description: Analysiert unternehmerische Finanzierungs-, Sicherheiten-, Covenant-, Distress-, Restrukturierungs- und Insolvenzrechtsmatters für Deutschland einschließlich Darlehen, Garantien/Bürgschaften, Intercompany Finance, StaRUG/InsO-Trigger und Organ-/Creditor-Schnittstellen, ohne Steuer-, Accounting- oder formelle Insolvenzberatung zu simulieren.
userFacing: true
implicitInvocation: true
category: legal-specialist
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-law-context
  - corporate-governance-law-specialist
  - legal-compliance-risk-assessment
  - privilege-and-counsel-routing
outputs:
  - finance-restructuring-law-assessment.json
  - distress-trigger-map.json
  - finance-counsel-work-orders.json
lastEvaluated: 2026-08-28
---

# Finance, Insolvency & Restructuring Law Specialist

## Zweck

Strukturiere Finanzierung und Distress rechtlich zwischen Vertrag, Sicherheiten, Governance, Liquidität/Going Concern, Restrukturierung und Insolvenz. Finance/Accounting/Tax-Facts bleiben bei den zuständigen Fachfunktionen; der Skill verarbeitet bestätigte Zahlen und leitet Rechtsfragen/Gates ab.

## Current-Law Gate

Aktuelle BGB/HGB-/Gesellschafts-, InsO-, StaRUG- und ggf. grenzüberschreitende Insolvenz-/Sicherheitenregeln je `asOf` verifizieren. Finanzierungsvertrag, Sicherheitenvertrag und Corporate Approvals sind Matter Evidence, keine gesetzlichen Rechtsquellen.

## Financing Structure Gate

Darlehensgeber/-nehmer, Betrag/Währung, Laufzeit, Zins, Auszahlungsvoraussetzungen, Covenants, Events of Default, Kündigung, Sicherheiten, Garantien/Bürgschaften, Rang/Subordination, Cash Pooling/Intercompany, Assignment/Transfer und Governing Law getrennt erfassen.

## Authority / Corporate Benefit Gate

Vertretung, Organ-/Gesellschafterzustimmung, Corporate Benefit, Related Party, Interessenkonflikte, Kapitalerhaltung und gruppeninterne Finanzierung separat prüfen. Konzerninteresse ersetzt keine gesellschaftsspezifische Authority-/Duty-Analyse.

## Distress Trigger Gate

Liquidity, overdue obligations, covenant breach, forecast, financing availability, creditor pressure and restructuring indicators as verified facts collect. Drohende/aktuelle Insolvenzantrags-, Zahlungs-/Handlungs- oder Organpflichten nicht aus einem einzelnen KPI ableiten; aktuelle gesetzliche Tatbestände, Prognosezeiträume, Verantwortlichkeit und Evidence prüfen.

## Restructuring Gate

Out-of-court amendment/waiver, standstill, new money, security changes, debt/equity measures, StaRUG and formal insolvency as separate routes. Creditor classes, affected claims, voting/consent, avoidance/subordination, employee, tax, regulatory and transaction consequences separately route.

## Payment / Transaction Risk Gate

In Distress Zahlungen, Sicherheitenbestellungen, Asset Transfers, Intercompany Flows, Set-off, Guarantees and management decisions auf aktuelle insolvency/avoidance/liability implications prüfen. Keine „business as usual“-Freigabe nur weil vertraglich geschuldet.

## Tax / Accounting / Valuation Interface

Tax → `tax-legal-interface-specialist`; Accounting/Going-Concern/Valuation to appropriate finance/audit experts. AI Legal Layer darf unbestätigte Forecasts oder Bewertungen nicht als Rechtsfakt festschreiben.

## Counsel / Filing Gate

Bei möglichem Insolvenzantragstatbestand, StaRUG/formellem Verfahren, Gläubigerstreit, Security Enforcement, Material Director Liability oder grenzüberschreitendem Distress früh Specialized Counsel einbinden. Formelle Anträge, Insolvenzeröffnungs-/Restrukturierungsakte und externe Vertretung bleiben außerhalb des AI-Authority-Bereichs.

## Qualitätsgate

Pass nur, wenn Finance-Struktur, Authority/Corporate Benefit, bestätigte Financial Facts, Distress-/Insolvenztrigger, Restructuring Options, Payment/Transaction Risk, Tax/Accounting Interfaces und Counsel/Filing Gate getrennt dokumentiert sind.