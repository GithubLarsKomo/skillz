---
name: private-legal-matter-router
description: Routet private deutsche/europäische Rechtsangelegenheiten getrennt vom Unternehmens-/Konzernkontext nach Rechtsgebiet, Dringlichkeit, Verfahrenslage, benötigter Specialist-Kompetenz und externer Authority. Verwenden für persönliche Vertrags-, Verbraucher-, Miet-, Immobilien-, Arbeits-, Familien-, Erb-, Steuer-, Versicherungs-, Verkehrs-, Straf-/Bußgeld- oder sonstige Privatmatters.
---

# Private Legal Matter Router

## Zweck

Private Matters werden **nicht** als Variante eines Unternehmensmatters behandelt. Mandant, Rechtsdienstleistungs-/Vertretungsgrenzen, Interessenkonflikte, Kosten-/Versicherungsthemen und externe Behörden-/Gerichts-/Notar-/Counsel-Gates werden eigenständig bestimmt.

## Boundary Gate

Die RDG-Ausnahme für Rechtsangelegenheiten innerhalb verbundener Unternehmen darf nicht auf private Matters übertragen werden. Für Deutschland aktuelle RDG-/Berufs-/Verfahrensregeln über `current-law-context` prüfen. Selbsthilfe, allgemeine Information, AI-Unterstützung, fremde Rechtsdienstleistung und formelle Vertretung sind nicht gleichzusetzen.

## Private Domains

Route insbesondere:

- private Verträge / Kauf / Dienstleistung / Verbraucher / Versicherung → `german-consumer-insurance-private-contract-law-specialist`,
- Wohnraummiete und private Immobilien → `real-estate-law-specialist`,
- eigenes Arbeitsverhältnis → `german-employment-labor-law-specialist`,
- Familie/Scheidung/Unterhalt/Sorge/Partnerschaft → `german-family-law-specialist`,
- Erbe/Testament/Pflichtteil/Schenkung/Nachfolge → `german-inheritance-succession-law-specialist`,
- private Tax Matters → `tax-legal-interface-specialist`,
- Verkehrsstraf-/OWi-Verfahren → `german-criminal-administrative-offence-procedure-specialist`,
- Fahrerlaubnis/Verkehrsverwaltung/sonstiges Verwaltungs-/Sozialrecht → `german-administrative-social-traffic-law-specialist`,
- Datenschutz/Persönlichkeitsrecht → `privacy-data-law-specialist`,
- Zivilstreit → `dispute-litigation-strategy-specialist`,
- Straf-/Ermittlungsverfahren → `german-criminal-administrative-offence-procedure-specialist`,
- sonstige Spezialgebiete → `capability-gap` plus präzise Professional/Counsel Work Order.

## Cross-Domain Routing

Ein privates Matter kann mehrere Specialists parallel benötigen. Beispiele:

- Scheidung + Immobilie + Steuer → Family + Real Estate + Tax Interface.
- Nachfolge + GmbH-Anteil + Immobilie + Steuer → Inheritance + Corporate Governance/Transactions + Real Estate + Tax Interface.
- Verkehrsunfall + Personenschaden + Versicherung + Bußgeld → Consumer/Insurance + Product/General Liability falls einschlägig + Criminal/OWi + ggf. Public-Law/Driving-Licence.
- Private Cyber-/Datenschutzverletzung → Privacy/Data + Digital/AI/Cyber + Dispute/Criminal je Sachlage.

## Urgency Gate

Sofort priorisieren bei laufender Frist, Zustellung/Bescheid/Klage, Durchsuchung/Vorladung/Ermittlungsmaßnahme, drohendem Rechtsverlust, Gewaltschutz/Kindswohl, Kündigungs-/Räumungs-/Vollstreckungslage, Verjährungs-/Ausschlussfrist oder irreversibler Vermögensdisposition. Konkrete Frist nur aus Dokument und aktueller Rechtslage ableiten.

## Representation / Authority Gate

Für Gericht, Behörde, Notariat, Steuerbehörde, Strafverteidigung oder sonstige formelle Vertretung prüfen, wer handeln darf/muss. Der Workflow darf Schriftsatz-/Entscheidungsgrundlagen vorbereiten, aber keine externe Zulassung oder Vollmacht simulieren.

## Conflict / Client Gate

Mandant und Gegenpartei explizit erfassen. Private Interessen nicht mit Unternehmensinteressen, Arbeitgeberinteressen oder Familienangehörigen vermischen. Bei möglichem Konflikt getrennte Matter States und ggf. unabhängige Beratung vorsehen.

## Legal Expense / Insurance Gate

Rechtsschutz-, Haftpflicht-, D&O-/private Versicherungsdeckung, Selbstbehalt, Melde-/Zustimmungsanforderungen und freie Anwaltswahl nur prüfen, wenn relevant; Deckung nicht aus Versicherungsname ableiten. Fristwahrung hat Vorrang vor ungeklärter Deckung, wenn sonst Rechtsverlust droht.

## Output

Jeder Route-Eintrag enthält `client`, `matterType`, `jurisdiction`, `urgency`, `document/deadline`, `specialist`, `authority/representationNeed`, `facts`, `unknowns`, `evidence`, `insurance`, `conflictStatus`, `nextSafeAction` und `escalationLevel`.

## Qualitätsgate

Pass nur, wenn privater Mandant, Matter Domain, Fristen/Dringlichkeit, Specialist Ownership, Vertretungs-/Authority-Gate, Interessenkonflikt und nächste sichere Aktion explizit sind und keine Konzern-/RDG-Annahme auf das Privatmatter übertragen wird.
