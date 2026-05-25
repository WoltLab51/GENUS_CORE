# GENUS_CORE Quality Gates

Status: draft for foundation freeze

## 1. Purpose

Quality Gates define the conditions that must be met before a GENUS_CORE phase can be accepted.

GENUS must not grow by enthusiasm alone.

Every phase must pass documentation, test, architecture, and safety checks.

## 2. Universal Quality Gate

Every GENUS_CORE phase must pass:

```text
pytest green
CLI smoke test green
all new terms documented
all new invariants tested
STATUS.md updated
DECISIONS.md updated when architecture changed
SAFETY_BOUNDARIES.md updated when power changed
no forbidden artifacts introduced
```

## 3. v0.0.1 Quality Gate

`v0.0.1 — Observation Truth Seed` is accepted only if:

```text
WorldEvent exists.
Observation exists.
EvidenceRecord exists.
LedgerEntry exists.
BeliefStateSnapshot exists.
ObservationReport exists.

WorldEvent is not treated as Observation.
Observation is not treated as Evidence.
Evidence is not treated as Belief.
Belief is not treated as World Truth.
Ledger is not treated as Truth.
Report is not treated as Decision.
Report is not treated as Action.
```

## 4. v0.0.1 Technical Gate

```text
SQLite persists EvidenceRecord.
SQLite persists LedgerEntry.
Ledger has UNIQUE(chain_id, step).
BeliefStateSnapshot requires Evidence IDs.
ObservationReport has no decision field.
No ReactionExecution class exists.
No MemoryWrite class exists.
No PhysicsMetric class exists.
No TransitionCandidate class exists.
No ConstraintDecision class exists.
```

## 5. v0.0.1 Test Gate

Required tests:

```text
test_world_event_is_not_observation
test_observation_is_not_evidence
test_evidence_is_not_belief
test_ledger_is_append_only
test_belief_requires_evidence
test_report_has_no_decision_power
test_no_reaction_execution_exists
test_no_memory_write_exists
test_language_rejects_unknown_sentence_type
```

## 6. v0.0.1 Smoke Gate

The following command or equivalent must pass:

```text
genus-core observe "merk dir das: larumipsum"
```

Expected output must include:

```text
Observation created
EvidenceRecord created
LedgerEntry appended
BeliefStateSnapshot created
ObservationReport created
No action possible
```

Expected output must not include:

```text
Memory written
Reaction executed
Transition allowed
Constraint decided
```

## 7. Stop Gate

Stop development if any of these occur:

```text
Observation directly creates Belief.
Report contains action fields.
Ledger is used as content truth.
BeliefStateSnapshot has no Evidence references.
A forbidden artifact appears in v0.0.1.
CLI contains hidden business logic.
A new term appears without vocabulary entry.
```

## 8. Architecture Review Result Format

Each phase review must output:

```text
Philosophy-Fit: green/yellow/red
Governance-Fit: green/yellow/red
Function-Granularity-Fit: green/yellow/red
Overengineering-Risk: low/medium/high
Documentation-Drift-Risk: low/medium/high
Decision: accept/harden/stop
```
