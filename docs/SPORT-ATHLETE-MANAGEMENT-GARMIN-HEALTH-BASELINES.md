# Sport Athlete Management – Garmin Health, Biometric Baselines and Body Composition

Status: normative extension to `SPORT-ATHLETE-MANAGEMENT-SPEC.md`  
Date: 2026-08-28

## 1. Purpose

This extension integrates passive wearable/health data into the existing Sport Athlete Management closed loop without creating a parallel “health twin” or a second training-decision system.

The governing architecture remains:

`profile -> goal -> plan -> session -> athlete response -> objective/passive response -> adaptation decision -> versioned revision -> retest`

Garmin and comparable wearable platforms are **data providers**. They do not own the training decision.

## 2. Design decision

The system adopts four useful ideas commonly seen in consumer health platforms:

1. passive longitudinal monitoring,
2. athlete-specific physiological baselines,
3. method-aware body/structural trends,
4. easy-to-read longitudinal trend views.

The system explicitly rejects opaque pseudo-precision as a control mechanism:

- no Biological Age as a health truth,
- no Pace of Aging,
- no Lifespan Meter / “days gained”,
- no Metabolic Capacity or Momentum as a validated physiological construct,
- no universal Health/Readiness score that controls training.

Provider-specific scores may be displayed with provenance, but their decision role is limited.

## 3. Metric taxonomy

Every persisted objective/passive metric must preserve at least:

- metric type,
- measured timestamp,
- value and unit,
- source/provider,
- device where known,
- method where known,
- quality flag,
- metric class,
- decision role,
- comparable-series identity where needed.

### 3.1 Metric classes

- `direct_sensor`: provider/device observation closest to a measured signal, e.g. resting HR, nocturnal HRV, respiration.
- `provider_derived`: proprietary provider output, e.g. Garmin Training Readiness, Body Battery, Sleep Score, Training Status, Fitness Age.
- `journal_derived`: deterministic Sports Journal output, e.g. baseline deviation or Health Drift.
- `reference_measurement`: reference/clinical or higher-order method, e.g. DXA body composition.
- `manual_measurement`: structured manual measurement, e.g. waist circumference.

### 3.2 Decision roles

- `primary_evidence`: may contribute materially to a decision but never bypasses safety/multisignal rules.
- `context_only`: may support interpretation but must not independently change training.
- `display_only`: athlete-facing context only.
- `excluded_from_adaptation`: retained only if there is a clear product reason; never used by the adaptation engine.

Provider-derived readiness/longevity scores default to `context_only`, `display_only` or `excluded_from_adaptation`.

## 4. Garmin integration boundary

### 4.1 Activity layer

Existing Garmin FIT/TCX ingestion remains the canonical path for training-session observations. Garmin, Concept2 and RP3 observations may describe the same activity and retain source provenance after deduplication.

### 4.2 Passive health layer

A future Garmin Health/API adapter may ingest, subject to actual API availability and athlete consent:

- resting/night HR,
- HRV,
- sleep duration and selected sleep summaries,
- respiration,
- skin-temperature trend/delta,
- Pulse Ox / SpO₂,
- Body Battery and other provider-derived context,
- body composition where supplied.

Passive health ingestion is separate from activity ingestion but joins the same athlete timeline.

### 4.3 Training publication

If Garmin Training API access is available, an approved/versioned Sports Journal prescription may be published to Garmin Connect. Publication occurs **after** the adaptation decision and athlete/human-control rules; Garmin does not generate the authoritative prescription.

## 5. Individual biometric baselines

Robust personal baselines are preferred over population cut-offs where clinically safe.

Baseline candidates include:

- resting HR,
- HRV,
- respiration,
- skin-temperature trend,
- sleep duration,
- selected SpO₂ summaries.

Requirements:

- minimum data coverage before activation,
- robust center/spread method documented,
- method/device comparability checked,
- missing data not treated as normal,
- device/firmware/method changes flagged,
- baseline version/window retained for audit.

A baseline is not a “normal health” guarantee; it is the athlete’s recent reference distribution.

## 6. Health Drift

`Health Drift` is a Sports Journal derived state describing physiological instability relative to the athlete’s baseline.

Allowed states:

- `normal`
- `elevated`
- `persistent`
- `resolving`
- `unknown`

Rules:

1. a single abnormal wearable value is insufficient for escalation;
2. persistence and multiple independent signals increase relevance;
3. data quality and device/method changes are checked before interpretation;
4. symptoms, pain, illness, training load, travel, environment and subjective recovery provide context;
5. Health Drift is not a diagnosis;
6. RED medical/safety signals bypass wellness scoring and route appropriately.

## 7. Morning Check remains mandatory as a concept

Passive data reduces friction but does not replace the athlete’s own report.

The daily routine continues to capture, as available:

- sleep quality,
- fatigue,
- soreness,
- stress,
- motivation,
- pain and location,
- illness symptoms.

Wearable data and subjective data may disagree. Such conflicts remain visible and lower confidence instead of being silently resolved in favor of the device.

## 8. Recovery interpretation

Recovery analysis combines:

- subjective recovery,
- sleep,
- resting HR/HRV,
- training history,
- physiological stability,
- contextual stressors,
- provider-derived scores only as context.

No provider readiness score or HRV value is an autonomous regulator.

## 9. Body and structural context

The system adds method-aware longitudinal body measurements:

- body mass,
- waist circumference,
- waist-height ratio,
- body fat,
- fat mass,
- fat-free/lean mass,
- bone mineral density when actually measured by an appropriate method.

Each series records method and quality class.

### 9.1 BIA

Consumer BIA may be useful for trends when conditions and device are stable. BIA-derived fat/lean estimates are not silently equated with DXA.

A BIA device’s “bone density” estimate is **not** treated as measured bone mineral density.

### 9.2 DXA

DXA values may be stored as a separate reference series. They do not overwrite consumer estimates; comparison requires explicit method awareness.

## 10. Five longitudinal analysis domains

Sports Journal longitudinal analysis remains multi-dimensional and does not collapse to one health number:

1. **Recovery**
2. **Training tolerance**
3. **Performance capacity**
4. **Physiological stability**
5. **Body / Energy context**

Each domain reports direction, evidence, coverage and uncertainty independently.

## 11. Adaptation-engine rules

The adaptation engine must:

- run safety gates before performance optimization;
- prefer repeated/multisignal trends to single wearable values;
- retain provider-score provenance;
- never let Garmin Training Readiness, Body Battery, Sleep Score, Training Status, Fitness Age or analogous vendor scores independently determine GREEN/YELLOW/ORANGE/RED;
- use persistent Health Drift plus symptoms/context as possible `health_route` evidence;
- avoid acute training modification from body mass/BIA alone;
- route combined body-mass/performance/recovery signals to Fueling/RED-S/health review where relevant;
- preserve human override and full auditability.

## 12. UI implications

Athlete-facing views should show domains rather than a single health score.

Preferred pattern:

- Recovery: trend/state + responsible signals
- Training tolerance: trend/state + load context
- Performance capacity: trend/state + tests/standard workloads
- Physiological stability: normal/elevated/persistent/resolving + signal details
- Body / Energy: trend/context + method label

Provider scores can appear in a secondary “device context” area.

Do not promote Biological Age, Pace of Aging, Lifespan, Metabolic Capacity or a universal Health score to primary navigation.

## 13. Persistence additions

The product data model should support, when implemented:

- `device_connections`
- enhanced `objective_metrics`
- `biometric_baselines`
- `biometric_anomalies`
- `body_measurements`

These additions preserve source provenance and do not change the architectural boundary: PostgreSQL is the operational source of truth, Skillz owns sport-science reasoning, and provider systems remain external observations.

## 14. Validation requirements

Before a metric influences training:

1. identify whether it is direct, provider-derived or journal-derived;
2. document device/method and evidence limitations;
3. define a decision role;
4. verify baseline eligibility and comparability;
5. test missing/outlier/device-change behavior;
6. verify that no single provider score can modify a plan;
7. verify that safety flags override favorable wellness signals;
8. keep every derived state traceable to underlying observations.

## 15. Acceptance criterion

The extension is correctly integrated when an athlete can have passive Garmin data, subjective Morning Check data, activity data and body measurements on one timeline; Sports Journal can derive transparent baselines/Health Drift; the adaptation engine can use the relevant underlying signals without delegating the decision to Garmin/Hume-style opaque scores; and every decision remains explainable and audit-reconstructable.
