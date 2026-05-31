# GENUS_CORE Roadmap - Planned
Status: active for v0.4.1 Passive Boundary Relevance Preview Seed
Moved from `docs/ROADMAP_STABLE_CORE.md`.

### v0.4.0 - Passive Boundary Relevance Spec

Accepted spec-only baseline for passive boundary relevance description.

This is not a runtime implementation. It defines how a later
`PassiveBoundaryRelevancePreview` and
`PassiveBoundaryRelevanceReport` may describe relevant boundary areas without
evaluating boundaries, granting permission, producing policy results,
allowing/blocking, deciding, reacting, or writing memory.

The name is deliberately `Boundary Relevance`, not `Boundary
Evaluation`, because boundary relevance must not evaluate boundaries.

### v0.4.1 - Passive Boundary Relevance Preview Seed

Active narrow runtime baseline for:

```text
BeliefStateSnapshot
+ PassiveMetricSnapshot
+ PassiveTransitionPreview
-> PassiveBoundaryRelevancePreview
-> PassiveBoundaryRelevanceReport
-> no decision
-> no action
```

It emits only `memory_boundary` and `passive_preview_boundary`.
`passive_foundation_boundary` remains spec-known but not emitted until a later
explicit passive derivation rule exists.

## Later, Not Yet Active

Future planning may later introduce passive cognitive physics concepts, but
only after the v0.1.0 foundation freeze and pre-Physics requirements are
accepted.

Still forbidden before explicit future acceptance:

```text
PhysicsMetric
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
