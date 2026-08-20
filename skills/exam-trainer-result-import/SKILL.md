---
name: exam-trainer-result-import
description: Übersetzt den von exam-trainer-framework exportierten Vertrag `etf-teach-review-evidence` in provider-neutrale, referenzierbare Laufzeitevidenz für `learning-assessment`. Verwenden nach ETF-Lern- oder Prüfungssitzungen; bewahrt ReviewEvent-Herkunft und IDs, importiert keine Scheduler-Interna und vergibt selbst keine Kompetenzstufe.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: draft
owners:
  - GithubLarsKomo
outputs:
  - learning-runtime-evidence.json
---

# Exam Trainer Result Import

## Zweck

Dieser Adapter bildet den Rückweg von ETF zu Skillz. Er normalisiert den von ETF definierten Evidence-Vertrag für die semantische Bewertung durch `learning-assessment`.

Normativer Eingangsformat-Identifier:

```text
etf-teach-review-evidence
```

Unterstützte Version: `1`.

Der Skill interpretiert **nicht**, ob eine Kompetenz nachgewiesen ist. Er bewahrt beobachtete Runtime-Evidenz und deren Provenance so, dass der Assessment-Skill sie gegen eine vorher definierte Spec bewerten kann.

## Eingabe

Ein ETF-v1-Evidence-Bundle mit mindestens:

- `format=etf-teach-review-evidence`,
- `version=1`,
- `missionId`,
- `catalogId`,
- `generatedAt`,
- Filter-/Scope-Angaben,
- `reviewEvents`,
- per-KnowledgeItem `summary`.

ReviewEvents dürfen unter anderem enthalten:

- `knowledgeItemId`,
- `questionVariantId`,
- `source=learning|exam`,
- `outcome=correct|partial|incorrect`,
- `answeredAt`,
- `responseTimeMs`,
- `confidence`,
- `masteryBefore`,
- `masteryAfter`.

## Eigentumsgrenzen

- ETF besitzt Roh-ReviewEvents, lokale Persistenz und Schedulerzustand.
- Dieser Skill besitzt nur die sichere Normalisierung des explizit exportierten Evidence-Bundles.
- `learning-assessment` besitzt die semantische Kompetenzbewertung.
- `learning-state` besitzt die spätere bestätigte Zustandsmutation.

Der Adapter darf keine verlorenen Scheduler-Felder rekonstruieren und keine nicht exportierte lokale Historie aus anderen Quellen ergänzen.

## Ausgabe

`learning-runtime-evidence.json`:

```json
{
  "schemaVersion": 1,
  "runtime": "exam-trainer-framework",
  "sourceFormat": "etf-teach-review-evidence",
  "sourceVersion": 1,
  "missionId": "...",
  "catalogId": "...",
  "generatedAt": "...",
  "scope": {
    "knowledgeItemIds": [],
    "questionVariantIds": [],
    "since": "...",
    "until": "..."
  },
  "knowledgeItems": [
    {
      "knowledgeItemId": "...",
      "summary": {
        "reviewCount": 0,
        "learningReviewCount": 0,
        "examReviewCount": 0,
        "correct": 0,
        "partial": 0,
        "incorrect": 0,
        "latestAnsweredAt": "..."
      },
      "reviewEvents": []
    }
  ],
  "evidenceRefs": []
}
```

`evidenceRefs` müssen stabile Referenzen auf die importierten Runtime-Ereignisse beziehungsweise das Bundle ermöglichen. Bestehende ETF-Event-IDs dürfen nicht ersetzt werden.

## Normalisierungsregeln

### 1. Scope bewahren

Übernimm den expliziten ETF-Filter-Scope. Erweitere ihn nicht stillschweigend auf andere KnowledgeItems, Varianten oder Zeiträume.

### 2. Events gruppieren, nicht umdeuten

Ordne jedes Event seinem `knowledgeItemId` zu. Bewahre insbesondere:

- konkrete `questionVariantId`,
- `source=learning|exam`,
- Outcome,
- Zeitstempel,
- vorhandene Unsicherheits-/Mastery-Signale.

`learning` und `exam` dürfen nicht zu einem ununterscheidbaren Gesamtscore verschmolzen werden.

### 3. ETF-Summary verifizieren

Die übernommene Summary muss zu den tatsächlich enthaltenen Events passen. Bei offensichtlicher Inkonsistenz kennzeichne den Import als konfliktbehaftet und reiche keine scheinbar saubere Evidenz weiter.

Der Adapter darf deterministische Zählungen zur Konsistenzprüfung wiederholen, aber keine neue Kompetenzmetrik erfinden.

### 4. Fehlende Evidenz sichtbar halten

Ein KnowledgeItem mit `reviewCount=0` bleibt als explizit angefragtes, aber unbeobachtetes Item erhalten. Leere Evidenz ist nicht dasselbe wie Fehlleistung.

### 5. Provider-neutral bleiben

Das Ausgabeformat darf keine Classic-/FSRS-Schedulerzustände, IndexedDB-Struktur oder ETF-UI-Sessions benötigen. Nur die explizit exportierte semantisch relevante Evidenz wird weitergegeben.

## Übergabe an learning-assessment

`learning-runtime-evidence.json` ist beobachtete Evidenz. `learning-assessment` muss sie gemeinsam mit `learning-assessment-spec.json` interpretieren.

Der Importer darf insbesondere **nicht** ausführen:

- `correct >= N -> application-demonstrated`,
- `masteryAfter=5 -> transfer-demonstrated`,
- `90% -> bestanden`,
- automatische Regression aufgrund einzelner Fehler.

Solche Schlüsse benötigen den semantischen Assessment-Kontext.

## Datenschutz

Importiere nur das von ETF für die konkrete Mission und den angefragten Scope exportierte Bundle. Keine Sessions, FSRS-Zustände, gesamten lokalen Backups oder andere Kataloghistorien hinzufügen.

## Fehlerbehandlung

- Unbekanntes Format oder Version: blockieren statt heuristisch interpretieren.
- Fehlende `missionId` oder `catalogId`: blockieren.
- Event außerhalb des deklarierten Scopes: Konflikt melden und nicht stillschweigend einbeziehen.
- Doppelte Event-ID mit widersprüchlichem Inhalt: Konflikt melden.
- Summary/Event-Widerspruch: Evidenz als konfliktbehaftet kennzeichnen.
- Fehlende ReviewEvents bei `reviewCount=0`: zulässig und als `not-observed` weiterreichbar.

## Formale Trainingsgrenze

Auch vollständig importierte ETF-Evidenz erzeugt keine Zertifizierung, QMS-Qualifikation oder formale Autorisierung. Sie ist lediglich Input für die pädagogische Kompetenzbewertung.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn das ETF-v1-Bundle scope-treu, event-treu und ohne Scheduler-/UI-Leakage in `learning-runtime-evidence.json` überführt wurde, Konflikte sichtbar sind und keine Kompetenzbewertung oder Zustandsmutation vorweggenommen wurde.
