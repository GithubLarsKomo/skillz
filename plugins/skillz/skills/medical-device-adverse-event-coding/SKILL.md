---
name: medical-device-adverse-event-coding
description: Normalisiert Medical-Device-/IVD-Complaint- und Adverse-Event-Fakten in versionierte IMDRF-/marktbezogene Code-Kandidaten mit Quellenbindung, ohne Codierung mit Kausalität oder Reportability zu verwechseln.
---

# Medical Device Adverse Event Coding

## Zweck und Grenze

Dieser Skill überführt belegte Complaint-/Investigation-/Adverse-Event-Fakten in **versionierte, quellengebundene Coding-Kandidaten**, insbesondere entlang der aktuellen IMDRF Adverse Event Terminology und – soweit anwendbar – aktueller marktbezogener Mappings wie FDA MDR.

Er besitzt weder Complaint Investigation noch Root Cause, Risk, PMS, Trend Detection, FDA MDR Reportability oder EU/IVDR Vigilance. **Coding ist eine strukturierte Beschreibung von Evidenz, keine regulatorische Entscheidung.** Der Skill darf eine zeitkritische regulatorische Bewertung nicht aufhalten, nur weil Coding unvollständig, unsicher oder noch nicht aktualisiert ist.

## Kernprinzipien

- **Narrative remains source of truth:** Originalnarrativ, Investigation Evidence und Outcome Facts bleiben primäre Evidenz; Codes referenzieren sie.
- **Current code set, not remembered list:** Code-Release, Source, Retrieval/Effective Context und `asOf` werden pro Coding-Lauf dokumentiert; statische eingebettete Code-Listen gelten nicht als zeitlos autoritativ.
- **Most specific supported, never invented specificity:** wähle die spezifischste durch Evidenz gestützte Codeebene; fehlende Details dürfen nicht durch einen präziseren Code erfunden werden.
- **Code ≠ cause:** Device-Problem-, Investigation- oder Component-Codes beweisen keine Kausalität.
- **Code ≠ reportability:** ein vorhandener oder fehlender Code entscheidet nicht über MDR/Vigilance.
- **Code ≠ severity shortcut:** Patient-/Health-Impact-Codes werden nur aus belegten Outcome-Fakten abgeleitet; unbekannter Outcome bleibt unbekannt.
- **One fact can support multiple orthogonal dimensions:** Device Problem, Investigation Type/Finding/Conclusion, Clinical Signs/Symptoms, Health Impact und Component bleiben getrennte Achsen.
- **Version changes are explicit:** neue Code-Release-/Mapping-Versionen oder neue Fallfakten erzeugen einen neuen Coding Snapshot/Delta statt stiller Überschreibung.
- **Deprecated/changed mapping stays historical:** frühere gültige Codierung bleibt mit damaligem Release nachvollziehbar; aktuelle Ausgaben referenzieren die neue Version.
- **Coding uncertainty is first-class:** `supported|candidate|ambiguous|insufficient-evidence|not-applicable|unknown` statt erzwungener Auswahl.
- **No coding gate before safety:** zeitkritische Complaint-Regulatory-Routing-/MDR-/Vigilance-Assessments laufen auch mit unvollständigem Coding.

## Trigger

Nutze den Skill, wenn Complaint-/Investigation-/Adverse-Event-Fakten für standardisierte interne Analyse, PMS-Aggregation, FDA-/EU-Berichtsvorbereitung oder interoperablen Datenaustausch normalisiert werden sollen.

Der Skill ist nicht erforderlich, um eine mögliche Safety-/Reportability-Frage überhaupt eskalieren zu dürfen.

## Voraussetzungen

- Complaint/Investigation Reference,
- Source-bound Event/Device/Outcome Facts soweit vorhanden,
- aktuelle autoritative Code-Set-/Mapping-Quelle für den Zielkontext,
- `regulatory-evidence-traceability` für Release-/Requirement-/Source-Provenance.

Fehlende Codequelle führt zu `codingBlockedBySource=true`, nicht zu erfundenen Codes. Fehlendes Coding blockiert keine regulatorische Eskalation.

## Ablauf

### 1. Coding Scope und Release fixieren

Erfasse:

- `codingSnapshotId`,
- Complaint/Investigation Reference,
- Zielkontext `IMDRF|FDA-MDR|EU-MIR-support|internal-PMS|other`,
- Code-System/Annex/Mapping Version,
- `sourceRefs`, `asOf`, Retrieval/Publication/Effective Dates soweit relevant,
- vorherigen Coding Snapshot soweit vorhanden.

Für IMDRF werden die jeweils aktuellen offiziellen Terminologie-Releases und Anhänge aufgelöst; für FDA wird die aktuell gültige FDA/IMDRF-Code-Unterstützung und Mapping-Lage geprüft. Der Skill konserviert keine Release-Nummer als dauerhaft gültige Wahrheit.

### 2. Evidenz in orthogonale Coding-Dimensionen zerlegen

Mappe nur soweit faktisch anwendbar:

- Device Problem / Event Problem,
- Investigation Type,
- Investigation Finding,
- Investigation Conclusion,
- Clinical Signs/Symptoms/Conditions,
- Health Impact,
- Medical Device Component,
- marktbezogene zusätzliche Felder/Mappings.

Ein fehlender Investigation-Abschluss verhindert nicht die Codierung bereits belegter Device-/Outcome-Fakten.

### 3. Kandidaten evidenzgebunden auswählen

Für jeden Code-Kandidaten dokumentiere:

- Code und Label,
- Dimension/Annex/System,
- unterstützende Source Fact References,
- `supportState`,
- Specificity Level,
- Alternative Candidates bei Ambiguität,
- fehlende Information für höhere Spezifität,
- Code-Release-/Mapping-Reference.

Verwende keine spezifischere Child-Kategorie, wenn die Evidenz nur den Parent trägt. Verwende keinen generischen Catch-all, wenn ein spezifischerer belegter Code existiert.

### 4. Investigation- und Causality-Grenze schützen

Investigation Type/Finding/Conclusion werden getrennt geführt. Insbesondere:

- ausgeführter Test ≠ Finding,
- Finding ≠ Root Cause,
- Root-Cause-Hypothese ≠ bestätigte Conclusion,
- Component Replacement ≠ bestätigter Component Failure,
- Problem Resolution after Service ≠ bestätigte Ursache.

Unklare Ursache kann mit belegtem Device Problem/Health Impact koexistieren.

### 5. Outcome Coding schützen

Health Impact und Signs/Symptoms stammen nur aus belegter Patient-/User-Outcome-Evidence. Bei fehlendem Outcome:

- keine implizite `no injury`-Codierung,
- kein Downgrade aus Non-response,
- `unknown`/`insufficient-evidence` erhalten,
- ggf. `medical-device-complaint-evidence-followup` für entscheidungsrelevante Daten nutzen.

### 6. Markt-Mapping getrennt anwenden

Wenn ein Zielsystem IMDRF-Terminologie mappt oder erweitert:

- dokumentiere Mapping Source/Version,
- trenne Original-IMDRF-Code von marktbezogenem Code/Representation,
- markiere unmapped/changed/deprecated States,
- erfinde keine 1:1-Entsprechung bei unklarer Mapping-Lage.

Ein FDA-kompatibler Code ist keine FDA-MDR-Reportability-Entscheidung. Ein MIR-kompatibler Code ist keine IVDR-Vigilance-Entscheidung.

### 7. Coding Delta bei neuer Evidenz oder Release erzeugen

Vergleiche mit vorherigem Snapshot:

- `unchanged`,
- `added`,
- `removed-with-rationale`,
- `refined`,
- `replaced-by-release-change`,
- `ambiguous`,
- `unknown`.

Neue Fallfakten und Code-System-Änderungen werden getrennt als Change Reason geführt. Frühere Snapshots bleiben auditierbar.

### 8. Downstream routen

- Complaint Record/Investigation → Coding Reference zurück an `medical-device-complaint-handling`.
- regulatorischer Faktenhandoff → `medical-device-complaint-regulatory-routing` kann Coding References ergänzend konsumieren, aber Routing nicht davon abhängig machen.
- FDA MDR → `fda-complaint-mdr-reportability` als strukturierte Zusatzinformation, keine Decision Override.
- IVDR Vigilance/MIR → `ivdr-pms-vigilance` als strukturierte Zusatzinformation, keine Decision Override.
- PMS → `medical-device-pms-system` für aggregierbare, versionskonsistente Kategorien; Trendbehauptung bleibt beim PMS-System.

## Prüfungen

Prüfe:

- stammt jeder Code aus einer aktuellen/kontextuell gültigen autoritativen Source,
- besitzt jeder Code konkrete Fact References,
- ist die Spezifität durch Evidenz gedeckt,
- bleiben Device Problem, Investigation, Conclusion, Outcome und Component getrennt,
- wird fehlender Outcome nicht als `no injury` kodiert,
- bleibt ein unvollständiges Coding non-blocking für zeitkritische Regulatory Assessment,
- sind Release-/Mapping-Änderungen versioniert statt still überschrieben.

## Fehlerbehandlung

- Code-Release nicht verifizierbar → keine Codebehauptung; `codingBlockedBySource=true`, Source-Gap eskalieren.
- Zwei plausible Codes → beide als Kandidaten mit Ambiguität/Evidence Gap, nicht willkürlich einen bestätigen.
- Alte Codierung passt neuer Terminologie nicht mehr → historischen Snapshot erhalten, neues Mapping separat dokumentieren.
- Narrative widerspricht späterem Investigation Finding → beide Evidence Sources erhalten; Coding Delta begründen.
- Kein Patient Outcome verfügbar → Unknown; kein Non-response-Downgrade.
- Coding fehlt, Safety-Fakten sind zeitkritisch → Regulatory Routing sofort weiterführen.

## Übergabe

`adverse-event-code-set.json` und Rationale werden ausschließlich als strukturierte Evidence-Layer referenziert. Complaint-, Regulatory- und PMS-Spezialisten behalten ihre Fachentscheidungen. Dieser Skill übermittelt keine Behördenmeldung und erzeugt keine Behauptung, ein Authority-Formular sei akzeptiert oder vollständig.

## Output-Verträge

`adverse-event-code-set.json` enthält Snapshot/Case References, Code-System/Release/Source, Zielkontext, je Dimension Code Candidates, Evidence Links, Support State, Specificity, Ambiguities, Unknowns und `asOf`.

`adverse-event-coding-rationale.json` enthält die Fact-to-Code-Begründung, Alternativen, ausgeschlossene Überpräzision, Mapping State und ausdrücklich getrennte Causality-/Reportability-Boundaries.

`adverse-event-coding-delta.json` enthält Prior Snapshot Reference, Change Reason (`new-evidence|release-change|mapping-change|correction|unknown`), Added/Removed/Refined Codes und unveränderte historische Provenance.

## Memory Path

Persistenzwürdig sind abstrahierte Coding-Methoden, validierte Fact-to-Dimension-Heuristiken und robuste Regeln gegen Overcoding. Konkrete Event-Codes einzelner Beschwerden, Patienten-/Reporter-/Geräte-/Lotdaten, aktuelle Code-Release-Snapshots und laufende Reportability-/Vigilance-Zustände bleiben run-only bzw. kontrollierte Regulatory/Quality Records. Code-System-Learnings benötigen `sourceRefs`, `asOf` und `reviewAfter`; nur abstrahierte `memory-candidate-handoff-v1`-Kandidaten gehen an `communication-memory-governance`.

## Abschlusskriterien

Bestanden nur wenn:

- Narrative/Evidence Source of Truth bleibt und Codes nur referenzierte Ableitungen sind,
- aktuelle autoritative Releases/Mappings statt erinnerter statischer Listen verwendet werden,
- die spezifischste **belegte**, nicht die maximal mögliche Codierung gewählt wird,
- Codes keine Kausalität, Schwere oder Reportability erfinden,
- unbekannter Outcome nicht als negative Evidenz kodiert wird,
- neue Fallfakten und Code-Release-Änderungen versionierte Deltas erzeugen,
- Coding niemals zeitkritische Complaint-/MDR-/Vigilance-Routingpfade blockiert,
- der Skill Complaint Investigation, PMS-Trending und jurisdiction-spezifische Reportability nicht dupliziert.
