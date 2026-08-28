---
name: document-layout-qa
description: Prüft editierbare DOCX-Dokumente strukturell gegen ein dokumentiertes Template-Profil auf Seiten-/Section-Setup, Style-Drift, Tabellenbreiten, Bild-/Caption-Verankerung, Listen/Nummerierung, Header/Footer, Felder, Seitenumbrüche und typische Overflow-/Reflow-Risiken. Verwenden vor finalem Render; nicht als Ersatz für die visuelle PDF-Prüfung.
---

# Document Layout QA

## Zweck und Grenze

`document-layout-qa` ist das strukturelle QA-Gate für editierbare Word-Dokumente. Es bewertet OOXML-/Dokumentstruktur und template-spezifische Regeln, bevor ein tatsächlicher visueller Render geprüft wird.

## Trigger

Nach DOCX-Erzeugung oder größerer Dokumentänderung verwenden, wenn Template-Fidelity, Seitenlogik, Tabellen, Styles oder kontrollierte Header-/Footer-Strukturen überprüft werden müssen.

## Voraussetzungen

- zu prüfendes DOCX;
- `document-template-profile.json`, sofern Template-/Referenztreue verlangt ist;
- optional bekannte Inhalts- oder Layoutwarnungen aus dem Renderer.

## Ablauf

1. Section-Anzahl, Page Setup, Orientierung, Ränder, Spalten und Abschnittswechsel gegen das Profil prüfen.
2. Named Styles, direkte Formatierungs-Ausreißer, Fontfamilien/-größen und Absatzabstände prüfen.
3. Header/Footer, Logo-/Feldbeziehungen, Seitenzahlen und section-spezifische Varianten prüfen.
4. Listen/Nummerierung auf beschädigte Definitionen, unerwartete Neustarts oder manuell nachgebaute Nummern prüfen.
5. Tabellen auf Satzbreite, Zell-/Zeilenstruktur, Header-Wiederholung und Split-Risiken prüfen.
6. Bilder, Captions, Textfluss, Anchoring und Seiten-/Abschnittsgrenzen prüfen.
7. kontrollierte Template-Regionen auf unbeabsichtigte Überschreibung prüfen.
8. Findings mit Objekt-/Section-/Paragraph-Referenz und Schweregrad ausgeben.

## Schweregrade

- `critical`: Inhalt/Template-Struktur objektiv beschädigt, abgeschnitten oder kontrollierte Region überschrieben.
- `major`: klare Template-Abweichung, hohes Reflow-/Lesbarkeitsrisiko oder fehlerhafte Seitenlogik.
- `review`: auffälliger Ausreißer, dessen visuelle Wirkung im Render geprüft werden muss.
- `info`: dokumentierte, akzeptierte Abweichung.

## Prüfungen

- Keine universellen Seiten-/Font-Grenzwerte anwenden, wenn das aktive Template andere valide Baselines definiert.
- Eine große Tabelle nicht durch unlesbare Schrift „reparieren“; zuerst Struktur, Umbruch oder logische Teilung prüfen.
- Direkte Formatierung nur dann als Fehler behandeln, wenn sie die Template-Regeln oder Wartbarkeit verletzt.
- Ein struktureller PASS darf nicht als visueller PASS ausgegeben werden.
- Fachliche Inhalte und Zahlen werden bei Layoutkorrekturen nicht verändert.

## Fehlerbehandlung

- **Kein Template-Profil trotz Fidelity-Anforderung:** QA auf generische strukturelle Defekte begrenzen und Fidelity als `not-assessed` markieren.
- **Beschädigtes DOCX/OOXML:** `fail`; nicht durch Neuaufbau stillschweigend ersetzen.
- **Unklare Style-Intention:** als `review` markieren statt pauschal umformatieren.
- **Möglicher Overflow ohne Renderbeweis:** strukturelles Risiko melden; finale Sichtbarkeit dem Render-Verifier überlassen.

## Übergabe

`document-layout-qa.json` enthält Findings, geprüfte Baselines, Coverage und Status. `document-layout-qa.md` ist die menschlich lesbare Projektion für Korrekturen und Review.

## Abschlusskriterien

Abgeschlossen, wenn alle strukturell prüfbaren Sections, Styles, Tabellen, Listen, Bilder, Header/Footer und kontrollierten Regionen bewertet sind und kein ungeklärtes Critical/Major Finding verbleibt oder die verbleibende Abweichung explizit als Blocker an die nächste Stufe übergeben wurde.
