---
name: precision-language-rewriter
description: Überarbeitet deutsche und englische Reports, Memos, Sachtexte, Reden, Sprechertexte und Folientexte auf Präzision, idiomatische Sprache, Genrepassung und optional bestätigte Author Voice, ohne neue Sachinformation zu erzeugen oder fachliche Terminologie zugunsten künstlicher Variation zu verwässern.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - revised-text
  - rewrite-change-map.json
lastEvaluated: 2026-08-23
---

# Precision Language Rewriter

## Prioritäten

Immer in dieser Reihenfolge arbeiten:

1. **semantic fidelity**
2. **epistemic precision**
3. **genre fidelity**
4. **authorial fidelity**
5. **linguistic quality**

Ein niedrigerer Punkt darf einen höheren niemals beschädigen.

## Parameter

- `language`: `de|en`
- `genre`: `report|memo|general|speech|speaker-notes|slide-copy`
- `mode`: `light|author|editorial`
- `audience`: `expert|management|mixed|public`
- `englishVariant`: `international|us|uk`, falls relevant
- optional `author-voice-profile.json` oder `speaker-profile.json`
- optional `prose-audit.json`
- optional Fidelity Lock mit Claims, Zahlen, Quellen, Modalität und Terminologie

## Modi

### light
Entfernt unnötige generische LLM-Muster, Redundanz und sprachliche Reibung. Struktur nur lokal verändern.

### author
Wie `light`, zusätzlich an bestätigten Author-Voice- oder Speaker-Profile-Merkmalen ausrichten. Fehlt ein belastbares Profil, transparent auf Genre-/Sprachregeln zurückfallen und keine persönliche Stimme erfinden.

### editorial
Darf Absätze oder Sprechpassagen stärker rekonstruieren, Reihenfolgen optimieren und Redundanz entfernen. Faktenlage und geschützte Claims bleiben erhalten.

## Allgemeine Stilregeln

- Direkte, analytische Formulierungen bevorzugen, aber keine Evidenzstufe erhöhen.
- Unsicherheit epistemisch präzise erhalten.
- Fachterminologie bewusst wiederholen, wenn Synonymvariation Referenzklarheit mindert.
- Redundanz entfernen, außer Wiederholung erfüllt bei gesprochener Sprache eine bewusste rhetorische Funktion.
- Keine generischen LLM-Übergänge, künstliche Dreierfiguren oder rhetorischen Fragen allein zur Wirkung hinzufügen.

### Deutsch

Natürliche Fachsprache vor Verwaltungsstil. Vermeidbare Nominalisierungen reduzieren, etablierte Fachnomina erhalten. Idiomatische Vorfeldvariation zulassen. Semikolons vermeiden, Doppelpunkte selten, Gedankenstriche sparsam.

Für `speech|speaker-notes` zusätzlich:
- sprechbare Satz- und Atemeinheiten bevorzugen;
- verschachtelte Nebensatzketten reduzieren;
- aktive Verben und konkrete Bezüge bevorzugen;
- bewusste Wiederholung, Kontrast und Rhythmus zulassen, wenn sie der Dramaturgie dienen;
- Zahlen, Abkürzungen und Fachbegriffe akustisch verständlich einführen.

### Englisch

Bei `report|memo` formelles Englisch ohne unnötige Kontraktionen; Passiv zulassen, wenn Prozess oder Ergebnis wichtiger als Akteur ist. Zielvariante an Adressat ausrichten.

Für `speech|speaker-notes` zusätzlich:
- idiomatisches gesprochenes Englisch und akustisch klare Clause-Struktur bevorzugen;
- Kontraktionen zulassen, wenn Register und Speaker Profile sie tragen;
- inflated register, noun stacks und template transitions reduzieren;
- aktive, konkrete Formulierungen bevorzugen, ohne wissenschaftliches Hedging zu verlieren.

### Slide Copy

Für `slide-copy` gelten unabhängig von der Sprache:
- eine Kernaussage pro Folie;
- aussageorientierte Headlines statt bloßer Themenüberschriften, sofern die Evidenz dies trägt;
- kurze, scanbare On-Slide-Texte;
- parallele Struktur nur bei tatsächlich gleichrangigen Elementen;
- Zahlen, Einheiten, Quellenhinweise und geschützte Terminologie unverändert erhalten;
- keine Prosaabsätze, wenn Information visuell oder in Speaker Notes besser aufgehoben ist;
- keine generischen Überschriften wie `Overview`, `Key Takeaways` oder `Zusammenfassung`, wenn eine konkrete Aussage möglich ist.

## Hard Stops

- **Keine neue Sachinformation erzeugen.**
- Keine Zahlen, Quellen, Negationen, Bedingungen oder fachlichen Claims still verändern.
- Keine Unsicherheit in Gewissheit umschreiben.
- Keine rhetorische Zuspitzung hinzufügen, die Konzept oder Ausgangstext nicht trägt.
- Keine "Humanisierung" durch Fehler, Zufall oder Detector-Evasion.
- Slide Copy darf komplexe Inhalte nicht durch Kürzung verfälschen; im Zweifel in Speaker Notes auslagern.

## Change Map

```json
{
  "schemaVersion": 1,
  "mode": "author",
  "language": "de",
  "genre": "speech",
  "changes": [
    {"span": "...", "type": "clarify|compress|restructure|terminology|tone|speakability|slide-density", "semanticImpact": "none"}
  ],
  "fallbacks": []
}
```

## Abschluss

Abgeschlossen, wenn der Zieltext lesbarer beziehungsweise sprechbarer und spezifischer ist, alle Hard Stops respektiert, das gewählte Sprach-/Genre-/Modusprofil eingehalten und die Änderung für `rewrite-fidelity-verifier` nachvollziehbar dokumentiert ist.
