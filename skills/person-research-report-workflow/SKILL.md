---
name: person-research-report-workflow
description: Orchestriert eine vollständige evidenzbasierte Personenrecherche von Identitätsklärung über Biographie, Ausbildung, Veröffentlichungen, IP, Arbeitgeber und Karriere bis zum quellengebundenen Personenreport. Verwenden, wenn der Nutzer eine Person umfassend recherchiert und das Ergebnis als Biographie, Scientific Profile, Executive Profile oder Deep-Dive-Report erhalten möchte.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - person-research-dossier
  - person-profile-report
outputs:
  - person-research-evidence.json
  - person-timeline.json
  - person-publications.json
  - person-ip-map.json
  - person-research-dossier.md
  - person-profile-report.md
lastEvaluated: 2026-08-25
---

# Person Research Report Workflow

## Ziel

Führe eine vollständige, quellengebundene Personenrecherche durch und überführe sie anschließend in einen kohärenten Report. Der Workflow verbindet zwei klar getrennte Aufgaben:

1. **Recherche und Evidenznormalisierung** mit `person-research-dossier`.
2. **Narrative, evidenztreue Reportgenerierung** mit `person-profile-report`.

Der Workflow ist für öffentliche und vom Nutzer bereitgestellte berufliche/wissenschaftliche Informationen gedacht. Er ist kein Werkzeug zur invasiven Privatprofilierung.

## Trigger

Verwenden bei Aufträgen wie:

- „Recherchiere Person X und erstelle einen vollständigen Report.“
- „Gib mir Biographie, Lebenslauf, Publikationen, Patente, Arbeitgeber und Karriere von X.“
- „Erstelle ein Scientific/Executive Profile zu X.“
- „Analysiere den wissenschaftlichen und beruflichen Werdegang von X.“

Wenn nur eine eng abgegrenzte Frage beantwortet werden soll, reicht gegebenenfalls `research-to-evidence-note`. Wenn die Person anschließend gegen eine Stelle bewertet werden soll, nach diesem Workflow `candidate-role-fit-assessment` verwenden.

## Standardablauf

### Phase 1 – Scope und Identität

Fixiere Zielperson, Rechercheauftrag, Standdatum und gewünschte Berichtstiefe. Disambiguiere die Person vor jeder breiten Zuordnung von Publikationen oder Patenten.

### Phase 2 – Quellenrecherche

Recherchiere systematisch in den Feldern:

- Biographie und akademische Ausbildung,
- Dissertation/PhD und postdoktorale bzw. frühe Forschungsphasen,
- wissenschaftliche Veröffentlichungen,
- IP/Patente,
- Arbeitgeber und Funktionen,
- Karriereentwicklung,
- fachliche öffentliche Aktivitäten,
- optional freiwillig öffentlich gemachte Hobbies und Sport.

Primärquellen und Originaldokumente priorisieren. Quellenqualität und Aktualität pro Claim bewerten.

### Phase 3 – Evidence Dossier

Rufe `person-research-dossier` auf. Erzeuge mindestens:

- `person-research-evidence.json`,
- `person-timeline.json`,
- `person-publications.json`,
- `person-ip-map.json`,
- `person-research-dossier.md`.

Keine Report-Synthese beginnen, solange zentrale Identitätskonflikte offen sind, die Publikations-, Patent- oder Arbeitgeberzuordnungen wesentlich verändern könnten.

### Phase 4 – Vertiefung wissenschaftlicher Arbeiten

Wenn PhD, Postdoc oder andere Forschungsphasen relevant sind, rekonstruiere die Arbeiten inhaltlich:

- Forschungsfrage,
- biologisches oder technisches System,
- Methoden,
- Hauptbefunde,
- wissenschaftliche Bedeutung,
- Anschluss an spätere Forschung, Translation, Produktentwicklung oder Karriere.

Nur belegte institutionelle Rollen als PhD/Postdoc titulieren. Bei Unsicherheit neutralere Bezeichnungen verwenden.

### Phase 5 – Karriere- und IP-Synthese

Verbinde Timeline, Publikationen, Patente und Arbeitgeber zu nachvollziehbaren Karrierephasen. Unterscheide direkte Evidenz von Interpretation. Patentfamilien werden konsolidiert; Erfinderstellung wird nicht mit alleiniger Produkt- oder Geschäftsverantwortung gleichgesetzt.

### Phase 6 – Reportgenerierung

Rufe `person-profile-report` auf. Wähle passend zum Nutzerziel eine der Fassungen:

- `brief`: kompakter Executive Snapshot,
- `standard`: vollständiges Personenprofil,
- `scientific`: Schwerpunkt PhD/Postdoc, Publikationen, Methoden und IP,
- `executive`: Schwerpunkt Karriere, Arbeitgeber, Scope und Führung,
- `deep-dive`: ausführliche Kombination aller belastbaren Bereiche.

Die Fassung verändert nicht die Evidenzbasis.

### Phase 7 – Übergabe

Falls der Nutzer eine konkrete Entscheidung treffen möchte, übergib den Report und die strukturierten Evidenzartefakte an den passenden Downstream-Skill, z. B.:

- `candidate-role-fit-assessment`,
- `meeting-preparation`,
- `research-to-evidence-note` für offene Spezialfragen.

## Evidenzregeln

Für zentrale Aussagen immer verwenden:

- `verified`,
- `supported-inference`,
- `unknown`,
- `contradicted`.

Kein `unknown` in negative Evidenz umdeuten. Keine zeitliche Lücke mit erfundenen Stationen schließen. Keine Rollenverantwortung aus dem Titel allein ableiten.

## Datenschutz und Recherchegrenzen

Nicht aktiv recherchieren oder inferieren:

- Gesundheit,
- Religion oder Weltanschauung,
- politische Einstellung oder Parteizugehörigkeit,
- sexuelle Orientierung oder Sexualleben,
- Familienplanung,
- private Anschriften oder private Kontaktdaten,
- nicht öffentlich gemachte Familien-/Beziehungsinformationen,
- andere geschützte oder sachfremde private Merkmale.

Hobbies und Sport dürfen nur aufgenommen werden, wenn sie freiwillig öffentlich dokumentiert, nicht sensibel und für den biographischen Kontext sinnvoll sind. Sie bleiben getrennt von beruflicher Eignung, Persönlichkeit und Leistungsbewertung.

## Qualitätsgates

Vor Abschluss müssen gelten:

1. Zielperson ausreichend disambiguiert.
2. Zentrale Karriere- und Ausbildungsstationen mit Quellen belegt oder als unbekannt markiert.
3. Publikationen und Patente mit Identitätsconfidence zugeordnet.
4. Wissenschaftliche Arbeiten inhaltlich zusammengefasst.
5. Patentfamilien konsolidiert.
6. Widersprüche und Zeitlücken sichtbar.
7. Report überschreitet keine Evidenzklasse.
8. Sensible/private Profilierung ausgeschlossen.
9. Optionaler Hobbies-/Sport-Block ist separat und evidenzgebunden.

## Fehlerbehandlung

Bei unzureichender Disambiguierung keine vollständige Publikations- oder IP-Liste als sicher ausgeben. Bei fehlenden Primärquellen einen partiellen Report mit klaren Limitierungen erzeugen. Bei widersprüchlicher Evidenz Konflikte sichtbar halten. Wenn die gewünschte Fragestellung in eine Eignungsbewertung übergeht, nicht improvisieren, sondern an `candidate-role-fit-assessment` übergeben.

## Abschlusskriterien

Abgeschlossen ist der Workflow, wenn die Recherche zu einer nachvollziehbaren Evidenzbasis normalisiert wurde, Biographie, wissenschaftliche Arbeiten, Veröffentlichungen, IP, Arbeitgeber und Karriere konsistent zusammengeführt sind, optionale öffentliche Interessen sauber getrennt bleiben und ein quellengebundener Report mit expliziten Unsicherheiten vorliegt.