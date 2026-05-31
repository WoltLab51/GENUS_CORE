"""Build passive boundary relevance artifacts from passive upstream artifacts."""

from typing import Any

from genus_core.models.belief_state_snapshot import BeliefStateSnapshot
from genus_core.passive_boundary_relevance.models import (
    PassiveBoundaryRelevancePreview,
    PassiveBoundaryRelevanceReport,
)
from genus_core.passive_physics.models import PassiveMetricSnapshot
from genus_core.passive_transition.models import PassiveTransitionPreview


def _metrics_by_name(snapshot: PassiveMetricSnapshot) -> dict[str, dict[str, Any]]:
    return {metric["metric_name"]: metric for metric in snapshot.metrics_json}


def _require_matching_lineage(
    belief_state_snapshot: BeliefStateSnapshot,
    passive_metric_snapshot: PassiveMetricSnapshot,
    passive_transition_preview: PassiveTransitionPreview,
) -> None:
    if passive_metric_snapshot.source_state_id != belief_state_snapshot.state_id:
        raise ValueError("PassiveMetricSnapshot source_state_id must match BeliefStateSnapshot")
    if passive_transition_preview.source_state_id != belief_state_snapshot.state_id:
        raise ValueError(
            "PassiveTransitionPreview source_state_id must match BeliefStateSnapshot"
        )
    if (
        passive_transition_preview.source_metric_snapshot_id
        != passive_metric_snapshot.snapshot_id
    ):
        raise ValueError(
            "PassiveTransitionPreview source_metric_snapshot_id must match "
            "PassiveMetricSnapshot"
        )
    if (
        passive_metric_snapshot.source_evidence_ids_json
        != belief_state_snapshot.source_evidence_ids_json
    ):
        raise ValueError("PassiveMetricSnapshot evidence lineage must match BeliefStateSnapshot")
    if (
        passive_transition_preview.source_evidence_ids_json
        != belief_state_snapshot.source_evidence_ids_json
    ):
        raise ValueError(
            "PassiveTransitionPreview evidence lineage must match BeliefStateSnapshot"
        )


def build_passive_boundary_relevance_preview(
    belief_state_snapshot: BeliefStateSnapshot,
    passive_metric_snapshot: PassiveMetricSnapshot,
    passive_transition_preview: PassiveTransitionPreview,
) -> PassiveBoundaryRelevancePreview:
    if not isinstance(belief_state_snapshot, BeliefStateSnapshot):
        raise TypeError(
            "build_passive_boundary_relevance_preview requires BeliefStateSnapshot"
        )
    if not isinstance(passive_metric_snapshot, PassiveMetricSnapshot):
        raise TypeError(
            "build_passive_boundary_relevance_preview requires PassiveMetricSnapshot"
        )
    if not isinstance(passive_transition_preview, PassiveTransitionPreview):
        raise TypeError(
            "build_passive_boundary_relevance_preview requires "
            "PassiveTransitionPreview"
        )
    _require_matching_lineage(
        belief_state_snapshot,
        passive_metric_snapshot,
        passive_transition_preview,
    )

    metrics = _metrics_by_name(passive_metric_snapshot)
    observed_memory_request = bool(
        belief_state_snapshot.payload_json.get("observed_memory_request")
    )
    memory_relevance_visible = (
        observed_memory_request
        and metrics.get("pressure", {}).get("level") == "medium"
        and metrics.get("pressure", {}).get("assessment_status") == "assessed"
        and metrics.get("inhibition", {}).get("level") == "high"
        and metrics.get("inhibition", {}).get("assessment_status") == "assessed"
        and passive_transition_preview.preview_type
        == "memory_request_transition_tension_preview"
    )

    if memory_relevance_visible:
        boundary_area = "memory_boundary"
        observed_boundary_relevance = "memory_request_relevance_observed"
        boundary_question = (
            "Could a later governed boundary describe whether observed memory "
            "content raises a memory boundary question?"
        )
    elif passive_transition_preview.preview_type == "no_visible_transition_tension_preview":
        boundary_area = "passive_preview_boundary"
        observed_boundary_relevance = "no_boundary_relevance_observed"
        boundary_question = (
            "Could a later governed boundary describe whether passive preview "
            "relevance is visible?"
        )
    else:
        raise ValueError(
            "Passive boundary relevance requires matching passive upstream inputs"
        )

    return PassiveBoundaryRelevancePreview(
        source_state_id=belief_state_snapshot.state_id,
        source_metric_snapshot_id=passive_metric_snapshot.snapshot_id,
        source_transition_preview_id=passive_transition_preview.preview_id,
        source_evidence_ids_json=list(belief_state_snapshot.source_evidence_ids_json),
        boundary_question=boundary_question,
        boundary_area=boundary_area,
        observed_boundary_relevance=observed_boundary_relevance,
        no_decision_possible=True,
        no_action_possible=True,
    )


def create_passive_boundary_relevance_report(
    passive_boundary_relevance_preview: PassiveBoundaryRelevancePreview,
) -> PassiveBoundaryRelevanceReport:
    if not isinstance(
        passive_boundary_relevance_preview, PassiveBoundaryRelevancePreview
    ):
        raise TypeError(
            "create_passive_boundary_relevance_report requires "
            "PassiveBoundaryRelevancePreview"
        )

    return PassiveBoundaryRelevanceReport(
        source_relevance_preview_id=(
            passive_boundary_relevance_preview.preview_id
        ),
        summary=(
            "Passive boundary relevance was described from passive upstream "
            "artifacts. No action or decision is possible under the passive "
            "boundary relevance boundary."
        ),
        payload_json={
            "source_relevance_preview_id": (
                passive_boundary_relevance_preview.preview_id
            ),
            "source_state_id": passive_boundary_relevance_preview.source_state_id,
            "source_metric_snapshot_id": (
                passive_boundary_relevance_preview.source_metric_snapshot_id
            ),
            "source_transition_preview_id": (
                passive_boundary_relevance_preview.source_transition_preview_id
            ),
            "source_evidence_ids_json": list(
                passive_boundary_relevance_preview.source_evidence_ids_json
            ),
            "boundary_question": passive_boundary_relevance_preview.boundary_question,
            "boundary_area": passive_boundary_relevance_preview.boundary_area,
            "observed_boundary_relevance": (
                passive_boundary_relevance_preview.observed_boundary_relevance
            ),
            "no_decision_possible": True,
            "no_action_possible": True,
        },
    )
