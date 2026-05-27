# GENUS_CORE Status

Current target: `v0.0.8 - Report Boundary Hardening`

Status: implemented after v0.0.7 release freeze

## Released baselines

`GENUS_CORE v0.0.1 - Observation Truth Seed` is released and frozen at:

```text
Tag: genus-core-v0.0.1-observation-truth-seed
Commit: 3cbb2d4416d4011bf53a9af9ead63932cf0be408
```

`GENUS_CORE v0.0.2 - Foundation Hardening` is released and frozen at:

```text
Tag: genus-core-v0.0.2-foundation-hardening
Commit: 44c4dfac04e83455d489d4961ac656f7884e48d8
```

`GENUS_CORE v0.0.3 - Minimal Language Hardening` is released and frozen at:

```text
Tag: genus-core-v0.0.3-minimal-language-hardening
Commit: ebed5c31bfbbfb112cefcace6c684d7dbee0a107
```

`GENUS_CORE v0.0.4 - Observation Classification Hardening` is released and frozen at:

```text
Tag: genus-core-v0.0.4-observation-classification-hardening
Commit: 139ee05e1c6f5a02c430fdce3352fd931f80052f
```

`GENUS_CORE v0.0.5 - Evidence Boundary Hardening` is released and frozen at:

```text
Tag: genus-core-v0.0.5-evidence-boundary-hardening
Commit: 1cde6bccaed6c27290284762a5f05b9dd7a1aaad
```

`GENUS_CORE v0.0.6 - Ledger Minimal Lineage Hardening` is released and frozen at:

```text
Tag: genus-core-v0.0.6-ledger-lineage-hardening
Commit: 2407d153fa91e86796cd9f85cf5fed334f603b74
```

`GENUS_CORE v0.0.7 - Belief Derivation Hardening` is released and frozen at:

```text
Tag: genus-core-v0.0.7-belief-derivation-hardening
Commit: e0ea167167f3cb010b60b497631762b6501b5731
```

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

`GENUS_CORE v0.0.8` is Report Boundary Hardening.

It adds no memory, action, decision, approval, constraint, physics, transition,
reaction, scoring, ranking, or schema version. It only hardens ObservationReport
as a descriptive explanation of BeliefStateSnapshot.

The package version is `0.0.8`, while `SCHEMA_VERSION` remains
`genus.foundation.v0.0.1`.

## Explicitly not active

```text
PhysicsMetric
CognitiveStateMap
TransitionCandidate
ConstraintDecision
Reaction
ReactionExecution
MemoryWrite
MemoryObject
LLM
Worker
RuntimeCell
Organ
Agent
Character
Autonomy
Mutation
Evolution
GraphDB
RuntimeShape
```

## Acceptance state

The implementation is accepted only while these remain true:

```text
pytest is green
CLI smoke test is green
Package version is 0.0.7
SCHEMA_VERSION remains genus.foundation.v0.0.1
Belief derivation accepts only observed EvidenceRecords
All source EvidenceRecord IDs are preserved exactly and in input order
Unsupported observation types are rejected
Mixed scopes are rejected
Belief payload contains no generic evidence, truth, decision, approval, constraint, action, reaction, transition, physics, memory_write, execute, or candidate fields
Forbidden v0.1+ artifacts do not exist
No product scope expansion exists in v0.0.7
```

For v0.0.8, acceptance additionally requires:

```text
Package version is 0.0.8
SCHEMA_VERSION remains genus.foundation.v0.0.1
ObservationReport accepts only BeliefStateSnapshot input through create_observation_report
ObservationReport has a source_state_id
ObservationReport payload rejects decision, action, approval, memory, truth, policy, constraint, transition, and physics fields
ObservationReport summary remains descriptive and does not imply approval, action taken, execution, memory written, or reaction created
ObservationReport creation creates no new Evidence, Ledger, Belief, Memory, Reaction, Decision, Transition, or Physics artifact
Forbidden v0.1+ artifacts do not exist
No product scope expansion exists in v0.0.8
```
