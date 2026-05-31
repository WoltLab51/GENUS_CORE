"""Build passive transition preview artifacts from passive foundation state."""

from genus_core.models.belief_state_snapshot import BeliefStateSnapshot
from genus_core.passive_physics.models import PassiveMetricSnapshot
from genus_core.passive_transition.models import (
    PassiveTransitionPreview,
    PassiveTransitionReport,
)


def _metrics_by_name(snapshot: PassiveMetricSnapshot) -> dict[str, dict]:
    return {metric["metric_name"]: metric for metric in snapshot.metrics_json}


def build_passive_transition_preview(
    belief_state_snapshot: BeliefStateSnapshot,
    passive_metric_snapshot: PassiveMetricSnapshot,
) -> PassiveTransitionPreview:
    if not isinstance(belief_state_snapshot, BeliefStateSnapshot):
        raise TypeError("build_passive_transition_preview requires BeliefStateSnapshot")
    if not isinstance(passive_metric_snapshot, PassiveMetricSnapshot):
        raise TypeError("build_passive_transition_preview requires PassiveMetricSnapshot")
    if passive_metric_snapshot.source_state_id != belief_state_snapshot.state_id:
        raise ValueError("PassiveMetricSnapshot source_state_id must match BeliefStateSnapshot")
    if (
        passive_metric_snapshot.source_evidence_ids_json
        != belief_state_snapshot.source_evidence_ids_json
    ):
        raise ValueError("PassiveMetricSnapshot evidence lineage must match BeliefStateSnapshot")

    metrics = _metrics_by_name(passive_metric_snapshot)
    observed_memory_request = bool(
        belief_state_snapshot.payload_json.get("observed_memory_request")
    )
    memory_tension_visible = (
        observed_memory_request
        and metrics.get("pressure", {}).get("level") == "medium"
        and metrics.get("inhibition", {}).get("level") == "high"
        and metrics.get("pressure", {}).get("assessment_status") == "assessed"
        and metrics.get("inhibition", {}).get("assessment_status") == "assessed"
    )

    if memory_tension_visible:
        preview_type = "memory_request_transition_tension_preview"
        observed_tension_summary = (
            "An observed memory request shows passive pressure while passive "
            "inhibition remains high under the current boundary."
        )
        possible_future_question = (
            "Could a later governed boundary describe whether observed memory "
            "content raises a governed memory question?"
        )
    else:
        preview_type = "no_visible_transition_tension_preview"
        observed_tension_summary = (
            "No passive memory-request tension is visible from the current "
            "belief and metric snapshots."
        )
        possible_future_question = (
            "Could a later governed boundary describe whether any passive "
            "state question is visible?"
        )

    return PassiveTransitionPreview(
        source_state_id=belief_state_snapshot.state_id,
        source_metric_snapshot_id=passive_metric_snapshot.snapshot_id,
        source_evidence_ids_json=list(belief_state_snapshot.source_evidence_ids_json),
        preview_type=preview_type,
        observed_tension_summary=observed_tension_summary,
        possible_future_question=possible_future_question,
        no_action_possible=True,
        no_decision_possible=True,
    )


def create_passive_transition_report(
    passive_transition_preview: PassiveTransitionPreview,
) -> PassiveTransitionReport:
    if not isinstance(passive_transition_preview, PassiveTransitionPreview):
        raise TypeError(
            "create_passive_transition_report requires PassiveTransitionPreview"
        )

    return PassiveTransitionReport(
        source_preview_id=passive_transition_preview.preview_id,
        summary=(
            "A passive preview question was described from passive foundation "
            "state and passive metrics. No action or decision is possible under "
            "the passive preview boundary."
        ),
        payload_json={
            "no_action_possible": True,
            "no_decision_possible": True,
            "source_preview_id": passive_transition_preview.preview_id,
            "source_state_id": passive_transition_preview.source_state_id,
            "source_metric_snapshot_id": (
                passive_transition_preview.source_metric_snapshot_id
            ),
            "source_evidence_ids_json": list(
                passive_transition_preview.source_evidence_ids_json
            ),
            "preview_type": passive_transition_preview.preview_type,
            "observed_tension_summary": (
                passive_transition_preview.observed_tension_summary
            ),
            "possible_future_question": (
                passive_transition_preview.possible_future_question
            ),
        },
    )
