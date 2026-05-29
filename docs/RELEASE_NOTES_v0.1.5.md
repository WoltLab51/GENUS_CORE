# GENUS_CORE v0.1.5 Release Notes

Release: Passive Metric Output Shape

## Summary

`GENUS_CORE v0.1.5` defines the planned-not-active output shape for future
passive metrics without implementing metrics.

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
Package version moves to 0.1.5
SCHEMA_VERSION remains genus.foundation.v0.0.1
Passive Metric Output Shape document added
Docs define allowed planned output fields
Docs distinguish level = none from insufficient_input
Docs keep cost and potential excluded from first output shape
Tests guard against premature metric output implementation artifacts
```

## Planned Output Shape

```text
metric_name: pressure | inhibition | stability
level: none | low | medium | high
assessment_status: assessed | insufficient_input | not_applicable
explanation: descriptive text only
source_state_id: BeliefStateSnapshot ID
source_evidence_ids_json: lineage only
```

## Explicit Non-Scope

v0.1.5 does not introduce:

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

v0.1.5 is accepted only when:

```text
pytest is green
CLI smoke test is green
Passive Metric Output Shape is documented
metric_name values are limited to pressure, inhibition, stability
cost and potential remain excluded
level values are limited to none, low, medium, high
assessment_status values are limited to assessed, insufficient_input, not_applicable
none is not used to mean insufficient input
explanation is descriptive-only
source evidence lineage does not imply scoring or weighting
metric output implementation artifacts remain absent from src/genus_core
allowed sentence types remain unchanged
public foundation functions remain unchanged
no product scope expansion exists
```
