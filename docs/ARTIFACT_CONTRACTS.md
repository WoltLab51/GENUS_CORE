# GENUS_CORE Artifact Contracts

Status: active for v0.3.9 Ledger Test Modularization

GENUS artifacts are allowed to have different shapes. They still need shared
contracts so they can compose without turning into a monolith.

Common artifact contracts define compatibility, not identical field shape.

## ID Contract

Every active GENUS artifact has exactly one primary ID field and an `id`
property that returns that primary ID.

Current primary IDs:

```text
WorldEvent.event_id
Observation.observation_id
EvidenceRecord.evidence_id
LedgerEntry.ledger_id
BeliefStateSnapshot.state_id
ObservationReport.report_id
PassiveMetricSnapshot.snapshot_id
PassiveMetricReport.report_id
PassiveTransitionPreview.preview_id
PassiveTransitionReport.report_id
```

Every active artifact also carries `created_at` and `schema_version`.

## Source Lineage Contract

Derived artifacts must explicitly reference the artifact they were derived
from.

Current source references:

```text
Observation.source_event_id -> WorldEvent.event_id
EvidenceRecord.source_observation_id -> Observation.observation_id
LedgerEntry.source_id -> Observation.observation_id
LedgerEntry.target_id -> EvidenceRecord.evidence_id
BeliefStateSnapshot.source_evidence_ids_json -> EvidenceRecord.evidence_id list
ObservationReport.source_state_id -> BeliefStateSnapshot.state_id
PassiveMetricSnapshot.source_state_id -> BeliefStateSnapshot.state_id
PassiveMetricReport.source_snapshot_id -> PassiveMetricSnapshot.snapshot_id
PassiveTransitionPreview.source_state_id -> BeliefStateSnapshot.state_id
PassiveTransitionPreview.source_metric_snapshot_id -> PassiveMetricSnapshot.snapshot_id
PassiveTransitionReport.source_preview_id -> PassiveTransitionPreview.preview_id
```

## Evidence Lineage Contract

When a passive downstream artifact is derived from `BeliefStateSnapshot`, it
must preserve the same evidence lineage.

Current downstream evidence lineage:

```text
BeliefStateSnapshot.source_evidence_ids_json
PassiveMetricSnapshot.source_evidence_ids_json
PassiveMetricSnapshot.metrics_json[*].source_evidence_ids_json
PassiveTransitionPreview.source_evidence_ids_json
PassiveMetricReport.payload_json.source_evidence_ids_json
PassiveTransitionReport.payload_json.source_evidence_ids_json
```

Reports may explain lineage, but reports do not create new lineage.

## Snapshot, Preview, And Report Contract

Snapshot means structured passive state or derivation state.

Preview means structured passive tension or later-question preview.

Report means an explanation of an existing artifact.

Reports explain existing artifacts. They do not derive new system state, create
new lineage, decide, recommend, permit, prioritize, react, write memory, execute
work, or create truth.

## Durable And Ephemeral Contract

The durable truth layer is still exactly:

```text
EvidenceRecord
LedgerEntry
```

Durable storage is still exactly:

```text
evidence_records
ledger_entries
```

The following remain ephemeral unless a later accepted persistence release says
otherwise:

```text
WorldEvent
Observation
BeliefStateSnapshot
ObservationReport
PassiveMetricSnapshot
PassiveMetricReport
PassiveTransitionPreview
PassiveTransitionReport
planned PassiveBoundaryRelevancePreview
planned PassiveBoundaryRelevanceReport
```

## Report Boundary Contract

Reports may carry source IDs, descriptive summaries, and descriptive payloads.

Reports must not introduce fields or wording that imply:

```text
decision
approval
permission
recommendation
priority
allow/block
action
execute
reaction
memory_write
truth
policy_result
constraint decision
transition candidate
```

## Watched Wording

`evaluate` and `evaluation` are watched terms.

Reason:

```text
They can drift toward permission, policy, approval, rejection, allow/block, or
decision semantics.
```

Allowed future use:

```text
Only when explicitly qualified by an accepted spec as descriptive relevance mapping.
```

Forbidden use:

```text
permission evaluation
policy evaluation
approval evaluation
decision evaluation
```
