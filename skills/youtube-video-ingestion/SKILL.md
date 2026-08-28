---
name: youtube-video-ingestion
description: Normalisiert ein zugängliches YouTube-Video zu einem nachvollziehbaren Quellenpaket aus Metadaten, zeitcodiertem Transcript, Kapitel-/Segmentstruktur und selektierten visuellen Evidenzankern. Verwenden als Ingestion-Schritt für Lern-, SOP- oder Analyseworkflows; nicht zum Umgehen von Zugriffsschutz, DRM oder Plattformbeschränkungen und nicht zur inhaltlichen Synthese.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - youtube-video-source.json
  - youtube-transcript-index.json
  - youtube-frame-index.json
lastEvaluated: 2026-08-28
---

# YouTube Video Ingestion

## Zweck und Grenze

Dieser Skill verwandelt eine YouTube-URL oder einen bereits bereitgestellten lokalen Video-/Audio-/Transcript-Export in ein **reproduzierbares Quellenpaket**. Er bewertet noch nicht, was gelernt werden soll, und schreibt keine Zusammenfassung oder SOP.

## Eingaben

- YouTube-URL oder eindeutige Video-ID;
- optional Nutzer-Transcript, Untertiteldatei oder lokales Video/Audio;
- gewünschte Sprache bzw. bevorzugte Caption-Sprache;
- optional Kapitel-, Zeitraum- oder Themen-Scope.

## Zugriffshierarchie

Nutze ausschließlich rechtmäßig zugängliche Quellen. Die Reihenfolge ist:

1. vom Nutzer bereitgestelltes Transcript/Subtitle;
2. regulär zugängliche manuelle Untertitel/Captions;
3. regulär zugängliche automatisch erzeugte Captions;
4. ASR aus einem vom Nutzer bereitgestellten oder anderweitig zulässig zugänglichen Audio-/Video-Asset;
5. partieller `metadata-only`- oder `transcript-only`-Modus.

**Nicht erlaubt:** Zugriffsschutz, Authentifizierung, Paywalls, Age-/Region-Restriktionen, DRM oder andere technische Schutzmaßnahmen umgehen. Ein fehlender Zugang wird als Evidenzgrenze dokumentiert, nicht technisch erzwungen.

## Normalisierung

### `youtube-video-source.json`

Mindestens:

```json
{
  "schemaVersion": 1,
  "provider": "youtube",
  "videoId": "...",
  "canonicalUrl": "...",
  "title": "...",
  "channel": "...",
  "publishedAt": "...",
  "durationSeconds": 0,
  "language": "...",
  "chapters": [],
  "accessMode": "caption|user-supplied|authorized-asr|metadata-only",
  "sourceWarnings": []
}
```

### Transcript

Segmentiere zeitcodiert und bewahre den Ursprung:

```json
{
  "id": "T-001",
  "start": 12.4,
  "end": 18.8,
  "text": "...",
  "source": "manual-caption|auto-caption|user-transcript|asr",
  "confidence": "high|medium|low|unknown"
}
```

Korrigiere offensichtliche Satzgrenzen nur, wenn Zeitanker erhalten bleiben. Fachbegriffe dürfen normalisiert werden, aber die Rohquelle muss referenzierbar bleiben.

### Visuelle Evidenzanker

Extrahiere **keine vollständige Bildfolge**. Identifiziere gezielt Stellen, an denen visuelle Information für Verständnis oder Prozessrekonstruktion relevant ist:

- gezeigte Bedienhandlung;
- Diagramm/Whiteboard;
- Geräte-/Softwarezustand;
- Vorher/Nachher;
- räumliche Anordnung;
- eingeblendete Werte oder Parameter.

`youtube-frame-index.json` speichert Timestamp, Segmentbezug, kurze Beobachtung und Provenance. Ein Frame ist zunächst **Quelle**, nicht automatisch ein wiederverwendbares Publikationsbild.

## Rechte- und Provenance-Regel

- Video-URL, Video-ID, Timestamp und Herkunft bleiben an jedem verwendeten Quellfragment nachvollziehbar.
- Für finale Lernartefakte bevorzugt der Workflow eigene Diagramme/Illustrationen statt massenhaft Originalframes zu reproduzieren.
- Originalframes nur gezielt verwenden, wenn sie zum Verständnis erforderlich und ihre Verwendung im konkreten Kontext zulässig ist.
- Keine vollständigen Transcripts oder längeren wortgetreuen Passagen als Lernoutput reproduzieren.

## Qualitätsgate

Vor Übergabe prüfen:

- Video eindeutig identifiziert;
- Transcript-Segmente monoton zeitcodiert;
- Caption-/ASR-Herkunft dokumentiert;
- Kapitel und Transcript-Zeiten plausibel;
- visuelle Anker besitzen Timestamp + Segmentreferenz;
- fehlende Audio-/Bildinformation ist explizit;
- keine Zugriffsbeschränkung wurde umgangen.

## Fehlerbehandlung

Kann das Video nicht ausreichend gelesen werden, liefere ein partielles Quellenpaket mit `sourceWarnings`. Die nachgelagerte Analyse muss ihre Confidence daran anpassen.

## Abschluss

Abgeschlossen, wenn Metadaten, Transcript-Index und visuelle Evidenzanker soweit zugänglich normalisiert, provenance-gesichert und ohne inhaltliche Erfindung an `multimodal-learning-analysis` übergeben werden können.
