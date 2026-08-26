---
name: presentation-language-rewriter
description: Überarbeitet deutsche und englische Präsentationstexte elementbezogen für Slide-Titel, Key Messages, Bullets, Chart-Labels, Tabellen, Annotationen und Speaker Notes. Verwenden, wenn Präsentationssprache prägnant, idiomatisch, management-, wissenschafts- oder fachgerecht verbessert werden soll; nicht als Ersatz für Report- oder Memo-Redaktion.
---

# Presentation Language Rewriter

Dieser Skill optimiert Text für das Medium Präsentation. Er behandelt Präsentationssprache ausdrücklich nicht wie Report-Prosa.

## Prioritäten

1. Semantic fidelity.
2. Epistemic precision.
3. Aussageklarheit der Slide.
4. Präsentationsgerechte Kürze und Scanbarkeit.
5. Zielgruppen- und Sprachpassung.
6. Stilistische Eleganz.

Keine niedrigere Priorität darf Claims, Zahlen, Quellen, Negationen, Bedingungen, Modalität oder geschützte Terminologie verändern.

## Parameter

- `language`: `de|en`
- `englishVariant`: `international|us|uk`, falls Englisch.
- `presentationStyle`: `executive|scientific|technical|sales|educational`
- `audience`: `expert|management|mixed|public`
- `elementType`: `slide-title|subtitle|key-message|bullet|annotation|chart-label|table-text|speaker-note`
- optional: Fidelity Lock, Terminologieliste, Author-Voice-Profil.

## Elementregeln

### Slide title

- Aussage statt bloßer Themenbezeichnung bevorzugen.
- Idealerweise eine vollständige, sofort verständliche Botschaft.
- In der Regel etwa 10-12 Wörter oder kürzer, sofern die Aussage nicht leidet.

### Key message

- Eine Konsequenz oder Entscheidung pro Aussage.
- In der Regel etwa 20 Wörter oder kürzer.
- Keine Wiederholung des Titels in anderen Worten.

### Bullet

- Ein Gedanke pro Bullet.
- Parallelität innerhalb einer Liste herstellen.
- Fließtextartige Mehrsatz-Bullets vermeiden.
- Kürzen, bevor Schrift verkleinert wird.

### Chart/Table text

- Labels so kurz wie fachlich eindeutig möglich.
- Einheiten, Zeiträume und Bezugsgrößen explizit halten.
- Fachterminologie nicht aus Stilgründen variieren.

### Speaker notes

- Dürfen vollständiger und narrativer sein als sichtbarer Slide-Text.
- Sichtbaren Slide-Text nicht unnötig duplizieren.

## Deutsch

- Prägnante, idiomatische Fachsprache statt Nominalstil und Berichtssätzen.
- Aussagekräftige Verben bevorzugen.
- Artikel und Funktionswörter nur streichen, wenn Natürlichkeit und Eindeutigkeit erhalten bleiben.
- Management-Slides dürfen zugespitzt sein, aber keine Evidenzstufe erhöhen.

## Englisch

- Natürliches Präsentationsenglisch statt übersetztem deutschem Nominalstil.
- International English als Default, sofern kein Adressatenstandard anderes verlangt.
- Executive Slides: klare action-oriented Aussagen.
- Scientific Slides: vorsichtige Evidenzsprache erhalten; keine Suggestion von Kausalität aus Assoziation.
- Unnötige Füllphrasen wie `it should be noted that` oder `in order to` verdichten.

## Textbudget als QA-Signal

Wortgrenzen sind keine Hard Stops. Überschreitungen lösen zuerst eine Redaktionsprüfung aus. Reihenfolge der Korrektur:

1. Redundanz entfernen.
2. Satzstruktur verdichten.
3. Inhalt auf mehrere Slides verteilen, falls mehrere Botschaften vorliegen.
4. Erst danach Layoutanpassung erwägen.
5. Schriftverkleinerung ist die letzte Option und muss template-konform bleiben.

## Fidelity-Verifikation

Jede materielle Überarbeitung wird anschließend mit `rewrite-fidelity-verifier` gegen Quelle und Fidelity Lock geprüft. Bei Hard Fail wird die Änderung zurückgenommen oder fachlich autorisiert.

## Abschluss

Abgeschlossen, wenn der sichtbare Text präsentationsgerecht, sprachspezifisch und elementgerecht formuliert ist, die gewünschte Zielgruppe trifft und der Fidelity-Verifier keine ungeklärten Hard Fails meldet.
