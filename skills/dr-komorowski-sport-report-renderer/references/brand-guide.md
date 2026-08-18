# Dr. Komorowski Sport Report – Brand Guide

## Herkunft

Diese Vorlage rekonstruiert das in den am 18.08.2026 erzeugten Reports verwendete ReportLab-Design. Das Referenz-PDF nutzt ausschließlich Vektor-/Textobjekte; das DK-Logo ist deshalb als SVG und zusätzlich als Vektor-Flowable im Renderer hinterlegt.

## Farbrollen

| Rolle | Hex | Verwendung |
|---|---:|---|
| Navy | `#173652` | Wortmarke, Header, Hauptüberschriften |
| Dark | `#1C2B3A` | große Reporttitel |
| Body | `#24313E` | Fließtext und Tabelleninhalt |
| Teal | `#2B8884` | Logo-Linien, Tabellenakzent, Rahmen |
| Teal text | `#246F6C` | Eyebrow, Subheads, Callouttitel |
| Muted | `#6B7785` | Footer und Nebeninformation |
| Border | `#D6E0E6` | feine Linien und Tabellenraster |
| Table fill | `#EDF3F6` | Tabellenkopf / Metadatenlabels |
| Callout fill | `#F6F8F9` | neutrale Informationsbox |
| Warning fill | `#FFF4D6` | Belastungs-/Sicherheitshinweis |
| Warning border | `#9A6500` | Warnbox-Rahmen |

## Typografie

- Primär: DejaVu Sans / DejaVu Sans Bold, wenn lokal vorhanden.
- Fallback: Helvetica / Helvetica-Bold.
- Fontdateien werden **nicht** als Skill-Asset gespeichert oder verteilt.
- Große Titel: 22–27 pt, Navy/Dark, bold.
- Abschnittsüberschriften: 18–20 pt, Navy, bold.
- Subheads/Callouttitel: 10–14 pt, Teal text, bold.
- Tabellen/Body: ca. 8–10 pt mit ausreichend Zeilenhöhe.

## Seitenaufbau

- A4 Hochformat.
- Inhalt ca. 18 mm links/rechts, 22 mm oben, 18 mm unten.
- Header oben rechts mit Dokumentkontext und dünner Border-Linie.
- Footer links Dokumenttyp + Datum, rechts `Seite N`.
- Cover beginnt mit Logo, kleinem Teal-Eyebrow, großer Marke/Einrichtungsbezeichnung, Reporttitel, Untertitel, Metadaten-Tabelle und optionalen Callouts.
- Folgeseiten verwenden klare Abschnittsüberschriften, Tabellen und sparsame Callouts.

## Layoutregeln

1. Weißraum ist Teil des Designs; keine dichten Dashboard-Seiten erzeugen.
2. Tabellenheader hell füllen und mit Teal-Linie akzentuieren.
3. Info-Callouts: neutraler sehr heller Hintergrund + Teal-Rahmen.
4. Warn-Callouts: warmes Hellgelb + Ocker-Rahmen, nicht aggressiv rot.
5. Keine Rasterbilder für Logo oder Text erzeugen.
6. Lange Inhalte als Flowables umbrechen; keine absoluten Koordinaten für Fließtext.
7. Visuelle Endkontrolle über gerenderte PNG-Seiten ist obligatorisch.
