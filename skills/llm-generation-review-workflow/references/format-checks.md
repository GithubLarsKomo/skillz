# Format-specific checks for LLM generation review

## Gemeinsame Regeln

1. **Original und Rendering unterscheiden.** Ein PDF kann nur der Export eines DOCX/PPTX/XLSX sein. Wenn die Quelle vorliegt, Quelle und Rendering getrennt untersuchen.
2. **Inhalt und Dateistruktur trennen.** Gleichmäßige Formatierung, saubere Templates oder konsistente Formeln sind keine LLM-Beweise.
3. **Segmentbezogen prüfen.** Gemischte Dokumente können menschliche und generierte Teile enthalten. Keine globale Durchschnittsbewertung erzwingen.
4. **Provenienz vor Stil.** Direkte, überprüfbare Workflow-Spuren wiegen stärker als generische Stilmerkmale.
5. **Fehlende Daten als Limitation behandeln.** Keine Metadaten, keine Notes oder keine Versionshistorie bedeuten nicht, dass ein LLM ausgeschlossen ist.

## Text / Markdown

### Extraktion
- Originaltext unverändert sichern.
- Sprache und Genre bestimmen.
- Absätze bzw. semantische Abschnitte bilden.
- Sehr kurze Texte separat als `low-evidence-volume` kennzeichnen.

### Prüfen
- `llm-prose-pattern-audit` auf ausreichend lange Abschnitte anwenden.
- Auf direkte Assistenten-/Promptreste achten, etwa ausdrücklich eingefügte Promptanweisungen, System-/User-Rollen oder Aussagen über die eigene Modellrolle. Solche Reste sind stärker als generische Stilmerkmale, können aber kopiert oder zitiert worden sein.
- Quellen, URLs und Zitate verifizieren, wenn sie Teil der Begründung sind.
- Bei Übersetzungen oder starker Redaktion detectorartige Stilurteile deutlich abwerten.

## DOCX

### Zusätzlich extrahieren
- Body-Text und Tabellenzellen,
- Headers/Footers,
- Footnotes/Endnotes,
- Comments,
- Track Changes bzw. Insert/Delete-Revisions,
- dokumentierte Felder/Hyperlinks,
- Core/App/Custom Properties,
- Template-/Generatorinformationen.

### Typische Befunde
- **Stark nur bei Verifikation:** konkrete Kommentare, Prompt-/Copilot-Spuren oder revisionsbezogene Workflow-Evidenz, die sich Textpassagen zuordnen lässt.
- **Schwach:** generische Metadaten, Office-App-Version, saubere Styles, gleichartige Überschriften.
- **Kontext:** ungewöhnlich geringe Revisionstiefe kann bei einem „fertig eingefügten“ Text vorkommen, ist aber ebenso mit Copy/Paste, externem Editing oder Template-Import vereinbar.
- Markdown-Reste (`###`, `**`, Backticks, nicht konvertierte Tabellen-/Listenmarker) können Copy/Paste aus einem Chat-/Markdown-Workflow anzeigen, sind aber ohne weitere Evidenz höchstens unterstützend.

## PDF

### Zusätzlich prüfen
- Born-digital vs. Scan,
- Textlayer pro Seite,
- Creator/Producer/XMP,
- Creation/Modification dates,
- eingebettete Dateien,
- sichtbare Quellen und Fußnoten,
- Duplikate oder Inkonsistenzen im Textlayer.

### Priorität
- Bei verfügbarem Source-Office-Dokument dessen Struktur-/Revisionsspuren höher gewichten als PDF-Metadaten.
- PDF Creator/Producer zeigen meist den Renderer oder Konverter, nicht den Inhaltsautor.
- Ein gescannter PDF ohne Source-Datei hat typischerweise geringe Provenienzauflösung; dies als Limitation ausweisen.

## XLSX

### Inhalt in Ebenen teilen
1. **Datenwerte**
2. **Formeln/Berechnungslogik**
3. **Narrative Zellen** wie Beschreibungen, Kommentare, Anweisungen, Zusammenfassungen
4. **Struktur** wie Sheets, Tabellen, Named Ranges, Hidden Sheets, External Links
5. **Metadaten/Provenienz**

### Formeln
- Formelgleichförmigkeit nicht als LLM-Indikator verwenden.
- Prüfen auf:
  - inkonsistente Formeln innerhalb erwarteter Serien,
  - unerklärte Hardcodes zwischen Formeln,
  - Referenzfehler,
  - zirkuläre oder logisch unplausible Abhängigkeiten,
  - Formeln, die nicht zur beschriebenen Business-Logik passen,
  - erfundene oder nicht existente Funktionsnamen,
  - unplausible externe Referenzen.

Diese Fehler können mit automatischer/LLM-gestützter Erzeugung vereinbar sein, sind aber nicht LLM-spezifisch.

### Narrative Inhalte
- Nur narrative Zellen und Kommentare mit `llm-prose-pattern-audit` prüfen.
- Tabellenköpfe, IDs, kurze Labels und Formeln nicht als Prosa behandeln.
- Quellen-/URL-Angaben und natürlichsprachliche Erklärungen auf Konsistenz mit den Daten prüfen.

### Struktur
- Hidden Sheets, Defined Names, External Links, Comments und Calc Chain dokumentieren.
- `openpyxl`, Office oder andere Generatorbibliotheken als Tooling, nicht als LLM-Beweis einstufen.

## PPTX

### Segmentierung
Pro Slide getrennt erfassen:
- Titel,
- Body/Bullets,
- Tabellen-/Chart-Texte,
- Bildunterschriften/Quellen,
- Speaker Notes.

Zusätzlich global:
- Master/Layout-Nutzung,
- Medien-/Chart-Verteilung,
- Quellenkonsistenz,
- wiederkehrende rhetorische/visuelle Templates.

### Sprachprüfung
- `llm-prose-pattern-audit` auf Slide-Text nur mit Präsentationskontext anwenden: kurze Bullets sind keine Report-Prosa.
- Wiederholte Dreiergruppen, generische „Key Takeaways“, mechanische Problem–Solution–Future-Strukturen oder identische Satzmuster sind höchstens schwache Template-Indikatoren.
- Speaker Notes können stärker analysierbare Prosa liefern als die Slides selbst.

### Inhalt/Visuals
- Quellen für Zahlen, Charts und Zitate prüfen.
- Generische Platzhalter, widersprüchliche Zahlen zwischen Slides, erfundene Quellen oder unpassende Bild-/Chart-Beschriftungen als Content-Integrity-Befunde markieren.
- Ein konsistenter Master, regelmäßige Abstände oder gleichartige Slides sind normale professionelle Präsentationsmerkmale und keine LLM-Evidenz.

## Gemischte oder teilgenerierte Artefakte

Wenn unterschiedliche Abschnitte/Sheets/Slides stark unterschiedliche Evidenzprofile zeigen:
- lokale Befunde beibehalten,
- `mixed-generation-pattern` als Hypothese dokumentieren,
- keine Gesamtautorschaft aus dem stärksten Einzelabschnitt ableiten,
- möglichst Entwurfs-/Versionshistorie oder Quellenkontext nachfordern.

## Empfohlene Follow-ups bei unklarer Lage

- Quelldatei statt nur PDF beschaffen.
- Versionshistorie oder frühere Entwürfe prüfen.
- authentische, genrepassende Author-Voice-Referenzen ergänzen.
- behauptete Quellen und Berechnungen verifizieren.
- bei externem Detector dessen Kalibrierung/Version dokumentieren.
- bei Hochrisikofällen unabhängige menschliche Zweitprüfung durchführen.
