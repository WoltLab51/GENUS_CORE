# Codex Implementation Prompt — GENUS_CORE v0.0.1

Use this prompt only after foundation documentation has been reviewed and accepted.

---

You are working in the repository:

```text
https://github.com/WoltLab51/GENUS_CORE
```

Build exactly:

```text
GENUS_CORE v0.0.1 — Observation Truth Seed
```

Do not build v0.1 full cognitive physics.

## Goal

Implement the smallest GENUS core:

```text
WorldEvent
→ Observation
→ EvidenceRecord
→ LedgerEntry
→ BeliefStateSnapshot
→ ObservationReport
```

This version proves only:

```text
Observation ≠ Evidence ≠ Belief
Ledger ≠ Truth
Report ≠ Decision
Report ≠ Action
```

## Forbidden in v0.0.1

Do not implement:

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

## Required project structure

```text
GENUS_CORE/
├── pyproject.toml
├── README.md
├── docs/
│   ├── FOUNDATION_SPEC_v0.0.1.md
│   ├── GENUS_LANGUAGE_SPEC_v0.0.1.md
│   ├── QUALITY_GATES.md
│   ├── BUILD_RULES.md
│   ├── VOCABULARY.md
│   ├── DECISIONS.md
│   ├── STATUS.md
│   └── ROADMAP_STABLE_CORE.md
│
├── src/
│   └── genus_core/
│       ├── __init__.py
│       ├── ids.py
│       ├── time.py
│       ├── cli.py
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   ├── world_event.py
│       │   ├── observation.py
│       │   ├── evidence_record.py
│       │   ├── ledger_entry.py
│       │   ├── belief_state_snapshot.py
│       │   └── observation_report.py
│       │
│       ├── functions/
│       │   ├── __init__.py
│       │   ├── observe_event.py
│       │   ├── create_evidence_record.py
│       │   ├── append_ledger_entry.py
│       │   ├── build_belief_state_snapshot.py
│       │   └── create_observation_report.py
│       │
│       └── truth/
│           ├── __init__.py
│           ├── sqlite_store.py
│           └── ledger.py
│
└── tests/
    ├── test_world_event_is_not_observation.py
    ├── test_observation_is_not_evidence.py
    ├── test_evidence_is_not_belief.py
    ├── test_ledger_is_append_only.py
    ├── test_belief_requires_evidence.py
    ├── test_report_has_no_decision_power.py
    ├── test_no_reaction_execution_exists.py
    ├── test_no_memory_write_exists.py
    └── test_language_rejects_unknown_sentence_type.py
```

## Required models

Implement dataclasses or pydantic-free plain Python models for:

```text
WorldEvent
Observation
EvidenceRecord
LedgerEntry
BeliefStateSnapshot
ObservationReport
```

Each model must include:

```text
schema_version
id field
created_at
```

Use stable prefixes:

```text
evt_
obs_
ev_
led_
state_
rep_
chain_
```

## Required functions

```text
observe_event(world_event) -> Observation
create_evidence_record(observation) -> EvidenceRecord
append_ledger_entry(...) -> LedgerEntry
build_belief_state_snapshot(evidence_records) -> BeliefStateSnapshot
create_observation_report(belief_state_snapshot) -> ObservationReport
```

Functions must be small and responsibility-focused.

No large manager classes.

No agent loop.

No hidden side effects.

## SQLite requirements

SQLite must persist:

```text
observations optional
evidence_records
ledger_entries
belief_state_snapshots optional
observation_reports optional
```

At minimum, evidence and ledger must persist.

Ledger must enforce:

```text
UNIQUE(chain_id, step)
```

Allowed enum checks:

```text
truth_status IN ('observed', 'derived', 'rejected')
confidence IN ('low', 'medium', 'high')
```

## CLI requirements

Implement:

```text
genus-core observe "merk dir das: larumipsum"
```

Equivalent module invocation is acceptable:

```text
python -m genus_core.cli observe "merk dir das: larumipsum"
```

Expected CLI output must include:

```text
Observation created
EvidenceRecord created
LedgerEntry appended
BeliefStateSnapshot created
ObservationReport created
No action possible in v0.0.1
```

## Required tests

All tests must prove the core invariants:

```text
WorldEvent is not Observation.
Observation is not Evidence.
Evidence is not Belief.
Ledger is append-only.
Belief requires Evidence IDs.
Report has no decision/action fields.
No ReactionExecution exists.
No MemoryWrite exists.
Unknown language sentence type is rejected.
```

## Documentation requirements

Keep the included docs.

Update `STATUS.md` after implementation.

Update `DECISIONS.md` if any scope decision changes.

Do not introduce new terms without updating `VOCABULARY.md`.

## Final report after implementation

Report:

```text
1. Files created
2. Functions implemented
3. Models implemented
4. SQLite tables created
5. Tests added
6. Test results
7. Invariants enforced
8. Explicitly not built
```

Commit message:

```text
Implement GENUS_CORE v0.0.1 observation truth seed
```
