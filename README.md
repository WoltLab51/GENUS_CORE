# GENUS_CORE

[![CI](https://github.com/WoltLab51/GENUS_CORE/actions/workflows/ci.yml/badge.svg)](https://github.com/WoltLab51/GENUS_CORE/actions/workflows/ci.yml)

`GENUS_CORE v0.3.6` is Vocabulary Modularization.

It keeps the `v0.1.0` passive foundation frozen:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

This release modularizes vocabulary without adding runtime capability. It keeps
code, tests, docs, specs, decisions, quality gates, vocabulary, and artifact
lineage governed while
keeping agents, workers, LLM calls, memory writes, reactions, decisions,
cognitive maps, transition candidates, constraint decisions, runtime cells,
organs, and GraphDB truth out of scope.

## Version and Boundary

Package version: `0.3.6`

Foundation schema version: `genus.foundation.v0.0.1`

Capability boundary: passive foundation plus passive Physics plus passive
transition preview only

Passive Physics in v0.2.x is a narrow passive metric description layer. It is
not dynamic physics, simulation, transition physics, constraint decision,
reaction, recommendation, prioritization, permission, or action.

Passive Transition Preview in v0.3.0 is a narrow descriptive question layer. It
is not a `TransitionCandidate`, `ConstraintDecision`, recommendation,
permission, priority, approval, reaction, memory write, or action.
v0.3.1 adds no capability; it hardens summary wording and neutralizes the
memory-tension question.
v0.3.2 adds no runtime capability; it adds build-structure guardrails for
governed artifacts.
v0.3.3 adds no runtime capability; it turns `QUALITY_GATES.md` into an index
and moves historical gate content into `docs/quality_gates/`.
v0.3.4 adds no runtime capability; it documents ID, source-lineage,
evidence-lineage, snapshot/preview/report, durable/ephemeral, and report
boundary contracts in `docs/ARTIFACT_CONTRACTS.md`.
v0.3.5 adds no runtime capability; it turns `DECISIONS.md` into an active index
and moves decision blocks into `docs/decisions/`.
v0.3.6 adds no runtime capability; it turns `VOCABULARY.md` into an active
index and moves vocabulary blocks into `docs/vocabulary/`.

Planned v0.4.0 work is spec-only: Passive Boundary Relevance may describe how a
later passive boundary relevance description is allowed to look. It must not
evaluate boundaries, grant permission, produce policy results, allow/block,
decide, react, write memory, or add runtime code.

Governance documents:

- `docs/GENUS_CHARTER.md`
- `docs/SAFETY_BOUNDARIES.md`
- `docs/ARTIFACT_CONTRACTS.md`

Durable truth layer:

- EvidenceRecord
- LedgerEntry

Ephemeral derivation:

- WorldEvent
- Observation
- BeliefStateSnapshot
- ObservationReport
- PassiveMetricSnapshot
- PassiveMetricReport
- PassiveTransitionPreview
- PassiveTransitionReport

## Install

Use Python 3.12 or a compatible newer Python.

```bash
python -m pip install -e ".[dev]"
```

## Run Tests

```bash
python -m pytest
```

## CLI Smoke Test

```bash
python -m genus_core.cli observe "merk dir das: larumipsum"
```

Expected output includes:

```text
WorldEvent created
Observation created
EvidenceRecord created
LedgerEntry appended
BeliefStateSnapshot created
ObservationReport created
No action is possible under the passive foundation boundary.
```

The CLI stores EvidenceRecord and LedgerEntry rows in SQLite. By default it uses
`.genus_core_truth.sqlite3`, which is ignored by Git.

## Stable Foundation Boundary

`ObservationReport` explains what was observed, recorded, and derived in the
foundation chain. It does not decide, approve, execute, react, write memory,
create truth, transition, constrain, or measure physics.

`PassiveMetricReport` describes passive metric outputs only. It does not
decide, approve, execute, recommend, prioritize, permit, transition, constrain,
react, or write memory.

`PassiveTransitionReport` describes a passive preview question only. It does
not decide, approve, execute, recommend, prioritize, permit, select a target
state, create a candidate, constrain, react, or write memory.

`SCHEMA_VERSION` remains `genus.foundation.v0.0.1`; v0.3.4 is artifact
contract alignment, v0.3.5 is decisions modularization, and v0.3.6 is
vocabulary modularization, not schema expansion.
