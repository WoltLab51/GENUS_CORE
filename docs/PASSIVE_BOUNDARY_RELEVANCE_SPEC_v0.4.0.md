# Passive Boundary Relevance Spec v0.4.0

Status: planned-not-active specification

This is a planning-only boundary specification. It defines how a later passive
boundary relevance description may look. It does not implement runtime code.

Expected diff for this spec step is docs and tests only.

Package version remains `0.3.2`.

`SCHEMA_VERSION` remains `genus.foundation.v0.0.1`.

## Purpose

Passive Boundary Relevance describes which boundary areas may later be relevant
for a governed question.

It does not evaluate boundaries.
It does not evaluate permission.
It does not evaluate policy.
It does not approve, reject, allow, block, decide, recommend, execute, react, or
write memory.

## Planned Flow

The planned later flow is:

```text
BeliefStateSnapshot
+ PassiveMetricSnapshot
+ PassiveTransitionPreview
-> PassiveBoundaryRelevancePreview
-> PassiveBoundaryRelevanceReport
-> no boundary evaluation
-> no decision
-> no action
```

## Planned Artifacts

These names are planned-not-active only:

```text
PassiveBoundaryRelevancePreview
PassiveBoundaryRelevanceReport
build_passive_boundary_relevance_preview(...)
create_passive_boundary_relevance_report(...)
```

No `src/genus_core/passive_boundary*` package may exist for this spec step.
No classes, functions, runtime exports, CLI commands, SQLite tables, sentence
types, or schema changes are introduced by this spec.

## Planned Inputs

A later implementation may read only:

```text
BeliefStateSnapshot
PassiveMetricSnapshot
PassiveTransitionPreview
```

These inputs must remain unchanged by a future implementation.

## Planned Output Shape

A later passive output may contain only descriptive fields such as:

```text
boundary_question
boundary_area
observed_boundary_relevance
no_boundary_evaluation_possible
no_decision_possible
no_action_possible
```

`no_boundary_evaluation_possible`, `no_decision_possible`, and
`no_action_possible` must be true.

## Boundary Area Enum

`boundary_area` must be a closed enum, not free-form text.

First planned values only:

```text
memory_boundary
passive_foundation_boundary
passive_preview_boundary
```

Unknown `boundary_area` values must be rejected in a future implementation.

## Relevance Semantics

Relevance means descriptive boundary relevance mapping only.

Relevance means that a boundary area is described as a later possibly relevant
boundary area.

Relevance does not mean:

```text
Evaluation
Permission evaluation
Policy evaluation
Approval
Rejection
Allow/block
Decision
```

`observed_boundary_relevance` must be descriptive only.

It must not be:

```text
numeric
level
score
rank
priority
severity
weight
recommendation
permission
```

## Non-Equivalence Rules

```text
PassiveBoundaryRelevancePreview != ConstraintDecision
PassiveBoundaryRelevanceReport != PolicyResult
observed_boundary_relevance != permission
boundary_question != allow/block
```

## Hard Exclusions

The following are forbidden for any future runtime payload in this boundary:

```text
ConstraintDecision
Decision
PolicyResult
policy
policy_status
policy_result
Authorization
permission
allow
block
approve
reject
recommendation
priority
score
rank
severity
weight
execute
Reaction
MemoryWrite
TransitionCandidate
target_state
selected_transition
proposed_transition
LLM
Worker
GraphDB
RuntimeShape
```

## Explicit Non-Implementation

This spec step must not add:

```text
src/genus_core/passive_boundary
src/genus_core/passive_boundary_relevance
PassiveBoundaryRelevancePreview class
PassiveBoundaryRelevanceReport class
build_passive_boundary_relevance_preview function
create_passive_boundary_relevance_report function
package version bump
SCHEMA_VERSION change
SQLite table
CLI command
sentence type
runtime export
```
