---
name: epub3-publication-renderer
description: Rendert einen finalen, kapitelstrukturierten Markdown-Text content-neutral als konservatives EPUB3 mit OPF-Spine, EPUB-Navigation, NCX-Kompatibilitätsnavigation, UTF-8, semantischen Absätzen und Scene Breaks und erzeugt eine strukturelle Validierungsnotiz. Interner Delivery-Worker; verändert keine Prosa und behauptet ohne Plattform-Smoke-Test keine verifizierte ElevenReader-Kompatibilität.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - epub3-publication.epub
  - epub3-validation.json
portableFiles:
  - scripts/render_epub3.py
lastEvaluated: 2026-09-06
---

# EPUB3 Publication Renderer

## Zweck

Eine reine Medienprojektion: finalen Manuskripttext in ein robustes, einfaches EPUB3 verpacken.

**Rendering schreibt nicht um.**

## Eingabeformat

Markdown:

- erstes `# Title` = Buchtitel;
- optional direkt danach `## Subtitle`;
- jedes weitere `# Chapter Title` = EPUB-Kapitel;
- `##` / `###` innerhalb eines Kapitels = Unterüberschriften;
- durch Leerzeilen getrennte Absätze bleiben Absätze;
- `---` oder `* * *` als eigener Block = Scene Break;
- einfache Listen, Blockquotes, Fett/Kursiv werden unterstützt.

## EPUB-Vertrag

Mindestens:

- EPUB3 OPF package;
- UTF-8;
- ZIP entry `mimetype` an erster Stelle und unkomprimiert;
- `META-INF/container.xml`;
- manifest;
- spine;
- `nav.xhtml`;
- `toc.ncx` für breitere Reader-Kompatibilität;
- valide XML-Struktur der erzeugten XHTML-/Package-Dateien;
- kein JavaScript;
- kein Webfont-Zwang;
- einfache, reflow-fähige CSS-Regeln;
- Kapitel-Navigation.

## ElevenReader-Grenze

Der Renderer optimiert für konservative Reader-/TTS-Kompatibilität und erzeugt einen `elevenReaderCompatibility`-Status `structural-pass|not-assessed`.

**Structural pass ist kein realer ElevenReader-Importtest.**

Ein tatsächlicher Import in die aktuelle ElevenReader-Version und die reale Aussprache/Stimme bleiben ein separater Integrationstest.

## Validierung

`epub3-validation.json` enthält mindestens:

- mimetypeFirst;
- mimetypeStored;
- requiredFilesPresent;
- xmlParsePass;
- navigationPresent;
- ncxPresent;
- chapterCount;
- javascriptFree;
- structuralStatus;
- elevenReaderCompatibility;
- limitations.

## Fehlerbehandlung

Kein finaler PASS bei:

- fehlendem Titel;
- keinem Kapitel;
- leerem Kapitel;
- fehlenden Package-Dateien;
- XML-Parsefehler;
- falschem mimetype;
- fehlender Navigation.

## Qualitätsgate

- **Rendering schreibt nicht um.**
- Scene Breaks und Absatzgrenzen bleiben semantisch erhalten.
- Navigation zeigt auf existierende Kapitel.
- Keine Plattformkompatibilität stärker behaupten als geprüft.
- Der Renderer ist genre-neutral; Science-/Fiction-spezifische Hörbarkeitsregeln gehören upstream.

## Abschluss

Abgeschlossen, wenn EPUB und strukturierte Validierungsnotiz erzeugt sind und `structuralStatus=pass` melden.
