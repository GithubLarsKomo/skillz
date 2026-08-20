---
name: teach
description: Orchestriert auf ausdrücklichen Wunsch einen zustandsbehafteten Lernprozess mit Lernmission, evidenzbasiertem Stoff, nachgewiesener Kompetenz, adaptivem nächsten Schritt und Übergaben an die Exam-Trainer-Lernruntime. Verwenden bei `/teach`, beim gezielten Erlernen eines Themas oder mit `/teach skill <skill-name>`; nicht für gewöhnliche Einzelerklärungen ohne Lernworkspace.
userFacing: true
implicitInvocation: false
category: productivity
version: 0.2.0
status: draft
owners:
  - GithubLarsKomo
requires:
  - learning-mission
  - learning-state
  - learning-next-step
  - learning-assessment-spec
  - learning-assessment
  - research-to-evidence-note
  - exam-trainer-catalog-builder
  - exam-trainer-result-import
outputs:
  - learning-mission.json
  - learning-state.json
  - learning-next-step.json
  - learning-practice-request.json
---

# Teach

## Zweck und Grenze

`teach` ist der explizite pädagogische Orchestrator für dauerhaftes Lernen über mehrere Sitzungen. Er verbindet Lernziel, belastbare Evidenz, Erklärung, Retrieval, Anwendung, Transfer und dokumentierte Kompetenz, ohne Fachlogik oder Scheduling selbst zu duplizieren.

Der Skill wird **nur explizit gestartet**. Eine normale Bitte wie „erkläre mir X“ erzeugt keinen persistenten Lernworkspace. Typische Aufrufe sind:

```text
/teach <topic>
/teach skill <skill-name>
/teach status
/teach review
```

## Normative Eigentumsgrenzen

- Fachliche Wahrheit bleibt bei spezialisierten Skillz-Skills und belastbaren Quellen.
- `research-to-evidence-note` strukturiert strittige oder mehrquellige Evidenz.
- `learning-mission` bestimmt Warum, Erfolgskriterien, Grenzen und Scope.
- `learning-state` hält semantisch nachgewiesene Kompetenz, Vorwissen, Fehlvorstellungen und Lücken.
- `learning-next-step` wählt die nächste pädagogische Herausforderung.
- `learning-assessment-spec` definiert, welche Evidenz für einen Kompetenzsprung erforderlich ist.
- `learning-assessment` interpretiert tatsächliche Lern-/Prüfungsevidenz.
- `exam-trainer-catalog-builder` übersetzt eine freigegebene Übungsabsicht in den ETF-Vertrag `etf-teach-catalog`; bei gewünschter gemeinsamer Wiederverwendung darf er nur einen approval-pflichtigen Hosted-Release-Kandidaten vorbereiten, keine Publikationsfreigabe erteilen.
- `exam-trainer-result-import` übersetzt den ETF-Vertrag `etf-teach-review-evidence` in provider-neutrale Laufzeitevidenz; er vergibt keine Kompetenzstufe.
- `structured-knowledge-artifact` kann bestätigte Mission-, Kompetenz- oder Referenzinhalte optional provider-neutral verpackt; `knowledge-view` und `knowledge-map-generator` dürfen diese projizieren, besitzen aber nicht die Lernsemantik.
- `exam-trainer-framework` (ETF) bleibt externe Runtime für Spaced Retrieval, adaptive Lernsitzungen, ReviewEvents, Prüfungen und den kontrollierten Hosted-Catalog-Publikationsprozess.

**Coverage ist kein Lernen.** Material darf nicht als beherrscht markiert werden, nur weil es erklärt, gelesen oder einmal gezeigt wurde.

## Kernworkflow

### 1. Lernmission herstellen oder laden

Nutze `learning-mission`, um ein beobachtbares Ziel festzulegen. Eine Mission muss mindestens beantworten:

- Warum soll das gelernt werden?
- Was kann der Lernende danach konkret tun?
- Welche Constraints gelten?
- Was ist ausdrücklich außerhalb des Scopes?

Ist bereits eine aktive Mission vorhanden, ändere sie nicht stillschweigend.

### 2. Vorwissen und belastbare Wissensbasis trennen

Erfasse vorhandenes Wissen zunächst als `priorKnowledge`, bis es ausreichend belegt ist. Für fachliche Claims nutze vorhandene Spezialskills oder, bei Recherchebedarf, `research-to-evidence-note`.

Parametrisches Modellwissen allein ist bei zeitabhängigen, regulierten oder strittigen Inhalten keine ausreichende Autorität.

### 3. Kompetenzpfad bilden

Zerlege das Ziel in beobachtbare Kompetenzen und Voraussetzungen. Bevorzuge wenige stabile Kompetenzen gegenüber vielen Kartenfragmenten.

Für `/teach skill <skill-name>` verwende den kanonischen Skillz-Index und die aktuelle `SKILL.md` des Zielskills. Berücksichtige deklarierte Abhängigkeiten, Outputs und Evaluationsfälle als Kandidaten für Anwendungs- und Transferaufgaben.

### 4. Nächsten Schritt wählen

Delegiere die Auswahl an `learning-next-step`. Zulässige nächste Schritte sind unter anderem:

- Erklärung,
- Worked Example,
- geführte Übung,
- Retrieval,
- Anwendung,
- Transfer,
- ETF-Lernsitzung,
- ETF-Prüfung,
- reale/praktische Aufgabe.

Die Schwierigkeit soll in der Zone der nächsten erreichbaren Herausforderung liegen: nicht trivial, aber mit dem vorhandenen Zustand plausibel lösbar.

### 5. Übung an ETF übergeben, wenn sinnvoll

Teach beschreibt **was** geübt beziehungsweise geprüft werden soll. ETF entscheidet **wann und wie** einzelne QuestionVariants wiederholt werden.

Für eine ETF-Übergabe erzeuge zunächst einen provider-neutralen `learning-practice-request.json` mit:

```json
{
  "schemaVersion": 1,
  "missionId": "...",
  "competencyIds": ["..."],
  "mode": "retrieval|application|transfer|exam",
  "assessmentSpecRef": "...",
  "sourceRefs": [],
  "runtime": "exam-trainer-framework",
  "publicationIntent": "draft|personal-local-runtime|shared-release-candidate"
}
```

`publicationIntent` ist optional. Ohne explizite Angabe gilt `draft`.

- `personal-local-runtime` erlaubt nur eine persönliche lokale Runtime-Freigabe nach den Gates des `exam-trainer-catalog-builder`; es ist keine formale Trainings- oder QMS-Freigabe.
- `shared-release-candidate` bedeutet nur, dass zusätzlich zum ETF-Katalog ein `etf-hosted-release-candidate.json` zur kontrollierten ETF-Release-Prüfung vorbereitet werden soll. Der Candidate MUSS `approvalRequired=true` tragen und darf weder `approved:true` noch einen erfundenen Registry-Hash oder eine bereits erfolgte Veröffentlichung behaupten.

Delegiere anschließend an `exam-trainer-catalog-builder`, der daraus den ETF-v1-Vertrag `etf-teach-catalog` und bei `shared-release-candidate` das nicht freigegebene Candidate-Artefakt erzeugt. Teach darf keine parallele ETF-Katalogstruktur, eigene Scheduling-Metadaten oder eine eigene Registry-Publikationslogik einführen.

### 5a. Shared Release nur als Kandidat vorbereiten

Wenn ein wiederverwendbarer Hosted Catalog gewünscht ist:

1. stelle sicher, dass fachliche Evidenz, Mission, Assessment-Spec und Provenance vollständig genug für einen Review-Kandidaten sind,
2. fordere `publicationIntent=shared-release-candidate` an,
3. bewahre alle offenen Inhalts-, Asset-, Provenance- oder Assessment-Probleme im Candidate,
4. übergib Katalog und Candidate an den kontrollierten ETF-Publikationsprozess,
5. behaupte erst nach dortiger expliziter Freigabe und technischer Validierung, dass ein Shared Release veröffentlicht ist.

Teach darf niemals selbst `approved:true` setzen, SHA-256-Registry-Hashes vorwegnehmen oder aus persönlicher Runtime-Fähigkeit eine Shared-Release-Freigabe ableiten.

### 6. Evidenz bewerten

Wenn der Lernende eine ETF-Übung oder Prüfung abgeschlossen hat, fordere von ETF nur den für Mission und KnowledgeItems benötigten `etf-teach-review-evidence`-Scope an. Übergib dieses Bundle zuerst an `exam-trainer-result-import` und anschließend gemeinsam mit der passenden `learning-assessment-spec.json` an `learning-assessment`.

Bei dialogischen oder realen Aufgaben ohne ETF kann `learning-assessment` die beobachtete Evidenz direkt bewerten.

Eine Prozentzahl allein darf keinen Kompetenzzustand bestimmen. Unterscheide mindestens:

- `introduced`,
- `retrieval-demonstrated`,
- `application-demonstrated`,
- `transfer-demonstrated`.

### 7. Lernzustand aktualisieren

`learning-state` übernimmt nur belegte Änderungen. Lernrecords entstehen bei tatsächlich nachgewiesenem Verständnis, relevantem Vorwissen, korrigierter Fehlvorstellung oder einer begründeten Missionsänderung.

Bestätigte semantische Artefakte können anschließend über `structured-knowledge-artifact` adressierbar verpackt und über `knowledge-view` oder `knowledge-map-generator` projiziert werden. Diese optionale Verpackung verändert weder Kompetenzbewertung noch Lernzustand.

### 8. Schleife fortsetzen oder sauber beenden

Nach jedem substantiellen Schritt:

1. Zustand aktualisieren,
2. offene Lücken bestimmen,
3. nächsten Schritt berechnen,
4. Mission gegen Erfolgskriterien prüfen.

Beende eine Mission nicht aufgrund bloßer Stoffabdeckung.

## Status- und Review-Modus

### `/teach status`

Zeige knapp:

- aktive Mission,
- nachgewiesene Kompetenzen nach Level,
- offene Fehlvorstellungen/Lücken,
- zuletzt belegte Entwicklung,
- vorgeschlagenen nächsten Schritt.

### `/teach review`

Nutze fällige oder schwach belegte Kompetenzen als semantischen Review-Fokus. ETF bleibt Scheduler einzelner Retrieval-Items; Teach darf keine zweite Fälligkeitslogik etablieren.

## Datenschutz und Persistenz

- Missions- und Kompetenzzustand darf im Lernworkspace persistent sein.
- Rohdaten privater Connectoren, Zugangsdaten und unnötige personenbezogene Daten bleiben laufzeitgebunden.
- Dauerhafte globale Kommunikationspräferenzen gehören zu `communication-memory-governance`, nicht in den Kompetenzzustand.
- ETF-Lernerhistorie bleibt standardmäßig lokal in ETF; Teach fordert nur den für semantische Bewertungen benötigten Evidence-Scope an.
- Hosted-Release-Kandidaten enthalten Lerninhalt und notwendige Provenance, aber keine Learner-History, ReviewEvents, Scheduler-/FSRS-Zustände oder private Missionsdaten, die für die gemeinsame Veröffentlichung nicht erforderlich sind.

## Formale Trainingsgrenze

Ein Teach-/ETF-Ergebnis darf nicht eigenständig als formale Qualifikation, QMS-Schulung, Autorisierung oder Zertifizierung ausgegeben werden. Dafür ist ein separat kontrollierter Trainingsrecord-Workflow mit zuständiger Autorität erforderlich.

Ebenso ist ein `shared-release-candidate` keine organisatorische oder technische Publikationsfreigabe. Die tatsächliche Hosted-Veröffentlichung gehört zum kontrollierten ETF-Release-Prozess.

## Fehlerbehandlung

- Fehlt belastbare Evidenz, kennzeichne die Lücke und lehre die Aussage nicht als gesicherte Tatsache.
- Widerspricht neue Evidenz dem bisherigen Lernzustand, bewahre die Provenance und korrigiere den Zustand explizit.
- Ist ETF nicht verfügbar, kann Teach mit dialogischen Retrieval-/Transferaufgaben fortfahren, darf aber keine ETF-ReviewEvents erfinden.
- Ist ein ETF-Bundle unbekannter Version oder scope-inkonsistent, lasse es vom Adapter blockieren statt es heuristisch umzudeuten.
- Ist die Mission zu breit, schneide ein kohärentes Lernziel statt beliebig viele Themen parallel zu verfolgen.
- Verlangt ein Shared-Release-Aufruf unmittelbare Publikation ohne ETF-Release-Review, erzeuge höchstens einen nicht freigegebenen Candidate und weise die fehlende Freigabe explizit aus.

## Abschlusskriterien

Ein Teach-Zyklus ist abgeschlossen, wenn die aktive Mission dokumentiert ist, verwendete fachliche Claims nachvollziehbar sind, der aktuelle Kompetenzzustand nur nachgewiesene Fähigkeiten enthält, der nächste Schritt begründet ist und jede Runtime-Übergabe einen expliziten portablen Vertrag besitzt. Bei gewünschter gemeinsamer Wiederverwendung darf ein approval-pflichtiger Hosted-Release-Kandidat vorbereitet sein; ein tatsächliches Shared Release gilt erst nach expliziter ETF-/Maintainer-Freigabe und technischer Registry-Validierung als veröffentlicht.
