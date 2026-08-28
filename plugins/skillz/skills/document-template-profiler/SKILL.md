---
name: document-template-profiler
description: Analysiert ein vorhandenes DOCX/DOTX-Template oder ein bestätigtes Referenzdokument und erzeugt ein wiederverwendbares, provenance-gebundenes Profil für Page Setup, Sections, Styles, Typografie, Header/Footer, Nummerierung, Tabellen, Felder, Content Controls und sichere Einfügepunkte. Verwenden vor template-treuer Dokumenterzeugung; nicht zum Erfinden eines Corporate Designs.
---

# Document Template Profiler

## Zweck und Grenze

Der Skill überführt ein vorhandenes Word-Template oder ein bestätigtes Referenzdokument in einen expliziten, überprüfbaren Layout- und Integrationsvertrag. Die Binärquelle bleibt Source of Truth; das Profil beschreibt sie, ersetzt sie aber nicht.

## Trigger

Verwenden, wenn ein DOCX/DOTX möglichst template-treu weiterverwendet, adaptiert oder als Basis für einen generischen Dokumentworkflow profiliert werden soll.

Nicht verwenden, um aus Webseiten, Logos oder Geschmacksvorgaben ein neues Corporate Design zu erfinden.

## Voraussetzungen

Priorität der Quellen:

1. explizit geliefertes kontrolliertes DOCX/DOTX-Template;
2. bestätigte Referenzdatei desselben Dokumenttyps;
3. dokumentierte Template-Spezifikation;
4. transparenter Fallback nur wenn ausdrücklich zulässig.

Bei einer Binärquelle Dateiname, SHA-256, Template-Status und Analysezeitpunkt dokumentieren.

## Ablauf

1. Dokumentidentität und Source-of-Truth-Status fixieren.
2. Sections, Seitengröße, Orientierung, Ränder, Spalten und Abschnittswechsel inventarisieren.
3. Named Styles, Vererbungen, Fonts, Größen, Absatz-/Zeichenformate und Listen-/Nummerierungsdefinitionen erfassen.
4. Header/Footer-Beziehungen, Logos, Felder, Seitenzahlen und section-spezifische Varianten erfassen.
5. Tabellen-, Caption-, Callout-, Bild- und Quellenmuster bestimmen.
6. Bookmarks, Content Controls, Platzhalter und andere sichere Einfügepunkte identifizieren.
7. kontrollierte Regionen markieren, die nicht rekonstruiert oder überschrieben werden dürfen.
8. beobachtete Layout-Baselines für nachgelagerte QA dokumentieren.

## Profilvertrag

`document-template-profile.json` enthält mindestens:

```json
{
  "schemaVersion": 1,
  "source": {
    "type": "docx|dotx|reference|spec",
    "reference": "...",
    "sha256": "...",
    "templateStatus": "approved-controlled|confirmed-reference|fallback|unknown"
  },
  "pageSetup": {},
  "sections": [],
  "styles": {},
  "typography": {},
  "numbering": {},
  "headersFooters": [],
  "tables": {},
  "fields": [],
  "insertionPoints": [],
  "controlledRegions": [],
  "qaBaselines": {},
  "warnings": []
}
```

Die Markdown-Projektion muss dieselbe Source-Identität, Priorität, Einschränkungen und relevante Warnungen erhalten.

## Prüfungen

- Binäridentität und Template-Status sind nachvollziehbar.
- Section-/Page-Setup und Header/Footer-Varianten wurden nicht zu einem einzigen globalen Layout geglättet.
- Style-Vererbungen und Nummerierung bleiben unterscheidbar.
- sichere Einfügepunkte sind von kontrollierten Regionen getrennt.
- Fallbacks werden nicht als `template-derived` bezeichnet.
- vertraulicher fachlicher Inhalt der Referenz wird nicht unnötig in das Profil übernommen.

## Fehlerbehandlung

- **Binärdatei nicht verfügbar:** nur mit dokumentierter Spezifikation/Referenz fortfahren und Fidelity-Level begrenzen.
- **Template beschädigt oder nicht lesbar:** keinen vollständigen Profil-PASS vergeben.
- **Kein sicherer Einfügepunkt:** als Blocker für template-derived Dokumenterzeugung markieren.
- **Widersprüchliche Referenzen:** Priorität nicht raten; Authority-Entscheidung upstream anfordern.

## Übergabe

Primäre Outputs sind `document-template-profile.json` und `document-template-profile.md`. Nachgelagerte Dokumenterzeugung und QA nutzen das JSON als Maschinenvertrag und die Binärquelle weiterhin als Layout-Authority.

## Abschlusskriterien

Abgeschlossen, wenn die Template-Identität, Page-/Section-Struktur, Styles, Header/Footer, Nummerierung, kontrollierte Regionen und sichere Einfügepunkte ausreichend explizit beschrieben sind, damit ein nachgelagerter Workflow Template-Fidelity prüfen kann, ohne das Design aus implizitem Wissen neu zu erfinden.
