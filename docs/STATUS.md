# GENUS_CORE Status

Current target: `v0.0.5 - Evidence Boundary Hardening`

Status: implemented after v0.0.4 release freeze

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

`GENUS_CORE v0.0.5` is Evidence Boundary Hardening.

It adds no action, memory, reaction, physics, transition, belief expansion, or
schema version. It only hardens how Observation becomes EvidenceRecord.

The package version is `0.0.5`, while `SCHEMA_VERSION` remains
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
Package version is 0.0.5
SCHEMA_VERSION remains genus.foundation.v0.0.1
EvidenceRecord provenance is constrained
Evidence payload contains evidence_claim = observation_recorded
Evidence payload contains no belief, decision, action, reaction, or memory_write fields
Evidence creation remains side-effect free
Forbidden v0.1+ artifacts do not exist
No product scope expansion exists in v0.0.5
```
