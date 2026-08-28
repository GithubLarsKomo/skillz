---
name: multimodal-learning-analysis
description: Analysiert ein zeitcodiertes Videoquellenpaket gemeinsam aus Sprache, visuellen Beobachtungen und Metadaten und erzeugt evidenzgebundene Lernclaims, Konzepte, Demonstrationen, Warnungen und Beziehungen. Verwenden nach Video-Ingestion; nicht zum Rendern finaler Lernartefakte oder zum Erfinden nicht sichtbarer Prozessdetails.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - learning-evidence.json
  - learning-concept-map.json
lastEvaluated: 2026-08-28
---

# Multimodal Learning Analysis

## Zweck

Überführe provider-neutrale Video-Metadaten, Transcript, Timestamps und visuelle Evidenzanker in eine belastbare semantische Lernbasis.

## Evidenzmodell

Jede relevante Aussage erhält:

- `claim`;
- `type`: `concept|fact|demonstration|instruction|warning|example|opinion`;
- `basis`: `speech|frame|speech+frame|metadata|derived`;
- `support`: Segment-/Frame-IDs;
- `timestampRange`;
- `confidence`: `high|medium|low`;
- `status`: `observed|derived|unknown`;
- `notes` für Einschränkungen.

**Observed** bedeutet direkt gesagt/gezeigt. **Derived** bedeutet nachvollziehbar aus mehreren beobachteten Elementen abgeleitet. **Unknown** bleibt unbekannt.

## Workflow

1. Kapitel und Themenblöcke rekonstruieren.
2. Atomare Claims und Begriffe extrahieren.
3. Demonstrationen und Zustandsänderungen separat erfassen.
4. Sprache und Bild miteinander abgleichen.
5. Widersprüche zwischen Gesagtem, Gezeigtem und eingeblendeten Daten markieren.
6. Konzepte und Beziehungen als `learning-concept-map.json` modellieren.
7. Relevanz für Takeaways, SOP, Visuals und Prüf-/Kontrollpunkte kennzeichnen.

## Multimodale Regeln

- Aus einem Transcript allein keine Drehrichtung, Position, Werkzeugwahl oder UI-Aktion erfinden.
- Ein sichtbarer Schritt ohne erklärenden Ton darf als beobachtete Handlung beschrieben werden, aber seine Absicht bleibt ggf. `unknown`.
- Eingeblendete Zahlen werden nur übernommen, wenn Einheit/Bezugsgröße lesbar oder aus unmittelbarem Kontext eindeutig ist.
- Creator-Meinung, Vermutung und demonstrierter Fakt bleiben getrennt.
- Ein animiertes oder schematisches Visual ist keine experimentelle Evidenz.

## Konzeptgraph

Der Graph darf Kanten wie `prerequisite-of`, `causes`, `part-of`, `contrasts-with`, `step-before`, `controls`, `measured-by` und `example-of` enthalten. Fehlende Beziehungen nicht ergänzen, nur weil sie fachlich plausibel erscheinen.

## Qualitätsgate

- jeder zentrale Claim besitzt Evidenzanker;
- abgeleitete Claims besitzen eine nachvollziehbare Kette;
- audiovisuelle Widersprüche bleiben sichtbar;
- relevante Unsicherheiten werden nicht in glatte Lernprosa umgewandelt;
- Prozesshandlungen sind in richtiger zeitlicher Reihenfolge;
- keine längeren Quellpassagen werden kopiert.

## Abschluss

Abgeschlossen, wenn `learning-evidence.json` und `learning-concept-map.json` als gemeinsame Source of Truth für Summary, SOP und Visualplanung nutzbar sind.
