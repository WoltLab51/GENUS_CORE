# GENUS_CORE Status

Current target: `v0.0.6 - Ledger Minimal Lineage Hardening`

Status: implemented after v0.0.5 release freeze

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

`GENUS_CORE v0.0.4 - Observation Classification Hardening` is released and frozen at:

```text
Tag: genus-core-v0.0.4-observation-classification-hardening
Commit: 139ee05e1c6f5a02c430fdce3352fd931f80052f
```

`GENUS_CORE v0.0.5 - Evidence Boundary Hardening` is released and frozen at:

```text
Tag: genus-core-v0.0.5-evidence-boundary-hardening
Commit: 1cde6bccaed6c27290284762a5f05b9dd7a1aaad
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

`GENUS_CORE v0.0.6` is Ledger Minimal Lineage Hardening.

It adds no generic lineage model and no new product scope. It only constrains
the current real Ledger flow:

```text
Observation -> EvidenceRecord
event_type = evidence_record_created
```

The package version is `0.0.6`, while `SCHEMA_VERSION` remains
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
Package version is 0.0.6
SCHEMA_VERSION remains genus.foundation.v0.0.1
Ledger event_type is only evidence_record_created
Ledger source_kind is only observation
Ledger target_kind is only evidence_record
LedgerEntry is not source_kind or target_kind
Ledger remains append-only
Forbidden v0.1+ artifacts do not exist
No product scope expansion exists in v0.0.6
```
