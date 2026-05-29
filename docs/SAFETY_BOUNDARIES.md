# GENUS_CORE Safety Boundaries

Status: active boundary document for GENUS_CORE v0.2.0

## Purpose

This document defines the operational build boundaries for GENUS_CORE.

It exists so that new power cannot enter the repository through ambiguous
language, convenience helpers, hidden side effects, or untested capability
growth.

## Current Boundary

The current active boundary is:

```text
passive foundation plus passive Physics only
```

The active foundation chain remains:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

The report may explain what was observed, recorded, and derived. It must not
decide, approve, execute, react, write memory, create truth, transition, or
constrain.

The only new product capability allowed in v0.2.0 is passive Physics.

Passive Physics may read only a `BeliefStateSnapshot` and produce:

```text
PassiveMetricSnapshot
PassiveMetricReport
```

These artifacts are descriptive, side-effect free, ephemeral, and not persisted.

## Capability Admission Rule

A new capability may be introduced only when all of these exist before or with
the change:

```text
GENUS_CHARTER.md allows the direction.
SAFETY_BOUNDARIES.md defines the boundary.
VOCABULARY.md defines the concept.
QUALITY_GATES.md defines acceptance.
DECISIONS.md records the reason.
STATUS.md reflects the current state.
Tests prove the capability and its forbidden effects.
```

No further product capability is allowed in v0.2.0.

## Forbidden in the Current Boundary

These remain forbidden as active runtime objects, modules, imports, public
functions, persistence tables, CLI commands, or hidden effects:

```text
PhysicsMetric
PassiveMetric
Potential
Cost
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

`pressure`, `inhibition`, and `stability` are allowed only as passive
`metric_name` string values inside `PassiveMetricSnapshot` outputs. They must
not become classes, modules, commands, persistence tables, policies,
priorities, recommendations, permissions, or action triggers.

`worker` remains allowed only as a passive Observation scope label. It is not a
Worker capability.

## Passive Physics Boundary

The active v0.2.0 direction is passive Physics only:

```text
BeliefStateSnapshot
-> PassiveMetricSnapshot
-> PassiveMetricReport
-> no action
```

The first implementation must remain descriptive and must not create
TransitionCandidate, ConstraintDecision, Reaction, MemoryWrite, Worker, LLM, or
new truth behavior.

The first implementation uses only:

```text
metric_name = pressure
metric_name = inhibition
metric_name = stability
```

`cost` and `potential` remain excluded from the first implementation unless a
later accepted decision changes that boundary.

## Stop Conditions

Stop development if any of these occur:

```text
A new CLI command appears.
A new product capability appears beyond passive Physics.
SCHEMA_VERSION changes from genus.foundation.v0.0.1 without an accepted schema release.
Observation, Evidence, Belief, Report, Decision, or Action are mixed.
LLM output is treated as truth.
Memory is written in v0.1.x or v0.2.0 passive Physics.
Reaction, TransitionCandidate, or ConstraintDecision appears before its accepted release.
Worker execution appears before governance exists.
GraphDB is introduced as truth.
RuntimeShape activates dynamically.
Self-mutation occurs without proposal, test, approval, rollback, and fossil.
Terms imply more power than the code actually controls.
```
