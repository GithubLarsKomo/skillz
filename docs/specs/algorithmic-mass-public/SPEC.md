# Algorithmic Mass–Public Model — Simulation Specification

Status: candidate  
Version: 0.1  
Date: 2026-09-12

## 1. Goal

Define a falsifiable agent-based model (ABM) for testing whether engagement-optimized social-media ranking can create a gap between:

1. **private opinion** — what individuals actually believe;
2. **public expression** — what they say or choose not to say;
3. **visible opinion climate** — what the platform shows;
4. **perceived opinion climate** — what users infer society believes; and
5. **civic responsibility willingness** — whether individuals remain willing to accept visible, responsibility-bearing roles.

The v0.1 model deliberately starts with **fixed private opinions**. It therefore cannot explain outcomes through persuasion or radicalization. Its first task is narrower and more diagnostic:

> Can engagement ranking plus empirically motivated expression and perception mechanisms create visible polarization, silence, preference falsification, norm distortion and selection out of civic responsibility even when private opinions do not change?

If the answer is no across plausible parameter ranges, the core hypothesis is weakened. If the answer is yes, later versions may add persuasion, network rewiring and institutional dynamics as separate mechanisms.

## 2. Scientific boundary

This specification does **not** claim to reproduce the proprietary ranking algorithm of Meta, TikTok, X, YouTube or another platform.

It models an abstract class of recommender systems in which predicted engagement contributes to content visibility. The model must keep separate:

- empirically supported mechanisms;
- theoretical mechanisms requiring calibration;
- exploratory assumptions;
- normative design choices in intervention conditions.

Classic mass-psychology theories are used as **construct generators**, not as empirical parameter sources. Parameters must be calibrated or bounded using modern behavioral, communication, network and recommender-system evidence.

## 3. Skillz architecture

Use existing Skillz capabilities rather than embedding research logic in the simulator:

```text
research question
  |
  v
research-to-evidence-note
  |-- empirical claims
  |-- source quality
  |-- contradictions
  `-- calibration bounds
  |
  v
algorithmic-mass-public model specification
  |
  +--> parameter set
  +--> preregistered hypotheses
  +--> experimental conditions
  +--> falsification criteria
  `--> run schema
  |
  v
throwaway-prototype
  |
  v
simulation implementation + verification
```

A dedicated reusable simulation skill should only be introduced after the model contract survives implementation and sensitivity testing.

## 4. Theory-to-mechanism mapping

| Theory / tradition | Model construct | v0.1 treatment |
|---|---|---|
| Gabriel Tarde — imitation / public | exposure, prestige-sensitive imitation, distributed public | mechanism prior; modern evidence required for parameterization |
| Gustave Le Bon — contagion / prestige | emotional salience and prestige increase interaction probability | retain only testable components; reject generic irrational-crowd assumption |
| Freud / later social-identity theory | identity congruence and out-group salience | operationalize primarily through modern Social Identity / SIDE evidence |
| Canetti | common adversarial target can synchronize otherwise heterogeneous agents | optional content feature; exploratory |
| Bernays | deliberate manipulation of visibility/prestige | intervention layer, not default endogenous mechanism |
| Noelle-Neumann | perceived opinion support affects willingness to speak | core expression mechanism |
| Timur Kuran | public expression can diverge from private preference under social pressure | core public/private divergence mechanism |
| Granovetter | heterogeneous activation thresholds can create nonlinear cascades | core threshold heterogeneity |
| Arendt | plural public space and withdrawal from public action | system-level outcome interpretation, not micro-psychology |

## 5. Empirical anchor set

The initial evidence baseline must include at least:

1. Lorenz-Spreen et al. (2023), *Nature Human Behaviour*, systematic review of digital media and democracy. DOI: `10.1038/s41562-022-01460-1`.
2. Milli et al. (2025), *PNAS Nexus*, engagement ranking, user satisfaction and amplification of divisive content. DOI: `10.1093/pnasnexus/pgaf062`.
3. Brady et al. (2023), *Nature Human Behaviour*, overperception of moral outrage and inferred intergroup hostility. DOI: `10.1038/s41562-023-01582-0`.
4. Matthes, Knoll & von Sikorski (2018), *Communication Research*, meta-analysis of the spiral of silence. DOI: `10.1177/0093650217745429`.
5. Granovetter (1978), *American Journal of Sociology*, threshold models of collective behavior. DOI: `10.1086/226707`.
6. Cabrera et al. (2021), *Journal of Business Economics*, agent-based spiral-of-silence model with community structure. DOI: `10.1007/s11573-021-01064-7`.
7. Sohn (2022; first online 2019), *Communication Research*, simulation of spiral of silence in networked media environments. DOI: `10.1177/0093650219856510`.
8. Ross et al. / Stieglitz line of work on agent-based spiral-of-silence and manipulative actors, including DOI: `10.1080/0960085X.2018.1560920`.
9. Germano, Gómez & Sobbrio (2026), *Journal of Public Economics*, dynamic feedback between engagement ranking, misinformation and polarization. DOI: `10.1016/j.jpubeco.2026.105589`.
10. *Modelling Public Opinion Dynamics: The Spiral of silence in clustered homophilic networks* (2026), *Chaos, Solitons & Fractals*. DOI: `10.1016/j.chaos.2025.117660`.
11. Kuran (1995), *Private Truths, Public Lies*, for preference falsification as theoretical structure.
12. Reicher, Spears, Postmes and later SIDE literature for social-identity effects in computer-mediated communication.

The evidence note must explicitly distinguish **directional support** from transportable numeric effect sizes. For example, the spiral-of-silence meta-analytic association (`r ≈ .10` overall) is a calibration target, not a coefficient that may be copied directly into a logistic decision rule.

## 6. Population and network

### 6.1 Population

Baseline:

- `N = 10,000` agents;
- private opinion `p_i ∈ [-1, 1]`;
- initial private-opinion distribution configurable as unimodal, weakly bimodal or asymmetric;
- no private-opinion updating in the core v0.1 experiment.

A useful default stress-test population is:

- 60% moderate / central;
- 20% leaning toward pole A;
- 20% leaning toward pole B;

but no substantive conclusion may depend on this single initialization.

### 6.2 Social graph

Use a stochastic block model or equivalent clustered graph with explicit homophily parameter `h`.

Baseline network properties:

- community count configurable;
- within-community tie probability > between-community tie probability;
- degree distribution recorded;
- network frozen in v0.1 to isolate ranking and expression effects.

Network rewiring, unfollowing and endogenous homophily are v0.2 extensions.

## 7. Agent state

Each agent `i` has at least:

```text
p_i       private opinion in [-1,1]                     [fixed in v0.1]
g_i       salient identity / community membership
iso_i     fear/cost of social isolation in [0,1]
conf_i    conflict tolerance in [0,1]
norm_i    sensitivity to perceived opinion climate [0,1]
neg_i     sensitivity to negative/arousing content [0,1]
out_i     sensitivity to out-group hostile content [0,1]
prest_i   prestige/social-proof sensitivity [0,1]
theta_i   expression/activation threshold [0,1]
kappa_i   preference-falsification susceptibility [0,1]
civic_i   willingness for civic responsibility [0,1]
fat_i     accumulated conflict fatigue [0,1]
harr_i    accumulated harassment exposure >= 0
```

Optional heterogeneity distributions must be declared before each run family and stored in the run artifact.

## 8. Content state

Each public item `j` contains at least:

```text
x_j        expressed stance in [-1,1]
neg_j      negativity/arousal in [0,1]
out_j      out-group hostility in [0,1]
prest_j    author/source prestige in [0,1]
proof_j    current social proof / interaction count
quality_j  optional epistemic-quality field; disabled in core experiment
age_j      content age
```

The core v0.1 model is about visibility and expression rather than misinformation, so `quality_j` is recorded but not used unless a dedicated extension is enabled.

## 9. Expression model

### 9.1 Perceived support

For agent `i`, perceived support for their private position at time `t` is derived from their observed feed rather than from the true population distribution:

```math
S_i(t) = Σ_j w_ij · sim(p_i, x_j) / Σ_j w_ij
```

where `sim` is a bounded opinion-similarity function and `w_ij` is exposure salience.

### 9.2 Speak utility

```math
U_speak,i(t) =
  a0
  + a1 · S_i(t)
  + a2 · conf_i
  - a3 · iso_i · (1 - S_i(t))
  - a4 · fat_i
  - a5 · ExpectedConflict_i(t)
  - theta_i
```

```math
P(speak_i(t)=1) = sigmoid(U_speak,i(t))
```

This is a computational implementation of heterogeneous willingness to express under perceived support and social cost. It is not claimed to be Noelle-Neumann's literal equation.

### 9.3 Preference falsification

If the agent speaks, expressed opinion may differ from private opinion:

```math
x_i(t) = clip[(1 - q_i(t)) · p_i + q_i(t) · M_i(t), -1, 1]
```

where `M_i(t)` is the perceived local opinion mean and

```math
q_i(t) = kappa_i · Pressure_i(t)
```

with `Pressure_i(t)` increasing with perceived isolation/conflict cost.

Silence and falsification are separate outcomes:

- `silent`: no expression;
- `truthful`: expression close to `p_i`;
- `falsified`: expressed stance moves materially toward perceived norm.

## 10. Engagement model

For each exposure of agent `i` to item `j`, define:

```math
Affinity_ij = 1 - |p_i - x_j| / 2
Conflict_ij = identity_outgroup(i,j) · |p_i - x_j| / 2
```

Expected interaction propensity:

```math
Z_ij =
  b0
  + b1 · Affinity_ij
  + b2 · neg_i · neg_j
  + b3 · out_i · Conflict_ij · out_j
  + b4 · prest_i · prest_j
  + b5 · log(1 + proof_j)
  + b6 · Novelty_j
```

Separate action heads may be used:

```math
P(like_ij)    = sigmoid(Z_ij + c_like)
P(comment_ij) = sigmoid(Z_ij + c_comment + c_conflict · Conflict_ij)
P(share_ij)   = sigmoid(Z_ij + c_share)
P(dwell_ij)   = bounded_dwell(Z_ij)
```

This allows both agreement-based engagement and conflict-driven engagement.

## 11. Ranking conditions

Exactly the same agents, graph, content-generation rules and seeds must be reusable across ranking conditions.

### Condition A — Chronological control

Visibility depends only on recency among eligible network/global-candidate content.

```math
Score_A(j) = -age_j
```

This is the principal no-engagement-ranking comparator.

### Condition B — Engagement ranking

```math
Score_B(i,j) =
  α · E[like_ij]
  + β · E[comment_ij]
  + γ · E[share_ij]
  + δ · E[dwell_ij]
  + η · Affinity_ij
  + ρ · Recency_j
```

The `α..ρ` weights are experimental parameters. No claim is made that they match a specific platform.

### Condition C — Pluralistic ranking

Condition C tests whether a ranking objective can retain utility while reducing visibility distortion:

```math
Score_C(i,j) =
  wE · EngagementScore_ij
  + wS · StatedPreferenceFit_ij
  + wD · ConstructiveDiversity_ij
  + wB · BridgingValue_ij
  - wH · OutgroupHostility_j
```

`StatedPreferenceFit` must be modeled separately from revealed engagement. `ConstructiveDiversity` must reward informative viewpoint diversity without merely maximizing ideological distance. `BridgingValue` rewards interactions predicted to cross group boundaries without hostility.

Condition C is a normative intervention and must not be presented as an empirically validated production algorithm.

## 12. Simulation cycle

For each discrete time step `t`:

1. agents update perceived climate from prior exposures;
2. agents decide whether to speak;
3. speakers generate content, possibly with preference falsification;
4. eligible items are assembled from network neighbors plus an explicit exploration pool;
5. ranking condition orders candidate items;
6. agents receive feeds;
7. agents engage or ignore;
8. social proof is updated;
9. perceived climate, hostility perception, fatigue and harassment exposure are updated;
10. civic-responsibility willingness is updated;
11. metrics are recorded.

Private opinion `p_i` does not change in the core experiment.

## 13. Perception model

Agents infer the social world from exposure rather than observing the population directly.

Perceived opinion mean:

```math
M_i(t) = Σ_j w_ij · x_j / Σ_j w_ij
```

Perceived hostility:

```math
H_i(t) = Σ_j w_ij · out_j / Σ_j w_ij
```

Optional perceptual amplification, motivated by overperception-of-outrage findings, is represented by:

```math
Hhat_i(t) = clip(H_i(t) + omega_i · Ambiguity_i(t), 0, 1)
```

`omega_i` requires empirical calibration and must be zero in a control sensitivity run.

## 14. Civic-responsibility model

This module tests the user's core extension beyond standard polarization models.

```math
civic_i(t+1) = clip[
  civic_i(t)
  + m1 · Meaning_i(t)
  + m2 · Efficacy_i(t)
  - m3 · fat_i(t)
  - m4 · harr_i(t)
  - m5 · PublicExposureCost_i(t),
  0, 1]
```

An agent is considered willing to enter or remain in a responsibility-bearing role when:

```math
civic_i(t) >= theta_civic,i
```

The candidate/office-bearing pool is therefore endogenous to experienced discourse costs.

Crucially, v0.1 must track whether attrition is selective by traits such as `conf_i`, `iso_i`, `norm_i` and initial `civic_i`.

## 15. Core outcome metrics

### 15.1 Private polarization

Computed only from `p_i`; must remain constant in the frozen-opinion experiment.

Use at least:

- variance;
- mean pairwise ideological distance;
- optional bimodality coefficient.

### 15.2 Expressed polarization

Same statistics computed over public `x_i` among speakers.

### 15.3 Visibility distortion

Distance between population-private and feed-visible opinion distributions.

Primary:

```math
VD(t) = Wasserstein(D_private, D_visible)
```

Also report binned Jensen-Shannon divergence as robustness check.

### 15.4 Perceived polarization

Average agent-level estimate of ideological spread from observed feeds minus true private spread.

### 15.5 Hostility perception bias

```math
HPB(t) = mean_i(Hhat_i(t)) - TruePopulationHostility(t)
```

### 15.6 Silence gap

Difference in speaking probability across latent opinion groups, especially between numerically moderate/private-majority agents and highly activated minorities.

### 15.7 Preference falsification

```math
PF(t) = mean_speakers(|x_i(t) - p_i|)
```

and proportion crossing a predeclared substantive threshold.

### 15.8 Civic retention

Proportion above the civic-role threshold over time.

### 15.9 Candidate selection bias

Difference between the trait distribution of the civic candidate pool and the total population, especially conflict tolerance:

```math
CSB_conf(t) = mean(conf_i | civic_i >= theta_civic,i) - mean(conf_i)
```

### 15.10 Pluralism / representational fidelity

A high-quality public sphere should be both diverse and representative. Report:

- entropy of visible viewpoints;
- visibility distortion;
- minority visibility floor;
- hostility burden;
- civic retention.

Do not reduce pluralism to entropy alone: a perfectly balanced 50/50 visible feed can be badly unrepresentative of a 90/10 population.

## 16. Preregistered hypotheses H1–H10

### H1 — Engagement visibility distortion

Relative to chronological ranking, engagement ranking increases `VD` when engagement propensity is correlated with negativity, out-group hostility or ideological extremity.

**Falsification:** no material increase across plausible calibrated parameter ranges.

### H2 — Perceived polarization without private polarization

Under fixed `p_i`, engagement ranking can increase perceived and expressed polarization while private polarization remains unchanged.

**Falsification:** perceived/expressed polarization cannot diverge from the fixed private baseline except trivially/noisily.

### H3 — Algorithmic spiral of silence

Visibility distortion reduces expression among agents whose private position is underrepresented in their perceived feed, amplifying the initial distortion.

**Falsification:** expression probability is not systematically related to feed-relative perceived support after calibration to empirical spiral-of-silence evidence.

### H4 — Preference-falsification amplification

Engagement ranking increases average `PF` relative to chronological ranking when perceived social pressure is nonzero.

**Falsification:** no robust condition-level increase in falsification across plausible `kappa` and isolation-cost ranges.

### H5 — Threshold nonlinearity

Heterogeneous expression thresholds generate nonlinear transitions: small ranking-weight changes can produce disproportionately large changes in visible opinion climate.

**Falsification:** outcome response remains approximately linear and free of tipping regions over the calibrated parameter space.

### H6 — Identity/conflict interaction

Out-group-sensitive engagement and salient group identity magnify visibility distortion more than affinity-only engagement.

**Falsification:** adding identity/out-group terms does not systematically increase distortion or hostility exposure.

### H7 — Selective public overrepresentation

Engagement ranking increases the public-share representation of high-conflict-tolerance/high-activation agents relative to their population share.

**Falsification:** speaker trait distributions remain representative after controlling for initial activity.

### H8 — Civic selection effect

Repeated high-conflict exposure reduces civic-role willingness disproportionately among low-conflict-tolerance / high-isolation-cost agents, shifting the candidate pool toward more conflict-tolerant agents.

**Falsification:** civic attrition is absent, random with respect to traits, or equal across ranking conditions.

### H9 — Pluralistic-objective mitigation

Condition C reduces visibility distortion, hostility perception bias, silence and civic selection bias relative to Condition B without collapsing total user utility/engagement below a predeclared acceptable floor.

**Falsification:** mitigation is absent or requires such a large utility loss that the trade-off fails the predefined criterion.

### H10 — Public/private decoupling as the core null test

A system can exhibit large changes in visible and perceived polarization with exactly zero change in private opinion.

**Falsification:** once private opinion is frozen and implementation artifacts are excluded, the model cannot generate a stable public/private divergence.

H10 is the central diagnostic hypothesis of v0.1.

## 17. Experimental matrix

Minimum factorial dimensions:

```text
ranking:              chronological | engagement | pluralistic
homophily:            low | medium | high
negativity response:  zero | calibrated-low | calibrated-high
outgroup response:    zero | calibrated-low | calibrated-high
spiral sensitivity:   zero | calibrated-low | calibrated-high
preference falsify:   off | on
civic cost:           off | calibrated-low | exploratory-high
```

Do not run the entire Cartesian product blindly. Use staged experiments:

1. mechanism-isolation tests;
2. calibrated baseline;
3. interaction tests;
4. global sensitivity analysis;
5. intervention comparison.

## 18. Baseline run profile

Initial engineering baseline, not a scientific final:

```text
N = 10,000
T = 250 time steps
network = stochastic block model
private opinion updating = OFF
network rewiring = OFF
bots = OFF
external manipulators = OFF
misinformation quality effect = OFF
ranking conditions = A/B/C
random seeds per cell = >= 250, increased until Monte Carlo intervals stabilize
```

Every comparative run must use paired seeds where possible.

## 19. Calibration discipline

Parameters are classified as:

- `empirical-direct`: estimable from directly relevant empirical work;
- `empirical-directional`: evidence supports direction but not transportable magnitude;
- `theoretical`: construct justified, magnitude not empirically established;
- `exploratory`: deliberately stress-tested assumption.

Rules:

1. no parameter is justified solely by Le Bon, Freud, Canetti, Bernays, Arendt, Tarde, Kuran or Noelle-Neumann;
2. classic theories may justify a construct, not a numeric coefficient;
3. modern empirical estimates must not be copied across measurement scales without a calibration model;
4. uncertain coefficients receive distributions/ranges, not false point precision;
5. sensitivity analysis must show whether headline conclusions depend on narrow parameter choices.

## 20. Sensitivity and robustness

Required:

- one-at-a-time mechanism ablation;
- Latin-hypercube or equivalent broad parameter sampling;
- variance-based global sensitivity analysis where computationally feasible;
- alternate initial opinion distributions;
- alternate network community structures;
- alternate ranking weight sets;
- zero-overperception control (`omega = 0`);
- zero-preference-falsification control (`kappa = 0`);
- zero-spiral control (`norm = 0` / isolation term disabled);
- no-negativity-bias control;
- alternative feed exploration rates.

A result is **structurally robust** only if its sign and qualitative interpretation survive broad plausible parameter ranges and multiple network seeds.

## 21. Verification gates

Before interpreting any social result:

1. chronological ranking must not accidentally use engagement state;
2. private opinions must remain bitwise/numerically unchanged in frozen-opinion runs;
3. paired runs must start from identical agents and graph;
4. feed distributions must reconstruct from logged ranking scores;
5. expression decisions must reconstruct from logged utilities/probabilities;
6. silence and preference falsification must be distinguishable;
7. civic attrition must not mechanically depend on ideology unless explicitly modeled;
8. metric implementations must be tested on synthetic toy populations with known expected values;
9. Monte Carlo uncertainty must be reported;
10. failed hypotheses remain failed; no post-hoc coefficient tuning may be described as confirmation.

## 22. Interpretation rules

The simulator can establish **model possibility and conditional mechanism behavior**, not real-world causal prevalence by itself.

Allowed interpretation:

> Under empirically plausible assumptions A–D, engagement ranking is sufficient in the model to generate X without changing private opinions.

Not allowed:

> Social-media algorithms cause X in the real world because the simulation produced X.

Real-world causal claims require empirical validation against platform, survey, field-experiment or natural-experiment data.

## 23. v0.1 non-goals

- reproducing a proprietary platform ranking stack;
- estimating the real-world population effect size of social media;
- predicting elections;
- labeling specific political groups as populist, competent or incompetent;
- modeling truth/misinformation as the core mechanism;
- endogenous private-opinion persuasion;
- endogenous network rewiring;
- bots or coordinated manipulation;
- global cultural generalization without country-level calibration;
- asserting that classic mass psychology is empirically valid as originally written.

## 24. v0.2 extension candidates

Only after v0.1 verification:

1. private-opinion updating / persuasion;
2. follow/unfollow and network rewiring;
3. endogenous identity salience;
4. influencer/prestige accumulation;
5. coordinated actors and bots;
6. misinformation/epistemic quality;
7. cross-platform diffusion;
8. office-holder decision dilemmas and constituency allocation;
9. explicit volunteer/municipal-office lifecycle;
10. country/culture-specific calibration.

## 25. Implementation recommendation

Use a transparent Python reference implementation before optimizing performance.

Preferred architecture:

```text
model/
  agents.py
  network.py
  content.py
  expression.py
  engagement.py
  ranking.py
  perception.py
  civic.py
  metrics.py
  simulation.py
experiments/
  mechanism_isolation.py
  baseline.py
  sensitivity.py
  interventions.py
tests/
  test_frozen_private_opinion.py
  test_ranking_controls.py
  test_expression_reconstruction.py
  test_metrics_known_populations.py
  test_paired_seed_equivalence.py
```

Avoid an opaque end-to-end ML recommender in v0.1. The purpose is causal interpretability of model mechanics.

## 26. Completion criteria for v0.1

The specification is ready for implementation when:

- every state variable has a declared domain;
- all update rules are explicit;
- ranking A/B/C are separable and testable;
- H1–H10 include falsification criteria;
- private-opinion freeze is enforceable;
- primary metrics are operationalized;
- calibration evidence is traceable;
- uncertain parameters are labeled;
- sensitivity plan is defined;
- interpretation boundaries prevent simulation-to-reality overclaiming.

The implementation is ready for scientific exploration only after the verification gates pass.