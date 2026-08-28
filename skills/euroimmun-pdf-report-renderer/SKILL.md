---
name: euroimmun-pdf-report-renderer
description: Erzeugt aus dem kanonischen EUROIMMUN-DOCX-Report ein professionelles PDF mit identischem Styling. Erbt den DOCX-Level-1/Level-2-Template-Status, konvertiert ohne Re-Authoring und erzwingt vollständige Render- und Source-Paritätsprüfung.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - euroimmun-docx-report-renderer
consumes:
  - euroimmun-report.docx
outputs:
  - euroimmun-report.pdf
lastEvaluated: 2026-08-28
---

# EUROIMMUN PDF Report Renderer

Erzeuge einen EUROIMMUN-PDF-Report **nicht mit einer zweiten unabhängigen Layout-Engine**, sondern ausschließlich aus dem vom `euroimmun-docx-report-renderer` erzeugten kanonischen DOCX. Das PDF ist Distribution Representation derselben kontrollierten Layoutquelle.

## Verbindlicher Corporate Design Contract

Für jedes EUROIMMUN-Firmen-PDF MUSS `docs/corporate/euroimmun/DESIGN.md` angewendet werden. Zusätzlich gelten `docs/corporate/euroimmun/ACTIVE_REPORT_REFERENCE.md` und `docs/corporate/euroimmun/GOLDEN_REFERENCE.md`.

- Ist `DESIGN.md` nicht verfügbar, darf das PDF nicht als Corporate-final/verified ausgegeben werden.
- Das PDF erbt Template-Identität, SHA-Provenienz, Template-Status, Golden-Reference-Level, Brand-/Theme-Verhalten, Klassifikation und Content-Revision des kanonischen DOCX.
- Das PDF eröffnet **keine zweite Designentscheidung** und darf kein höheres Golden-Reference-Level erhalten als sein DOCX-Source.
- Voraussetzung ist ein kanonisches DOCX mit `Corporate Design Gate: PASS`.
- `template-derived` bzw. Report-Level-2-PASS für PDF ist nur zulässig, wenn das DOCX selbst Report-Level-2-PASS erreicht hat und die PDF-Parität vollständig bestanden wurde.

## Aktueller Referenzstatus

Solange `ACTIVE_REPORT_REFERENCE.md` keine verifizierte reale Corporate-DOCX-Binärreferenz enthält, gilt:

- DOCX-Level-2 = `NOT_RUN`;
- PDF-Level-2 = `NOT_RUN`;
- Public-Reference-DOCX/PDF darf Level 1 und `Corporate Design Gate: PASS` erreichen, bleibt aber `template-compatible / public-reference-fallback`.

Ein PDF-Export kann fehlende DOCX-Level-2-Evidenz niemals nachträglich erzeugen.

## Architekturregel

`Report-Spec -> verified DOCX template/source -> canonical DOCX -> PDF -> full parity QA`

Der PDF-Skill darf Inhalt und Layout nicht erneut authoren, zusammenfassen, stempeln oder reparieren.

## Ablauf

1. **Design-/Referenzprovenienz laden.** `DESIGN.md`, `ACTIVE_REPORT_REFERENCE.md` und Golden-Reference-Status des finalen DOCX übernehmen.
2. **Kanonisches DOCX bestimmen.** Nur die finale DOCX-Revision mit `Corporate Design Gate: PASS` verwenden.
3. **DOCX-Level übernehmen.** `public-reference-fallback / Level 1` oder `template-derived / Level 2` unverändert übernehmen. Keine Hochstufung im PDF-Schritt.
4. **Source Lock dokumentieren.** SHA-256 der finalen DOCX-Revision festhalten; bei Level 2 zusätzlich SHA-Identität der zugrunde liegenden Corporate-DOCX-Binärquelle referenzieren.
5. **Konvertieren.** `scripts/render_pdf.py INPUT.docx OUTPUT.pdf` verwenden; Referenzimplementierung via LibreOffice/soffice headless.
6. **PDF vollständig rendern.** Jede Seite in PNG/äquivalente Seitenbilder rendern; Stichproben genügen nicht.
7. **Alle Seiten auf DOCX/PDF-Parität prüfen.** Seitenzahl, Inhaltsreihenfolge, Sections, Header/Footer, Logos, Tabellen, Bilder, Callouts, Felder, Seitenzahlen, Glyphen, Weißraum und Umbrüche vergleichen.
8. **Bei Level 2 kontrollierte Regionen vergleichen.** Header/Footer/Logo/Field-/Page-Setup-Verhalten muss mit der finalen DOCX-Quelle und deren Template-Profil übereinstimmen. Der PDF-Export darf keine kontrollierten Regionen verlieren oder materiell verändern.
9. **Fehler ausschließlich an der DOCX-/Template-Quelle beheben.** Danach DOCX-Gate erneut ausführen und PDF komplett neu erzeugen/rendern.
10. **PDF-Gate abschließen.** Critical/Major = 0, vollständige Render-Coverage und Source-Parität dokumentieren.
11. **Finale PDF ausgeben.** QA-Renderings können intern bleiben.

## PDF-Level-2-Akzeptanz

PDF kann `LEVEL_2_PASS` nur erreichen, wenn alle Bedingungen erfüllt sind:

- Source DOCX hat Report-Level-2 = `LEVEL_2_PASS`;
- finale DOCX-SHA-256 ist dokumentiert;
- zugrunde liegende Corporate-DOCX/DOTX-Binärquelle und deren SHA-256 sind dokumentiert;
- PDF wurde aus exakt dieser finalen DOCX-Revision erzeugt;
- jede PDF-Seite gerendert und geprüft;
- Seitenzahl und Inhaltsreihenfolge stimmen überein;
- kontrollierte Header/Footer/Logo/Field/Page-Setup-Regionen bleiben erhalten;
- keine PDF-spezifische Reparatur oder Rekonstruktion;
- unresolved Critical = 0;
- unresolved Major = 0;
- DOCX/PDF source parity = `PASS`;
- `Corporate Design Gate: PASS`.

Fehlt eine Bedingung, ist PDF-Level-2 `FAIL` oder `NOT_RUN`.

## Invarianten

- Der PDF-Skill ändert keine fachlichen Aussagen.
- Keine separate PDF-spezifische Corporate-Design-Implementierung.
- Kein höherer Template-/Golden-Reference-Status als das Source-DOCX.
- Keine Behauptung einer Corporate-Freigabe allein aufgrund erfolgreicher Konvertierung.
- Keine Fontdateien paketieren oder weitergeben.
- Keine PDF-spezifische Reparatur, die Layoutparität aufhebt.

## Qualitätsprüfung

Vor Übergabe prüfen:

- PDF ist nicht leer und vollständig renderbar.
- Seitenzahl und Inhaltsreihenfolge entsprechen dem kanonischen DOCX.
- Keine abgeschnittenen Tabellen, Bilder, Header/Footer oder kontrollierten Felder.
- Keine zusätzlichen Leer- oder Verlustseiten.
- Keine defekten Glyphen oder sichtbare Font-Reflow-Fehler.
- Public-Reference-Ausgaben bleiben korrekt als Fallback gekennzeichnet.
- Level-2-Ausgaben enthalten vollständige Source-/Template-SHA-Provenienz und Paritätsnachweis.

## Fehlerbehandlung

- **`DESIGN.md` fehlt:** Gate FAIL.
- **DOCX ohne Corporate Design Gate PASS:** zuerst DOCX-QA abschließen.
- **DOCX-Level-2 NOT_RUN:** PDF-Level-2 bleibt NOT_RUN.
- **DOCX nach PASS verändert:** DOCX-Gate erneut ausführen.
- **LibreOffice/soffice fehlt:** klare Dependency-Fehlermeldung; keine Fake-PDF erzeugen.
- **Conversion schlägt fehl:** Fehler ausgeben, keine leere PDF übernehmen.
- **PDF-Reflow weicht sichtbar ab:** zurück zur DOCX-/Template-Quelle; nicht im PDF kaschieren.
- **PDF-QA nicht möglich:** nicht als final geprüft kennzeichnen.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn das kanonische DOCX bereits den Corporate Design Gate bestanden hat, erfolgreich konvertiert wurde, jede PDF-Seite vollständig auf Layout- und Source-Parität geprüft, alle Critical/Major Findings geschlossen und `Corporate Design Gate: PASS` für die finale PDF-Revision dokumentiert wurde. `LEVEL_2_PASS` ist nur zulässig, wenn auch das Source-DOCX Level 2 bestanden hat.
