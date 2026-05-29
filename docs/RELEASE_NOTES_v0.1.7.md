# GENUS_CORE v0.1.7 Release Notes

Release: Foundation Cleanup and Integrity Repair

## Summary

`GENUS_CORE v0.1.7` cleans up the v0.1.6 baseline before the first passive
Physics implementation.

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
Package version moves to 0.1.7
SCHEMA_VERSION remains genus.foundation.v0.0.1
Project metadata now describes the current cleanup release
Status documentation treats v0.1.6 as the released baseline
LedgerEntry now requires target_kind and target_id
New SQLite ledger_entries tables require non-empty target_id
worker scope is clarified as a passive label, not a Worker capability
GitHub Actions failure with zero jobs is documented as an external CI signal
```

## Explicit Non-Scope

v0.1.7 does not introduce:

```text
PhysicsMetric
MetricRecord
PassiveMetric
MetricOutput
PassiveMetricOutput
MetricOutputShape
Pressure
Potential
Cost
Inhibition
Stability
metric persistence
new sentence types
new CLI commands
Worker
Agent
LLM
```

## Acceptance Evidence

v0.1.7 is accepted only when:

```text
pytest is green
CLI smoke test is green
Ledger target hardening is tested
worker remains only a passive scope label
metric implementation artifacts remain absent from src/genus_core
allowed sentence types remain unchanged
public foundation functions remain unchanged
no product scope expansion exists
```
