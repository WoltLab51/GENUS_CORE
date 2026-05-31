# GENUS_CORE Roadmap - Foundation
Status: active for v0.4.0 Passive Boundary Relevance Spec
Moved from `docs/ROADMAP_STABLE_CORE.md`.

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
