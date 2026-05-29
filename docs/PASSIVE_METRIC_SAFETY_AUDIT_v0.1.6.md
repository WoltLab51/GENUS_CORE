# GENUS_CORE Passive Metric Safety Audit v0.1.6

Status: historical safety audit; activated narrowly in v0.2.0 as PassiveMetricSnapshot/PassiveMetricReport

Activated narrowly in v0.2.0 as PassiveMetricSnapshot/PassiveMetricReport.
v0.2.1 clarifies that these passive artifacts are allowed while active metric
classes, modules, functions, persistence, CLI commands, transitions,
constraints, reactions, memory writes, workers, LLMs, GraphDB, and RuntimeShape
remain forbidden.

## Purpose

v0.1.6 audits the passive metric preparation line before any passive Physics
implementation exists.

It does not implement `PhysicsMetric`, metric models, metric records, metric
functions, metric persistence, sentence types, CLI commands, or product
behavior.

## Required Foundation Documents

The safety audit requires:

```text
docs/PRE_PHYSICS_REQUIREMENTS_v0.1.1.md
docs/PASSIVE_METRIC_VOCABULARY_v0.1.2.md
docs/PASSIVE_METRIC_ACCEPTANCE_CRITERIA_v0.1.3.md
docs/PASSIVE_METRIC_OUTPUT_SHAPE_v0.1.5.md
.github/workflows/ci.yml
```

## Status And Level Consistency

The planned passive metric output shape must preserve these consistency rules:

```text
assessment_status = insufficient_input requires level = none
assessment_status = not_applicable requires level = none
assessment_status = assessed may use level = none | low | medium | high
```

These rules prevent contradictory future outputs such as:

```text
assessment_status = insufficient_input
level = high
```

## Excluded Metric Terms

`cost` and `potential` remain excluded from the first implementation and first output shape.

They may remain planned vocabulary only. They must not become first passive
metric outputs before later explicit acceptance.

## Implementation Artifact Absence

Metric safety rules may exist only in docs and tests.

They must not appear in `src/genus_core` as constants, enums, registries,
allowed lists, classes, modules, files, imports, public exports, or public
function references.

## Language And CLI Boundaries

Allowed sentence types remain exactly:

```text
WORLD_EVENT
OBSERVATION
EVIDENCE
LEDGER
BELIEF
REPORT
```

Public foundation functions remain exactly:

```text
observe_event
create_evidence_record
append_ledger_entry
build_belief_state_snapshot
create_observation_report
```

The CLI continues to expose only:

```text
observe
```

## CI Boundary

The CI gate remains minimal:

```text
install
pytest
CLI smoke
```

CI must not add coverage, linting, formatting, matrix builds, caching, release
automation, or deployment in v0.1.6.

## Non-Scope

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
```
