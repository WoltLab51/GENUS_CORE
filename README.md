# GENUS_CORE

[![CI](https://github.com/WoltLab51/GENUS_CORE/actions/workflows/ci.yml/badge.svg)](https://github.com/WoltLab51/GENUS_CORE/actions/workflows/ci.yml)

`GENUS_CORE v0.1.7` is Foundation Cleanup and Integrity Repair.

It keeps the `v0.1.0` passive foundation frozen:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

This release cleans up the v0.1.6 baseline before any passive Physics
implementation. It tightens Ledger lineage targets, clarifies passive worker
scope wording, and keeps agents, workers, LLM calls, memory writes, reactions,
decisions, physics metrics, metric functions, cognitive maps, transition
candidates, constraint decisions, runtime cells, organs, and GraphDB truth out
of scope.

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
No action possible in v0.0.1
```

The CLI stores EvidenceRecord and LedgerEntry rows in SQLite. By default it uses
`.genus_core_truth.sqlite3`, which is ignored by Git.

## Stable Foundation Boundary

The report explains what was observed, recorded, and derived. It does not
decide, approve, execute, react, write memory, create truth, transition,
constrain, or measure physics.

`SCHEMA_VERSION` remains `genus.foundation.v0.0.1`; v0.1.7 is a cleanup and
integrity step, not a schema expansion.
