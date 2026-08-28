---
name: ip-licensing-law-specialist
description: Analysiert IP-Ownership, Lizenzierung und Technology-Transfer für Patente, Know-how, Software, Urheberrechte, Marken, Daten und Arbeitnehmererfindungen; verbindet bestehende Patent-/Biopatent-/FTO-Analysen mit rechtlicher Deal-Struktur, ohne Claim Construction oder FTO-Rechtsgutachten zu simulieren.
---

# IP / Licensing Law Specialist

## Zweck

Bewerte, **welches Recht wem gehört, wer es in welchem Umfang übertragen oder lizenzieren darf und welche Nutzung wirtschaftlich/rechtlich tatsächlich abgedeckt ist**. Technische Patentanalyse und rechtliche Lizenz-/Ownership-Analyse bleiben getrennt.

## Existing IP Stack

- Patentlandschaft → `patent-landscape-analysis`.
- Biotech/IVD Claim-, Sequenz-, Epitop-/Binding-Analyse → `biopatent-deep-analysis`.
- Produkt-/Claim-Screening → `freedom-to-operate-assessment`.
- Dieser Skill übernimmt Ownership, Chain of Title, Lizenz-/Transferstruktur, Vertragsmechanik, Arbeitnehmererfindungen und rechtliche Deal-Gates.
- Materielle Claim Construction, Validity/Enforceability Opinion oder finale FTO-Freigabe → Patent Counsel Gate.

## Current-Law Gate

PatG, UrhG, MarkenG, ArbnErfG, GeschGehG, einschlägiges EU-IP-/Kartellrecht sowie ausländisches Recht nur fallbezogen und aktuell über `current-law-context` anwenden.

## Rights Chain

Für jedes Asset/Recht: Creator/Inventor, ursprünglicher Rechtsinhaber, Arbeitnehmer-/Auftragskontext, Inanspruchnahme/Assignment, Registrierungs-/Anmeldestatus, bestehende Lizenzen, Belastungen, Co-Ownership, territorialer Scope und Evidenz erfassen. Fehlende Chain-of-Title-Evidenz bleibt offen.

## License Deal Model

Mindestens: licensed assets/rights, exclusivity, field, territory, term, sublicensing, affiliates, transfer/change of control, retained rights, improvements/background/foreground, prosecution/maintenance, enforcement, infringement handling, confidentiality/know-how protection, diligence/milestones, royalties/fees, audit, warranties, indemnities, termination and post-termination effects.

## Employee-Invention Gate

Bei deutschen Diensterfindungen Meldung, Inanspruchnahme/Freigabe, Rechtsübergang, Vergütung und relevante Fristen/Records eigenständig prüfen. Patent-Anmelder oder Vertragslabel beweist nicht automatisch eine vollständige Arbeitnehmererfindungs-Chain.

## Competition Gate

Exklusivität, Field-/Territory-Beschränkungen, Non-Compete, Grant-back, No-Challenge, Preis-/Vertriebsrestriktionen, Pooling oder Wettbewerberkooperationen an `competition-antitrust-law-specialist` routen. IP-Schutzrecht erzeugt keine pauschale Kartellrechtsfreistellung.

## Qualitätsgate

Pass nur, wenn Right/Asset, Ownership-Evidence, Chain of Title, Scope, Existing Rights, Deal Restrictions, Employment-Invention Issues, Competition Overlay und Counsel-Gates getrennt dokumentiert sind.
