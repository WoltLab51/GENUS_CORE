# Passive Boundary Relevance Spec v0.4.0

Status: accepted spec baseline with narrow v0.4.1 runtime seed

This is an accepted boundary specification. It defines how a passive boundary
relevance description may look. v0.4.1 implements the first narrow runtime seed
under this spec.

The v0.4.0 baseline was docs and tests only. The v0.4.1 baseline activates
only the passive preview and report artifacts named below.

Package version is `0.4.2`.

`SCHEMA_VERSION` remains `genus.foundation.v0.0.1`.

## Purpose

Passive Boundary Relevance describes which boundary areas may later be relevant
for a governed question.

It does not evaluate boundaries.
It does not evaluate permission.
It does not evaluate policy.
It does not approve, reject, allow, block, decide, recommend, execute, react, or
write memory.

## Active Flow

The v0.4.1 implementation flow is:

```text
BeliefStateSnapshot
+ PassiveMetricSnapshot
+ PassiveTransitionPreview
-> PassiveBoundaryRelevancePreview
-> PassiveBoundaryRelevanceReport
-> no decision
-> no action
```

## Active Artifacts

These names are active in v0.4.1:

```text
PassiveBoundaryRelevancePreview
PassiveBoundaryRelevanceReport
build_passive_boundary_relevance_preview(...)
create_passive_boundary_relevance_report(...)
```

Only `src/genus_core/passive_boundary_relevance` may implement these names.
No CLI commands, SQLite tables, sentence types, or schema changes are introduced
by the v0.4.1 runtime seed.

## Artifact Contract Alignment

The v0.4.1 implementation must comply with `ARTIFACT_CONTRACTS.md`.

Common contracts define compatibility, not identical field shape.

Passive boundary relevance artifacts must preserve:

```text
primary ID plus id property
created_at
schema_version
explicit source references
source_evidence_ids_json from Belief lineage
ephemeral-only lifecycle
```

Reports may explain source lineage, but reports must not create new lineage.

## Active Inputs

The v0.4.1 implementation may read only:

```text
BeliefStateSnapshot
PassiveMetricSnapshot
PassiveTransitionPreview
```

These inputs must remain unchanged by the implementation.

## Active Preview Shape

`PassiveBoundaryRelevancePreview` may contain only contract fields and
descriptive fields such as:

```text
preview_id
source_state_id
source_metric_snapshot_id
source_transition_preview_id
source_evidence_ids_json
boundary_question
boundary_area
observed_boundary_relevance
no_decision_possible
no_action_possible
```

`source_state_id`, `source_metric_snapshot_id`, and
`source_transition_preview_id` must reference the three planned input artifacts.

`source_evidence_ids_json` must be inherited from the source
`BeliefStateSnapshot` lineage and must match the passive metric and passive
transition preview lineage.

## Active Report Shape

`PassiveBoundaryRelevanceReport` may contain only explanatory fields
such as:

```text
report_id
source_relevance_preview_id
summary
payload_json
```

The report payload may repeat the preview source references and descriptive
fields for explanation only:

```text
source_state_id
source_metric_snapshot_id
source_transition_preview_id
source_evidence_ids_json
boundary_question
boundary_area
observed_boundary_relevance
no_decision_possible
no_action_possible
```

`no_decision_possible` and `no_action_possible` must be true.

The report must not invent source references or evidence lineage.

## Boundary Area Enum

`boundary_area` must be a closed enum, not free-form text.

Closed enum values:

```text
memory_boundary
passive_foundation_boundary
passive_preview_boundary
```

Unknown `boundary_area` values must be rejected.

`passive_foundation_boundary` remains a spec-known value, but v0.4.1 must not
emit it until an explicit passive derivation rule exists.

Emitted v0.4.1 values are only:

```text
memory_boundary
passive_preview_boundary
```

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

The following are forbidden for runtime payloads in this boundary:

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

## v0.4.1 Runtime Limits

The runtime seed must not add:

```text
src/genus_core/passive_boundary
SCHEMA_VERSION change
SQLite table
CLI command
sentence type
foundation function export
```
