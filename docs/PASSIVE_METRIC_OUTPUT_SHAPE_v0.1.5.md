# GENUS_CORE Passive Metric Output Shape v0.1.5

Status: historical output shape; activated narrowly in v0.2.0 as PassiveMetricSnapshot/PassiveMetricReport

Activated narrowly in v0.2.0 as PassiveMetricSnapshot/PassiveMetricReport.
v0.2.1 clarifies that these passive artifacts are allowed while active metric
classes, modules, functions, persistence, CLI commands, transitions,
constraints, reactions, memory writes, workers, LLMs, GraphDB, and RuntimeShape
remain forbidden.

## Purpose

v0.1.5 defines the planned-not-active output shape for future passive metrics.

It does not implement `PhysicsMetric`, metric models, metric records, metric
functions, metric persistence, sentence types, CLI commands, or product
behavior.

## Allowed First Output Metric Names

The first future passive metric output shape may use only:

```text
metric_name = pressure
metric_name = inhibition
metric_name = stability
```

These names remain inactive until a later accepted implementation release.

## Excluded From First Output Shape

The first future passive metric output shape must exclude:

```text
cost
potential
```

They remain higher-risk because they can drift toward optimization,
prioritization, or transition selection.

## Planned Output Fields

A future passive metric output may contain only:

```text
metric_name
level
assessment_status
explanation
source_state_id
source_evidence_ids_json
```

These fields define a planned shape only. v0.1.5 does not add a class, schema,
record, function, persistence table, public export, sentence type, or CLI
command.

## Level Values

Allowed `level` values are exactly:

```text
none
low
medium
high
```

`level = none` means the metric was assessed and no visible metric expression
was found. It must not mean insufficient input.

## Assessment Status Values

Allowed `assessment_status` values are exactly:

```text
assessed
insufficient_input
not_applicable
```

`assessment_status = assessed` means the future metric had enough foundation
state to describe a level.

`assessment_status = insufficient_input` means the foundation state cannot
support assessment.

`assessment_status = not_applicable` means the metric does not apply to that
foundation state.

## Status And Level Consistency

`assessment_status = insufficient_input` requires `level = none`.

`assessment_status = not_applicable` requires `level = none`.

`assessment_status = assessed` may use `level = none`, `level = low`,
`level = medium`, or `level = high`.

```text
assessment_status = insufficient_input requires level = none
assessment_status = not_applicable requires level = none
assessment_status = assessed may use level = none | low | medium | high
```

## Explanation Boundary

`explanation` is descriptive-only.

It must not recommend, permit, approve, rank, prioritize, trigger, execute,
transition, react, or write memory.

It must not introduce facts not derivable from `source_state_id` and
`source_evidence_ids_json`.

## Lineage Boundary

`source_state_id` references the source `BeliefStateSnapshot`.

`source_evidence_ids_json` preserves evidence lineage only.

It must not imply scoring, weighting, ranking, priority, or confidence.

## Forbidden Output Fields

Future passive metric output must not contain:

```text
score
priority
rank
recommendation
permission
decision
approval
action
execute
candidate
transition
constraint
reaction
memory_write
truth
```

## Non-Scope

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
```

## Forbidden Implementation Locations

Metric output shape must not be implemented in:

```text
src/genus_core/models
src/genus_core/functions
src/genus_core/language
src/genus_core/truth
CLI
public exports
```

No metric output constants, enums, registries, allowed lists, classes, modules,
files, imports, public exports, or public function references may be added to
`src/genus_core` in v0.1.5.
