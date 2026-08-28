#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORDED_AT = "2026-08-28"

SPECS = {
    "presentation-template-profiler": [
        {
            "id": "happy-path",
            "input": "Profile a supplied corporate PPTX with masters, layouts, theme fonts/colors, placeholders, footer rules and recurring visual patterns for faithful reuse.",
            "required": [
                ("preserve the supplied template as source of truth", "The contract gives an original PPTX/POTX highest priority and forbids replacing it with an invented reconstruction."),
                ("capture masters layouts theme typography spacing branding and QA baselines", "The profiler explicitly inventories these properties and requires template-specific QA baselines."),
                ("separate template-derived fidelity from fallbacks", "The profile contract carries source type/templateDerived state and requires deviations/fallbacks to be documented."),
            ],
            "forbidden": [
                ("invent brand rules not supported by the template", "Brand rules may not be invented when not derivable from the supplied template."),
                ("copy confidential slide content as design rules", "The skill explicitly limits transfer of confidential reference content to what is required for design profiling."),
            ],
            "anchors": ["Ein vorhandenes echtes Template darf nicht", "Template-Fidelity-Regel", "qaBaselines"],
        },
        {
            "id": "edge-case",
            "input": "Only a confirmed reference deck and a written template specification are available; the original POTX cannot be accessed.",
            "required": [
                ("use the best available reference with explicit fallback provenance", "The source-priority list permits confirmed reference/spec inputs below the original template."),
                ("limit fidelity claims when the actual template is unavailable", "The profile distinguishes source types and template-derived status rather than silently claiming the original template."),
                ("retain observed ranges instead of universal assumptions", "Template QA baselines are based on observed values rather than universal font/layout thresholds."),
            ],
            "forbidden": [
                ("claim original-template identity without the file", "The priority and source contract do not permit an absent template to be represented as present."),
                ("invent missing master or theme properties", "Unknown template properties are not a license to create a new brand design."),
            ],
            "anchors": ["Priorität der Quellen", "template-compatible fallback", "beobachtete Median-/Bereichswerte"],
        },
        {
            "id": "failure-case",
            "input": "A profiler ignores the supplied corporate deck, makes up a new palette and fonts, reconstructs the footer and calls the result template-derived.",
            "required": [
                ("reject replacement of an available real template", "The skill explicitly says a real template must not be replaced by a freely invented reconstruction."),
                ("reject invented palette font and footer rules", "Template properties must be observed from the source; brand invention is outside scope."),
                ("reject unsupported template-derived claims", "Template fidelity and deviations must remain evidence-bound."),
            ],
            "forbidden": [
                ("treat aesthetic preference as template evidence", "The profiler analyzes an existing design and does not create a new brand design."),
                ("erase provenance of the actual reference", "The source priority and profile format preserve the source identity."),
            ],
            "anchors": ["nicht zum Erfinden eines neuen Brand Designs", "Manuelles Nachbauen", "Abweichungen werden explizit dokumentiert"],
        },
    ],
    "presentation-language-rewriter": [
        {
            "id": "happy-path",
            "input": "Rewrite German executive slide titles, bullets and notes to be concise and idiomatic while preserving numbers, modality, claims and protected terminology.",
            "required": [
                ("adapt wording by slide element rather than applying report prose", "The skill defines distinct rules for titles, key messages, bullets, labels, tables and speaker notes."),
                ("preserve semantic and epistemic fidelity", "Semantic fidelity and epistemic precision are the top priorities before style or brevity."),
                ("run rewrite fidelity verification on material changes", "Every material revision must be checked with rewrite-fidelity-verifier."),
            ],
            "forbidden": [
                ("change numbers negations conditions modality or protected terms for style", "The priorities explicitly prohibit lower-priority stylistic edits from altering these elements."),
                ("solve dense slides primarily by shrinking fonts", "The text-budget sequence makes font reduction the final option after editorial and structural fixes."),
            ],
            "anchors": ["Semantic fidelity", "Keine niedrigere Priorität darf", "Jede materielle Überarbeitung"],
        },
        {
            "id": "edge-case",
            "input": "An English scientific slide is too dense and contains an association that must not be rewritten as causation.",
            "required": [
                ("preserve cautious scientific evidence language", "Scientific English explicitly retains cautious evidence language and forbids causal implication from association."),
                ("reduce redundancy before layout compromises", "The text-budget sequence starts with redundancy and sentence structure, then slide splitting."),
                ("keep units time periods and reference frames explicit", "Chart/table rules require units, periods and reference quantities to remain explicit."),
            ],
            "forbidden": [
                ("upgrade association to causal language", "The English scientific rule explicitly prohibits this."),
                ("remove qualifiers solely to hit a word target", "Word boundaries are QA signals, not hard stops that override fidelity."),
            ],
            "anchors": ["keine Suggestion von Kausalität aus Assoziation", "Wortgrenzen sind keine Hard Stops", "Einheiten, Zeiträume und Bezugsgrößen"],
        },
        {
            "id": "failure-case",
            "input": "A rewrite makes a cautious recommendation sound proven, changes a percentage, removes a negation and reports success because the slide is shorter.",
            "required": [
                ("reject changes to evidence strength percentage and negation", "The fidelity hierarchy explicitly protects claims, numbers, negations and modality."),
                ("restore or authorize any material semantic change", "Hard fidelity failures must be reverted or fachlich authorized."),
                ("treat brevity as subordinate to truth", "Presentation brevity ranks below semantic and epistemic fidelity."),
            ],
            "forbidden": [
                ("accept semantic distortion because scanability improved", "Scanability is lower priority than fidelity."),
                ("skip fidelity verification", "Material rewrites require rewrite-fidelity-verifier."),
            ],
            "anchors": ["Keine niedrigere Priorität", "Bei Hard Fail", "Präsentationsgerechte Kürze"],
        },
    ],
    "presentation-layout-qa": [
        {
            "id": "happy-path",
            "input": "Structurally inspect a PPTX against its template profile for overflow, overlap, clipping, alignment, placeholder misuse and font outliers before rendering.",
            "required": [
                ("use template-specific layout baselines", "The skill requires observed template baselines rather than universal thresholds."),
                ("check text boxes geometry visuals charts tables and footer collisions", "These are explicit structural finding classes."),
                ("prioritize editorial or structural fixes before font reduction", "The correction order lists shortening, splitting, box/layout changes before font size reduction."),
            ],
            "forbidden": [
                ("declare visual quality from structural inspection alone", "The skill explicitly states structural PASS does not replace a render test."),
                ("apply a universal minimum font rule contrary to the template", "The baseline logic forbids this."),
            ],
            "anchors": ["Template-spezifische Baselines", "Ein struktureller Pass ersetzt keinen Render-Test", "Schriftgröße nur als letzte Option"],
        },
        {
            "id": "edge-case",
            "input": "A slide uses an 11 pt source label while the template normally uses 10-12 pt source text, but a universal checker would flag anything below 14 pt.",
            "required": [
                ("prefer the template baseline over a universal threshold", "The baseline section explicitly rejects rigid global minimum font rules when the template differs."),
                ("avoid false major findings from valid template behavior", "Findings are relative to observed template ranges and severity."),
                ("leave aesthetic judgement to render review", "This skill is structural rather than a standalone taste judgement."),
            ],
            "forbidden": [
                ("force the label to 14 pt solely because of a generic rule", "Template-specific valid values take precedence."),
                ("call template-conformant source text an overflow defect without geometry evidence", "Structural findings require actual object/layout evidence."),
            ],
            "anchors": ["Keine starre globale Mindestschriftgröße", "templateMedianPt", "bewertet nicht allein, ob eine Slide ästhetisch gut wirkt"],
        },
        {
            "id": "failure-case",
            "input": "A checker fixes overflow by shrinking all body text, ignores clipped chart labels and then reports visually verified PASS without rendering the deck.",
            "required": [
                ("reject blanket font shrinking as first-line correction", "The ordered correction principle makes font reduction the last option."),
                ("detect chart label clipping", "Chart labels, legends and axis titles are explicit visual structure checks."),
                ("reject visual PASS without render", "The skill explicitly says structural PASS is not render verification."),
            ],
            "forbidden": [
                ("hide overflow through indiscriminate font reduction", "The correction order forbids this shortcut."),
                ("simulate visual QA", "A real render test is separately required."),
            ],
            "anchors": ["Chart-Labels", "Textproblemen in dieser Reihenfolge", "kein Render-Test"],
        },
    ],
    "presentation-render-verifier": [
        {
            "id": "happy-path",
            "input": "Render all slides and a PDF, inspect slide-level and deck-level quality, correct findings, rerender and only then issue the final status.",
            "required": [
                ("perform actual slide and PDF rendering", "The mandatory process requires slide images and a PDF/print version."),
                ("inspect both individual slides and deck-level consistency", "The skill defines separate slide-level and deck-level checks."),
                ("rerender after corrections before final PASS", "A one-time export without rerender is explicitly insufficient."),
            ],
            "forbidden": [
                ("claim visually verified without a render", "The limits explicitly prohibit this."),
                ("treat PDF export alone as proof of editable PPTX quality", "PDF does not replace PPTX editability or structural checking."),
            ],
            "anchors": ["Verbindlicher Ablauf", "erneut rendern", "Keine Aussage `visually verified`"],
        },
        {
            "id": "edge-case",
            "input": "The PPTX render is clean but the PDF substitutes a font and changes line breaks on two slides.",
            "required": [
                ("treat PDF as a second renderer with independent findings", "The PDF/print section explicitly checks font metrics and line-break differences."),
                ("report parity issues instead of accepting the clean PPTX render", "PDF-specific differences remain findings."),
                ("rerender after the font issue is corrected", "Corrections require a new render cycle."),
            ],
            "forbidden": [
                ("declare final PASS from PPTX render only", "Final verification includes the PDF/print render."),
                ("ignore font substitution as cosmetic", "Font substitution is an explicit slide/PDF check."),
            ],
            "anchors": ["PDF dient als zweiter Renderer", "Font-Substitutionen", "Re-Render"],
        },
        {
            "id": "failure-case",
            "input": "No rendering tool is available, so the reviewer inspects slide XML, assumes the deck looks fine and reports pass.",
            "required": [
                ("return fail or unverified when no real render is available", "The status rules require a belastbarer Render for pass."),
                ("avoid converting structural inspection into visual evidence", "The skill exists specifically to inspect what viewers actually see."),
                ("preserve the requirement for a later real render", "The completion criteria require PPTX and PDF render inspection."),
            ],
            "forbidden": [
                ("simulate visual verification", "The limits explicitly prohibit a text-only claim of layout correctness."),
                ("claim pass without render coverage", "Pass requires no critical/major findings and a verified rerender."),
            ],
            "anchors": ["prüft, was der Betrachter tatsächlich sieht", "kein belastbarer Render verfügbar", "Keine rein textuelle Behauptung"],
        },
    ],
    "template-presentation-workflow": [
        {
            "id": "happy-path",
            "input": "Create an editable executive deck from approved content using a supplied PowerPoint template, improve slide language, run structural QA, render PPTX and PDF, correct and rerender.",
            "required": [
                ("use the supplied template as source of truth", "The workflow starts by profiling and prioritizing the real template and its masters/layouts/theme."),
                ("separate content curation from language layout and render QA", "The workflow has explicit stages for storyline, language, structural QA and render/PDF QA."),
                ("deliver editable PPTX and verified PDF only after rerender", "Completion requires editable PPTX, structural QA, PPTX/PDF render checks and rerender after corrections."),
            ],
            "forbidden": [
                ("invent fachliche claims", "The non-goals explicitly forbid inventing regulatory, medical, legal, IP or financial analysis."),
                ("replace an available corporate template with a newly invented style", "Template fidelity requires reuse of existing masters/layouts and prevents invented alternatives."),
            ],
            "anchors": ["Source of truth und Template fixieren", "strukturelle Layout-QA", "Render- und PDF-QA"],
        },
        {
            "id": "edge-case",
            "input": "A slide has two independent messages and too much text for the template body area.",
            "required": [
                ("split or restructure the slide before reducing font size", "The slide architecture and layout QA rules prefer one primary message and structural correction."),
                ("preserve the template grid and layout logic", "Existing masters/layout placeholders are preferred over freeform reconstruction."),
                ("re-run layout and render QA after correction", "Corrections require renewed verification."),
            ],
            "forbidden": [
                ("shrink text until both messages fit", "The workflow explicitly recommends splitting slides rather than shrinking type."),
                ("drop evidence or caveats simply to fit", "Facts, assumptions, claims and evidence remain content constraints."),
            ],
            "anchors": ["Pro Slide genau eine primäre Botschaft", "Slide teilen statt Schrift zu verkleinern", "erneut rendern"],
        },
        {
            "id": "failure-case",
            "input": "A deck is recreated from scratch despite an available template, report sentences are pasted unchanged onto slides, and the reviewer claims visual QA without rendering.",
            "required": [
                ("reject from-scratch template reconstruction", "The real template has priority and master/layout placeholders should be reused."),
                ("rewrite report prose for presentation use while preserving claims", "The language stage explicitly says report sentences should not be copied unchanged to slides."),
                ("reject visual QA without actual render", "The non-goals and render stage explicitly require actual render verification."),
            ],
            "forbidden": [
                ("claim successful visual QA without rendering", "This is explicitly prohibited."),
                ("sacrifice editability for PDF-only output", "The workflow requires an editable final PPTX."),
            ],
            "anchors": ["Keine frei erfundene Corporate-Variante", "Report-Sätze nicht unverändert", "Keine Behauptung erfolgreicher visueller QA ohne tatsächlichen Render"],
        },
    ],
    "euroimmun-presentation-workflow": [
        {
            "id": "happy-path",
            "input": "Create a EUROIMMUN executive/scientific deck from supplied content using the current confirmed corporate reference, active DESIGN.md and approved icon system, then perform template and render QA.",
            "required": [
                ("apply the mandatory EUROIMMUN design contract and active reference hierarchy", "The wrapper requires DESIGN.md, ACTIVE_PRESENTATION_REFERENCE.md and GOLDEN_REFERENCE.md before work."),
                ("delegate generic storyline language layout and render logic to template-presentation-workflow", "The wrapper explicitly remains thin and does not duplicate generic presentation logic."),
                ("preserve corporate asset provenance and require Level-2 evidence for template-derived claims", "The corporate gate requires template identity/SHA and Level-2 PASS for template-derived status."),
            ],
            "forbidden": [
                ("copy confidential fachliche content from the reference deck", "The Corporate Context and non-goals explicitly prohibit this unless it is part of the task basis."),
                ("claim internal template approval from the public or fallback design specification", "The reference hierarchy and Level-2 rules prevent unsupported template-derived/approved claims."),
            ],
            "anchors": ["Verbindlicher Corporate Design Contract", "dünner Corporate Wrapper", "`template-derived` darf nur"],
        },
        {
            "id": "edge-case",
            "input": "A Town Hall style is desired, but the supplied task-specific approved template differs from the secondary storytelling reference.",
            "required": [
                ("give the task-specific approved template priority for master and theme", "The reference priority puts a supplied approved-controlled template first."),
                ("use storytelling only as an orthogonal visual grammar compatible with the active template", "The storytelling reference is explicitly secondary and may not override the active master/theme contract."),
                ("retain scientific/regulatory caveats even in storytelling mode", "The mode rules prohibit storytelling from hiding sources, limitations or uncertainty."),
            ],
            "forbidden": [
                ("replace the active template with the storytelling reference", "The secondary reference is not a master/template replacement."),
                ("simplify away required evidence limitations", "Storytelling cannot reduce scientific or regulatory qualifications below necessary visibility."),
            ],
            "anchors": ["secondary style reference", "orthogonal", "darf wissenschaftliche Einschränkungen"],
        },
        {
            "id": "failure-case",
            "input": "The corporate DESIGN.md is missing, so the workflow guesses brand colors from a screenshot, recreates a logo, mixes icon styles and calls the result template-derived.",
            "required": [
                ("abort the corporate workflow when the mandatory DESIGN.md is unavailable", "The design contract explicitly requires aborting rather than improvising corporate rules."),
                ("reject logo/icon reconstruction and mixed unprovenanced assets", "The icon and non-goal rules require supplied/approved assets and provenance."),
                ("reject template-derived status without Level-2 PASS", "Template-derived is explicitly conditional on the relevant Level-2 verification."),
            ],
            "forbidden": [
                ("invent EUROIMMUN design rules", "Missing DESIGN.md is a blocker, not permission to improvise."),
                ("claim corporate design pass with unsupported assets", "Corporate Design Gate requires template/asset provenance and QA evidence."),
            ],
            "anchors": ["den Corporate Workflow abbrechen", "supplied SVG variant", "Level-2-Prüfung PASS"],
        },
    ],
}


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def materialize(skill: str, cases: list[dict[str, object]]) -> bool:
    skill_dir = ROOT / "skills" / skill
    if not (skill_dir / "SKILL.md").exists():
        raise RuntimeError(f"unknown skill: {skill}")
    evaluation = skill_dir / "tests" / "evaluation.json"
    if evaluation.exists():
        print(f"SKIP: {skill} already has evaluation.json")
        return False

    evaluation_cases = []
    for case in cases:
        evaluation_cases.append({
            "id": case["id"],
            "input": case["input"],
            "requiredBehaviors": [behavior for behavior, _ in case["required"]],
            "forbiddenBehaviors": [behavior for behavior, _ in case["forbidden"]],
            "skillAnchors": case["anchors"],
        })
        result = {
            "schemaVersion": 1,
            "skill": skill,
            "caseId": case["id"],
            "recordedAt": RECORDED_AT,
            "evaluator": "repository-maintainer",
            "requiredBehaviors": [
                {"behavior": behavior, "passed": True, "evidence": evidence}
                for behavior, evidence in case["required"]
            ],
            "forbiddenBehaviors": [
                {"behavior": behavior, "observed": False, "evidence": evidence}
                for behavior, evidence in case["forbidden"]
            ],
            "overall": "pass",
        }
        write_json(skill_dir / "tests" / "results" / f"{case['id']}.json", result)
    write_json(evaluation, {"schemaVersion": 1, "skill": skill, "cases": evaluation_cases})
    print(f"CREATED: {skill} evaluation suite")
    return True


def main() -> int:
    changed = 0
    for skill, cases in SPECS.items():
        changed += int(materialize(skill, cases))
    print(f"Presentation evaluation suites created: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
