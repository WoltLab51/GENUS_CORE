# GENUS_CORE Passive Metric Acceptance Criteria v0.1.3

Status: acceptance criteria only, not implementation

## Purpose

v0.1.3 defines acceptance criteria for future passive metrics.

It does not implement `PhysicsMetric`, metric models, metric records, metric
functions, metric output shape, metric persistence, sentence types, CLI
commands, or product behavior.

## First Implementation Candidates

The first future passive metric implementation may consider only:

```text
pressure
inhibition
stability
```

These are candidates only. They remain inactive until a later accepted
implementation release.

## Excluded From First Implementation

The first future passive metric implementation must exclude:

```text
cost
potential
```

They remain higher-risk because they can drift toward optimization,
prioritization, or transition selection.

## Allowed Read Surface

A future passive metric may read only:

```text
BeliefStateSnapshot
source_evidence_ids_json
safe descriptive foundation payload fields
```

It must not read hidden runtime state, LLM output, workers, agents, mutable
memory stores, transition engines, constraint engines, reaction systems, or
external execution state.

## Allowed Future Output Category

A future passive metric may produce only:

```text
passive descriptive label plus explanation only
```

The exact output shape is deferred to v0.1.5.

v0.1.3 does not define fields, schemas, classes, records, persistence, sentence
types, numeric scores, or enum values for metric output.

## Forbidden Effects

A future passive metric must not cause or create:

```text
Ledger writes
Evidence creation
Belief mutation
Report triggering
TransitionCandidate
ConstraintDecision
Reaction
MemoryWrite
prioritization
recommendation
permission
activation
action
truth creation
```

## Acceptance Rule

A future passive metric is acceptable only if it remains descriptive and
side-effect free.

It may help explain a foundation state. It must not choose, rank, permit,
activate, transition, constrain, react, write memory, or create truth.

## Non-Scope

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
```

## Forbidden Implementation Locations

Metric acceptance criteria must not be implemented in:

```text
src/genus_core/models
src/genus_core/functions
src/genus_core/language
src/genus_core/truth
CLI
public exports
```

No metric constants, enums, registries, allowed lists, classes, modules, files,
imports, public exports, or public function references may be added to
`src/genus_core` in v0.1.3.
