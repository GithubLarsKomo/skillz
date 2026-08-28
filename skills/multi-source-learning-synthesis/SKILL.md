---
name: multi-source-learning-synthesis
description: Konsolidiert mehrere evidenzgebundene Learning-Modelle zu einem deduplizierten gemeinsamen Wissensmodell mit Claim-Clustern, Konflikten, Quellenabdeckung, Konsensstärke und offenen Lücken. Verwenden für Playlist-, Kurs- oder Multi-Video-Learning vor gemeinsamer HTML/PPTX/DOCX/PDF-Ausgabe.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - learning-source-arbitration
outputs:
  - multi-source-learning-model.json
  - multi-source-conflict-map.json
lastEvaluated: 2026-08-28
---

# Multi-Source Learning Synthesis

## Ziel

Mehrere einzelne `learning-content-model.json`-Artefakte werden nicht einfach aneinandergereiht, sondern zu einer gemeinsamen, nachvollziehbaren Lernbasis verdichtet.

## Eingaben

- zwei oder mehr per Einzelvideo-Workflow erzeugte Learning-Modelle;
- zugehörige Evidence Maps;
- `learning-source-arbitration.json`;
- gewünschte Zielgruppe, Sprache, Tiefe und Output-Modus.

## Normalisierung

Vor der Synthese:

1. Begriffe/Synonyme normalisieren, Originalterminologie erhalten;
2. Einheiten und Zahlenformate harmonisieren, ohne Werte umzudeuten;
3. Claims atomisieren;
4. Scope/Population/Version/Methode/Setting als Qualifier erhalten;
5. semantisch identische Claims clustern;
6. bloß thematisch ähnliche Aussagen nicht fälschlich verschmelzen.

## Deduplizierung

Jeder Claim-Cluster erhält:

- `canonicalClaim`;
- unterstützende Source-/Evidence-IDs;
- `independentSourceCount`;
- `convergenceStatus` aus der Arbitration;
- relevante Qualifier;
- stärkste zulässige Formulierung;
- abweichende Varianten;
- Konflikt-/Unsicherheitsstatus.

Redundanz wird aus der Darstellung entfernt, aber Provenienz bleibt erhalten.

## Konflikte

Konflikte werden als eigene Objekte modelliert:

- strittige Aussage;
- Position A/B/...;
- zugehörige Quellen und Evidenz;
- mögliche Erklärungen wie Scope, Zeitpunkt, Methode, Definition oder echte fachliche Uneinigkeit;
- Auflösungsstatus `resolved-by-scope | resolved-by-authority | unresolved | insufficient`;
- sichere Formulierung für Lernartefakte.

Ein ungelöster materieller Konflikt darf nicht als eindeutige Take-Home-Message erscheinen.

## Coverage Map

Das Modell dokumentiert:

- welche Lernziele von welchen Quellen abgedeckt werden;
- Single-Source-Bereiche;
- Bereiche mit unabhängiger Konvergenz;
- widersprüchliche Bereiche;
- Wissenslücken;
- optionale Empfehlung für weitere Recherche.

## Konsolidierte Struktur

Default:

`why it matters -> shared mental model -> consensus core -> deeper mechanisms -> variants/context -> conflicts/open questions -> procedure if defensible -> common mistakes -> takeaways -> source map`

Die Struktur folgt der Lernlogik, nicht der Reihenfolge der Videos.

## SOP-Synthese

Wenn mehrere Videos Prozesse zeigen:

- identische Schritte clustern;
- Varianten als Varianten erhalten;
- Parameter nur übernehmen, wenn ihre Bedingungen klar sind;
- unterschiedliche Protokolle nicht zu einem hypothetischen Hybrid-Protokoll verschmelzen;
- `observed`, `derived`, `recommended`, `open` erhalten;
- bei kritischen ungelösten Differenzen `incomplete-for-controlled-use` setzen.

## Output

`multi-source-learning-model.json` enthält mindestens:

- `schemaVersion`;
- `sources[]`;
- `sourceModelFingerprints[]`;
- `audience`, `language`, `mode`;
- `learningObjectives[]`;
- `claimClusters[]`;
- `consensusCore[]`;
- `qualifiedClaims[]`;
- `conflicts[]`;
- `coverageMap[]`;
- `procedureVariants[]` optional;
- `sections[]`;
- `sourceMap[]`;
- `openEvidenceGaps[]`;
- `requestedFormats[]`.

`multi-source-conflict-map.json` ist die kompakte prüfbare Konfliktansicht.

## Regeln

- Kein Claim wird stärker formuliert als die Arbitration erlaubt.
- Häufige Wiederholung ist keine Evidenzstärke.
- Der Synthese-Text darf Quellenunterschiede komprimieren, aber nicht ausradieren.
- Quellen mit gemeinsamem Ursprung werden beim unabhängigen Support nicht mehrfach gezählt.
- Alle Renderer nutzen denselben unveränderlichen Multi-Source-Fingerprint.

## Qualitätsfälle

**Happy Path:** mehrere Quellen ergänzen sich und bestätigen den Kern -> kompakter Consensus Core mit breiter Source Map.

**Edge Case:** eine Quelle behandelt qPCR, andere klassische PCR -> gemeinsamer PCR-Kern plus klar getrennte Erweiterung.

**Failure Case:** widersprüchliche Protokollparameter werden zu einem neuen Mittelwert kombiniert -> stoppen; Varianten getrennt halten.
