---
name: fda-510k-predicate-strategy
description: Findet und bewertet 510(k)-Predicate-Kandidaten evidenzgebunden auf rechtliche Vermarktbarkeit, Intended Use, Technologie, Safety/Performance und aktuelle FDA-Quellen.
---

# FDA 510(k) Predicate Strategy

## Zweck und Grenze

Dieser Skill identifiziert und bewertet Kandidaten für einen rechtlich zulässigen 510(k)-Predicate und erzeugt eine nachvollziehbare Predicate-Strategie. Er prüft Legal-Marketing-Basis, Intended Use, technologische Nähe, verfügbare Safety-/Performance-Informationen, Product Code/Regulation und aktuelle FDA-Quellen.

Er trifft **keine Substantial-Equivalence-Entscheidung** und erstellt keine 510(k)-Submission. Die finale SE-Argumentation gehört zu `fda-510k-substantial-equivalence`.

## Kernprinzipien

- Ein ähnliches Gerät ist nicht automatisch ein zulässiger Predicate.
- Same Product Code ist häufig ein starker Suchanker, aber weder notwendiger Alleinbeweis noch ausreichende SE-Begründung.
- Intended Use und rechtliche Vermarktbarkeit werden vor technologischer Detailnähe geprüft.
- Aktuelle 510(k)-, Classification-, De-Novo-/Downclassification- und andere offizielle FDA-Daten werden mit `asOf` dokumentiert.
- Draft Guidance bleibt Draft: Empfehlungen aus nicht finaler FDA-Guidance werden als `draft-recommendation`, nicht als verbindliche Zulässigkeitsregel, verwendet.
- Recall-, Safety- oder Performance-Historie ist ein Strategy-Faktor und kein automatischer rechtlicher Predicate-Ausschluss ohne entsprechende Rechts-/FDA-Grundlage.
- Reference Devices, falls fachlich nützlich, werden klar von dem Predicate getrennt, auf dem die SE-Behauptung beruht.

## Workflow

### 1. Suchbasis fixieren

Übernimm Product Context sowie Class/Regulation/Product-Code-Kandidaten aus `fda-device-classification-product-code`. Halte Intended Use, Indications, Technologie und zentrale Performance-/Safety-Fragen stabil.

### 2. Kandidaten finden

Suche aktuelle offizielle FDA-Quellen, insbesondere 510(k)- und Product-Classification-Daten, nach legal vermarkteten Geräten mit geeigneter regulatorischer und fachlicher Nähe. Dokumentiere Clearance-/Legal-Marketing-Basis und relevante Submission-/Product-Code-Referenzen.

### 3. Predicate Eligibility prüfen

Für jeden Kandidaten erfasse mindestens:

- Legal-Marketing-Basis,
- Intended Use/Indications,
- Device Type/Product Code/Regulation,
- technologische Merkmale,
- relevante Performance-/Safety-Information,
- verfügbare Labeling-/Summary-Daten,
- bekannte Limitationen der öffentlichen Evidenz,
- `asOf` und Source References.

Nicht ausreichend belegte Legal-Marketing-Basis führt zu `eligibility-uncertain`, nicht zu einer stillen Predicate-Annahme.

### 4. Fachliche Vergleichbarkeit screenen

Bewerte `same|similar|materially-different|unknown` für Intended Use und zentrale Technologie-/Performance-Dimensionen. Technologische Unterschiede werden nicht schon hier als SE-fähig erklärt; sie werden für den SE-Skill strukturiert.

### 5. Strategy-Faktoren ergänzen

Berücksichtige aktuelle finale FDA-Guidance sowie klar gekennzeichnete Draft-Empfehlungen. Bei Verwendung der FDA-Predicate-Best-Practice-Draft-Faktoren werden deren Draft-Status und Nicht-Verbindlichkeit explizit erhalten.

### 6. Kandidaten ranken

Ordne `preferred-predicate|viable-alternative|reference-only|weak-candidate|ineligible|uncertain`. Ranking beruht auf Legal Eligibility, Intended Use, regulatorischer Nähe, technologischer Vergleichbarkeit und verfügbarer Evidenz; reine Clearance-Aktualität oder Product-Code-Gleichheit entscheidet nicht allein.

### 7. Handoff an SE

Übergebe einen Preferred Predicate plus Alternativen, Unterschiede, offene Safety/Effectiveness-Fragen und benötigte Performance-Evidenz an `fda-510k-substantial-equivalence`. Wenn kein tragfähiger Predicate erkennbar ist, eskaliere an FDA Regulatory Strategy / De Novo statt einen schwachen Predicate zu erzwingen.

## Output-Verträge

`predicate-candidate-set.json` enthält Kandidaten-ID, FDA-Submission-/Device-Referenz, Legal-Marketing-Basis, Product Code/Regulation, Intended-Use-Vergleich, Technologievergleich, Strategy-Faktoren, Source References, Freshness und Candidate Status.

`predicate-strategy.md` dokumentiert Suchstrategie, Auswahlkriterien, bevorzugten Predicate, Alternativen, verworfene Kandidaten, Draft-vs-Final-Guidance-Kontext, zentrale Unterschiede, offene Evidenzfragen und den Übergabepunkt an SE.

## Downstream

Primärer Consumer ist `fda-510k-substantial-equivalence`. Unklare FDA-Fragen können an `fda-qsub-strategy` bzw. FDA Regulatory Strategy gehen. Fehlt ein geeigneter Predicate, ist `fda-de-novo-strategy` ein möglicher nächster Pfad; dies wird nicht durch den Predicate-Skill selbst entschieden.

## Memory Path

Persistenzwürdig sind validierte produktspezifische Predicate-Suchräume, robuste Ausschluss-/Disambiguierungsheuristiken und wiederverwendbare Vergleichsdimensionen. Aktuelle Candidate Rankings, Clearance-/Recall-Snapshots, Draft-Guidance-Status, offene Eligibility-Fragen und vorläufige Preferred-Predicate-Entscheidungen bleiben run-only. Regulatory Candidates benötigen `sourceRefs`, `asOf` und bei veränderlichen Daten/Guidance `reviewAfter`. Übergib nur geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- Legal-Marketing-Basis jedes ernsthaften Kandidaten belegt ist,
- Intended Use vor technologischer Detailähnlichkeit bewertet wurde,
- Product-Code-Gleichheit nicht als ausreichender Predicate-Beweis verwendet wird,
- Draft Guidance eindeutig als Draft/Not-for-Implementation behandelt wird,
- Reference Devices und Predicate-Rolle getrennt bleiben,
- kein finaler SE-Schluss im Predicate-Skill vorweggenommen wird,
- fehlender tragfähiger Predicate sichtbar zu Strategy/De Novo eskaliert wird,
- aktuelle Candidate-Rankings nicht als dauerhaftes Memory-Faktum gespeichert werden.
