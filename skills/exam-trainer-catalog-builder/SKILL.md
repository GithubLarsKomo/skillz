---
name: exam-trainer-catalog-builder
description: Übersetzt eine explizite Teach-Lernübergabe mit Lernmission, Kompetenzbezug, Assessment-Spec und belegten Inhalten in den portablen ETF-Vertrag `etf-teach-catalog` mit stabilen KnowledgeItems und QuestionVariants. Verwenden, wenn Skillz Lernmaterial an exam-trainer-framework übergeben soll; recherchiert keine Fachwahrheit, schedult nichts und erzeugt keine formale Trainingsfreigabe.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: draft
owners:
  - GithubLarsKomo
requires:
  - learning-mission
  - learning-assessment-spec
outputs:
  - etf-teach-catalog.json
---

# Exam Trainer Catalog Builder

## Zweck

Dieser Adapter übersetzt semantisch vorbereitete Teach-Inhalte in den von `exam-trainer-framework` (ETF) definierten portablen Katalogvertrag. Er besitzt weder Fachwahrheit noch Lernzustand noch Scheduling.

Normativer Zielformat-Identifier:

```text
etf-teach-catalog
```

Version für diesen Skill: `1`.

## Eingaben

Mindestens:

- `learning-practice-request.json`,
- passende `learning-mission.json`,
- referenzierte `learning-assessment-spec.json`,
- belegte Kompetenz-/Konzeptinhalte mit stabilen Source-Refs.

Optional:

- aktueller `learning-state.json` zur Vermeidung bereits ungeeigneter oder redundanter Übungsziele,
- `sourceSkill` und `sourceCommit` bei `/teach skill <skill-name>`,
- explizite Veröffentlichungsabsicht `draft|personal-local-runtime`.

Fehlt fachliche Evidenz, delegiere an den zuständigen Fachskill beziehungsweise `research-to-evidence-note`; erfinde sie nicht im Adapter.

## Eigentumsgrenzen

- Teach bestimmt Lernmission, Kompetenzpfad und Übungsabsicht.
- Spezialskills/Evidenzquellen bestimmen fachliche Claims.
- Dieser Skill bestimmt nur die ETF-Katalogprojektion.
- ETF bestimmt Scheduling, Runtime, ReviewEvents und Exam-Mechanik.
- `learning-assessment` bewertet spätere Evidenz; dieser Skill markiert keine Kompetenz als nachgewiesen.

## Kanonische Ausgabe

`etf-teach-catalog.json` MUSS dem ETF-v1-Vertrag entsprechen:

```json
{
  "format": "etf-teach-catalog",
  "version": 1,
  "catalog": {
    "catalogId": "teach-<mission-id>",
    "title": "...",
    "version": "1.0.0",
    "createdAt": "...",
    "updatedAt": "...",
    "cards": [],
    "origin": {
      "type": "skillz-teach",
      "missionId": "...",
      "sourceSkill": "...",
      "sourceRefs": [],
      "sourceCommit": "..."
    },
    "knowledgeItems": []
  }
}
```

`cards` MUSS vorhanden sein und darf für native Teach-Kataloge leer sein. Native Teach-Inhalte werden primär über `KnowledgeItem -> QuestionVariants` modelliert.

## KnowledgeItem-Regeln

Ein `KnowledgeItem` repräsentiert genau ein dauerhaftes semantisches Lernobjekt, nicht eine einzelne Formulierung einer Frage.

Jedes Item benötigt mindestens:

- stabile `id`,
- `version`,
- `status`,
- `topicId`,
- belastbare `source`,
- `changedAt`,
- `tags`,
- mindestens eine passende `QuestionVariant`,
- `origin.type=skillz-teach`,
- `origin.missionId`.

Nutze vorhandene Kompetenz-/Konzept-IDs als Identitätsbasis. Erzeuge keine neue KnowledgeItem-ID nur deshalb, weil eine zweite Frageformulierung benötigt wird.

## QuestionVariants

Mehrere `QuestionVariants` dürfen dasselbe KnowledgeItem aus unterschiedlichen Perspektiven prüfen, zum Beispiel:

- Retrieval,
- repräsentative Anwendung,
- Edge Case,
- Transfer.

Jede Variante referenziert dieselbe `knowledgeItemId`, besitzt aber eine eigene stabile `id`. Die Variante darf Schwierigkeit, Prompt, Fragetyp, Antwortkriterien und variantenspezifische Provenance tragen.

Fragmentiere einen semantischen Lerngegenstand nicht in mehrere KnowledgeItems, nur um Wiederholungsvariation zu erzeugen.

## Assessment-Bezug

QuestionVariants müssen zur vorliegenden Assessment-Spec passen. Ein Variant-Set darf keine höhere Kompetenzklasse behaupten, als Aufgabe und Unterstützungsgrad tatsächlich prüfen können.

Beispiele:

- freie Reproduktion kann Retrieval prüfen,
- repräsentativer Fall kann Anwendung prüfen,
- ausreichend neuer Fall kann Transfer prüfen.

Ein hoher erwarteter Score ersetzt diesen semantischen Abgleich nicht.

## Provenance

Übernimm verfügbare Provenance explizit:

- `missionId`,
- `sourceSkill`,
- `sourceRefs`,
- `sourceCommit`.

Eine Quelle muss auf das tatsächlich gelehrte beziehungsweise geprüfte Konzept zeigen. Kopiere keine privaten Connector-Rohdaten, Secrets oder unnötige personenbezogene Informationen in den Katalog.

## Status und lokale Veröffentlichung

Default ist `draft`.

`released` ist für durch Teach erzeugtes Material nur zulässig, wenn:

1. die Übergabe ausdrücklich `personal-local-runtime` verlangt,
2. fachliche Inhalte nachvollziehbar belegt sind,
3. KnowledgeItem-/QuestionVariant-IDs konsistent sind,
4. die Assessment-Spec zur Variantenklasse passt,
5. keine offene kritische Inhaltslücke bekannt ist.

`released` bedeutet hier lediglich **runtime-fähiger persönlicher ETF-Inhalt**. Es ist keine formale Trainingsfreigabe, keine QMS-Genehmigung und keine Zertifizierung. Wiederverwendbare oder organisatorisch freigegebene Kataloge benötigen den kontrollierten ETF-Publikationsprozess.

## Qualitätsgates

Vor Ausgabe prüfen:

- `format == etf-teach-catalog` und `version == 1`,
- `catalog.cards` existiert,
- KnowledgeItem-IDs sind eindeutig,
- jede QuestionVariant-ID ist eindeutig,
- jede Variante verweist auf das umgebende KnowledgeItem,
- jedes runtime-fähige Item besitzt mindestens eine runtime-fähige Variante,
- Mission- und Source-Provenance sind vorhanden,
- keine Fachbehauptung wurde nur für die Adapterübersetzung erfunden,
- keine zweite Scheduler- oder Progress-Semantik wurde eingebettet.

## Fehlerbehandlung

- Fehlt die Mission oder stimmt `missionId` zwischen Inputs nicht überein, Ausgabe blockieren.
- Fehlt eine referenzierte Assessment-Spec, keine transfer-/application-spezifische Variante als ausreichend geprüft ausgeben.
- Sind Quellen widersprüchlich oder ungeklärt, zurück an Evidenz-/Fachskill routen.
- Sind IDs inkonsistent, nicht stillschweigend neue IDs erzeugen.
- Ist nur Draft-Qualität erreicht, `status=draft` beibehalten.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn ein ETF-v1-kompatibler `etf-teach-catalog` mit stabiler semantischer KnowledgeItem-Identität, passenden QuestionVariants und vollständiger Teach-Provenance vorliegt, ohne Fachwahrheit, Scheduling, Kompetenzbewertung oder formale Trainingsautorität zu duplizieren.
