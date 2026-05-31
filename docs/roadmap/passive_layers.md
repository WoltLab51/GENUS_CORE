# GENUS_CORE Roadmap - Passive Layers
Status: active for v0.4.3 Artifact Contract and Boundary Wording Alignment
Moved from `docs/ROADMAP_STABLE_CORE.md`.

### v0.2.0 - Passive Physics Seed

First implementation of accepted passive Physics concepts after v0.1.10.

The active chain extends only to:

```text
BeliefStateSnapshot
-> PassiveMetricSnapshot
-> PassiveMetricReport
-> no action
```

The first active metric names are limited to:

```text
pressure
inhibition
stability
```

`cost` and `potential` remain excluded. v0.2.0 does not introduce transition,
constraint, reaction, memory, worker, LLM, persistence, or CLI expansion.

### v0.2.1 - Passive Physics Boundary Cleanup

Clarifies the v0.2.0 passive Physics seed without adding new capability.

It distinguishes `ObservationReport` from `PassiveMetricReport`, records that
v0.2.x is narrow passive metric description rather than dynamic physics or
simulation, and updates pre-Physics gates so allowed passive v0.2.x artifacts
do not conflict with the continued ban on active metric classes, functions,
persistence, CLI expansion, transition, constraint, reaction, memory, workers,
LLMs, GraphDB, or RuntimeShape.

### v0.3.0 - Passive Transition Preview Seed

Adds the first passive preview layer after passive Physics:

```text
BeliefStateSnapshot
+ PassiveMetricSnapshot
-> PassiveTransitionPreview
-> PassiveTransitionReport
-> no action
```

This is not `TransitionCandidate`, `ConstraintDecision`, `Reaction`, or
MemoryWrite. It describes only a possible later governed question while keeping
`target_state`, selected/proposed transition fields, permission, priority,
recommendation, allow/block, execution, and persistence out of scope.

### v0.3.1 - Passive Transition Boundary Audit

Audits the v0.3.0 passive preview layer without adding capability.

It hardens `PassiveTransitionReport.summary` against active wording and
neutralizes the memory-tension `possible_future_question`. It does not add new
preview types, persistence, CLI commands, schema changes, transition
candidates, constraint decisions, reactions, memory writes, workers, LLMs,
GraphDB, or RuntimeShape.
