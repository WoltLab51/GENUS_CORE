# GENUS_CORE Status

Current target: `v0.0.4 - Observation Classification Hardening`

Status: implemented after v0.0.3 release freeze

## Released baselines

`GENUS_CORE v0.0.1 - Observation Truth Seed` is released and frozen at:

```text
Tag: genus-core-v0.0.1-observation-truth-seed
Commit: 3cbb2d4416d4011bf53a9af9ead63932cf0be408
```

`GENUS_CORE v0.0.2 - Foundation Hardening` is released and frozen at:

```text
Tag: genus-core-v0.0.2-foundation-hardening
Commit: 44c4dfac04e83455d489d4961ac656f7884e48d8
```

`GENUS_CORE v0.0.3 - Minimal Language Hardening` is released and frozen at:

```text
Tag: genus-core-v0.0.3-minimal-language-hardening
Commit: ebed5c31bfbbfb112cefcace6c684d7dbee0a107
```

The only active epistemic chain remains:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

## Current implementation state

`GENUS_CORE v0.0.4` is Observation Classification Hardening.

It adds no action, memory, physics, transition, reaction, agent, LLM, or schema
expansion. It only hardens deterministic classification from WorldEvent to
Observation.

The package version is `0.0.4`, while `SCHEMA_VERSION` remains
`genus.foundation.v0.0.1`.

## Explicitly not active

```text
PhysicsMetric
CognitiveStateMap
TransitionCandidate
ConstraintDecision
Reaction
ReactionExecution
MemoryWrite
MemoryObject
LLM
Worker
RuntimeCell
Organ
Agent
Character
Autonomy
Mutation
Evolution
GraphDB
RuntimeShape
```

## Acceptance state

The implementation is accepted only while these remain true:

```text
pytest is green
CLI smoke test is green
Package version is 0.0.4
SCHEMA_VERSION remains genus.foundation.v0.0.1
Observation classification remains deterministic and side-effect free
Unsupported events become unknown_input_observed
Incomplete memory requests become ambiguous_input_observed
Forbidden v0.1+ artifacts do not exist
No product scope expansion exists in v0.0.4
```
