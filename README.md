# GENUS_CORE

`GENUS_CORE v0.0.1` is the Observation Truth Seed.

It implements only this epistemic chain:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

This version does not implement agents, workers, LLM calls, memory writes,
reactions, decisions, physics metrics, transition candidates, or constraint
decisions.

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
Observation created
EvidenceRecord created
LedgerEntry appended
BeliefStateSnapshot created
ObservationReport created
No action possible in v0.0.1
```

The CLI stores EvidenceRecord and LedgerEntry rows in SQLite. By default it uses
`.genus_core_truth.sqlite3`, which is ignored by Git.

## v0.0.1 Boundary

The report explains what was observed and derived. It does not decide, approve,
execute, react, or write memory.
