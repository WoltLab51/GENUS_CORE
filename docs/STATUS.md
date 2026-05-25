# GENUS_CORE Status

Current target: `v0.0.1 - Observation Truth Seed`

Status: implemented

## Current architectural state

The implemented first kernel is:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

## Current principle

GENUS first distinguishes:

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

## Current implementation state

`GENUS_CORE v0.0.1` implements the Observation Truth Seed with plain Python
dataclasses, five domain functions, SQLite persistence for EvidenceRecord and
LedgerEntry, pytest coverage, and a minimal CLI smoke path.

## Explicitly not active

```text
PhysicsMetric
CognitiveStateMap
TransitionCandidate
ConstraintDecision
ReactionExecution
MemoryWrite
LLM
Worker
RuntimeCell
Organ
Agent
Character
Autonomy
Mutation
Evolution
```

## Acceptance state

The implementation is accepted only while these remain true:

```text
pytest is green
CLI smoke test is green
Ledger remains append-only
BeliefStateSnapshot references Evidence IDs
ObservationReport has no decision or action power
Forbidden v0.1+ artifacts do not exist
```
