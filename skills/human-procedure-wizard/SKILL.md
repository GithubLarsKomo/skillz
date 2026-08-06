---
name: human-procedure-wizard
description: Führt sicher durch unvermeidbare menschliche Schritte in ansonsten agentengesteuerten Workflows, etwa Dashboard-Aktionen, Freigaben, Secret-Eingaben, physische Bestätigungen oder irreversible Cutover-Gates. Verwenden, wenn ein Agent den nächsten Schritt nicht selbst ausführen darf oder kann und danach verifizierbar weiterarbeiten soll; nicht für normale Anforderungsklärung oder reine Übergaben.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - human-procedure-plan.md
  - human-procedure-result.json
lastEvaluated: 2026-08-06
---

# Human Procedure Wizard

## Zweck

Dieser Skill verwandelt einen technisch verstandenen, aber nicht vollständig agentenausführbaren Arbeitsschritt in eine sichere menschliche Prozedur und endet erst, wenn das Ergebnis durch beobachtbare Evidenz wieder in den Agentenworkflow übernommen werden kann.

Er übernimmt nicht die fachliche Entscheidung, ob ein Produkt, eine Architektur oder eine regulatorische Maßnahme grundsätzlich richtig ist. Er strukturiert ausschließlich die menschliche Ausführung eines bereits identifizierten notwendigen Schritts.

## Trigger

Verwenden, wenn mindestens eine notwendige Aktion:

- nur über eine interaktive Oberfläche möglich ist,
- eine menschliche Freigabe oder Identitätsprüfung benötigt,
- ein Secret erfordert, das der Agent nicht sehen oder speichern soll,
- eine physische Handlung oder externe Bestätigung benötigt,
- irreversibel oder schwer rückgängig zu machen ist und deshalb eine explizite Bestätigung verlangt,
- wegen fehlender Tool-Berechtigung nicht agentisch ausgeführt werden kann.

Nicht verwenden für normale Requirements-Elicitation, offene Architekturentscheidungen, allgemeine Meeting-Vorbereitung oder einen bloßen Session-Wechsel. Dafür bleiben `conversation-to-spec`, fachliche Entscheidungs-Skills, `meeting-preparation` beziehungsweise `agent-handoff` zuständig.

## Kernregeln

- **Nur echte Human-only-Schritte:** Alles, was sicher und autorisiert automatisierbar ist, bleibt Agentenarbeit.
- **Vorbereiten vor Fragen:** Repository, Konfiguration und autoritative Dokumentation prüfen, bevor der Mensch um Eingaben gebeten wird.
- **Minimale Offenlegung:** Secrets werden weder abgefragt, wenn eine lokale Eingabe genügt, noch in Chat, Markdown, Logs oder Kommandohistorie kopiert.
- **Ein Schritt pro Gate:** Menschliche Aktionen werden in klar getrennte, beobachtbare Schritte zerlegt.
- **Irreversibilität explizit markieren:** Vor destruktiven, produktiven oder kostenwirksamen Aktionen ist eine unmittelbare Bestätigung erforderlich.
- **Keine Erfolgssimulation:** Der Agent behauptet keine UI-, Hardware- oder Freigabeaktion als erledigt, solange keine Rückmeldung oder externe Evidenz vorliegt.
- **Verifikation danach:** Jeder menschliche Schritt besitzt ein erwartetes Resultat und eine anschließende Prüfung.

## Ablauf

### 1. Blocker klassifizieren

Bestimme, warum der Schritt menschlich ausgeführt werden muss:

- `interactive-ui`
- `human-approval`
- `secret-entry`
- `physical-action`
- `irreversible-gate`
- `missing-agent-permission`

Ist der Schritt lediglich noch nicht verstanden, zuerst `disciplined-diagnosis`, `large-work-wayfinder` oder einen passenden Fach-Skill verwenden.

### 2. Agentenarbeit vorziehen

Erledige vor dem menschlichen Schritt alles, was sicher automatisierbar ist:

- Zielzustand und Vorbedingungen bestimmen,
- relevante Konfiguration und aktuellen Zustand lesen,
- autoritative Dokumentation identifizieren,
- Werte vorbereiten, die nicht geheim sind,
- Validierungsbefehle oder Prüfpfade vorbereiten,
- Rückroll- oder Abbruchbedingung definieren, falls nötig.

Der Mensch soll keine Information zusammensuchen müssen, die der Agent selbst zuverlässig beschaffen kann.

### 3. Human Procedure Plan erzeugen

Erzeuge `human-procedure-plan.md` mit:

1. Ziel des menschlichen Schritts,
2. warum er nicht agentisch ausgeführt wird,
3. Vorbedingungen,
4. exakt geordneten Aktionen,
5. erwarteter sichtbarer Reaktion nach jeder Aktion,
6. Kennzeichnung von Secret-, Kosten-, Produktiv- und Irreversibilitätsgrenzen,
7. Abbruchbedingung,
8. Informationen, die zurückgemeldet werden müssen,
9. anschließender Agenten-Verifikation.

Verlinke nach Möglichkeit direkt auf die autoritative Oberfläche oder Dokumentation. Verwende keine erfundenen Navigationspfade, wenn die aktuelle UI nicht verifiziert wurde.

### 4. Secrets sicher behandeln

Für jeden geheimen Wert festlegen:

- wer ihn erzeugt oder besitzt,
- wo er eingegeben wird,
- wo er dauerhaft gespeichert werden darf,
- welche nicht-geheime Kennung oder Prüfinformation zurückgegeben werden darf.

Bevorzuge Formulierungen wie „Trage den Token direkt in das Feld ein und bestätige nur, dass er gespeichert wurde“ statt den Wert im Gespräch anzufordern.

### 5. Irreversible Gates bestätigen

Unmittelbar vor einer irreversiblen, produktiven, extern kommunizierenden oder kostenwirksamen Aktion:

- konkreten Effekt nennen,
- Zielsystem und Scope nennen,
- Rückrollmöglichkeit oder deren Fehlen nennen,
- eine explizite Bestätigung verlangen.

Eine frühere allgemeine Freigabe ersetzt diese letzte Gate-Bestätigung nicht.

### 6. Ergebnis aufnehmen

Nach menschlicher Ausführung nur die minimal notwendige Rückmeldung erfassen. Erzeuge `human-procedure-result.json`:

```json
{
  "procedure": "...",
  "status": "completed|blocked|aborted|unverified",
  "humanSteps": [
    {
      "step": "...",
      "reportedResult": "...",
      "sensitiveValueReturned": false
    }
  ],
  "verification": {
    "method": "...",
    "status": "passed|failed|pending|not-possible",
    "evidence": "..."
  },
  "nextAction": "...",
  "nextSkill": "..."
}
```

Secrets, vollständige Screenshots mit vertraulichen Werten und unnötige personenbezogene Informationen gehören nicht in dieses Artefakt.

### 7. Agentisch verifizieren

Wenn möglich, prüfe den neuen Zustand unabhängig über API, CLI, Repository, Healthcheck, Audit-Log oder anderes autoritatives Signal.

- `passed`: Workflow darf fortgesetzt werden.
- `failed`: zurück zu Diagnose oder klar definiertem Korrekturschritt.
- `pending`: an `deferred-external-action-verification` übergeben.
- `not-possible`: menschliche Rückmeldung bleibt explizit als nicht unabhängig verifiziert markiert.

## Fehler- und Abbruchfälle

Die Prozedur stoppen, wenn:

- der Mensch einen Secret-Wert in den Chat kopieren soll,
- die Zielumgebung oder der Scope nicht eindeutig sind,
- die Oberfläche nicht mit der Beschreibung übereinstimmt,
- eine unerwartete Warnung, Kostenfolge oder Berechtigungsänderung erscheint,
- ein irreversibler Schritt ohne unmittelbare Bestätigung erreicht wird,
- die notwendige Verifikation nicht definiert ist.

Bei UI-Abweichungen nicht raten. Aktuellen Zustand neu erfassen und den Plan korrigieren.

## Komposition

Typische vorgelagerte Skills:

- `large-work-wayfinder` für Sequenz und Abhängigkeiten,
- `disciplined-diagnosis` für unbekannte Blocker,
- Fach-Skills für die Entscheidung, was fachlich getan werden soll.

Typische nachgelagerte Skills:

- `deferred-external-action-verification` bei asynchronem Ergebnis,
- `agent-handoff` wenn der verifizierte Zustand in eine andere Sitzung übertragen werden muss,
- der ursprüngliche Fach- oder Implementierungs-Skill bei erfolgreicher Verifikation.

## Evaluation

### Happy Path

Ein Deployment benötigt einmalig das Anlegen eines Tokens in einem Anbieter-Dashboard. Der Skill bereitet Ziel, Feld, Secret-Grenze und anschließenden API-Healthcheck vor. Der Mensch trägt den Token direkt ein, meldet nur „gespeichert“, und der Agent verifiziert den Dienst ohne den Token offenzulegen.

### Grenzfall

Eine UI hat sich geändert und die erwartete Schaltfläche fehlt. Der Skill stoppt, statt einen Navigationspfad zu erfinden, und fordert nur den aktuellen nicht-sensitiven Zustand zur Neuplanung an.

### Fehlerfall

Vor einem produktiven DNS-Cutover erscheint eine unerwartete Warnung über irreversible Auswirkungen. Der Skill bricht vor der Änderung ab und verlangt eine neue Bewertung; er behandelt die frühere Freigabe nicht als ausreichende Bestätigung.

## Abschlusskriterien

Die Aufgabe ist abgeschlossen, wenn:

- nur tatsächlich menschliche Schritte beim Menschen verblieben sind,
- jede Aktion einen eindeutigen erwarteten Zustand besitzt,
- Secrets nicht in Gespräch oder Artefakte gelangt sind,
- irreversible Schritte unmittelbar bestätigt wurden,
- Ergebnis und Verifikationsstatus maschinenlesbar festgehalten sind,
- der nächste Agentenschritt ohne erneute Rekonstruktion ausführbar ist.
