---
name: contract-workflow
description: Orchestriert private und berufliche Vertragsarbeit von Requirements-Grilling und Rechtsgrundlagenprüfung über Dokumentbewertung oder Vertragserzeugung bis zu Verhandlung, Final-Check und anwaltlicher Eskalation. Verwenden, wenn ein Vertrag geprüft, erstellt, aus einer Vorlage erzeugt oder als Vertragsprozess strukturiert werden soll.
---

# Contract Workflow

## Zweck und Grenze

Dieser Skill ist der user-facing Einstiegspunkt für **private und berufliche Verträge**. Er koordiniert fachliche Klärung, aktuelle Rechtsgrundlagen, Dokumentprüfung oder Drafting und den nachgelagerten Abschlussprozess, ohne die juristische Fachlogik der Specialist Skills zu duplizieren.

Deutschland ist der Default-Kontext, **nicht automatisch das anwendbare Recht**. Internationale Parteien, Leistungsorte, Verbraucherbezug, Arbeitsverhältnisse, Immobilien, IP-/Lizenzthemen, Datenschutz, regulierte Branchen oder eine Rechtswahlklausel können andere oder zusätzliche Rechtsgrundlagen auslösen.

Der Skill ersetzt keine verbindliche anwaltliche Einzelfallberatung und darf insbesondere bei materiellen Haftungs-, Arbeits-, Gesellschafts-, Immobilien-, Finanzierungs-, IP-, Kartell-, Datenschutz- oder ausländischen Rechtsfragen keine nicht verifizierte Rechtssicherheit behaupten.

## Trigger

Typische Trigger:

- „Prüfe diesen Vertrag.“
- „Bewerte die Risiken in diesem NDA / Kaufvertrag / Dienstleistungsvertrag / Arbeitsvertrag.“
- „Erstelle mir einen Vertrag.“
- „Nutze diese Vertragsvorlage und passe sie an meinen Fall an.“
- „Welche Punkte muss ich vor Unterschrift noch klären?“
- „Erzeuge aus dem Grilling einen Vertragsentwurf.“

## Eingang

Mindestens eines der folgenden Elemente ist vorhanden oder wird durch Grilling erhoben:

- Vertragsziel und gewünschtes Ergebnis,
- Parteien und Rollen,
- privater oder beruflicher Kontext,
- vorhandener Vertrag / Vertragsset als Datei oder Text,
- Vorlage / Muster als Datei oder Text,
- bestehende Verhandlungspositionen,
- relevante Länder, Leistungsorte und Rechtswahl,
- materielle wirtschaftliche oder operative Anforderungen.

Originaldokumente werden nicht stillschweigend überschrieben. Bei mehreren Dateien wird zunächst ein `documentSet` mit Hauptvertrag, Anlagen, AGB, SOW, DPA, Preislisten und sonstigen referenzierten Dokumenten aufgebaut.

## Ablauf

### 1. Intent Gate

Bestimme `mode` als:

- `review` – vorhandenen Vertrag bewerten,
- `draft` – neuen Vertrag erzeugen,
- `template-draft` – vorhandene Vorlage parametrisieren und anpassen,
- `revise` – bereits bewerteten oder erzeugten Entwurf überarbeiten.

### 2. Requirement Sufficiency Gate

Prüfe, ob Ziel, Rollen, Muss-Punkte, wirtschaftliche Eckdaten, gewünschte Risikoposition, Laufzeit/Exit und wesentliche operative Randbedingungen ausreichend klar sind.

Fehlende **fachliche Entscheidungen** → `round-based-requirements-grilling`.

Vertragsspezifische Grilling-Themen umfassen mindestens: Zweck, Parteien/Rollen, Leistung/Gegenleistung, Termine, Abnahme, Vergütung, Laufzeit/Kündigung, Haftungsziel, Vertraulichkeit, IP/Nutzungsrechte, Daten, Unterauftragnehmer, Change Control, Versicherungen/Sicherheiten, Streitbeilegung, Rechtswahl/Gerichtsstand und gewünschte Verhandlungsposition. Nicht einschlägige Themen werden übersprungen.

### 3. Legal Context Gate

→ `contract-legal-context`

Kein Review und kein Drafting darf eine materielle Rechtsaussage nur aus einem vermuteten „deutschen Standardvertrag“ ableiten. Der Legal-Context-Handoff muss anwendbares bzw. potenziell anwendbares Recht, Vertragsart, Parteirollen, zwingende Normen, Formanforderungen, Spezialrecht, internationale Konfliktregeln und offene Rechtsfragen ausweisen.

### 4A. Review Path

Bei `review` → `contract-review`.

Danach werden Findings in drei Arbeitsklassen überführt:

- `must-fix` – rechtlich, wirtschaftlich oder operativ nicht akzeptabel bzw. wesentlich ungeklärt,
- `negotiate` – materielle, aber verhandelbare Risikoverteilung,
- `accept-or-monitor` – vertretbar, sofern die dokumentierten Annahmen stimmen.

### 4B. Drafting Path

Bei `draft` oder `template-draft` → `contract-drafting`.

Eine vom Nutzer gelieferte Vorlage hat strukturell Vorrang, sofern sie nicht gegen bestätigte Requirements, zwingendes Recht oder ausdrückliche Nutzerentscheidungen verstößt. Abweichungen von der Vorlage werden transparent protokolliert.

### 5. Negotiation / Revision Loop

Für jede materielle Klausel werden Zielposition, akzeptabler Fallback, rote Linie und Begründung festgehalten, soweit diese Informationen vorliegen. Gegenangebote oder Redlines werden als Delta zum letzten Stand bewertet; bereits geklärte Punkte werden nicht erneut geöffnet, sofern neue Informationen sie nicht verändern.

### 6. Final Contract Gate

Vor Freigabe prüfen:

- Parteien, Vertretungsmacht und Bezeichnungen,
- Definitionen, Querverweise, Anlagen und Rangfolge,
- Leistung, Preise, Steuern und Zahlungsmechanik,
- Laufzeit, Verlängerung, Kündigung und Exit,
- Haftung, Freistellung, Gewährleistung und Versicherungen,
- IP, Vertraulichkeit, Datenschutz und Unterauftragnehmer,
- Rechtswahl, Gerichtsstand/Schiedsverfahren,
- Form- und Unterschriftserfordernisse,
- offene Platzhalter und widersprüchliche Klauseln,
- erforderliche Zustimmungen, Anlagen oder externe Reviews.

### 7. Escalation Gate

`qualified-counsel-review-required` ist auszugeben, wenn eine verlässliche Bewertung ohne qualifizierte Rechtsberatung nicht vertretbar ist. Typische Auslöser:

- ungeklärtes oder fremdes anwendbares Recht,
- hohe oder atypische Haftung / Freistellung,
- Kündigung oder Gestaltung von Arbeitsverhältnissen,
- Gesellschafts-, M&A-, Beteiligungs- oder Finanzierungsverträge,
- Grundstücks-/Immobiliengeschäfte oder notarielle Form,
- wesentliche IP-Lizenzen, Exklusivität oder Kartellrisiken,
- regulatorisch kritische Qualitäts-/Compliance-Verträge,
- komplexe Datenschutz- oder internationale Datentransfers,
- erhebliche wirtschaftliche Bedeutung bei unsicherer Rechtsprechung.

## Outputs

`contract-case.json` enthält mindestens:

- `schemaVersion`, `caseId`, `mode`, `asOf`, `parties`, `documentSet`,
- `requirementsStatus`, `legalContextStatus`, `workProductStatus`,
- `materialIssues`, `openQuestions`, `escalations`, `versionHistory`.

`contract-plan.md` fasst Vorgehen, aktuellen Stand, nächste Verhandlungsschritte und Freigabestatus zusammen.

`contract-handoff.json` ist der kompakte Übergabestand für eine spätere Revision oder anwaltliche Prüfung und enthält Dokumentversionen/Hashes, Legal-Context-Version, Entscheidungen, offene Punkte und Risikoflags.

## Prüfungen

Pass nur wenn:

- fehlende fachliche Entscheidungen zu Grilling geroutet werden,
- Rechtsgrundlagen vor Review/Drafting geprüft werden,
- hochgeladene Originale unverändert bleiben,
- Review und Drafting nicht vermischt werden,
- Versionen und offene Punkte nachvollziehbar bleiben,
- ausländisches oder Spezialrecht nicht aus deutschem Allgemeinwissen erfunden wird,
- ein Final-Gate vor „unterschriftsreif“ erfolgt,
- notwendige anwaltliche Eskalation sichtbar bleibt.

## Abschluss

Der Skill ist abgeschlossen, wenn der Vertragsfall entweder mit nachvollziehbarer Bewertung bzw. Entwurf, dokumentierten Entscheidungen und Final-Status bereitsteht oder mit konkret begründeter Eskalation an qualifizierte Rechtsberatung übergeben wurde.
