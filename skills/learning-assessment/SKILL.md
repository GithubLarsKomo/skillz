---
name: learning-assessment
description: Bewertet beobachtete Lern-, ETF- oder Praxisevidenz gegen eine learning-assessment-spec und leitet daraus eine begründete Kompetenzempfehlung ab. Verwenden nach Retrieval, Anwendung, Transfer, ETF-ReviewEvents, Prüfung oder realer Aufgabe; aktualisiert den dauerhaften learning-state nicht selbst und behandelt Prozentwerte nicht automatisch als Kompetenz.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: draft
owners:
  - GithubLarsKomo
requires:
  - learning-assessment-spec
outputs:
  - learning-assessment.json
---

# Learning Assessment

## Zweck

Dieser Skill interpretiert tatsächliche Leistungsevidenz gegen eine vorab definierte `learning-assessment-spec.json`. Er beantwortet: **Welche Kompetenz ist durch diese Evidenz tatsächlich belegt, welche nicht, und warum?**

Er verändert den dauerhaften `learning-state` nicht direkt. Dadurch bleiben Bewertung und Zustandsmutation getrennt und überprüfbar.

## Eingaben

Mindestens:

- `learning-assessment-spec.json`,
- beobachtete Evidenz,
- stabile Evidenzreferenzen.

Mögliche Evidenzquellen:

- dialogische Antworten,
- strukturierte Aufgaben,
- ETF ReviewEvents,
- ETF Exam-Zusammenfassungen,
- reale Arbeitsprodukte,
- Mentor-/KOL-Feedback,
- nachprüfbare Ausführungsergebnisse.

## Grundregeln

### Evidenzniveau begrenzt Kompetenzniveau

- Recall kann Retrieval belegen.
- Repräsentative Anwendung kann Anwendung belegen.
- Ausreichend neue, nicht nur oberflächlich variierte Aufgaben können Transfer belegen.

**Die Bewertung darf nie höher sein als das tatsächlich beobachtete Evidenzniveau.**

### Prozentwerte sind Hilfsdaten

Ein hoher Score kann wichtig sein, aber der Skill muss prüfen:

- welche Items/Kompetenzen der Score abdeckt,
- ob kritische Fehler vorlagen,
- ob das Assessment Retrieval, Anwendung oder Transfer gemessen hat,
- ob die Evidenz breit genug war.

`92 %` ist daher kein eigenständiger Kompetenzstatus.

### Selbstbewertung ist Kontext, nicht Wahrheit

Selbstbewertung wie „gewusst/unsicher/nicht gewusst“ kann wertvolle Evidenz liefern, insbesondere für Unsicherheit und Metakognition. Sie darf strukturierte oder beobachtbare Leistungsdaten jedoch nicht heimlich überschreiben.

## Ablauf

### 1. Spec und Evidenz abgleichen

Prüfe zuerst, ob die Evidenz überhaupt zur Zielkompetenz, zum Assessment-Typ und zum erlaubten Unterstützungsgrad passt.

Wenn eine Aufgabe mit mehr Hilfe gelöst wurde als die Spec erlaubt, kennzeichne die Evidenz als begrenzt statt sie vollständig anzurechnen.

### 2. Required Evidence prüfen

Bewerte jedes in der Spec geforderte Evidenzmerkmal einzeln:

- erfüllt,
- teilweise erfüllt,
- nicht erfüllt,
- nicht beobachtbar.

### 3. Kritische Fehler prüfen

Ein kritischer Fehler kann einen ansonsten hohen Gesamtscore entwerten, wenn er die Kernkompetenz betrifft. Begründe dies konkret statt pauschal „durchgefallen“ zu melden.

### 4. Evidenzbreite prüfen

Wenn weniger unabhängige Beobachtungen vorliegen als die Spec benötigt, lautet das Ergebnis `insufficient-evidence`, nicht automatisch `failed`.

### 5. Kompetenzempfehlung ableiten

Zulässige Empfehlungen:

- `no-change`,
- `promote-to-retrieval-demonstrated`,
- `promote-to-application-demonstrated`,
- `promote-to-transfer-demonstrated`,
- `regression-or-reassessment-needed`.

Die Empfehlung ist Input für `learning-state`; sie ist selbst noch keine Mutation.

### 6. Fehlvorstellungen und Muster markieren

Wenn Fehler konsistent auf eine falsche Regel oder ein falsches mentales Modell hindeuten, darf der Skill eine `misconceptionCandidate` formulieren. Er muss klar zwischen beobachtetem Fehler und interpretierter Ursache unterscheiden.

Bei ETF-Diagnostik wie repeated failure, uncertainty, slow recall oder leech state darf Teach diese Signale nutzen, aber nicht daraus ohne semantische Prüfung eine Ursache erfinden.

## Ausgabe

`learning-assessment.json`:

```json
{
  "schemaVersion": 1,
  "missionId": "...",
  "competencyId": "...",
  "assessmentSpecRef": "...",
  "evidenceRefs": ["..."],
  "observedLevel": "retrieval|application|transfer|insufficient",
  "requiredEvidenceResults": [
    {
      "criterion": "...",
      "result": "met|partial|not-met|not-observed",
      "evidenceRefs": []
    }
  ],
  "criticalErrors": [],
  "evidenceSufficiency": "sufficient|insufficient|conflicting",
  "recommendation": "no-change|promote-to-retrieval-demonstrated|promote-to-application-demonstrated|promote-to-transfer-demonstrated|regression-or-reassessment-needed",
  "misconceptionCandidates": [],
  "reason": "..."
}
```

## ETF-Integration

ETF bleibt Eigentümer von ReviewEvent-Persistenz, Scheduler und Exam-Session-Mechanik. `learning-assessment` konsumiert nur die für die semantische Beurteilung erforderlichen Events oder Zusammenfassungen.

Ein ETF ReviewEvent mit `source=learning` und ein Exam-Review mit `source=exam` bleiben unterscheidbar. Der Skill darf diese Herkunft nicht zusammenwerfen, wenn sie für Interpretation oder Evidenzstärke relevant ist.

## Konflikte

Bei widersprüchlicher Evidenz:

1. prüfe Aktualität, Schwierigkeit und Vergleichbarkeit,
2. bewahre beide Evidenzstränge,
3. setze `evidenceSufficiency=conflicting`, wenn keine belastbare Auflösung möglich ist,
4. empfehle gezielte Reassessment-Evidenz statt einen Mittelwert als Wahrheit auszugeben.

## Formale Trainingsgrenze

Auch ein starkes Assessment belegt nur den in der Lernmission definierten pädagogischen Kompetenzzustand. Es erzeugt keine formale Zertifizierung, QMS-Qualifikation oder regulatorische Autorisierung.

## Fehlerbehandlung

- Fehlt eine Assessment-Spec, darf keine nachträgliche opportunistische Bestehensregel erfunden werden.
- Fehlen stabile Evidenzreferenzen, ist die Bewertung nicht dauerhaft promotierbar.
- Ist die Aufgabe nicht ausreichend neu, darf sie keinen starken Transfernachweis begründen.
- Enthält ein Gesamtscore kritische Fehler, müssen diese sichtbar bleiben.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn jedes geforderte Evidenzmerkmal bewertet, kritische Fehler und Evidenzbreite berücksichtigt, Konflikte sichtbar gehalten, eine level-konsistente Kompetenzempfehlung erzeugt und keine direkte Zustandsmutation oder formale Qualifikationsbehauptung vorgenommen wurde.
