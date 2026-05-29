# GENUS_CORE v0.1.1 Release Notes

Release: Pre-Physics Requirements

## Summary

`GENUS_CORE v0.1.1` defines requirements for future passive Physics without
implementing Physics.

The frozen foundation remains:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

## What Changed

```text
Package version moves to 0.1.1
SCHEMA_VERSION remains genus.foundation.v0.0.1
Pre-Physics requirements document added
Docs clarify that Physics is still not active
Tests guard against premature Physics artifacts
```

## Passive Measure Boundary

Future passive measures may read or derive from foundation artifacts, but they:

```text
do not decide
do not prioritize
do not execute
do not react
do not write memory
do not transition
do not constrain
do not create truth
```

## Explicit Non-Scope

v0.1.1 does not introduce:

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

## Acceptance Evidence

v0.1.1 is accepted only when:

```text
pytest is green
CLI smoke test is green
Pre-Physics requirements are documented
Physics artifacts remain absent from src/genus_core
Allowed sentence types remain unchanged
Public foundation functions remain unchanged
No product scope expansion exists
```
