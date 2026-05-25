# GENUS_CORE Status

Current target: `v0.0.3 - Minimal Language Hardening`

Status: implemented after v0.0.2 release freeze

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

`GENUS_CORE v0.0.3` is Minimal Language Hardening.

It adds no new GENUS capability and no new schema version. It centralizes and
tests the allowed internal sentence types around the existing v0.0.1 foundation
language.

The package version is `0.0.3`, while `SCHEMA_VERSION` remains
`genus.foundation.v0.0.1`.

## Current principle

GENUS still first distinguishes:

```text
Observation
Evidence
Belief
Ledger
Report
```

before it can introduce:

```text
Physics
Map
Transition
Constraint
Reaction
Memory
```

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
Package version is 0.0.3
SCHEMA_VERSION remains genus.foundation.v0.0.1
Only WORLD_EVENT, OBSERVATION, EVIDENCE, LEDGER, BELIEF, REPORT are valid sentence types
Unknown and forbidden future sentence types are rejected
Forbidden v0.1+ artifacts do not exist
No product scope expansion exists in v0.0.3
```
