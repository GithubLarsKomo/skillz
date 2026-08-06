---
name: external-stakeholder-questionnaire
description: Erzeugt fokussierte, priorisierte Fragen für einen externen Wissensinhaber, wenn der aktuelle Nutzer eine notwendige Information oder Entscheidung nicht selbst liefern kann. Verwenden, wenn fehlende Fakten gezielt bei Stakeholdern beschafft werden müssen; nicht für allgemeines Requirements-Grilling, Meeting-Vorbereitung oder das Nachverfolgen bereits zugesagter Antworten.
userFacing: true
implicitInvocation: true
category: productivity
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - stakeholder-questionnaire.json
  - stakeholder-questionnaire.md
lastEvaluated: 2026-08-06
---

# External Stakeholder Questionnaire

## Zweck und Grenze

Dieser Skill verwandelt eine klar benannte Informations- oder Entscheidungslücke in einen kompakten Fragebogen für genau den externen Wissensinhaber, der sie schließen kann. Er endet mit einem versandfertigen, nachvollziehbaren Fragenpaket und einer definierten Rücknahme der Antworten in den ursprünglichen Workflow.

Er recherchiert die Antwort nicht selbst, setzt kein Meeting an und verfolgt keine bereits ausgesandten Fragen. `round-based-requirements-grilling` bleibt für systematische Requirements-Elicitation mit dem aktuellen Nutzer zuständig; `meeting-preparation` bleibt für einen bestätigten Termin zuständig; `decision-and-follow-up-tracker` übernimmt offene Zusagen nach dem Versand.

## Trigger

Verwenden, wenn:

- eine notwendige Information ausdrücklich bei einer anderen Person oder Rolle liegt,
- der aktuelle Nutzer bereits erklärt hat, die Antwort nicht zu kennen,
- eine externe Freigabe, Präferenz, Zahl, Policy-Auskunft oder fachliche Entscheidung benötigt wird,
- mehrere offene Punkte an denselben Stakeholder gebündelt werden sollen,
- Antworten später strukturiert in Spec, Decision Record, Meeting Prep oder Projektarbeit übernommen werden sollen.

Nicht verwenden, wenn die Information aus vorhandenen Quellen recherchierbar ist oder der aktuelle Nutzer sie selbst beantworten kann.

## Kernregeln

- **Nicht weitergrillen, wenn der Wissensinhaber extern ist.** Eine bekannte Zuständigkeitslücke wird nicht durch weitere Spekulationen beim aktuellen Nutzer ersetzt.
- **Eine Entscheidung pro Frage.** Keine Mehrfachfragen, deren Teilantworten später unklar zuzuordnen sind.
- **Höchster Informationswert zuerst.** Fragen priorisieren, die Blocker oder Folgefragen auflösen.
- **Antwortbarkeit vor Vollständigkeit.** Nur Kontext geben, den der Empfänger zur belastbaren Antwort benötigt.
- **`unknown` ist zulässig.** Unsicherheit wird sichtbar gemacht statt zu einer Scheingenauigkeit gezwungen.
- **Keine eingebettete Präferenz.** Fragen dürfen die gewünschte Antwort nicht vorgeben.
- **Verwendungszweck sichtbar machen.** Der Stakeholder soll wissen, welche Entscheidung oder Arbeit von der Antwort abhängt.
- **Datensparsamkeit.** Nur notwendige Projekt- und Personenkontexte in den Fragebogen aufnehmen.

## Ablauf

### 1. Wissenslücke fixieren

Für jeden offenen Punkt erfassen:

- benötigte Tatsache oder Entscheidung,
- warum sie benötigt wird,
- welche Folgeentscheidung davon abhängt,
- was bereits bestätigt ist,
- was ausdrücklich unbekannt bleibt.

Falls die Lücke durch Recherche oder vorhandene Evidenz geschlossen werden kann, zuerst den passenden Research-/Evidence-Skill verwenden.

### 2. Empfänger und Autorität bestimmen

Nur bestätigten Empfängerkontext verwenden:

- Person oder Rolle,
- Zuständigkeitsbereich,
- bekannte Entscheidungskompetenz,
- relevanter Projektkontext.

Ist nicht klar, wer die Information besitzt, zuerst diese Zuständigkeit klären; keine Fragen an eine zufällige Person adressieren.

### 3. Fragen schneiden

Jede Frage soll genau eine verwertbare Information liefern. Für jede Frage definieren:

- `id`,
- konkrete Frage,
- warum sie benötigt wird,
- gewünschtes Antwortformat,
- zulässiges `unknown`,
- optional Antwortoptionen nur, wenn diese vollständig und neutral sind,
- Priorität,
- Abhängigkeiten zu späteren Fragen.

Eine Frage darf Beispiele enthalten, wenn sie Verständnis schaffen, aber keine bevorzugte Lösung suggerieren.

### 4. Reihenfolge optimieren

Sortiere nach:

1. Blocker für weitere Arbeit,
2. Fragen, die andere Fragen überflüssig machen können,
3. irreversible oder zeitkritische Entscheidungen,
4. Detailfragen.

Bedingte Folgefragen werden als solche markiert und nicht unnötig gestellt, wenn die Vorbedingung nicht erfüllt ist.

### 5. Antwortvertrag definieren

Für jeden Fragebogen festlegen:

- gewünschte Antwortfrist, falls bestätigt,
- zulässiger Kanal oder Format, falls relevant,
- ob Teilantworten akzeptiert werden,
- wie `unknown` oder „nicht zuständig“ behandelt wird,
- wo die Antwort später fachlich übernommen wird.

Keine Frist erfinden. Fehlt sie, bleibt sie offen.

### 6. Artefakte erzeugen

`stakeholder-questionnaire.json`:

```json
{
  "schemaVersion": 1,
  "recipient": {
    "nameOrRole": "...",
    "authority": "confirmed|partial|unknown",
    "context": "..."
  },
  "purpose": "...",
  "dependencies": ["..."],
  "questions": [
    {
      "id": "Q1",
      "priority": "blocking|high|normal|low",
      "question": "...",
      "whyNeeded": "...",
      "answerFormat": "free-text|yes-no|single-choice|number|date|reference",
      "allowUnknown": true,
      "options": [],
      "askIf": "always",
      "downstreamUse": "..."
    }
  ],
  "response": {
    "deadline": null,
    "partialAllowed": true,
    "unknownAllowed": true,
    "returnTo": "..."
  }
}
```

`stakeholder-questionnaire.md` enthält eine kurze Einleitung, die priorisierten Fragen und klare Antwortanweisungen. Der Text ist direkt versendbar, enthält aber keine erfundenen Kontaktdaten oder Versandbehauptungen.

### 7. Rücknahme vorbereiten

Definiere vor Versand, wie Antworten weiterverarbeitet werden:

- bestätigte Fakten zurück in Spec oder Projektkontext,
- wesentliche Entscheidungen in `decision-record`,
- neue Commitments oder ausstehende Antworten in `decision-and-follow-up-tracker`,
- meetingrelevante Informationen in `meeting-preparation`.

Antworten werden nicht automatisch als wahr oder autorisiert behandelt, wenn die Autorität des Empfängers unklar ist.

## Fehlerbehandlung

Stoppe oder korrigiere den Fragebogen, wenn:

- dieselbe Frage bereits beantwortet wurde,
- der aktuelle Nutzer erneut nach Fakten gefragt wird, die ausdrücklich nur ein externer Stakeholder kennt,
- mehrere unabhängige Entscheidungen in einer Frage vermischt sind,
- Optionen eine bevorzugte Antwort suggerieren oder nicht vollständig sind,
- vertrauliche Inhalte ohne Notwendigkeit an den Empfänger gelangen würden,
- eine Antwortfrist oder Entscheidungskompetenz erfunden wird,
- der Fragebogen bereits versandt wurde und die eigentliche Aufgabe jetzt Follow-up-Tracking ist.

## Komposition

Typische vorgelagerte Skills:

- `large-work-wayfinder` für erkannte externe Abhängigkeiten,
- `conversation-to-spec` für sichtbar gewordene offene Requirements,
- `research-to-evidence-note` wenn zunächst geklärt werden muss, ob die Antwort überhaupt extern eingeholt werden muss.

Typische nachgelagerte Skills:

- `decision-and-follow-up-tracker` nach Versand oder bei ausstehenden Antworten,
- `decision-record` für eine erhaltene wesentliche Entscheidung,
- `meeting-preparation` wenn Antworten in einen bestätigten Termin einfließen,
- `conversation-to-spec` beziehungsweise den ursprünglichen Fach-Skill zur Weiterverarbeitung bestätigter Antworten.

## Evaluation

### Happy Path

Ein Projekt benötigt drei Policies vom Informationssicherheitsverantwortlichen. Der aktuelle Nutzer kennt sie nicht. Der Skill bündelt drei getrennte, priorisierte Fragen, erlaubt `unknown`, erklärt den Downstream-Zweck und erfindet weder Antworten noch Frist.

### Grenzfall

Es ist bekannt, dass entweder Security oder Legal zuständig ist, aber nicht wer. Der Skill erstellt noch keinen autoritativen Fachfragebogen, sondern markiert die Empfängerautorität als ungeklärt und reduziert die erste externe Frage auf die Zuständigkeitsklärung.

### Fehlerfall

Ein Entwurf fragt gleichzeitig nach bevorzugtem Anbieter, Budget und Freigabe in einem Satz, bietet nur die gewünschte Anbieteroption an und setzt ohne Vorgabe eine Frist auf morgen. Der Skill zerlegt die Fragen, entfernt die Suggestion und lässt die Frist offen.

## Abschlusskriterien

Die Aufgabe ist abgeschlossen, wenn:

- jede Frage genau eine verwertbare Informations- oder Entscheidungslücke adressiert,
- Empfänger und bekannte Autorität explizit sind,
- Priorität und Downstream-Verwendung jeder Frage nachvollziehbar sind,
- `unknown` und Teilantworten korrekt behandelt werden,
- keine bereits beantworteten Fragen oder erfundenen Fristen enthalten sind,
- der Fragebogen direkt versendbar ist und seine Antworten ohne mündliche Zusatzinformation weiterverarbeitet werden können.

## Memory Path

At completion, extract only confirmed, reusable, non-sensitive learnings that remain useful beyond the current run. Current task state, open follow-ups, tool snapshots, speculative hypotheses, secrets, sensitive personal data and raw connector payloads remain run-only. Encode eligible candidates using `memory-candidate-handoff-v1` from `docs/MEMORY-PATH-CONTRACT.md`, preserve provenance and freshness, and pass the ephemeral handoff to `communication-memory-governance`. The producing skill does not persist memory and never claims persistence succeeded without confirmation from the memory layer.

