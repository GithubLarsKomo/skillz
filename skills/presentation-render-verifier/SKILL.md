---
name: presentation-render-verifier
description: Rendert ein Präsentationsdeck in visuell prüfbare Folienbilder und eine Druck-/PDF-Version und bewertet das Ergebnis auf Clipping, Font-Substitution, unerwartete Umbrüche, Kontrast, visuelle Hierarchie, Dichte und Deck-Konsistenz. Verwenden als finales visuelles QA-Gate nach struktureller Layoutprüfung; nicht als Ersatz für objektbasierte PPTX-Prüfung.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - presentation-layout-qa
outputs:
  - presentation-render-qa.json
  - presentation-render-qa.md
  - presentation-preview.pdf
lastEvaluated: 2026-08-26
---

# Presentation Render Verifier

Dieser Skill prüft, was der Betrachter tatsächlich sieht. Er ergänzt strukturelle PPTX-QA um Render- und Deck-Level-Kontrolle.

## Verbindlicher Ablauf

1. Aktuelles Deck rendern.
2. Einzelne Slides als Bilder oder vergleichbare Renderausgaben erzeugen.
3. Gesamtes Deck als Kontaktbogen/Montage prüfen, sofern technisch möglich.
4. Eine PDF-/Druckversion exportieren und separat prüfen.
5. Findings nach Slide dokumentieren.
6. Findings korrigieren lassen.
7. Deck erneut rendern und erneut prüfen.
8. Finalen Pass nur nach erfolgreicher Re-Render-Prüfung vergeben.

Ein einmaliger Export ohne Re-Render nach Änderungen gilt nicht als abgeschlossenes QA-Gate.

## Slide-Level-Prüfung

- abgeschnittene oder verschwundene Texte,
- geänderte Zeilenumbrüche,
- Font-Substitutionen,
- überlagerte Objekte,
- verzerrte oder falsch gerenderte Bilder/SVGs,
- Tabellen-/Chart-Clipping,
- schwacher Kontrast,
- unlesbare Quellen/Labels,
- inkonsistente Ränder und Ausrichtung,
- Footer- oder Branding-Probleme.

## Deck-Level-Prüfung

- visuelle Hierarchie,
- Rhythmus und Dichte über die Slide-Folge,
- unnötige Wiederholung derselben Layoutidee,
- abrupte Stilbrüche,
- konsistente Titelhierarchie,
- ausgewogene Mischung aus Text, Visuals, Tabellen und Charts,
- erkennbare Section-Struktur,
- konsistentes Corporate Look & Feel.

## PDF-/Druckprüfung

Die PDF dient als zweiter Renderer und als Stabilitätscheck. Besonders prüfen:

- Schriftmetriken und Substitutionen,
- Umbruchunterschiede gegenüber PPTX-Ansicht,
- Transparenzen,
- Vektor-/SVG-Darstellung,
- Crop/Seitenrand,
- eingebettete Fonts oder ersetzte Glyphen.

## Ergebnisstatus

- `pass`: keine ungeklärten critical/major Findings und Re-Render geprüft.
- `review`: nur begründete visuelle Review-Punkte verbleiben.
- `fail`: critical/major Finding oder kein belastbarer Render verfügbar.

## Grenzen

- Keine Aussage `visually verified`, wenn kein tatsächlicher Render geprüft wurde.
- Keine rein textuelle Behauptung, ein Deck sei layoutfehlerfrei.
- PDF-Export ersetzt nicht die Editierbarkeit der finalen PPTX.

## Abschluss

Abgeschlossen, wenn PPTX-Render und PDF-/Druckrender geprüft, relevante Findings korrigiert, die korrigierte Version erneut gerendert und der finale QA-Status dokumentiert wurde.
