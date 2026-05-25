# GENUS_CORE Decisions

Status: draft for foundation freeze

## Decision 0001 — Start smaller than Full Cognitive Physics

Decision:

`GENUS_CORE` starts with `v0.0.1 — Observation Truth Seed`, not full `v0.1 Cognitive Physics Seed`.

Reason:

The first stable core must prove that GENUS can distinguish Observation, Evidence, Ledger, Belief, and Report before introducing Physics, Map, Transition, Constraint, or Reaction.

Impact:

The following concepts are out of scope for v0.0.1:

```text
PhysicsMetric
CognitiveStateMap
TransitionCandidate
ConstraintDecision
ReactionExecution
MemoryWrite
LLM
Worker
Cell
Organ
```

## Decision 0002 — Observation is first true GENUS act

Decision:

`WorldEvent` is an occasion. `Observation` is the first true GENUS act.

Reason:

GENUS does not possess the world. GENUS observes world events.

Impact:

`WorldEvent` must never be treated as `Observation`.

## Decision 0003 — Ledger is lineage, not truth

Decision:

`LedgerEntry` proves sequence and lineage, not content truth.

Reason:

A ledger can prove that a record was created, but not that the content of that record is world-true.

Impact:

`EvidenceRecord.truth_status` is the truth-status marker, not `LedgerEntry`.

## Decision 0004 — Report has no decision power

Decision:

`ObservationReport` explains but never decides, approves, or executes.

Reason:

Reports must remain inspectable explanations and must not become hidden control surfaces.

Impact:

Report models must not contain `decision`, `action`, `approval`, `execute`, `reaction`, or `memory_write` fields.

## Decision 0005 — Function-first, responsibility-first

Decision:

GENUS_CORE is built from small responsibility-focused functions, not a monolith, manager, service god-object, or atomized helper files.

Reason:

The core must be testable, inspectable, and later refinable without creating a hidden orchestration monolith.

Impact:

Public functions must carry a GENUS responsibility. Helpers stay private.

## Decision 0006 - v0.0.1 builds no action path

Decision:

v0.0.1 baut nur Observation -> Evidence -> Belief und keine Handlung.

Reason:

The first implementation must freeze the epistemic foundation before any
decision, reaction, memory write, worker, runtime cell, organ, agent, LLM, or
physics capability exists.

Impact:

The CLI may compose the smoke path and print an explanation, but it must not
execute memory writes, reactions, decisions, transitions, or constraints.
