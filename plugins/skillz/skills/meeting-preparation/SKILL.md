---
name: meeting-preparation
description: Verdichtet einen bestätigten Termin, Teilnehmerkontext und verfügbare Evidence Notes zu einem kompakten, entscheidungsorientierten Meeting-Prep-Brief. Verwenden, wenn vor einem Meeting Ziele, Entscheidungen, belegte Fakten, offene Fragen, Risiken und konkrete Vorbereitung strukturiert werden sollen, ohne Kalender-, Kontakt-, Dokument- oder Retrieval-Logik zu duplizieren.
---

# Meeting Preparation

## Zweck und Grenze

Erzeuge aus einem bestätigten Meeting-Kontext und verfügbaren Evidenznotizen einen praktischen Vorbereitungsbrief. Der Skill strukturiert Vorbereitung und Entscheidungsbedarf; er ist **kein Kalender-Connector, Kontaktverzeichnis, Dokumenten-Retriever, Scheduler oder Protokollgenerator**.

Connectoren oder andere Tools dürfen Termin, Teilnehmer, frühere Entscheidungen und relevante Unterlagen liefern. Recherche mit mehreren Quellen wird über `research-to-evidence-note` verdichtet. Dieser Skill beginnt bei bestätigten Meeting-Fakten plus verfügbarer Evidenz und endet vor Einladung, Terminänderung oder Durchführung des Meetings.

## Trigger

Verwenden, wenn mindestens eines zutrifft:

- ein anstehendes Meeting benötigt eine kompakte Vorbereitung,
- Entscheidungen oder offene Fragen müssen vorab sichtbar sein,
- mehrere Evidenznotizen sollen auf ein konkretes Meeting fokussiert werden,
- Risiken, Teilnehmerinteressen oder fehlende Informationen sollen vor dem Termin erkannt werden.

Nicht verwenden für reine Kalenderzusammenfassungen ohne Vorbereitungsziel oder wenn der primäre Auftrag Scheduling beziehungsweise Einladung ist.

## Voraussetzungen

Vor der Synthese fixieren:

1. Meeting-Titel, Datum/Zeit und bestätigten Zweck,
2. bekannte Teilnehmer und Rollen nur soweit für die Vorbereitung relevant,
3. gewünschtes Ergebnis oder Entscheidungsbedarf,
4. vorhandene `evidence-note`-Artefakte und bestätigte frühere Entscheidungen,
5. bekannte Informationslücken oder Zugriffsbeschränkungen.

Unklare Meeting-Ziele nicht durch Vermutungen ersetzen. Wenn Teilnehmerrolle oder Entscheidungskompetenz nicht bestätigt ist, als offen markieren.

## Eingaben

- `meetingFacts`: Titel, Zeitpunkt, Dauer, Format/Ort, bestätigte Agenda oder Zweck,
- `participants`: Name/Bezeichner, bestätigte Rolle, relevante Zuständigkeit,
- `evidenceNotes`: null oder mehrere `evidence-note.json`/äquivalente strukturierte Notizen,
- `priorDecisions`: bestätigte Entscheidungen mit Quelle/Datum,
- `constraints`: Vertraulichkeit, Zeitlimit, gewünschte Entscheidungstiefe.

## Ablauf

### 1. Meeting-Fakten fixieren

Trenne bestätigte Fakten von Annahmen. Titel, Zeit, Zweck und Teilnehmer werden nicht aus Kontext „erraten“. Fehlende Felder bleiben sichtbar offen.

### 2. Ziel und Entscheidungspunkte bestimmen

Formuliere maximal die entscheidungsrelevanten Ziele. Für jeden Entscheidungspunkt notiere:

- Entscheidung oder gewünschtes Ergebnis,
- Entscheidungsträger, falls bestätigt,
- benötigte Evidenz,
- noch fehlende Information,
- Konsequenz einer Vertagung, falls relevant.

### 3. Evidenz fokussieren

Übernimm aus `research-to-evidence-note` nur Claims, Konflikte und offene Fragen, die für dieses Meeting relevant sind. Bewahre Claim-IDs, Quellenreferenzen, Confidence und Widersprüche.

Keine neue `high`-Confidence-Aussage erzeugen, wenn die zugrunde liegende Evidence Note `medium`, `low` oder einen offenen Konflikt ausweist.

### 4. Teilnehmerkontext begrenzen

Nutze nur verifizierten, meetingrelevanten Kontext wie Rolle, Zuständigkeit, bekannte Entscheidung oder zugesagte Aktion. Keine Persönlichkeitsprofile, sensiblen Eigenschaften oder spekulativen Motive ableiten.

### 5. Fragen und Risiken priorisieren

Ordne offene Fragen nach Einfluss auf Meeting-Ziel und Entscheidung. Risiken umfassen z. B. widersprüchliche Evidenz, fehlende Entscheider, ungeklärte Abhängigkeiten oder zeitkritische Informationen.

Trenne sachliche Risiken von bloßen Gesprächsstrategien.

### 6. Vorbereitung ableiten

Formuliere konkrete Vorbereitungsaktionen, z. B. eine Zahl verifizieren, eine Entscheidungsvorlage öffnen oder einen offenen Punkt einem Teilnehmer zuordnen. Keine Aktion vortäuschen, die ein Connector oder Mensch erst noch ausführen muss.

### 7. Brief erstellen

Der Brief beginnt mit einem 30-Sekunden-Überblick und enthält danach nur entscheidungsrelevante Details. Hintergrundwissen ohne Einfluss auf Ziel, Risiko oder Entscheidung wird weggelassen.

## Ausgabe

`meeting-prep.json`:

```json
{
  "schemaVersion": 1,
  "meeting": {
    "title": "...",
    "start": "...",
    "purpose": "...",
    "confirmedFacts": [],
    "unknowns": []
  },
  "participants": [
    {
      "id": "P1",
      "name": "...",
      "role": "...",
      "context": "...",
      "source": "..."
    }
  ],
  "objectives": [],
  "decisionsNeeded": [],
  "evidence": [
    {
      "claimId": "C1",
      "claim": "...",
      "confidence": "medium",
      "sourceRefs": ["S1"],
      "conflicts": []
    }
  ],
  "openQuestions": [],
  "risks": [],
  "preparationActions": [],
  "brief": "...",
  "persistence": {
    "allowed": ["meeting facts", "meeting-relevant evidence", "confirmed roles", "preparation actions"],
    "runOnly": ["credentials", "private raw connector payloads", "unnecessary attendee personal data"]
  }
}
```

`meeting-prep.md` enthält dieselben Inhalte lesbar gegliedert in 30-Sekunden-Brief, Ziele, Entscheidungen, Evidenz, offene Fragen, Risiken, Teilnehmerkontext und Vorbereitung.

## Datenschutz und Persistenz

Persistiere nur meetingrelevante, zulässige Informationen. Rohdaten aus Kalender-, Kontakt- oder Dokument-Connectoren bleiben laufzeitgebunden, sofern sie nicht ausdrücklich als notwendiger Fakt in den Brief übernommen werden.

Keine sensiblen persönlichen Merkmale, privaten Kommunikationsinhalte oder spekulativen Teilnehmerprofile in dauerhafte Prep-Artefakte übernehmen. Credentials und Tokens werden niemals persistiert.

## Prüfungen

Vor Übergabe prüfen:

- Meeting-Zweck und Zeit stammen aus bestätigten Fakten,
- jede relevante Evidenzaussage ist auf eine Evidence Note beziehungsweise nachvollziehbare Quelle zurückführbar,
- Confidence und Konflikte wurden nicht „hochgestuft“ oder entfernt,
- Entscheidungen, offene Fragen und Vorbereitung sind voneinander getrennt,
- Teilnehmerkontext ist verifiziert und meetingrelevant,
- keine Kalender-/Connector-Aktion wird als ausgeführt dargestellt,
- Brief ist kurz genug, um unmittelbar vor dem Meeting nutzbar zu sein,
- Datenschutz- und Persistenzgrenzen sind eingehalten.

## Fehlerbehandlung

Wenn Meeting-Zweck oder Termin nicht eindeutig bestätigt ist, erzeuge keinen autoritativen Prep-Brief. Liefere stattdessen einen partiellen Stand mit `unknowns` und den kleinsten fehlenden Informationen.

Wenn Evidence Notes widersprüchliche Claims enthalten, bleibt der Konflikt sichtbar und wird als Entscheidungsrisiko übernommen. Wenn keine belastbare Evidenz verfügbar ist, formuliere Fragen und Vorbereitung, aber keine scheinbar belegten Antworten.

## Übergaben

Nachgelagerte Verbraucher können sein:

- `decision-record` für tatsächlich getroffene Entscheidungen nach dem Meeting,
- `document-production` für freigegebene Briefings oder Entscheidungsvorlagen,
- `project-status-brief` für bestätigte Ergebnisse oder neue Blocker.

Der Prep-Brief selbst ist **kein** Meeting-Protokoll und darf nach dem Termin nicht automatisch als Entscheidungsnachweis behandelt werden.

## Qualitätsfälle

### Happy Path

Termin, Rollen, Ziel und zwei aktuelle Evidence Notes sind bestätigt. Der Brief fokussiert drei relevante Claims, zwei Entscheidungen, konkrete Vorbereitung und übernimmt Confidence/Quellen unverändert.

### Grenzfall

Ein Teilnehmer ist bestätigt, seine Entscheidungsrolle jedoch nicht; zwei relevante Claims widersprechen sich. Ergebnis: Rolle bleibt offen, Konflikt wird als Risiko übernommen und eine konkrete Klärungsfrage wird vorbereitet.

### Fehlerfall

Eine vorgeschlagene Vorbereitung erfindet Teilnehmermotive, stuft einen `low`-Confidence-Claim auf sicher hoch und behauptet, fehlende Unterlagen seien bereits angefordert. Stoppe und korrigiere Teilnehmerkontext, Evidenzstatus und Aktionsstatus.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Meeting-Fakten, Ziele, Entscheidungen, relevante Evidenz, offene Fragen, Risiken und konkrete Vorbereitung kompakt getrennt vorliegen, Provenance und Unsicherheit erhalten bleiben und ein Teilnehmer den Brief unmittelbar vor dem Termin nutzen kann, ohne Rohrecherche oder versteckte Annahmen rekonstruieren zu müssen.
