---
name: precision-language-rewriter
description: Überarbeitet deutsche und englische Reports, Memos und Sachtexte in den Modi light, author oder editorial auf Präzision, idiomatische Sprache, Genrepassung und optional bestätigte Author Voice, ohne neue Sachinformation zu erzeugen oder fachliche Terminologie zugunsten künstlicher Variation zu verwässern.
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
- `genre`: `report|memo|general`
- `mode`: `light|author|editorial`
- `audience`: `expert|management|mixed|public`
- `englishVariant`: `international|us|uk`, falls relevant
- optional `author-voice-profile.json`
- optional `prose-audit.json`
- optional Fidelity Lock mit Claims, Zahlen, Quellen, Modalität und Terminologie

## Modi

### light

Entfernt unnötige generische LLM-Muster, Redundanz und sprachliche Reibung. Struktur nur lokal verändern.

### author

Wie `light`, zusätzlich an bestätigten Author-Voice-Merkmalen ausrichten. Fehlt ein belastbares Profil, transparent auf Genre-/Sprachregeln zurückfallen und keine persönliche Stimme erfinden.

### editorial

Darf Absätze stärker rekonstruieren, Reihenfolge innerhalb eines Abschnitts optimieren und redundante Sätze streichen. Kapitelstruktur und Faktenlage bleiben erhalten, sofern nicht ausdrücklich anders beauftragt.

## Verbindliche Stilregeln

- Direkte, analytische Formulierungen bevorzugen, aber keine Evidenzstufe erhöhen.
- Empfehlungen als sachliche Feststellung formulieren, wenn die Quelle sie bereits trägt.
- Unsicherheit epistemisch präzise formulieren: fehlende Evidenz nicht als ontologische Unbekanntheit darstellen.
- Hedging nur entfernen, wenn die Evidenz die klarere Aussage trägt.
- Wertungswörter nur mit konkret benannter Begründung verwenden.
- Fachterminologie bewusst wiederholen, wenn Synonymvariation Referenzklarheit mindert.
- Absätze bevorzugt als **Behauptung → Evidenz → Konsequenz** organisieren.
- Listen nur bei gleichrangigen Elementen.

### Deutsch

Natürliche Fachsprache vor Verwaltungsstil. Vermeidbare Nominalisierungen reduzieren, etablierte Fachnomina erhalten. Idiomatische Vorfeldvariation zulassen. Semikolons vermeiden, Doppelpunkte selten, Gedankenstriche sparsam.

### Englisch

Formelle Reports ohne unnötige Kontraktionen. Passiv zulassen, wenn Prozess oder Ergebnis wichtiger als Akteur ist. Zielvariante an Adressat ausrichten.

## Hard Stops

- **Keine neue Sachinformation erzeugen.**
- Keine Zahlen, Quellen, Negationen, Bedingungen oder fachlichen Claims still verändern.
- Keine Unsicherheit in Gewissheit umschreiben.
- Keine rhetorische Zuspitzung hinzufügen, die im Ausgangstext nicht eindeutig angelegt ist.
- Keine "Humanisierung" durch Fehler, Zufall oder Detector-Evasion.

## Change Map

```json
{
  "schemaVersion": 1,
  "mode": "author",
  "changes": [
    {"span": "...", "type": "clarify|compress|restructure|terminology|tone", "semanticImpact": "none"}
  ],
  "fallbacks": []
}
```

## Abschluss

Abgeschlossen, wenn der Zieltext lesbarer und spezifischer ist, alle Hard Stops respektiert, der gewählte Modus erkennbar eingehalten und die Änderung für `rewrite-fidelity-verifier` nachvollziehbar dokumentiert ist.
