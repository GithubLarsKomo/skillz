---
name: euroimmun-pdf-report-renderer
description: Erzeugt aus dem kanonischen EUROIMMUN-DOCX-Report ein professionelles PDF mit identischem Styling und aktuellem EUROIMMUN-From-Revvity-Kopf. Verwendet den DOCX-Renderer als einzige Layoutquelle, konvertiert ohne inhaltliches Re-Authoring und erzwingt eine visuelle PDF-Endkontrolle.
---

# EUROIMMUN PDF Report Renderer

Erzeuge einen EUROIMMUN-PDF-Report **nicht mit einer zweiten unabhängigen Layout-Engine**, sondern aus dem vom `euroimmun-docx-report-renderer` erzeugten kanonischen DOCX. Damit bleiben Header, Footer, Typografie, Tabellen, Callouts und Seitenumbrüche zwischen editierbarer und finaler Ausgabe konsistent.

## Trigger

Nutze diesen Skill, wenn ein finalisierter Report als PDF im EUROIMMUN-Stil benötigt wird. Wenn noch kein kanonisches DOCX existiert, zuerst `euroimmun-docx-report-renderer` ausführen.

## Architekturregel

`Report-Spec -> EUROIMMUN DOCX Template -> DOCX -> PDF`

Der PDF-Skill darf den Inhalt nicht erneut aufbauen, zusammenfassen oder anders layouten. Er ist **Conversion + PDF-QA**, nicht ein zweiter Report-Autor.

## Ablauf

1. **Kanonisches DOCX bestimmen.** Nur die final geprüfte DOCX-Ausgabe verwenden.
2. **DOCX-QA voraussetzen.** Wenn die DOCX-Version noch nicht visuell geprüft wurde, zuerst deren QA abschließen.
3. **Konvertieren.** `scripts/render_pdf.py INPUT.docx OUTPUT.pdf` verwenden. Die Referenzimplementierung nutzt LibreOffice/soffice headless.
4. **PDF rendern.** Das erzeugte PDF in PNG-Seiten rendern.
5. **Alle Seiten visuell prüfen.** Kopf, Footer, Tabellen, Bilder, Callouts, Seitenumbrüche, Glyphen und Weißraum mit der finalen DOCX-Ausgabe vergleichen.
6. **Bei Reflow- oder Konvertierungsfehlern nicht im PDF reparieren.** Ursache im DOCX/Template beheben, DOCX erneut rendern und anschließend PDF neu konvertieren.
7. **Finale PDF ausgeben.** QA-Renderings bleiben intern, sofern nicht angefordert.

Beispiel:

```bash
python scripts/render_pdf.py /tmp/euroimmun-report.docx /tmp/euroimmun-report.pdf
```

## Invarianten

- Der PDF-Skill ändert keine fachlichen Aussagen.
- Keine separate PDF-spezifische Corporate-Design-Implementierung.
- Das PDF muss denselben Template-Status wie das DOCX behalten: Public-Reference oder supplied/approved Corporate Template.
- Keine Behauptung einer Corporate-Freigabe allein aufgrund erfolgreicher Konvertierung.
- Keine Fontdateien paketieren oder weitergeben.

## Qualitätsprüfung

Vor Übergabe prüfen:

- PDF ist nicht leer und lässt sich rendern.
- Seitenzahl und Inhaltsreihenfolge entsprechen der kanonischen DOCX-Ausgabe.
- Keine abgeschnittenen Tabellen, Bilder oder Header/Footer.
- Keine zusätzlichen Leer- oder Verlustseiten durch Konvertierung.
- Keine defekten Glyphen oder Schrift-Substitutionen mit sichtbar verändertem Layout.
- Public-Reference-Reports zeigen den aktuellen EUROIMMUN-From-Revvity-Kopf; supplied Corporate Templates bleiben unverändert.

## Fehlerbehandlung

- **LibreOffice/soffice fehlt:** klare Dependency-Fehlermeldung; keine Datei mit `.pdf`-Endung vortäuschen.
- **Conversion schlägt fehl:** Fehler ausgeben, keine leere PDF übernehmen.
- **PDF-Reflow weicht sichtbar ab:** zurück zum DOCX/Template; nicht per PDF-Stempelung kaschieren.
- **PDF-QA nicht möglich:** PDF nicht als final geprüft kennzeichnen.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn das kanonische geprüfte DOCX erfolgreich konvertiert wurde, das PDF vollständig in Seitenbilder gerendert und **jede Seite visuell auf Layoutparität und Defekte geprüft** wurde.
