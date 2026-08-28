---
name: learning-artifact-qa
description: Prüft HTML-, PPTX-, DOCX- und PDF-Lernartefakte sowie ihre SVG-/Bildassets gemeinsam gegen das kanonische Learning-Modell, Timestamp-/Claim-Traceability, SOP-Evidenzklassen, DESIGN.md und vollständige Render-Evidenz. Verwenden als finales Cross-Format-Gate; nicht als Ersatz für fachliche Quellanalyse.
---

# Learning Artifact QA

## Zweck

Ein Lernpaket gilt erst als final, wenn Inhalt, Visuals und alle angeforderten Formate dieselbe semantische Basis transportieren.

## Kanonische Referenz

Berechne bzw. dokumentiere einen Fingerprint des finalen `learning-content-model.json`. Jeder Renderer muss genau diese Revision referenzieren.

## Gates

### A. Claim Traceability

- jeder Key Takeaway auf Evidence Claim(s);
- wichtige Zahlen/Einheiten auf Quelle;
- Timestamp-Map gültig;
- keine neue Behauptung nur in einem Renderer.

### B. SOP Integrity

- `observed`, `derived`, `recommended` bleiben erhalten;
- Reihenfolge und kritische Warnungen identisch;
- keine Lücke durch Layoutkürzung entfernt;
- Controlled/approved status wird nicht vorgetäuscht.

### C. Visual Semantic Fit

- jedes Visual besitzt Lernbotschaft + Quellclaim;
- Source Frames und generierte Bilder sind unterschiedlich gekennzeichnet;
- Illustration wird nicht als Evidenz ausgegeben;
- SVG-Labels stimmen mit Content-Modell überein.

### D. Design Conformance

- gleiche autoritative DESIGN.md-Kette;
- konsistente Farben, Typografie und Visualgrammatik;
- Corporate Design Gate zusätzlich vollständig, wenn anwendbar.

### E. Format QA

**HTML:** Wide/Narrow, Links, Overflow, Accessibility, Print.

**PPTX:** `presentation-layout-qa` + `presentation-render-verifier`; jede Slide rendern, PDF-Export ebenfalls prüfen.

**DOCX/PDF:** vollständiger Seitenrender + Source/Parity-Prüfung.

### F. Cross-Format Fidelity

Vergleiche:

- Titel/Kernbotschaften;
- Takeaways;
- Zahlen/Einheiten;
- Warnungen;
- SOP-Schritte;
- offene Punkte;
- Source Map;
- Visual captions.

Kürzung ist erlaubt, Bedeutungsänderung nicht.

## Severity

- `critical`: falsche/fehlende Claims, Warnungen, SOP-Schritte, falsche Corporate Authority, ungeprüfter finaler Render;
- `major`: relevante Layout-/Lesbarkeits-/Visual-Semantikfehler;
- `warning`: dokumentierte nicht-materiale Abweichung.

PASS nur bei 0 offenen Critical/Major Findings und vollständiger Renderabdeckung der angeforderten Formate.

## Abschluss

Abgeschlossen, wenn `learning-artifact-qa` PASS für exakt die ausgelieferte Revision meldet.
