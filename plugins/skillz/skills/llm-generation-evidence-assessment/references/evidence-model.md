# Evidence Model for LLM Generation Review

## Grundsatz

Die Frage „Wurde dieses Dokument durch ein LLM generiert?“ ist in realen Arbeitsabläufen selten binär. Texte werden kopiert, redigiert, übersetzt, mit Templates kombiniert, aus anderen Formaten exportiert oder nur teilweise durch GenAI unterstützt. Das Modell bewertet deshalb **Evidenz für Beteiligung**, nicht eine metaphysische Alleinautorschaft.

## Evidenzhierarchie

### A. Direkte Provenienz — höchste Aussagekraft

Beispiele:
- verifizierbare Prompt-/Antwort-Protokolle, die Textstellen dem untersuchten Artefakt zuordnen,
- dokumentierte Copilot-/GenAI-Aktionen im relevanten Workflow,
- signierte oder anderweitig überprüfbare Provenienz-/Content-Credential-Spuren,
- unveränderte Projektartefakte, die Generator und konkreten Output verbinden.

Grenze: frei editierbare Metadaten oder ein bloßes `Creator=ChatGPT` sind manipulierbar und ohne Zusatzprüfung nicht ausreichend für `documented`.

### B. Workflow-Spuren — stark bis mittel

Entwurfsstände, Track Changes, Kommentare, Versionshistorien, Notizen, eingefügte Promptreste oder reproduzierbare Generatorartefakte können einen Entstehungsweg stützen. Die Aussagekraft steigt, wenn Zeitfolge und konkrete Textpassagen zusammenpassen.

### C. Author Voice — mittel, wenn gut kontrolliert

Ein belastbares Profil kann starke Abweichungen oder Übereinstimmungen zeigen. Voraussetzungen:
- authentische Referenzen,
- gleiche Sprache,
- vergleichbares Genre und Kommunikationsziel,
- ausreichend umfangreiches Korpus,
- dokumentierte Übersetzungs-/Redaktions-/Koautorenschaft.

Ein Mismatch kann auch aus Genrewechsel, Zeitdruck, Co-Authoring, Übersetzung oder professionellem Editing entstehen.

### D. Prose Patterns — schwach einzeln, mittel in unabhängigen Kombinationen

Nutze `llm-prose-pattern-audit` statt Wortlisten. Relevant sind kontextuelle Kombinationen wie Pseudoanalyse, Signifikanzinflation, mechanische Übergänge, syntaktische Gleichförmigkeit, Templatisierung oder Synonymdrift. Einzelne Wörter, Gedankenstriche, Dreierlisten oder Konnektoren sind keine belastbare Autorschaftsevidenz.

### E. Artefaktstruktur und Tooling — überwiegend Kontext

DOCX-/XLSX-/PPTX-/PDF-Metadaten können Generator- oder Konvertierungstools zeigen. `python-docx`, `openpyxl`, `python-pptx`, Pandoc, LibreOffice oder ReportLab belegen höchstens programmatische Erzeugung. Office-Master, konsistente Tabellen, wiederholte Formeln und saubere Slide-Layouts sind normale Eigenschaften professioneller Dokumente.

### F. Content Integrity — schwach bis mittel

Auffällige Quellen, erfundene Zitate, Platzhalter, unplausible Referenzen, nicht erklärbare Claims, inkonsistente Formeln oder nicht belegte Zahlen können zu einem generativen Workflow passen. Sie sind aber nicht LLM-spezifisch und benötigen unabhängige Stützung.

### G. Externe AI-Textdetektoren — ergänzend

Ein Detector-Score ist nur sinnvoll zusammen mit:
- Tool/Modell/Version,
- Sprache und Textlänge,
- Domäne,
- bekannter False-Positive-/False-Negative-Charakteristik,
- Information über Paraphrasierung, Übersetzung und Editing.

Ein Score ist **nicht** automatisch eine Wahrscheinlichkeit, dass der Text von einem LLM stammt.

## Korrelation vermeiden

Mehrere Merkmale können dieselbe Ursache haben. Beispiele:
- `rule-of-three` + drei Bulletpoints + drei gleichartige Slides → möglicherweise eine einzige Template-Ursache.
- Nominalstil + formeller Register + lange Nominalphrasen → möglicherweise regulatorisches Genre statt drei unabhängiger Indizien.
- ReportLab-Producer + PDF-Metadaten + gleichmäßige Seitengestaltung → ein automatischer PDF-Renderer, nicht drei LLM-Spuren.

Nur unabhängige Evidenzfamilien dürfen eine Bewertungsstufe gemeinsam anheben.

## Gegenindikatoren

Mögliche Gegen- oder Kontext-Evidenz:
- nachvollziehbare menschliche Entwurfs- und Revisionshistorie,
- belastbare Übereinstimmung mit einem authentischen Author-Voice-Profil,
- vollständige Quellen-/Berechnungsprovenienz,
- erklärbare Template-/Corporate-Language-Ursachen,
- formatbezogene Generatorhinweise ohne jeden LLM-spezifischen Bezug.

Gegenindikatoren beweisen nicht, dass überhaupt kein LLM beteiligt war. Sie reduzieren die Plausibilität einer **überwiegend oder direkt LLM-generierten** Entstehungshypothese.

## Hochrisiko-Anwendung

Bei akademischen Sanktionen, Personalmaßnahmen, Compliance-Vorwürfen, Rechtsstreit oder vergleichbar folgenreichen Entscheidungen:
- keine Entscheidung aus Stilmerkmalen oder einem einzelnen Detector,
- menschliche Zweitprüfung,
- möglichst direkte Provenienz oder mehrere unabhängige Belege,
- dokumentierte Alternativerklärungen,
- klarer Hinweis auf die methodischen Grenzen.

## Forschungsbasis

- NIST, *Reducing Risks Posed by Synthetic Content: An Overview of Technical Approaches to Digital Content Transparency*, NIST AI 100-4: https://doi.org/10.6028/NIST.AI.100-4
- NIST, *2024 NIST GenAI (Pilot Study): Text-to-Text Evaluation Overview and Results* (2025): https://www.nist.gov/publications/2024-nist-genai-pilot-study-text-text-evaluation-overview-and-results
- NIST GenAI Text 2026 challenge: https://ai-challenges.nist.gov/text-2026
- Tufts, Zhao & Li, *A Practical Examination of AI-Generated Text Detectors for Large Language Models*, Findings of NAACL 2025: https://aclanthology.org/2025.findings-naacl.271/
- Pudasaini et al., *Benchmarking AI Text Detection: Assessing Detectors Against New Datasets, Evasion Tactics, and Enhanced LLMs* (2025): https://aclanthology.org/2025.genaidetect-1.4/
- Skillz `llm-prose-pattern-audit/references/pattern-taxonomy.md` für die redaktionelle Musterbasis.

Die Literatur dient zur Kalibrierung von Grenzen und Evidenzgewichtung. Der Skill behauptet keine allgemeingültige Detektionsgenauigkeit.
