---
name: person-profile-report
description: Erzeugt aus einem strukturierten, quellengebundenen Person Research Dossier einen lesbaren Personenreport mit Biographie, Karriere, wissenschaftlichen Arbeiten, Publikationen, IP, Arbeitgebern und optional öffentlich gemachten Interessen. Verwenden, wenn aus belastbarer Personenrecherche eine kohärente, zitierfähige Gesamtbiographie oder Executive-/Scientific-Profile-Fassung entstehen soll.
---

# Person Profile Report

## Zweck

Verdichte ein abgeschlossenes `person-research-dossier` zu einem klaren, quellengebundenen Bericht über eine konkrete Person. Der Report soll fachliche Entwicklung und Karriere verständlich machen, ohne unbelegte Eigenschaften, private Profilierung oder rollenbezogene Eignung zu erfinden.

## Trigger

Verwenden, wenn nach abgeschlossener Personenrecherche ein Report, eine Biographie, ein Executive Profile, Scientific Profile oder chronologischer Karrierebericht benötigt wird.

Nicht als Ersatz für `candidate-role-fit-assessment` verwenden. Der Report beschreibt die Person; er bewertet nicht automatisch deren Fit für eine Stelle.

## Eingangs-Gates

Erforderlich sind mindestens:

- ausreichend disambiguierte Zielperson,
- nachvollziehbare Quellenreferenzen,
- Timeline,
- Evidenzklassen für zentrale Claims,
- explizite offene Punkte und Konflikte.

Wenn diese Basis fehlt, zurück zu `person-research-dossier`.

## Report-Struktur

Passe die Tiefe an den Auftrag an, verwende aber grundsätzlich:

1. **Executive Summary** – 5–10 Sätze zu fachlichem Kern, Karriereentwicklung und wichtigsten belegten Stationen.
2. **Biographischer und akademischer Hintergrund** – Ausbildung, Dissertation, Forschungsgruppen und frühe fachliche Prägung.
3. **Wissenschaftliche Arbeiten** – nach Forschungsphasen statt bloß chronologisch; Forschungsfragen, Methoden, Hauptbefunde und wissenschaftliche Bedeutung erklären.
4. **Veröffentlichungen** – wichtigste Arbeiten oder Themencluster; keine lange Bibliographie ohne Einordnung.
5. **IP und Patente** – technische Erfindungsschwerpunkte, Patentfamilien, Assignees und Zusammenhang mit Karriere-/Forschungsphasen.
6. **Arbeitgeber und Karriere** – chronologische Stationen, belegter Scope und erkennbare Funktionswechsel.
7. **Fachliche Entwicklung** – Synthese der belegten Entwicklung, z. B. Grundlagenforschung → Translation → Produkt/Business → Führung; als `supported-inference` markieren, wenn nicht direkt belegt.
8. **Öffentliche Aktivitäten** – Vorträge, Boards, Verbände oder Interviews, soweit relevant.
9. **Hobbies und Sport** – nur wenn belastbar öffentlich und für den gewünschten Biographiekontext sinnvoll; separat und knapp.
10. **Offene Punkte und Unsicherheiten** – relevante Lücken, widersprüchliche Daten oder unklare Zuordnungen.

## Wissenschaftliche Zusammenfassung

Für PhD-/Postdoc-/Forschungsphasen nicht lediglich Titel nennen. Erkläre pro Phase:

- zentrale wissenschaftliche Frage,
- biologisches/technisches System,
- wichtigste Methoden,
- zentrale Erkenntnisse,
- Bedeutung im damaligen Forschungsfeld,
- erkennbare Brücke zur nächsten Karriere- oder Forschungsphase.

Einzelpublikationen werden nur hervorgehoben, wenn sie eine Phase, Methode, Erfindung oder Translation besonders gut repräsentieren.

## Karriere-Synthese

Trenne strikt:

- **belegt:** Titel, Arbeitgeber, Zeitraum, offiziell beschriebene Verantwortung,
- **supported inference:** nachvollziehbare Interpretation eines Karriereübergangs,
- **unknown:** tatsächlicher Scope, Teamgröße, Budget oder Verantwortungsniveau, wenn nicht belegt.

Nicht aus Titeln allein auf Organisationsgröße, Entscheidungsrechte oder Führungstiefe schließen.

## IP-Darstellung

Patente nach Familien bzw. technischen Themen gruppieren. Erfinderstellung bedeutet nicht automatisch alleinige Erfindung, Produktverantwortung oder kommerziellen Erfolg. Bei komplexen Patentfamilien genügt eine repräsentative Publikationsnummer plus Hinweis auf die Familie.

## Stil

Der Report soll:

- analytisch und sachlich sein,
- Quellenbezug für wesentliche Aussagen sichtbar halten,
- wissenschaftliche Inhalte allgemeinverständlich, aber fachlich korrekt erklären,
- keine PR-Sprache übernehmen,
- Unsicherheit offen formulieren,
- Wiederholungen zwischen Biographie, Timeline und Karriere-Synthese vermeiden.

## Datenschutz und Grenzen

Keine sensiblen oder sachfremden privaten Merkmale aufnehmen. Hobbies und Sport nur aus freiwillig öffentlich gemachten Quellen und nie als Leistungs-, Persönlichkeits- oder Eignungsproxy verwenden. Keine private Adresse, Familienrecherche, Gesundheit, Religion, politische Orientierung oder andere geschützte Merkmale aufnehmen oder inferieren.

## Ausgabe

`person-profile-report.md` enthält mindestens:

- Titel und Standdatum,
- Executive Summary,
- Ausbildung und wissenschaftliche Prägung,
- Forschungsphasen,
- ausgewählte Publikationen/Themencluster,
- IP/Patente,
- Arbeitgeber- und Karriereverlauf,
- Synthese der fachlichen Entwicklung,
- optional öffentliche Aktivitäten und Interessen,
- offene Punkte/Limitierungen,
- Quellenreferenzen.

Je nach Auftrag sind Kurzfassung, Scientific Profile, Executive Profile oder ausführlicher Deep-Dive zulässig, solange dieselbe Evidenzbasis erhalten bleibt.

## Prüfungen

Vor Abschluss prüfen:

- keine zentrale Aussage überschreitet ihre Evidenzklasse,
- wissenschaftliche Arbeiten sind inhaltlich erklärt,
- Timeline und Report widersprechen sich nicht,
- Publikationen/IP sind der richtigen Person zugeordnet,
- Karriere-Synthesen sind als Inferenz erkennbar,
- private/sensitive Inhalte fehlen,
- öffentliche Hobbies/Sport sind separat und optional,
- Limitierungen sind sichtbar.

## Übergaben

Der fertige Report kann an `meeting-preparation`, `candidate-role-fit-assessment`, `document-production` oder andere dokumentierende Workflows übergeben werden. Rollenbezogene Auswahlentscheidungen müssen weiterhin auf einer freigegebenen Role Architecture und Scorecard beruhen.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn die Recherchebasis zu einem kohärenten, quellengebundenen und evidenztreuen Personenprofil verdichtet ist, wissenschaftliche und berufliche Entwicklung verständlich erklärt werden und Unsicherheiten sowie Datenschutzgrenzen sichtbar bleiben.
