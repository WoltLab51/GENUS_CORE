# GENUS_CORE v0.1.2 Release Notes

Release: Passive Metric Vocabulary

## Summary

`GENUS_CORE v0.1.2` defines planned-not-active passive metric vocabulary without
implementing metrics.

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
Package version moves to 0.1.2
SCHEMA_VERSION remains genus.foundation.v0.0.1
Passive Metric Vocabulary document added
Docs clarify that metric vocabulary is not metric implementation
Tests guard against premature metric artifacts in src/genus_core
```

## Planned-Not-Active Terms

First passive candidates:

```text
pressure
inhibition
stability
```

Higher-risk planned terms:

```text
cost
potential
```

## Explicit Non-Scope

v0.1.2 does not introduce:

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
CognitiveStateMap
TransitionCandidate
ConstraintDecision
Reaction
MemoryWrite
```

## Acceptance Evidence

v0.1.2 is accepted only when:

```text
pytest is green
CLI smoke test is green
Passive Metric Vocabulary is documented
metric terms are planned-not-active
metric implementation artifacts remain absent from src/genus_core
allowed sentence types remain unchanged
public foundation functions remain unchanged
no product scope expansion exists
```
