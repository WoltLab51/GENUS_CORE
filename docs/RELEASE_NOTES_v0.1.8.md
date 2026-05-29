# GENUS_CORE v0.1.8 Release Notes

Release: Release Integrity Finalization

## Summary

`GENUS_CORE v0.1.8` makes the post-CI-fix `main` state the clean baseline before
the first passive Physics implementation.

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
Package version moves to 0.1.8
SCHEMA_VERSION remains genus.foundation.v0.0.1
Release metadata now points to the green post-CI-fix baseline
DECISIONS records the concrete Ledger target invariant
DECISIONS records the GitHub Actions YAML smoke fix
v0.1.7 tag remains historical and is not rewritten
```

## Explicit Non-Scope

v0.1.8 does not introduce:

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

v0.1.8 is accepted only when:

```text
pytest is green
CLI smoke test is green
GitHub Actions is green on the v0.1.8 commit
Ledger target hardening remains tested
worker remains only a passive scope label
metric implementation artifacts remain absent from src/genus_core
allowed sentence types remain unchanged
public foundation functions remain unchanged
no product scope expansion exists
```
