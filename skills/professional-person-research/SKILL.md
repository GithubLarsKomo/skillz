---
name: professional-person-research
description: Verdichtet öffentlich zugängliche, berufsbezogene Quellen zu einem nachvollziehbaren professionellen Personenprofil mit Timeline, Claims, Quellen, abgeleiteten Capabilities, Widersprüchen und sichtbaren Evidenzlücken. Verwenden, wenn der berufliche Hintergrund einer konkreten Person für Executive Search, Expert Search, Meeting Prep oder Due-Diligence-nahe Recherche strukturiert werden soll, ohne Rollenfit, Persönlichkeitsdiagnostik oder Hiring-Entscheidung vorwegzunehmen.
userFacing: true
implicitInvocation: true
category: research-knowledge
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - research-to-evidence-note
outputs:
  - person-professional-profile.json
  - person-professional-profile.md
  - person-evidence-note.json
  - person-source-register.json
lastEvaluated: 2026-08-20
---

# Professional Person Research

## Zweck und Grenze

Erzeuge aus tatsächlich zugänglichen, öffentlich verfügbaren und berufsbezogenen Quellen ein prüfbares professionelles Profil einer konkreten Person.

Der Skill beantwortet ausschließlich:

> **What professional evidence exists about this person?**

Er ist **kein Suchanbieter, Scraper, Datenbroker, Personality Profiler, Rollenfit-Scorer, Background Check für private Lebensbereiche oder Einstellungsentscheidungssystem**.

Retrieval erfolgt über vorhandene Werkzeuge. Die generische Claim-/Source-/Confidence-Logik wird über `research-to-evidence-note` wiederverwendet und nicht parallel neu implementiert.

## Trigger

Verwenden, wenn mindestens eines zutrifft:

- der berufliche Hintergrund einer konkreten Person soll nachvollziehbar recherchiert werden,
- eine Professional Timeline muss aus mehreren Quellen konsolidiert werden,
- berufliche Fähigkeiten sollen aus belegbaren Erfahrungen abgeleitet werden,
- widersprüchliche öffentliche Angaben zu Rollen oder Zeiträumen müssen sichtbar gemacht werden,
- ein nachgelagerter Skill benötigt ein belastbares Personenprofil statt unstrukturierter Webtreffer.

Nicht verwenden für private Background Checks oder wenn der Auftrag bereits ausschließlich eine rollenbezogene Fit-Bewertung ist; dafür ist ein separater Capability-Mapping-Skill vorgesehen.

## Voraussetzungen

Vor Recherche fixieren:

1. eindeutige oder hinreichend disambiguierte Person,
2. Recherchefrage und professionellen Nutzungskontext,
3. zeitlichen Geltungsbereich,
4. bekannte Namensvarianten und Organisationen nur soweit für Disambiguierung notwendig,
5. gegebenenfalls einen `role-search-brief` als Kontext, ohne ihn bereits zur Bewertung zu verwenden.

Wenn die Identität nicht hinreichend sicher ist, keine Profile verschiedener Personen verschmelzen.

## Quellenhierarchie

Bewerte Quellen relativ zur konkreten beruflichen Aussage.

### Tier A — Primärquellen

Bevorzugt:

- aktuelle oder historische Arbeitgeber-Webseiten,
- offizielle Management-Biografien,
- Geschäfts- und Jahresberichte,
- offizielle Unternehmensmeldungen,
- Register- oder Filing-Dokumente soweit berufsrelevant,
- Patentdokumente,
- wissenschaftliche Publikationen,
- Konferenzprogramme,
- Universitäts- und Institutsseiten.

### Tier B — starke professionelle Sekundärquellen

- etablierte Wirtschafts- und Fachmedien,
- hochwertige Branchenpublikationen,
- belastbare professionelle Interviews oder Profile.

### Tier C — berufliche Selbstdarstellung

- LinkedIn oder vergleichbare professionelle Profile,
- persönliche professionelle Websites,
- Speaker Bios,
- Autorenprofile.

Selbstaussagen müssen als solche erkennbar bleiben und dürfen nicht allein wegen professioneller Darstellung als unabhängig bestätigt behandelt werden.

### Tier D — Kontextquellen

- Podcasts,
- öffentliche Präsentationen,
- öffentlich zugängliche Social-Media-Inhalte mit eindeutig beruflichem Bezug.

Sie dienen primär Kontext und können belastbare Claims nur entsprechend ihrer Quellenqualität stützen.

## Research Scope

Typische berufsbezogene Dimensionen:

- aktuelle und frühere Arbeitgeber,
- Rollen und Funktionsbezeichnungen,
- Beschäftigungszeiträume,
- berichteter Verantwortungsumfang,
- Produkte, Technologien und Märkte,
- Regionen und Internationalität,
- Führungs- und Organisationsumfang soweit belegt,
- P&L-/Budget-/Geschäftsverantwortung soweit belegt,
- dokumentierte Launches, Transformationen, Integrationen oder Turnarounds,
- wissenschaftliche Publikationen,
- Patente und Erfindertätigkeit,
- Board- oder Advisory-Mandate,
- berufliche Ausbildung und Qualifikation,
- öffentliche professionelle Aussagen, sofern für die Forschungsfrage relevant.

## Nicht zu recherchierende oder zu persistierende Bereiche

Ohne eigenständigen legitimen und zulässigen Auftrag nicht erheben, bewerten oder persistent übernehmen:

- private Wohnadressen,
- private Telefonnummern,
- Familienverhältnisse,
- Religion,
- ethnische Zugehörigkeit,
- sexuelle Orientierung,
- Gesundheitsinformationen,
- politische Überzeugungen,
- Gewerkschaftszugehörigkeit,
- private Freizeitaktivitäten ohne berufliche Relevanz,
- sonstige geschützte oder für die berufliche Qualifikation irrelevante persönliche Merkmale.

Keine Proxy-Ableitungen solcher Merkmale.

## Professional Timeline

Erzeuge eine chronologische Timeline. Jeder Eintrag enthält mindestens:

- Organisation,
- Rolle,
- Start-/Ende soweit belegt,
- bestätigten oder berichteten Scope,
- Claim-Referenzen,
- Quellenreferenzen,
- Unsicherheiten und Konflikte.

Keine scheinpräzisen Monats- oder Tagesangaben erzeugen, wenn nur Jahre belegt sind.

Widersprechende Zeitangaben nicht stillschweigend harmonisieren.

## Claim-Modell

Nutze `research-to-evidence-note` für atomare Claims, Quellenreferenzen, `basis`, `confidence`, Widersprüche und offene Fragen.

Für personenbezogene professionelle Recherche sind insbesondere folgende Claim-Typen zu unterscheiden:

- `employment-fact`
- `scope-fact`
- `achievement-fact`
- `self-reported-professional-claim`
- `publication-or-patent-fact`
- `derived-capability`
- `unknown`

Die Typen ergänzen den bestehenden Evidence Contract, ersetzen ihn nicht.

## Fact / Inference Boundary

Beispiel:

```text
FACT:
Person war von X bis Y VP R&D.

EVIDENCE:
Offizielle Unternehmensbiografie.

DERIVED:
Die Person hatte wahrscheinlich Führungsverantwortung im Bereich R&D.

NOT ESTABLISHED:
Teamgröße.
Budgetverantwortung.
Qualität der Führung.
Persönlicher Anteil am Unternehmenserfolg.
```

Zwingende Regeln:

```text
Job Title != Capability
Company Success != Individual Achievement
Presence During Event != Responsibility For Event
```

## Achievement Attribution

Ein Unternehmenserfolg darf einer Person nur zugerechnet werden, wenn eine Quelle deren Rolle oder Beitrag hinreichend konkret beschreibt.

Beispiel:

- zulässig: „Die Pressemitteilung nennt Person X als Leiter des Programms Y.“
- nicht zulässig: „Unternehmen Y wuchs während ihrer Amtszeit; daher hat sie das Wachstum verursacht.“

Korrelation in der Timeline ist keine Attribution.

## Capability Extraction

Capabilities dürfen als `derived` aus mehreren belegten Claims abgeleitet werden.

Beispiel:

```json
{
  "capability": "IVD product development leadership",
  "claimRefs": ["C3", "C7", "C9"],
  "basis": "derived",
  "confidence": "high",
  "limitations": [
    "team size unknown"
  ]
}
```

Jede Capability muss auf ihre Claims zurückverfolgbar bleiben.

Keine Capabilities aus Prestige, Titelinflation, Unternehmensgröße oder bloßer Medienpräsenz ableiten.

## Negative Evidence

Nicht gefundene Information wird als `not-found` dokumentiert und nicht als Negation der Realität behandelt.

Zulässig:

> Keine belastbare öffentlich zugängliche Evidenz für direkte P&L-Verantwortung gefunden.

Nicht zulässig:

> Die Person hat keine P&L-Erfahrung.

Ausnahme: Eine belastbare Quelle bestätigt explizit das Fehlen beziehungsweise den begrenzten Scope.

## Disambiguierung

Vor Zusammenführung von Quellen prüfen:

- vollständiger Name und Varianten,
- Arbeitgeber-/Institutionsüberschneidung,
- Fachgebiet,
- geografischer Kontext,
- Publikations-/Patentaffiliationen,
- Zeitachsenkompatibilität.

Bei Identitätskonflikt Profile getrennt halten und `identityConfidence` herabsetzen.

## Aktualität

Jedes Profil enthält:

- `researchedAt`,
- `evidenceCurrentThrough`,
- Stand der wichtigsten Quellen,
- bekannte Aktualitätslücken.

Zeitabhängige Angaben wie aktuelle Rolle, Arbeitgeber oder Board-Mandate müssen mit möglichst aktuellen Quellen bestätigt werden.

## Ausgabe

`person-professional-profile.json`:

```json
{
  "schemaVersion": 1,
  "person": {
    "name": "...",
    "disambiguation": "...",
    "identityConfidence": "high"
  },
  "researchedAt": "YYYY-MM-DD",
  "evidenceCurrentThrough": "YYYY-MM-DD",
  "timeline": [
    {
      "organization": "...",
      "role": "...",
      "from": "...",
      "to": "...",
      "scope": [],
      "claimRefs": [],
      "sourceRefs": [],
      "uncertainties": []
    }
  ],
  "capabilities": [
    {
      "id": "CAP1",
      "capability": "...",
      "claimRefs": [],
      "basis": "derived",
      "confidence": "medium",
      "limitations": []
    }
  ],
  "achievements": [],
  "publications": [],
  "patents": [],
  "boardAndAdvisoryRoles": [],
  "conflicts": [],
  "notFound": [],
  "openQuestions": [],
  "persistence": {
    "allowed": [
      "professionally relevant public facts",
      "source references",
      "evidence-linked capability synthesis"
    ],
    "runOnly": [
      "credentials",
      "private connector payloads",
      "unnecessary personal data",
      "sensitive attributes"
    ]
  }
}
```

`person-professional-profile.md` ist die lesbare Synthese.

`person-evidence-note.json` folgt dem Contract von `research-to-evidence-note` und enthält die für dieses Profil verwendeten Claims und Quellen.

`person-source-register.json` hält verwendete Quellen inklusive Klasse, Datum, Aktualität, Limitierungen und Claim-Verknüpfung.

## Optionaler Rollen-Kontext

Ein vorhandener `role-search-brief` darf genutzt werden, um die Recherchefrage einzugrenzen, zum Beispiel auf internationale Commercial-Verantwortung oder bestimmte Technologien.

Er darf jedoch nicht dazu führen, dass Gegen- oder Nicht-Fit-Evidenz gesucht, verstärkt oder ausgeblendet wird.

Das Personenprofil bleibt als professionelles Evidence Artifact unabhängig von der späteren Rollenbewertung wiederverwendbar.

## Batch Research

Bei mehreren Personen jede Person zunächst separat recherchieren und als separates Profil speichern.

Keine vergleichende Bewertung während der Evidence Collection.

Erst ein nachgelagerter Skill darf mehrere Profile gegen dieselben Rollenanforderungen stellen.

## Prüfungen

Vor Übergabe prüfen:

- Identität ist ausreichend disambiguiert,
- jeder relevante Fakt ist auf Claims und Quellen zurückführbar,
- Selbstaussagen sind als solche erkennbar,
- Capabilities besitzen Claim-Provenance,
- Unternehmensereignisse wurden nicht unbelegt der Person zugerechnet,
- `not-found` wurde nicht als `does-not-exist` formuliert,
- widersprüchliche Rollen- oder Datumsangaben bleiben sichtbar,
- Aktualität wurde für zeitabhängige Angaben geprüft,
- keine Rollenfit- oder Hiring-Entscheidung wurde erzeugt,
- keine sensiblen oder unnötigen privaten Informationen persistiert wurden.

## Fehlerbehandlung

### Sparse Evidence

Wenn nur wenige belastbare Quellen existieren, erzeuge ein partielles Profil mit niedriger beziehungsweise ungeklärter Confidence und konkreten Evidenzlücken. Keine fehlenden Karriereabschnitte ergänzen.

### Conflicting Sources

Wenn hochwertige Quellen widersprechen, Konflikt sichtbar halten. Nur auflösen, wenn eine stärkere, aktuellere oder eindeutig primäre Quelle den Widerspruch sachlich erklärt.

### Identity Ambiguity

Bei möglicher Namensverwechslung keine Quellen zusammenführen, bevor die Identität hinreichend geklärt ist.

### Sensitive Information Encountered

Irrelevante sensible/private Information nicht in Profile oder Source Register übernehmen. Ihre bloße öffentliche Auffindbarkeit begründet keine berufliche Relevanz.

## Übergaben

Geeignete nachgelagerte Verbraucher:

- `role-capability-evidence-map` für rollenbezogene Evidence-Zuordnung,
- `meeting-preparation` für belegten professionellen Teilnehmerkontext,
- `document-production` für freigegebene Profile oder Research Briefs,
- `knowledge-ingestion` für strukturierte professionelle Claims, sofern Speicherung zulässig ist.

## Qualitätsfälle

### Happy Path

Mehrere aktuelle Primärquellen dokumentieren Karriere, Verantwortungsbereiche, Patente und internationale Tätigkeiten konsistent. Ergebnis: Timeline, atomare Claims, mehrere nachvollziehbar abgeleitete Capabilities und wenige offene Punkte.

### Sparse Evidence

Es existieren nur ein veraltetes Speaker Bio und eine aktuelle Arbeitgeberseite. Ergebnis: begrenztes Profil, klare Aktualitätsgrenzen, keine erfundenen Zwischenstationen oder Scope-Angaben.

### Conflicting Sources

Zwei Quellen nennen unterschiedliche Startjahre einer Rolle. Ergebnis: beide Angaben bleiben mit Quellen sichtbar; die Timeline markiert den Zeitraum als konfliktbehaftet.

### Self-Reported Profile

Eine wichtige Leistungsangabe stammt ausschließlich aus LinkedIn. Ergebnis: Claim als berufliche Selbstaussage markieren und Confidence nicht ohne unabhängige Bestätigung künstlich erhöhen.

### Sensitive Information

Eine Quelle enthält private Gesundheits- oder Familieninformationen. Ergebnis: diese Information wird nicht in das professionelle Profil übernommen.

### Fehlerfall

Eine vorgeschlagene Recherche folgert aus einem CEO-Titel automatisch starke Führung, schreibt dem Kandidaten das gesamte Unternehmenswachstum zu und interpretiert fehlende P&L-Angaben als fehlende P&L-Erfahrung. Stoppe und korrigiere Fact/Inference-, Attribution- und Negative-Evidence-Grenzen.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn eine ausreichend disambiguierte Person als professionelle Timeline mit nachvollziehbaren Claims und Quellen vorliegt, abgeleitete Capabilities vollständig auf Claims zurückführbar sind, Unsicherheit, Konflikte und `not-found` sichtbar bleiben, Aktualität bewertet wurde, Datenschutzgrenzen eingehalten sind und ein nachgelagerter Skill das Profil ohne erneute Rohrecherche für eine rollenbezogene Evidence Map verwenden kann.
