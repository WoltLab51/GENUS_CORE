# GENUS_CORE v0.1.0 Release Notes

Release: Full Epistemic Core Freeze

## Summary

`GENUS_CORE v0.1.0` freezes the passive epistemic foundation:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

This is a freeze release, not a feature expansion.

## Release Path

```text
v0.0.1 Observation Truth Seed
v0.0.2 Foundation Hardening
v0.0.3 Minimal Language Hardening
v0.0.4 Observation Classification Hardening
v0.0.5 Evidence Boundary Hardening
v0.0.6 Ledger Minimal Lineage Hardening
v0.0.7 Belief Derivation Hardening
v0.0.8 Report Boundary Hardening
v0.0.9 Foundation Freeze Readiness Audit
v0.1.0 Full Epistemic Core Freeze
```

## Frozen Interfaces

The public foundation functions remain:

```text
observe_event()
create_evidence_record()
append_ledger_entry()
build_belief_state_snapshot()
create_observation_report()
```

The allowed sentence types remain:

```text
WORLD_EVENT
OBSERVATION
EVIDENCE
LEDGER
BELIEF
REPORT
```

## Version And Schema

```text
Package version: 0.1.0
SCHEMA_VERSION: genus.foundation.v0.0.1
```

`SCHEMA_VERSION` remains unchanged because v0.1.0 does not introduce a new data
schema or product capability.

## Acceptance Evidence

v0.1.0 is accepted only when:

```text
pytest is green
CLI smoke test is green
public foundation functions are unchanged
allowed sentence types are unchanged
forbidden future artifacts are absent
README, STATUS, ROADMAP, DECISIONS, QUALITY_GATES, and release notes are updated
no product scope expansion exists
```

## Explicit Non-Scope

v0.1.0 does not introduce:

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

Future work may plan passive cognitive physics only after this foundation
baseline remains accepted.
