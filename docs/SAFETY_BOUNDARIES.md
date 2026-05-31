# GENUS_CORE Safety Boundaries

Status: active boundary document for GENUS_CORE v0.3.6

## Purpose

This document defines the operational build boundaries for GENUS_CORE.

It exists so that new power cannot enter the repository through ambiguous
language, convenience helpers, hidden side effects, or untested capability
growth.

Artifact composition must also respect `ARTIFACT_CONTRACTS.md`. Shared artifact
contracts preserve IDs, lineage, report limits, and durable/ephemeral boundaries
without forcing every artifact to use identical fields.

## Current Boundary

The current active boundary is:

```text
passive foundation plus passive Physics plus passive transition preview only
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

`ObservationReport` may explain what was observed, recorded, and derived. It
must not decide, approve, execute, react, write memory, create truth,
transition, constrain, or measure physics.

The only new product capability allowed in v0.2.x is passive Physics.

Passive Physics may read only a `BeliefStateSnapshot` and produce:

```text
PassiveMetricSnapshot
PassiveMetricReport
```

These artifacts are descriptive, side-effect free, ephemeral, and not persisted.
`PassiveMetricReport` describes passive metrics only. It must not decide,
recommend, prioritize, permit, execute, transition, constrain, react, write
memory, or create truth.

## Capability Admission Rule

A new capability may be introduced only when all of these exist before or with
the change:

```text
GENUS_CHARTER.md allows the direction.
SAFETY_BOUNDARIES.md defines the boundary.
VOCABULARY.md indexes the vocabulary definition.
QUALITY_GATES.md defines acceptance.
DECISIONS.md records the reason.
STATUS.md reflects the current state.
Tests prove the capability and its forbidden effects.
```

The only new product capability allowed in v0.3.0 is passive transition
preview.

No further product capability is allowed in v0.3.0.

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

The active v0.2.x direction is passive Physics only:

```text
BeliefStateSnapshot
-> PassiveMetricSnapshot
-> PassiveMetricReport
-> no action
```

The first implementation must remain descriptive and must not create
TransitionCandidate, ConstraintDecision, Reaction, MemoryWrite, Worker, LLM, or
new truth behavior.

This is narrow passive metric description. It is not dynamic physics,
simulation, transition physics, constraint decision, recommendation,
prioritization, permission, reaction, or action.

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
Memory is written in v0.1.x or v0.2.x passive Physics.
Reaction, TransitionCandidate, or ConstraintDecision appears before its accepted release.
Worker execution appears before governance exists.
GraphDB is introduced as truth.
RuntimeShape activates dynamically.
Self-mutation occurs without proposal, test, approval, rollback, and fossil.
Terms imply more power than the code actually controls.
```

## Passive Transition Preview Boundary

The active v0.3.0 direction is passive preview only:

```text
BeliefStateSnapshot
+ PassiveMetricSnapshot
-> PassiveTransitionPreview
-> PassiveTransitionReport
-> no action
```

`PassiveTransitionPreview` is not `TransitionCandidate`.
`PassiveTransitionReport` is not `ConstraintDecision`.

The word `transition` may appear in passive v0.3.0 artifact names, module
names, function names, docs, and tests only when it is clearly qualified as
passive preview or a forbidden active capability. It must not appear as a
standalone output or payload field and must not imply an active transition.

The runtime `possible_future_question` value must remain descriptive and
question-like. It must not contain `should`, `must`, `allow`, `block`,
`execute`, `write`, `approve`, or `recommend`.

`PassiveTransitionReport.summary` must remain descriptive-only. It must not
imply approval, permission, decision, execution, action taken, memory creation,
reaction creation, selected transition, selected candidate, or decision made.

## Planned v0.4.0 Passive Boundary Relevance

Planned v0.4.0 work is spec-only. It must not add runtime code.

Passive Boundary Relevance may define how a later passive description names
boundary areas that could be relevant. It must not evaluate boundaries, evaluate
permission, evaluate policy, approve, reject, allow, block, decide, recommend,
execute, react, or write memory.

`boundary_area` must be planned as a closed enum:

```text
memory_boundary
passive_foundation_boundary
passive_preview_boundary
```

`observed_boundary_relevance` must remain descriptive and non-numeric. It must
not imply score, rank, priority, severity, weight, recommendation, or
permission.

## Watched Wording

`evaluate` and `evaluation` are watched terms. They may drift toward permission,
policy, approval, rejection, allow/block, or decision semantics. Future use is
allowed only when an accepted spec explicitly qualifies it as descriptive
relevance mapping.
