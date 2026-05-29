# GENUS_CORE v0.1.3 Release Notes

Release: Passive Metric Acceptance Criteria

## Summary

`GENUS_CORE v0.1.3` defines acceptance criteria for future passive metrics
without implementing metrics.

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
Package version moves to 0.1.3
SCHEMA_VERSION remains genus.foundation.v0.0.1
Passive Metric Acceptance Criteria document added
Docs clarify accepted read surfaces and forbidden effects
Tests guard against premature metric implementation artifacts
```

## Future First Candidates

```text
pressure
inhibition
stability
```

## Still Excluded

```text
cost
potential
```

## Explicit Non-Scope

v0.1.3 does not introduce:

```text
PhysicsMetric
MetricRecord
PassiveMetric
Pressure
Potential
Cost
Inhibition
Stability
calculate_pressure_metric
calculate_inhibition_metric
calculate_stability_metric
calculate_cost_metric
calculate_potential_metric
TransitionCandidate
ConstraintDecision
Reaction
MemoryWrite
```

## Acceptance Evidence

v0.1.3 is accepted only when:

```text
pytest is green
CLI smoke test is green
Passive Metric Acceptance Criteria are documented
accepted read surface is limited
forbidden metric effects are documented
exact output shape is deferred to v0.1.4
metric implementation artifacts remain absent from src/genus_core
allowed sentence types remain unchanged
public foundation functions remain unchanged
no product scope expansion exists
```
