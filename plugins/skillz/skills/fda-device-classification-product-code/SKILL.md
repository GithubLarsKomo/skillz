---
name: fda-device-classification-product-code
description: Ermittelt FDA-Geräteklasse, Regulation Number, Product Code und Premarket-Kontext evidenzgebunden aus aktuellen offiziellen Quellen, ohne eine FDA-Entscheidung zu simulieren.
---

# FDA Device Classification and Product Code

## Zweck und Grenze

Dieser Skill erzeugt eine evidenzgebundene US-FDA-Klassifikations- und Product-Code-Bewertung für ein Medical Device oder IVD. Er verbindet Product Context, aktuelle FDA Product Classification Database, einschlägige 21-CFR-Klassifikationsregeln und offizielle FDA-Quellen zu einer nachvollziehbaren Hypothese über Device Class, Regulation Number, Product Code, Review Panel und Premarket-Kontext.

Er entscheidet **nicht** selbst über 510(k), De Novo oder PMA als vollständige Strategie, wählt keinen Predicate und simuliert keine formale FDA-Klassifikationsentscheidung. Wenn die öffentliche Evidenz keine belastbare Zuordnung erlaubt, bleibt die Bewertung `provisional|blocked` und wird an den FDA-Regulatory-Front-Door bzw. eine formale FDA-Interaktion weitergegeben.

## Kernprinzipien

- **Product Context zuerst:** Intended Use, Indications for Use, Technologie, Analyte/Specimen soweit relevant, Benutzer, Setting und wesentliche Funktionen werden vor der Datenbanksuche fixiert.
- **Aktuelle FDA-Daten statt Erinnerung:** Product Codes, Regulation Numbers, Class und Submission Type werden gegen aktuelle FDA-Datenbanken/Regulations geprüft.
- **Product Code ist Klassifikationsanker, keine Marketingfreigabe:** Ein ähnlicher Code allein beweist weder richtige Zuordnung noch Clearance.
- **Mehrere Codes bleiben sichtbar:** Primary- und potenzielle Secondary-Codes werden getrennt bewertet; die endgültige FDA-Zuordnung wird nicht vorweggenommen.
- **Unclassified / not-classified / unclear sind echte Zustände:** fehlende klare Regulation oder neuartige Technologie wird nicht in den nächstbesten bestehenden Code gezwungen.
- **Guidance-Status beachten:** Final, Draft/Not-for-Implementation, Regulation, Database Entry und informatives FDA-Webmaterial werden als unterschiedliche Authority Types gekennzeichnet.

## Workflow

### 1. US-relevanten Product Context fixieren

Dokumentiere mindestens Intended Use, Indications for Use, Patient-/User-Population, Technologie/Prinzip, zentrale Features, IVD-Target/Specimen soweit relevant und bekannte US-Vergleichsprodukte.

### 2. Klassifikationsquellen durchsuchen

Suche aktuelle FDA Product Classification Database sowie relevante 21-CFR-Teile und offizielle FDA-Guidance. Erfasse pro Kandidat Product Code, Device Name, Regulation Number, Class, Review Panel, Submission Type/Exemption-Kontext, Datenbankstatus und `asOf`.

### 3. Kandidaten auf Product Context abbilden

Bewerte Übereinstimmung in Intended Use/Indications, Technologie, Device Type und regulatorischer Definition. Ähnliche Handelsnamen oder einzelne technische Merkmale reichen nicht.

### 4. Primary-/Secondary-Code-Hypothese bilden

Ordne Kandidaten als `primary-candidate|secondary-candidate|unlikely|insufficient-evidence`. Begründe die Primary-Hypothese über regulatorische Definition, Class und stärkste Product-Context-Passung; konkurrierende Codes bleiben sichtbar.

### 5. Premarket-Kontext ableiten

Dokumentiere, welche Premarket-Konsequenz die offizielle Klassifikationsinformation nahelegt, einschließlich Exemption-/510(k)-/PMA-/unclassified-Kontext soweit evidenziert. Eine vollständige Pathway-Strategie bleibt Eigentum von `fda-medical-device-ivd-regulatory-specialist` bzw. nachgelagerten Fach-Skills.

### 6. Unsicherheit eskalieren

Bei neuartiger Technologie, widersprüchlichen Codes, unklarem Device Type, möglicher Combination-Product-Frage oder fehlender belastbarer Klassifikation wird kein definitive Resultat erzwungen. Dokumentiere die offene FDA-Frage und übergib an Regulatory Strategy/Decision Record bzw. formale FDA-Feedbackwege.

## Output-Verträge

`fda-device-classification.json` enthält mindestens `asOf`, Product Context Reference, Assessment State, Device Class Hypothesis, Regulation Number, Primary Product Code Candidate, Secondary Candidates, Review Panel, Premarket Context, Uncertainties, Authority Boundary und Source References.

`fda-product-code-evidence.json` enthält pro Code Kandidatenquelle, Definition, Regulation, Class, Submission-Type-Metadaten, Applicability-Faktoren, Konflikte, Freshness und Evidence Links.

## Downstream

Primäre Consumer sind `fda-medical-device-ivd-regulatory-specialist`, `fda-510k-predicate-strategy`, `fda-de-novo-strategy`, CLIA-/QMSR- und spätere Submission-Skills. Formale FDA-Entscheidungen werden als externe Evidenz zurückgeführt, nicht vom Skill erfunden.

## Memory Path

Persistenzwürdig sind bestätigte produktspezifische US-Klassifikations-Constraints, robuste Such-/Disambiguierungsheuristiken und validierte Hinweise darauf, welche Product-Context-Merkmale die Code-Auswahl unterscheiden. Aktuelle Datenbankeinträge, momentane Submission-Type-Flags, ungeklärte Code-Hypothesen und vorläufige FDA-Pathway-Schlüsse bleiben run-only. Regulatory Candidates benötigen `sourceRefs`, `asOf` und für veränderliche Datenbank-/Guidance-Fakten `reviewAfter`. Übergib nur geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- Product Context vor der Code-Auswahl fixiert wurde,
- aktuelle offizielle FDA-Quellen verwendet werden,
- Regulation, Class, Product Code und Premarket-Kontext getrennt dokumentiert sind,
- konkurrierende oder unklare Zuordnungen sichtbar bleiben,
- Product Code nicht mit Clearance oder FDA-Bestätigung gleichgesetzt wird,
- Draft Guidance nicht als verbindliche Final Guidance behandelt wird,
- volatile Klassifikationsdaten nicht als zeitlose Memory-Fakten gespeichert werden.
