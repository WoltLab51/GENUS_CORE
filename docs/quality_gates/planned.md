# GENUS_CORE Quality Gates Planned

Status: active for v0.3.5 Decisions Modularization

## 70. Planned v0.4.0 Passive Boundary Relevance Spec Gate

`v0.4.0 - Passive Boundary Relevance Spec` is accepted only as a planned,
spec-only step if:

```text
pytest green
package version remains 0.3.5
SCHEMA_VERSION remains genus.foundation.v0.0.1
PASSIVE_BOUNDARY_RELEVANCE_SPEC_v0.4.0.md exists
the spec states planned-not-active and spec-only
the spec states no runtime implementation is introduced
the spec references ARTIFACT_CONTRACTS.md
planned artifacts are named only as planned-not-active
planned preview shape includes preview_id, source_state_id, source_metric_snapshot_id, source_transition_preview_id, and source_evidence_ids_json
planned report shape includes report_id, source_relevance_preview_id, summary, and payload_json
planned report does not create new lineage
planned artifacts remain ephemeral-only
PassiveBoundaryRelevancePreview != ConstraintDecision
PassiveBoundaryRelevanceReport != PolicyResult
observed_boundary_relevance != permission
boundary_question != allow/block
boundary_area is a closed enum
first planned boundary_area values are memory_boundary, passive_foundation_boundary, and passive_preview_boundary
unknown boundary_area values must be rejected in a future implementation
observed_boundary_relevance is descriptive-only and non-numeric
observed_boundary_relevance is not level, score, rank, priority, severity, weight, recommendation, or permission
no src/genus_core/passive_boundary* runtime package exists
public foundation functions remain unchanged
CLI exposes only observe
SQLite tables remain evidence_records and ledger_entries
```

## 71. Planned v0.4.0 Spec Stop Gate

Stop development if any of these occur:

```text
Package version changes from 0.3.5.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
src/genus_core/passive_boundary* appears.
PassiveBoundaryRelevancePreview or PassiveBoundaryRelevanceReport appears as a runtime class.
build_passive_boundary_relevance_preview or create_passive_boundary_relevance_report appears as a runtime function.
A new CLI command appears.
A new SQLite table appears.
A new sentence type appears.
The planned spec permits boundary evaluation, permission evaluation, policy evaluation, approval, rejection, allow/block, decision, recommendation, priority, score, rank, severity, weight, execute, reaction, memory write, TransitionCandidate, ConstraintDecision, PolicyResult, Worker, LLM, GraphDB, or RuntimeShape.
```
