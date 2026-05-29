# GENUS_CORE v0.1.4 Release Notes

Release: Release Integrity & CI Gate

## Summary

`GENUS_CORE v0.1.4` adds a minimal GitHub Actions CI gate for the frozen
foundation and pre-Physics documentation line.

The frozen foundation remains:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

## What Changed

```text
Package version moves to 0.1.4
SCHEMA_VERSION remains genus.foundation.v0.0.1
Minimal GitHub Actions CI workflow added
CI installs dev dependencies
CI runs pytest
CI runs the existing CLI smoke path with an isolated temp SQLite path
Docs mark Passive Metric Output Shape as v0.1.5
```

## Explicit Non-Scope

v0.1.4 does not introduce:

```text
PhysicsMetric
MetricRecord
PassiveMetric
Pressure
Potential
Cost
Inhibition
Stability
metric output shape
metric functions
metric persistence
new sentence types
new CLI commands
coverage
linting
formatting
matrix builds
caching
release automation
deployment
```

## Acceptance Evidence

v0.1.4 is accepted only when:

```text
pytest is green locally
CLI smoke test is green locally
GitHub Actions CI workflow exists
CI uses ubuntu-latest and Python 3.12
CI runs only install, pytest, and CLI smoke
CI stores CLI truth data under runner temp
package version is 0.1.4
SCHEMA_VERSION remains genus.foundation.v0.0.1
no product scope expansion exists
```
