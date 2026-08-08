---
name: medical-device-complaint-evidence-followup
description: Plant und steuert gezielte Medical-Device-/IVD-Complaint-Folgeabfragen als versionierte Evidenzereignisse, ohne fehlende Informationen als Entlastung zu werten oder zeitkritische Vigilance-/MDR-Bewertung aufzuhalten.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - medical-device-complaint-handling
  - quality-record-integrity
outputs:
  - complaint-followup-plan.json
  - complaint-followup-request.json
  - complaint-evidence-delta.json
lastEvaluated: 2026-08-08
---

# Medical Device Complaint Evidence Follow-up

## Zweck und Grenze

Dieser Skill besitzt die **gezielte Informationsnachforderung** nach Complaint Intake/Evaluation: Welche fehlenden Fakten sind für Investigation, Risk, PMS oder regulatorische Neubewertung relevant, wie werden sie neutral angefragt und wie wird eine spätere Antwort als neue Evidenz in den bestehenden Fall zurückgeführt?

Er entscheidet nicht über Complaint-Klassifikation, Root Cause, CAPA, FDA MDR oder EU/IVDR Vigilance. Vor allem ist er **kein Warte-Gate vor regulatorischer Eskalation**. Eine offene Follow-up-Anfrage darf eine zeitkritische Bewertung niemals in den Zustand `not-reportable`, `no-event` oder `closed` umdeuten.

## Kernprinzipien

- **Ask only for decision-relevant evidence:** jede Nachfrage erhält Zweck, Decision Link und Priorität; „alles anfordern“ ist kein Qualitätsmerkmal.
- **Critical routing never waits for reply:** Safety-/MDR-/Vigilance-Eskalation läuft mit den verfügbaren Facts/Unknowns weiter.
- **Unknown is not negative evidence:** keine Antwort, unbekannter Outcome, unbekannte Lotnummer oder fehlendes Device werden nicht als Entlastung interpretiert.
- **Neutral questions protect evidence:** Fragen dürfen Reporter nicht zu gewünschter Ursache, Schwere oder Outcome-Antwort führen.
- **Original reply is evidence:** Kunden-/Distributor-/Service-Antwort wird mit eigener Source Reference und `receivedAt` erhalten; strukturierte Extraktion bleibt getrennt.
- **Every response is a delta:** neue Informationen überschreiben weder den ursprünglichen Complaint noch frühere Investigation-/Reportability-Entscheidungen.
- **Material delta triggers reassessment:** neue Outcome-, Seriousness-, Malfunction-, False-Result-, Use-, Market-, Lot-, Device- oder Remedial-Action-Fakten werden an die zuständigen bestehenden Skills zurückgegeben.
- **Contradictions stay visible:** neue Angaben, die früheren Aussagen widersprechen, werden als Konflikt geführt; die alte Aussage wird nicht gelöscht.
- **Data minimization by question design:** personenbezogene/gesundheitsbezogene Daten werden nur nachgefragt, soweit sie für die konkrete Quality-/Regulatory-Frage notwendig sind.
- **No harassment by completeness:** wiederholte Follow-ups benötigen fachlichen Zweck, angemessene Frequenz und dokumentierte Stop-/Escalation-Regeln.

## Trigger

Nutze den Skill, wenn `medical-device-complaint-handling` relevante Unknowns oder offene Evidenzbedarfe identifiziert, die durch Kunde, Anwender, Distributor, Service, Healthcare Professional, interne Funktion oder andere zulässige Quelle geklärt werden können.

Nicht nötig ist ein Follow-up nur deshalb, weil ein Formularfeld leer ist. Entscheidend ist, ob die Information eine konkrete Entscheidung, Investigation oder gesetzliche Pflicht beeinflussen kann.

## Voraussetzungen

- Complaint Reference und aktueller Evidence Snapshot,
- bekannte Facts/Unknowns,
- Investigation-/Regulatory-Handoff-State soweit vorhanden,
- Quelle/Empfängerrolle und zulässiger Kontaktweg soweit bekannt.

Unvollständige Voraussetzungen blockieren keine parallele Safety-/Regulatory-Aktion.

## Ablauf

### 1. Unknowns nach Entscheidungsrelevanz klassifizieren

Ordne jede fehlende Information mindestens einer Kategorie zu:

- `time-critical-regulatory`,
- `safety-outcome`,
- `event-sequence`,
- `device-identification`,
- `lot-serial-udi`,
- `result-performance`,
- `use-environment`,
- `medical-intervention`,
- `sample-specimen`,
- `service-repair-log`,
- `return-analysis`,
- `market-role`,
- `investigation-support`,
- `nice-to-have`,
- `not-needed`,
- `unknown`.

Dokumentiere für jede geplante Nachfrage, **welche konkrete Entscheidung** dadurch besser getroffen werden kann.

### 2. Waiting-Prohibition Gate setzen

Für jedes Unknown bestimme:

- `canProceedWithout=true|false|unknown`,
- `timeCriticalAssessmentAlreadyRouted=true|false|unknown`,
- `followupMayBlockComplaintClosure=true|false`,
- `followupMayBlockRegulatoryAssessment=false` bei möglicher zeitkritischer Relevanz.

Wenn Reportability/Vigilance mit verfügbaren Fakten bereits bewertet werden muss, wird der Specialist-Handoff parallel fortgesetzt. Der Follow-up-Skill darf kein künstliches „awaiting customer“ als regulatorischen Stop-State erzeugen.

### 3. Neutrale Frage formulieren

Fragen müssen:

- beobachtbare Fakten statt gewünschte Schlussfolgerungen erfragen,
- Zeitpunkt/Sequenz klar trennen,
- keine Ursache suggerieren,
- keine Schwere herunter- oder hochstufen,
- verständliche Kundensprache verwenden,
- unnötige medizinische/personenbezogene Detailabfragen vermeiden.

Beispiel: Statt „War der Benutzerfehler die Ursache?“ frage nach beobachteten Schritten, Anzeigen und Ereignisfolge. Statt „Es gab keine Verletzung, korrekt?“ frage, ob und welche medizinische Intervention oder gesundheitliche Auswirkung bekannt ist.

### 4. Anfrage priorisieren und begrenzen

`complaint-followup-plan.json` setzt pro Anfrage:

- Owner,
- Empfängerrolle,
- Question Set,
- Decision Link,
- Priority,
- Due/Review Trigger soweit prozessual erforderlich,
- Attempt State,
- Stop Condition,
- Parallel Regulatory State.

Mehrere Fragen werden gruppiert, wenn dies den Kontakt reduziert, ohne zeitkritische Einzelinformationen zu verzögern.

### 5. Antwort als neues Evidence Event aufnehmen

Beim Eingang einer Antwort:

1. Original Source Reference und `receivedAt` erfassen,
2. Antwort nicht rückdatieren oder in Originalnarrativ editieren,
3. neue Facts, weiterhin Unknowns und Widersprüche getrennt extrahieren,
4. `materiality: none|possible|material|unknown` bestimmen,
5. betroffene frühere Decisions/Investigations nur referenzieren,
6. `complaint-evidence-delta.json` erzeugen.

### 6. Reassessment routen

Materielle neue Information wird zurückgeführt an:

- `medical-device-complaint-handling` für Reopen/Investigation,
- `medical-device-complaint-regulatory-routing` für jurisdiction-spezifisches Reassessment,
- vorhandene FDA-/IVDR-Spezialisten bei zeitkritischer Relevanz über den bestehenden Router,
- Risk/CAPA/PMS nur über deren bestehende Ownership-Grenzen.

Kein Follow-up-Ergebnis wird direkt als `reportable|not-reportable` ausgegeben.

### 7. Non-response sauber behandeln

Bei ausbleibender Antwort:

- `responseState=no-response|partial-response|contact-unavailable|declined|unknown`,
- vorhandene Evidence bleibt gültiger Snapshot,
- Unknowns bleiben Unknowns,
- notwendige Specialist Assessment/Investigation wird mit dokumentierter Datenlücke fortgeführt,
- Complaint Closure hängt nur dann von der Antwort ab, wenn der zuständige Complaint-Owner dies evidenzbasiert begründet.

Non-response erzeugt niemals automatisch `no-injury`, `no-malfunction`, `user-error`, `not-reportable` oder `investigation-not-required`.

## Prüfungen

Vor Versand/Übergabe prüfe:

- besitzt jede Frage einen fachlichen Decision Link,
- enthält keine Frage eine gewünschte Antwort oder ungeprüfte Ursache,
- werden Safety-/Regulatory-Pfade nicht durch `awaiting reply` blockiert,
- sind personenbezogene/gesundheitsbezogene Fragen minimiert,
- bleiben ursprüngliche und spätere Aussagen versioniert getrennt,
- erzeugen relevante neue Fakten einen Reassessment-Handoff.

## Fehlerbehandlung

- Widersprüchliche Antworten → beide Source Statements erhalten, Konflikt markieren, ggf. weitere Verifikation statt stiller Auswahl.
- Kunde kann Device/Lot nicht identifizieren → Unknown belassen; nicht aus Nachbarfall ableiten.
- HCP-/Patientendaten unnötig detailliert → auf erforderliche Entscheidungsinformation reduzieren.
- Mehrfach erfolglos kontaktiert → Stop Condition/Owner Review statt unendlicher Wiederholung.
- Antwort kommt nach Closure → als neues Evidence Event aufnehmen und Materiality/Reopen prüfen.
- Antwort kommt nach früherem `not-reportable` → frühere Entscheidung nicht überschreiben; bei materiellem Delta Reassessment auslösen.

## Übergabe

`complaint-evidence-delta.json` geht mit Source/ReceivedAt, New Facts, Remaining Unknowns, Contradictions, Materiality und Prior Decision References zurück an `medical-device-complaint-handling` und bei regulatorischer Relevanz an `medical-device-complaint-regulatory-routing`.

Zeitkritische Regulatory-Handoffs erfolgen unabhängig vom Follow-up-State. Der Skill übermittelt keine Behördenmeldung und versendet keine Kundenkommunikation ohne den dafür vorgesehenen Human-/Systemprozess.

## Output-Verträge

`complaint-followup-plan.json` enthält Unknowns, Decision Links, Priorities, Owners, Contact Strategy, Attempt/Stop State, Data-Minimization State und parallele Quality-/Regulatory States.

`complaint-followup-request.json` enthält ein neutrales, begrenztes Question Set mit Zweckreferenzen und ohne interne spekulative Root-Cause-/Reportability-Aussagen.

`complaint-evidence-delta.json` enthält immutable Response Reference, `receivedAt`, New Facts, Remaining Unknowns, Contradictions, Materiality, Prior Decision/Complaint References und Reassessment Routing.

## Memory Path

Persistenzwürdig sind abstrahierte, validierte Fragepatterns, Decision-Link-Kategorien, Non-response-Regeln und Datenminimierungsheuristiken. Konkrete Fragen/Antworten, Kunden-/Patienten-/Reporterinformationen, Complaint IDs, Outcomes, Geräte-/Lotdaten und laufende Investigation-/Regulatory-Zustände bleiben run-only bzw. kontrollierte Quality Records. Nur abstrahierte `memory-candidate-handoff-v1`-Kandidaten gehen an `communication-memory-governance`.

## Abschlusskriterien

Bestanden nur wenn:

- Follow-up nur entscheidungsrelevante Evidenz anfordert,
- offene Nachfragen zeitkritische MDR-/Vigilance-Bewertung nicht blockieren,
- Non-response niemals als negative oder entlastende Evidenz ausgegeben wird,
- Fragen neutral und datensparsam sind,
- jede Antwort als neues Source-/Receipt-Ereignis versioniert bleibt,
- Widersprüche nicht überschrieben werden,
- materielle neue Evidenz Reopen/Reassessment auslösen kann,
- der Skill keine Complaint-, Investigation-, CAPA-, PMS- oder Reportability-Ownership dupliziert.
