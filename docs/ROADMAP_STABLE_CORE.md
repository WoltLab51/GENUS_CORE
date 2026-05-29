# GENUS_CORE Roadmap to Stable Core

Status: aligned after v0.1.0 foundation freeze

## Stable Core Direction

GENUS_CORE becomes stable by first freezing the epistemic foundation:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

Only after that foundation is frozen may later cognitive physics concepts be
planned.

## Completed Foundation Path

### v0.0.1 - Observation Truth Seed

Established the first active chain:

```text
WorldEvent -> Observation -> EvidenceRecord -> LedgerEntry -> BeliefStateSnapshot -> ObservationReport
```

Goal:

```text
Observation != Evidence
Evidence != Belief
Ledger != Truth
Report != Action
```

### v0.0.2 - Foundation Hardening

Hardened SQLite constraints, append-only Ledger behavior, enum validation,
schema persistence, model invariants, CLI smoke behavior, and forbidden-object
scanning.

### v0.0.3 - Minimal Language Hardening

Centralized the allowed sentence types:

```text
WORLD_EVENT
OBSERVATION
EVIDENCE
LEDGER
BELIEF
REPORT
```

### v0.0.4 - Observation Classification Hardening

Hardened deterministic `WorldEvent -> Observation` classification without
Meaning, Intent, parser, LLM, transition, reaction, memory, or physics.

### v0.0.5 - Evidence Boundary Hardening

Hardened `Observation -> EvidenceRecord` so Evidence records an Observation
with provenance and truth status, but does not become truth, belief, memory,
decision, or action.

### v0.0.6 - Ledger Minimal Lineage Hardening

Constrained Ledger to the only real v0.0.x lineage event:

```text
event_type = evidence_record_created
source_kind = observation
target_kind = evidence_record
```

### v0.0.7 - Belief Derivation Hardening

Hardened `EvidenceRecord -> BeliefStateSnapshot` so Belief is derived only from
all supplied observed EvidenceRecords, preserves source evidence IDs, rejects
mixed scopes, and remains neither truth nor action.

### v0.0.8 - Report Boundary Hardening

Hardened `BeliefStateSnapshot -> ObservationReport` so Report is
descriptive-only and cannot become decision, approval, action, memory, reaction,
truth, transition, constraint, or physics surface.

### v0.0.9 - Foundation Freeze Readiness Audit

Audits the complete foundation chain, release history, boundary invariants,
forbidden objects, version/schema invariants, and roadmap alignment.

It adds no new GENUS capability.

### v0.1.0 - Full Epistemic Core Freeze

Scope:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

Goal:

```text
The complete passive epistemic foundation is frozen as the base for future work.
```

v0.1.0 does not introduce Physics, Map, Transition, Constraint, Reaction,
MemoryWrite, Worker, Cell, Organ, Agent, LLM, RuntimeShape, or GraphDB.

### v0.1.1 - Pre-Physics Requirements

Defines requirements for future passive Physics without implementing metrics,
metric records, metric functions, or new sentence types.

Likely first passive concepts are `pressure`, `inhibition`, and `stability`.
Higher-risk planned concepts are `cost` and `potential`.

### v0.1.2 - Passive Metric Vocabulary

Defines planned-not-active passive metric vocabulary while keeping metric
implementation inactive.

First passive candidates:

```text
pressure
inhibition
stability
```

Higher-risk planned terms:

```text
cost
potential
```

### v0.1.3 - Passive Metric Acceptance Criteria

Defines accepted inputs, output category, forbidden effects, and quality gates
for a future passive Physics seed without implementing metrics.

First future implementation candidates remain:

```text
pressure
inhibition
stability
```

Still excluded from first implementation:

```text
cost
potential
```

The exact metric output shape is deferred to v0.1.5.

### v0.1.4 - Release Integrity & CI Gate

Adds a minimal GitHub Actions gate for the frozen foundation and pre-Physics
documentation line.

CI runs only:

```text
install
pytest
CLI smoke
```

It does not add coverage, linting, formatting, matrix builds, caching, release
automation, deployment, metric output shape, or product behavior.

### v0.1.5 - Passive Metric Output Shape

Defines the exact planned-not-active passive metric output shape without
implementing metrics.

The first output metric names are limited to:

```text
pressure
inhibition
stability
```

The output shape separates `level` from `assessment_status` so `none` does not
mean insufficient input.

`cost` and `potential` remain excluded from the first output shape.

### v0.1.6 - Passive Metric Safety Audit

Audits requirements, vocabulary, acceptance criteria, output shape, CI,
forbidden-object absence, and non-agentic metric boundaries before the first
passive Physics implementation.

The audit requires:

```text
assessment_status = insufficient_input -> level = none
assessment_status = not_applicable -> level = none
assessment_status = assessed -> level = none | low | medium | high
```

### v0.1.7 - Foundation Cleanup and Integrity Repair

Cleans up the v0.1.6 baseline before passive Physics begins.

It tightens Ledger lineage target requirements, clarifies that `worker` remains
only a passive observation scope label, records the current GitHub Actions
signal, and keeps `SCHEMA_VERSION` at `genus.foundation.v0.0.1`.

### v0.1.8 - Release Integrity Finalization

Finalizes the green pre-v0.2.0 baseline.

It records the concrete Ledger target invariant and the GitHub Actions YAML
smoke fix while preserving the v0.1.7 tag as historical.

### v0.1.9 - Boundary Naming Cleanup

Sharpens passive foundation terminology before passive Physics begins.

It renames ephemeral Belief and Report memory-request payload fields from
`pending_memory_request` and `candidate_content` to `observed_memory_request`
and `observed_memory_content`, clarifies package/schema/capability boundaries,
and hardens the CI workflow test for the YAML block scalar CLI smoke command.

### v0.1.10 - GENUS Charter and Safety Boundary

Anchors the GENUS vision as repository governance before passive Physics begins.

It adds the GENUS charter, operational safety boundaries, and tests proving the
core build directives are present. It adds no runtime capability.

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

### v0.3.2 - Build Structure Guardrails

Adds project-structure governance without runtime capability.

It treats code, tests, docs, specs, decisions, and quality gates as governed
artifacts and freezes historical longfiles behind explicit ceilings, reasons,
and planned split/review notes.

### Planned v0.4.0 - Passive Boundary Relevance Spec

Spec-only planning for a later passive boundary relevance description.

This is not an implementation and does not change the active v0.3.2 baseline.
It defines how a later `PassiveBoundaryRelevancePreview` and
`PassiveBoundaryRelevanceReport` may describe relevant boundary areas without
evaluating boundaries, granting permission, producing policy results,
allowing/blocking, deciding, reacting, or writing memory.

The planned name is deliberately `Boundary Relevance`, not `Boundary
Evaluation`, because v0.4.0 must not yet evaluate boundaries.

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
