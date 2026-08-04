---
name: inbox-action-triage
description: Klassifiziert eine abgegrenzte Menge bereits geladener Nachrichten nach Dringlichkeit und Handlungsbedarf und leitet überprüfbare nächste Aktionen ab. Verwenden, wenn Inbox-Nachrichten in urgent, reply-soon, waiting, delegated, FYI/archive oder needs-context geordnet werden sollen, ohne Gmail-/Outlook-Connectorlogik oder Mailbox-Mutationen zu duplizieren.
userFacing: true
category: productivity
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - inbox-triage.json
  - inbox-triage.md
lastEvaluated: 2026-08-02
---

# Inbox Action Triage

## Zweck und Grenze

Verdichte eine **begrenzte, bereits zugängliche Nachrichtenmenge** in eine nachvollziehbare Aktionssicht. Der Skill entscheidet über Priorität und nächste Schritte; er ist **kein Mailbox-Connector, Suchclient, Sender, Archivierer, Labeler, Forwarder oder Scheduler**.

Mailbox-Tools liefern Nachrichten/Threads und führen gewünschte Mutationen separat aus. Dieser Skill darf niemals aus einer geplanten Aktion ableiten, dass eine Nachricht tatsächlich beantwortet, archiviert, weitergeleitet oder delegiert wurde.

## Trigger

Verwenden, wenn Nachrichten nach Handlungsbedarf sortiert, Antwortbedarf erkannt oder wartende/delegierte Vorgänge sichtbar gemacht werden sollen.

Nicht verwenden für reine Volltextsuche, das Schreiben einer konkreten Antwort oder Mailbox-Mutationen ohne vorherige Triage.

## Voraussetzungen

Vor der Klassifikation fixieren:

1. betrachteten Nachrichten-/Thread-Scope und Stichtag,
2. stabile Referenz pro Nachricht/Thread,
3. Absender, Zeit, Betreff und relevanten Inhalt soweit verfügbar,
4. bekannte Fristen, Zusagen oder vorherige Aktionen,
5. Informationslücken, wenn Kontext nur teilweise geladen wurde.

Fehlenden Kontext nicht durch Vermutungen ersetzen.

## Klassen

Jeder Thread erhält genau eine primäre Klasse:

- `urgent`: konkrete zeitkritische Aktion oder erhebliches Risiko bei Verzögerung,
- `reply-soon`: Antwort/Aktion erforderlich, aber nicht akut,
- `waiting`: nächste sinnvolle Aktion liegt bei einer anderen Partei; eigener Follow-up-Zeitpunkt kann relevant sein,
- `delegated`: Verantwortung wurde nachweisbar an eine andere Person/Funktion übergeben,
- `fyi-archive`: keine erkennbare Aktion; Information kann zur Kenntnis genommen beziehungsweise später extern archiviert werden,
- `needs-context`: relevante Entscheidung ist mit den geladenen Informationen nicht belastbar möglich.

Eine Klasse ist eine **Triage-Empfehlung**, kein Mailbox-Status.

## Ablauf

### 1. Nachrichtenfakten erfassen

Trenne explizite Fakten von Interpretation: Absender, Zeitpunkt, Thread-ID, genannte Frist, Frage/Aufforderung und bekannte frühere Aktion.

### 2. Handlungsbedarf bestimmen

Frage pro Thread:

- Ist eine konkrete Aktion vom Nutzer/Team verlangt oder implizit notwendig?
- Gibt es eine bestätigte Frist oder zeitkritische Folge?
- Wurde Verantwortung bereits nachweisbar delegiert?
- Warten wir nachweisbar auf eine andere Partei?
- Reicht der verfügbare Kontext für eine sichere Einordnung?

### 3. Priorität begründen

`urgent` benötigt konkrete Evidenz wie Frist, Betriebs-/Sicherheitsrisiko oder unmittelbare Blockade. Tonfall, Großschreibung oder Absenderhierarchie allein machen eine Nachricht nicht dringend.

### 4. Nächste Aktion formulieren

Formuliere eine kleine, überprüfbare nächste Aktion, z. B. „Frage X beantworten“, „Dokument Y prüfen“, „am Datum Z nachfassen“ oder „keine Aktion; FYI“.

Geplante Aktionen bleiben `pending`, bis ein externes Tool oder der Nutzer ihre Ausführung bestätigt.

### 5. Doppelungen/Threads konsolidieren

Mehrere Nachrichten desselben Vorgangs werden als Thread behandelt. Neuere Information darf frühere Fristen/Anforderungen ersetzen, aber nicht stillschweigend widersprechende Angaben löschen.

### 6. Ambiguität sichtbar halten

Fehlt z. B. ein Anhang, vorheriger Threadteil oder eine bestätigte Delegation, nutze `needs-context` statt eine scheinbar sichere Klasse zu erfinden.

## Ausgabe

`inbox-triage.json`:

```json
{
  "schemaVersion": 1,
  "asOf": "...",
  "scope": "...",
  "items": [
    {
      "threadRef": "...",
      "sender": "...",
      "receivedAt": "...",
      "subject": "...",
      "classification": "reply-soon",
      "confidence": "high",
      "facts": [],
      "reason": "...",
      "nextAction": "...",
      "actionStatus": "pending",
      "deadline": null,
      "waitingOn": null,
      "missingContext": []
    }
  ],
  "summary": {
    "urgent": 0,
    "replySoon": 0,
    "waiting": 0,
    "delegated": 0,
    "fyiArchive": 0,
    "needsContext": 0
  },
  "persistence": {
    "allowed": ["thread references", "minimal action facts", "classification", "next actions"],
    "runOnly": ["credentials", "unnecessary message bodies", "private raw connector payloads"]
  }
}
```

`inbox-triage.md` enthält eine kurze priorisierte Übersicht sowie je Thread Begründung und nächste Aktion.

## Datenschutz und Persistenz

Persistiere nur den für Nachverfolgung notwendigen Inhalt. Vollständige Nachrichtentexte, unnötige personenbezogene Details und private Connector-Rohdaten bleiben laufzeitgebunden, sofern keine explizite sachliche Notwendigkeit besteht.

Credentials, Tokens und versteckte Mail-Header werden niemals in Triage-Artefakte übernommen.

## Prüfungen

Vor Übergabe prüfen:

- jede Klasse ist durch konkrete Nachrichtenfakten begründet,
- `urgent` beruht nicht allein auf Tonfall oder Hierarchie,
- `waiting`/`delegated` sind durch eine tatsächliche frühere Aktion oder klare Nachricht belegt,
- fehlender Kontext führt nicht zu erfundener Sicherheit,
- nächste Aktionen sind klein und ausführbar,
- `actionStatus` ist nicht `completed`, solange keine externe Ausführung belegt ist,
- keine Mailbox-Mutation wird als erfolgt dargestellt,
- Datenschutzgrenzen sind eingehalten.

## Fehlerbehandlung

Wenn Thread-Kontext fehlt oder Aussagen widersprüchlich sind, verwende `needs-context` beziehungsweise reduziere Confidence. Wenn eine Frist nur vermutet wird, behandle sie nicht als bestätigte Dringlichkeit.

Bei unklarer Delegation nicht `delegated` setzen. Bei einer gesendeten eigenen Nachricht ohne Antwort kann `waiting` passend sein, sofern das Senden tatsächlich belegt ist.

## Übergaben

Nachgelagerte Verbraucher können sein:

- `daily-and-weekly-review` für priorisierte Aufgaben und wartende Vorgänge,
- `meeting-preparation` wenn ein Thread konkrete Vorbereitung für ein Meeting auslöst,
- ein Mailbox-Adapter für ausdrücklich bestätigte Reply-/Archive-/Label-Aktionen.

Der Triage-Output ist keine Autorisierung für automatische Mailbox-Mutationen.

## Qualitätsfälle

### Happy Path

Mehrere Threads enthalten klare Fristen, Antwortfragen, bestätigte Delegationen und FYI-Nachrichten. Ergebnis: begründete Klassen, kompakte nächste Aktionen und unveränderte Mailbox.

### Grenzfall

Eine Nachricht klingt dringend, enthält aber keine Frist; zugleich fehlt der vorherige Threadteil. Ergebnis: nicht automatisch `urgent`, sondern `needs-context` oder niedrige Confidence mit konkreter Kontextanforderung.

### Fehlerfall

Eine vorgeschlagene Triage erklärt eine Nachricht wegen eines Senior-Absenders für dringend, markiert eine nicht belegte Delegation als abgeschlossen und behauptet, FYI-Mails seien bereits archiviert. Stoppe und korrigiere Evidenz, Aktionsstatus und Mailbox-Status.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn jeder betrachtete Thread eine nachvollziehbare Klasse oder explizite Kontextlücke besitzt, Priorität und nächste Aktion aus belegten Nachrichtenfakten ableitbar sind, keine externe Aktion vorgetäuscht wird und die Triage ohne unnötige Nachrichtendaten an einen Review- oder Mailbox-Workflow übergeben werden kann.
