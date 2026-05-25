# GENUS_CORE Status

Current target: `v0.0.2 - Foundation Hardening`

Status: implemented after v0.0.1 release freeze

## Released baseline

`GENUS_CORE v0.0.1 - Observation Truth Seed` is released and frozen at:

```text
Tag: genus-core-v0.0.1-observation-truth-seed
Commit: 3cbb2d4416d4011bf53a9af9ead63932cf0be408
```

The v0.0.1 release defines the only active epistemic chain:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

## Current implementation state

`GENUS_CORE v0.0.2` is Foundation Hardening.

It adds no new GENUS capability. It strengthens tests, SQLite invariants,
version/schema checks, CLI smoke coverage, forbidden-object scanning, and
release documentation around the existing v0.0.1 Observation Truth Seed.

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
Ledger remains append-only
SQLite constraints remain verified
Package version is 0.0.2
SCHEMA_VERSION remains genus.foundation.v0.0.1
BeliefStateSnapshot references Evidence IDs
ObservationReport has no decision or action power
Forbidden v0.1+ artifacts do not exist
No product scope expansion exists in v0.0.2
```
