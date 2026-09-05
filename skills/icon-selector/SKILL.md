---
name: icon-selector
description: Wählt aus einer registrierten Icon-Bibliothek das semantisch passendste vorhandene Icon und eine zulässige Farb-/Kontrastvariante anhand von Intent, Kontext, Domain, Zielmedium und Hintergrund. Verwenden intern vor dem Platzieren von Icons in Präsentationen, Dokumenten oder anderen gebrandeten Artefakten; keine Icons erfinden, umzeichnen oder regulatorische/klinische Bedeutung aus einem Symbol ableiten.
userFacing: false
implicitInvocation: true
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - icon-selection.json
lastEvaluated: 2026-09-02
---

# Icon Selector

## Zweck

Dieser Skill verwandelt eine semantische Icon-Anfrage plus Brand-/Bibliothekskontext in genau eine begründete primäre Icon-Auswahl, zulässige Darstellungsparameter und höchstens wenige Alternativen. Er rendert, verändert und verteilt keine Icon-Binaries.

## Eingabe

Mindestens erforderlich:

- `intent` — was das Icon ausdrücken soll;
- `provider` oder genügend Brand-/Kontextinformation, um einen registrierten Provider zu bestimmen.

Optional:

- `context` — konkrete Aussage des Message-Blocks;
- `domain` — z. B. executive, laboratory, regulatory, IT, HR, sport, travel;
- `medium` — presentation, document, pdf, web;
- `background` — light, dark, photo;
- `statusMeaning` — falls das Icon einen Status begleitet;
- `criticalMeaning` — true, wenn Fehlinterpretation sicherheits-, regulatorisch- oder entscheidungsrelevant wäre;
- `exactProject`, `technique`, `portfolio` — explizite enge Semantik, wenn der Provider solche Klassen unterstützt;
- `designSystem` — bekannte Farb-/Stroke-/Size-Tokens für generische Provider.

## Provider

Vor Auswahl `references/provider-registry.json` lesen. Jeder Provider muss auf einen menschenlesbaren Systemvertrag und einen maschinenlesbaren semantischen Katalog zeigen.

Aktuell registriert:

- `euroimmun-corporate` -> `docs/corporate/euroimmun/ICON_SYSTEM.md` + `docs/corporate/euroimmun/icon-semantic-catalog.json`;
- `lucide-generic` -> `docs/icons/lucide/ICON_SYSTEM.md` + `docs/icons/lucide/icon-semantic-catalog.json`.

### Provider-Priorität

1. Explizit für die Aufgabe vorgegebener/approved Provider.
2. Registrierter Corporate-/Brand-Provider, dessen Brand-Alias eindeutig zum Kontext passt.
3. Explizit angeforderter `lucide-generic` Provider.
4. `lucide-generic` als impliziter Fallback nur für klar unbranded/generische Skillz-Artefakte, wenn keine Corporate Library, user-supplied Icon Family oder regulierte Spezialsemantik erforderlich ist.
5. Sonst `status = "unresolved-provider"`.

Ein generischer Provider darf einen passenden Corporate Provider niemals still verdrängen. Lucide ist insbesondere kein Ersatz für Brand-Logos, Project Icons, Zertifizierungszeichen oder regulatorische Symbole.

## Auswahlpriorität

Wenn der Provider spezielle Klassen unterstützt, zuerst die engsten provider-spezifischen Semantiken prüfen. Beim EUROIMMUN-Provider:

1. exakt benanntes Project-/Program-Icon nur für genau dieses Projekt;
2. exakte Technik-/Plattformsemantik;
3. Portfolio-/Indikationssemantik;
4. spezifischstes Essential-Icon;
5. generischer Fallback nur, wenn der Provider ihn ausdrücklich zulässt.

Beim generischen Lucide-Provider:

1. exakter Treffer in `preferredRouting`;
2. engster Treffer in `semanticDomains`;
3. gültiger Treffer aus Upstream-Tags/Aliases/Kategorien der profilierten Runtime-Version;
4. neutraler Lucide-Fallback nur nach dessen Provider-Vertrag.

Ein breiteres Icon darf ein verfügbares engeres Icon nicht verdrängen, nur weil es bekannter aussieht.

## Routing-Ablauf

1. **Provider auflösen.** Expliziten Provider, Brand-Aliases und generischen Kontext gegen Registry prüfen.
2. **Provider-Verträge laden.** Systemregeln und semantischen Katalog lesen.
3. **Intent normalisieren.** Aliases, Legacy-Schreibweisen und deutsch/englische Synonyme anwenden; kanonischen Asset-Namen nicht erfinden oder unnötig umbenennen.
4. **Enge Semantik prüfen.** Provider-spezifische Project/Technique/Portfolio-Klassen bzw. Preferred Routing zuerst behandeln.
5. **Kandidaten bilden.** Preferred-Routing, Alias-Treffer, semantische Kategorie und bei offenen Providern Upstream-Metadaten priorisieren.
6. **Existenz prüfen.** Der ausgewählte Name muss in der autorisierten Corporate Library oder in der profilierten/runtime-gebundenen Open-Provider-Version existieren. Nicht aus Namensintuition erfinden.
7. **Ambiguitäten auflösen.** Kontext und Domain verwenden; bei echter Bedeutungsunsicherheit nicht raten.
8. **Claim-Safety prüfen.** Icon darf keine regulatorische Freigabe, Intended Use, Performance, klinische Evidenz, Zertifizierung oder positiven Status implizieren, wenn dies nicht explizit belegt ist.
9. **Darstellung wählen.** Corporate Provider: nur zulässige supplied Variant. Lucide: `currentColor`/Stroke/Size aus aktivem Design-System nach Provider-Vertrag; keine neue Palette erfinden.
10. **Text-Redundanz markieren.** Bei `criticalMeaning=true` oder Status-/Risikoaussagen `requiresTextLabel=true` setzen.
11. **Output erzeugen.** Genau einen primären Treffer, maximal drei Alternativen und offene Unsicherheiten ausgeben.

## Ambiguitätsregel

Nicht nur lexikalisch matchen. Bedeutung schlägt Wortähnlichkeit.

Beispiele beim EUROIMMUN-Provider:

- strategisches Ziel -> `hit the bullseye`; analytische Präzision -> `Precision`;
- Literatur-/Evidenzsuche -> `magnifying glass`; Laborwissenschaft -> `microscope`;
- Programmrisko -> `risk protection`; geschützter Zugang -> `shield lock`;
- Laborautomation -> `automatic lab`; Portfolio-Automation -> `Automation`;
- Dokument/Dossier -> `Document`; Dateiformat explizit PDF -> `PDF`.

Beispiele beim Lucide-Provider:

- Ziel/Objectives -> `target`; gemessene Performance/Kapazität -> `gauge`;
- Suche/Information Retrieval -> `search`; Laborbeobachtung -> `microscope`;
- allgemeine Security -> `shield`; Access Control -> `lock`; Identität/MFA -> `fingerprint`;
- Reise/Flug -> `plane`; Route/Itinerary -> `route`; Ort -> `map-pin`;
- Training/Kraft -> `dumbbell`; Wettkampf/Sieg -> `trophy`; Auszeichnung/Resultat -> `medal`;
- Bericht/Dokument -> `file-text`; Lernen/Wissen -> `book-open`.

## Output Contract

`icon-selection.json` bleibt provider-neutral. Beispiel Lucide:

```json
{
  "schemaVersion": 1,
  "provider": "lucide-generic",
  "status": "selected",
  "request": {
    "intent": "training and strength",
    "context": "sport dashboard",
    "domain": "sport",
    "medium": "web",
    "background": "light",
    "criticalMeaning": false
  },
  "selection": {
    "canonicalName": "dumbbell",
    "family": "Lucide",
    "variant": "design-token",
    "assetStem": "dumbbell",
    "colorToken": "currentColor",
    "strokeWidth": 2,
    "sourceLicense": "ISC",
    "rationale": "Training/strength is narrower than competition or general activity semantics.",
    "confidence": "high",
    "requiresTextLabel": false
  },
  "alternatives": [],
  "warnings": []
}
```

Statuswerte:

- `selected`
- `ambiguous`
- `unresolved-provider`
- `no-approved-match`

Bei `ambiguous` keine scheinpräzise Primärauswahl erzwingen; Kandidaten und benötigte Kontextinformation angeben.

## Provider-spezifische Darstellungsmodelle

### EUROIMMUN Corporate

- supplied SVG variant vor eigenem Recoloring;
- Variant muss zu Hintergrund und Corporate Contract passen;
- proprietäre Runtime Assets nicht persistieren.

### Lucide Generic

- Geometrie/Styling gemäß `docs/icons/lucide/ICON_SYSTEM.md`;
- standardmäßig `viewBox 0 0 24 24`, `fill=none`, `stroke=currentColor`, `strokeWidth=2`;
- aktive Design-System-Farb-/Status-Tokens nutzen;
- keine neue Icon-Palette erfinden;
- bevorzugt framework-native/tree-shaken Lucide-Abhängigkeit oder gepinnte offizielle SVG/`@lucide/icons`-Quelle;
- verwendete Runtime-Version dokumentieren, wenn Reproduzierbarkeit relevant ist.

## Sicherheits- und Governance-Regeln

- Keine nicht vorhandenen Icons erfinden oder aus nicht registrierten Libraries beimischen.
- Keine proprietären Binaries in das öffentliche Skillz-Repo übernehmen.
- Keine SVGs umzeichnen, tracen oder gegen Provider-Vertrag recolorieren.
- Corporate Project Icons nie als generische Symbole zweckentfremden.
- Lucide nie als Fake-Brand-/Project-/Certification-Logo verwenden.
- Kritische Bedeutung nie nur durch Icon oder Farbe ausdrücken.
- Technik-/Indikations-/Medizinicons nie als Beleg für regulatorischen Status, Intended Use, Validierung, Diagnose oder Performance behandeln.
- Positiv konnotierte Statusicons nur bei tatsächlich positivem Status verwenden.
- Corporate Provider haben Vorrang vor `lucide-generic`, wenn der Brand-Kontext eindeutig ist.

## Fehlerbehandlung

- Provider unbekannt und Kontext nicht klar unbranded -> `unresolved-provider`.
- Corporate Provider passt, aber gewünschtes Corporate Asset fehlt -> nicht still zu Lucide wechseln; `no-approved-match` oder explizite Provider-Ausnahme erforderlich.
- Katalog/Vertrag fehlt -> `no-approved-match` plus fehlende Quelle nennen.
- Zwei semantisch gleich plausible Kandidaten -> `ambiguous`; keine willkürliche Auswahl.
- Lucide-Mapping existiert lokal, aber Name fehlt in der aufgelösten Runtime-Version -> Upstream-Alias/Metadata prüfen; sonst `no-approved-match`.
- Passender Corporate Name vorhanden, aber Variante für Hintergrund unzulässig -> alternative zugelassene Variante wählen; sonst `no-approved-match`.
- Intent würde einen unbelegten Claim erzeugen -> Auswahl verweigern oder neutrales Icon nur dann wählen, wenn der Provider dies semantisch trägt.

## Übergabe

Downstream-Skills verwenden `selection.canonicalName` und provider-spezifische Darstellungsfelder.

- Corporate/proprietär: tatsächliches Asset erst zur Laufzeit aus der autorisierten Bibliothek auflösen; keinen Dateipfad erfinden.
- Lucide/open: bevorzugt die im Zielprojekt vorhandene Lucide-Abhängigkeit oder eine gepinnte offizielle Quelle verwenden; Lizenz- und Versionsevidenz erhalten.

## Qualitätsgate

PASS nur wenn:

- Provider gemäß Prioritätsregeln korrekt aufgelöst ist;
- ausgewählter Name in der autorisierten Provider-Version/Bibliothek existiert;
- engste passende Semantik gewählt wurde;
- Darstellungsparameter mit Provider-/Design-System-Regeln kompatibel sind;
- Claim-Safety bestanden ist;
- kritische Bedeutung zusätzlich textlich abgesichert wird;
- Corporate/Generic Provider Isolation erhalten bleibt;
- proprietäre Binärdateien nicht persistiert und Open-Provider-Lizenzpflichten nicht entfernt wurden.

## Abschluss

Abgeschlossen ist der Skill, wenn ein valides `icon-selection.json` mit nachvollziehbarer Auswahl oder einem expliziten unresolved/ambiguous Status vorliegt.