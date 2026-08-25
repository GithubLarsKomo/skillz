---
name: person-research-dossier
description: Recherchiert eine konkrete Person aus belastbaren öffentlichen und bereitgestellten Quellen und strukturiert Biographie, Lebenslauf, Veröffentlichungen, IP, Arbeitgeber, Karriere sowie freiwillig öffentlich gemachte Hobbies und Sport in ein quellengebundenes Dossier. Verwenden, wenn eine Person systematisch verstanden werden soll, bevor ein Profilbericht, Meeting-Briefing oder rollenbezogenes Assessment entsteht.
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
  - person-research-evidence.json
  - person-timeline.json
  - person-publications.json
  - person-ip-map.json
  - person-research-dossier.md
lastEvaluated: 2026-08-25
---

# Person Research Dossier

## Zweck

Erzeuge eine nachvollziehbare, quellengebundene Recherchebasis zu einer namentlich bestimmten Person. Der Skill beantwortet nicht primär, ob die Person für eine Rolle geeignet ist, sondern: **Was ist über Ausbildung, wissenschaftliche Arbeit, beruflichen Werdegang, Veröffentlichungen, IP, Arbeitgeber und öffentlich dokumentierte Aktivitäten belastbar belegt?**

Die Ausgabe ist ein Research-Dossier und keine psychologische, politische, medizinische oder private Profilierung.

## Trigger

Verwenden bei Anfragen wie:

- „Recherchiere Person X vollständig.“
- „Erstelle mir Biographie und Karriereverlauf von X.“
- „Welche wissenschaftlichen Arbeiten, Patente und Arbeitgeber hatte X?“
- „Baue eine belastbare Personenrecherche als Basis für einen Report oder ein Interview.“

Für die anschließende rollenbezogene Eignungsbewertung `candidate-role-fit-assessment` verwenden. Für die lesbare Gesamtdarstellung `person-profile-report` verwenden.

## Recherchefelder

Untersuche soweit relevant und öffentlich belegbar:

1. **Identität und Disambiguierung** – Namensvarianten, eindeutige Zuordnung von Publikationen, Patenten und Beschäftigungen.
2. **Biographische Eckdaten** – nur beruflich bzw. wissenschaftlich relevante, öffentlich belegte Angaben.
3. **Ausbildung** – Hochschulen, Abschlüsse, Dissertation, Forschungsgruppen, erkennbare fachliche Schwerpunkte.
4. **Wissenschaftliche Arbeiten** – PhD, Postdoc/frühe Forschungsphase, spätere Forschung, Themen, Methoden, Co-Autoren, Institutionen und erkennbare Entwicklung des Forschungsprofils.
5. **Publikationen** – peer-reviewed Publikationen, Reviews, Bücher/Beiträge soweit relevant; Titel, Jahr, Rolle, Themencluster, Primärquelle.
6. **IP** – Patente/Patentanmeldungen, Erfinderrolle, Assignee, Patentfamilien soweit auflösbar, technische Kernaussage und Zusammenhang mit der Karriere.
7. **Arbeitgeber und Funktionen** – Organisation, Einheit, Rolle, Zeitraum, belegter Scope und Übergänge.
8. **Karriere** – chronologische Entwicklung, Funktionswechsel, Verantwortungszuwachs und Übergang zwischen Forschung, Entwicklung, Business, Führung oder anderen Domänen.
9. **Hobbies und Sport** – ausschließlich freiwillig öffentlich gemachte, nicht-sensitive Angaben aus belastbaren Quellen; nur als separater Kontextblock, niemals als Eignungsproxy.
10. **Öffentliche fachliche Aktivitäten** – Vorträge, Beiräte, Verbände, Konferenzen, Interviews oder öffentlich dokumentierte fachliche Nebenrollen.

## Quellenpriorität

Bevorzuge in dieser Reihenfolge, abhängig von der konkreten Aussage:

- Primärpublikationen, Dissertationen, Hochschularchive, PubMed/Crossref/DOI-Verlagsseiten,
- Patentämter und Patentdokumente,
- offizielle Arbeitgeber-/Unternehmensseiten und SEC/Behördenunterlagen,
- institutionelle Biographien und Konferenzprofile,
- hochwertige Sekundärquellen zur Einordnung,
- Profile/soziale Netzwerke nur ergänzend und niemals als alleinige Basis für entscheidende Claims.

Eine Arbeitgeber-Biographie kann eine Funktion bestätigen, beweist aber nicht automatisch deren tatsächlichen Scope. Ein Autorenname beweist keine Personenidentität ohne ausreichende Disambiguierung.

## Evidenzklassen

Jede zentrale Aussage erhält genau eine Klasse:

- `verified`: unmittelbar durch belastbare Quelle belegt,
- `supported-inference`: aus mehreren belegten Fakten plausibel abgeleitet,
- `unknown`: nicht ausreichend belegt,
- `contradicted`: belastbare Quellen widersprechen der Aussage.

Fehlende Online-Evidenz ist **kein Gegenbeleg**.

## Ablauf

### 1. Person disambiguieren

Fixiere die Zielperson mit mindestens zwei unabhängigen Ankern, z. B. Arbeitgeber + Fachgebiet, Institution + Publikation oder Arbeitgeber + Ausbildung. Dokumentiere Namensvarianten und mögliche Namenskonflikte.

### 2. Zeitachse zuerst aufbauen

Sammle belastbare Stationen chronologisch. Trenne exakte Daten von ungefähren Zeiträumen. Überlappungen bleiben sichtbar, bis sie aufgelöst sind.

### 3. Forschungs- und Publikationsprofil rekonstruieren

Ordne Publikationen nicht nur als Liste, sondern in Phasen und Themencluster. Extrahiere für relevante Arbeiten:

- Forschungsfrage,
- System/Material,
- zentrale Methoden,
- Hauptbefund,
- wissenschaftliche Bedeutung,
- mögliche Translation oder Anschlussarbeit.

Bei PhD/Postdoc-Rekonstruktion Institution, Arbeitsgruppe und Zeitpunkt berücksichtigen. Den Status „Postdoc“ nur behaupten, wenn er belegt ist; sonst „postdoktorale/frühe Forschungsphase“ oder äquivalent verwenden.

### 4. IP analysieren

Disambiguiere Erfindername, Assignee und Zeitraum. Gruppiere Familien statt dieselbe Erfindung mehrfach als unabhängige Leistung zu zählen. Beschreibe den technischen Kern sachlich und trenne Erfinderstellung von Produktverantwortung oder kommerziellem Erfolg.

### 5. Arbeitgeber und Karriere verbinden

Verknüpfe jede Station mit belegten Rollen- und Technologieinformationen. Unterscheide:

- Titel,
- belegte Verantwortlichkeit,
- plausible Funktion,
- unbekannten tatsächlichen Scope.

Leite Karrierephasen erst nach Sammlung der Stationen ab, z. B. Forschung → Translation → Business Development → General Management.

### 6. Öffentliche Interessen optional ergänzen

Hobbies und Sport nur aufnehmen, wenn die Person dies selbst oder eine belastbare öffentliche Quelle freiwillig dokumentiert hat. Keine Suche nach Wohnort, Familie, Gesundheit, Religion, politischer Orientierung, Sexualität oder anderen sensiblen bzw. sachfremden Privatmerkmalen.

### 7. Widersprüche und Lücken dokumentieren

Bei abweichenden Jahreszahlen, Titeln, Ausbildungseinträgen oder Publikationszuordnungen nicht stillschweigend harmonisieren. Den Konflikt mit Quellen, möglicher Erklärung und verbleibender Unsicherheit festhalten.

## Ausgaben

### `person-research-evidence.json`

Enthält mindestens:

- `schemaVersion`,
- `person`,
- `asOf`,
- `identityAnchors`,
- `nameVariants`,
- `claims`,
- `sources`,
- `education`,
- `employment`,
- `researchPhases`,
- `publicActivities`,
- `publicInterests`,
- `conflicts`,
- `openQuestions`,
- `limitations`.

### `person-timeline.json`

Chronologische Events mit `start`, `end`, `eventType`, `organization`, `role`, `evidenceClass`, `sourceRefs` und `notes`.

### `person-publications.json`

Relevante Publikationen mit DOI/PMID soweit vorhanden, Jahr, Autorenrolle, Institution, Themencluster, Methoden, Kernbefund, Quellenreferenz und Identitätsconfidence.

### `person-ip-map.json`

Patentfamilien mit Publikationsnummern, Prioritätsdatum, Assignee, Erfinderstatus, technischer Kernaussage, zugehöriger Karrierephase und Quellenreferenzen.

### `person-research-dossier.md`

Lesbare Research-Fassung mit Kurzprofil, Zeitachse, Ausbildung, wissenschaftlichen Phasen, Publikationsclustern, IP, Arbeitgeber/Karriere, öffentlichen fachlichen Aktivitäten, optionalen öffentlichen Interessen sowie Widersprüchen und offenen Punkten.

## Datenschutz und Fairness

Nicht aktiv recherchieren, ableiten oder persistieren:

- Gesundheitsdaten,
- Religion/Weltanschauung,
- politische Einstellung oder Parteizugehörigkeit,
- sexuelle Orientierung oder Sexualleben,
- Familienplanung,
- private Anschriften oder Kontaktdaten,
- nicht öffentlich gemachte Familien- oder Beziehungsinformationen,
- andere geschützte oder für den legitimen Recherchekontext sachfremde Merkmale.

Alter, Name, Foto, Herkunft, Hobbies oder Sport dürfen nicht als Leistungs- oder Eignungsproxy verwendet werden. Private Informationen aus Datenlecks, People-Search-Diensten oder ähnlich invasiven Quellen sind ausgeschlossen.

## Prüfungen

Vor Abschluss prüfen:

- Zielperson ist ausreichend disambiguiert.
- Jede zentrale Aussage besitzt Quellenreferenz und Evidenzklasse.
- Publikationen und Patente sind tatsächlich der Zielperson zugeordnet.
- Patentfamilien werden nicht als mehrere unabhängige Erfindungen gezählt.
- Forschung wird inhaltlich zusammengefasst statt nur bibliographisch aufgelistet.
- Titel und tatsächlicher Scope werden nicht gleichgesetzt.
- `unknown` wird nicht als negative Evidenz behandelt.
- private/sensitive Merkmale sind ausgeschlossen.
- Hobbies/Sport sind optional, öffentlich und klar vom professionellen Profil getrennt.

## Fehlerbehandlung

Bei Namenskonflikten oder unsicherer Publikations-/Patentzuordnung die Identitätsconfidence senken und die Zuordnung nicht als `verified` ausgeben. Bei fehlender Primärquelle kann eine starke Sekundärquelle den Punkt stützen, aber nicht automatisch dieselbe Confidence erzeugen. Wenn zentrale Zeitabschnitte unbekannt bleiben, explizit als Lücke dokumentieren.

## Übergaben

Geeignete Verbraucher:

- `person-profile-report` für den integrierten Personenreport,
- `candidate-role-fit-assessment` für rollenbezogene Eignungsbewertung,
- `meeting-preparation` für Gesprächsvorbereitung,
- `research-to-evidence-note` für eng abgegrenzte Vertiefungsfragen.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Identität und Karrierezeitachse ausreichend disambiguiert, relevante Forschung/Publikationen/IP quellengebunden strukturiert, Arbeitgeber- und Rollenstationen nachvollziehbar, Widersprüche und Lücken sichtbar und optionale private Kontextangaben auf freiwillig öffentlich gemachte, nicht-sensitive Informationen begrenzt sind.