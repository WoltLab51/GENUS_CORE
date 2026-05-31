# GENUS_CORE Foundation Spec v0.0.1

Status: frozen historical reference; active contracts live in current governance docs
Scope: `GENUS_CORE v0.0.1 — Observation Truth Seed`

Boundary note: this document preserves historical v0.0.1 foundation wording.
It must not override `GENUS_CHARTER.md`, `SAFETY_BOUNDARIES.md`,
`ARTIFACT_CONTRACTS.md`, `BUILD_RULES.md`, `QUALITY_GATES.md`,
`DECISIONS.md`, `VOCABULARY.md`, or `STATUS.md`.

## 1. Purpose

`GENUS_CORE v0.0.1` defines the smallest stable foundation of GENUS.

It does not build intelligence, autonomy, reaction execution, memory write, agent behavior, worker execution, LLM parsing, graph runtime, or cell runtime.

It builds only the epistemic base:

```text
WorldEvent
→ Observation
→ EvidenceRecord
→ LedgerEntry
→ BeliefStateSnapshot
→ ObservationReport
```

The purpose is to ensure that GENUS can distinguish:

```text
what happened
what was observed
what was stored as evidence
what is derived as current internal belief
what is only explained in a report
```

## 2. Core Principle

GENUS must never confuse observation, evidence, belief, report, decision, or action.

The first stable GENUS core exists to enforce this principle.

## 3. Primitive 1: WorldEvent

### Definition

A `WorldEvent` is a raw external or internal occurrence before GENUS interprets it.

### Meaning

It is the raw occasion that may be observed.

### It is

- raw
- uninterpreted
- unvalidated
- not evidence
- not belief
- not truth
- not action

### It is not

- an Observation
- an EvidenceRecord
- a BeliefStateSnapshot
- a decision
- a reaction
- a memory write

### Required fields

```text
event_id
event_type
raw_text optional
payload_json optional
created_at
schema_version
```

### Example

```json
{
  "schema_version": "genus.foundation.v0.0.1",
  "event_id": "evt_001",
  "event_type": "user_text",
  "raw_text": "merk dir das: larumipsum",
  "payload_json": {},
  "created_at": "2026-05-24T12:00:00Z"
}
```

## 4. Primitive 2: Observation

### Definition

An `Observation` is a structured perception of a `WorldEvent` by GENUS.

### Meaning

Observation is the first true GENUS act.

GENUS does not own the world. GENUS observes events.

### It is

- structured perception
- classified
- scoped
- confidence-marked
- derived from a WorldEvent

### It is not

- evidence
- truth
- belief
- memory
- decision
- action

### Required fields

```text
observation_id
source_event_id
observation_type
scope
confidence
payload_json
created_at
schema_version
```

### Example

```json
{
  "schema_version": "genus.foundation.v0.0.1",
  "observation_id": "obs_001",
  "source_event_id": "evt_001",
  "observation_type": "memory_request_observed",
  "scope": "memory",
  "confidence": "high",
  "payload_json": {
    "observed_memory_content": "larumipsum"
  },
  "created_at": "2026-05-24T12:00:01Z"
}
```

## 5. Primitive 3: EvidenceRecord

### Definition

An `EvidenceRecord` is a stored and provenance-marked record of an Observation.

### Meaning

Evidence does not claim absolute world truth.

It says:

```text
GENUS stored that this observation occurred.
```

### It is

- persistent
- provenance-aware
- truth-status-marked
- traceable to an Observation

### It is not

- the world
- a belief state
- a report
- a decision
- an action

### Required fields

```text
evidence_id
source_observation_id
truth_status
provenance
payload_json
created_at
schema_version
```

### Allowed truth_status values

```text
observed
derived
rejected
```

### Example

```json
{
  "schema_version": "genus.foundation.v0.0.1",
  "evidence_id": "ev_001",
  "source_observation_id": "obs_001",
  "truth_status": "observed",
  "provenance": "user_input",
  "payload_json": {
    "note": "User text was observed and classified as memory request."
  },
  "created_at": "2026-05-24T12:00:02Z"
}
```

## 6. Primitive 4: LedgerEntry

### Definition

A `LedgerEntry` is an append-only historical trace of how a GENUS artifact was created, linked, or recorded.

### Meaning

The Ledger proves lineage and sequence.

It does not prove that the content itself is world-true.

### It is

- append-only
- ordered
- historical
- chain-aware
- audit-oriented

### It is not

- Evidence
- Belief
- Truth
- Decision
- Action

### Required fields

```text
ledger_id
chain_id
step
event_type
source_kind
source_id
target_kind optional
target_id optional
payload_json optional
created_at
schema_version
```

### Required invariant

```text
UNIQUE(chain_id, step)
```

### Hardened after v0.1.7 / v0.1.9

This document preserves the historical v0.0.1 foundation wording. In the active
v0.1.7+ hardened Ledger flow, `target_kind` and `target_id` are required for
LedgerEntry creation and persistence. Earlier optional wording is historical
and must not be read as the active runtime contract.

### Example

```json
{
  "schema_version": "genus.foundation.v0.0.1",
  "ledger_id": "led_001",
  "chain_id": "chain_001",
  "step": 1,
  "event_type": "evidence_record_created",
  "source_kind": "observation",
  "source_id": "obs_001",
  "target_kind": "evidence_record",
  "target_id": "ev_001",
  "payload_json": {},
  "created_at": "2026-05-24T12:00:03Z"
}
```

## 7. Primitive 5: BeliefStateSnapshot

### Definition

A `BeliefStateSnapshot` is a time-bound internal state derived from EvidenceRecords.

### Meaning

Belief is not absolute truth.

Belief is GENUS' current internal derivation from stored evidence.

### It is

- derived
- scoped
- time-bound
- evidence-referenced
- inspectable

### It is not

- the world
- an Observation
- an EvidenceRecord
- a report
- a decision
- an action

### Required fields

```text
state_id
scope
source_evidence_ids_json
payload_json
created_at
schema_version
```

### Required invariant

A BeliefStateSnapshot must reference at least one EvidenceRecord.

### Example

```json
{
  "schema_version": "genus.foundation.v0.0.1",
  "state_id": "state_001",
  "scope": "memory",
  "source_evidence_ids_json": ["ev_001"],
  "payload_json": {
    "observed_memory_request": true,
    "observed_memory_content": "larumipsum"
  },
  "created_at": "2026-05-24T12:00:04Z"
}
```

## 8. Primitive 6: ObservationReport

### Definition

An `ObservationReport` is an explanation of what GENUS observed, stored as evidence, and derived as belief.

### Meaning

The Report explains.

It does not decide, approve, execute, write memory, create reactions, or activate capabilities.

### It is

- explanatory
- inspectable
- report-only
- human-readable
- linked to a BeliefStateSnapshot

### It is not

- a decision
- approval
- action
- reaction
- memory write
- evidence

### Required fields

```text
report_id
source_state_id
summary
payload_json
created_at
schema_version
```

### Example

```json
{
  "schema_version": "genus.foundation.v0.0.1",
  "report_id": "rep_001",
  "source_state_id": "state_001",
  "summary": "A memory request was observed and recorded. This version cannot write memory.",
  "payload_json": {
    "no_action_possible": true
  },
  "created_at": "2026-05-24T12:00:05Z"
}
```

## 9. v0.0.1 Pipeline

```text
WorldEvent
→ Observation
→ EvidenceRecord
→ LedgerEntry
→ BeliefStateSnapshot
→ ObservationReport
```

No other GENUS object is allowed in v0.0.1.

## 10. Required Invariants

```text
WorldEvent ≠ Observation
Observation ≠ EvidenceRecord
EvidenceRecord ≠ BeliefStateSnapshot
BeliefStateSnapshot ≠ World
LedgerEntry ≠ Truth
ObservationReport ≠ Decision
ObservationReport ≠ Action
```

## 11. Explicitly Out of Scope

The following must not exist in v0.0.1:

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

## 12. First Smoke Scenario

Input:

```text
merk dir das: larumipsum
```

Expected artifacts:

```text
WorldEvent
Observation(memory_request_observed)
EvidenceRecord(observed)
LedgerEntry
BeliefStateSnapshot(observed_memory_request=true)
ObservationReport(no_action_possible=true)
```

Forbidden artifacts:

```text
MemoryWrite
MemoryObject
PhysicsMetric
TransitionCandidate
ConstraintDecision
ReactionExecution
```

## 13. Acceptance Criteria

v0.0.1 is accepted only if:

```text
All core terms are defined.
All invariants are tested.
SQLite persists EvidenceRecord and LedgerEntry.
Ledger is append-only.
BeliefStateSnapshot requires EvidenceRecord IDs.
ObservationReport contains no decision field.
No forbidden artifacts exist.
CLI smoke scenario passes.
```
