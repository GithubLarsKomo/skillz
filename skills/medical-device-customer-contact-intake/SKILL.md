---
name: medical-device-customer-contact-intake
description: Normalisiert Medical-Device-/IVD-Kundenkontakte kanalunabhängig in einen belastbaren Quality-Intake und trennt Service, Feedback, mögliche Complaint und potenzielles Safety-Signal, ohne Beschwerden durch Wortwahl, Kulanz oder Frontline-Lösung wegzuklassifizieren.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - quality-record-integrity
outputs:
  - customer-contact-record.json
  - customer-contact-triage.json
  - complaint-intake-handoff.json
lastEvaluated: 2026-08-08
---

# Medical Device Customer Contact Intake

## Zweck und Grenze

Dieser Skill besitzt den kontrollierten **Erst- und Folgekontakt** für Medical-Device-/IVD-Kunden-, Anwender-, Distributor-, Service- und Feldinformationen. Er macht aus Telefon, E-Mail, Portal, Außendienst, Serviceeinsatz oder vergleichbarer Quelle einen nachvollziehbaren Intake, ohne bereits Complaint Investigation, CAPA, FDA-MDR- oder EU-Vigilance-Entscheidungen zu übernehmen.

Der Skill ist ausdrücklich **kein CRM-, Helpdesk- oder Complaint-Closure-System**. Ein Kundenkontakt kann parallel einen kommerziellen Servicepfad und einen Quality-/Complaint-Pfad erzeugen. Ein späterer Kontakt kann neue Quality-/Safety-Evidence liefern und muss deshalb unabhängig vom administrativen Status eines früheren Tickets aufgenommen werden.

## Kernprinzipien

- **Original voice is evidence:** ursprüngliche Aussage, Quelle, Kanal und Empfangszeit werden unverändert referenziert; strukturierte Zusammenfassungen bleiben davon getrennt.
- **Customer wording does not control classification:** weder das Wort `complaint` noch dessen Fehlen entscheidet, ob eine mögliche Beschwerde vorliegt.
- **Service resolution does not erase quality signal:** Austausch, Gutschrift, Troubleshooting, Schulung oder sofortige Fehlerbehebung schließen eine mögliche Complaint nicht.
- **Every follow-up is a new evidence event:** spätere E-Mails, Rückrufe, Serviceberichte, Distributor-Updates oder Feldbeobachtungen erhalten eigene Source Reference und eigenen Empfangszeitpunkt; sie überschreiben weder den Erstkontakt noch eine frühere Complaint-/Regulatory-Entscheidung.
- **New material information reopens quality routing:** neue Safety-, Performance-, Outcome-, Malfunction-, False-Result- oder Marktfakten nach `ticket closed`, `customerResolved`, `complaintClosed` oder einer früheren regulatorischen Bewertung erzeugen einen neuen Quality-/Complaint-/Regulatory-Handoff, sofern sie die bisherige Bewertung materiell beeinflussen können.
- **Safety beats service SLA:** Hinweise auf Tod, Verletzung, medizinische Intervention, falsches/fehlendes Ergebnis, potenziell gefährliche Fehlfunktion oder anderes mögliches Safety-Ereignis erzeugen unverzüglich einen Quality-/Regulatory-Handoff; der normale Servicepfad läuft höchstens parallel.
- **Received time is immutable:** `receivedAt`, Kanal und Quelle werden nicht nachträglich auf eine günstigere Bearbeitungszeit verschoben. Spätere Awareness-/Reportability-Bewertungen gehören nachgelagerten Skills.
- **Unknown stays unknown:** Produkt, Lot, UDI, Outcome, Reporterrolle oder Ereignisdetails werden nicht erraten.
- **Data minimization:** nur für Kontakt-, Quality-, Investigation- oder regulatorische Zwecke notwendige personenbezogene/gesundheitsbezogene Daten werden in kontrollierte Artefakte übernommen.

## Workflow

### 1. Kontaktquelle fixieren

Erfasse mindestens:

- `contactId`,
- `receivedAt`, `channel`, `sourceType`,
- Originalnachricht bzw. unveränderliche Source Reference,
- Kontakt-/Reporterbezug soweit erforderlich,
- Produkt-/Device-Bezug soweit bekannt,
- Land/Markt/Nutzungskontext soweit bekannt,
- beobachtetes Problem, gewünschte Hilfe und bekannte Auswirkungen,
- bereits erfolgte Service-/Commercial-Aktion,
- `relatedPriorContactIds` / bestehende Complaint-/Case-Reference soweit bekannt.

Weitergeleitete Nachrichten behalten die früheste belegte Empfangsinformation und die Transferkette; nur der aktuelle Eingang in ein anderes Team wird nicht als ursprünglicher Empfang ausgegeben. Folgekontakte werden als neue Evidence Events ergänzt, nicht in den früheren Kontakt hineineditiert.

### 2. Kontakt semantisch triagieren

Klassifiziere nicht exklusiv, sondern multi-label-fähig:

- `information-request`,
- `order-logistics`,
- `service-support`,
- `feedback`,
- `possible-complaint`,
- `confirmed-complaint`,
- `potential-safety-event`,
- `supplemental-information`,
- `reopen-candidate`,
- `unknown`.

Eine Servicefrage kann gleichzeitig `possible-complaint` sein. Eine positive oder höfliche Formulierung kann dennoch einen Produktfehler enthalten. Ein Distributor-/Außendienstkontakt wird nicht niedriger priorisiert als direkter Endkundenkontakt.

### 3. Complaint Trigger prüfen

Erzeuge `complaint-intake-handoff.json`, sobald Tatsachen eine mögliche Unzufriedenheit oder einen möglichen Fehler/Defekt/Nichterfüllung von Produkt-, Labeling-, Packaging-, Performance- oder Safety-Erwartungen erkennen lassen. Der Handoff bleibt auch dann bestehen, wenn die Anfrage unmittelbar gelöst wurde.

Nicht als Complaint erzwingen, wenn ausschließlich neutrale Information, Bestellung oder Logistik ohne Qualitäts-/Leistungsbezug vorliegt. Unsicherheit führt zu `possible-complaint`, nicht zu `not-a-complaint`.

### 4. Safety Trigger prüfen

Markiere `safetyEscalationRequired=true`, wenn verfügbare Informationen vernünftigerweise einen potenziell regulatorisch relevanten Adverse-/Incident-/Serious-Incident-/Malfunction-/False-Result-Sachverhalt nahelegen können. Der Skill entscheidet **nicht**, ob FDA MDR oder EU Vigilance tatsächlich reportable ist.

Erhalte separat:

- `receivedAt`,
- `firstKnownInternalReceiptAt` soweit belegbar,
- `safetySignalObservedAt`,
- beobachtete Safety-Fakten,
- Unknowns,
- Quelle/Employee/Team-Transfer-Evidence soweit zulässig.

Kein Frontline-Team darf den Handoff bis zur vollständigen Root Cause oder Rücksendung des Produkts zurückhalten.

### 5. Folgekontakt und Reopen Trigger bewerten

Wenn ein neuer Kontakt zu einem bestehenden oder früher geschlossenen Customer-/Complaint-/Regulatory-Fall gehört:

1. referenziere den bisherigen Zustand statt ihn zu überschreiben,
2. ermittle `newMaterialFacts` gegenüber dem letzten bekannten Stand,
3. setze `reopenCandidate=true`, wenn neue Fakten Complaint Scope, Investigation, Risk, PMS oder Regulatory Assessment ändern können,
4. erzeuge einen aktualisierten `complaint-intake-handoff.json` mit Delta-/Source-References,
5. route potenzielle Safety-Information sofort weiter, selbst wenn Ticket oder Complaint zuvor geschlossen waren.

Ein früheres `not-a-complaint`, `complaintClosed`, `not-reportable` oder `customerResolved` ist historische Evidenz, keine Sperre für Neubewertung.

### 6. Parallelpfade explizit machen

Erlaube gleichzeitig:

- Customer-Service-Antwort,
- technische Soforthilfe,
- Ersatz/Gutschrift,
- Complaint Handling,
- regulatorische Eskalation.

`customerResolved=true` bedeutet niemals automatisch `complaintClosed=true` oder `regulatoryClosed=true`.

### 7. Record Integrity sichern

Nutze `quality-record-integrity` für Attribution, Zeitstempel, unveränderliche Source References, Korrekturhistorie und Datenminimierung. Korrekturen überschreiben den ursprünglichen Kontakt nicht; sie werden als nachvollziehbare Ergänzungen geführt.

## Output-Verträge

`customer-contact-record.json` enthält Original-Source-Reference, Intake-Zeit, Kanal, bekannte Kontakt-/Produkt-/Marktfakten, Customer Request, bereits erfolgte Service Actions, Related-Case-References, Follow-up-/Delta-State, Data-Minimization-State und Record-Integrity-Status.

`customer-contact-triage.json` enthält alle zutreffenden Kontaktklassen, Begründung, Facts/Unknowns, `complaintCandidate`, `safetyEscalationRequired`, `supplementalInformation`, `reopenCandidate`, Dringlichkeit, Owner-Handoff und Parallelpfade.

`complaint-intake-handoff.json` enthält nur die für Complaint Handling notwendigen Fakten und Source References, insbesondere Intake-/Transfer-Timeline, Related Prior Record, neue materielle Fakten, Device/Market Context soweit bekannt, Problem/Impact, Safety Flags, fehlende Informationen und bereits erfolgte Service Actions. Es enthält keine finale Reportability-Entscheidung.

## Memory Path

Persistenzwürdig sind abstrahierte, validierte Intake-Kategorien, wiederverwendbare Safety-/Complaint-/Reopen-Trigger und bewährte Datenminimierungs-/Routing-Muster. Konkrete Kontakte, Kunden-/Patienten-/Reporter-Daten, IDs, Zeitstempel, Produkt-/Lot-Informationen, einzelne Beschwerden und aktuelle Safety-Hinweise bleiben run-only bzw. in kontrollierten CRM-/Quality-/Complaint-Records. Übergib nur geeignete abstrahierte `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- die ursprüngliche Aussage und jeder belegte Erst-/Folgeempfang erhalten bleiben,
- Customer-Wortwahl oder gewünschte Kulanz nicht über Complaint-Klassifikation entscheidet,
- eine Service-Lösung mögliche Complaint-/Safety-Pfade nicht schließt,
- neue materielle Informationen nach früherer Closure oder Bewertung einen Reopen-/Reassessment-Handoff auslösen können,
- potenzielle Safety-Information ohne Warten auf Root Cause oder vollständige Produktdaten eskaliert wird,
- `customerResolved`, `complaintClosed`, frühere `not-reportable`-Bewertung und aktueller Regulatory State getrennt bleiben,
- Folgeinformationen den historischen Record nicht überschreiben oder günstig rückdatieren,
- Unknowns nicht ergänzt oder rückdatiert werden,
- personenbezogene/gesundheitsbezogene Daten minimiert und kontrolliert bleiben.
