---
name: learning-source-arbitration
description: Bewertet mehrere Lernquellen hinsichtlich Unabhängigkeit, Autorität, Aktualität, Evidenznähe und gegenseitiger Bestätigung, ohne Mehrheitsvoten mit Wahrheit gleichzusetzen. Verwenden vor Multi-Video-Synthesen, wenn Claims zwischen Quellen konsolidiert oder Konflikte transparent eingeordnet werden müssen.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - multimodal-learning-analysis
outputs:
  - learning-source-arbitration.json
lastEvaluated: 2026-08-28
---

# Learning Source Arbitration

## Ziel

Mehrere Videos oder andere Lernquellen dürfen nicht durch bloßes Stimmenzählen zusammengeführt werden. Dieser Skill erzeugt eine nachvollziehbare Quellenbewertung für die spätere Synthese.

## Eingaben

Pro Quelle mindestens:

- Source-ID, Titel, Provider/Creator und URL;
- Veröffentlichungs-/Aktualitätsinformation soweit verfügbar;
- `learning-evidence.json` oder äquivalente evidenzgebundene Claims;
- Provenienz von Transcript/Frames;
- optionale Lizenz-/Rechteinformation;
- bekannte fachliche Autorität oder institutionelle Herkunft.

## Bewertungsdimensionen

Jede Quelle wird getrennt bewertet nach:

1. **Evidence proximity** — direkt demonstriert/gemessen vs. nur behauptet;
2. **Authority** — Primärquelle, Fachinstitution, Hersteller, Review-/Lehrquelle, Creator ohne überprüfbare Fachautorität;
3. **Independence** — echte unabhängige Quelle vs. Wiederholung/Abschreiben desselben Ursprungs;
4. **Recency relevance** — nur wenn Aktualität fachlich relevant ist;
5. **Specificity** — passt die Quelle exakt zum Claim/Use Case?;
6. **Internal confidence** — Qualität der zugänglichen Transcript-/Frame-Evidenz;
7. **Conflict-of-interest context** — dokumentieren, nicht pauschal abwerten.

Keine dieser Dimensionen wird zu einer scheinpräzisen universellen Wahrheitsscore-Zahl verdichtet. Der Output darf qualitative Klassen oder begründete Teil-Scores enthalten, muss aber die Einzelgründe erhalten.

## Claim-Level Arbitration

Für jeden normalisierten Claim:

- Quellen identifizieren, die ihn stützen;
- Quellen identifizieren, die ihm widersprechen;
- Quellen identifizieren, die nur scheinbar dasselbe sagen, aber anderen Scope/Definitionen nutzen;
- Abhängigkeiten zwischen Quellen markieren;
- Primär-/Sekundärbezug unterscheiden;
- zeitliche oder methodische Ursachen für Unterschiede markieren.

Zulässige Ergebniszustände:

- `convergent` — unabhängige Quellen stimmen im relevanten Scope überein;
- `qualified-convergence` — Kernaussage stimmt, Randbedingungen unterscheiden sich;
- `conflicted` — materieller Widerspruch bleibt offen;
- `single-source` — nur eine belastbare Quelle;
- `insufficient` — Evidenz reicht nicht für Synthese.

## Regeln

- Zwei voneinander abhängige Videos zählen nicht als zwei unabhängige Bestätigungen.
- Popularität, Likes, Views oder Kanalgröße sind kein Wahrheitsbeweis.
- Ein Hersteller kann für sein eigenes Produkt Primärquelle sein, aber interessengebundene Aussagen bleiben als Kontext sichtbar.
- Neuere Quelle schlägt ältere nicht automatisch; Aktualität muss für den Claim relevant sein.
- Ein Widerspruch darf nicht durch sprachliches Glätten verschwinden.
- Unterschiedliche Definitionen, Assays, Versionen, Populationen oder Settings werden zuerst harmonisiert, bevor ein Konflikt behauptet wird.
- Generierte Visuals bleiben außerhalb der Quellevidenz.

## Output

`learning-source-arbitration.json` enthält mindestens:

- Source registry;
- source relationships / dependency groups;
- claim-level support matrix;
- conflict sets;
- convergence status;
- rationale pro Claim;
- unresolved questions;
- recommended wording strength für die Synthese.

## Qualitätsfälle

**Happy Path:** drei unabhängige hochwertige Quellen erklären denselben Prozess mit kompatiblen Randbedingungen -> `convergent`.

**Edge Case:** zwei Videos nennen unterschiedliche Temperaturen, beziehen sich aber auf unterschiedliche Primer/Protokolle -> Scope-Differenz statt falschem Konflikt.

**Failure Case:** drei Reaktionsvideos kopieren dieselbe Ursprungsquelle und werden als drei unabhängige Belege gezählt -> stoppen und Abhängigkeit modellieren.
