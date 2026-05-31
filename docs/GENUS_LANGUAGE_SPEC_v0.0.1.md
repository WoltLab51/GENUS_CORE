# GENUS Language Spec v0.0.1

Status: frozen historical reference; active contracts live in current governance docs
Scope: minimal internal language for `GENUS_CORE v0.0.1`

Boundary note: this document preserves historical v0.0.1 language wording.
It must not override `GENUS_CHARTER.md`, `SAFETY_BOUNDARIES.md`,
`ARTIFACT_CONTRACTS.md`, `BUILD_RULES.md`, `QUALITY_GATES.md`,
`DECISIONS.md`, `VOCABULARY.md`, or `STATUS.md`.

## 1. Purpose

GENUS needs an internal language so that raw human text does not directly become belief, action, memory, or capability.

The language is not a natural language and not a programming language.

It is a small, controlled meaning language for representing GENUS artifacts.

## 2. Design Goals

The GENUS internal language must be:

```text
small
versioned
schema-based
explicit
non-poetic
non-agentic
non-executing
```

It must prevent free invention of concepts by code or models.

## 3. Allowed Sentence Types in v0.0.1

Only these sentence types exist:

```text
WORLD_EVENT
OBSERVATION
EVIDENCE
LEDGER
BELIEF
REPORT
```

No other sentence type is allowed in v0.0.1.

In `GENUS_CORE v0.0.3`, this allowed set is centralized in code as the minimal
foundation language:

```text
WORLD_EVENT
OBSERVATION
EVIDENCE
LEDGER
BELIEF
REPORT
```

Unknown sentence types must be rejected.

v0.0.3 does not change the schema version. `schema_version` remains:

```text
genus.foundation.v0.0.1
```

## 4. Required Common Fields

Every GENUS language object must include:

```text
schema_version
id
created_at
```

Where `schema_version` must be:

```text
genus.foundation.v0.0.1
```

## 5. WORLD_EVENT

A WORLD_EVENT sentence records a raw event.

Required fields:

```text
schema_version
id
event_type
raw_text optional
payload_json optional
created_at
```

Allowed event_type examples:

```text
user_text
system_event
memory_lookup_failed
guard_blocked_transition
```

## 6. OBSERVATION

An OBSERVATION sentence records structured perception.

Required fields:

```text
schema_version
id
source_event_id
observation_type
scope
confidence
payload_json
created_at
```

Allowed confidence values:

```text
low
medium
high
```

Allowed initial scopes:

```text
input
memory
system
worker
```

Allowed initial observation_type examples:

```text
memory_request_observed
memory_lookup_failure_observed
guard_block_observed
unknown_input_observed
ambiguous_input_observed
```

In `GENUS_CORE v0.0.4`, these are the only allowed observation classifications:

```text
memory_request_observed
memory_lookup_failure_observed
guard_block_observed
unknown_input_observed
ambiguous_input_observed
```

Observation classification is deterministic and non-agentic. It does not create
Evidence, Belief, decisions, actions, memory writes, reactions, MeaningCandidate,
Intent, parser objects, LLM calls, or execution paths.

## 7. EVIDENCE

An EVIDENCE sentence records stored observation evidence.

Required fields:

```text
schema_version
id
source_observation_id
truth_status
provenance
payload_json
created_at
```

Allowed truth_status values:

```text
observed
derived
rejected
```

Allowed provenance examples:

```text
user_input
system_event
runtime_probe
manual_entry
```

In `GENUS_CORE v0.0.5`, provenance is constrained to:

```text
user_input
system_event
runtime_probe
manual_entry
```

An EVIDENCE sentence claims that GENUS recorded an Observation. It does not
claim that the observed content is world-true, believed, action-ready, or
memory-worthy.

## 8. LEDGER

A LEDGER sentence records lineage and sequence.

Required fields:

```text
schema_version
id
chain_id
step
event_type
source_kind
source_id
target_kind optional
target_id optional
payload_json optional
created_at
```

Hardened after v0.1.7 / v0.1.9:

```text
The v0.0.1 wording above is historical.
The active v0.1.7+ LedgerEntry flow requires target_kind and target_id.
Current runtime behavior is governed by the hardened docs and tests.
```

Required invariant:

```text
(chain_id, step) must be unique.
```

In `GENUS_CORE v0.0.6`, Ledger is limited to the current real flow:

```text
event_type = evidence_record_created
source_kind = observation
target_kind = evidence_record
```

`ledger_entry` is not an allowed source or target kind. Ledger proves lineage
and sequence only; it does not prove truth, derive belief, decide, act, react,
write memory, model transitions, or measure physics.

## 9. BELIEF

A BELIEF sentence records an internal derived state.

Required fields:

```text
schema_version
id
scope
source_evidence_ids_json
payload_json
created_at
```

Required invariant:

```text
source_evidence_ids_json must contain at least one EvidenceRecord id.
```

In `GENUS_CORE v0.0.7`, BELIEF derivation is limited to observed EvidenceRecords:

```text
truth_status = observed
evidence_claim = observation_recorded
observed_observation_type must be supported
observation_scope is required
mixed scopes are rejected
all source EvidenceRecord IDs are preserved in input order
```

The BELIEF payload may include `observed_memory_request` and
`observed_memory_content` for observed memory requests. It must not include
generic `evidence`, truth, truth_status, decision, approval, action, reaction,
constraint, transition, physics, memory_write, execute, or generic `candidate`
fields.

## 10. REPORT

A REPORT sentence records a descriptive-only explanation of a BeliefStateSnapshot.

Required fields:

```text
schema_version
id
source_state_id
summary
payload_json
created_at
```

Forbidden fields in REPORT:

```text
decision
action
execute
approval
reaction
memory_write
memory
memory_object
constraint
transition
candidate
physics
metric
truth
truth_status
world_truth
evidence_claim
policy
allow
block
approved
rejected_by_policy
```

In `GENUS_CORE v0.0.8`, REPORT may explain `source_state_id`, safe source
evidence lineage, and passive observed memory-request fields. In the active
v0.1.9 boundary naming cleanup, those fields are `observed_memory_request` and
optional `observed_memory_content`. REPORT must not decide, approve, execute,
react, write memory, create new truth, create new belief, trigger transitions,
apply constraints, or measure physics. No new sentence types are introduced.

## 11. Forbidden Language in v0.0.1

The language must not include:

```text
ACTION
REACTION
EXECUTION
MEMORY_WRITE
PHYSICS
MAP
TRANSITION
CONSTRAINT
AGENT
WORKER
CELL
ORGAN
```

## 12. Rule for New Terms

A new language term can be added only if:

```text
1. It is defined in VOCABULARY.md.
2. It is added to this language spec.
3. It has a schema.
4. It has tests.
5. It does not bypass safety boundaries.
6. It has a DECISIONS.md entry.
```
