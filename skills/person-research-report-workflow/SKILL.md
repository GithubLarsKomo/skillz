---
name: person-research-report-workflow
description: Orchestriert eine vollständige evidenzbasierte Personenrecherche von Identitätsklärung über Biographie, Ausbildung, Veröffentlichungen, IP, Arbeitgeber und Karriere bis zum sprachlich optimierten, quellengebundenen Personenreport mit optionaler DOCX- und PDF-Ausgabe. Verwenden, wenn der Nutzer eine Person umfassend recherchiert und das Ergebnis als Biographie, Scientific Profile, Executive Profile oder Deep-Dive-Report erhalten möchte.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - person-research-dossier
  - person-profile-report
  - precision-writing-revision
  - person-profile-document-delivery
outputs:
  - person-research-evidence.json
  - person-timeline.json
  - person-publications.json
  - person-ip-map.json
  - person-research-dossier.md
  - person-profile-report.md
  - person-profile-report.docx
  - person-profile-report.pdf
lastEvaluated: 2026-08-25
---

# Person Research Report Workflow

## Ziel

Führe eine vollständige, quellengebundene Personenrecherche durch und überführe sie anschließend in einen kohärenten, sprachlich geprüften Report. Wenn der Nutzer ein Dokumentartefakt benötigt, erzeuge aus genau dieser finalisierten Textfassung zusätzlich DOCX und/oder PDF.

Der Workflow trennt vier Aufgaben:

1. **Recherche und Evidenznormalisierung** mit `person-research-dossier`.
2. **Narrative, evidenztreue Reportgenerierung** mit `person-profile-report`.
3. **Sprachliche Verbesserung mit Fidelity Lock** über `precision-writing-revision`.
4. **Dokumentausgabe und visuelle QA** über `person-profile-document-delivery`.

Der Workflow ist für öffentliche und vom Nutzer bereitgestellte berufliche/wissenschaftliche Informationen gedacht. Er ist kein Werkzeug zur invasiven Privatprofilierung.

## Trigger

Verwenden bei Aufträgen wie:

- „Recherchiere Person X und erstelle einen vollständigen Report.“
- „Gib mir Biographie, Lebenslauf, Publikationen, Patente, Arbeitgeber und Karriere von X.“
- „Erstelle ein Scientific/Executive Profile zu X.“
- „Analysiere den wissenschaftlichen und beruflichen Werdegang von X.“
- „Erstelle daraus einen professionellen DOCX- und PDF-Report.“

Wenn nur eine eng abgegrenzte Frage beantwortet werden soll, reicht gegebenenfalls `research-to-evidence-note`. Wenn die Person anschließend gegen eine Stelle bewertet werden soll, nach diesem Workflow `candidate-role-fit-assessment` verwenden.

## Standardablauf

### Phase 1 – Scope und Identität

Fixiere Zielperson, Rechercheauftrag, Standdatum, gewünschte Berichtstiefe, Zielsprache sowie gewünschte Ausgabeformate. Disambiguiere die Person vor jeder breiten Zuordnung von Publikationen oder Patenten.

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

### Phase 7 – Sprachliche Verbesserung

Rufe `precision-writing-revision` auf, standardmäßig im Modus `editorial`, sofern der Nutzer keinen anderen Modus vorgibt.

Vor dem Rewrite wird ein Fidelity Lock aus dem Evidence Dossier und dem Rohreport gebildet. Geschützt sind insbesondere:

- Fakten und Zeitangaben,
- Zahlen und Funktionsbezeichnungen,
- Publikations- und Patentzuordnungen,
- Quellenreferenzen,
- Evidenzklassen und Confidence,
- Negationen, Einschränkungen und offene Fragen.

Sprachliche Verbesserung darf Struktur, Klarheit, Präzision, Lesefluss und Wiederholungen optimieren, aber keine Unsicherheit entfernen, keine neue Eignungsaussage erzeugen und keine Quelle stärker darstellen als die Evidenz erlaubt. Nur eine Fassung mit bestandenem Fidelity-Check wird als `person-profile-report.md` finalisiert.

### Phase 8 – DOCX- und PDF-Generierung

Wenn DOCX und/oder PDF gewünscht sind, rufe `person-profile-document-delivery` mit dem sprachlich finalisierten Report auf.

- DOCX ist die kanonische editierbare Dokumentfassung.
- PDF wird aus derselben finalen Inhalts- und Layoutquelle erzeugt; kein unabhängiges Re-Authoring.
- Bei EUROIMMUN-Kontext vorhandene EUROIMMUN-DOCX/PDF-Renderer verwenden.
- Bei anderem Kontext ein bereitgestelltes Template oder einen neutralen professionellen Reportstil verwenden.
- Beide Formate müssen Quellen, Tabellen, Überschriftenhierarchie und Evidenzhinweise identisch transportieren.
- DOCX und PDF vor Übergabe visuell auf Seitenumbrüche, Tabellen, Links, Glyphen, Header/Footer und Quellenblöcke prüfen.

### Phase 9 – Übergabe

Falls der Nutzer eine konkrete Entscheidung treffen möchte, übergib den Report und die strukturierten Evidenzartefakte an den passenden Downstream-Skill, z. B.:

- `candidate-role-fit-assessment`,
- `meeting-preparation`,
- `research-to-evidence-note` für offene Spezialfragen.

Für Downstream-Entscheidungen bleibt das Evidence Dossier normativ; die sprachlich verbesserte Fassung und DOCX/PDF sind Darstellungsartefakte und dürfen Evidenzklassen nicht verändern.

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
7. Rohreport überschreitet keine Evidenzklasse.
8. Sprachliche Revision hat Fidelity-Check bestanden.
9. Sensible/private Profilierung ausgeschlossen.
10. Optionaler Hobbies-/Sport-Block ist separat und evidenzgebunden.
11. DOCX/PDF stammen aus der finalen geprüften Reportfassung und wurden visuell geprüft, sofern diese Formate angefordert wurden.

## Fehlerbehandlung

Bei unzureichender Disambiguierung keine vollständige Publikations- oder IP-Liste als sicher ausgeben. Bei fehlenden Primärquellen einen partiellen Report mit klaren Limitierungen erzeugen. Bei widersprüchlicher Evidenz Konflikte sichtbar halten. Bei einem Fidelity-Hard-Fail keine sprachlich überarbeitete Fassung oder Dokumentartefakte als final ausgeben. Wenn DOCX/PDF-Rendering oder visuelle QA scheitert, den geprüften Markdown-Report liefern und das fehlende Format ausdrücklich als nicht erzeugt bzw. nicht final geprüft kennzeichnen. Wenn die gewünschte Fragestellung in eine Eignungsbewertung übergeht, an `candidate-role-fit-assessment` übergeben.

## Abschlusskriterien

Abgeschlossen ist der Workflow, wenn die Recherche zu einer nachvollziehbaren Evidenzbasis normalisiert wurde, Biographie, wissenschaftliche Arbeiten, Veröffentlichungen, IP, Arbeitgeber und Karriere konsistent zusammengeführt sind, der Report sprachlich verbessert und fidelity-geprüft ist, optionale öffentliche Interessen sauber getrennt bleiben und die angeforderten DOCX/PDF-Ausgaben aus derselben finalen Inhaltsbasis erzeugt und visuell geprüft wurden.