---
name: procedure-sop-extractor
description: Rekonstruiert aus multimodaler Videoevidenz einen nachvollziehbaren Ablauf mit Zweck, Voraussetzungen, Materialien, Schritten, Kontrollpunkten, Warnungen, Akzeptanzkriterien und Troubleshooting und kennzeichnet jeden Punkt als observed, derived oder recommended. Verwenden für Anleitungen und SOP-Entwürfe aus Demonstrationsvideos; nicht zur Freigabe einer regulierten oder sicherheitskritischen Unternehmens-SOP ohne externe Validierung.
---

# Procedure / SOP Extractor

## Zweck

Überführe eine tatsächlich gezeigte oder erklärte Vorgehensweise in eine reproduzierbare **derived instructional SOP**.

## Evidenzklassen

Jedes Element trägt genau eine Klasse:

- `observed`: im Video direkt gesagt oder gezeigt;
- `derived`: aus mehreren beobachteten Elementen logisch rekonstruiert;
- `recommended`: als Best Practice ergänzt, aber nicht aus dem Video belegt.

`recommended` darf niemals so formuliert werden, als stamme es vom Videoautor.

## Struktur

`derived-procedure.json` unterstützt:

- Purpose;
- Scope;
- Preconditions;
- Required materials/tools;
- Safety/warnings;
- Procedure steps;
- Expected result pro Schritt;
- Critical control points;
- Acceptance criteria;
- Troubleshooting;
- Evidence/timestamps;
- Gaps requiring validation.

Ein Schritt enthält mindestens `id`, `action`, `status`, `evidence`, `timestamp`, optional `parameter`, `expectedResult`, `warning`, `visualRef`.

## Rekonstruktionsregeln

- Reihenfolge aus Zeitablauf und expliziter Logik ableiten.
- Mengen, Zeiten, Drehmomente, Temperaturen, Einstellungen oder Toleranzen **nicht erfinden**.
- Visuell gezeigte, aber nicht benannte Parameter nur so präzise beschreiben, wie sie erkennbar sind.
- Fehlt ein sicherheits- oder qualitätskritischer Parameter, markiere den Ablauf als `incomplete-for-controlled-use`.
- Varianten und optionale Schritte nicht zu einem scheinbar eindeutigen Standard verschmelzen.
- Bei Software-UIs Zustand vor Aktion, Aktion und erwarteten Zustand nach Aktion trennen.

## Regulierter / sicherheitskritischer Kontext

Ein Video kann einen SOP-Entwurf liefern, aber keine kontrollierte Freigabe ersetzen. Für QMS-/IVD-/Labor-/Produktionskontext gilt:

`derived instructional SOP -> fachliche Verifikation -> controlled-quality-documentation -> Approval/Effective State`

Ohne diese Schritte darf das Artefakt nicht als freigegebene Unternehmens-SOP bezeichnet werden.

## Qualitätsgate

- jeder Schritt besitzt Evidenz oder ist als `recommended` markiert;
- kritische Lücken sind explizit;
- keine fehlenden Parameter ergänzt;
- Warnungen und Kontrollpunkte sind nicht durch Kürzung verloren;
- Quell-Timestamps sind vorhanden;
- Freigabestatus wird nicht vorgetäuscht.

## Abschluss

Abgeschlossen, wenn ein Leser klar erkennt, was tatsächlich beobachtet, was abgeleitet und was zusätzlich empfohlen wurde und welche Punkte vor kontrollierter Nutzung noch validiert werden müssen.
