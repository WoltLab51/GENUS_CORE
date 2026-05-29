# GENUS_CORE v0.1.6 Release Notes

Release: Passive Metric Safety Audit

## Summary

`GENUS_CORE v0.1.6` audits the passive metric preparation line before any
passive Physics implementation exists.

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
Package version moves to 0.1.6
SCHEMA_VERSION remains genus.foundation.v0.0.1
Passive Metric Safety Audit document added
Status/level consistency rules added to the output shape
Tests verify requirements, vocabulary, acceptance criteria, output shape, and CI exist
Tests verify metric implementation artifacts remain absent from src/genus_core
```

## Status And Level Consistency

```text
assessment_status = insufficient_input requires level = none
assessment_status = not_applicable requires level = none
assessment_status = assessed may use level = none | low | medium | high
```

## Explicit Non-Scope

v0.1.6 does not introduce:

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
calculate_pressure_metric
calculate_inhibition_metric
calculate_stability_metric
calculate_cost_metric
calculate_potential_metric
metric persistence
new sentence types
new CLI commands
```

## Acceptance Evidence

v0.1.6 is accepted only when:

```text
pytest is green
CLI smoke test is green
Passive Metric Safety Audit is documented
Pre-Physics Requirements exist
Passive Metric Vocabulary exists
Passive Metric Acceptance Criteria exist
Passive Metric Output Shape exists
CI Gate exists
status/level consistency rules are documented
cost and potential remain excluded
metric implementation artifacts remain absent from src/genus_core
allowed sentence types remain unchanged
public foundation functions remain unchanged
no product scope expansion exists
```
