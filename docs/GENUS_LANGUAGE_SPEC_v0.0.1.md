# GENUS Language Spec v0.0.1

Status: draft for foundation freeze  
Scope: minimal internal language for `GENUS_CORE v0.0.1`

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
```

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
system_log
runtime_probe
manual_entry
```

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

Required invariant:

```text
(chain_id, step) must be unique.
```

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

## 10. REPORT

A REPORT sentence records an explanation.

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
```

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
