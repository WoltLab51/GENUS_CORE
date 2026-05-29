# GENUS_CORE Status

Current target: `v0.1.5 - Passive Metric Output Shape`

Status: docs/tests-only output shape step after v0.1.4 Release Integrity & CI
Gate.

## Released baselines

```text
v0.0.1 Observation Truth Seed
Tag: genus-core-v0.0.1-observation-truth-seed
Commit: 3cbb2d4416d4011bf53a9af9ead63932cf0be408

v0.0.2 Foundation Hardening
Tag: genus-core-v0.0.2-foundation-hardening
Commit: 44c4dfac04e83455d489d4961ac656f7884e48d8

v0.0.3 Minimal Language Hardening
Tag: genus-core-v0.0.3-minimal-language-hardening
Commit: ebed5c31bfbbfb112cefcace6c684d7dbee0a107

v0.0.4 Observation Classification Hardening
Tag: genus-core-v0.0.4-observation-classification-hardening
Commit: 139ee05e1c6f5a02c430fdce3352fd931f80052f

v0.0.5 Evidence Boundary Hardening
Tag: genus-core-v0.0.5-evidence-boundary-hardening
Commit: 1cde6bccaed6c27290284762a5f05b9dd7a1aaad

v0.0.6 Ledger Minimal Lineage Hardening
Tag: genus-core-v0.0.6-ledger-lineage-hardening
Commit: 2407d153fa91e86796cd9f85cf5fed334f603b74

v0.0.7 Belief Derivation Hardening
Tag: genus-core-v0.0.7-belief-derivation-hardening
Commit: e0ea167167f3cb010b60b497631762b6501b5731

v0.0.8 Report Boundary Hardening
Tag: genus-core-v0.0.8-report-boundary-hardening
Commit: 4f738f10bf221f2b215f765effab80871b9838bb

v0.0.9 Foundation Freeze Readiness Audit
Tag: genus-core-v0.0.9-foundation-freeze-readiness
Commit: adc53da7ad645a034bfa07ade2f4a3a8cac1b4ac

v0.1.0 Full Epistemic Core Freeze
Tag: genus-core-v0.1.0-full-epistemic-core-freeze
Commit: 57aa74f9e841befa521c9cff23c996e50ec36d47

v0.1.1 Pre-Physics Requirements
Tag: genus-core-v0.1.1-pre-physics-requirements
Commit: f32aa894f34efbdc4fb007a709f4961a6f4e9731

v0.1.2 Passive Metric Vocabulary
Tag: genus-core-v0.1.2-passive-metric-vocabulary
Commit: 96d9176e3020cea8c20a2fd8e7d835292fb60160

v0.1.3 Passive Metric Acceptance Criteria
Tag: genus-core-v0.1.3-passive-metric-acceptance-criteria
Commit: 38e0aa8569dce2d7463ff0db972cf6c77f2c7f18

v0.1.4 Release Integrity & CI Gate
Tag: genus-core-v0.1.4-release-integrity-ci-gate
Commit: 43720b9005b134a96a0876981274b42b0ee39f42
```

## Frozen foundation chain

The only active epistemic chain remains:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

## Current implementation state

`GENUS_CORE v0.1.5` is Passive Metric Output Shape.

It defines a planned-not-active future passive metric output shape in docs and
tests only. It does not add runtime metric classes, metric records, metric
functions, metric persistence, sentence types, CLI commands, or product
behavior.

The package version is `0.1.5`, while `SCHEMA_VERSION` remains
`genus.foundation.v0.0.1`.

## Explicitly not active

```text
PhysicsMetric
Pressure
Potential
Cost
Inhibition
Stability
MetricRecord
PassiveMetric
MetricOutput
PassiveMetricOutput
MetricOutputShape
CognitiveStateMap
TransitionCandidate
ConstraintDecision
Reaction
ReactionExecution
MemoryWrite
MemoryObject
Worker
RuntimeCell
Organ
Agent
Character
LLM
Autonomy
Mutation
Evolution
GraphDB
RuntimeShape
```

## v0.1.5 Output Shape Acceptance

The implementation is accepted only while these remain true:

```text
pytest is green
CLI smoke test is green
Package version is 0.1.5
SCHEMA_VERSION remains genus.foundation.v0.0.1
PASSIVE_METRIC_OUTPUT_SHAPE_v0.1.5.md exists
metric_name values are limited to pressure, inhibition, stability
cost and potential remain excluded from first output shape
level values are limited to none, low, medium, high
assessment_status values are limited to assessed, insufficient_input, not_applicable
level = none does not mean insufficient input
explanation is descriptive-only
explanation does not recommend, permit, approve, rank, prioritize, trigger, execute, transition, react, or write memory
source_evidence_ids_json is lineage only
source_evidence_ids_json does not imply scoring, weighting, ranking, priority, or confidence
Allowed sentence types remain exactly WORLD_EVENT, OBSERVATION, EVIDENCE, LEDGER, BELIEF, REPORT
Public foundation functions remain exactly observe_event, create_evidence_record, append_ledger_entry, build_belief_state_snapshot, create_observation_report
CLI exposes only observe
No product scope expansion exists in v0.1.5
```
