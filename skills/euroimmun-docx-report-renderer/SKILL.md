---
name: euroimmun-docx-report-renderer
description: Rendert fachlich finalisierte strukturierte Report-Inhalte als professionelles A4-DOCX im EUROIMMUN-/Revvity-Erscheinungsbild. Bevorzugt eine verifizierte interne Corporate-DOCX-Binärvorlage mit Level-2-Template-Parität und nutzt die Public-Reference-Vorlage ausschließlich als transparenten Level-1-Fallback.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - euroimmun-report.docx
lastEvaluated: 2026-08-28
---

# EUROIMMUN DOCX Report Renderer

Setze bereits fachlich geklärten Inhalt in einen wiederverwendbaren EUROIMMUN-Report um. Der Skill trennt **Inhalt** und **Darstellung**: Fach-Skills liefern den Report-Inhalt, dieser Renderer wendet Binärtemplate, Styles, Header/Footer, Tabellen, Callouts, Bilder und Seitenlogik an.

## Verbindlicher Corporate Design Contract

Für jeden EUROIMMUN-Firmenreport MUSS vor dem Rendern `docs/corporate/euroimmun/DESIGN.md` gelesen und als normativer Design Contract angewendet werden. Zusätzlich MUSS `docs/corporate/euroimmun/ACTIVE_REPORT_REFERENCE.md` für den aktuellen DOCX-Referenzstatus und `docs/corporate/euroimmun/GOLDEN_REFERENCE.md` für Level-1/Level-2-Verifikation berücksichtigt werden.

- Ist `docs/corporate/euroimmun/DESIGN.md` nicht verfügbar, den Corporate Workflow abbrechen statt Designregeln zu improvisieren.
- Ein für die konkrete Aufgabe geliefertes `approved-controlled` Corporate-DOCX hat höchste Priorität.
- Ein verifiziertes Corporate-DOCX bleibt Source of Truth für Sections, Page Setup, Styles, Header/Footer, Logos, Felder, Nummerierung und kontrollierte Template-Elemente.
- Das Brand-Profil `euroimmun-corporate` ist nur für neu zu definierende Corporate-Farbrollen autoritativ, soweit das aktive Template die Rolle nicht selbst definiert.
- `template-derived`, `controlled-template parity` oder vergleichbare Aussagen sind ausschließlich nach Report-Level-2-PASS zulässig.
- Vor Übergabe MUSS der vollständige `Corporate Design Gate` aus `DESIGN.md` durchgeführt werden.

## Aktueller Referenzstatus

Derzeit ist **keine intern freigegebene oder anderweitig bestätigte EUROIMMUN-DOCX-Binärvorlage als bevorzugte aktuelle Level-2-Referenz registriert**. Die vorhandene gebündelte Vorlage ist ausdrücklich `public-reference-fallback` und bleibt Level 1.

Daraus folgt:

- ohne echte Corporate-DOCX-Binärvorlage: Report-Level-2 = `NOT_RUN`;
- Public-Reference-Ausgaben dürfen `Corporate Design Gate: PASS` erreichen, bleiben aber `template-compatible / public-reference-fallback`;
- sie dürfen niemals als intern freigegebenes oder `template-derived` Corporate-Dokument bezeichnet werden;
- sobald eine echte Vorlage bereitgestellt wird, muss deren SHA-256, Status und Template-Inventar vor Level-2-Verwendung in `ACTIVE_REPORT_REFERENCE.md` bzw. dem Laufnachweis erfasst werden.

## Referenz-Priorität

1. Für die konkrete Aufgabe geliefertes `approved-controlled` Corporate-DOCX.
2. Verifizierte bevorzugte aktuelle DOCX-Binärreferenz aus `ACTIVE_REPORT_REFERENCE.md`, sobald vorhanden.
3. Andere explizit gelieferte bestätigte Corporate-DOCX-Binärreferenz mit dokumentierter Provenienz.
4. Gebündelte Public-Reference-Vorlage als `template-compatible / public-reference-fallback`.

Ein niedriger priorisiertes Template darf ein höher priorisiertes nicht stillschweigend verdrängen.

## Template-Modell

### Level 1 — Public Reference

- Repo-kompatible Repräsentation: `assets/euroimmun-report-template.docx.b64`
- Generatorquelle: `scripts/build_template.py`
- Theme/Brand-Metadaten: `assets/report-theme.json`
- Logo-Referenz: `assets/euroimmun-logo-public-reference.svg`
- Beispiel-Spec: `assets/report-spec.example.json`

Diese Vorlage basiert auf dem öffentlichen EUROIMMUN-From-Revvity-Auftritt und ist **kein dokumentenlenkungsseitig freigegebenes Corporate Template**.

### Level 2 — Reales Corporate-DOCX

Eine reale interne oder bestätigte DOCX-Binärvorlage wird nicht in Skillz umgebaut. Stattdessen werden Binärquelle und Adapter getrennt:

- **Binary source:** unverändertes `.docx`/`.dotx` zur Laufzeit;
- **identity lock:** Dateiname, SHA-256 und Template-Status;
- **template profile/adapter:** explizite Mapping-Information, wie Inhalt eingefügt werden darf, ohne kontrollierte Template-Elemente zu rekonstruieren oder zu überschreiben.

Der Level-2-Adapter MUSS mindestens dokumentieren:

- Sections, Seitengröße und Ränder;
- verwendete Named Styles und Hierarchie;
- Header/Footer-Beziehungen je Section;
- Logos/Bilder in kontrollierten Regionen;
- Felder, Seitenzahlen und Dokumentmetadaten;
- Fontfamilien und bekannte Fallbacks;
- erlaubten Body-Einfügepunkt bzw. Content-Control/Bookmark/Anchor;
- Tabellen-/Caption-/Callout-Mapping, soweit anwendbar.

Fehlt ein sicherer Einfügepunkt oder Adapter, Level 2 `NOT_RUN` bzw. `FAIL`; das Template darf nicht destruktiv für Skillz umgebaut werden.

## Template-Vertrag

Für den **Public-Reference-Fallback** gelten weiterhin die Pflichtplatzhalter:

- `{{DOCUMENT_TYPE}}`
- `{{DOCUMENT_ID}}`
- `{{DATE}}`
- `{{CONFIDENTIALITY}}`
- `{{REPORT_BODY}}`

Für ein reales Level-2-Corporate-Template sind diese Tokens **nicht verpflichtend**. Dort gilt der explizite Adaptervertrag des Template-Profils. Niemals still auf das Public-Reference-Template zurückfallen, wenn ein kontrolliertes Template bereitgestellt wurde, aber nicht sicher verarbeitet werden kann.

## Report-Spec

Eingabe ist ein JSON-Objekt mit `metadata`, optional `summary` und `sections[]`.

Pflicht-Metadaten: `title`, `date`, `document_type`.

Optionale Metadaten: `subtitle`, `document_id`, `version`, `author`, `department`, `subject`, `confidentiality`.

Unterstützte Blocktypen: `paragraph`, `heading`, `bullets`, `table`, `callout`, `image`, `spacer`, `pagebreak`.
Callout-Rollen: `info`, `warning`, `decision`, `neutral`.

## Ablauf

1. **Design- und Referenzstatus laden.** `DESIGN.md`, `ACTIVE_REPORT_REFERENCE.md` und `GOLDEN_REFERENCE.md` lesen; Gate A mit Template-Status, SHA-Identität, Sprache/Zielgruppe und Klassifikationsquelle vorbereiten.
2. **Inhalt einfrieren.** Fachtext, Tabellen, Bilder und Schlussfolgerungen als Report-Spec strukturieren. Keine fachlichen Aussagen, Zahlen oder Evidenzgrade durch Layoutarbeit verändern.
3. **Template nach Priorität bestimmen.** Task-spezifisches approved-controlled > aktive Level-2-Referenz > andere bestätigte Binärreferenz > Public Reference.
4. **Bei Binärtemplate Source Lock durchführen.** SHA-256 berechnen und gegen registrierte/angegebene Identität prüfen. Bei Abweichung keine bestehende Level-2-Zertifizierung übernehmen.
5. **Template-Profil validieren.** Für Level 2 Sections, Styles, Header/Footer, Felder, Bilder/Logos, Fonts und Content-Anchor inventarisieren bzw. gegen registriertes Profil prüfen. Public Reference validiert stattdessen die Pflichtplatzhalter.
6. **Report rendern.** Public Reference: `scripts/render_report.py INPUT.json OUTPUT.docx`. Kontrolliertes Template nur über dessen validierten Adapter verwenden.
7. **Strukturelles Corporate Design QA.** Page Geometry, Header/Footer, Logos, Fields, Named Styles, Tabellen, Callouts, Bilder, Metadaten, Klassifikation und unerlaubte Rekonstruktionen prüfen.
8. **DOCX vollständig rendern.** Jede Seite als Seitenbild/äquivalent rendern und bei 100 % visuell prüfen; Stichproben genügen nicht.
9. **Level-2-Parität prüfen, wenn Binärtemplate aktiv.** Kontrollierte Template-Regionen über stabile Geometrie/Fingerprints und Rendervergleich prüfen. Keine erforderlichen Template-Elemente dürfen rekonstruiert worden sein.
10. **Fehler korrigieren und erneut rendern.** Nach jeder materiellen Änderung die betroffenen strukturellen und visuellen Checks wiederholen.
11. **Corporate Design Gate und Golden-Reference-Level abschließen.** Critical/Major = 0; Render-Coverage vollständig. `template-derived` nur bei Report-Level-2-PASS.
12. **Finale DOCX ausgeben.** QA-Artefakte können intern bleiben, sofern nicht angefordert.

## Report-Level-2-Akzeptanz

`LEVEL_2_PASS` für DOCX erfordert mindestens:

- echte DOCX/DOTX-Binärquelle verfügbar;
- SHA-256 und Template-Status dokumentiert;
- derivation = `template-derived`;
- valides Template-Profil/Adapter;
- keine erforderlichen Header/Footer/Logo/Field/Style-Elemente rekonstruiert;
- Sections/Page Setup und kontrollierte Regionen nachweislich erhalten;
- jede DOCX-Seite gerendert und geprüft;
- unresolved Critical = 0;
- unresolved Major = 0;
- `Corporate Design Gate: PASS`.

Fehlt eine Bedingung, ist Level 2 `FAIL` oder `NOT_RUN`, niemals stillschweigend PASS.

## Designregeln für das Public-Reference-Template

Diese Regeln gelten nur für `public-reference-fallback`:

- A4, ca. 20 mm Seitenränder und großzügiger Weißraum.
- EUROIMMUN-From-Revvity-Kopf links; Dokumenttyp, ID und Datum rechts.
- Schwarz/dunkles Grau für Primärtext; Public-Reference-Grün als Akzent.
- Tabellen mit zurückhaltender Headerfläche und klaren Borders.
- Callouts semantisch, nicht dekorativ.
- Keine Fontdateien einbetten oder weitergeben.

Die Public-Reference-Farbdefinition ist eine reproduzierbare Arbeitsdefinition, keine Behauptung eines internen Corporate-Design-Hexwertes.

## Qualitäts- und Safety-Regeln

- Inhalt nicht still korrigieren oder verdichten, wenn Aussage, Evidenzgrad oder Unsicherheit verändert würden.
- Kein erfundenes Dokumentenkennzeichen, keine erfundene Freigabe, kein erfundener Autor.
- Klassifikation nur entsprechend Aufgabenbasis setzen.
- Bei kontrolliertem Template weder Logo, Footer noch Fields durch Public-Reference-Assets ersetzen.
- Keine Level-2-/Approval-Aussage aus bloßer optischer Ähnlichkeit ableiten.

## Fehlerbehandlung

- **Corporate `DESIGN.md` fehlt:** abbrechen.
- **Aktive Referenzinformation fehlt:** keine Level-2-Aussage; Public Reference bleibt Level 1.
- **Binärtemplate fehlt oder SHA weicht ab:** Level 2 `NOT_RUN`/`FAIL`; nicht rekonstruieren.
- **Template-Adapter fehlt/unsicher:** Level 2 `NOT_RUN`/`FAIL`; Binärtemplate nicht destruktiv verändern.
- **python-docx fehlt:** Abhängigkeit melden; keine Fake-DOCX erzeugen.
- **Public-Reference-Pflichtplatzhalter fehlen:** abbrechen.
- **Bild fehlt:** mit Blockpfad abbrechen; kein Platzhalterbild erfinden.
- **Zu breite Tabelle:** umbrechen, logisch teilen oder ggf. Landscape-Section über erlaubtes Template-Verhalten; nicht unlesbar klein skalieren.
- **Visuelles QA nicht möglich:** Dokument nicht als final geprüft ausgeben; Corporate Design Gate bleibt FAIL.

## Übergabe

Primärer Output ist `euroimmun-report.docx`. Für PDF-Ausgabe danach `euroimmun-pdf-report-renderer` verwenden, damit DOCX und PDF aus derselben kontrollierten Layoutquelle stammen.

## Abschlusskriterien

Abgeschlossen ist der Skill erst, wenn Template/Referenzstatus korrekt ausgewiesen, DOCX erzeugt, jede Seite visuell geprüft, alle Critical/Major Findings geschlossen und `Corporate Design Gate: PASS` dokumentiert wurde. `template-derived` oder Report-Level-2-PASS darf nur ausgegeben werden, wenn die reale Binärquelle und sämtliche Level-2-Paritätschecks bestanden wurden.
