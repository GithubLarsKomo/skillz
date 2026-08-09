---
name: research-to-evidence-note
description: Verdichtet eine klar abgegrenzte Recherchefrage und zugängliche Quellen zu einer zitierfähigen Evidenznotiz mit expliziter Quellenqualität, Aktualität, Widersprüchen, Unsicherheit und offenen Punkten. Verwenden, wenn Rechercheergebnisse belastbar an Meeting-Prep, Projektstatus, Dokumentproduktion oder Knowledge-Ingestion übergeben werden sollen, ohne Retrieval-, Connector- oder Drafting-Logik zu duplizieren.
---

# Research to Evidence Note

## Zweck und Grenze

Überführe eine **begrenzte Forschungsfrage** und eine Menge tatsächlich zugänglicher Quellen in eine nachvollziehbare Evidenznotiz. Der Skill bewertet und strukturiert Evidenz; er ist **kein eigener Browser, Suchanbieter, Connector, RAG-Ingestor oder Dokumentautor**.

Retrieval darf durch vorhandene Werkzeuge wie Websuche, GitHub, Drive, Datenbanken oder andere Connectoren erfolgen. Dieser Skill beginnt, sobald Frage und Quellen/Evidenzen vorliegen oder parallel gesammelt werden können, und definiert, wie daraus belastbare Aussagen entstehen.

## Trigger

Verwenden, wenn mindestens eines zutrifft:

- eine Recherche soll später zitierfähig weiterverwendet werden,
- mehrere Quellen müssen nach Qualität, Aktualität und Widerspruch geordnet werden,
- Fakten, Schlussfolgerungen und Unsicherheiten müssen getrennt bleiben,
- ein nachgelagerter Skill benötigt eine kompakte, überprüfbare Evidenzbasis.

Nicht verwenden, wenn nur eine einfache bekannte Tatsache ohne Quellenvergleich benötigt wird oder der primäre Auftrag bereits die Erstellung des finalen Memos, Berichts oder der Präsentation ist.

## Voraussetzungen

Vor der Synthese fixieren:

1. Forschungsfrage und beabsichtigte Entscheidung beziehungsweise Nutzung,
2. zeitlichen Geltungsbereich, falls Aktualität relevant ist,
3. verfügbare Quellen mit stabilen Referenzen oder nachvollziehbaren Herkunftsangaben,
4. bekannte Einschränkungen des Zugriffs oder der Datenbasis.

Wenn die Frage zu breit ist, enger formulieren. Fehlende Evidenz nicht durch plausible Annahmen ersetzen.

## Evidenzmodell

Behandle jede belastbare Aussage als Claim mit mindestens:

- `claim`: präzise Aussage,
- `support`: Quellenreferenzen, die den Claim stützen,
- `contradictions`: Quellenreferenzen, die widersprechen oder relevante Abweichungen zeigen,
- `confidence`: `high`, `medium` oder `low`,
- `basis`: `direct`, `derived` oder `unknown`,
- `notes`: Grenzen, Definitionen oder Kontext.

### Quellenqualität

Bewerte Quellen relativ zur Forschungsfrage, nicht nach Prestige allein:

- **primary**: Originaldaten, offizielle Dokumente, Standards, Gesetze, Primärpublikationen, Hersteller-/Projektquellen für eigene Eigenschaften,
- **strong-secondary**: belastbare Reviews, Fachinstitutionen oder hochwertige journalistische/fachliche Sekundärquellen,
- **contextual**: hilfreiche Einordnung, Community-Erfahrung oder nicht unabhängig bestätigte Sekundärangaben,
- **weak/unknown**: Herkunft, Methode oder Aktualität unklar.

Dokumentiere außerdem Veröffentlichungs-/Standdatum, soweit vorhanden, und ob die Quelle für die konkrete Frage noch aktuell genug ist.

## Ablauf

### 1. Frage und Entscheidungskontext fixieren

Formuliere die Forschungsfrage in einem Satz und notiere, wofür die Evidenz verwendet werden soll. Trenne ausdrücklich Kernfrage von interessanten Nebenfragen.

### 2. Quellen inventarisieren

Erzeuge für jede verwendete Quelle einen kurzen Record mit Referenz, Typ, Datum, Qualitätsklasse, relevanter Aussage und erkennbaren Einschränkungen. Quellen, die nur gefunden, aber nicht für einen Claim verwendet wurden, müssen nicht künstlich aufgeführt werden.

### 3. Claims extrahieren

Formuliere atomare Claims. Kopiere keine langen Quellpassagen. Trenne:

- direkt belegte Fakten,
- aus mehreren Fakten abgeleitete Synthesen,
- ungeklärte oder spekulative Punkte.

`derived` Claims benötigen eine nachvollziehbare Kette zu ihren direkten Evidenzen. Eine plausible Interpretation ohne diese Kette bleibt `unknown` beziehungsweise offener Punkt.

### 4. Widersprüche sichtbar halten

Bei widersprüchlicher Evidenz nicht mitteln oder die unbequemere Quelle verwerfen. Dokumentiere:

- welche Aussagen kollidieren,
- ob unterschiedliche Definitionen, Zeitpunkte oder Populationen den Konflikt erklären könnten,
- welche Evidenz für die konkrete Frage stärker ist,
- was zur Auflösung noch fehlt.

### 5. Confidence vergeben

Confidence ist eine Eigenschaft des Claims, nicht nur der Quelle.

- `high`: direkte, aktuelle und für die Frage passende Evidenz; wesentliche Widersprüche geklärt,
- `medium`: insgesamt tragfähig, aber relevante Einschränkung, indirekte Ableitung oder begrenzte unabhängige Bestätigung,
- `low`: dünne, veraltete, widersprüchliche oder nur kontextuelle Evidenz.

Keine numerischen Wahrscheinlichkeiten erfinden.

### 6. Synthese schreiben

Die Kurzsynthese darf nur Claims zusammenfassen, die in der Evidenzliste auftauchen. Markiere Unsicherheit sprachlich sichtbar. Trenne Ergebnis von Empfehlung: Eine Handlungsempfehlung muss erkennen lassen, welche Evidenz und welche Wert-/Risikoprämisse sie verbindet.

### 7. Offene Punkte ableiten

Liste nur offene Fragen auf, deren Beantwortung die Entscheidung oder die Confidence eines relevanten Claims ändern könnte. Vermeide generische „mehr Forschung nötig“-Formulierungen.

## Ausgabe

`evidence-note.json`:

```json
{
  "schemaVersion": 1,
  "question": "...",
  "decisionContext": "...",
  "asOf": "YYYY-MM-DD",
  "summary": "...",
  "claims": [
    {
      "id": "C1",
      "claim": "...",
      "basis": "direct",
      "confidence": "high",
      "support": ["S1"],
      "contradictions": [],
      "notes": "..."
    }
  ],
  "sources": [
    {
      "id": "S1",
      "reference": "...",
      "sourceClass": "primary",
      "date": "YYYY-MM-DD",
      "freshness": "current",
      "limitations": "..."
    }
  ],
  "conflicts": [],
  "openQuestions": [],
  "persistence": {
    "allowed": ["question", "claims", "source references", "non-sensitive synthesis"],
    "runOnly": ["credentials", "private raw connector payloads", "unnecessary personal data"]
  }
}
```

`evidence-note.md` enthält dieselben Inhalte lesbar gegliedert in Frage, Kurzantwort, Claims/Evidenz, Konflikte, offene Punkte und Quellen.

## Datenschutz und Persistenz

Speichere nur Informationen, die für die Evidenznotiz erforderlich und zulässig sind. Credentials, Tokens und private Rohantworten von Connectoren bleiben immer laufzeitgebunden. Personenbezogene oder vertrauliche Inhalte werden nur persistent übernommen, wenn sie für die Aufgabe erforderlich sind und der Zielkontext ihre Speicherung erlaubt; andernfalls abstrahieren oder weglassen.

## Prüfungen

Vor Übergabe prüfen:

- jeder relevante Synthesesatz ist durch mindestens einen Claim abgedeckt,
- jeder `direct`/`derived` Claim verweist auf existierende Quellen,
- widersprechende Evidenz ist sichtbar und nicht stillschweigend entfernt,
- Aktualität ist bei zeitabhängigen Fragen bewertet,
- Confidence folgt Evidenzqualität und Konfliktlage,
- keine Empfehlung wird als Fakt dargestellt,
- offene Punkte sind entscheidungsrelevant,
- persistierte Inhalte respektieren die Datenschutzgrenze.

## Fehlerbehandlung

Wenn zentrale Quellen nicht zugänglich oder die Evidenz für die Kernfrage unzureichend ist, liefere keine definitive Antwort. Erzeuge stattdessen eine partielle Evidence Note mit niedriger/ungeklärter Confidence und konkreten fehlenden Nachweisen.

Bei Quellenkonflikten mit ähnlicher Evidenzstärke bleibt der Konflikt offen. Bei veralteten Quellen für eine aktuelle Frage wird der Claim nicht allein durch historische Konsistenz auf `high` gesetzt.

## Übergaben

Geeignete nachgelagerte Verbraucher sind insbesondere:

- `meeting-preparation`: übernimmt bestätigte Claims und offene Entscheidungsfragen,
- `project-status-brief`: übernimmt belegte Status-/Risikoaussagen,
- `document-production`: übernimmt zitierfähige Evidenz statt Rohrecherche,
- `knowledge-ingestion`: übernimmt strukturierte Claims und Quellenreferenzen.

Diese Skills dürfen die Evidence Note erweitern, sollen aber deren Claim/Source-Trennung nicht auflösen.

## Qualitätsfälle

### Happy Path

Mehrere aktuelle Primär- und starke Sekundärquellen stimmen in der Kernfrage überein. Ergebnis: atomare Claims, hohe Confidence, klare Synthese und wenige entscheidungsrelevante offene Punkte.

### Grenzfall

Zwei hochwertige Quellen widersprechen sich aufgrund unterschiedlicher Zeitpunkte oder Definitionen. Ergebnis: Konflikt bleibt explizit, Confidence wird angepasst und die fehlende Auflösung wird konkret benannt.

### Fehlerfall

Eine vorgeschlagene Notiz übernimmt eine unbelegte Schlussfolgerung als Fakt, verschweigt eine widersprechende Quelle und nennt eine veraltete Community-Aussage „high confidence“. Stoppe und korrigiere Claim-Basis, Konflikt und Confidence.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Forschungsfrage und Entscheidungskontext fixiert sind, alle entscheidungsrelevanten Aussagen auf nachvollziehbare Claims und Quellen zurückgeführt werden können, Konflikte und Unsicherheiten sichtbar sind, Datenschutzgrenzen eingehalten werden und eine nachgelagerte Aufgabe die Evidence Note ohne erneute Rohrecherche verstehen kann.
