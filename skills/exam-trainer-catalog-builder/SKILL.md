---
name: exam-trainer-catalog-builder
description: Übersetzt eine explizite Teach-Lernübergabe mit Lernmission, Kompetenzbezug, Assessment-Spec und belegten Inhalten in den portablen ETF-Vertrag `etf-teach-catalog` mit stabilen KnowledgeItems und QuestionVariants. Verwenden, wenn Skillz Lernmaterial an exam-trainer-framework übergeben oder einen kontrollierten Shared-Release-Kandidaten vorbereiten soll; recherchiert keine Fachwahrheit, schedult nichts und erzeugt keine formale Trainings- oder Publikationsfreigabe.
userFacing: false
implicitInvocation: true
version: 0.2.0
status: draft
owners:
  - GithubLarsKomo
requires:
  - learning-mission
  - learning-assessment-spec
outputs:
  - etf-teach-catalog.json
  - etf-hosted-release-candidate.json
---

# Exam Trainer Catalog Builder

## Zweck

Dieser Adapter übersetzt semantisch vorbereitete Teach-Inhalte in den von `exam-trainer-framework` (ETF) definierten portablen Katalogvertrag. Er besitzt weder Fachwahrheit noch Lernzustand noch Scheduling. Bei ausdrücklich gewünschter gemeinsamer Wiederverwendung darf er zusätzlich einen **Release-Kandidaten** für den kontrollierten ETF-Hosted-Publishing-Prozess vorbereiten; er besitzt dabei keine Release-Autorität.

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
- explizite Veröffentlichungsabsicht `draft|personal-local-runtime|shared-release-candidate`.

Fehlt fachliche Evidenz, delegiere an den zuständigen Fachskill beziehungsweise `research-to-evidence-note`; erfinde sie nicht im Adapter.

## Eigentumsgrenzen

- Teach bestimmt Lernmission, Kompetenzpfad und Übungsabsicht.
- Spezialskills/Evidenzquellen bestimmen fachliche Claims.
- Dieser Skill bestimmt nur die ETF-Katalogprojektion und optional die Beschreibung eines noch nicht freigegebenen Hosted-Release-Kandidaten.
- ETF bestimmt Scheduling, Runtime, ReviewEvents, Exam-Mechanik und die technische Hosted-Release-Validierung.
- Der kontrollierte ETF-Publikationsprozess beziehungsweise zuständige Maintainer bestimmt, ob ein Shared Release tatsächlich freigegeben wird.
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

## Shared-Release-Kandidat

Bei `publicationIntent=shared-release-candidate` erzeuge zusätzlich `etf-hosted-release-candidate.json`. Dieses Artefakt ist eine Übergabe an den ETF-Publikationsprozess und **keine Freigabe**.

Kanonische Mindestform:

```json
{
  "schemaVersion": 1,
  "catalogId": "teach-<mission-id>",
  "version": "1.0.0",
  "title": "...",
  "sourceArtifact": "etf-teach-catalog.json",
  "status": "release-candidate",
  "approvalRequired": true,
  "requestedRegistry": "etf-hosted-catalog-registry-v1",
  "provenance": {
    "missionId": "...",
    "sourceSkill": "...",
    "sourceRefs": [],
    "sourceCommit": "..."
  },
  "openIssues": []
}
```

Regeln:

- `approvalRequired` MUSS `true` sein.
- Der Kandidat darf **kein** `approved:true`, keinen `contentHash` und keinen fertigen Registry-Eintrag vortäuschen; Hash und Release-Artefakte entstehen erst aus dem ETF-Build des tatsächlich freigegebenen Runtime-Katalogs.
- Der Candidate darf nicht behaupten, bereits `released` oder gehostet zu sein.
- Offene Inhalts-, Provenance-, Asset- oder Assessment-Probleme müssen in `openIssues` erhalten bleiben und blockieren die Empfehlung zur Freigabe.
- Der Candidate darf eine gewünschte semantische Version benennen, aber ETF MUSS beim späteren Publishing die exakte Runtime-ID und -Version erneut gegen den autoritativen Release-Plan prüfen.
- Aus einer Teach-, Anki- oder persönlichen ETF-Freigabe folgt niemals automatisch eine Shared-Release-Freigabe.

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
- keine zweite Scheduler- oder Progress-Semantik wurde eingebettet,
- bei `shared-release-candidate`: `approvalRequired=true`, kein `approved:true`, kein vorweggenommener Registry-Hash und alle offenen Release-Blocker explizit erhalten.

## Fehlerbehandlung

- Fehlt die Mission oder stimmt `missionId` zwischen Inputs nicht überein, Ausgabe blockieren.
- Fehlt eine referenzierte Assessment-Spec, keine transfer-/application-spezifische Variante als ausreichend geprüft ausgeben.
- Sind Quellen widersprüchlich oder ungeklärt, zurück an Evidenz-/Fachskill routen.
- Sind IDs inkonsistent, nicht stillschweigend neue IDs erzeugen.
- Ist nur Draft-Qualität erreicht, `status=draft` beibehalten.
- Fordert ein Caller bei einem Shared-Release-Kandidaten `approved:true`, einen erfundenen SHA-256-Hash oder unmittelbare Registry-Publikation, verweigere diese Felder und route zur kontrollierten ETF-Release-Freigabe.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn ein ETF-v1-kompatibler `etf-teach-catalog` mit stabiler semantischer KnowledgeItem-Identität, passenden QuestionVariants und vollständiger Teach-Provenance vorliegt, ohne Fachwahrheit, Scheduling, Kompetenzbewertung oder formale Trainingsautorität zu duplizieren. Bei ausdrücklich angefordertem Shared Release darf zusätzlich ein nicht freigegebener, approval-pflichtiger Release-Kandidat vorliegen; die tatsächliche Veröffentlichung bleibt ETF-/Maintainer-Autorität.
