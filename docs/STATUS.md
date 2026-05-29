# GENUS_CORE Status

Current target: `v0.1.3 - Passive Metric Acceptance Criteria`

Status: acceptance-criteria-only step after v0.1.2 Passive Metric Vocabulary

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

`GENUS_CORE v0.1.3` is Passive Metric Acceptance Criteria.

It adds no active Physics, metric model, metric record, metric function, metric
output shape, metric persistence, memory, action, decision, approval,
constraint, transition, reaction, domain function behavior, public domain
function, CLI command, sentence type, or schema version. It only defines
acceptance criteria for future passive metrics in docs and tests.

The package version is `0.1.3`, while `SCHEMA_VERSION` remains
`genus.foundation.v0.0.1`.

## Explicitly not active

```text
PhysicsMetric
Pressure
Potential
Cost
Inhibition
Stability
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

## v0.1.3 Acceptance Criteria Acceptance

The implementation is accepted only while these remain true:

```text
pytest is green
CLI smoke test is green
Package version is 0.1.3
SCHEMA_VERSION remains genus.foundation.v0.0.1
PASSIVE_METRIC_ACCEPTANCE_CRITERIA_v0.1.3.md exists
pressure, inhibition, and stability are first future implementation candidates
cost and potential remain excluded from first implementation
Allowed read surface is limited to BeliefStateSnapshot, source_evidence_ids_json, and safe descriptive foundation payload fields
Output category is passive descriptive label plus explanation only
Exact output shape is deferred to v0.1.4
Forbidden effects include Ledger writes, Evidence creation, Belief mutation, Report triggering, TransitionCandidate, ConstraintDecision, Reaction, MemoryWrite, prioritization, recommendation, permission, activation, action, and truth creation
No metric implementation artifacts exist in src/genus_core
Allowed sentence types remain exactly WORLD_EVENT, OBSERVATION, EVIDENCE, LEDGER, BELIEF, REPORT
Public foundation functions remain exactly observe_event, create_evidence_record, append_ledger_entry, build_belief_state_snapshot, create_observation_report
CLI exposes only observe
No product scope expansion exists in v0.1.3
```
