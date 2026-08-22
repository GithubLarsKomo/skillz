# Scoring model

## Ordering

1. identity validity
2. hard requirements
3. evidence sufficiency
4. criterion scores
5. confirmed weighting
6. winner classes
7. shortlist
8. sensitivity

## Scores

Criterion scores are 0–100 only when meaningful. Missing is not average. Utility is the weighted sum only when the configured model is complete enough to support it.

## Winner classes

Quality excludes price criteria but still respects hard budget ceilings. Price/performance uses the confirmed overall utility model. Bargain requires the configured fraction of Quality Winner quality utility, lower price, PASS gates, acceptable evidence and no material reliability blocker.

## Sensitivity and near ties

The deterministic default sensitivity method is a one-at-a-time weight shift of **±5 percentage points** (`sensitivityDelta: 0.05`). When one criterion changes, all remaining criterion weights are rescaled proportionally so the full weight vector continues to sum to 1.0. The delta is configurable when the decision context justifies a different plausible range.

Report both Quality Winner and Price/Performance Winner reversals. A reversal under any tested perturbation makes the corresponding winner unstable and reduces overall `rankingConfidence`.

Independently of winner reversal, compare the top two baseline candidates. The default `nearTieThreshold` is **1.0 utility point** on the 0–100 scale for both `qualityUtility` and overall `utilityScore`. A gap at or below that threshold is a near tie and reduces `rankingConfidence`, because a practically indistinguishable numerical lead must not be presented as a high-confidence unique winner. The threshold is configurable and must be reported in the sensitivity output.

The output should include the baseline winners, score margins, near-tie flags, stability flags, tested scenario count and every perturbation that changes a winner.

## Confidence

Never multiply utility by an invented confidence percentage. `evidenceCoverage`, score margins, sensitivity stability and `rankingConfidence` remain separate decision metadata. `rankingConfidence` is `low` when material input is incomplete, a winner changes under the configured perturbation range, or a winner falls within the configured near-tie threshold; otherwise the deterministic layer may report `high`.
