---
name: spoken-tutorial-listener-review
description: Prüft eine hörgerecht redigierte Tutorial-Fassung aus der Perspektive eines anspruchsvollen regelmäßigen Hörbuch- und Podcastnutzers, der ohne Bildschirm zuhört. Bewertet Verständlichkeit, Hörermüdung, Rhythmus, Wiederholung, Wiedereinstieg, Aufzählungen, Informationsdichte und natürliche Sprache und gibt ein hartes Freigabe-Gate für Audio-Tutorials aus. Nicht als Fakten- oder Fachreview verwenden.
---

# Spoken Tutorial Listener Review

## Zweck

Dieser Skill simuliert die Endabnahme durch einen **kritischen, erfahrenen Hörbuch- und Podcastnutzer**.

Die Prüfperspektive ist bewusst nicht die eines Autors, Lektors oder Fachexperten. Die Leitfrage lautet:

> Würde ein anspruchsvoller Hörer diesen Text über längere Zeit freiwillig weiterhören, verstehen und nach einer Unterbrechung wieder aufnehmen können, ohne auf einen Bildschirm schauen zu müssen?

Der Skill prüft die bereits fachlich und sprachlich redigierte Sprechfassung. Er erzeugt keine neuen fachlichen Claims und ersetzt weder `precision-writing-revision` noch `rewrite-fidelity-verifier`.

## Hörsituation

Standardannahme, sofern Grilling nichts anderes festlegt:

- Hören ohne Bildschirm;
- unterwegs, beim Spazierengehen, im Auto oder bei leichter Nebenbeschäftigung;
- regelmäßige Hörbuch-/Podcast-Erfahrung;
- geringe Toleranz für künstliche LLM-Rhetorik, monotone Wiederholungsmuster und unnötige Metasprache;
- Bereitschaft zu anspruchsvollen Inhalten, aber keine Bereitschaft, missverständliche Sätze mehrfach zurückzuspulen.

## Prüfdimensionen

### 1. Sofortige Orientierung

- Ist innerhalb der ersten Sätze klar, worum es geht?
- Beginnt jedes Kapitel mit ausreichender Orientierung?
- Ist nach einer Pause erkennbar, wo man sich befindet?

### 2. Hörverständlichkeit

- Funktionieren Sätze ohne visuelle Zeichensetzung?
- Sind Bezüge von Pronomen eindeutig?
- Werden Fachbegriffe und Abkürzungen beim ersten Auftreten verständlich eingeführt?
- Verlangen Sätze unnötig viel Arbeitsgedächtnis?

### 3. Informationsdichte

- Werden zu viele neue Gedanken in einem Satz oder Absatz kombiniert?
- Gibt es ausreichend semantische Atempausen?
- Werden komplexe Kausalitäten in einer hörbaren Reihenfolge erklärt?

### 4. Rhythmus und Prosodie-Tauglichkeit

- Wechseln Satzlängen natürlich?
- Erzeugen wiederholte Formeln einen mechanischen Rhythmus?
- Gibt es Stellen, die auf dem Papier gut aussehen, gesprochen aber sperrig klingen?
- Sind Kapitelübergänge natürlich und nicht formularhaft?

### 5. Wiederholung und Ermüdung

- Unterstützt Wiederholung das Lernen oder wirkt sie redundant?
- Wiederholen sich Metasätze wie `Die zentrale Schlussfolgerung lautet` oder `Im Folgenden` zu regelmäßig?
- Gibt es unnötige Zusammenfassungen unmittelbar nach bereits klaren Aussagen?
- Entsteht über mehrere Kapitel ein hörbarer Schabloneneffekt?

### 6. Aufzählungen, Zahlen und Struktur

- Werden Listen angekündigt und akustisch gegliedert?
- Sind lange Listen aufteilbar?
- Sind Zahlen, Abkürzungen und Zeichen TTS-tauglich?
- Wird kein visuelles Layout vorausgesetzt?

### 7. Wiedereinstieg und Kapitelarchitektur

- Sind Kapitel in sich sinnvoll abgeschlossen?
- Gibt es natürliche Stellen für Pause und Wiederaufnahme?
- Ist ein Wiedereinstieg nach mehreren Stunden ohne Rücklesen möglich?
- Sind Kapitel weder künstlich kleinteilig noch unnötig lang?

### 8. Sprachliche Natürlichkeit

- Klingt der Text wie gesprochene Fachsprache und nicht wie vorgelesene Berichtssprache?
- Deutsche Fassungen vermeiden unnötige Anglizismen und Beratungsjargon.
- Englische Fassungen entsprechen dem im Auftrag festgelegten Sprachstandard.
- Slang, Poesie oder Regionalität erscheinen nur bei entsprechendem Auftrag.

### 9. Motivation zum Weiterhören

- Gibt es eine erkennbare gedankliche Bewegung?
- Ist der Nutzen des nächsten Abschnitts nachvollziehbar?
- Bleibt der Ton sachlich, ohne trocken oder belehrend zu werden?
- Werden Schlussabschnitte wirklich konklusiv statt nur repetitiv?

### 10. Stimmenpassung

Auf Textebene beurteilen:

- welche Art Stimme und welches Tempo zum Inhalt passen;
- ob der Text starke Emotion, Dialog oder besondere Prosodie verlangt;
- ob die vorhandene Stimmenempfehlung zum Text passt.

Keine tatsächliche Audioqualität, Aussprache oder Stimmleistung behaupten, wenn nur der Text vorliegt.

## Findings

Jedes Finding enthält:

- `severity`: `minor|major|critical`;
- `dimension`;
- konkrete Textstelle oder Abschnitt;
- `listenerImpact`;
- konkrete Änderungsempfehlung;
- Kennzeichnung `requiredForPass: true|false`.

### Severity

**minor**  
Kurze lokale Reibung. Verständnis bleibt erhalten und Hörermüdung steigt nur gering.

**major**  
Wiederkehrende oder deutliche Hörbarriere, unnötige kognitive Last, starker Schabloneneffekt oder schlechter Wiedereinstieg. Muss vor Freigabe behoben werden.

**critical**  
Der Text ist in wesentlichen Teilen ohne visuelle Unterstützung nicht zuverlässig verständlich oder führt fachlich relevante Missverständnisse durch die Sprechform herbei.

## Gate

Output `gateStatus`:

- `pass`: keine offenen Major- oder Critical-Findings; Minor-Findings sind entweder behoben oder ausdrücklich nicht freigaberelevant.
- `minor_revision`: nur lokale Minor-Findings, die vor endgültiger Auslieferung sinnvoll korrigiert werden sollten.
- `major_revision`: mindestens ein Major-Finding.
- `fail`: mindestens ein Critical-Finding oder die Sprechfassung ist als Ganzes nicht sinnvoll beurteilbar.

**Der Audio-Tutorial-Workflow darf nur bei `gateStatus=pass` final freigeben.**

Nach jeder erforderlichen Überarbeitung wird der vollständige Listener Review erneut ausgeführt. Ein früheres PASS darf nicht auf eine geänderte Fassung übertragen werden.

## Output

`spoken-tutorial-listener-review.json` enthält mindestens:

```json
{
  "schemaVersion": 1,
  "reviewMode": "critical-audiobook-listener",
  "assumedListeningContext": "screenless",
  "gateStatus": "pass|minor_revision|major_revision|fail",
  "findings": [],
  "strengths": [],
  "listenerFatigueRisk": "low|medium|high",
  "resumeQuality": "good|mixed|poor",
  "voiceFit": {
    "status": "fit|review",
    "notes": []
  },
  "limitations": [
    "Text-based listener simulation; rendered voice/audio performance not directly assessed unless an audio artifact is separately available."
  ]
}
```

## Qualitätsregeln

- Kein Gefälligkeits-PASS.
- Fachliche Präzision nicht zugunsten vermeintlicher Lockerheit opfern.
- Nicht jede Wiederholung entfernen; didaktisch sinnvolle Wiederholung erhalten.
- Keine neue Metasprache ergänzen, um bestehende Metasprache zu ersetzen.
- Keine tatsächliche Aussprache-, Klang- oder Stimmqualität behaupten, wenn nur Text geprüft wurde.
- Findings müssen konkret genug sein, dass ein nachgelagerter Revisionslauf sie gezielt beheben kann.

## Abschluss

Abgeschlossen, wenn die Sprechfassung aus der definierten Hörsituation geprüft, alle Findings mit Severity versehen, die Ermüdungs- und Wiedereinstiegsrisiken bewertet und ein belastbarer Gate-Status ausgegeben wurde.
