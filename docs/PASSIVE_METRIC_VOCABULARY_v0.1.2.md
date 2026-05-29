# GENUS_CORE Passive Metric Vocabulary v0.1.2

Status: vocabulary only, planned-not-active

## Purpose

v0.1.2 defines planned passive metric terms without implementing metrics.

This document may name future metric vocabulary. It does not activate that
vocabulary in runtime code, sentence types, CLI commands, storage, or public
exports.

## Vocabulary Boundaries

```text
Metric Vocabulary != Metric Implementation
Metric Term != Decision
Metric Term != Priority
Metric Term != Transition
Metric Term != Action
Metric Term != Permission
Metric Term != Recommendation
Metric Term != Activation
Metric Term != MemoryWrite
```

Metric terms are names for possible future passive descriptions. They are not
scores, policies, recommendations, candidate generators, or triggers.

## First Passive Candidates

The first passive candidates are:

```text
pressure
inhibition
stability
```

These are candidates for the first passive metric implementation only after a
later accepted plan defines inputs, outputs, persistence, and tests.

## Higher-Risk Planned Terms

The higher-risk planned terms are:

```text
cost
potential
```

They are not first implementation terms. They require later explicit acceptance
because they can drift toward optimization, prioritization, or transition
selection.

## pressure

planned-not-active

A passive indication that a BeliefState suggests unresolved tension or repeated
need.

It is not a decision, priority, action trigger, permission, recommendation,
activation, transition, constraint, truth claim, or memory write.

## inhibition

planned-not-active

A passive indication that a boundary, absence, or blocking condition may exist.

It is not a ConstraintDecision, block command, policy engine, action, reaction,
permission, recommendation, transition, truth claim, or memory write.

## stability

planned-not-active

A passive indication of whether the current foundation state appears internally
coherent.

It is not a health manager, repair trigger, runtime supervisor, approval,
decision, action, recommendation, truth claim, or memory write.

## cost

planned-not-active

A higher-risk planned passive estimate of effort, complexity, or resource
demand.

It is not a scheduler, optimizer, budget allocator, priority score, decision,
permission, recommendation, action, transition, truth claim, or memory write.

## potential

planned-not-active

A higher-risk planned passive estimate that a future transition might relieve
pressure.

It is not a TransitionCandidate, recommendation, permission, execution plan,
activation, decision, action, truth claim, or memory write.

Potential is not active in the first passive physics implementation unless
explicitly accepted later.

## Non-Scope

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
```

## Allowed Locations

Metric vocabulary may exist only in docs and tests.

## Forbidden Implementation Locations

Metric vocabulary must not be implemented in:

```text
src/genus_core/models
src/genus_core/functions
src/genus_core/language
src/genus_core/truth
CLI
public exports
```

No metric-term constants, enums, registries, allowed lists, classes, modules,
files, imports, public exports, or public function references may be added to
`src/genus_core` in v0.1.2.
