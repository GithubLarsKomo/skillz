# Precision Writing & Author Voice — SPEC v1

Status: implementation baseline
Date: 2026-08-20
Repository: `GithubLarsKomo/skillz`

## 1. Zweck

Ein komponierbarer Skill-Satz soll deutsche und englische Reports, Memos und sonstige Sachtexte sprachlich präzise überarbeiten. Primärziel ist nicht die Umgehung von KI-Detektoren, sondern in dieser Reihenfolge: **semantic fidelity → epistemic precision → genre fidelity → authorial fidelity → linguistic quality**.

Das System soll typische generische LLM-Prosa erkennen, ohne daraus eine Autorschaftsbehauptung abzuleiten, und Texte in drei Intensitäten überarbeiten: `light`, `author`, `editorial`.

## 2. Nicht-Ziele

- kein AI-Detector oder Klassifikator für menschliche/KI-Autorschaft
- keine Optimierung gegen GPTZero oder ähnliche Detektoren
- keine künstlichen Fehler, Zufallsvariation oder "perplexity/burstiness"-Manipulation
- keine pauschalen Verbotslisten einzelner Wörter
- keine Erfindung, Erweiterung oder Abschwächung fachlicher Claims
- keine Speicherung persönlicher Rohtexte im öffentlichen Skill-Repository

## 3. Bestätigte Stilentscheidungen

### 3.1 Global

- professionell, analytisch und direkt; Direktheit meist moderat, bei eindeutiger Evidenz deutlich
- Fachtermini bewusst wiederholen, wenn Synonyme Referenzklarheit mindern
- Satzrhythmus darf deutlich variieren; kurze Sätze sind zulässig
- Absatzlogik bevorzugt **Behauptung → Evidenz → Konsequenz**, ohne obligatorische Einleitungs- oder Fazitsätze
- Wertungswörter wie `key`, `significant`, `important`, `entscheidend`, `wesentlich`, `relevant` nur mit konkreter Begründung
- Redundanz entfernen; terminologische Wiederholung gilt nicht automatisch als Redundanz
- Listen nur für tatsächlich gleichrangige Elemente
- vorhandene Kapitelstruktur im Normalfall erhalten; Absatzstruktur darf verbessert werden

### 3.2 Englisch

- Zielvariante abhängig von Adressat: international, US oder UK
- Executive-Standard: klare analytische Sätze, z. B. `The current evidence supports X as the lead option.`
- Empfehlungen bevorzugt als direkte sachliche Feststellung, z. B. `X is the preferred option.`
- Unsicherheit epistemisch formulieren: `The available information does not allow X to be assessed.` statt unbelegtem `X is unknown.`
- Passiv beibehalten, wenn Prozess oder Ergebnis wichtiger als Akteur ist
- Hedging reduzieren, wenn die Evidenz eine klarere Aussage trägt; wissenschaftlich notwendige Unsicherheit bleibt erhalten
- Kontraktionen in formellen Reports vermeiden; in informelleren Memos optional

### 3.3 Deutsch

- natürliche Fachsprache statt Verwaltungs- oder übermäßigem Nominalstil
- Nominalisierungen deutlich reduzieren, etablierte Fachnomina erhalten
- idiomatische deutsche Informationsstruktur und Vorfeldvariation zulassen; keine künstliche SVO-Gleichförmigkeit
- Semikolons vermeiden
- Doppelpunkte selten
- Gedankenstriche sparsam
- Klammern für technische Zusatzinformation zulässig

## 4. Architektur

### 4.1 `author-voice-profiler`

Erzeugt aus authentischen Referenztexten ein `author-voice-profile.json` und optional eine lesbare Markdown-Zusammenfassung. Profile sind nach Sprache und Genre trennbar, insbesondere `de/report`, `de/memo`, `de/general`, `en/report`, `en/memo`, `en/general`.

Der Skill extrahiert beobachtbare Stilmerkmale und bestätigt keine psychologischen oder demografischen Eigenschaften. Rohkorpora bleiben außerhalb des öffentlichen Repositories.

### 4.2 `llm-prose-pattern-audit`

Analysiert einen Text auf redaktionell relevante Muster wie generische Signifikanz, Pseudoanalyse, unnötiges Hedging, rhetorische Templates, elegante Variation, Nominalisierung, Konnektorübergebrauch, syntaktische Gleichförmigkeit, englisch beeinflusste deutsche Informationsstruktur, Format-Templates und Redundanz.

Output: `prose-audit.json` und optional `prose-audit.md`.

Die Befunde sind Editing-Signale, keine Autorschaftsklassifikation.

### 4.3 `precision-language-rewriter`

Überarbeitet Text anhand von:

- `language`: `de|en`
- `genre`: `report|memo|general`
- `mode`: `light|author|editorial`
- `audience`: `expert|management|mixed|public`
- `englishVariant`: `international|us|uk` bei Englisch
- optional `author-voice-profile.json`
- optional `prose-audit.json`
- optional Fidelity Lock aus Claims, Zahlen, Referenzen, Modalität und Terminologie

`light` entfernt generische und unnötig glatte Muster ohne größeren Stilumbau. `author` richtet zusätzlich am bestätigten Voice Profile aus. `editorial` darf Absätze stärker rekonstruieren, Reihenfolgen optimieren und Redundanz entfernen, aber keine neue Sachinformation erzeugen.

### 4.4 `rewrite-fidelity-verifier`

Vergleicht Quelle und Rewrite mindestens auf:

- Zahlen, Einheiten und Zeitangaben
- Produkt-, Plattform- und Fachbegriffe
- Literaturreferenzen und URLs
- Negationen
- Modalität, Hedging und Confidence
- Bedingungen und Ausnahmen
- Ursache-Wirkungs-Beziehungen
- fachliche Claims

Jede Änderung wird als `preserved`, `clarified`, `potentially_changed`, `added` oder `removed` klassifiziert. Ein neu hinzugefügter fachlicher Claim ist ein Hard Fail.

### 4.5 `precision-writing-revision`

Dünner Orchestrator:

`source → prose audit → fidelity lock → rewrite → fidelity verification → optional correction pass → final text`

Er dupliziert keine Fachlogik der vier Teil-Skills.

## 5. Pattern-Taxonomie

### 5.1 Sprachübergreifend

- `generic-significance`
- `pseudo-analysis`
- `unnecessary-hedging`
- `rule-of-three`
- `negative-parallelism`
- `elegant-variation`
- `connector-overuse`
- `syntactic-uniformity`
- `format-template`
- `unsupported-evaluation`
- `redundancy`

### 5.2 Deutsch zusätzlich

- `nominalization-density`
- `subject-initial-uniformity`
- `english-interference-de`
- `bureaucratic-register`

### 5.3 Englisch zusätzlich

- `inflated-academic-register`
- `participial-pseudo-analysis`
- `template-transition-density`

Die Taxonomie liegt ausführlicher in `skills/llm-prose-pattern-audit/references/pattern-taxonomy.md`.

## 6. Deterministische Metriken

`llm-prose-pattern-audit/scripts/style_metrics.py` liefert reproduzierbare Beobachtungen wie Satzlängenmittel und -streuung, Semikolon-/Doppelpunkt-/Gedankenstrichdichte, Listenhäufigkeit, Satzanfangs-Konnektoren, Hedging- und Wertungswortdichte sowie einfache sprachspezifische Heuristiken.

Die Werte sind keine Qualitätsziele. Sie werden mit Genre- oder Author-Baselines verglichen und dienen nur als Abweichungsindikatoren.

`rewrite-fidelity-verifier/scripts/fidelity_tokens.py` prüft konservativ die Erhaltung von Zahlen, Einheiten, DOI/PMID/URLs, nummerierten Referenzen und optional vorgegebenen Fachtermini. Semantische Fidelity bleibt zusätzlich LLM-/Review-Aufgabe.

## 7. Datenschutz und Persistenz

- persönliche Rohtexte und vertrauliche Reports werden nicht als Repo-Assets abgelegt
- Style Profiles enthalten abstrahierte Merkmale, keine unnötigen Textpassagen
- persistente persönliche Profile folgen `communication-memory-governance`
- sensible oder vertrauliche Projektinhalte bleiben run-only, sofern keine explizit zulässige Ablage besteht

## 8. Forschungsbasis

Die Taxonomie verwendet als Ausgangspunkt Wikipedia `Wikipedia:Signs of AI writing`, ergänzt um neuere Forschung zu überrepräsentiertem akademischem Vokabular, Stilimitation, Post-Editing und deutschsprachiger LLM-Syntax. Der Skill übernimmt daraus Prinzipien und eigene Formulierungen, keine langen Quellpassagen.

Relevante Startquellen:

- https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- https://aclanthology.org/2025.coling-main.426/
- https://aclanthology.org/2025.findings-emnlp.532/
- https://aclanthology.org/2026.acl-long.2030/
- https://ai-ling.publia.org/ai_ling/article/view/36
- https://www.degruyter.com/document/doi/10.1515/glot-2025-2011/html
- https://doi.org/10.1016/j.patter.2023.100779

## 9. Anforderungen und Akzeptanzkriterien

- **PW-01:** Audit und Rewrite dürfen keine KI-Autorschaft behaupten. Akzeptiert, wenn alle Befunde als redaktionelle Muster formuliert sind.
- **PW-02:** `author` benötigt ein explizites Author-Voice-Profil oder fällt transparent auf genrebezogene Regeln zurück.
- **PW-03:** Rewriter verändert keine Zahlen, Quellen oder fachlichen Claims ohne Kennzeichnung. Akzeptiert, wenn der Fidelity-Verifier jede relevante Abweichung sichtbar macht.
- **PW-04:** Deutsch und Englisch besitzen getrennte Regeln. Akzeptiert, wenn deutsche Syntax-/Nominalstil-Prüfungen nicht blind auf Englisch angewandt werden und umgekehrt.
- **PW-05:** Die drei Rewrite-Modi unterscheiden sich im zulässigen Eingriff, nicht in der Faktenlage.
- **PW-06:** Fachterminologie gewinnt gegen stilistische Synonymvariation, wenn Referenzklarheit betroffen ist.
- **PW-07:** Deterministische Metriken sind diagnostisch und nicht als AI-Score oder starres Stilziel zu verwenden.
- **PW-08:** Jeder Skill besitzt Happy-Path-, Edge- und Failure-Evaluation.
- **PW-09:** Der Orchestrator bleibt dünn und verweist auf die vier Fach-Skills.

## 10. Entscheidungsregister

- D-01: Ziel ist Precision Writing, nicht Detector Evasion.
- D-02: Fünf kleine Skills statt eines monolithischen Humanizers.
- D-03: Getrennte DE/EN- und Genreprofile.
- D-04: Drei Modi `light|author|editorial`.
- D-05: Claim- und Zahlen-Fidelity hat Vorrang vor Stil.
- D-06: Direkter, analytischer Ton; Empfehlungen als sachliche Feststellung.
- D-07: Semikolons vermeiden, Doppelpunkte selten, Gedankenstriche sparsam.
- D-08: Absätze folgen bevorzugt Behauptung → Evidenz → Konsequenz.

## 11. Konsistenzbericht

Die bestätigten Präferenzen sind untereinander konsistent. Der einzige bewusste Trade-off liegt zwischen Direktheit und wissenschaftlichem Hedging; er wird durch die Regel gelöst, dass Evidenzstärke und epistemische Präzision Vorrang vor Kürze haben. Author Voice darf Fidelity und fachliche Terminologie niemals überschreiben.

## 12. Sequenzierung

1. Taxonomie und Audit
2. Author-Voice-Profil
3. Rewriter
4. Fidelity-Verifier
5. Orchestrator
6. Capability-/Adapter-Artefakte durch bestehende Repo-Generatoren aktualisieren
