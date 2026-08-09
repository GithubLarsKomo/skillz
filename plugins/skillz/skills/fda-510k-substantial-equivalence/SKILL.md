---
name: fda-510k-substantial-equivalence
description: Baut eine evidenzgebundene 510(k)-Substantial-Equivalence-Bewertung aus Intended Use, technologischen Merkmalen, Safety/Effectiveness-Fragen und Performance-Daten.
---

# FDA 510(k) Substantial Equivalence

## Zweck und Grenze

Dieser Skill baut eine nachvollziehbare Substantial-Equivalence-(SE)-Bewertung für einen 510(k)-Kandidaten gegen einen ausgewählten Predicate. Er bildet die FDA-Entscheidungslogik evidenzgebunden ab: Intended Use, technologische Merkmale, mögliche different questions of safety and effectiveness sowie die Performance-Evidenz, die Unterschiede trägt.

Er erstellt **keine FDA-Clearance**, trifft keine Behördentscheidung und assembliert noch keine vollständige eSTAR-/510(k)-Submission. Ein positives internes Assessment bleibt `SE-hypothesis`, bis FDA tatsächlich eine SE-Order erteilt.

## Kernprinzipien

- Same Intended Use ist ein eigener Gate-Schritt und darf nicht durch technische Ähnlichkeit kompensiert werden.
- Technologische Merkmale werden systematisch verglichen; Unterschiede sind nicht automatisch NSE.
- Bei unterschiedlichen technologischen Merkmalen wird explizit geprüft, ob **different questions of safety and effectiveness** entstehen.
- Performance-Daten müssen die relevanten Unterschiede adressieren und zeigen, dass das neue Device gegenüber dem Predicate ausreichend sicher und wirksam ist; bloße Tabellenähnlichkeit reicht nicht.
- Product Code, Regulation Number oder Predicate Clearance allein beweisen keine SE.
- Aktuelle finale FDA-Guidance, device-spezifische Guidance und anwendbare Standards werden von Draft-/informativen Quellen unterschieden.
- Risk Management liefert Safety-/Failure-Mode-Kontext, ersetzt aber nicht die FDA-SE-Entscheidungslogik.

## Workflow

### 1. Predicate und Scope fixieren

Übernimm den bevorzugten Predicate aus `fda-510k-predicate-strategy` einschließlich Legal-Marketing-Basis, Product Code/Regulation, Intended Use, Technologie, bekannte Unterschiede, Source References und offene Fragen.

### 2. Intended Use Gate

Vergleiche Intended Use und Indications for Use strukturiert. Klassifiziere `same|potentially-same-with-differences|different|uncertain`. Ein klar anderer Intended Use blockiert eine positive SE-Hypothese; Ambiguität bleibt offen und wird nicht durch technische Daten überspielt.

### 3. Technological Characteristics Matrix

Vergleiche relevante Merkmale, z. B. Design, Funktionsprinzip, Energie/Signal, Materialien, Software, Reagenzien/Analyte, Specimen, Leistungsbereich, Sterilität oder andere device-spezifische Dimensionen. Markiere `same|different|unknown|not-applicable` plus Source/Evidence Reference.

### 4. Different-Questions-Analyse

Für jeden materiellen Unterschied formuliere:

- welche Safety-/Effectiveness-Frage dadurch betroffen sein könnte,
- ob diese Frage bereits durch den Predicate-/Device-Type-Kontext abgedeckt ist oder qualitativ neu ist,
- welche Evidenz die Einordnung trägt,
- welches Restrisiko/Uncertainty verbleibt.

Status mindestens `no-different-question-supported|potential-different-question|different-question|insufficient-evidence`.

### 5. Performance Evidence Map

Ordne Bench-, Analytical-, Software-, Electrical-, Biocompatibility-, Human-Factors-, Animal-, Clinical- oder sonstige relevante Daten den Unterschieden und Fragen zu. Die Evidenzart richtet sich nach Device Type und Difference; der Skill erzwingt keine universelle Testliste.

### 6. SE-Hypothese ableiten

Pro Decision Point und insgesamt sind mindestens `supports-SE|partially-supports-SE|NSE-risk|blocked|inconclusive` zulässig. Eine interne positive Hypothese wird nur erzeugt, wenn Same-Intended-Use-Gate, Different-Questions-Analyse und erforderliche Performance-Evidenz konsistent getragen sind.

### 7. Gaps routen

Jeder Gap erhält einen fachlichen Owner:

- Predicate/Eligibility → `fda-510k-predicate-strategy`
- Classification/Product Code → `fda-device-classification-product-code`
- Performance-/Study-Evidence → zuständiger Engineering/Clinical/Analytical Skill
- Risk-/Failure-Mode-Frage → `medical-device-risk-management-iso14971`
- zentrale FDA-Auslegungsfrage → `fda-qsub-strategy` / FDA Regulatory Strategy
- kein tragfähiger Predicate / echte neue Safety-Effectiveness-Fragen → De-Novo-/andere Pathway-Bewertung statt erzwungener SE.

## Output-Verträge

`substantial-equivalence-assessment.json` enthält Predicate Reference, `asOf`, Intended-Use Gate, Technology Differences, Different-Questions Assessment, Performance-Evidence Coverage, Risk References, Gesamtstatus, Authority Boundary und Re-evaluation Trigger.

`substantial-equivalence-matrix.md` dokumentiert New Device vs Predicate side-by-side mit Intended Use, relevanten technischen Merkmalen, Unterschieden, Safety/Effectiveness-Fragen, Evidenz und Schlussstatus.

`se-evidence-gaps.json` enthält Gap-ID, Decision Point, Difference/Question, benötigte Evidenz, Impact, Owner/Next Skill, Stop Condition und Source References.

## Downstream

Primäre Consumer sind `fda-estar-submission-builder`, `fda-qsub-strategy` und der FDA Regulatory Front Door. Die spätere Submission darf die Matrix verwenden, muss aber ihre eigenen aktuellen Format-/Acceptance-Anforderungen prüfen.

## Memory Path

Persistenzwürdig sind validierte produktspezifische Vergleichsdimensionen, robuste Different-Questions-Heuristiken und wiederverwendbare Evidence-Mapping-Muster. Aktuelle SE-Hypothesen, momentane Predicate-Auswahl, offene Gaps, aktuelle Guidance-Snapshots und unbestätigte FDA-Interpretationen bleiben run-only. Regulatory Candidates benötigen `sourceRefs`, `asOf` und bei veränderlichen Quellen `reviewAfter`. Übergib nur geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- Intended Use als eigenständiges Gate behandelt wird,
- alle materiellen technologischen Unterschiede sichtbar sind,
- different questions of safety and effectiveness explizit analysiert werden,
- Performance-Evidenz den konkreten Unterschieden/Fragen zugeordnet ist,
- Product Code oder Clearance des Predicate nicht als ausreichender SE-Beweis gilt,
- ein positives Ergebnis klar als interne SE-Hypothese und nicht FDA-Clearance gekennzeichnet ist,
- echte neue Fragen oder fehlender Predicate nicht in eine künstliche SE-Story gezwungen werden,
- aktuelle SE-Hypothesen nicht als dauerhaftes Memory-Faktum gespeichert werden.
