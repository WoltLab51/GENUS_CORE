# GENUS_CORE Function Cells

Status: active for v0.4.3 Artifact Contract and Boundary Wording Alignment

This document makes public GENUS function contracts reviewable without turning
runtime files into large documentation containers.

## Contract Shape

Every public GENUS function must have:

```text
Purpose
Inputs
Outputs
Side effects
Allowed writes
Forbidden effects
Tests
```

Across public function cells, forbidden effects include no persistence, no decision,
no permission, no reaction, no memory write, and no new lineage unless an accepted
contract explicitly permits the lineage reference.

## Foundation Function Cells

`observe_event(...)`

```text
Purpose: derive a passive Observation from a WorldEvent.
Inputs: WorldEvent.
Outputs: Observation.
Side effects: none.
Allowed writes: none.
Forbidden effects: no Evidence, Ledger, Belief, Report, decision, action, memory write, worker, LLM.
Tests: tests/test_observation_classification.py.
```

`create_evidence_record(...)`

```text
Purpose: create a passive EvidenceRecord from an Observation.
Inputs: Observation.
Outputs: EvidenceRecord.
Side effects: none.
Allowed writes: none.
Forbidden effects: no Belief, Report, decision, action, memory write, worker, LLM.
Tests: tests/test_evidence_is_not_belief.py.
```

`append_ledger_entry(...)`

```text
Purpose: create an append-only LedgerEntry lineage record.
Inputs: event type, source reference, target reference, chain metadata.
Outputs: LedgerEntry.
Side effects: none.
Allowed writes: none; SQLite persistence is separate.
Forbidden effects: no truth creation, Belief, Report, decision, action, memory write, worker, LLM.
Tests: tests/test_ledger_append_only.py and tests/test_ledger_lineage_model_hardening.py.
```

`build_belief_state_snapshot(...)`

```text
Purpose: derive a passive BeliefStateSnapshot from observed EvidenceRecord lineage.
Inputs: EvidenceRecord list.
Outputs: BeliefStateSnapshot.
Side effects: none.
Allowed writes: none.
Forbidden effects: no Ledger mutation, Report, decision, action, memory write, worker, LLM.
Tests: tests/test_belief_derivation_hardening.py.
```

`create_observation_report(...)`

```text
Purpose: explain a BeliefStateSnapshot.
Inputs: BeliefStateSnapshot.
Outputs: ObservationReport.
Side effects: none.
Allowed writes: none.
Forbidden effects: no new lineage, decision, action, memory write, reaction, permission, truth.
Tests: tests/test_report_has_no_decision_power.py.
```

## Passive Layer Function Cells

`build_passive_metric_snapshot(...)`

```text
Purpose: describe passive metric outputs from a BeliefStateSnapshot.
Inputs: BeliefStateSnapshot.
Outputs: PassiveMetricSnapshot.
Side effects: none.
Allowed writes: none.
Forbidden effects: no persistence, transition, constraint decision, action, memory write, truth.
Tests: tests/test_passive_physics_derivation.py.
```

`create_passive_metric_report(...)`

```text
Purpose: explain a PassiveMetricSnapshot.
Inputs: PassiveMetricSnapshot.
Outputs: PassiveMetricReport.
Side effects: none.
Allowed writes: none.
Forbidden effects: no new lineage, recommendation, permission, decision, action, memory write, truth.
Tests: tests/test_passive_physics_derivation.py.
```

`build_passive_transition_preview(...)`

```text
Purpose: describe a passive future question from matched Belief and Metric artifacts.
Inputs: BeliefStateSnapshot, PassiveMetricSnapshot.
Outputs: PassiveTransitionPreview.
Side effects: none.
Allowed writes: none.
Forbidden effects: no TransitionCandidate, constraint decision, permission, action, memory write, truth.
Tests: tests/test_passive_transition_derivation.py.
```

`create_passive_transition_report(...)`

```text
Purpose: explain a PassiveTransitionPreview.
Inputs: PassiveTransitionPreview.
Outputs: PassiveTransitionReport.
Side effects: none.
Allowed writes: none.
Forbidden effects: no new lineage, candidate, transition selection, decision, action, memory write, truth.
Tests: tests/test_passive_transition_derivation.py.
```

`build_passive_boundary_relevance_preview(...)`

```text
Purpose: describe passive boundary relevance from matched Belief, Metric, and Transition Preview artifacts.
Inputs: BeliefStateSnapshot, PassiveMetricSnapshot, PassiveTransitionPreview.
Outputs: PassiveBoundaryRelevancePreview.
Side effects: none.
Allowed writes: none.
Forbidden effects: no boundary evaluation, permission, policy result, decision, action, reaction, memory write, truth.
Tests: tests/test_passive_boundary_relevance_derivation.py.
```

`create_passive_boundary_relevance_report(...)`

```text
Purpose: explain a PassiveBoundaryRelevancePreview.
Inputs: PassiveBoundaryRelevancePreview.
Outputs: PassiveBoundaryRelevanceReport.
Side effects: none.
Allowed writes: none.
Forbidden effects: no new lineage, boundary evaluation, permission, policy result, decision, action, reaction, memory write, truth.
Tests: tests/test_passive_boundary_relevance_derivation.py and tests/test_passive_boundary_relevance_boundary_audit.py.
```
