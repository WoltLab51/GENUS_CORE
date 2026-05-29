# GENUS_CORE

`GENUS_CORE v0.1.2` is Passive Metric Vocabulary.

It keeps the `v0.1.0` passive foundation frozen:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

This release defines planned-not-active passive metric vocabulary only. It does
not implement agents, workers, LLM calls, memory writes, reactions, decisions,
physics metrics, metric functions, cognitive maps, transition candidates,
constraint decisions, runtime cells, organs, or GraphDB truth.

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

`SCHEMA_VERSION` remains `genus.foundation.v0.0.1`; v0.1.2 is a vocabulary
release, not a schema expansion.
