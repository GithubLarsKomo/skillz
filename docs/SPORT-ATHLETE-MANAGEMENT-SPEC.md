# Sport Athlete Management – System Specification

Status: Draft for implementation

## 1. Purpose

Extend `skillz` from a set of useful sport diagnostics, training-programming and report-generation skills into a coherent athlete-management system that supports longitudinal, evidence-based training control.

The target system shall close the loop between goals, planning, execution, monitoring, recovery, health, testing, adaptation and reporting:

`Athlete profile -> goals -> season plan -> macro/meso/micro plan -> prescribed session -> completed session -> subjective/objective response -> adaptation decision -> revised plan -> retest`

The architecture must remain composable. Specialized skills own their domain logic; an orchestrator coordinates them without duplicating specialist reasoning.

## 2. Existing baseline in skillz

The current sport stack already provides a strong foundation:

- `sport-performance-diagnostics`: evaluates lactate, heart-rate, RPE and ergometer-style performance data and derives working thresholds/zones with uncertainty.
- `sport-training-programming`: creates periodized executable plans with strength, power, endurance, RIR/RPE, progression, taper and safety rules.
- `sport-diagnostics-training-report-workflow`: orchestrates diagnostics -> plan -> DOCX/PDF report generation.
- Dr.-Komorowski sport report renderers: presentation layer only.

Current gap: there is no persistent athlete state, no longitudinal daily monitoring, no dedicated season/meso/micro hierarchy, no explicit adaptive control engine, and no specialist skills for recovery/sleep, nutrition/energy availability, rehabilitation/return-to-sport, illness return, performance psychology or sex/age modifiers.

## 3. Design principles

### 3.1 Closed-loop control, not static planning

Training control must compare:

- prescribed load,
- completed load,
- internal response,
- recovery response,
- objective performance response,
- health constraints,
- trend over time.

A plan is provisional. The system must support acute, tactical and strategic adaptation.

### 3.2 Explainable decisions

The system may produce traffic-light states such as green/yellow/orange/red, but must not present opaque pseudo-precision such as a single unexplained readiness score.

Every adaptation decision must preserve:

- trigger,
- input snapshot,
- decision,
- previous prescription,
- revised prescription,
- rationale,
- confidence,
- safety flags,
- whether a human override occurred.

### 3.3 Multi-dimensional monitoring

No single metric is sufficient. Monitoring should combine, where available:

- session RPE / internal load,
- sleep duration and quality,
- general fatigue,
- soreness,
- stress,
- motivation/readiness,
- pain and symptom location,
- illness symptoms,
- resting HR / HRV as optional context,
- objective external load/performance,
- sport-specific markers.

### 3.4 Individual baselines over population cut-offs

Where safe and meaningful, athlete-specific baselines and rolling trends are preferred over universal thresholds. Population norms remain context, not the sole decision rule.

### 3.5 Age and sex as modifiers, not separate universes

The system must support differentiated logic for:

- age 20–30,
- age 50+,
- male athletes,
- female athletes,
- menstrual-cycle status where relevant and voluntarily supplied,
- peri-/post-menopause where relevant and voluntarily supplied.

These modify risk, recovery assumptions, interpretation and emphasis; they must not produce simplistic hard-coded stereotypes.

### 3.6 Medical boundary

The system is a training-support system, not a replacement for medical diagnosis, treatment or return-to-sport clearance.

Red flags must route to medical evaluation. Rehabilitation skills may operationalize documented medical/physiotherapy restrictions but must not invent diagnoses or clearance.

## 4. Target skill architecture

### 4.1 Orchestrator

#### `sport-athlete-management`

Purpose: coordinate persistent athlete state, planning, monitoring, testing and adaptation across all specialist sport skills.

Primary inputs:

- athlete profile,
- goals and competition calendar,
- current season structure,
- recent training history,
- diagnostics,
- daily monitoring,
- completed-session data,
- recovery/health state,
- active injuries/illness constraints.

Primary outputs:

- `athlete-management-state.json`
- `next-training-decision.json`
- `plan-revision.json` when required

The orchestrator must not duplicate domain-specific logic for strength, endurance, rehabilitation, nutrition or psychology.

## 5. Specialist skills

### P0 – required for a functioning control loop

#### 5.1 `sport-athlete-profile`

Owns durable athlete context:

- biological sex where relevant to training decisions,
- date of birth / age band,
- sport and discipline,
- training age,
- performance history,
- PBs and benchmark results,
- injury and illness history,
- current restrictions,
- available training time,
- equipment,
- environmental context,
- preferences,
- optional menstrual/menopause context,
- explicit consented health-context fields.

Output: `athlete-profile.json`

#### 5.2 `sport-goal-performance-model`

Transforms a broad goal into a hierarchy:

- outcome goals,
- performance goals,
- process goals,
- limiting factors,
- sport-specific KPI tree,
- target dates,
- priority competitions,
- acceptable trade-offs.

Output: `sport-performance-model.json`

#### 5.3 `sport-season-periodization`

Owns annual/season structure:

- A/B/C competitions,
- target peaks,
- macrocycles,
- general preparation,
- specific preparation,
- competition phase,
- taper windows,
- transition/off-season,
- retest points.

Output: `sport-season-plan.json`

#### 5.4 `sport-mesocycle-planning`

Owns approximately 3–8 week blocks:

- primary adaptation target,
- secondary maintenance qualities,
- intended load progression,
- overload/recovery logic,
- planned diagnostics,
- entry and exit criteria.

Output: `sport-mesocycle.json`

#### 5.5 `sport-microcycle-planning`

Owns the concrete weekly / short-cycle distribution of training stress:

- high/low organization,
- sequencing of key sport sessions,
- strength/endurance interference management,
- recovery spacing,
- session placement,
- deload decisions.

Output: `sport-microcycle.json`

#### 5.6 `sport-daily-athlete-monitoring`

Owns morning and post-session athlete input.

Morning check-in core fields:

- sleep duration,
- sleep quality,
- fatigue,
- soreness,
- stress,
- motivation/readiness,
- pain score and location,
- illness symptoms,
- optional resting HR,
- optional HRV,
- optional cycle/menopause symptoms.

Post-session core fields:

- completed duration,
- session RPE,
- external load/performance,
- strength sets/reps/load/RIR where applicable,
- pain during/after training,
- technique/quality notes,
- local fatigue,
- deviations from plan.

Outputs:

- `daily-checkin.json`
- `completed-session.json`

#### 5.7 `sport-training-adaptation-engine`

This is the central decision skill.

It compares planned versus actual load and the athlete response and decides whether to:

- execute as planned,
- reduce volume,
- reduce intensity,
- substitute a session,
- move a key session,
- insert recovery,
- progress earlier,
- delay progression,
- trigger retesting,
- trigger rehabilitation/illness routing,
- trigger medical review.

It must operate on three levels:

1. Acute: today's training decision.
2. Tactical: micro-/mesocycle modification.
3. Strategic: season-plan revision.

Output: `training-adaptation-decision.json`

### P1 – required for comprehensive athlete management

#### 5.8 `sport-strength-power-programming`

Specializes current generic training logic for:

- hypertrophy,
- maximal strength,
- strength endurance,
- rate of force development,
- ballistic/power work,
- Olympic-lift derivatives,
- plyometrics,
- isometrics,
- eccentric loading,
- maintenance.

Supports RIR/RPE, percentage-based loading, e1RM, APRE-style logic and velocity where available.

Output: `strength-power-plan.json`

#### 5.9 `sport-endurance-programming`

Owns endurance-specific prescription:

- low intensity / Zone 1–2,
- threshold work,
- VO2-oriented intervals,
- sprint/anaerobic work,
- polarized/pyramidal/other justified intensity distributions,
- volume progression,
- sport-specific pace/power/HR prescriptions.

Output: `endurance-plan.json`

#### 5.10 `sport-recovery-sleep`

Owns recovery interpretation and intervention options:

- athlete-specific sleep baseline,
- sleep opportunity,
- sleep quality trend,
- travel/competition disruption,
- accumulated fatigue,
- recovery-day design,
- optional HRV/resting-HR contextual interpretation.

Output: `recovery-state.json`

#### 5.11 `sport-nutrition-fueling`

Owns performance-oriented nutrition support without replacing clinical dietetics:

- energy availability risk awareness,
- carbohydrate periodization,
- protein intake distribution,
- hydration/electrolytes,
- pre/during/post training fueling,
- race fueling,
- weight-management safety,
- RED-S risk routing for all sexes.

Outputs:

- `sport-fueling-plan.json`
- `energy-availability-risk.json` when relevant

#### 5.12 `sport-injury-rehabilitation`

Supports criterion-based rehabilitation from documented medical/physiotherapy constraints.

Model phases:

- protection / symptom control,
- restore tolerated ROM/load,
- rebuild force capacity,
- rebuild power/elastic capacity,
- sport-specific loading,
- return to participation,
- return to sport,
- return to performance.

Output: `rehab-progression.json`

#### 5.13 `sport-return-after-illness`

Owns graded return following acute illness or interruption.

Must evaluate:

- current symptoms,
- symptom-free interval where relevant,
- duration of interruption,
- previous training load,
- first-session response,
- stepwise volume/intensity restoration,
- cardiopulmonary and systemic red flags.

Output: `return-after-illness-plan.json`

#### 5.14 `sport-testing-battery`

Selects test batteries based on sport, goal, age, sex and current phase.

Potential domains:

- aerobic threshold,
- anaerobic threshold,
- VO2-related field/ergometer tests,
- sprint power,
- maximal strength/e1RM,
- isometric force,
- jump/power metrics,
- sport-specific performance tests,
- functional reserve for masters athletes.

Output: `sport-testing-plan.json`

#### 5.15 `sport-adaptation-analysis`

Performs longitudinal analysis:

- training load trend,
- performance trend,
- response at standard workloads,
- RPE drift,
- HR/power/pace drift,
- recovery trend,
- test-to-test delta,
- plateau detection,
- probable non-response / excessive fatigue signals,
- uncertainty and missing-data effects.

Output: `sport-adaptation-analysis.json`

### P2 – extension modules

#### 5.16 `sport-performance-psychology`

Supports performance psychology only:

- goal setting,
- motivation,
- self-efficacy,
- imagery,
- self-talk,
- pre-performance routines,
- attentional control,
- arousal regulation,
- competition routines.

Output: `performance-psychology-plan.json`

#### 5.17 `sport-mental-health-routing`

Provides screening/routing boundaries only. It does not diagnose or provide psychotherapy.

Output: `mental-health-routing.json`

#### 5.18 `sport-training-music`

Builds music recommendations from:

- user preferences,
- session type,
- desired activation level,
- tempo preference,
- familiar/favorite tracks,
- explicit exclusions.

Output: `training-music-profile.json`

#### 5.19 `sport-environment-travel`

Supports:

- heat,
- cold,
- altitude,
- travel,
- jet lag,
- competition scheduling disruption.

Output: `environment-adjustment.json`

## 6. Age modifier requirements

### 6.1 Age 20–30

Default emphasis may include:

- maximal performance development,
- high trainability and exposure when history supports it,
- aggressive but evidence-constrained progression,
- sport-specific peak performance.

The system must still respect individual recovery, injury history and life stress.

### 6.2 Age 50+

The system must not automatically prescribe low-intensity or low-power training solely because of age.

It should more explicitly account for:

- slower or more variable recovery when observed,
- maintenance/development of maximal strength,
- preservation of power/RFD,
- tendon/joint history,
- bone-health context,
- cardiometabolic/cardiovascular risk context,
- higher value of functional reserve,
- longer consequences of poorly tolerated overload,
- larger role for adaptive deloading and trend-based progression.

Age is a modifier. Observed athlete response remains primary.

## 7. Sex-specific modifier requirements

### 7.1 Female athletes

Optional, consented fields may include:

- menstrual cycle status,
- cycle regularity,
- hormonal contraception,
- menstrual symptoms,
- peri-/post-menopause status,
- menopause symptoms.

The system must not use rigid phase-based training rules without athlete-specific evidence.

It should support symptom-informed adjustment and identify contexts where medical or nutrition review may be appropriate, particularly where energy availability, menstrual disturbance, bone health or persistent symptoms raise concern.

### 7.2 Male athletes

The system must apply the same vigilance for:

- low energy availability / RED-S,
- overtraining/excessive fatigue,
- sleep disruption,
- psychological distress,
- injury and illness.

Male sex must not be treated as the unmodified default athlete model.

## 8. Web application architecture

Recommended deployment target: Hetzner-hosted web application with authenticated athlete access and an API-backed relational database.

### 8.1 Components

- Responsive athlete web app / PWA.
- Authenticated API service.
- Relational DB as source of truth.
- Optional scheduled jobs for trend aggregation.
- Skillz/LLM integration as reasoning layer.
- Deterministic calculation utilities for load, trends and derived metrics.
- Export/report layer for DOCX/PDF.

### 8.2 Principle

LLM-generated documents are not the source of truth. Structured DB records are authoritative; reports are derived views.

## 9. Core database schema

### 9.1 Athlete identity and context

`athletes`

- id
- display_name
- timezone
- active
- created_at
- updated_at

`athlete_profiles`

- athlete_id
- date_of_birth
- sex_at_birth optional where relevant
- gender optional if user wishes to store it
- sport
- discipline
- training_age_years
- height_cm optional
- body_mass_kg optional
- profile_version
- valid_from

`athlete_preferences`

- athlete_id
- preferred_training_days
- equipment_json
- music_preferences_json
- communication_preferences_json

### 9.2 Goals and competition structure

`goals`

- id
- athlete_id
- goal_type: outcome|performance|process
- description
- target_value optional
- target_unit optional
- target_date
- priority
- status

`competitions`

- id
- athlete_id
- name
- competition_date
- priority: A|B|C
- discipline
- notes

### 9.3 Planning hierarchy

`seasons`

- id
- athlete_id
- name
- start_date
- end_date
- primary_goal_id
- status

`macrocycles`

- id
- season_id
- start_date
- end_date
- objective
- phase

`mesocycles`

- id
- macrocycle_id
- start_date
- end_date
- primary_adaptation
- secondary_adaptations_json
- entry_criteria_json
- exit_criteria_json
- planned_load_strategy_json

`microcycles`

- id
- mesocycle_id
- start_date
- end_date
- focus
- load_target_json

### 9.4 Session prescription and completion

`planned_sessions`

- id
- athlete_id
- microcycle_id
- planned_start
- session_type
- objective
- planned_duration_min
- planned_rpe
- status
- prescription_json
- version

`planned_session_items`

- id
- session_id
- sequence_no
- item_type
- exercise_or_interval
- prescription_json

`completed_sessions`

- id
- planned_session_id optional
- athlete_id
- started_at
- completed_at
- duration_min
- session_rpe
- completion_status
- external_load_json
- notes

`completed_session_items`

- id
- completed_session_id
- planned_item_id optional
- actual_json
- pain_during optional
- technical_quality optional

### 9.5 Daily monitoring

`daily_checkins`

- id
- athlete_id
- local_date
- sleep_duration_min
- sleep_quality_1_5
- fatigue_1_5
- soreness_1_5
- stress_1_5
- motivation_1_5
- pain_0_10
- pain_location_json
- illness_symptoms_json
- free_text optional
- created_at

`objective_metrics`

- id
- athlete_id
- measured_at
- metric_type
- value
- unit
- source
- quality_flag

Examples: resting HR, HRV, body mass, temperature, power, pace, jump metric.

### 9.6 Health and rehabilitation

`injury_events`

- id
- athlete_id
- onset_date
- body_region
- source_diagnosis_text optional
- source_reference optional
- active_restrictions_json
- status

`illness_events`

- id
- athlete_id
- onset_date
- symptom_json
- medical_restrictions_json optional
- status

`rehab_states`

- id
- athlete_id
- injury_event_id
- phase
- criteria_met_json
- current_load_limits_json
- next_criteria_json
- assessed_at

### 9.7 Nutrition and sex-specific optional monitoring

`nutrition_checkins`

- id
- athlete_id
- local_date
- fueling_adequacy optional
- hydration_adequacy optional
- body_mass_change optional
- concern_flags_json

`menstrual_health_optional`

- id
- athlete_id
- local_date
- cycle_context optional
- bleeding_status optional
- symptom_json optional
- menopause_context optional

This table is optional and should require explicit user choice/consent.

### 9.8 Diagnostics and adaptation

`performance_tests`

- id
- athlete_id
- test_date
- test_type
- protocol_json
- result_json
- source_file_reference optional

`adaptation_decisions`

- id
- athlete_id
- created_at
- decision_level: acute|tactical|strategic
- trigger
- input_snapshot_json
- previous_plan_json
- decision_json
- revised_plan_json
- rationale
- confidence
- safety_flag
- human_override
- engine_version

`training_plan_revisions`

- id
- affected_entity_type
- affected_entity_id
- prior_version
- new_version
- adaptation_decision_id
- changed_at

## 10. API contract – initial version

Suggested endpoints:

### Athlete and goals

- `GET /api/v1/athlete/profile`
- `PUT /api/v1/athlete/profile`
- `GET /api/v1/goals`
- `POST /api/v1/goals`
- `GET /api/v1/competitions`

### Daily monitoring

- `GET /api/v1/checkins/today`
- `POST /api/v1/checkins`
- `GET /api/v1/checkins/trends?days=28`

### Training

- `GET /api/v1/training/today`
- `GET /api/v1/training/week`
- `POST /api/v1/sessions/{id}/complete`
- `POST /api/v1/sessions/manual`

### Adaptation

- `POST /api/v1/adaptation/evaluate`
- `GET /api/v1/adaptation/latest`
- `GET /api/v1/adaptation/history`
- `POST /api/v1/adaptation/{id}/override`

### Diagnostics

- `POST /api/v1/tests`
- `GET /api/v1/tests`
- `GET /api/v1/tests/{id}`

### Health

- `POST /api/v1/injuries`
- `POST /api/v1/illness`
- `GET /api/v1/health/active`

## 11. Daily app UX

The athlete-facing workflow should be deliberately short.

### Morning

Target completion time: approximately 20–40 seconds.

Screen 1:

- sleep duration,
- sleep quality,
- fatigue,
- soreness,
- stress,
- motivation.

Screen 2 shown only if relevant:

- pain,
- illness symptoms,
- optional physiological metrics,
- optional cycle/menopause symptoms.

Result:

- today’s planned session,
- explainable status: proceed / caution / modify / stop-and-review,
- concise reason.

### After training

- duration,
- session RPE,
- whether completed as planned,
- pain/symptoms,
- optional detailed strength/endurance metrics,
- note.

The app should minimize mandatory manual input when metrics can be imported later from devices.

## 12. Adaptation logic

### 12.1 Acute decision examples

Possible modification triggers include combinations such as:

- unexpectedly high session RPE at standard workload,
- significant sleep disruption plus high fatigue,
- escalating pain,
- illness symptoms,
- repeated failure to complete target intensity,
- unusual deterioration in sport-specific performance.

No single wellness field should automatically determine load except clear safety/red-flag conditions.

### 12.2 Tactical adaptation

Examples:

- shift key session by 24–48 h,
- reduce accessory strength volume,
- extend recovery between high-intensity days,
- bring forward progression if repeated submaximal work becomes clearly easier,
- insert retest after unexplained plateau.

### 12.3 Strategic adaptation

Examples:

- revise mesocycle priority,
- change expected peak timing,
- reallocate strength vs endurance emphasis,
- extend rehabilitation phase,
- redefine performance targets when evidence changes.

## 13. Derived metrics

The system may calculate and display:

- session load = duration × session RPE,
- rolling weekly load,
- monotony/strain as contextual metrics if useful,
- completed/planned load ratio,
- standard-session RPE delta,
- standard-session HR/power/pace delta,
- sleep/fatigue trend,
- pain trend,
- test-to-test change,
- strength e1RM trend,
- sport-specific KPI trend.

Derived metrics must not be presented as medically validated risk scores unless appropriate evidence exists.

ACWR must not be a central automatic injury-prediction algorithm. If calculated, it is contextual only.

HRV must not independently determine training readiness. If used, it should be interpreted against individual baseline and together with other signals.

## 14. Safety state machine

Suggested states:

### GREEN

- no meaningful adverse signal,
- training can proceed as planned.

### YELLOW

- mild/moderate mismatch or recovery concern,
- preserve key objective but consider reduced volume/intensity or extra recovery.

### ORANGE

- multiple adverse signals or worsening localized symptoms,
- substantial modification, substitution or recovery day;
- targeted reassessment required.

### RED

- relevant medical red flag, severe/worsening pain, significant systemic illness signal or explicit medical restriction,
- do not use the adaptation engine to push through training;
- route to appropriate medical assessment.

The color must always be accompanied by the reason and the responsible rule/decision.

## 15. Data governance and privacy

The platform may contain health-adjacent and potentially sensitive data. Therefore:

- collect only data required for training support,
- keep optional health/sex-specific fields explicitly optional,
- separate authentication identity from health/training content where practical,
- use role-based access,
- encrypt transport and backups,
- maintain audit logs for data changes and plan overrides,
- define retention/deletion workflows,
- avoid storing unnecessary free-text clinical detail,
- preserve source references for externally supplied medical restrictions.

Before production use with third-party athletes, perform a GDPR/privacy and medical-device/software-boundary review.

## 16. Skill contracts and shared entities

All sport skills should use shared canonical identifiers and avoid copying mutable athlete state into isolated documents.

Recommended shared entities:

- `athlete_id`
- `goal_id`
- `season_id`
- `macrocycle_id`
- `mesocycle_id`
- `microcycle_id`
- `planned_session_id`
- `completed_session_id`
- `test_id`
- `injury_event_id`
- `illness_event_id`
- `adaptation_decision_id`

Each JSON output should include:

```json
{
  "schema_version": 1,
  "athlete_id": "",
  "generated_at": "",
  "source_refs": [],
  "uncertainties": [],
  "safety_flags": []
}
```

## 17. Skill DAG

```text
sport-athlete-profile
        |
        v
sport-goal-performance-model
        |
        v
sport-season-periodization
        |
        v
sport-mesocycle-planning
        |
        v
sport-microcycle-planning
        |
        +------------------------------+
        |                              |
        v                              v
sport-strength-power-programming   sport-endurance-programming
        |                              |
        +---------------+--------------+
                        v
             planned training sessions
                        |
                        v
             sport-daily-athlete-monitoring
                        |
        +---------------+------------------+
        |               |                  |
        v               v                  v
sport-recovery-sleep  health routes   completed-session data
        |               |                  |
        +-------+-------+------------------+
                v
      sport-training-adaptation-engine
                |
        +-------+---------------------+
        |                             |
        v                             v
 micro/meso/season revision      sport-testing-battery
        |                             |
        +--------------+--------------+
                       v
            sport-adaptation-analysis
                       |
                       +----> next planning cycle
```

Cross-cutting modifiers:

- `sport-athlete-profile`
- age band 20–30 / 50+
- sex-specific context
- `sport-nutrition-fueling`
- `sport-performance-psychology`
- `sport-environment-travel`
- injury/illness restrictions

## 18. Interaction with existing skills

### `sport-performance-diagnostics`

Keep as specialist diagnostic engine. Extend only where needed for common IDs/schema versioning.

### `sport-training-programming`

Refactor progressively rather than delete immediately.

Recommended future role:

- compatibility/generalist training-plan entrypoint,
- routes detailed strength/power work to `sport-strength-power-programming`,
- routes endurance work to `sport-endurance-programming`,
- consumes season/meso/micro context,
- remains capable of simple one-off plans.

### `sport-diagnostics-training-report-workflow`

Keep as report-focused orchestration. It may consume the new athlete-management outputs but should not become the operational daily control loop.

## 19. Implementation phases

### Phase P0 – closed-loop MVP

Implement first:

1. `sport-athlete-profile`
2. `sport-goal-performance-model`
3. `sport-season-periodization`
4. `sport-mesocycle-planning`
5. `sport-microcycle-planning`
6. `sport-daily-athlete-monitoring`
7. `sport-training-adaptation-engine`
8. initial relational DB schema
9. daily check-in web UI
10. planned/completed session workflow
11. decision audit trail

Exit criterion:

A single athlete can define goals and a season, receive a structured week, complete a daily morning check-in, log a session with sRPE, and receive an explainable adaptation decision that can revise the next session while preserving an audit trail.

### Phase P1 – specialist depth

Add:

- `sport-strength-power-programming`
- `sport-endurance-programming`
- `sport-recovery-sleep`
- `sport-nutrition-fueling`
- `sport-injury-rehabilitation`
- `sport-return-after-illness`
- `sport-testing-battery`
- `sport-adaptation-analysis`
- age/sex modifier rules and tests

Exit criterion:

The system supports an entire training block with performance testing, recovery/fueling context and criterion-based health constraints, and can compare measured adaptation against planned adaptation.

### Phase P2 – performance ecosystem

Add:

- `sport-performance-psychology`
- `sport-mental-health-routing`
- `sport-training-music`
- `sport-environment-travel`
- wearable/device ingestion where technically justified
- advanced dashboards

Exit criterion:

The athlete-management system supports performance, behavior and environmental context without blurring the boundary to medical diagnosis or psychotherapy.

## 20. Evaluation strategy

Every new skill should receive compatibility/evaluation cases consistent with the skillz repository conventions.

Required cross-cutting evaluation cohorts:

1. Male athlete age 20–30.
2. Female athlete age 20–30.
3. Male athlete age 50+.
4. Female athlete age 50+.
5. Healthy build phase.
6. Competition taper.
7. Acute sleep/stress disturbance.
8. Emerging localized pain.
9. Return after illness.
10. Rehabilitation with explicit medical restrictions.
11. Low-energy-availability concern.
12. Sparse/missing monitoring data.

Evaluation must specifically test that:

- the system does not lower training simply because age >50,
- female athletes are not assigned rigid menstrual-phase periodization,
- male athletes are not excluded from RED-S logic,
- HRV does not autonomously overrule all other evidence,
- an opaque readiness number is not used as the sole decision,
- red flags route out of normal progression,
- missing data increases uncertainty instead of triggering fabricated conclusions.

## 21. Initial deterministic utilities

Consider small deterministic helpers for:

- session-load calculation,
- rolling trend computation,
- e1RM estimation,
- time-in-zone aggregation,
- planned-vs-completed comparison,
- baseline deviation calculations,
- test-to-test deltas,
- schema validation.

These utilities should calculate; skills should interpret.

## 22. Proposed repository work packages

### WP-1 Domain contracts

- canonical JSON schemas,
- IDs and references,
- athlete profile contract,
- training hierarchy contract,
- adaptation decision contract.

### WP-2 Planning skills

- goals,
- season,
- mesocycle,
- microcycle.

### WP-3 Monitoring and DB

- daily check-in,
- completed session,
- session RPE,
- DB migrations,
- API endpoints.

### WP-4 Adaptation engine

- acute/tactical/strategic decision logic,
- safety state machine,
- explainability and audit trail.

### WP-5 Specialist training

- strength/power,
- endurance,
- recovery/sleep,
- fueling.

### WP-6 Health return pathways

- injury rehabilitation,
- illness return,
- medical routing.

### WP-7 Testing and longitudinal analytics

- test battery,
- adaptation analysis,
- dashboards.

### WP-8 Psychology/music/environment

- performance psychology,
- mental-health routing,
- training music,
- travel/environment.

## 23. Non-goals

The first versions will not:

- diagnose disease or injury,
- provide medical clearance,
- replace physiotherapy,
- replace psychotherapy,
- claim injury prediction from ACWR or any single metric,
- generate a universal readiness score presented as validated truth,
- rigidly prescribe training by menstrual-cycle phase,
- make age alone a reason to remove intensity, heavy strength or power training.

## 24. Definition of done for the overall program

The sport athlete-management program is mature enough for practical use when:

- athlete state is persisted independently from reports,
- goals -> season -> meso -> micro -> sessions are linked by IDs,
- every completed session can be compared with its prescription,
- daily recovery/health data can modify training through explicit rules,
- all adaptation decisions are explainable and auditable,
- age and sex modifiers are implemented and evaluated without stereotyping,
- injury/illness red flags route safely,
- testing results update future planning,
- longitudinal adaptation can be analyzed,
- specialist skills remain composable,
- the existing diagnostic/report stack can consume the new structured outputs.

## 25. Recommended first implementation slice

Start with the smallest vertical slice that proves the architecture:

1. athlete profile,
2. one goal + one target competition,
3. one mesocycle + one microcycle,
4. planned sessions,
5. morning check-in,
6. completed session + sRPE,
7. adaptation decision,
8. next-session revision,
9. audit history,
10. minimal dashboard.

Do not begin with wearables, music, advanced analytics or a broad psychological module. First prove that the core training-control loop is reliable, explainable and easy enough to use every day.
