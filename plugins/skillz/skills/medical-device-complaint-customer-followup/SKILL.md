---
name: medical-device-complaint-customer-followup
description: Plant und dokumentiert Medical-Device-/IVD-Customer-Follow-up für offene oder wieder zu öffnende Complaints evidenzbasiert, konsistent und datensparsam und führt neue Fakten kontrolliert in Complaint- und Regulatory-Reassessment zurück, ohne Investigation oder Reportability zu übernehmen.
---

# Medical Device Complaint Customer Follow-up

## Zweck und Grenze

Dieser Skill besitzt den **kontrollierten Customer-Follow-up-Schritt nach Complaint-Eröffnung oder bei späterem Follow-up zu einem bestehenden Complaint**. Er bestimmt aus dokumentierten Informationslücken, welche kundenbezogenen Rückfragen oder Evidence-Aktionen erforderlich sind, formuliert neutrale Fragen, dokumentiert Kontaktversuche und Antworten und erzeugt ein versioniertes Evidence Delta für Complaint Handling und ggf. Regulatory Reassessment.

Er ist **nicht** der Owner der Complaint-Klassifikation, Ursachenuntersuchung, CAPA, Risk-Bewertung, MDR-/Vigilance-Entscheidung oder externen Behördenkommunikation. Er darf Customer Service nicht zu einem parallelen Investigation- oder Regulatory-System machen und führt keine Kommunikation autonom aus.

## Kernprinzipien

- **Follow-up criteria are explicit:** Follow-up wird aus konkreten Information Gaps, Safety-/Performance-Relevanz, Device/Evidence Availability und definierten Verfahrenskriterien abgeleitet; vergleichbare Fälle werden nicht willkürlich unterschiedlich nachverfolgt.
- **No response is not a negative fact:** `no-response|unable-to-contact|declined|unknown` bedeutet nicht `no injury`, `no malfunction`, `user error`, `not reportable` oder Complaint Closure.
- **Customer resolution ≠ quality closure:** Ersatzlieferung, Refund, Troubleshooting-Erfolg oder Kundenzufriedenheit können einen Service-State schließen, aber weder Complaint Investigation noch Regulatory-/Vigilance-State.
- **Questions are neutral and purpose-linked:** Fragen sollen Facts erheben und dürfen den Kunden nicht zu gewünschter Causality, Outcome, Severity oder Product-Fault-Antwort führen.
- **Original voice is preserved:** relevante Antworten werden mit Originalaussage/Source/Receipt-Time erhalten; Übersetzungen oder strukturierte Zusammenfassungen bleiben davon getrennt.
- **Evidence preservation precedes destructive support:** bevor Reset, Firmware-/Software-Update, Reparatur, Desinfektion, Entsorgung, Device Return Processing oder andere verändernde Schritte empfohlen werden, wird geprüft, ob Logs, Einstellungen, Proben, Fotos oder Device Evidence für Complaint/Investigation/Regulatory Work erhalten werden müssen.
- **Minimum necessary data:** Patienten-/Anwenderdaten werden nur erhoben, wenn sie für Complaint-/Safety-/Regulatory-Zweck notwendig sind; unnötige Gesundheits-, Identitäts- oder Kontaktdaten werden nicht repliziert.
- **New material facts reopen decisions:** neue Outcome-, Safety-, Malfunction-, False-Result-, Usage-, Device-/Lot-, Market-, Remedial-Action- oder Timeline-Fakten werden als Delta markiert und können Complaint-/FDA-/IVDR-Reassessment auslösen.
- **Follow-up never delays time-critical escalation:** ein laufender Fragebogen, fehlende Antwort oder ausstehender Device Return blockiert keine bereits mögliche zeitkritische Regulatory-/Vigilance-Bewertung.
- **External communication is verified:** Draft/Plan/queued ≠ sent/delivered/answered. Nur belegte externe Kommunikation erhält einen entsprechenden State.

## Workflow

### 1. Complaint- und Gap-Kontext übernehmen

Konsumiere mindestens Complaint Reference, Product/Variant Context, Complaint State, Investigation State, bekannte Safety-/Performance-Fakten, Device/Evidence Availability, prior Contact/Follow-up Events, Missing Information und offene Regulatory-/Reassessment-References aus `medical-device-complaint-handling`.

Trenne:

- bekannte Facts,
- Unknowns,
- bereits angefragte aber unbeantwortete Punkte,
- technisch nicht mehr beschaffbare Information,
- Information, die vorhanden aber noch nicht verifiziert ist.

### 2. Follow-up Need und Priorität bestimmen

Klassifiziere jeden Informationsbedarf mindestens als:

- `not-needed`,
- `routine-followup`,
- `priority-followup`,
- `time-critical-parallel-followup`,
- `evidence-preservation-first`,
- `cannot-obtain|declined|unknown`.

Dokumentiere pro Punkt den Zweck: z. B. Event Chronology, Patient/User Outcome, Device Identification, Usage Context, False Result/Clinical Consequence, Malfunction Description, Environment, Existing Logs/Photos, Return Availability oder Follow-up Contact Permission.

Follow-up-Priorisierung darf wirtschaftlichen Kundenwert, Lautstärke oder kommerzielle Eskalation nicht als Ersatz für Quality-/Safety-Relevanz verwenden.

### 3. Frage- und Kontaktplan erzeugen

`customer-followup-plan.json` enthält nur Fragen/Aktionen, die einen dokumentierten Gap adressieren. Für jede Frage:

- Gap/Question ID,
- Zweck,
- neutrale Formulierung,
- benötigte Granularität,
- notwendige personenbezogene Daten oder `none`,
- Priorität/Time-Criticality,
- Evidence-Preservation-Hinweis,
- Owner/Channel,
- Stop/Escalation Condition.

Vermeide suggestive Fragen wie „War das Gerät schuld?“ oder „Es gab keine Verletzung, richtig?“. Frage stattdessen beobachtbare Tatsachen, Zeitpunkt, Outcome und konkrete Nutzungssituation ab.

### 4. Support-/Return-Interventionen absichern

Vor einem verändernden Support-Schritt prüfe mindestens:

- müssen Logs/Fehlercodes/Settings exportiert oder fotografiert werden,
- muss Device-/Lot-/UDI-Identität bestätigt werden,
- sind Proben/Verbrauchsmaterialien/Verpackung relevant,
- darf ein Device repariert, gereinigt, zurückgesetzt oder aktualisiert werden,
- braucht ein Return/RMA eine Evidence-Preservation-Instruktion,
- gibt es eine bereits laufende Investigation oder Regulatory-Anforderung.

Wenn unklar, setze `preservationHold=true` für den verändernden Schritt und eskaliere an Complaint/Investigation Owner. Dies ist kein pauschales Verbot notwendiger sicherheitsbezogener Sofortmaßnahmen; Safety Advice und Evidence Preservation werden gemeinsam dokumentiert.

### 5. Kommunikation ausführen lassen und Evidenz erfassen

Der Skill erstellt Plan/Draft, führt aber keine E-Mail, Telefonaktion oder Portalkommunikation selbständig aus. Für tatsächliche Kontaktversuche dokumentiere:

- Attempt ID,
- Channel,
- `attemptedAt|sentAt|deliveredAt|answeredAt` nur mit Evidence,
- Original Response Reference,
- Response Facts,
- neue Unknowns,
- Data-Minimization/Consent Context soweit relevant,
- Device/Evidence Return State.

Mehrere Kontaktversuche bleiben getrennt; ein fehlgeschlagener Versuch wird nicht als Kundenverweigerung umetikettiert.

### 6. Evidence Delta klassifizieren

Vergleiche neue Information gegen den letzten Complaint-/Regulatory-Evidence Snapshot. Klassifiziere:

- `no-new-information`,
- `clarification-only`,
- `material-complaint-update`,
- `investigation-impact`,
- `regulatory-reassessment-trigger`,
- `risk-pms-impact`,
- `unknown-review-required`.

Bei neuen materiellen Fakten referenziere alte und neue Evidence-Version; überschreibe keine frühere Complaint- oder Reportability-Entscheidung.

### 7. Kontrolliert zurückgeben

`customer-followup-evidence.json` geht mit Complaint Reference, New Facts/Unknowns, Evidence Delta, Prior Decision References und Reassessment Trigger zurück in den Complaint-/Regulatory-Workflow.

- Complaint Record/Investigation → `medical-device-complaint-handling`
- jurisdiction-spezifisches Reassessment → `medical-device-complaint-regulatory-routing`
- zeitkritischer Specialist State bleibt unabhängig offen; Customer Follow-up wartet ihn nicht ab
- Risk/PMS/CAPA werden nur über ihre bestehenden Owner aktualisiert

Der Rückkanal ist temporal: Follow-up ist downstream des aktuellen Complaint-State und liefert neue Evidenz für eine spätere Version desselben kontrollierten Falls. Deshalb wird kein zyklischer `requires`-Graph erzeugt.

## Output-Verträge

`customer-followup-plan.json` enthält Complaint/Gaps, Follow-up Need, Question/Action IDs, neutrale Formulierungen, Purpose, Data-Minimization, Priority, Evidence-Preservation, Owner/Channel und Stop/Escalation Conditions.

`customer-followup-evidence.json` enthält Attempt/Response References, immutable Receipt Chronology, Original-Response References, New Facts/Unknowns, Evidence Delta Classification, Device/Return/Preservation State, Prior Decision References und Reassessment Trigger.

`customer-communication-record.json` enthält Draft/Approved/Sent/Delivered/Answered State getrennt, verwendete kontrollierte Message Version, External Evidence Reference und Customer-Service-Resolution-State. Er enthält keine erfundene Reportability-/Vigilance-Closure.

## Memory Path

Persistenzwürdig sind abstrahierte, validierte Follow-up-Question-Patterns, Evidence-Preservation-Heuristiken, Gap-Typen und wiederverwendbare neutrale Kommunikationsmuster. Konkrete Complaint IDs, Kunden-/Patienten-/Anwenderdaten, Originalantworten, Contact Details, Device/Lot/UDI, aktuelle Contact Attempts, offene Investigation-/Reportability-States und Return-Tracking bleiben kontrollierte Records/run-only. Regulatory/Quality Learnings benötigen `sourceRefs`, `asOf` und bei volatilen Regeln `reviewAfter`. Nur geeignete abstrahierte `memory-candidate-handoff-v1`-Kandidaten gehen an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- Follow-up-Kriterien aus dokumentierten Gaps/Quality-/Safety-Relevanz abgeleitet und konsistent angewendet werden,
- Fragen neutral und zweckgebunden sind,
- Nicht-Antwort nicht in ein negatives Safety-/Complaint-/Reportability-Faktum umgedeutet wird,
- Service Resolution nicht als Complaint-/Regulatory-Closure gilt,
- potenziell relevante Logs/Device Evidence vor verändernden Support-/Return-Schritten geprüft werden,
- zeitkritische Regulatory-/Vigilance-Eskalation nicht auf Customer Follow-up oder Device Return wartet,
- neue materielle Fakten versioniert Complaint-/Regulatory-Reassessment auslösen können,
- externe Customer Communication nicht ohne Evidence als gesendet/zugestellt/beantwortet behauptet wird,
- personenbezogene Daten minimiert und nicht unnötig in Handoffs/Memory kopiert werden,
- konkrete Complaint-/Customer-/Patient-/Device-Zustände nicht in globales dauerhaftes Memory gelangen.
