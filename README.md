# GENUS_CORE

[![CI](https://github.com/WoltLab51/GENUS_CORE/actions/workflows/ci.yml/badge.svg)](https://github.com/WoltLab51/GENUS_CORE/actions/workflows/ci.yml)

`GENUS_CORE v0.2.0` is Passive Physics Seed.

It keeps the `v0.1.0` passive foundation frozen:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

This release introduces the first narrow passive Physics layer after the passive
foundation. It preserves the v0.1.10 governance baseline and keeps agents,
workers, LLM calls, memory writes, reactions, decisions, cognitive maps,
transition candidates, constraint decisions, runtime cells, organs, and GraphDB
truth out of scope.

## Version and Boundary

Package version: `0.2.0`

Foundation schema version: `genus.foundation.v0.0.1`

Capability boundary: passive foundation plus passive Physics only

Governance documents:

- `docs/GENUS_CHARTER.md`
- `docs/SAFETY_BOUNDARIES.md`

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

The report explains what was observed, recorded, and derived. It does not
decide, approve, execute, react, write memory, create truth, transition,
constrain, or measure physics.

`SCHEMA_VERSION` remains `genus.foundation.v0.0.1`; v0.2.0 is a passive
Physics step, not a schema expansion.
