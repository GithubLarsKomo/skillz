---
name: contract-legal-context
description: Bestimmt für einen privaten oder beruflichen Vertragsfall die relevanten Parteirollen, Vertragsart, Rechtswahl, potenziell anwendbaren Rechtsordnungen, zwingenden Normen, Formanforderungen und Spezialrechts-Overlays und belegt materielle Rechtsaussagen mit aktuellen autoritativen Quellen. Verwenden vor Vertragsprüfung oder Vertragserzeugung.
userFacing: true
implicitInvocation: false
category: research-knowledge
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - research-to-evidence-note
outputs:
  - contract-legal-context.json
  - contract-legal-source-note.md
lastEvaluated: 2026-08-23
---

# Contract Legal Context

## Zweck

Dieser Skill beantwortet vor Review oder Drafting die Frage: **Welche Rechtsgrundlagen müssen für genau diesen Vertragsfall geprüft werden?**

Deutschland ist der Default-Ausgangspunkt. Der Skill darf deutsches Recht aber nicht allein aus Sprache, Wohnsitz eines Beteiligten oder Nutzerwunsch als anwendbar annehmen, wenn grenzüberschreitende oder spezialgesetzliche Anknüpfungen bestehen.

## Kernprinzipien

1. **Rechtsgrundlage vor Klauselbewertung.** Erst Parteirollen, Vertragstyp, Rechtswahl, Gerichtsstand und zwingende Regeln bestimmen, dann Klauseln bewerten.
2. **Aktuelle Primärquellen.** Materielle Rechtsaussagen werden soweit praktisch möglich anhand aktueller amtlicher Gesetzestexte, EUR-Lex, amtlicher Rechtsprechung oder vergleichbarer Primärquellen verifiziert.
3. **Keine erfundene Fremdrechtsanalyse.** Ist ausländisches Recht materiell, wird aktuelle verlässliche Recherche verlangt; reicht sie nicht, wird an qualifizierte Beratung in der betreffenden Rechtsordnung eskaliert.
4. **Zwingendes Recht schlägt Vertragswunsch.** Eine Rechtswahl oder Vorlage darf zwingende Schutzregeln nicht unsichtbar machen.
5. **Versionierung.** Jede Legal-Context-Ausgabe trägt `asOf`, Quellenstand und offene Rechtsfragen.

## Mindest-Intake

Ermittle soweit einschlägig:

- Parteien, Rechtsform und Rolle,
- Verbraucher / Unternehmer / Kaufmann / Arbeitnehmer / Arbeitgeber,
- Sitz, gewöhnlicher Aufenthalt und Niederlassungen,
- Leistungs- und Lieferorte,
- Vertragsgegenstand und Vertragstyp,
- bestehende Rechtswahl-, Gerichtsstands- oder Schiedsklauseln,
- B2C, B2B, C2C, Employment oder sonstige Konstellation,
- AGB-/Formularvertrag versus individuell ausgehandelte Bedingungen,
- digitale Leistungen, personenbezogene Daten, IP, regulierte Produkte/Dienstleistungen,
- Immobilienbezug, Sicherheiten, Finanzierung, Gesellschaftsbezug,
- internationale Warenlieferung oder sonstige grenzüberschreitende Leistung.

Fehlt eine fachliche Entscheidung, route zurück zu `round-based-requirements-grilling`; fehlt nur juristische Evidenz, recherchiere statt den Nutzer nach einer Rechtsmeinung zu fragen.

## Deutscher Baseline-Router

Lade bei deutschem Bezug `references/german-contract-law-routing.md`.

Die Baseline umfasst je nach Fall insbesondere:

- BGB Allgemeiner Teil und Schuldrecht,
- AGB-Recht (§§ 305 ff. BGB),
- Verbraucher-/Fernabsatz-/Widerrufsrecht,
- besondere Vertragstypen des BGB,
- HGB bei Handelsgeschäften,
- Arbeitsrecht einschließlich § 611a BGB und Spezialgesetzen,
- Datenschutzrecht einschließlich Art. 28 DSGVO bei Auftragsverarbeitung,
- IP-Spezialrecht bei Lizenz-/Rechteklauseln,
- weitere Spezialgesetze nur bei tatsächlichem Trigger.

Keine Norm wird allein wegen möglicher Relevanz als tatsächlich anwendbar behauptet.

## Internationaler Router

Bei grenzüberschreitenden Sachverhalten prüfe mindestens:

1. Rechtswahl und deren Reichweite.
2. Ohne wirksame/ausreichende Rechtswahl die Kollisionsregeln, innerhalb der EU regelmäßig Rom I für vertragliche Schuldverhältnisse.
3. Besondere Schutzregeln, insbesondere für Verbraucher und Arbeitsverträge.
4. Zuständigkeit / Gerichtsstandsmechanik, soweit für die Vertragsgestaltung relevant, innerhalb der EU regelmäßig Brüssel Ia.
5. Bei internationalen Warenkäufen die mögliche Anwendung des CISG einschließlich etwaiger vertraglicher Ein- oder Ausschlüsse.
6. Zwingende Normen, ordre public, Form- und Registeranforderungen.

Ein Gerichtsstand ist nicht mit einer Rechtswahl gleichzusetzen.

## Spezialrechts-Trigger

Setze `specialistOverlay` statt eine generische BGB-Antwort zu erzwingen, u. a. bei:

- `employment`,
- `real-estate`,
- `corporate-ma-financing`,
- `ip-licensing`,
- `data-processing-privacy`,
- `distribution-agency-franchise`,
- `regulated-industry-quality`,
- `public-procurement`,
- `competition-antitrust`,
- `consumer-digital-products`.

Für IVD/MedTech-/Pharma-nahe Qualitäts-, Entwicklungs-, Studien-, Daten- oder Lieferverträge können zusätzlich regulatorische Pflichten relevant sein; diese werden an vorhandene Regulated-Engineering-Skills übergeben, statt hier dupliziert zu werden.

## Form Gate

Ermittle, ob:

- Formfreiheit genügt,
- Textform,
- Schriftform,
- qualifizierte elektronische Signatur,
- öffentliche Beglaubigung,
- notarielle Beurkundung,
- Register-/Behördenhandlung

erforderlich oder vertraglich vereinbart ist. Unterscheide gesetzliche von lediglich vertraglich vereinbarter Form.

## Output

`contract-legal-context.json` enthält mindestens:

- `schemaVersion`, `asOf`, `jurisdictionAssessmentStatus`,
- `partyRoles`, `contractType`, `transactionContext`,
- `governingLaw`, `choiceOfLaw`, `forum`, `arbitration`,
- `mandatoryRules`, `specialistOverlays`, `formRequirements`,
- `sourceAuthorities`, `materialUnknowns`, `counselEscalations`, `confidence`.

Statuswerte:

- `supportable`,
- `supportable-with-caveats`,
- `jurisdiction-uncertain`,
- `specialist-law-required`,
- `qualified-counsel-review-required`.

`contract-legal-source-note.md` dokumentiert nur die für den konkreten Fall materiellen Normen und Quellen, nicht eine enzyklopädische Gesetzessammlung.

## Prüfungen

Pass nur wenn Parteirollen und Rechtsordnung getrennt bestimmt werden; Verbraucher-/Arbeits-/B2B-Unterschiede sichtbar sind; Rechtswahl und Gerichtsstand nicht verwechselt werden; aktuelle Quellen für materielle Rechtsaussagen verwendet werden; Spezialrecht nur bei Trigger aktiviert wird; ausländisches Recht nicht erfunden wird; Formfragen geprüft und Unsicherheiten offen ausgewiesen werden.

## Abschluss

Der Skill endet mit einem versionierten, quellenbelegten Legal-Context-Handoff, der Review oder Drafting eine belastbare Rechtsgrundlagenkarte liefert oder den Fall gezielt an die erforderliche Fachberatung eskaliert.
