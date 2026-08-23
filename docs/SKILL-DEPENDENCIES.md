# Skill Dependency Graph

Generated from canonical `requires`, `consumes`, and `outputs` frontmatter. Do not edit manually.

```mermaid
graph TD
  agent_handoff --> iterate_software_projects
  architecture_deepening_review --> disciplined_diagnosis
  architecture_deepening_review --> iterate_software_projects
  audit_inspection_finding_response --> decision_record
  audit_inspection_finding_response --> regulatory_evidence_traceability
  candidate_role_fit_assessment --> role_architecture
  central_skill_repository_curation --> composable_skill_factory
  clinical_evidence_update_impact --> decision_record
  clinical_evidence_update_impact --> regulated_product_context
  clinical_evidence_update_impact --> regulatory_evidence_traceability
  clinical_evidence_update_impact --> research_to_evidence_note
  contract_drafting --> contract_legal_context
  contract_legal_context --> research_to_evidence_note
  contract_review --> contract_legal_context
  contract_workflow --> contract_drafting
  contract_workflow --> contract_legal_context
  contract_workflow --> contract_review
  contract_workflow --> round_based_requirements_grilling
  controlled_quality_documentation --> regulated_product_context
  controlled_quality_documentation --> two_axis_compliance_review
  daily_and_weekly_review --> inbox_action_triage
  decision_and_follow_up_tracker --> daily_and_weekly_review
  decision_and_follow_up_tracker --> meeting_preparation
  decision_and_follow_up_tracker --> project_status_brief
  decision_record --> agent_handoff
  decision_record --> large_work_wayfinder
  decision_record --> throwaway_prototype
  decision_record --> two_axis_code_review
  design_change_regulatory_impact --> decision_record
  design_change_regulatory_impact --> design_control_traceability
  design_change_regulatory_impact --> medical_device_risk_management_iso14971
  design_change_regulatory_impact --> regulatory_evidence_traceability
  design_control_traceability --> medical_device_risk_management_iso14971
  design_control_traceability --> regulated_product_context
  design_control_traceability --> two_axis_compliance_review
  disciplined_diagnosis --> iterate_software_projects
  domain_model_maintenance --> agent_handoff
  domain_model_maintenance --> architecture_deepening_review
  domain_model_maintenance --> decision_record
  domain_model_maintenance --> test_driven_vertical_slice
  domain_model_maintenance --> two_axis_code_review
  dr_komorowski_sport_pdf_report_renderer --> dr_komorowski_sport_docx_report_renderer
  engineering_delivery_followup --> deferred_external_action_verification
  engineering_delivery_followup --> two_axis_code_review
  eu_mdr_ivdr_regulatory_specialist --> medical_device_risk_management_iso14971
  eu_mdr_ivdr_regulatory_specialist --> regulated_product_context
  eu_mdr_ivdr_regulatory_specialist --> research_to_evidence_note
  eudamed_udi_ivd --> ivdr_device_classification
  eudamed_udi_ivd --> medical_device_labeling_ifu
  eudamed_udi_ivd --> regulated_product_context
  eudamed_udi_ivd --> regulatory_evidence_traceability
  euroimmun_pdf_report_renderer --> euroimmun_docx_report_renderer
  evidence_based_causal_investigation --> research_to_evidence_note
  exam_trainer_catalog_builder --> learning_assessment_spec
  exam_trainer_catalog_builder --> learning_mission
  fda_510k_predicate_strategy --> fda_device_classification_product_code
  fda_510k_predicate_strategy --> regulated_product_context
  fda_510k_predicate_strategy --> regulatory_evidence_traceability
  fda_510k_predicate_strategy --> research_to_evidence_note
  fda_510k_substantial_equivalence --> fda_510k_predicate_strategy
  fda_510k_substantial_equivalence --> medical_device_risk_management_iso14971
  fda_510k_substantial_equivalence --> regulatory_evidence_traceability
  fda_acceptance_readiness --> fda_estar_submission_builder
  fda_acceptance_readiness --> regulatory_evidence_traceability
  fda_acceptance_readiness --> two_axis_compliance_review
  fda_additional_information_response --> decision_record
  fda_additional_information_response --> fda_estar_submission_builder
  fda_additional_information_response --> regulatory_evidence_traceability
  fda_complaint_mdr_reportability --> medical_device_risk_management_iso14971
  fda_complaint_mdr_reportability --> quality_record_integrity
  fda_complaint_mdr_reportability --> regulated_product_context
  fda_complaint_mdr_reportability --> regulatory_evidence_traceability
  fda_corrections_removals --> decision_record
  fda_corrections_removals --> fda_complaint_mdr_reportability
  fda_corrections_removals --> medical_device_capa
  fda_corrections_removals --> medical_device_risk_management_iso14971
  fda_de_novo_special_controls --> fda_de_novo_strategy
  fda_de_novo_special_controls --> medical_device_risk_management_iso14971
  fda_de_novo_special_controls --> regulatory_evidence_traceability
  fda_de_novo_strategy --> fda_device_classification_product_code
  fda_de_novo_strategy --> medical_device_risk_management_iso14971
  fda_de_novo_strategy --> regulated_product_context
  fda_de_novo_strategy --> regulatory_evidence_traceability
  fda_device_classification_product_code --> regulated_product_context
  fda_device_classification_product_code --> regulatory_evidence_traceability
  fda_device_classification_product_code --> research_to_evidence_note
  fda_dual_510k_clia_waiver --> fda_510k_substantial_equivalence
  fda_dual_510k_clia_waiver --> fda_ivd_clia_waiver
  fda_dual_510k_clia_waiver --> regulatory_evidence_traceability
  fda_estar_submission_builder --> fda_medical_device_ivd_regulatory_specialist
  fda_estar_submission_builder --> regulatory_evidence_traceability
  fda_ivd_clia_waiver --> fda_device_classification_product_code
  fda_ivd_clia_waiver --> medical_device_risk_management_iso14971
  fda_ivd_clia_waiver --> regulated_product_context
  fda_ivd_clia_waiver --> regulatory_evidence_traceability
  fda_medical_device_ivd_regulatory_specialist --> medical_device_qms_iso13485
  fda_medical_device_ivd_regulatory_specialist --> regulated_product_context
  fda_medical_device_ivd_regulatory_specialist --> research_to_evidence_note
  fda_pccp_change_control --> decision_record
  fda_pccp_change_control --> design_change_regulatory_impact
  fda_pccp_change_control --> medical_device_risk_management_iso14971
  fda_pccp_change_control --> regulatory_evidence_traceability
  fda_qmsr_inspection_readiness --> fda_qmsr_iso13485_gap
  fda_qmsr_inspection_readiness --> iso13485_qms_audit
  fda_qmsr_inspection_readiness --> two_axis_compliance_review
  fda_qmsr_iso13485_gap --> medical_device_qms_iso13485
  fda_qmsr_iso13485_gap --> regulatory_evidence_traceability
  fda_qmsr_iso13485_gap --> two_axis_compliance_review
  fda_qsub_strategy --> decision_record
  fda_qsub_strategy --> fda_medical_device_ivd_regulatory_specialist
  fda_qsub_strategy --> regulatory_evidence_traceability
  fda_recall_status_termination --> fda_corrections_removals
  fda_recall_status_termination --> medical_device_field_action_effectiveness
  fda_recall_status_termination --> quality_record_integrity
  fda_recall_status_termination --> regulatory_evidence_traceability
  fda_registration_listing_udi --> decision_record
  fda_registration_listing_udi --> medical_device_labeling_ifu
  fda_registration_listing_udi --> regulated_product_context
  fda_registration_listing_udi --> regulatory_evidence_traceability
  freedom_to_operate_assessment --> research_to_evidence_note
  frontend_design_director --> communication_memory_governance
  frontend_design_director --> frontend_design_review
  frontend_design_director --> frontend_design_shaping
  frontend_design_director --> frontend_design_system_context
  frontend_design_director --> frontend_product_context
  frontend_design_review --> frontend_design_system_context
  frontend_design_review --> frontend_product_context
  frontend_design_shaping --> frontend_design_system_context
  frontend_design_shaping --> frontend_product_context
  frontend_design_shaping --> large_work_wayfinder
  frontend_design_shaping --> round_based_requirements_grilling
  frontend_design_system_context --> frontend_product_context
  frontend_design_system_context --> round_based_requirements_grilling
  frontend_product_context --> round_based_requirements_grilling
  iec62304_software_lifecycle --> design_control_traceability
  iec62304_software_lifecycle --> medical_device_qms_iso13485
  iec62304_software_lifecycle --> medical_device_risk_management_iso14971
  iec62304_software_lifecycle --> regulated_product_context
  iec62366_usability_engineering --> design_control_traceability
  iec62366_usability_engineering --> medical_device_labeling_ifu
  iec62366_usability_engineering --> medical_device_risk_management_iso14971
  iec62366_usability_engineering --> regulated_product_context
  implement_from_issue --> agent_handoff
  implement_from_issue --> deferred_external_action_verification
  implement_from_issue --> disciplined_diagnosis
  implement_from_issue --> test_driven_vertical_slice
  iso13485_qms_audit --> medical_device_qms_iso13485
  iso13485_qms_audit --> two_axis_compliance_review
  iso27001_isms_audit --> medical_device_isms_governance
  iso27001_isms_audit --> two_axis_compliance_review
  ivdr_analytical_performance --> medical_device_risk_management_iso14971
  ivdr_analytical_performance --> regulated_product_context
  ivdr_analytical_performance --> regulatory_evidence_traceability
  ivdr_class_d_conformity --> ivdr_device_classification
  ivdr_class_d_conformity --> ivdr_performance_evaluation
  ivdr_class_d_conformity --> mdcg_guidance_navigator
  ivdr_class_d_conformity --> regulatory_evidence_traceability
  ivdr_clinical_performance_study --> mdcg_guidance_navigator
  ivdr_clinical_performance_study --> medical_device_risk_management_iso14971
  ivdr_clinical_performance_study --> regulated_product_context
  ivdr_clinical_performance_study --> regulatory_evidence_traceability
  ivdr_companion_diagnostic_consultation --> decision_record
  ivdr_companion_diagnostic_consultation --> ivdr_device_classification
  ivdr_companion_diagnostic_consultation --> ivdr_performance_evaluation
  ivdr_companion_diagnostic_consultation --> regulated_product_context
  ivdr_companion_diagnostic_consultation --> regulatory_evidence_traceability
  ivdr_device_classification --> mdcg_guidance_navigator
  ivdr_device_classification --> regulated_product_context
  ivdr_device_classification --> regulatory_evidence_traceability
  ivdr_economic_operator_postmarket_propagation --> quality_record_integrity
  ivdr_economic_operator_postmarket_propagation --> regulated_product_context
  ivdr_economic_operator_postmarket_propagation --> regulatory_evidence_traceability
  ivdr_field_safety_corrective_action --> controlled_quality_documentation
  ivdr_field_safety_corrective_action --> ivdr_pms_vigilance
  ivdr_field_safety_corrective_action --> mdcg_guidance_navigator
  ivdr_field_safety_corrective_action --> medical_device_capa
  ivdr_field_safety_corrective_action --> medical_device_risk_management_iso14971
  ivdr_field_safety_corrective_action --> regulatory_evidence_traceability
  ivdr_fsca_status_final_reporting --> ivdr_field_safety_corrective_action
  ivdr_fsca_status_final_reporting --> mdcg_guidance_navigator
  ivdr_fsca_status_final_reporting --> medical_device_field_action_effectiveness
  ivdr_fsca_status_final_reporting --> regulatory_evidence_traceability
  ivdr_inhouse_health_institution --> decision_record
  ivdr_inhouse_health_institution --> medical_device_qms_iso13485
  ivdr_inhouse_health_institution --> medical_device_risk_management_iso14971
  ivdr_inhouse_health_institution --> regulated_product_context
  ivdr_inhouse_health_institution --> regulatory_evidence_traceability
  ivdr_performance_evaluation --> ivdr_analytical_performance
  ivdr_performance_evaluation --> ivdr_clinical_performance_study
  ivdr_performance_evaluation --> ivdr_scientific_validity
  ivdr_performance_evaluation --> regulatory_evidence_traceability
  ivdr_performance_evaluation_report --> ivdr_performance_evaluation
  ivdr_performance_evaluation_report --> mdcg_guidance_navigator
  ivdr_performance_evaluation_report --> regulatory_evidence_traceability
  ivdr_pmpf --> ivdr_performance_evaluation
  ivdr_pmpf --> mdcg_guidance_navigator
  ivdr_pmpf --> medical_device_risk_management_iso14971
  ivdr_pmpf --> regulatory_evidence_traceability
  ivdr_pms_vigilance --> mdcg_guidance_navigator
  ivdr_pms_vigilance --> medical_device_pms_system
  ivdr_pms_vigilance --> medical_device_risk_management_iso14971
  ivdr_pms_vigilance --> regulated_product_context
  ivdr_pms_vigilance --> regulatory_evidence_traceability
  ivdr_pms_vigilance --> two_axis_compliance_review
  ivdr_scientific_validity --> regulated_product_context
  ivdr_scientific_validity --> regulatory_evidence_traceability
  ivdr_scientific_validity --> research_to_evidence_note
  job_description_authoring --> role_architecture
  knowledge_map_generator --> structured_knowledge_artifact
  knowledge_view --> structured_knowledge_artifact
  large_work_wayfinder --> agent_handoff
  large_work_wayfinder --> architecture_deepening_review
  large_work_wayfinder --> disciplined_diagnosis
  learning_assessment --> learning_assessment_spec
  learning_assessment_spec --> learning_mission
  learning_assessment_spec --> learning_state
  learning_next_step --> learning_mission
  learning_next_step --> learning_state
  mdcg_guidance_navigator --> regulated_product_context
  mdcg_guidance_navigator --> regulatory_evidence_traceability
  mdcg_guidance_navigator --> research_to_evidence_note
  mdsap_audit_readiness --> iso13485_qms_audit
  mdsap_audit_readiness --> medical_device_qms_iso13485
  mdsap_audit_readiness --> regulatory_evidence_traceability
  measurement_system_validation --> medical_device_qms_iso13485
  measurement_system_validation --> medical_device_risk_management_iso14971
  measurement_system_validation --> two_axis_compliance_review
  medical_device_adverse_event_coding --> medical_device_complaint_handling
  medical_device_adverse_event_coding --> regulatory_evidence_traceability
  medical_device_capa --> evidence_based_causal_investigation
  medical_device_capa --> medical_device_qms_iso13485
  medical_device_capa --> medical_device_risk_management_iso14971
  medical_device_complaint_customer_followup --> medical_device_complaint_handling
  medical_device_complaint_customer_followup --> quality_record_integrity
  medical_device_complaint_customer_followup --> regulated_product_context
  medical_device_complaint_handling --> medical_device_customer_contact_intake
  medical_device_complaint_handling --> quality_record_integrity
  medical_device_complaint_handling --> regulated_product_context
  medical_device_complaint_regulatory_routing --> fda_complaint_mdr_reportability
  medical_device_complaint_regulatory_routing --> ivdr_pms_vigilance
  medical_device_complaint_regulatory_routing --> medical_device_complaint_customer_followup
  medical_device_complaint_regulatory_routing --> medical_device_complaint_handling
  medical_device_complaint_regulatory_routing --> regulated_product_context
  medical_device_complaint_regulatory_routing --> regulatory_evidence_traceability
  medical_device_customer_contact_intake --> quality_record_integrity
  medical_device_cybersecurity_lifecycle --> design_control_traceability
  medical_device_cybersecurity_lifecycle --> iec62304_software_lifecycle
  medical_device_cybersecurity_lifecycle --> medical_device_risk_management_iso14971
  medical_device_cybersecurity_lifecycle --> regulated_product_context
  medical_device_field_action_communication --> controlled_quality_documentation
  medical_device_field_action_communication --> quality_record_integrity
  medical_device_field_action_communication --> regulated_product_context
  medical_device_field_action_effectiveness --> medical_device_capa
  medical_device_field_action_effectiveness --> medical_device_field_action_communication
  medical_device_field_action_effectiveness --> medical_device_field_action_physical_execution
  medical_device_field_action_effectiveness --> medical_device_pms_system
  medical_device_field_action_effectiveness --> medical_device_risk_management_iso14971
  medical_device_field_action_effectiveness --> quality_record_integrity
  medical_device_field_action_physical_execution --> controlled_quality_documentation
  medical_device_field_action_physical_execution --> medical_device_field_action_communication
  medical_device_field_action_physical_execution --> quality_record_integrity
  medical_device_isms_governance --> regulated_product_context
  medical_device_isms_governance --> two_axis_compliance_review
  medical_device_labeling_ifu --> medical_device_risk_management_iso14971
  medical_device_labeling_ifu --> regulated_product_context
  medical_device_labeling_ifu --> regulatory_evidence_traceability
  medical_device_pms_system --> decision_record
  medical_device_pms_system --> medical_device_risk_management_iso14971
  medical_device_pms_system --> regulated_product_context
  medical_device_pms_system --> regulatory_evidence_traceability
  medical_device_privacy_gdpr_bdsg --> regulated_product_context
  medical_device_privacy_gdpr_bdsg --> research_to_evidence_note
  medical_device_privacy_gdpr_bdsg --> two_axis_compliance_review
  medical_device_qms_iso13485 --> regulated_product_context
  medical_device_qms_iso13485 --> two_axis_compliance_review
  medical_device_regulatory_strategy --> eu_mdr_ivdr_regulatory_specialist
  medical_device_regulatory_strategy --> fda_medical_device_ivd_regulatory_specialist
  medical_device_regulatory_strategy --> large_work_wayfinder
  medical_device_regulatory_strategy --> medical_device_risk_management_iso14971
  medical_device_regulatory_strategy --> regulated_product_context
  medical_device_risk_management_iso14971 --> regulated_product_context
  medical_device_risk_management_iso14971 --> research_to_evidence_note
  medical_device_service_report_quality_routing --> medical_device_customer_contact_intake
  medical_device_service_report_quality_routing --> quality_record_integrity
  meeting_preparation --> research_to_evidence_note
  memory_sync_reconciliation --> communication_memory_governance
  merge_conflict_resolution --> agent_handoff
  merge_conflict_resolution --> deferred_external_action_verification
  merge_conflict_resolution --> disciplined_diagnosis
  merge_conflict_resolution --> test_driven_vertical_slice
  merge_conflict_resolution --> two_axis_code_review
  nonconformance_mrb_disposition --> medical_device_qms_iso13485
  nonconformance_mrb_disposition --> medical_device_risk_management_iso14971
  nonconformance_mrb_disposition --> two_axis_compliance_review
  obsidian_adapter --> knowledge_map_generator
  obsidian_adapter --> knowledge_view
  obsidian_adapter --> structured_knowledge_artifact
  patent_landscape_analysis --> research_to_evidence_note
  precision_writing_revision --> author_voice_profiler
  precision_writing_revision --> llm_prose_pattern_audit
  precision_writing_revision --> precision_language_rewriter
  precision_writing_revision --> rewrite_fidelity_verifier
  process_validation_iq_oq_pq --> design_control_traceability
  process_validation_iq_oq_pq --> medical_device_qms_iso13485
  process_validation_iq_oq_pq --> medical_device_risk_management_iso14971
  product_evidence_research --> research_to_evidence_note
  project_beta_readiness --> iterate_software_projects
  purchase_decision_planner --> price_availability_snapshot
  purchase_decision_planner --> product_comparison_ranking
  purchase_decision_planner --> product_evidence_research
  qms_management_review_action_followup --> decision_and_follow_up_tracker
  qms_management_review_action_followup --> deferred_external_action_verification
  qms_management_review_action_followup --> qms_management_review_governance
  qms_management_review_governance --> iso13485_qms_audit
  qms_management_review_governance --> medical_device_capa
  qms_management_review_governance --> medical_device_pms_system
  qms_management_review_governance --> medical_device_qms_iso13485
  qms_management_review_governance --> project_status_brief
  quality_record_integrity --> controlled_quality_documentation
  quality_record_integrity --> medical_device_qms_iso13485
  quality_record_integrity --> two_axis_compliance_review
  regulatory_change_impact_orchestrator --> decision_record
  regulatory_change_impact_orchestrator --> regulated_product_context
  regulatory_change_impact_orchestrator --> regulatory_evidence_traceability
  regulatory_change_monitoring --> regulatory_evidence_traceability
  regulatory_change_monitoring --> research_to_evidence_note
  regulatory_claims_consistency --> design_control_traceability
  regulatory_claims_consistency --> medical_device_labeling_ifu
  regulatory_claims_consistency --> regulated_product_context
  regulatory_claims_consistency --> regulatory_evidence_traceability
  regulatory_evidence_traceability --> regulated_product_context
  regulatory_evidence_traceability --> research_to_evidence_note
  role_requirements_grilling --> round_based_requirements_grilling
  spec_to_vertical_issues --> conversation_to_spec
  sport_adaptation_analysis --> sport_daily_athlete_monitoring
  sport_adaptation_analysis --> sport_microcycle_planning
  sport_adaptation_analysis --> sport_performance_diagnostics
  sport_athlete_management --> sport_adaptation_analysis
  sport_athlete_management --> sport_athlete_profile
  sport_athlete_management --> sport_daily_athlete_monitoring
  sport_athlete_management --> sport_endurance_programming
  sport_athlete_management --> sport_environment_travel
  sport_athlete_management --> sport_goal_performance_model
  sport_athlete_management --> sport_injury_rehabilitation
  sport_athlete_management --> sport_mental_health_routing
  sport_athlete_management --> sport_mesocycle_planning
  sport_athlete_management --> sport_microcycle_planning
  sport_athlete_management --> sport_nutrition_fueling
  sport_athlete_management --> sport_performance_psychology
  sport_athlete_management --> sport_recovery_sleep
  sport_athlete_management --> sport_return_after_illness
  sport_athlete_management --> sport_season_periodization
  sport_athlete_management --> sport_strength_power_programming
  sport_athlete_management --> sport_testing_battery
  sport_athlete_management --> sport_training_adaptation_engine
  sport_athlete_management --> sport_training_music
  sport_daily_athlete_monitoring --> sport_athlete_profile
  sport_diagnostics_training_report_workflow --> dr_komorowski_sport_docx_report_renderer
  sport_diagnostics_training_report_workflow --> dr_komorowski_sport_pdf_report_renderer
  sport_diagnostics_training_report_workflow --> sport_performance_diagnostics
  sport_diagnostics_training_report_workflow --> sport_training_programming
  sport_endurance_programming --> sport_athlete_profile
  sport_endurance_programming --> sport_goal_performance_model
  sport_endurance_programming --> sport_mesocycle_planning
  sport_endurance_programming --> sport_microcycle_planning
  sport_endurance_programming --> sport_performance_diagnostics
  sport_environment_travel --> sport_athlete_profile
  sport_environment_travel --> sport_microcycle_planning
  sport_environment_travel --> sport_recovery_sleep
  sport_goal_performance_model --> sport_athlete_profile
  sport_injury_rehabilitation --> sport_athlete_profile
  sport_injury_rehabilitation --> sport_daily_athlete_monitoring
  sport_mental_health_routing --> sport_athlete_profile
  sport_mental_health_routing --> sport_daily_athlete_monitoring
  sport_mesocycle_planning --> sport_season_periodization
  sport_microcycle_planning --> sport_mesocycle_planning
  sport_nutrition_fueling --> sport_athlete_profile
  sport_nutrition_fueling --> sport_daily_athlete_monitoring
  sport_nutrition_fueling --> sport_mesocycle_planning
  sport_nutrition_fueling --> sport_microcycle_planning
  sport_performance_psychology --> sport_athlete_profile
  sport_performance_psychology --> sport_goal_performance_model
  sport_performance_psychology --> sport_microcycle_planning
  sport_recovery_sleep --> sport_athlete_profile
  sport_recovery_sleep --> sport_daily_athlete_monitoring
  sport_return_after_illness --> sport_athlete_profile
  sport_return_after_illness --> sport_daily_athlete_monitoring
  sport_season_periodization --> sport_goal_performance_model
  sport_strength_power_programming --> sport_athlete_profile
  sport_strength_power_programming --> sport_goal_performance_model
  sport_strength_power_programming --> sport_mesocycle_planning
  sport_strength_power_programming --> sport_microcycle_planning
  sport_testing_battery --> sport_athlete_profile
  sport_testing_battery --> sport_goal_performance_model
  sport_testing_battery --> sport_season_periodization
  sport_training_adaptation_engine --> sport_athlete_profile
  sport_training_adaptation_engine --> sport_daily_athlete_monitoring
  sport_training_adaptation_engine --> sport_microcycle_planning
  sport_training_music --> sport_athlete_profile
  sport_training_music --> sport_microcycle_planning
  supplier_quality_medical_device --> medical_device_qms_iso13485
  supplier_quality_medical_device --> medical_device_risk_management_iso14971
  supplier_quality_medical_device --> two_axis_compliance_review
  teach --> exam_trainer_catalog_builder
  teach --> exam_trainer_result_import
  teach --> learning_assessment
  teach --> learning_assessment_spec
  teach --> learning_mission
  teach --> learning_next_step
  teach --> learning_state
  teach --> research_to_evidence_note
  technology_due_diligence --> technology_offer_assessment
  technology_offer_assessment --> research_to_evidence_note
  test_driven_vertical_slice --> disciplined_diagnosis
  test_driven_vertical_slice --> spec_to_vertical_issues
  throwaway_prototype --> agent_handoff
  throwaway_prototype --> disciplined_diagnosis
  throwaway_prototype --> large_work_wayfinder
  throwaway_prototype --> spec_to_vertical_issues
  two_axis_code_review --> agent_handoff
  two_axis_code_review --> architecture_deepening_review
  two_axis_code_review --> disciplined_diagnosis
  two_axis_code_review --> implement_from_issue
  two_axis_compliance_review --> research_to_evidence_note
```

## Artifact consumption

`requires` declares hard skill prerequisites. `consumes` declares concrete artifacts a skill can consume without creating a hard prerequisite edge. For backward compatibility, outputs of a required skill are inferred as consumed only when the consumer declares no explicit `consumes` list. Explicit artifact consumption therefore takes precedence over broad legacy inference.

| Consumer | Artifact | Producer |
|---|---|---|
| `candidate-role-fit-assessment` | `role-architecture.json` | `role-architecture` |
| `candidate-role-fit-assessment` | `role-scorecard.json` | `role-architecture` |
| `job-description-authoring` | `role-architecture.json` | `role-architecture` |
| `job-description-authoring` | `role-scorecard.json` | `role-architecture` |
| `role-architecture` | `role-requirements-handoff.json` | `role-requirements-grilling` |

## Output contracts

`consumerSkills` prefer explicit `consumes` declarations. Legacy consumer inference from hard `requires` remains only for consumers without an explicit artifact list. Ambiguous producers are never guessed. A missing consumer is reported as `unconsumed`, not as an error: terminal user-facing artifacts are valid outputs.

| Output | Producers | Consumer skills | Status |
|---|---|---|---|
| `DESIGN.md` | `frontend-design-system-context` | `frontend-design-director`, `frontend-design-review`, `frontend-design-shaping` | inferred |
| `GRILL-REPORT.md` | `round-based-requirements-grilling` | `contract-workflow`, `frontend-design-shaping`, `frontend-design-system-context`, `frontend-product-context`, `role-requirements-grilling` | inferred |
| `PRODUCT.md` | `frontend-product-context` | `frontend-design-director`, `frontend-design-review`, `frontend-design-shaping`, `frontend-design-system-context` | inferred |
| `SPEC.md` | `conversation-to-spec` | `spec-to-vertical-issues` | inferred |
| `acceptance-gaps.json` | `fda-acceptance-readiness` | — | unconsumed |
| `adverse-event-code-set.json` | `medical-device-adverse-event-coding` | — | unconsumed |
| `adverse-event-coding-delta.json` | `medical-device-adverse-event-coding` | — | unconsumed |
| `adverse-event-coding-rationale.json` | `medical-device-adverse-event-coding` | — | unconsumed |
| `agent-handoff.json` | `agent-handoff` | `decision-record`, `domain-model-maintenance`, `implement-from-issue`, `large-work-wayfinder`, `merge-conflict-resolution`, `throwaway-prototype`, `two-axis-code-review` | inferred |
| `agent-handoff.md` | `agent-handoff` | `decision-record`, `domain-model-maintenance`, `implement-from-issue`, `large-work-wayfinder`, `merge-conflict-resolution`, `throwaway-prototype`, `two-axis-code-review` | inferred |
| `analytical-performance-assessment.json` | `ivdr-analytical-performance` | `ivdr-performance-evaluation` | inferred |
| `analytical-performance-plan.json` | `ivdr-analytical-performance` | `ivdr-performance-evaluation` | inferred |
| `analytical-performance-report.md` | `ivdr-analytical-performance` | `ivdr-performance-evaluation` | inferred |
| `architecture-review.json` | `architecture-deepening-review` | `domain-model-maintenance`, `large-work-wayfinder`, `two-axis-code-review` | inferred |
| `architecture-review.md` | `architecture-deepening-review` | `domain-model-maintenance`, `large-work-wayfinder`, `two-axis-code-review` | inferred |
| `athlete-management-state.json` | `sport-athlete-management` | — | unconsumed |
| `athlete-profile.json` | `sport-athlete-profile` | `sport-athlete-management`, `sport-daily-athlete-monitoring`, `sport-endurance-programming`, `sport-environment-travel`, `sport-goal-performance-model`, `sport-injury-rehabilitation`, `sport-mental-health-routing`, `sport-nutrition-fueling`, `sport-performance-psychology`, `sport-recovery-sleep`, `sport-return-after-illness`, `sport-strength-power-programming`, `sport-testing-battery`, `sport-training-adaptation-engine`, `sport-training-music` | inferred |
| `audit-finding-response-map.json` | `audit-inspection-finding-response` | — | unconsumed |
| `author-voice-profile.json` | `author-voice-profiler` | `precision-writing-revision` | inferred |
| `author-voice-profile.md` | `author-voice-profiler` | `precision-writing-revision` | inferred |
| `beta-readiness.json` | `project-beta-readiness` | — | unconsumed |
| `beta-readiness.md` | `project-beta-readiness` | — | unconsumed |
| `beta-runbook.md` | `project-beta-readiness` | — | unconsumed |
| `candidate-interview-question-set.md` | `candidate-role-fit-assessment` | — | unconsumed |
| `candidate-role-fit.json` | `candidate-role-fit-assessment` | — | unconsumed |
| `candidate-role-fit.md` | `candidate-role-fit-assessment` | — | unconsumed |
| `capa-effectiveness-plan.json` | `medical-device-capa` | `fda-corrections-removals`, `ivdr-field-safety-corrective-action`, `medical-device-field-action-effectiveness`, `qms-management-review-governance` | inferred |
| `capa-plan.json` | `medical-device-capa` | `fda-corrections-removals`, `ivdr-field-safety-corrective-action`, `medical-device-field-action-effectiveness`, `qms-management-review-governance` | inferred |
| `capa-status.md` | `medical-device-capa` | `fda-corrections-removals`, `ivdr-field-safety-corrective-action`, `medical-device-field-action-effectiveness`, `qms-management-review-governance` | inferred |
| `causal-investigation.json` | `evidence-based-causal-investigation` | `medical-device-capa` | inferred |
| `causal-investigation.md` | `evidence-based-causal-investigation` | `medical-device-capa` | inferred |
| `cdx-consultation-readiness.json` | `ivdr-companion-diagnostic-consultation` | — | unconsumed |
| `cdx-medicinal-product-linkage.json` | `ivdr-companion-diagnostic-consultation` | — | unconsumed |
| `cdx-scope-assessment.json` | `ivdr-companion-diagnostic-consultation` | — | unconsumed |
| `change-impact-assessment.json` | `controlled-quality-documentation` | `ivdr-field-safety-corrective-action`, `medical-device-field-action-communication`, `medical-device-field-action-physical-execution`, `quality-record-integrity` | inferred |
| `change-integration-status.json` | `regulatory-change-impact-orchestrator` | — | unconsumed |
| `change-verification-needs.json` | `design-change-regulatory-impact` | `fda-pccp-change-control` | inferred |
| `claim-conflicts.json` | `regulatory-claims-consistency` | — | unconsumed |
| `claims-consistency-map.json` | `regulatory-claims-consistency` | — | unconsumed |
| `claims-remediation-plan.md` | `regulatory-claims-consistency` | — | unconsumed |
| `class-d-conformity-plan.json` | `ivdr-class-d-conformity` | — | unconsumed |
| `class-d-external-dependencies.json` | `ivdr-class-d-conformity` | — | unconsumed |
| `clia-evidence-gaps.json` | `fda-ivd-clia-waiver` | `fda-dual-510k-clia-waiver` | inferred |
| `clia-waiver-strategy.json` | `fda-ivd-clia-waiver` | `fda-dual-510k-clia-waiver` | inferred |
| `clinical-evidence-actions.json` | `clinical-evidence-update-impact` | — | unconsumed |
| `clinical-evidence-delta.json` | `clinical-evidence-update-impact` | — | unconsumed |
| `clinical-evidence-impact-map.json` | `clinical-evidence-update-impact` | — | unconsumed |
| `clinical-performance-evidence.json` | `ivdr-clinical-performance-study` | `ivdr-performance-evaluation` | inferred |
| `clinical-performance-study-plan.json` | `ivdr-clinical-performance-study` | `ivdr-performance-evaluation` | inferred |
| `communication-profile.json` | `communication-memory-governance` | `frontend-design-director`, `memory-sync-reconciliation` | inferred |
| `communication-profile.merged.json` | `memory-sync-reconciliation` | — | unconsumed |
| `complaint-closure-readiness.json` | `medical-device-complaint-handling` | `medical-device-adverse-event-coding`, `medical-device-complaint-customer-followup`, `medical-device-complaint-regulatory-routing` | inferred |
| `complaint-intake-handoff.json` | `medical-device-customer-contact-intake` | `medical-device-complaint-handling`, `medical-device-service-report-quality-routing` | inferred |
| `complaint-investigation-plan.json` | `medical-device-complaint-handling` | `medical-device-adverse-event-coding`, `medical-device-complaint-customer-followup`, `medical-device-complaint-regulatory-routing` | inferred |
| `complaint-record.json` | `medical-device-complaint-handling` | `medical-device-adverse-event-coding`, `medical-device-complaint-customer-followup`, `medical-device-complaint-regulatory-routing` | inferred |
| `complaint-regulatory-actions.json` | `fda-complaint-mdr-reportability` | `fda-corrections-removals`, `medical-device-complaint-regulatory-routing` | inferred |
| `complaint-regulatory-handoff.json` | `medical-device-complaint-handling` | `medical-device-adverse-event-coding`, `medical-device-complaint-customer-followup`, `medical-device-complaint-regulatory-routing` | inferred |
| `complaint-regulatory-routing.json` | `medical-device-complaint-regulatory-routing` | — | unconsumed |
| `completed-session.json` | `sport-daily-athlete-monitoring` | `sport-adaptation-analysis`, `sport-athlete-management`, `sport-injury-rehabilitation`, `sport-mental-health-routing`, `sport-nutrition-fueling`, `sport-recovery-sleep`, `sport-return-after-illness`, `sport-training-adaptation-engine` | inferred |
| `compliance-evidence-effectiveness.json` | `two-axis-compliance-review` | `controlled-quality-documentation`, `design-control-traceability`, `fda-acceptance-readiness`, `fda-qmsr-inspection-readiness`, `fda-qmsr-iso13485-gap`, `iso13485-qms-audit`, `iso27001-isms-audit`, `ivdr-pms-vigilance`, `measurement-system-validation`, `medical-device-isms-governance`, `medical-device-privacy-gdpr-bdsg`, `medical-device-qms-iso13485`, `nonconformance-mrb-disposition`, `quality-record-integrity`, `supplier-quality-medical-device` | inferred |
| `compliance-requirement-coverage.json` | `two-axis-compliance-review` | `controlled-quality-documentation`, `design-control-traceability`, `fda-acceptance-readiness`, `fda-qmsr-inspection-readiness`, `fda-qmsr-iso13485-gap`, `iso13485-qms-audit`, `iso27001-isms-audit`, `ivdr-pms-vigilance`, `measurement-system-validation`, `medical-device-isms-governance`, `medical-device-privacy-gdpr-bdsg`, `medical-device-qms-iso13485`, `nonconformance-mrb-disposition`, `quality-record-integrity`, `supplier-quality-medical-device` | inferred |
| `compliance-review-decision.md` | `two-axis-compliance-review` | `controlled-quality-documentation`, `design-control-traceability`, `fda-acceptance-readiness`, `fda-qmsr-inspection-readiness`, `fda-qmsr-iso13485-gap`, `iso13485-qms-audit`, `iso27001-isms-audit`, `ivdr-pms-vigilance`, `measurement-system-validation`, `medical-device-isms-governance`, `medical-device-privacy-gdpr-bdsg`, `medical-device-qms-iso13485`, `nonconformance-mrb-disposition`, `quality-record-integrity`, `supplier-quality-medical-device` | inferred |
| `conflict-residual-risk-handoff.json` | `merge-conflict-resolution` | — | unconsumed |
| `conflict-resolution-evidence.json` | `merge-conflict-resolution` | — | unconsumed |
| `consistency report` | `conversation-to-spec` | `spec-to-vertical-issues` | inferred |
| `containment-actions.json` | `nonconformance-mrb-disposition` | — | unconsumed |
| `continuation result` | `deferred-external-action-verification` | `engineering-delivery-followup`, `implement-from-issue`, `merge-conflict-resolution`, `qms-management-review-action-followup` | inferred |
| `contract-case.json` | `contract-workflow` | — | unconsumed |
| `contract-draft.md` | `contract-drafting` | `contract-workflow` | inferred |
| `contract-drafting-report.json` | `contract-drafting` | `contract-workflow` | inferred |
| `contract-handoff.json` | `contract-workflow` | — | unconsumed |
| `contract-issue-list.json` | `contract-review` | `contract-workflow` | inferred |
| `contract-legal-context.json` | `contract-legal-context` | `contract-drafting`, `contract-review`, `contract-workflow` | inferred |
| `contract-legal-source-note.md` | `contract-legal-context` | `contract-drafting`, `contract-review`, `contract-workflow` | inferred |
| `contract-open-points.md` | `contract-drafting` | `contract-workflow` | inferred |
| `contract-plan.md` | `contract-workflow` | — | unconsumed |
| `contract-review.json` | `contract-review` | `contract-workflow` | inferred |
| `contract-review.md` | `contract-review` | `contract-workflow` | inferred |
| `controlled-document-plan.md` | `controlled-quality-documentation` | `ivdr-field-safety-corrective-action`, `medical-device-field-action-communication`, `medical-device-field-action-physical-execution`, `quality-record-integrity` | inferred |
| `correction-removal-action-plan.json` | `fda-corrections-removals` | `fda-recall-status-termination` | inferred |
| `correction-removal-assessment.json` | `fda-corrections-removals` | `fda-recall-status-termination` | inferred |
| `correction-removal-reporting-state.json` | `fda-corrections-removals` | `fda-recall-status-termination` | inferred |
| `customer-communication-record.json` | `medical-device-complaint-customer-followup` | `medical-device-complaint-regulatory-routing` | inferred |
| `customer-contact-record.json` | `medical-device-customer-contact-intake` | `medical-device-complaint-handling`, `medical-device-service-report-quality-routing` | inferred |
| `customer-contact-triage.json` | `medical-device-customer-contact-intake` | `medical-device-complaint-handling`, `medical-device-service-report-quality-routing` | inferred |
| `customer-followup-evidence.json` | `medical-device-complaint-customer-followup` | `medical-device-complaint-regulatory-routing` | inferred |
| `customer-followup-plan.json` | `medical-device-complaint-customer-followup` | `medical-device-complaint-regulatory-routing` | inferred |
| `cybersecurity-evidence-map.json` | `medical-device-cybersecurity-lifecycle` | — | unconsumed |
| `cybersecurity-lifecycle-assessment.json` | `medical-device-cybersecurity-lifecycle` | — | unconsumed |
| `cybersecurity-postmarket-actions.json` | `medical-device-cybersecurity-lifecycle` | — | unconsumed |
| `daily-checkin.json` | `sport-daily-athlete-monitoring` | `sport-adaptation-analysis`, `sport-athlete-management`, `sport-injury-rehabilitation`, `sport-mental-health-routing`, `sport-nutrition-fueling`, `sport-recovery-sleep`, `sport-return-after-illness`, `sport-training-adaptation-engine` | inferred |
| `de-novo-evidence-gaps.json` | `fda-de-novo-strategy` | `fda-de-novo-special-controls` | inferred |
| `de-novo-risk-control-rationale.md` | `fda-de-novo-special-controls` | — | unconsumed |
| `de-novo-strategy.json` | `fda-de-novo-strategy` | `fda-de-novo-special-controls` | inferred |
| `decision register` | `conversation-to-spec` | `spec-to-vertical-issues` | inferred |
| `decision-follow-up-register.json` | `decision-and-follow-up-tracker` | `qms-management-review-action-followup` | inferred |
| `decision-follow-up-register.md` | `decision-and-follow-up-tracker` | `qms-management-review-action-followup` | inferred |
| `decision-record.json` | `decision-record` | `audit-inspection-finding-response`, `clinical-evidence-update-impact`, `design-change-regulatory-impact`, `domain-model-maintenance`, `fda-additional-information-response`, `fda-corrections-removals`, `fda-pccp-change-control`, `fda-qsub-strategy`, `fda-registration-listing-udi`, `ivdr-companion-diagnostic-consultation`, `ivdr-inhouse-health-institution`, `medical-device-pms-system`, `regulatory-change-impact-orchestrator` | inferred |
| `decision-record.md` | `decision-record` | `audit-inspection-finding-response`, `clinical-evidence-update-impact`, `design-change-regulatory-impact`, `domain-model-maintenance`, `fda-additional-information-response`, `fda-corrections-removals`, `fda-pccp-change-control`, `fda-qsub-strategy`, `fda-registration-listing-udi`, `ivdr-companion-diagnostic-consultation`, `ivdr-inhouse-health-institution`, `medical-device-pms-system`, `regulatory-change-impact-orchestrator` | inferred |
| `delivery-review-handoff.json` | `two-axis-code-review` | `decision-record`, `domain-model-maintenance`, `engineering-delivery-followup`, `merge-conflict-resolution` | inferred |
| `dependency-graph.json` | `large-work-wayfinder` | `decision-record`, `frontend-design-shaping`, `medical-device-regulatory-strategy`, `throwaway-prototype` | inferred |
| `dependency-order.json` | `spec-to-vertical-issues` | `test-driven-vertical-slice`, `throwaway-prototype` | inferred |
| `design-change-impact.json` | `design-change-regulatory-impact` | `fda-pccp-change-control` | inferred |
| `design-control-traceability.json` | `design-control-traceability` | `design-change-regulatory-impact`, `iec62304-software-lifecycle`, `iec62366-usability-engineering`, `medical-device-cybersecurity-lifecycle`, `process-validation-iq-oq-pq`, `regulatory-claims-consistency` | inferred |
| `design-evidence-gaps.json` | `design-control-traceability` | `design-change-regulatory-impact`, `iec62304-software-lifecycle`, `iec62366-usability-engineering`, `medical-device-cybersecurity-lifecycle`, `process-validation-iq-oq-pq`, `regulatory-claims-consistency` | inferred |
| `diagnosis-report.json` | `disciplined-diagnosis` | `architecture-deepening-review`, `implement-from-issue`, `large-work-wayfinder`, `merge-conflict-resolution`, `test-driven-vertical-slice`, `throwaway-prototype`, `two-axis-code-review` | inferred |
| `diagnosis-residual-risk-handoff.json` | `disciplined-diagnosis` | `architecture-deepening-review`, `implement-from-issue`, `large-work-wayfinder`, `merge-conflict-resolution`, `test-driven-vertical-slice`, `throwaway-prototype`, `two-axis-code-review` | inferred |
| `disposal-record.json` | `throwaway-prototype` | `decision-record` | inferred |
| `docs/agents/CONFIG.md` | `repository-skill-bootstrap` | — | unconsumed |
| `docs/agents/CONTEXT.md` | `repository-skill-bootstrap` | — | unconsumed |
| `docs/agents/DECISIONS.md` | `repository-skill-bootstrap` | — | unconsumed |
| `document-control-assessment.json` | `controlled-quality-documentation` | `ivdr-field-safety-corrective-action`, `medical-device-field-action-communication`, `medical-device-field-action-physical-execution`, `quality-record-integrity` | inferred |
| `domain-change-plan.md` | `domain-model-maintenance` | — | unconsumed |
| `domain-model-map.json` | `domain-model-maintenance` | — | unconsumed |
| `domain-validation.json` | `domain-model-maintenance` | — | unconsumed |
| `dpia-decision.json` | `medical-device-privacy-gdpr-bdsg` | — | unconsumed |
| `dr-komorowski-report.pdf` | `dr-komorowski-sport-report-renderer` | — | unconsumed |
| `dr-komorowski-sport-report.docx` | `dr-komorowski-sport-docx-report-renderer` | `dr-komorowski-sport-pdf-report-renderer`, `sport-diagnostics-training-report-workflow` | inferred |
| `dr-komorowski-sport-report.pdf` | `dr-komorowski-sport-pdf-report-renderer` | `sport-diagnostics-training-report-workflow` | inferred |
| `dual-510k-clia-strategy.json` | `fda-dual-510k-clia-waiver` | — | unconsumed |
| `dual-evidence-package.json` | `fda-dual-510k-clia-waiver` | — | unconsumed |
| `dual-study-evidence-map.json` | `fda-dual-510k-clia-waiver` | — | unconsumed |
| `due-diligence-handoff.json` | `technology-due-diligence` | — | unconsumed |
| `endurance-plan.json` | `sport-endurance-programming` | `sport-athlete-management` | inferred |
| `energy-availability-risk.json` | `sport-nutrition-fueling` | `sport-athlete-management` | inferred |
| `engineering-closure-gaps.json` | `engineering-delivery-followup` | — | unconsumed |
| `engineering-delivery-status.json` | `engineering-delivery-followup` | — | unconsumed |
| `engineering-iteration-return-input.json` | `engineering-delivery-followup` | — | unconsumed |
| `engineering-iteration-state.json` | `iterate-software-projects` | `agent-handoff`, `architecture-deepening-review`, `disciplined-diagnosis`, `project-beta-readiness` | inferred |
| `environment-adjustment.json` | `sport-environment-travel` | `sport-athlete-management` | inferred |
| `estar-content-map.json` | `fda-estar-submission-builder` | `fda-acceptance-readiness`, `fda-additional-information-response` | inferred |
| `etf-hosted-release-candidate.json` | `exam-trainer-catalog-builder` | `teach` | inferred |
| `etf-teach-catalog.json` | `exam-trainer-catalog-builder` | `teach` | inferred |
| `eu-regulatory-assessment.json` | `eu-mdr-ivdr-regulatory-specialist` | `medical-device-regulatory-strategy` | inferred |
| `eu-regulatory-assessment.md` | `eu-mdr-ivdr-regulatory-specialist` | `medical-device-regulatory-strategy` | inferred |
| `eu-regulatory-investigations.json` | `eu-mdr-ivdr-regulatory-specialist` | `medical-device-regulatory-strategy` | inferred |
| `eudamed-readiness.json` | `eudamed-udi-ivd` | — | unconsumed |
| `euroimmun-report.docx` | `euroimmun-docx-report-renderer` | `euroimmun-pdf-report-renderer` | inferred |
| `euroimmun-report.pdf` | `euroimmun-pdf-report-renderer` | — | unconsumed |
| `evaluation evidence` | `composable-skill-factory` | `central-skill-repository-curation` | inferred |
| `evidence-note.json` | `research-to-evidence-note` | `clinical-evidence-update-impact`, `contract-legal-context`, `eu-mdr-ivdr-regulatory-specialist`, `evidence-based-causal-investigation`, `fda-510k-predicate-strategy`, `fda-device-classification-product-code`, `fda-medical-device-ivd-regulatory-specialist`, `freedom-to-operate-assessment`, `ivdr-scientific-validity`, `mdcg-guidance-navigator`, `medical-device-privacy-gdpr-bdsg`, `medical-device-risk-management-iso14971`, `meeting-preparation`, `patent-landscape-analysis`, `product-evidence-research`, `regulatory-change-monitoring`, `regulatory-evidence-traceability`, `teach`, `technology-offer-assessment`, `two-axis-compliance-review` | inferred |
| `evidence-note.md` | `research-to-evidence-note` | `clinical-evidence-update-impact`, `contract-legal-context`, `eu-mdr-ivdr-regulatory-specialist`, `evidence-based-causal-investigation`, `fda-510k-predicate-strategy`, `fda-device-classification-product-code`, `fda-medical-device-ivd-regulatory-specialist`, `freedom-to-operate-assessment`, `ivdr-scientific-validity`, `mdcg-guidance-navigator`, `medical-device-privacy-gdpr-bdsg`, `medical-device-risk-management-iso14971`, `meeting-preparation`, `patent-landscape-analysis`, `product-evidence-research`, `regulatory-change-monitoring`, `regulatory-evidence-traceability`, `teach`, `technology-offer-assessment`, `two-axis-compliance-review` | inferred |
| `execution plan` | `synapse-orchestrator` | — | unconsumed |
| `executive-search-brief.md` | `job-description-authoring` | — | unconsumed |
| `expert handoff` | `synapse-orchestrator` | — | unconsumed |
| `fda-acceptance-preflight.json` | `fda-acceptance-readiness` | — | unconsumed |
| `fda-device-classification.json` | `fda-device-classification-product-code` | `fda-510k-predicate-strategy`, `fda-de-novo-strategy`, `fda-ivd-clia-waiver` | inferred |
| `fda-device-listing-readiness.json` | `fda-registration-listing-udi` | — | unconsumed |
| `fda-product-code-evidence.json` | `fda-device-classification-product-code` | `fda-510k-predicate-strategy`, `fda-de-novo-strategy`, `fda-ivd-clia-waiver` | inferred |
| `fda-recall-authority-state.json` | `fda-recall-status-termination` | — | unconsumed |
| `fda-recall-status-report.json` | `fda-recall-status-termination` | — | unconsumed |
| `fda-recall-termination-request.json` | `fda-recall-status-termination` | — | unconsumed |
| `fda-registration-readiness.json` | `fda-registration-listing-udi` | — | unconsumed |
| `fda-regulatory-assessment.json` | `fda-medical-device-ivd-regulatory-specialist` | `fda-estar-submission-builder`, `fda-qsub-strategy`, `medical-device-regulatory-strategy` | inferred |
| `fda-regulatory-assessment.md` | `fda-medical-device-ivd-regulatory-specialist` | `fda-estar-submission-builder`, `fda-qsub-strategy`, `medical-device-regulatory-strategy` | inferred |
| `fda-regulatory-investigations.json` | `fda-medical-device-ivd-regulatory-specialist` | `fda-estar-submission-builder`, `fda-qsub-strategy`, `medical-device-regulatory-strategy` | inferred |
| `fda-request-issue-map.json` | `fda-additional-information-response` | — | unconsumed |
| `fda-response-package.md` | `fda-additional-information-response` | — | unconsumed |
| `fidelity-review.md` | `rewrite-fidelity-verifier` | `precision-writing-revision` | inferred |
| `field-action-closure-readiness.json` | `medical-device-field-action-effectiveness` | `fda-recall-status-termination`, `ivdr-fsca-status-final-reporting` | inferred |
| `field-action-communication-state.json` | `medical-device-field-action-communication` | `medical-device-field-action-effectiveness`, `medical-device-field-action-physical-execution` | inferred |
| `field-action-disposition-evidence.json` | `medical-device-field-action-physical-execution` | `medical-device-field-action-effectiveness` | inferred |
| `field-action-effectiveness-assessment.json` | `medical-device-field-action-effectiveness` | `fda-recall-status-termination`, `ivdr-fsca-status-final-reporting` | inferred |
| `field-action-notice-package.json` | `medical-device-field-action-communication` | `medical-device-field-action-effectiveness`, `medical-device-field-action-physical-execution` | inferred |
| `field-action-physical-execution-plan.json` | `medical-device-field-action-physical-execution` | `medical-device-field-action-effectiveness` | inferred |
| `field-action-product-reconciliation.json` | `medical-device-field-action-effectiveness` | `fda-recall-status-termination`, `ivdr-fsca-status-final-reporting` | inferred |
| `field-action-recipient-scope.json` | `medical-device-field-action-communication` | `medical-device-field-action-effectiveness`, `medical-device-field-action-physical-execution` | inferred |
| `field-action-unit-custody-ledger.json` | `medical-device-field-action-physical-execution` | `medical-device-field-action-effectiveness` | inferred |
| `field-safety-notice-content.json` | `ivdr-field-safety-corrective-action` | `ivdr-fsca-status-final-reporting` | inferred |
| `final-revised-text` | `precision-writing-revision` | — | unconsumed |
| `finding-action-plan.json` | `audit-inspection-finding-response` | — | unconsumed |
| `finding-closure-status.json` | `audit-inspection-finding-response` | — | unconsumed |
| `flex-study-needs.json` | `fda-ivd-clia-waiver` | `fda-dual-510k-clia-waiver` | inferred |
| `frontend-design-brief.md` | `frontend-design-shaping` | `frontend-design-director` | inferred |
| `frontend-design-findings.json` | `frontend-design-review` | `frontend-design-director` | inferred |
| `frontend-design-handoff.md` | `frontend-design-director` | — | unconsumed |
| `frontend-design-review.md` | `frontend-design-review` | `frontend-design-director` | inferred |
| `frontend-design-routing.json` | `frontend-design-director` | — | unconsumed |
| `frontend-design-system-context-handoff.json` | `frontend-design-system-context` | `frontend-design-director`, `frontend-design-review`, `frontend-design-shaping` | inferred |
| `frontend-product-context-handoff.json` | `frontend-product-context` | `frontend-design-director`, `frontend-design-review`, `frontend-design-shaping`, `frontend-design-system-context` | inferred |
| `frontend-shaping-handoff.json` | `frontend-design-shaping` | `frontend-design-director` | inferred |
| `fto-claim-map.json` | `freedom-to-operate-assessment` | — | unconsumed |
| `fto-design-around-options.json` | `freedom-to-operate-assessment` | — | unconsumed |
| `fto-risk-heatmap.md` | `freedom-to-operate-assessment` | — | unconsumed |
| `fto-scope.json` | `freedom-to-operate-assessment` | — | unconsumed |
| `gudid-udi-readiness.json` | `fda-registration-listing-udi` | — | unconsumed |
| `human-procedure-plan.md` | `human-procedure-wizard` | — | unconsumed |
| `human-procedure-result.json` | `human-procedure-wizard` | — | unconsumed |
| `ifu-content-structure.md` | `medical-device-labeling-ifu` | `eudamed-udi-ivd`, `fda-registration-listing-udi`, `iec62366-usability-engineering`, `regulatory-claims-consistency` | inferred |
| `implementation-evidence.json` | `implement-from-issue` | `two-axis-code-review` | inferred |
| `implementation-residual-risk-handoff.json` | `implement-from-issue` | `two-axis-code-review` | inferred |
| `import verification` | `openasr-offline-model-import` | — | unconsumed |
| `inbox-triage.json` | `inbox-action-triage` | `daily-and-weekly-review` | inferred |
| `inbox-triage.md` | `inbox-action-triage` | `daily-and-weekly-review` | inferred |
| `inhouse-ivd-condition-map.json` | `ivdr-inhouse-health-institution` | — | unconsumed |
| `inhouse-ivd-eligibility.json` | `ivdr-inhouse-health-institution` | — | unconsumed |
| `inhouse-ivd-transition-readiness.json` | `ivdr-inhouse-health-institution` | — | unconsumed |
| `inspection-evidence-index.json` | `fda-qmsr-inspection-readiness` | — | unconsumed |
| `installed OpenASR model` | `openasr-offline-model-import` | — | unconsumed |
| `investigation-backlog.json` | `large-work-wayfinder` | `decision-record`, `frontend-design-shaping`, `medical-device-regulatory-strategy`, `throwaway-prototype` | inferred |
| `isms-audit-findings.json` | `iso27001-isms-audit` | — | unconsumed |
| `isms-audit-plan.json` | `iso27001-isms-audit` | — | unconsumed |
| `isms-audit-report.md` | `iso27001-isms-audit` | — | unconsumed |
| `isms-governance-assessment.json` | `medical-device-isms-governance` | `iso27001-isms-audit` | inferred |
| `isms-governance.md` | `medical-device-isms-governance` | `iso27001-isms-audit` | inferred |
| `isms-risk-treatment-context.json` | `medical-device-isms-governance` | `iso27001-isms-audit` | inferred |
| `ivd-udi-data-set.json` | `eudamed-udi-ivd` | — | unconsumed |
| `ivdr-authority-state.json` | `ivdr-fsca-status-final-reporting` | — | unconsumed |
| `ivdr-classification-assessment.json` | `ivdr-device-classification` | `eudamed-udi-ivd`, `ivdr-class-d-conformity`, `ivdr-companion-diagnostic-consultation` | inferred |
| `ivdr-classification-rationale.md` | `ivdr-device-classification` | `eudamed-udi-ivd`, `ivdr-class-d-conformity`, `ivdr-companion-diagnostic-consultation` | inferred |
| `ivdr-economic-operator-escalation-log.json` | `ivdr-economic-operator-postmarket-propagation` | — | unconsumed |
| `ivdr-economic-operator-obligation-map.json` | `ivdr-economic-operator-postmarket-propagation` | — | unconsumed |
| `ivdr-economic-operator-propagation-state.json` | `ivdr-economic-operator-postmarket-propagation` | — | unconsumed |
| `ivdr-fsca-assessment.json` | `ivdr-field-safety-corrective-action` | `ivdr-fsca-status-final-reporting` | inferred |
| `ivdr-fsca-authority-followup.json` | `ivdr-fsca-status-final-reporting` | — | unconsumed |
| `ivdr-fsca-regulatory-plan.json` | `ivdr-field-safety-corrective-action` | `ivdr-fsca-status-final-reporting` | inferred |
| `ivdr-performance-evaluation-gaps.json` | `ivdr-performance-evaluation` | `ivdr-class-d-conformity`, `ivdr-companion-diagnostic-consultation`, `ivdr-performance-evaluation-report`, `ivdr-pmpf` | inferred |
| `ivdr-performance-evaluation.json` | `ivdr-performance-evaluation` | `ivdr-class-d-conformity`, `ivdr-companion-diagnostic-consultation`, `ivdr-performance-evaluation-report`, `ivdr-pmpf` | inferred |
| `ivdr-pms-assessment.json` | `ivdr-pms-vigilance` | `ivdr-field-safety-corrective-action`, `medical-device-complaint-regulatory-routing` | inferred |
| `ivdr-vigilance-final-report-package.json` | `ivdr-fsca-status-final-reporting` | — | unconsumed |
| `job-description.md` | `job-description-authoring` | — | unconsumed |
| `knowledge-artifact.json` | `structured-knowledge-artifact` | `knowledge-map-generator`, `knowledge-view`, `obsidian-adapter` | inferred |
| `knowledge-artifact.md` | `structured-knowledge-artifact` | `knowledge-map-generator`, `knowledge-view`, `obsidian-adapter` | inferred |
| `knowledge-map.json` | `knowledge-map-generator` | `obsidian-adapter` | inferred |
| `knowledge-view.json` | `knowledge-view` | `obsidian-adapter` | inferred |
| `labeling-content-map.json` | `medical-device-labeling-ifu` | `eudamed-udi-ivd`, `fda-registration-listing-udi`, `iec62366-usability-engineering`, `regulatory-claims-consistency` | inferred |
| `labeling-evidence-gaps.json` | `medical-device-labeling-ifu` | `eudamed-udi-ivd`, `fda-registration-listing-udi`, `iec62366-usability-engineering`, `regulatory-claims-consistency` | inferred |
| `learning-assessment-spec.json` | `learning-assessment-spec` | `exam-trainer-catalog-builder`, `learning-assessment`, `teach` | inferred |
| `learning-assessment.json` | `learning-assessment` | `teach` | inferred |
| `learning-mission.json` | `learning-mission`, `teach` | — | ambiguous |
| `learning-next-step.json` | `learning-next-step`, `teach` | — | ambiguous |
| `learning-practice-request.json` | `teach` | — | unconsumed |
| `learning-record.md` | `learning-state` | `learning-assessment-spec`, `learning-next-step`, `teach` | inferred |
| `learning-runtime-evidence.json` | `exam-trainer-result-import` | `teach` | inferred |
| `learning-state.json` | `learning-state`, `teach` | — | ambiguous |
| `lifecycle-impact-gates.json` | `regulatory-change-impact-orchestrator` | — | unconsumed |
| `management-review-actions.json` | `qms-management-review-governance` | `qms-management-review-action-followup` | inferred |
| `management-review-brief.json` | `qms-management-review-governance` | `qms-management-review-action-followup` | inferred |
| `management-review-brief.md` | `qms-management-review-governance` | `qms-management-review-action-followup` | inferred |
| `management-review-effectiveness-gaps.json` | `qms-management-review-action-followup` | — | unconsumed |
| `management-review-follow-up-status.json` | `qms-management-review-action-followup` | — | unconsumed |
| `management-review-return-input.json` | `qms-management-review-action-followup` | — | unconsumed |
| `mdcg-guidance-changes.json` | `mdcg-guidance-navigator` | `ivdr-class-d-conformity`, `ivdr-clinical-performance-study`, `ivdr-device-classification`, `ivdr-field-safety-corrective-action`, `ivdr-fsca-status-final-reporting`, `ivdr-performance-evaluation-report`, `ivdr-pmpf`, `ivdr-pms-vigilance` | inferred |
| `mdcg-guidance-set.json` | `mdcg-guidance-navigator` | `ivdr-class-d-conformity`, `ivdr-clinical-performance-study`, `ivdr-device-classification`, `ivdr-field-safety-corrective-action`, `ivdr-fsca-status-final-reporting`, `ivdr-performance-evaluation-report`, `ivdr-pmpf`, `ivdr-pms-vigilance` | inferred |
| `mdr-reportability-assessment.json` | `fda-complaint-mdr-reportability` | `fda-corrections-removals`, `medical-device-complaint-regulatory-routing` | inferred |
| `mdsap-audit-scope.json` | `mdsap-audit-readiness` | — | unconsumed |
| `mdsap-evidence-gaps.json` | `mdsap-audit-readiness` | — | unconsumed |
| `mdsap-task-readiness.json` | `mdsap-audit-readiness` | — | unconsumed |
| `measurement-capability-study.json` | `measurement-system-validation` | — | unconsumed |
| `measurement-evidence-gaps.json` | `measurement-system-validation` | — | unconsumed |
| `measurement-system-assessment.json` | `measurement-system-validation` | — | unconsumed |
| `meeting-prep.json` | `meeting-preparation` | `decision-and-follow-up-tracker` | inferred |
| `meeting-prep.md` | `meeting-preparation` | `decision-and-follow-up-tracker` | inferred |
| `memory-ledger.json` | `communication-memory-governance` | `frontend-design-director`, `memory-sync-reconciliation` | inferred |
| `memory-ledger.merged.json` | `memory-sync-reconciliation` | — | unconsumed |
| `memory-reconciliation-plan.json` | `memory-sync-reconciliation` | — | unconsumed |
| `mental-health-routing.json` | `sport-mental-health-routing` | `sport-athlete-management` | inferred |
| `mrb-disposition-decision.json` | `nonconformance-mrb-disposition` | — | unconsumed |
| `next increment` | `iterate-software-projects` | `agent-handoff`, `architecture-deepening-review`, `disciplined-diagnosis`, `project-beta-readiness` | inferred |
| `next-step-handoff.json` | `architecture-deepening-review` | `domain-model-maintenance`, `large-work-wayfinder`, `two-axis-code-review` | inferred |
| `next-training-decision.json` | `sport-athlete-management` | — | unconsumed |
| `nonconformance-assessment.json` | `nonconformance-mrb-disposition` | — | unconsumed |
| `obsidian-candidate.json` | `obsidian-adapter` | — | unconsumed |
| `obsidian-map.canvas` | `obsidian-adapter` | — | unconsumed |
| `obsidian-note.md` | `obsidian-adapter` | — | unconsumed |
| `obsidian-view.base` | `obsidian-adapter` | — | unconsumed |
| `opaque-analysis-evidence.md` | `opaque-system-analysis` | — | unconsumed |
| `patent-landscape.json` | `patent-landscape-analysis` | — | unconsumed |
| `patent-landscape.md` | `patent-landscape-analysis` | — | unconsumed |
| `patent-search-log.json` | `patent-landscape-analysis` | — | unconsumed |
| `pccp-applicability.json` | `fda-pccp-change-control` | — | unconsumed |
| `pccp-change-evidence.json` | `fda-pccp-change-control` | — | unconsumed |
| `pccp-deviation-routing.json` | `fda-pccp-change-control` | — | unconsumed |
| `per-traceability.json` | `ivdr-performance-evaluation-report` | — | unconsumed |
| `performance-evaluation-report.md` | `ivdr-performance-evaluation-report` | — | unconsumed |
| `performance-psychology-plan.json` | `sport-performance-psychology` | `sport-athlete-management` | inferred |
| `performance-study-gaps.json` | `ivdr-clinical-performance-study` | `ivdr-performance-evaluation` | inferred |
| `plan-revision.json` | `sport-athlete-management` | — | unconsumed |
| `pmpf-evaluation-report.md` | `ivdr-pmpf` | — | unconsumed |
| `pmpf-plan.json` | `ivdr-pmpf` | — | unconsumed |
| `pmpf-signals.json` | `ivdr-pmpf` | — | unconsumed |
| `pms-management-review-input.json` | `medical-device-pms-system` | `ivdr-pms-vigilance`, `medical-device-field-action-effectiveness`, `qms-management-review-governance` | inferred |
| `pms-review-status.json` | `medical-device-pms-system` | `ivdr-pms-vigilance`, `medical-device-field-action-effectiveness`, `qms-management-review-governance` | inferred |
| `pms-source-register.json` | `medical-device-pms-system` | `ivdr-pms-vigilance`, `medical-device-field-action-effectiveness`, `qms-management-review-governance` | inferred |
| `pms-system-plan.json` | `medical-device-pms-system` | `ivdr-pms-vigilance`, `medical-device-field-action-effectiveness`, `qms-management-review-governance` | inferred |
| `precision-writing-report.json` | `precision-writing-revision` | — | unconsumed |
| `predicate-candidate-set.json` | `fda-510k-predicate-strategy` | `fda-510k-substantial-equivalence` | inferred |
| `predicate-strategy.md` | `fda-510k-predicate-strategy` | `fda-510k-substantial-equivalence` | inferred |
| `price-snapshot.json` | `price-availability-snapshot` | `purchase-decision-planner` | inferred |
| `price-snapshot.md` | `price-availability-snapshot` | `purchase-decision-planner` | inferred |
| `privacy-assessment.json` | `medical-device-privacy-gdpr-bdsg` | — | unconsumed |
| `privacy-governance.md` | `medical-device-privacy-gdpr-bdsg` | — | unconsumed |
| `process-validation-assessment.json` | `process-validation-iq-oq-pq` | — | unconsumed |
| `process-validation-protocol.md` | `process-validation-iq-oq-pq` | — | unconsumed |
| `process-validation-strategy.json` | `process-validation-iq-oq-pq` | — | unconsumed |
| `product-evidence-set.json` | `product-evidence-research` | `purchase-decision-planner` | inferred |
| `product-evidence-set.md` | `product-evidence-research` | `purchase-decision-planner` | inferred |
| `product-ranking.json` | `product-comparison-ranking` | `purchase-decision-planner` | inferred |
| `product-ranking.md` | `product-comparison-ranking` | `purchase-decision-planner` | inferred |
| `progress summary` | `synapse-orchestrator` | — | unconsumed |
| `project-status.json` | `project-status-brief` | `decision-and-follow-up-tracker`, `qms-management-review-governance` | inferred |
| `project-status.md` | `project-status-brief` | `decision-and-follow-up-tracker`, `qms-management-review-governance` | inferred |
| `prose-audit.json` | `llm-prose-pattern-audit` | `precision-writing-revision` | inferred |
| `prose-audit.md` | `llm-prose-pattern-audit` | `precision-writing-revision` | inferred |
| `prototype-brief.md` | `throwaway-prototype` | `decision-record` | inferred |
| `prototype-evidence.json` | `throwaway-prototype` | `decision-record` | inferred |
| `public-job-posting.md` | `job-description-authoring` | — | unconsumed |
| `pull request` | `composable-skill-factory` | `central-skill-repository-curation` | inferred |
| `purchase-plan.json` | `purchase-decision-planner` | — | unconsumed |
| `purchase-plan.md` | `purchase-decision-planner` | — | unconsumed |
| `purchase-shortlist.json` | `purchase-decision-planner` | — | unconsumed |
| `qms-audit-findings.json` | `iso13485-qms-audit` | `fda-qmsr-inspection-readiness`, `mdsap-audit-readiness`, `qms-management-review-governance` | inferred |
| `qms-audit-plan.json` | `iso13485-qms-audit` | `fda-qmsr-inspection-readiness`, `mdsap-audit-readiness`, `qms-management-review-governance` | inferred |
| `qms-audit-report.md` | `iso13485-qms-audit` | `fda-qmsr-inspection-readiness`, `mdsap-audit-readiness`, `qms-management-review-governance` | inferred |
| `qms-gap-analysis.json` | `medical-device-qms-iso13485` | `fda-medical-device-ivd-regulatory-specialist`, `fda-qmsr-iso13485-gap`, `iec62304-software-lifecycle`, `iso13485-qms-audit`, `ivdr-inhouse-health-institution`, `mdsap-audit-readiness`, `measurement-system-validation`, `medical-device-capa`, `nonconformance-mrb-disposition`, `process-validation-iq-oq-pq`, `qms-management-review-governance`, `quality-record-integrity`, `supplier-quality-medical-device` | inferred |
| `qms-process-map.json` | `medical-device-qms-iso13485` | `fda-medical-device-ivd-regulatory-specialist`, `fda-qmsr-iso13485-gap`, `iec62304-software-lifecycle`, `iso13485-qms-audit`, `ivdr-inhouse-health-institution`, `mdsap-audit-readiness`, `measurement-system-validation`, `medical-device-capa`, `nonconformance-mrb-disposition`, `process-validation-iq-oq-pq`, `qms-management-review-governance`, `quality-record-integrity`, `supplier-quality-medical-device` | inferred |
| `qms-readiness.md` | `medical-device-qms-iso13485` | `fda-medical-device-ivd-regulatory-specialist`, `fda-qmsr-iso13485-gap`, `iec62304-software-lifecycle`, `iso13485-qms-audit`, `ivdr-inhouse-health-institution`, `mdsap-audit-readiness`, `measurement-system-validation`, `medical-device-capa`, `nonconformance-mrb-disposition`, `process-validation-iq-oq-pq`, `qms-management-review-governance`, `quality-record-integrity`, `supplier-quality-medical-device` | inferred |
| `qmsr-gap-assessment.md` | `fda-qmsr-iso13485-gap` | `fda-qmsr-inspection-readiness` | inferred |
| `qmsr-inspection-readiness.json` | `fda-qmsr-inspection-readiness` | — | unconsumed |
| `qmsr-iso13485-delta.json` | `fda-qmsr-iso13485-gap` | `fda-qmsr-inspection-readiness` | inferred |
| `qsub-briefing-package.md` | `fda-qsub-strategy` | — | unconsumed |
| `qsub-commitments.json` | `fda-qsub-strategy` | — | unconsumed |
| `qsub-question-set.json` | `fda-qsub-strategy` | — | unconsumed |
| `quality-record-integrity-assessment.json` | `quality-record-integrity` | `fda-complaint-mdr-reportability`, `fda-recall-status-termination`, `ivdr-economic-operator-postmarket-propagation`, `medical-device-complaint-customer-followup`, `medical-device-complaint-handling`, `medical-device-customer-contact-intake`, `medical-device-field-action-communication`, `medical-device-field-action-effectiveness`, `medical-device-field-action-physical-execution`, `medical-device-service-report-quality-routing` | inferred |
| `quality-review.json` | `two-axis-code-review` | `decision-record`, `domain-model-maintenance`, `engineering-delivery-followup`, `merge-conflict-resolution` | inferred |
| `record-integrity-gaps.json` | `quality-record-integrity` | `fda-complaint-mdr-reportability`, `fda-recall-status-termination`, `ivdr-economic-operator-postmarket-propagation`, `medical-device-complaint-customer-followup`, `medical-device-complaint-handling`, `medical-device-customer-contact-intake`, `medical-device-field-action-communication`, `medical-device-field-action-effectiveness`, `medical-device-field-action-physical-execution`, `medical-device-service-report-quality-routing` | inferred |
| `record-retrieval-index.json` | `quality-record-integrity` | `fda-complaint-mdr-reportability`, `fda-recall-status-termination`, `ivdr-economic-operator-postmarket-propagation`, `medical-device-complaint-customer-followup`, `medical-device-complaint-handling`, `medical-device-customer-contact-intake`, `medical-device-field-action-communication`, `medical-device-field-action-effectiveness`, `medical-device-field-action-physical-execution`, `medical-device-service-report-quality-routing` | inferred |
| `recovered-system-model.json` | `opaque-system-analysis` | — | unconsumed |
| `recovery-state.json` | `sport-recovery-sleep` | `sport-athlete-management`, `sport-environment-travel` | inferred |
| `regulated-product-context.json` | `regulated-product-context` | `clinical-evidence-update-impact`, `controlled-quality-documentation`, `design-control-traceability`, `eu-mdr-ivdr-regulatory-specialist`, `eudamed-udi-ivd`, `fda-510k-predicate-strategy`, `fda-complaint-mdr-reportability`, `fda-de-novo-strategy`, `fda-device-classification-product-code`, `fda-ivd-clia-waiver`, `fda-medical-device-ivd-regulatory-specialist`, `fda-registration-listing-udi`, `iec62304-software-lifecycle`, `iec62366-usability-engineering`, `ivdr-analytical-performance`, `ivdr-clinical-performance-study`, `ivdr-companion-diagnostic-consultation`, `ivdr-device-classification`, `ivdr-economic-operator-postmarket-propagation`, `ivdr-inhouse-health-institution`, `ivdr-pms-vigilance`, `ivdr-scientific-validity`, `mdcg-guidance-navigator`, `medical-device-complaint-customer-followup`, `medical-device-complaint-handling`, `medical-device-complaint-regulatory-routing`, `medical-device-cybersecurity-lifecycle`, `medical-device-field-action-communication`, `medical-device-isms-governance`, `medical-device-labeling-ifu`, `medical-device-pms-system`, `medical-device-privacy-gdpr-bdsg`, `medical-device-qms-iso13485`, `medical-device-regulatory-strategy`, `medical-device-risk-management-iso14971`, `regulatory-change-impact-orchestrator`, `regulatory-claims-consistency`, `regulatory-evidence-traceability` | inferred |
| `regulated-product-context.md` | `regulated-product-context` | `clinical-evidence-update-impact`, `controlled-quality-documentation`, `design-control-traceability`, `eu-mdr-ivdr-regulatory-specialist`, `eudamed-udi-ivd`, `fda-510k-predicate-strategy`, `fda-complaint-mdr-reportability`, `fda-de-novo-strategy`, `fda-device-classification-product-code`, `fda-ivd-clia-waiver`, `fda-medical-device-ivd-regulatory-specialist`, `fda-registration-listing-udi`, `iec62304-software-lifecycle`, `iec62366-usability-engineering`, `ivdr-analytical-performance`, `ivdr-clinical-performance-study`, `ivdr-companion-diagnostic-consultation`, `ivdr-device-classification`, `ivdr-economic-operator-postmarket-propagation`, `ivdr-inhouse-health-institution`, `ivdr-pms-vigilance`, `ivdr-scientific-validity`, `mdcg-guidance-navigator`, `medical-device-complaint-customer-followup`, `medical-device-complaint-handling`, `medical-device-complaint-regulatory-routing`, `medical-device-cybersecurity-lifecycle`, `medical-device-field-action-communication`, `medical-device-isms-governance`, `medical-device-labeling-ifu`, `medical-device-pms-system`, `medical-device-privacy-gdpr-bdsg`, `medical-device-qms-iso13485`, `medical-device-regulatory-strategy`, `medical-device-risk-management-iso14971`, `regulatory-change-impact-orchestrator`, `regulatory-claims-consistency`, `regulatory-evidence-traceability` | inferred |
| `regulatory-awareness-timeline.json` | `medical-device-complaint-regulatory-routing` | — | unconsumed |
| `regulatory-change-decisions.json` | `design-change-regulatory-impact` | `fda-pccp-change-control` | inferred |
| `regulatory-change-events.json` | `regulatory-change-monitoring` | — | unconsumed |
| `regulatory-change-route-map.json` | `regulatory-change-impact-orchestrator` | — | unconsumed |
| `regulatory-change-watch-status.json` | `regulatory-change-monitoring` | — | unconsumed |
| `regulatory-evidence-gaps.json` | `regulatory-evidence-traceability` | `audit-inspection-finding-response`, `clinical-evidence-update-impact`, `design-change-regulatory-impact`, `eudamed-udi-ivd`, `fda-510k-predicate-strategy`, `fda-510k-substantial-equivalence`, `fda-acceptance-readiness`, `fda-additional-information-response`, `fda-complaint-mdr-reportability`, `fda-de-novo-special-controls`, `fda-de-novo-strategy`, `fda-device-classification-product-code`, `fda-dual-510k-clia-waiver`, `fda-estar-submission-builder`, `fda-ivd-clia-waiver`, `fda-pccp-change-control`, `fda-qmsr-iso13485-gap`, `fda-qsub-strategy`, `fda-recall-status-termination`, `fda-registration-listing-udi`, `ivdr-analytical-performance`, `ivdr-class-d-conformity`, `ivdr-clinical-performance-study`, `ivdr-companion-diagnostic-consultation`, `ivdr-device-classification`, `ivdr-economic-operator-postmarket-propagation`, `ivdr-field-safety-corrective-action`, `ivdr-fsca-status-final-reporting`, `ivdr-inhouse-health-institution`, `ivdr-performance-evaluation`, `ivdr-performance-evaluation-report`, `ivdr-pmpf`, `ivdr-pms-vigilance`, `ivdr-scientific-validity`, `mdcg-guidance-navigator`, `mdsap-audit-readiness`, `medical-device-adverse-event-coding`, `medical-device-complaint-regulatory-routing`, `medical-device-labeling-ifu`, `medical-device-pms-system`, `regulatory-change-impact-orchestrator`, `regulatory-change-monitoring`, `regulatory-claims-consistency` | inferred |
| `regulatory-evidence-map.json` | `regulatory-evidence-traceability` | `audit-inspection-finding-response`, `clinical-evidence-update-impact`, `design-change-regulatory-impact`, `eudamed-udi-ivd`, `fda-510k-predicate-strategy`, `fda-510k-substantial-equivalence`, `fda-acceptance-readiness`, `fda-additional-information-response`, `fda-complaint-mdr-reportability`, `fda-de-novo-special-controls`, `fda-de-novo-strategy`, `fda-device-classification-product-code`, `fda-dual-510k-clia-waiver`, `fda-estar-submission-builder`, `fda-ivd-clia-waiver`, `fda-pccp-change-control`, `fda-qmsr-iso13485-gap`, `fda-qsub-strategy`, `fda-recall-status-termination`, `fda-registration-listing-udi`, `ivdr-analytical-performance`, `ivdr-class-d-conformity`, `ivdr-clinical-performance-study`, `ivdr-companion-diagnostic-consultation`, `ivdr-device-classification`, `ivdr-economic-operator-postmarket-propagation`, `ivdr-field-safety-corrective-action`, `ivdr-fsca-status-final-reporting`, `ivdr-inhouse-health-institution`, `ivdr-performance-evaluation`, `ivdr-performance-evaluation-report`, `ivdr-pmpf`, `ivdr-pms-vigilance`, `ivdr-scientific-validity`, `mdcg-guidance-navigator`, `mdsap-audit-readiness`, `medical-device-adverse-event-coding`, `medical-device-complaint-regulatory-routing`, `medical-device-labeling-ifu`, `medical-device-pms-system`, `regulatory-change-impact-orchestrator`, `regulatory-change-monitoring`, `regulatory-claims-consistency` | inferred |
| `regulatory-source-register.json` | `regulatory-change-monitoring` | — | unconsumed |
| `regulatory-strategy.json` | `medical-device-regulatory-strategy` | — | unconsumed |
| `regulatory-strategy.md` | `medical-device-regulatory-strategy` | — | unconsumed |
| `regulatory-wayfinding-handoff.json` | `medical-device-regulatory-strategy` | — | unconsumed |
| `rehab-progression.json` | `sport-injury-rehabilitation` | `sport-athlete-management` | inferred |
| `remaining-unknowns.json` | `opaque-system-analysis` | — | unconsumed |
| `requirement-coverage.json` | `two-axis-code-review` | `decision-record`, `domain-model-maintenance`, `engineering-delivery-followup`, `merge-conflict-resolution` | inferred |
| `requirements-handoff.json` | `round-based-requirements-grilling` | `contract-workflow`, `frontend-design-shaping`, `frontend-design-system-context`, `frontend-product-context`, `role-requirements-grilling` | inferred |
| `resolved-change-brief.md` | `merge-conflict-resolution` | — | unconsumed |
| `response-evidence-matrix.json` | `fda-additional-information-response` | — | unconsumed |
| `return-after-illness-plan.json` | `sport-return-after-illness` | `sport-athlete-management` | inferred |
| `review findings` | `iterate-software-projects` | `agent-handoff`, `architecture-deepening-review`, `disciplined-diagnosis`, `project-beta-readiness` | inferred |
| `review-brief.json` | `daily-and-weekly-review` | `decision-and-follow-up-tracker` | inferred |
| `review-brief.md` | `daily-and-weekly-review` | `decision-and-follow-up-tracker` | inferred |
| `review-decision.md` | `two-axis-code-review` | `decision-record`, `domain-model-maintenance`, `engineering-delivery-followup`, `merge-conflict-resolution` | inferred |
| `reviewable-change-brief.md` | `implement-from-issue` | `two-axis-code-review` | inferred |
| `revised-text` | `precision-language-rewriter` | `precision-writing-revision` | inferred |
| `rewrite-change-map.json` | `precision-language-rewriter` | `precision-writing-revision` | inferred |
| `rewrite-fidelity.json` | `rewrite-fidelity-verifier` | `precision-writing-revision` | inferred |
| `risk-management-analysis.json` | `medical-device-risk-management-iso14971` | `design-change-regulatory-impact`, `design-control-traceability`, `eu-mdr-ivdr-regulatory-specialist`, `fda-510k-substantial-equivalence`, `fda-complaint-mdr-reportability`, `fda-corrections-removals`, `fda-de-novo-special-controls`, `fda-de-novo-strategy`, `fda-ivd-clia-waiver`, `fda-pccp-change-control`, `iec62304-software-lifecycle`, `iec62366-usability-engineering`, `ivdr-analytical-performance`, `ivdr-clinical-performance-study`, `ivdr-field-safety-corrective-action`, `ivdr-inhouse-health-institution`, `ivdr-pmpf`, `ivdr-pms-vigilance`, `measurement-system-validation`, `medical-device-capa`, `medical-device-cybersecurity-lifecycle`, `medical-device-field-action-effectiveness`, `medical-device-labeling-ifu`, `medical-device-pms-system`, `medical-device-regulatory-strategy`, `nonconformance-mrb-disposition`, `process-validation-iq-oq-pq`, `supplier-quality-medical-device` | inferred |
| `risk-management-analysis.md` | `medical-device-risk-management-iso14971` | `design-change-regulatory-impact`, `design-control-traceability`, `eu-mdr-ivdr-regulatory-specialist`, `fda-510k-substantial-equivalence`, `fda-complaint-mdr-reportability`, `fda-corrections-removals`, `fda-de-novo-special-controls`, `fda-de-novo-strategy`, `fda-ivd-clia-waiver`, `fda-pccp-change-control`, `iec62304-software-lifecycle`, `iec62366-usability-engineering`, `ivdr-analytical-performance`, `ivdr-clinical-performance-study`, `ivdr-field-safety-corrective-action`, `ivdr-inhouse-health-institution`, `ivdr-pmpf`, `ivdr-pms-vigilance`, `measurement-system-validation`, `medical-device-capa`, `medical-device-cybersecurity-lifecycle`, `medical-device-field-action-effectiveness`, `medical-device-labeling-ifu`, `medical-device-pms-system`, `medical-device-regulatory-strategy`, `nonconformance-mrb-disposition`, `process-validation-iq-oq-pq`, `supplier-quality-medical-device` | inferred |
| `risk-wayfinding-handoff.json` | `medical-device-risk-management-iso14971` | `design-change-regulatory-impact`, `design-control-traceability`, `eu-mdr-ivdr-regulatory-specialist`, `fda-510k-substantial-equivalence`, `fda-complaint-mdr-reportability`, `fda-corrections-removals`, `fda-de-novo-special-controls`, `fda-de-novo-strategy`, `fda-ivd-clia-waiver`, `fda-pccp-change-control`, `iec62304-software-lifecycle`, `iec62366-usability-engineering`, `ivdr-analytical-performance`, `ivdr-clinical-performance-study`, `ivdr-field-safety-corrective-action`, `ivdr-inhouse-health-institution`, `ivdr-pmpf`, `ivdr-pms-vigilance`, `measurement-system-validation`, `medical-device-capa`, `medical-device-cybersecurity-lifecycle`, `medical-device-field-action-effectiveness`, `medical-device-labeling-ifu`, `medical-device-pms-system`, `medical-device-regulatory-strategy`, `nonconformance-mrb-disposition`, `process-validation-iq-oq-pq`, `supplier-quality-medical-device` | inferred |
| `role-architecture.json` | `role-architecture` | `candidate-role-fit-assessment`, `job-description-authoring` | explicit |
| `role-architecture.md` | `role-architecture` | — | unconsumed |
| `role-requirements-handoff.json` | `role-requirements-grilling` | `role-architecture` | explicit |
| `role-requirements-report.md` | `role-requirements-grilling` | — | unconsumed |
| `role-scorecard.json` | `role-architecture` | `candidate-role-fit-assessment`, `job-description-authoring` | explicit |
| `scientific-validity-assessment.json` | `ivdr-scientific-validity` | `ivdr-performance-evaluation` | inferred |
| `scientific-validity-report.md` | `ivdr-scientific-validity` | `ivdr-performance-evaluation` | inferred |
| `se-evidence-gaps.json` | `fda-510k-substantial-equivalence` | `fda-dual-510k-clia-waiver` | inferred |
| `service-complaint-handoff.json` | `medical-device-service-report-quality-routing` | — | unconsumed |
| `service-event-quality-record.json` | `medical-device-service-report-quality-routing` | — | unconsumed |
| `service-quality-routing.json` | `medical-device-service-report-quality-routing` | — | unconsumed |
| `skills/<skill-name>/SKILL.md` | `composable-skill-factory` | `central-skill-repository-curation` | inferred |
| `software-evidence-gaps.json` | `iec62304-software-lifecycle` | `medical-device-cybersecurity-lifecycle` | inferred |
| `software-lifecycle-assessment.json` | `iec62304-software-lifecycle` | `medical-device-cybersecurity-lifecycle` | inferred |
| `software-safety-classification.json` | `iec62304-software-lifecycle` | `medical-device-cybersecurity-lifecycle` | inferred |
| `source-context.json` | `source-to-context` | — | unconsumed |
| `source-context.md` | `source-to-context` | — | unconsumed |
| `special-controls-matrix.json` | `fda-de-novo-special-controls` | — | unconsumed |
| `sport-adaptation-analysis.json` | `sport-adaptation-analysis` | `sport-athlete-management` | inferred |
| `sport-diagnostics.json` | `sport-performance-diagnostics` | `sport-adaptation-analysis`, `sport-diagnostics-training-report-workflow`, `sport-endurance-programming` | inferred |
| `sport-fueling-plan.json` | `sport-nutrition-fueling` | `sport-athlete-management` | inferred |
| `sport-mesocycle.json` | `sport-mesocycle-planning` | `sport-athlete-management`, `sport-endurance-programming`, `sport-microcycle-planning`, `sport-nutrition-fueling`, `sport-strength-power-programming` | inferred |
| `sport-microcycle.json` | `sport-microcycle-planning` | `sport-adaptation-analysis`, `sport-athlete-management`, `sport-endurance-programming`, `sport-environment-travel`, `sport-nutrition-fueling`, `sport-performance-psychology`, `sport-strength-power-programming`, `sport-training-adaptation-engine`, `sport-training-music` | inferred |
| `sport-performance-model.json` | `sport-goal-performance-model` | `sport-athlete-management`, `sport-endurance-programming`, `sport-performance-psychology`, `sport-season-periodization`, `sport-strength-power-programming`, `sport-testing-battery` | inferred |
| `sport-report-package` | `sport-diagnostics-training-report-workflow` | — | unconsumed |
| `sport-season-plan.json` | `sport-season-periodization` | `sport-athlete-management`, `sport-mesocycle-planning`, `sport-testing-battery` | inferred |
| `sport-testing-plan.json` | `sport-testing-battery` | `sport-athlete-management` | inferred |
| `sport-training-plan.json` | `sport-training-programming` | `sport-diagnostics-training-report-workflow` | inferred |
| `stakeholder-questionnaire.json` | `external-stakeholder-questionnaire` | — | unconsumed |
| `stakeholder-questionnaire.md` | `external-stakeholder-questionnaire` | — | unconsumed |
| `strength-power-plan.json` | `sport-strength-power-programming` | `sport-athlete-management` | inferred |
| `submission-readiness.json` | `fda-estar-submission-builder` | `fda-acceptance-readiness`, `fda-additional-information-response` | inferred |
| `substantial-equivalence-assessment.json` | `fda-510k-substantial-equivalence` | `fda-dual-510k-clia-waiver` | inferred |
| `substantial-equivalence-matrix.md` | `fda-510k-substantial-equivalence` | `fda-dual-510k-clia-waiver` | inferred |
| `supplier-control-plan.json` | `supplier-quality-medical-device` | — | unconsumed |
| `supplier-quality-assessment.json` | `supplier-quality-medical-device` | — | unconsumed |
| `supplier-signal-set.json` | `supplier-quality-medical-device` | — | unconsumed |
| `synchronization manifest` | `central-skill-repository-curation` | — | unconsumed |
| `technology-due-diligence.json` | `technology-due-diligence` | — | unconsumed |
| `technology-due-diligence.md` | `technology-due-diligence` | — | unconsumed |
| `technology-offer-assessment.json` | `technology-offer-assessment` | `technology-due-diligence` | inferred |
| `technology-offer-assessment.md` | `technology-offer-assessment` | `technology-due-diligence` | inferred |
| `technology-offer-gap-set.json` | `technology-offer-assessment` | `technology-due-diligence` | inferred |
| `technology-offer-question-set.json` | `technology-offer-assessment` | `technology-due-diligence` | inferred |
| `technology-offer-question-set.md` | `technology-offer-assessment` | `technology-due-diligence` | inferred |
| `training-adaptation-decision.json` | `sport-training-adaptation-engine` | `sport-athlete-management` | inferred |
| `training-music-profile.json` | `sport-training-music` | `sport-athlete-management` | inferred |
| `trend-signal-set.json` | `ivdr-pms-vigilance` | `ivdr-field-safety-corrective-action`, `medical-device-complaint-regulatory-routing` | inferred |
| `ui-prototype-plan.md` | `project-beta-readiness` | — | unconsumed |
| `updated skill repository` | `central-skill-repository-curation` | — | unconsumed |
| `usability-engineering-assessment.json` | `iec62366-usability-engineering` | — | unconsumed |
| `usability-evidence-gaps.json` | `iec62366-usability-engineering` | — | unconsumed |
| `use-related-risk-evidence.json` | `iec62366-usability-engineering` | — | unconsumed |
| `verification evidence` | `iterate-software-projects` | `agent-handoff`, `architecture-deepening-review`, `disciplined-diagnosis`, `project-beta-readiness` | inferred |
| `verification-report.md` | `test-driven-vertical-slice` | `domain-model-maintenance`, `implement-from-issue`, `merge-conflict-resolution` | inferred |
| `verified terminal status` | `deferred-external-action-verification` | `engineering-delivery-followup`, `implement-from-issue`, `merge-conflict-resolution`, `qms-management-review-action-followup` | inferred |
| `verified-fix-evidence.md` | `disciplined-diagnosis` | `architecture-deepening-review`, `implement-from-issue`, `large-work-wayfinder`, `merge-conflict-resolution`, `test-driven-vertical-slice`, `throwaway-prototype`, `two-axis-code-review` | inferred |
| `vertical-issues.json` | `spec-to-vertical-issues` | `test-driven-vertical-slice`, `throwaway-prototype` | inferred |
| `vertical-issues.md` | `spec-to-vertical-issues` | `test-driven-vertical-slice`, `throwaway-prototype` | inferred |
| `vertical-slice-evidence.json` | `test-driven-vertical-slice` | `domain-model-maintenance`, `implement-from-issue`, `merge-conflict-resolution` | inferred |
| `vertical-slice-residual-risk-handoff.json` | `test-driven-vertical-slice` | `domain-model-maintenance`, `implement-from-issue`, `merge-conflict-resolution` | inferred |
| `vigilance-decision-log.json` | `ivdr-pms-vigilance` | `ivdr-field-safety-corrective-action`, `medical-device-complaint-regulatory-routing` | inferred |
| `vigilance-entry-handoff.json` | `medical-device-complaint-regulatory-routing` | — | unconsumed |
| `watch record` | `deferred-external-action-verification` | `engineering-delivery-followup`, `implement-from-issue`, `merge-conflict-resolution`, `qms-management-review-action-followup` | inferred |
| `wayfinding-brief.md` | `large-work-wayfinder` | `decision-record`, `frontend-design-shaping`, `medical-device-regulatory-strategy`, `throwaway-prototype` | inferred |
