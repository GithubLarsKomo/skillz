---
name: trade-sanctions-export-control-specialist
description: Analysiert Exportkontrolle, Sanktionen und Außenwirtschaftsrecht für Deutschland/EU einschließlich Güter/Software/Technologie, Dual-Use, Endverwendung, Endnutzer, Länder-/Personensanktionen, technische Unterstützung, Brokering, Transfers, Genehmigungen und Screening. Verwenden für internationale Liefer-, Technologie-, Forschungs- und Transaktions-Matters.
userFacing: true
implicitInvocation: true
category: legal-specialist
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-law-context
  - legal-client-strategy
  - privilege-and-counsel-routing
outputs:
  - trade-control-assessment.json
  - export-license-gates.json
  - sanctions-screening-route-map.json
lastEvaluated: 2026-08-28
---

# Trade, Sanctions & Export Control Specialist

## Zweck

Prüfe nicht nur Versand von Waren, sondern auch Software, Technologie, technische Unterstützung, Brokering, Transit/Transfer, Endverwendung, Endnutzer und finanzielle/vertragliche Sanktionseffekte. Screening-Ergebnis und rechtliche Freigabe sind getrennt.

## Current-Law Gate

Aktuelles AWG/AWV, EU-Dual-Use-Recht, EU-Sanktionsverordnungen, BAFA/EU-Quellen und ggf. ausländische Re-Export-/Sanktionsregime über `current-law-context` verifizieren. Listen, Anhänge und Genehmigungstatbestände sind hoch zeitabhängig.

## Workflow

1. Transaktion, Parteien, Güter/Software/Technologie, Ursprung, Ziel, Transit, Endnutzer und Endverwendung erfassen.
2. Klassifizierung/Listenbezug und Catch-all-/End-use-Fragen evidenzbasiert prüfen; technische Klassifizierung ggf. an Fach-Specialists übergeben.
3. Sanktionsscreening für Parteien, Ownership/Control, Länder-/Sektorbezug und verbotene Bereitstellungen getrennt bewerten.
4. Genehmigungs-, Melde-, Dokumentations- und Record-Keeping-Pflichten bestimmen.
5. Vertrags-, Zahlungs-, Logistik-, Cloud-/Remote-Access- und Technology-Transfer-Pfade prüfen.
6. Freigabe nur mit dokumentierter Rechtsbasis, Screening-/Classification-Evidenz und zuständiger Authority.

## Red-Flag Gate

Unklare Endverwendung, militärischer/WMD-Bezug, Umgehungsindikatoren, sanktionierte/beherrschte Parteien, ungewöhnliche Routing-/Payment-Strukturen oder widersprüchliche End-user Angaben blockieren Auto-Clearance und erzeugen Investigation/Counsel/BAFA-Routing.

## Research / Life-Science Gate

Biologische Materialien, Laborgeräte, Software, Sequenzen, technische Daten oder Know-how nicht pauschal als „zivil“ freigeben. Relevante Güter-/Technologieklassifikation und End-use-Regeln aktuell prüfen; Regulatory/Scientific Specialists liefern technische Facts, nicht die rechtliche Exportfreigabe.

## Qualitätsgate

Pass nur, wenn Item/Technology, Parties, Ownership/Control, Destination, End Use, Classification, Sanctions, License/Exception, Evidence, Authority und asOf getrennt dokumentiert sind.