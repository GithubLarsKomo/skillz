# Algorithmic Mass–Public Model — Evidence Baseline

Status: candidate  
Version: 0.1  
As of: 2026-09-12

## Research question

Can engagement-optimized social-media ranking, combined with empirically supported mechanisms of selective expression and social perception, produce a persistent divergence between private opinion, public expression, visible opinion climate and willingness to assume civic responsibility, even if private opinions themselves remain unchanged?

## Decision context

This evidence note supports parameterization and falsification of `SPEC.md`. It does not establish real-world causal prevalence. It separates:

- direct empirical evidence;
- theoretical/model evidence;
- directional evidence that cannot be copied as a numeric parameter;
- open hypotheses requiring new evidence.

## Short answer

The evidence is sufficient to justify a model of **engagement amplification + distorted social perception + selective expression**. There is direct evidence that engagement-based ranking can amplify emotionally charged/out-group-hostile political content relative to chronological ranking, evidence that users can overperceive online moral outrage and infer excessive intergroup hostility, and meta-analytic evidence that perceived opinion support is associated with willingness to express political opinions online and offline.

Agent-based and analytical models show that spiral-of-silence dynamics, network structure and engagement ranking can generate nonlinear collective outcomes under explicit assumptions. These models establish plausibility, not real-world effect size.

The proposed **civic-selection effect** — selective withdrawal of lower-conflict-tolerance or higher-isolation-cost individuals from responsibility-bearing civic roles — remains an evidence gap. It is therefore an exploratory hypothesis (H8), not a calibrated empirical mechanism.

## Claims

### C1 — Engagement ranking can amplify divisive political content

**Claim:** Engagement-based ranking can increase exposure to emotionally charged and out-group-hostile political content relative to a reverse-chronological baseline.

- **Basis:** direct
- **Confidence:** high for direction; medium for transport to other platforms/populations
- **Support:** Milli et al. (2025), *PNAS Nexus*, DOI `10.1093/pnasnexus/pgaf062`.
- **Notes:** The audit concerns a specific platform/context. It supports inclusion of negativity/out-group terms and a chronological comparator, not universal effect sizes.

### C2 — Engagement-weighted ranking can create a behavioral feedback loop

**Claim:** A model in which social interactions increase ranking visibility can produce feedback between user behavior and content distribution; greater weight on likes/shares can increase polarization under the model's assumptions.

- **Basis:** direct for the published model; derived for real-world generalization
- **Confidence:** high that the theoretical mechanism exists; medium/low for external effect size
- **Support:** Germano, Gómez & Sobbrio (2026), *Journal of Public Economics*, DOI `10.1016/j.jpubeco.2026.105589`.
- **Notes:** This is a theoretical/economic model with empirical consistency checks, not a direct estimate of all social-media algorithms.

### C3 — Online outrage can be systematically overperceived

**Claim:** Observers can infer more moral outrage from political social-media messages than authors report feeling, and this can inflate perceived hostile norms, affective polarization and ideological extremity.

- **Basis:** direct
- **Confidence:** high for the studied settings
- **Support:** Brady et al. (2023), *Nature Human Behaviour*, DOI `10.1038/s41562-023-01582-0`.
- **Notes:** This justifies a separate perception layer. It does not justify a universal fixed `omega` parameter.

### C4 — Perceived opinion support is associated with opinion expression

**Claim:** Perceived support for one's opinion is positively associated with willingness to express political opinions; the relationship is small overall but robust and not weaker online than offline in the meta-analysis.

- **Basis:** direct
- **Confidence:** high for direction; medium for causal magnitude
- **Support:** Matthes, Knoll & von Sikorski (2018), *Communication Research*, DOI `10.1177/0093650217745429`.
- **Relevant estimate:** 66 studies, >27,000 participants; overall association approximately `r = .10`.
- **Notes:** The meta-analytic correlation is a calibration target, not a logistic-regression coefficient.

### C5 — Network structure can condition spiral-of-silence dynamics

**Claim:** Agent-based models of opinion expression show that community structure, connectivity and media/network conditions can change whether local silencing remains local or develops into a broader apparent consensus.

- **Basis:** direct for models
- **Confidence:** high for model behavior; medium for empirical transport
- **Support:**
  - Sohn (2022; online 2019), *Communication Research*, DOI `10.1177/0093650219856510`.
  - Cabrera et al. (2021), *Journal of Business Economics*, DOI `10.1007/s11573-021-01064-7`.
  - Ross/Stieglitz line, including DOI `10.1080/0960085X.2018.1560920`.
  - *Modelling Public Opinion Dynamics: The Spiral of silence in clustered homophilic networks* (2026), DOI `10.1016/j.chaos.2025.117660`.
- **Notes:** Because network topology itself has strong effects, v0.1 freezes the graph when comparing ranking conditions.

### C6 — Threshold heterogeneity can produce nonlinear collective outcomes

**Claim:** Populations with similar average dispositions can produce very different aggregate behavior when individual action thresholds differ; small contextual changes can cross cascades/tipping regions.

- **Basis:** direct theoretical model
- **Confidence:** high as a formal result; requires empirical calibration for this application
- **Support:** Granovetter (1978), *American Journal of Sociology*, DOI `10.1086/226707`.
- **Notes:** Supports heterogeneous expression thresholds and explicit tests for nonlinearity; it does not prove social-media tipping behavior by itself.

### C7 — Public expression need not reveal private preference

**Claim:** Social pressure can create divergence between private preference and public expression, with collective consequences.

- **Basis:** theoretical
- **Confidence:** high as a coherent theoretical construct; numeric calibration unresolved here
- **Support:** Timur Kuran (1995), *Private Truths, Public Lies*.
- **Notes:** v0.1 treats preference falsification separately from silence. Parameter magnitude is not derived from the book.

### C8 — Classic deindividuation should not be modeled as generic irrationality

**Claim:** Modern social-identity/SIDE accounts reject the simple idea that anonymity or crowd immersion inherently destroys self-control; computer-mediated settings can instead increase salience of group identity and conformity to group norms.

- **Basis:** strong-secondary / theoretical + empirical program
- **Confidence:** medium-high
- **Support:** Reicher, Spears & Postmes; Postmes, Spears & Lea; later SIDE reviews.
- **Notes:** This is why Le Bon/Freud are not used as direct behavioral equations. Identity effects are routed through modern social-identity constructs.

### C9 — Digital media effects on democracy are mixed, not uniformly negative

**Claim:** The literature does not support a one-directional claim that digital media simply reduce democratic participation; observed associations include both increased participation and adverse outcomes such as polarization/trust effects depending on context.

- **Basis:** strong-secondary
- **Confidence:** high
- **Support:** Lorenz-Spreen et al. (2023), *Nature Human Behaviour*, DOI `10.1038/s41562-022-01460-1`.
- **Notes:** The simulator must therefore include possible mobilization/meaning/efficacy benefits in the civic module rather than modeling only costs.

### C10 — Civic selection out of responsibility-bearing roles is not yet established

**Claim:** Repeated exposure to conflict/harassment may selectively reduce willingness of some personality/behavioral types to assume or retain public responsibility, thereby changing the composition of the candidate pool.

- **Basis:** unknown / derived hypothesis
- **Confidence:** low
- **Support:** no sufficiently direct source in the current evidence set.
- **Contradictions / caution:** digital media can also mobilize participation; observational evidence on abuse of politicians does not establish a general population-level selection effect.
- **Notes:** This is H8 and must remain exploratory until directly calibrated or empirically tested.

## Conflicts and tensions

### F1 — Algorithmic amplification versus attitude change

Evidence that ranking changes what people see does not imply that it rapidly changes private political attitudes. The model must therefore keep visibility/expression effects distinct from persuasion. This is the main reason private opinions are frozen in v0.1.

### F2 — Participation versus withdrawal

Digital media can lower coordination costs and increase participation while simultaneously increasing perceived conflict or expression costs. The civic module must allow both positive (`Meaning`, `Efficacy`) and negative (`Fatigue`, `Harassment`, `PublicExposureCost`) terms.

### F3 — Local versus global spiral of silence

Simulation work does not imply that minority silence inevitably becomes global. Some models find local silencing without global convergence except under specific connectivity/media conditions. Global-silence outcomes must therefore be treated as conditional, not expected by default.

### F4 — Classic theory versus modern mechanism

Le Bon, Freud, Tarde, Canetti, Bernays, Noelle-Neumann, Kuran and Arendt differ greatly in epistemic status. Their concepts may motivate constructs but must not be treated as equivalent empirical evidence.

## Parameter evidence classes

| Parameter family | Initial class | Reason |
|---|---|---|
| engagement amplification by divisive/out-group-hostile content | empirical-directional | direct audit supports direction, not universal coefficient |
| outrage overperception | empirical-directional | direct experiments support mechanism; transport uncertain |
| opinion-climate effect on expression | empirical-directional | meta-analysis supports association; causal/scale conversion unresolved |
| activation thresholds | theoretical + empirical-calibration-needed | Granovetter formalism, application-specific distribution unknown |
| preference falsification susceptibility | theoretical | construct supported; numeric range unresolved |
| homophily/community structure | empirical-direct for networks, context-specific magnitude | measurable from real networks but not yet selected for target platform |
| civic fatigue/harassment cost | exploratory | direct calibration not yet assembled |
| civic candidate-selection effect | exploratory | central evidence gap |
| pluralistic ranking weights | normative/exploratory | intervention design, not empirical fact |

## Open questions that could change model conclusions

1. What empirical distributions best represent `iso_i`, `conf_i`, `theta_i` and `kappa_i` in a general adult population versus politically active users?
2. How strongly do likes, comments, shares and dwell time differ in their response to agreement, negativity and out-group hostility across platforms?
3. How should stated user preference be measured independently of revealed engagement for Condition C?
4. What is the best empirical measure of conflict exposure that predicts withdrawal from responsibility-bearing civic roles?
5. Does online hostility selectively deter compromise-oriented or conflict-averse people from local office/volunteer leadership, or does it also mobilize them?
6. Which country/culture variables materially moderate isolation fear, expression cost and civic-role persistence?
7. How much apparent polarization can be reproduced using selection/expression alone before any private-opinion updating is needed?
8. Under which network structures does engagement ranking produce local distortion only versus system-wide norm distortion?

## Calibration rule

No parameter moves from `theoretical` or `exploratory` to `empirical-direct` without a source that measures a sufficiently close construct in a sufficiently close setting. Directional evidence may constrain sign and plausible range but may not be presented as a measured platform coefficient.

## Evidence baseline conclusion

There is enough evidence to implement the v0.1 ABM as a **mechanism test**. The strongest supported chain is:

```text
engagement-sensitive visibility
  -> disproportionate exposure to divisive/hostile content under some conditions
  -> distorted perception of opinion climate / hostility
  -> selective willingness to express
  -> further distortion of the visible public sphere
```

The extension from distorted discourse to **selective civic withdrawal and candidate-pool composition** is scientifically interesting precisely because it remains unresolved. The simulation should therefore be used to identify conditions and empirical predictions for that mechanism, not to assert that the mechanism already occurs at a known real-world magnitude.