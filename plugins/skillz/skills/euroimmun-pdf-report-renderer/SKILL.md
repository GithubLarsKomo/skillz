---
name: euroimmun-pdf-report-renderer
description: Erzeugt aus dem kanonischen EUROIMMUN-DOCX-Report ein professionelles PDF mit identischem Styling und aktuellem EUROIMMUN-From-Revvity-Kopf. Verwendet den DOCX-Renderer als einzige Layoutquelle, konvertiert ohne inhaltliches Re-Authoring und erzwingt eine visuelle PDF-Endkontrolle.
---

# EUROIMMUN PDF Report Renderer

Erzeuge einen EUROIMMUN-PDF-Report **nicht mit einer zweiten unabhängigen Layout-Engine**, sondern aus dem vom `euroimmun-docx-report-renderer` erzeugten kanonischen DOCX. Damit bleiben Header, Footer, Typografie, Tabellen, Callouts und Seitenumbrüche zwischen editierbarer und finaler Ausgabe konsistent.

## Verbindlicher Corporate Design Contract

Für jedes EUROIMMUN-Firmen-PDF MUSS `docs/corporate/euroimmun/DESIGN.md` als normativer Design Contract angewendet werden.

- Ist `docs/corporate/euroimmun/DESIGN.md` nicht verfügbar, darf das PDF nicht als Corporate-final/verified ausgegeben werden.
- Das PDF erbt Designquelle, Template-Status, Brand-Profil, Klassifikation und Content-Revision des kanonischen DOCX; es eröffnet keine zweite Designentscheidung.
- Voraussetzung ist ein kanonisches DOCX mit `Corporate Design Gate: PASS`. Fehlt dieser Nachweis, zuerst den DOCX-Gate abschließen.
- Nach der Konvertierung ist zusätzlich die PDF-Parität gemäß Corporate Design Gate vollständig zu prüfen.
- Der finale Status `Corporate Design Gate: PASS|FAIL` MUSS für die PDF-Revision kommuniziert werden.

## Trigger

Nutze diesen Skill, wenn ein finalisierter Report als PDF im EUROIMMUN-Stil benötigt wird. Wenn noch kein kanonisches DOCX existiert, zuerst `euroimmun-docx-report-renderer` ausführen.

## Architekturregel

`Report-Spec -> EUROIMMUN DOCX Template -> DOCX -> PDF`

Der PDF-Skill darf den Inhalt nicht erneut aufbauen, zusammenfassen oder anders layouten. Er ist **Conversion + PDF-QA**, nicht ein zweiter Report-Autor.

## Ablauf

1. **Corporate Design Contract laden.** `docs/corporate/euroimmun/DESIGN.md` lesen und die Design-/QA-Provenance des kanonischen DOCX übernehmen.
2. **Kanonisches DOCX bestimmen.** Nur die finale DOCX-Ausgabe verwenden, für die `Corporate Design Gate: PASS` dokumentiert ist.
3. **DOCX-QA voraussetzen.** Wenn die DOCX-Version noch nicht vollständig visuell geprüft wurde oder seit dem PASS verändert wurde, zuerst deren QA erneut abschließen.
4. **Konvertieren.** `scripts/render_pdf.py INPUT.docx OUTPUT.pdf` verwenden. Die Referenzimplementierung nutzt LibreOffice/soffice headless.
5. **PDF vollständig rendern.** Das erzeugte PDF in PNG-Seiten/äquivalente Seitenbilder rendern; Stichproben genügen nicht.
6. **Alle Seiten visuell und auf Parität prüfen.** Kopf, Footer, Tabellen, Bilder, Callouts, Seitenumbrüche, Glyphen, Weißraum, Seitenzahl und Inhaltsreihenfolge mit der finalen DOCX-Ausgabe vergleichen.
7. **Bei Reflow- oder Konvertierungsfehlern nicht im PDF reparieren.** Ursache im DOCX/Template beheben, DOCX erneut rendern und den DOCX-Gate erneut bestehen; anschließend PDF neu konvertieren und vollständig neu prüfen.
8. **Corporate Design Gate für PDF abschließen.** Critical/Major Findings = 0, Render-Coverage `checked/total` und Source-Parität dokumentieren; `PASS` gilt nur für exakt die geprüfte PDF-Revision.
9. **Finale PDF ausgeben.** QA-Renderings bleiben intern, sofern nicht angefordert.

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
- Keine PDF-spezifische Reparatur, die die Layoutparität zum kanonischen DOCX aufhebt.

## Qualitätsprüfung

Vor Übergabe prüfen:

- PDF ist nicht leer und lässt sich vollständig rendern.
- Seitenzahl und Inhaltsreihenfolge entsprechen der kanonischen DOCX-Ausgabe.
- Keine abgeschnittenen Tabellen, Bilder oder Header/Footer.
- Keine zusätzlichen Leer- oder Verlustseiten durch Konvertierung.
- Keine defekten Glyphen oder Schrift-Substitutionen mit sichtbar verändertem Layout.
- Public-Reference-Reports zeigen den aktuellen EUROIMMUN-From-Revvity-Kopf; supplied Corporate Templates bleiben unverändert.
- Corporate Design Gate enthält vollständige Render-Coverage und Source-Parität.

## Fehlerbehandlung

- **Corporate `DESIGN.md` fehlt:** PDF nicht als Corporate-final ausgeben; Gate bleibt FAIL.
- **DOCX ohne Corporate Design Gate PASS:** zuerst DOCX-QA abschließen; keine ungeprüfte Quelle konvertieren und als final deklarieren.
- **LibreOffice/soffice fehlt:** klare Dependency-Fehlermeldung; keine Datei mit `.pdf`-Endung vortäuschen.
- **Conversion schlägt fehl:** Fehler ausgeben, keine leere PDF übernehmen.
- **PDF-Reflow weicht sichtbar ab:** zurück zum DOCX/Template; nicht per PDF-Stempelung kaschieren.
- **PDF-QA nicht möglich:** PDF nicht als final geprüft kennzeichnen; Gate bleibt FAIL.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn das kanonische DOCX bereits den Corporate Design Gate bestanden hat, erfolgreich konvertiert wurde, das PDF vollständig in Seitenbilder gerendert, **jede Seite auf Layoutparität und Defekte geprüft**, alle Critical/Major Findings geschlossen und `Corporate Design Gate: PASS` für die finale PDF-Revision dokumentiert wurde.
