---
name: euroimmun-docx-report-renderer
description: Rendert fachlich finalisierte strukturierte Report-Inhalte als professionelles A4-DOCX im aktuellen EUROIMMUN-From-Revvity-Erscheinungsbild. Nutzt ein im Skill hinterlegtes Public-Reference-DOCX-Template mit aktuellem 2025+-Kopf und unterstützt ein kontrolliertes internes Corporate-Template als Override, ohne fachliche Inhalte zu erfinden oder zu verändern.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - euroimmun-report.docx
lastEvaluated: 2026-08-19
---

# EUROIMMUN DOCX Report Renderer

Setze bereits fachlich geklärten Inhalt in einen wiederverwendbaren EUROIMMUN-Report um. Der Skill trennt **Inhalt** und **Darstellung**: Fach-Skills liefern den Report-Inhalt, dieser Renderer wendet Template, Header/Footer, Styles, Tabellen, Callouts und Seitenlogik an.

## Trigger

Nutze diesen Skill, wenn der Nutzer einen finalisierten Report als **DOCX im EUROIMMUN-Stil** benötigt, insbesondere für Technology-/IP-Due-Diligence, wissenschaftlich-technische Bewertungen, Management-Reports, Entwicklungsberichte oder vergleichbare Arbeitsdokumente.

Nicht nutzen, um die zugrunde liegende fachliche Analyse neu zu erfinden. Wenn Inhalt oder Schlussfolgerungen noch offen sind, zuerst den passenden Fach-Skill ausführen.

## Template-Modell

Die kanonische Layoutquelle ist ein DOCX-Template.

- Bundled fallback template: als repo-kompatible Textrepräsentation `assets/euroimmun-report-template.docx.b64` hinterlegt. `scripts/build_template.py` ist die editierbare Generatorquelle; der Renderer dekodiert die geprüfte DOCX-Vorlage bei Bedarf in-memory.
- Theme/Brand-Metadaten: `assets/report-theme.json`
- Editierbare Logo-Referenz: `assets/euroimmun-logo-public-reference.svg`
- Beispiel-Spec: `assets/report-spec.example.json`
- Kontrolliertes Template-Override: `--template PATH.docx`

Die gebündelte Template-Definition ist eine **Public-Reference-Vorlage** auf Basis des seit Juli 2025 ausgerollten öffentlichen EUROIMMUN-From-Revvity-Auftritts. Es ist kein Ersatz für ein intern dokumentenlenkungsseitig freigegebenes Corporate-Template. Für formale externe oder kontrollierte Dokumente hat ein aktuelles freigegebenes internes Template Vorrang.

Der aktuelle öffentliche Kopf enthält die kleingeschriebene EUROIMMUN-Wortmarke mit `From Revvity` und das grüne Titerplane-Symbol. Der Footer des Public-Reference-Templates führt `EUROIMMUN Medizinische Labordiagnostika AG · Seekamp 31 · 23560 Lübeck`.

## Template-Vertrag

Ein Template muss mindestens diese Platzhalter enthalten:

- `{{DOCUMENT_TYPE}}`
- `{{DOCUMENT_ID}}`
- `{{DATE}}`
- `{{CONFIDENTIALITY}}`
- `{{REPORT_BODY}}`

Fehlt ein Pflichtplatzhalter, **abbrechen**. Niemals still auf das gebündelte Template zurückfallen, wenn der Nutzer ausdrücklich ein kontrolliertes Template bereitgestellt hat.

Ein Template-Override behält seinen eigenen Header, Footer, Logoaufbau, Corporate Styles und Seitenfelder. Der Renderer befüllt nur die vereinbarten Platzhalter und den Body.

## Report-Spec

Eingabe ist ein JSON-Objekt mit `metadata`, optional `summary` und `sections[]`.

Pflicht-Metadaten:

- `title`
- `date`
- `document_type`

Optionale Metadaten:

- `subtitle`
- `document_id`
- `version`
- `author`
- `department`
- `subject`
- `confidentiality`

Unterstützte Blocktypen:

- `paragraph`
- `heading`
- `bullets`
- `table`
- `callout`
- `image`
- `spacer`
- `pagebreak`

Callout-Rollen: `info`, `warning`, `decision`, `neutral`.

## Ablauf

1. **Inhalt einfrieren.** Fachtext, Tabellen, Bilder und Schlussfolgerungen als Report-Spec strukturieren. Der Renderer ändert keine Assay-Performance, Claim-Mappings, regulatorischen Bewertungen, Zahlen oder Managemententscheidungen.
2. **Template bestimmen.** Wenn ein freigegebenes aktuelles Corporate-Template bereitgestellt wurde, dieses verwenden. Sonst die hinterlegte Public-Reference-DOCX-Vorlage aus `assets/euroimmun-report-template.docx.b64` verwenden und deren Status transparent halten. Die binäre DOCX-Datei selbst wird wegen des textbasierten Skill-Repo-Vertrags nicht direkt versioniert; die Base64-Repräsentation, der Builder, Theme und Logo-Referenz bilden gemeinsam die versionierte Template-Quelle.
3. **Template-Vertrag validieren.** Alle Pflichtplatzhalter müssen vorhanden sein.
4. **Report rendern.** `scripts/render_report.py INPUT.json OUTPUT.docx [--template TEMPLATE.docx]` verwenden.
5. **Struktur prüfen.** A4, Header/Footer, Styles, Tabellenbreiten, Callouts, Bilder, Überschriftenhierarchie und Dokument-Metadaten prüfen.
6. **DOCX rendern.** Mit dem verfügbaren DOCX-Renderer nach PNG rendern; alle Seiten bei 100 % visuell prüfen.
7. **Fehler korrigieren und erneut rendern.** Clipping, Überlappung, Tabellenüberlauf, schlechte Umbrüche, fehlende Glyphen oder Header-/Footer-Probleme müssen vor Übergabe behoben sein.
8. **Nur finale DOCX ausgeben.** QA-PNG/PDF bleiben interne Prüfartefakte, sofern der Nutzer sie nicht verlangt.

Beispiel:

```bash
python scripts/render_report.py assets/report-spec.example.json /tmp/euroimmun-report.docx
python scripts/render_report.py input.json output.docx --template /path/to/approved-euroimmun-template.docx
```

## Designregeln für das Public-Reference-Template

- A4, ca. 20 mm Seitenränder und großzügiger Weißraum.
- Aktueller EUROIMMUN-From-Revvity-Kopf links; Dokumenttyp, ID und Datum rechts.
- Schwarz/dunkles Grau für Primärtext, frisches EUROIMMUN-Grün als Akzent.
- Kein altes blaues EUROIMMUN-Branding in neu erzeugten Public-Reference-Reports.
- Tabellen mit zurückhaltender grüner Headerfläche und klaren Borders.
- Callouts nur als semantische Information, Warning oder Decision; keine dekorative Überladung.
- Keine Fontdateien in Skill oder Dokumentpaket einbetten oder weitergeben.

Die konkrete Farbdefinition im Public-Reference-Theme ist eine reproduzierbare Arbeitsdefinition, **keine Behauptung eines internen Corporate-Design-Hexwertes**. Ein freigegebenes internes Template überschreibt sie vollständig.

## Qualitäts- und Safety-Regeln

- Inhalt nicht still korrigieren oder verdichten, wenn dadurch Aussage, Evidenzgrad oder Unsicherheit verändert wird.
- Kein erfundenes Dokumentenkennzeichen, keine erfundene Freigabe, kein erfundener Autor.
- `EUROIMMUN Confidential` nur verwenden, wenn das gewünschte Dokument als vertraulich ausgegeben werden soll; ansonsten passende Klassifikation im Spec setzen.
- Externe oder kontrollierte Reports nicht als "official corporate template" bezeichnen, wenn nur die Public-Reference-Vorlage verwendet wurde.
- Bei einem bereitgestellten kontrollierten Template weder Logo noch Footer durch Public-Reference-Assets ersetzen.
- Sensible oder personenbezogene Daten nur übernehmen, soweit für das beauftragte Dokument erforderlich.

## Fehlerbehandlung

- **python-docx fehlt:** Abhängigkeit melden; keine Fake-DOCX-Datei erzeugen.
- **Public-Reference-Template fehlt:** aus `assets/euroimmun-report-template.docx.b64` laden; fehlt oder ist diese Repräsentation ungültig, mit `scripts/build_template.py` neu erzeugen beziehungsweise den Fehler melden; schlägt das fehl, abbrechen. Bei einem ausdrücklich bereitgestellten Corporate-Template niemals automatisch ersetzen.
- **Pflichtplatzhalter fehlen:** mit konkreter Token-Liste abbrechen; kein stilles Fallback.
- **Bild fehlt:** mit Blockpfad abbrechen; kein Platzhalterbild erfinden.
- **Zu breite Tabelle:** relative Breiten anpassen, Text umbrechen oder Tabelle logisch teilen; nicht unlesbar klein skalieren.
- **Visuelles QA nicht möglich:** Dokument nicht als final geprüft ausgeben.

## Übergabe

Primärer Output ist `euroimmun-report.docx`. Die Report-Spec kann als reproduzierbares Audit-Artefakt erhalten bleiben. Für PDF-Ausgabe danach `euroimmun-pdf-report-renderer` verwenden, damit DOCX und PDF aus derselben Layoutquelle stammen.

## Abschlusskriterien

Abgeschlossen ist der Skill erst, wenn das gewünschte Template validiert, die DOCX-Datei erzeugt und **jede Seite visuell geprüft** wurde und keine Clipping-, Umbruch-, Tabellen-, Header-/Footer- oder Glyphenfehler mehr sichtbar sind.
