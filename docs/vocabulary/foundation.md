# GENUS_CORE Vocabulary - Foundation
Status: active for v0.3.6 Vocabulary Modularization
Vocabulary blocks moved verbatim from `docs/VOCABULARY.md`.

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

In v0.0.7, BeliefStateSnapshot is derived only from observed EvidenceRecords.
It preserves source EvidenceRecord IDs in `source_evidence_ids_json`, rejects
mixed evidence scopes, and does not contain generic `evidence`, truth, decision,
approval, constraint, action, reaction, memory-write, execution, or generic
candidate fields in its payload.

Allowed in: v0.0.1

## observed_memory_request

A Belief payload field indicating that observed Evidence supports the internal
state "a memory request was observed".

It may only be true when at least one source EvidenceRecord has
`observed_observation_type = memory_request_observed`.

It is not a queue, MemoryWrite, approval, action, decision, reaction, or
guarantee that memory will be stored.

Allowed in: v0.1.9

## observed_memory_content

A passive Observation, Belief, or Report payload field containing text observed
after the `merk dir das:` prefix.

It is not selected content, approved content, a MemoryObject, or a memory write.

Allowed in: v0.1.9

## source_evidence_ids_json

The required top-level BeliefStateSnapshot field that references all source
EvidenceRecord IDs used for derivation.

It is not the forbidden generic payload key `evidence`; it is the allowed
lineage reference field.

Allowed in: v0.0.1

## ObservationReport

A human-readable explanation of a BeliefStateSnapshot.

It explains the current derived Belief and may include safe lineage references.

It does not decide, approve, execute, react, write memory, create truth, create
Belief, create Evidence, append Ledger, transition, constrain, or measure
physics.

Allowed in: v0.0.1

## source_state_id

The required ObservationReport field referencing the BeliefStateSnapshot being
explained.

It is not a decision target, action target, approval target, memory target, or
new truth claim.

Allowed in: v0.0.1

## report payload

The structured ObservationReport payload containing only descriptive metadata
and safe lineage references.

It may include `no_action_possible`, `observed_memory_request`,
`observed_memory_content`, and `source_evidence_ids` when those are descriptive.

It must not contain decision, action, execute, approval, reaction, memory_write,
memory, memory_object, constraint, transition, candidate, physics, metric,
truth, truth_status, world_truth, evidence_claim, policy, allow, block,
approved, or rejected_by_policy fields.

Allowed in: v0.0.8

## descriptive-only report

An ObservationReport that explains Belief without granting permission, choosing
an action, writing memory, creating a reaction, or asserting world truth.

It is not a hidden control surface.

Allowed in: v0.0.8

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

`worker` is only a passive scope label for an observed source area. It is not a
`Worker` object, runtime, execution surface, or capability.

Allowed in: v0.0.1

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
