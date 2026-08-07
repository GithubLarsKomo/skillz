---
name: regulatory-change-monitoring
description: Erkennt belastbare Änderungen an offiziellen Regulatory-Quellen über versionierte Snapshots, Status-/Inhalts-Deltas und Freshness und übergibt normalisierte Change Events an bestehende Regulatory-Impact-Owner.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - research-to-evidence-note
  - regulatory-evidence-traceability
outputs:
  - regulatory-source-register.json
  - regulatory-change-events.json
  - regulatory-change-watch-status.json
lastEvaluated: 2026-08-07
---

# Regulatory Change Monitoring

## Zweck und Grenze

Dieser Skill erkennt nachvollziehbare Änderungen an offiziellen regulatorischen Quellen und überführt sie in normalisierte Change Events. Er pflegt dafür einen evidenzgebundenen Source Register, vergleicht aktuelle und vorherige bestätigte Snapshots, trennt Status-/Metadaten-/Inhaltsänderungen und dokumentiert Freshness, Unsicherheit und Recheck-Bedarf.

Er ist **kein** allgemeiner Webcrawler, keine Produkt-Impact-Bewertung und kein automatischer Legal-/Regulatory-Decision-Maker. Der Skill sagt nicht, dass eine Guidance-Änderung automatisch einen Product Change, eine Submission oder CAPA auslöst. Produkt-/Prozess-/Marktauswirkung bleibt beim `regulatory-change-impact-orchestrator` bzw. zuständigen Regulatory Specialist.

## Kernprinzipien

- **Authoritative source first:** relevante Änderungen werden auf offiziellen/autoritativen Primärquellen verifiziert; Blogs, Newsletter oder Suchsnippets können Discovery auslösen, sind aber nicht alleinige Change-Evidence.
- **Snapshot identity is explicit:** Quelle, URL/Document ID, Status, Version/Revision, Veröffentlichungs-/Effective Date soweit vorhanden, Abrufdatum und Content Fingerprint bleiben unterscheidbar.
- **Metadata change is not automatically substantive change:** geändertes Datum, Layout oder Download-Link ist nicht automatisch eine regulatorisch materielle Inhaltsänderung.
- **Draft, final and superseded stay distinct:** Statusänderungen werden explizit behandelt und Draft Guidance wird nicht als bindende Finalregel ausgegeben.
- **Unknown beats invented diff:** wenn alte oder neue Primärevidenz nicht verfügbar ist, bleibt der konkrete Inhaltsdelta `unknown` statt aus Sekundärquellen geraten zu werden.
- **Detection is not impact:** ein bestätigtes Regulatory Change Event ist Input für eine spätere Impact-Bewertung, nicht deren Ergebnis.

## Workflow

### 1. Source Register definieren

Erfasse pro überwachte Quelle mindestens:
- Authority/Organization,
- Jurisdiction/Market,
- Source Type (`law|regulation|guidance|standard-reference|official-program-document|form|database-page|other`),
- canonical URL oder Document ID,
- Topic/Capability Tags,
- Current Status/Version soweit bestätigt,
- expected/known update semantics,
- Owner,
- lastVerifiedAt,
- nextReview/reviewAfter.

Der Register speichert keine Credentials und behauptet keine Update-Frequenz ohne Grundlage.

### 2. Current Snapshot erfassen

Nutze die aktuelle autoritative Quelle und dokumentiere:
- Source Reference,
- retrieval timestamp,
- publication/version/effective/status fields,
- relevante strukturierte Metadaten,
- Content Fingerprint bzw. geeignete stabile Vergleichsmerkmale,
- Source Availability/Access State.

Lange urheberrechtlich geschützte Texte werden nicht vollständig repliziert; speichere Referenzen und erforderliche strukturierte Deltas.

### 3. Previous Snapshot validieren

Verwende nur einen vorherigen Snapshot mit nachvollziehbarer Source Identity und Provenance. Wenn Identität, Version oder Herkunft unklar ist, klassifiziere den Vergleich als `baseline-uncertain`.

### 4. Delta klassifizieren

Mindestens:
- `no-change`,
- `metadata-only`,
- `status-change`,
- `new-version-or-revision`,
- `substantive-content-change-confirmed`,
- `source-added`,
- `source-withdrawn-or-superseded`,
- `access-or-location-change`,
- `change-detected-content-not-yet-characterized`,
- `baseline-uncertain`.

Dokumentiere, welche Felder/Evidence den Delta tragen. Keine semantische Inhaltsänderung aus Hash-/Layout-Differenz allein ableiten.

### 5. Regulatory Change Event erzeugen

Nur bei bestätigter oder klar zu triagierender Änderung erzeuge:
- Event ID,
- Authority/Jurisdiction,
- Source/Previous Snapshot References,
- Change Type,
- publication/effective/status dates soweit bestätigt,
- concise verified change summary,
- potentially affected capability/domain tags,
- uncertainty/open questions,
- `asOf`,
- urgency hypothesis,
- required specialist route.

### 6. Routing

- MDCG-spezifische aktuelle Guidance-/Applicability-Fragen → `mdcg-guidance-navigator`
- Evidence-Synthese/Quellenkonflikt → `research-to-evidence-note`
- Produkt-/QMS-/PMS-/Submission-/Lifecycle-Impact → `regulatory-change-impact-orchestrator`
- marktbezogene Legal/Regulatory Interpretation → jeweiliger FDA-/EU-/anderer Specialist Owner.

Der Monitoring-Skill schließt keine Lifecycle-Gates selbst.

### 7. Watch Status pflegen

`regulatory-change-watch-status.json` führt pro Source `current|change-open|triage-open|baseline-uncertain|source-unavailable|superseded|review-due` sowie letzte Verification, nächste Review, offene Questions und Event References.

Eine geplante zukünftige Prüfung wird nur als Plan/State dokumentiert; tatsächliche periodische Ausführung benötigt einen autorisierten Scheduler/Workflow außerhalb dieses Skills.

## Output-Verträge

`regulatory-source-register.json` enthält Source Identity, Authority/Jurisdiction, Type, Topic Tags, version/status references, Verification/Freshness State, Owner und Review Trigger.

`regulatory-change-events.json` enthält Previous/Current Evidence References, Change Classification, verified summary, dates/status, uncertainty, capability/domain tags, urgency hypothesis und downstream route.

`regulatory-change-watch-status.json` enthält Monitoring State, lastVerifiedAt, reviewAfter, access/baseline gaps und offene Events.

## Memory Path

Persistenzwürdig sind stabile Source-Identity-Muster, validierte Change-Klassifikationsheuristiken und abstrahierte Authority-/Topic-Routing-Patterns. Aktuelle Versionsstände, momentane Guidance-/Form-/Program-States, unbestätigte Änderungen, aktuelle Impact Decisions und volatile Fristen bleiben run-only bzw. versionierte Regulatory Knowledge Records mit Freshness. Regulatory Memory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`; übergib nur abstrahierte `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- Change Evidence auf autoritativen Quellen beruht,
- Previous und Current Snapshot eindeutig referenzierbar sind oder Baseline-Uncertainty sichtbar bleibt,
- Metadata-/Location-Deltas nicht automatisch als substantive Inhaltsänderung behandelt werden,
- Draft/Final/Superseded-Status getrennt bleibt,
- unbekannte Inhaltsdeltas nicht aus Sekundärquellen erfunden werden,
- Detection und Product/Lifecycle Impact getrennt bleiben,
- periodische Ausführung nicht ohne realen Scheduler als erfolgt behauptet wird,
- volatile aktuelle Regulatory States nicht als zeitloses globales Memory persistiert werden.
