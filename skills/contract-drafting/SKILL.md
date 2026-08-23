---
name: contract-drafting
description: Erzeugt aus bestätigten Requirements und einem geprüften Legal Context einen privaten oder beruflichen Vertragsentwurf, wahlweise auf Basis einer hochgeladenen Vorlage, und dokumentiert Platzhalter, Abweichungen, Rechtsannahmen und offene Punkte. Verwenden für neue Vertragsentwürfe oder template-basiertes Drafting, nicht für die primäre Bewertung eines fremden Vertrags.
userFacing: true
implicitInvocation: false
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - contract-legal-context
outputs:
  - contract-draft.md
  - contract-drafting-report.json
  - contract-open-points.md
lastEvaluated: 2026-08-23
---

# Contract Drafting

## Zweck und Grenze

Dieser Skill erzeugt einen nachvollziehbaren Vertragsentwurf aus bestätigten fachlichen Anforderungen und einem aktuellen Rechtsgrundlagen-Handoff. Er unterstützt sowohl freie Neuerstellung als auch **template-basiertes Drafting**.

Eine Vorlage wird nicht als automatisch rechtlich geeignet behandelt. Sie liefert Struktur, Hausstil, Nummerierung und Ausgangsklauseln; der Legal Context bestimmt, welche zwingenden oder sachlich notwendigen Anpassungen erforderlich sind.

## Voraussetzung

Vor Drafting müssen vorliegen:

- bestätigte Requirements oder ein ausreichend vollständiger `requirements-handoff`,
- Parteien/Rollen und Vertragsziel,
- wirtschaftliche Eckdaten,
- gewünschte Risikopositionen, soweit materiell,
- aktuelles `contract-legal-context.json`,
- bei `template-draft` die Vorlage einschließlich relevanter Anlagen.

Fehlende fachliche Entscheidungen → über `contract-workflow` zu `round-based-requirements-grilling`.

## Template Intake

Wenn eine Vorlage hochgeladen wurde:

1. Dokumentstruktur, Überschriften, Nummerierung und definierte Begriffe erfassen.
2. Platzhalter, Optionen, Kommentare und alternative Klauseln identifizieren.
3. Anlagen, Querverweise und Rangfolgen erfassen.
4. House Style und Sprachfassung beibehalten, soweit nicht ausdrücklich anders gewünscht.
5. Jede materielle Abweichung als `templateDeviation` protokollieren.
6. Widersprüchliche oder erkennbar unpassende Template-Klauseln nicht stillschweigend übernehmen.

Bei mehreren Templates nicht automatisch vermischen; zunächst Primary Template und ergänzende Klauselquellen bestimmen.

## Drafting-Reihenfolge

### 1. Deal Model

Baue vor Fließtext ein strukturiertes Vertragsmodell:

- Parteien und Rollen,
- Vertragsgegenstand,
- Leistungen / Deliverables / Abhängigkeiten,
- Vergütung / Preise / Steuern / Währung,
- Termine / Abnahme / Service Levels,
- Laufzeit / Verlängerung / Kündigung / Exit,
- Haftungs- und Gewährleistungsposition,
- IP / Vertraulichkeit / Daten,
- Compliance / Audit / Unterauftragnehmer,
- Rechtswahl / Forum / Form,
- Anlagen und Rangfolge.

### 2. Clause Coverage Gate

Bestimme, welche Klauselthemen für diesen konkreten Vertrag erforderlich, optional oder nicht einschlägig sind. Vermeide Boilerplate nur der Vollständigkeit halber.

### 3. Draft

Formuliere eindeutig, intern konsistent und operationalisierbar. Definierte Begriffe nur verwenden, wenn sie definiert sind; messbare Pflichten möglichst mit Verantwortlichem, Frist, Trigger und Rechtsfolge formulieren.

### 4. Risk Alignment

Prüfe jede materielle Risikoklausel gegen die bestätigte Nutzerposition. Erfinde keine aggressiven Haftungs-, Freistellungs-, Exklusivitäts- oder IP-Regelungen, wenn diese nicht aus Requirements, Template oder Legal Context ableitbar sind.

### 5. Placeholder Discipline

Unbekannte Fakten werden als sichtbare Platzhalter markiert, z. B. `[● Betrag]`, `[● Datum]`, `[● Gerichtsstand]`. Keine plausibel klingenden Firmendaten, Beträge, Registernummern, Fristen oder Ansprechpartner erfinden.

### 6. Cross-Clause Consistency Pass

Prüfe insbesondere:

- Definitionen und Querverweise,
- Leistung ↔ Abnahme ↔ Gewährleistung ↔ Remedies,
- Laufzeit ↔ Kündigung ↔ Exit ↔ Survival,
- Haftung ↔ Freistellung ↔ Versicherung,
- IP ↔ Vertraulichkeit ↔ Datennutzung,
- Preise ↔ Change Control ↔ Indexierung,
- Hauptvertrag ↔ Anlagen ↔ Rangfolge,
- Rechtswahl ↔ Gerichtsstand/Arbitration.

### 7. Legal/Form Final Gate

Verifiziere anhand des Legal Context:

- zwingende Klauseln bzw. unzulässige Abweichungen,
- Verbraucher-/AGB-Besonderheiten,
- Spezialrecht,
- erforderliche Form und Signatur,
- notwendige Anlagen, Belehrungen, Zustimmungen oder separate Verträge.

## Sprach- und Stilregel

Vertragssprache ist standardmäßig die Sprache der bestätigten Vorlage oder Nutzeranforderung. Juristische Präzision hat Vorrang vor unnötig komplizierter Sprache. Keine archaischen Formulierungen nur zur Erzeugung eines „juristischen Tons“.

Bei zweisprachigen Verträgen muss klar geregelt sein, welche Sprachfassung maßgeblich ist; Übersetzungen dürfen nicht stillschweigend als identisch behandelt werden.

## Ausgabe

`contract-draft.md` ist der vollständige Vertragsentwurf mit sichtbaren offenen Platzhaltern.

`contract-drafting-report.json` enthält mindestens:

- `schemaVersion`, `asOf`, `draftVersion`, `sourceTemplate`, `templateHash` soweit verfügbar,
- `legalContextVersion`, `requirementsVersion`,
- `templateDeviations`, `insertedClauses`, `removedClauses`,
- `materialAssumptions`, `openPoints`, `formRequirements`, `counselEscalations`.

`contract-open-points.md` enthält nur Punkte, die vor Freigabe beantwortet, verhandelt oder extern geprüft werden müssen.

Auf Wunsch kann der Entwurf in ein editierbares Dokumentformat überführt werden; die kanonische inhaltliche Version und der Abweichungsreport bleiben getrennt nachvollziehbar.

## Prüfungen

Pass nur wenn Requirements und Legal Context vorliegen; eine Nutzer-Vorlage strukturell respektiert und Abweichungen protokolliert werden; keine unbekannten Fakten erfunden werden; Klauselabdeckung fallbezogen statt boilerplate-getrieben erfolgt; Cross-Clause-Konsistenz geprüft wird; Form- und Spezialrechtsfragen sichtbar sind; alle offenen Platzhalter vor „final“ aufgelistet werden.

## Abschluss

Der Skill endet mit einem versionierten Vertragsentwurf, einem nachvollziehbaren Drafting-/Template-Delta und einer expliziten Open-Points-Liste für Verhandlung, Finalisierung oder qualifiziertes Legal Review.
