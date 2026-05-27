# GENUS_CORE Vocabulary v0.0.1

Status: draft for foundation freeze

## WorldEvent

A raw external or internal occurrence before GENUS interprets it.

It is not Observation, Evidence, Belief, Decision, Action, Memory, or Reaction.

Allowed in: v0.0.1

## Observation

A structured perception of a WorldEvent by GENUS.

It is the first true GENUS act.

It is not Evidence, Truth, Belief, Decision, Action, or Memory.

Allowed in: v0.0.1

## EvidenceRecord

A stored and provenance-marked record of an Observation.

It says that GENUS has stored an observation with provenance and truth status.

It is not absolute world truth and not Belief.

Allowed in: v0.0.1

## LedgerEntry

An append-only historical trace of how an artifact was created, linked, or recorded.

It proves lineage and sequence.

It does not prove content truth.

Allowed in: v0.0.1

## BeliefStateSnapshot

A scoped, time-bound internal state derived from EvidenceRecords.

It is GENUS' current internal view derived from evidence.

It is not the world and not Evidence.

Allowed in: v0.0.1

## ObservationReport

A human-readable explanation of what was observed, stored as evidence, and derived as belief.

It explains.

It does not decide, approve, execute, react, or write memory.

Allowed in: v0.0.1

## TruthStatus

A controlled enum describing the status of an EvidenceRecord.

Allowed values:

```text
observed
derived
rejected
```

Allowed in: v0.0.1

For `EvidenceRecord`, `truth_status = observed` means GENUS recorded the source
Observation. It does not mean the observed content is world-true, believed,
action-ready, or memory-worthy.

## Provenance

A controlled enum describing where an EvidenceRecord came from.

Allowed values:

```text
user_input
system_event
runtime_probe
manual_entry
```

It is not a trust score, belief, decision, action, or proof of world truth.

Allowed in: v0.0.5

## Confidence

A controlled enum describing observation confidence.

Allowed values:

```text
low
medium
high
```

Allowed in: v0.0.1

## Scope

A controlled category describing the area a GENUS object refers to.

Initial allowed values:

```text
input
memory
system
worker
```

Allowed in: v0.0.1

## ReactionExecution

A future concept meaning an actual system action.

It is explicitly forbidden in v0.0.1.

## MemoryWrite

A future concept meaning writing memory.

It is explicitly forbidden in v0.0.1.

## PhysicsMetric

A future concept for measuring pressure, stability, inhibition, cost, or potential.

It is explicitly forbidden in v0.0.1.

## TransitionCandidate

A future concept for possible state change.

It is explicitly forbidden in v0.0.1.

## ConstraintDecision

A future concept for deciding whether a candidate transition is allowed, blocked, or preview-only.

It is explicitly forbidden in v0.0.1.

## Reaction

A future concept for a system response.

It is not Observation, Evidence, Belief, Ledger, Report, or an allowed v0.0.1
capability. It is explicitly forbidden in v0.0.1.

## CognitiveStateMap

A future concept for mapping cognitive state.

It is not BeliefStateSnapshot and is explicitly forbidden in v0.0.1.

## MemoryObject

A future concept for stored memory content.

It is not EvidenceRecord and is explicitly forbidden in v0.0.1.

## Worker

A future concept for execution responsibility.

It is not a foundation function and is explicitly forbidden in v0.0.1.

## RuntimeCell

A future concept for runtime structure.

It is not a v0.0.1 model and is explicitly forbidden in v0.0.1.

## Organ

A future concept for grouped capability.

It is not a v0.0.1 module or capability and is explicitly forbidden in v0.0.1.

## Agent

A future concept for autonomous behavior.

It is not CLI composition and is explicitly forbidden in v0.0.1.

## LLM

A future concept for language model use.

It is not observation, evidence, belief, report, or truth storage and is
explicitly forbidden in v0.0.1.

## memory_request_observed

An Observation type for user text that explicitly starts with `merk dir das:`
and contains memory candidate content.

It is not Evidence, Belief, MemoryWrite, Decision, or Action.

Scope: `memory`

Confidence expectation: `high`

Example: `merk dir das: larumipsum`

## memory_lookup_failure_observed

An Observation type for a `memory_lookup_failed` WorldEvent.

It is not Evidence, Belief, MemoryObject, MemoryWrite, Decision, or Action.

Scope: `memory`

Confidence expectation: `high`

Example: a WorldEvent with `event_type = "memory_lookup_failed"`.

## guard_block_observed

An Observation type for a `guard_blocked_transition` WorldEvent.

It is not ConstraintDecision, TransitionCandidate, Reaction, Decision, or Action.

Scope: `system`

Confidence expectation: `high`

Example: a WorldEvent with `event_type = "guard_blocked_transition"`.

## unknown_input_observed

An Observation type for empty user text or unsupported WorldEvent types.

It is not Meaning, Intent, Evidence, Belief, Decision, or Action.

Scope: `input`

Confidence expectation: `low`

Example: an unsupported WorldEvent with `event_type = "unrecognized_event"`.

## ambiguous_input_observed

An Observation type for input that resembles a known observation pattern but is
missing required content.

It is not MeaningCandidate, Intent, Evidence, Belief, Decision, or Action.

Scope: `memory`

Confidence expectation: `medium`

Example: `merk dir das:`

## LedgerEventType

A controlled enum describing why a LedgerEntry exists.

Allowed values in v0.0.6:

```text
evidence_record_created
```

It is not a truth claim, belief, decision, action, reaction, transition, or
physics measurement.

## LedgerSourceKind

A controlled enum describing the source artifact kind for the current Ledger
lineage event.

Allowed values in v0.0.6:

```text
observation
```

It is not `ledger_entry`, world truth, belief, decision, action, reaction,
transition, or memory write.

## LedgerTargetKind

A controlled enum describing the target artifact kind for the current Ledger
lineage event.

Allowed values in v0.0.6:

```text
evidence_record
```

It is not `ledger_entry`, belief, report, decision, action, reaction,
transition, or memory write.
