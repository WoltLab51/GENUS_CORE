"""Build passive physics artifacts from BeliefStateSnapshot."""

from typing import Any

from genus_core.models.belief_state_snapshot import BeliefStateSnapshot
from genus_core.passive_physics.models import (
    PassiveMetricReport,
    PassiveMetricSnapshot,
)


def _metric_output(
    *,
    metric_name: str,
    level: str,
    assessment_status: str,
    explanation: str,
    source_state_id: str,
    source_evidence_ids_json: list[str],
) -> dict[str, Any]:
    return {
        "metric_name": metric_name,
        "level": level,
        "assessment_status": assessment_status,
        "explanation": explanation,
        "source_state_id": source_state_id,
        "source_evidence_ids_json": list(source_evidence_ids_json),
    }


def build_passive_metric_snapshot(
    belief_state_snapshot: BeliefStateSnapshot,
) -> PassiveMetricSnapshot:
    if not isinstance(belief_state_snapshot, BeliefStateSnapshot):
        raise TypeError("build_passive_metric_snapshot requires BeliefStateSnapshot")

    source_evidence_ids = list(belief_state_snapshot.source_evidence_ids_json)
    observed_memory_request = bool(
        belief_state_snapshot.payload_json.get("observed_memory_request")
    )

    if observed_memory_request:
        pressure = _metric_output(
            metric_name="pressure",
            level="medium",
            assessment_status="assessed",
            explanation=(
                "The belief state contains an observed memory request, which "
                "creates passive unresolved tension."
            ),
            source_state_id=belief_state_snapshot.state_id,
            source_evidence_ids_json=source_evidence_ids,
        )
        inhibition = _metric_output(
            metric_name="inhibition",
            level="high",
            assessment_status="assessed",
            explanation=(
                "The passive foundation boundary prevents memory write or "
                "action for the observed memory request."
            ),
            source_state_id=belief_state_snapshot.state_id,
            source_evidence_ids_json=source_evidence_ids,
        )
    else:
        pressure = _metric_output(
            metric_name="pressure",
            level="none",
            assessment_status="assessed",
            explanation=(
                "No observed memory request is present, so no passive pressure "
                "is visible."
            ),
            source_state_id=belief_state_snapshot.state_id,
            source_evidence_ids_json=source_evidence_ids,
        )
        inhibition = _metric_output(
            metric_name="inhibition",
            level="none",
            assessment_status="not_applicable",
            explanation=(
                "No observed memory request is present, so the passive memory "
                "boundary is not applicable."
            ),
            source_state_id=belief_state_snapshot.state_id,
            source_evidence_ids_json=source_evidence_ids,
        )

    has_valid_lineage = bool(source_evidence_ids) and all(
        isinstance(evidence_id, str) and evidence_id.strip()
        for evidence_id in source_evidence_ids
    )
    if has_valid_lineage and isinstance(belief_state_snapshot.payload_json, dict):
        stability = _metric_output(
            metric_name="stability",
            level="high",
            assessment_status="assessed",
            explanation=(
                "The belief state has evidence lineage and a descriptive "
                "payload, so it is internally coherent for passive assessment."
            ),
            source_state_id=belief_state_snapshot.state_id,
            source_evidence_ids_json=source_evidence_ids,
        )
    else:
        stability = _metric_output(
            metric_name="stability",
            level="none",
            assessment_status="insufficient_input",
            explanation=(
                "The belief state lacks valid evidence lineage or descriptive "
                "payload for passive stability assessment."
            ),
            source_state_id=belief_state_snapshot.state_id,
            source_evidence_ids_json=source_evidence_ids,
        )

    return PassiveMetricSnapshot(
        source_state_id=belief_state_snapshot.state_id,
        source_evidence_ids_json=source_evidence_ids,
        metrics_json=[pressure, inhibition, stability],
    )


def create_passive_metric_report(
    passive_metric_snapshot: PassiveMetricSnapshot,
) -> PassiveMetricReport:
    if not isinstance(passive_metric_snapshot, PassiveMetricSnapshot):
        raise TypeError("create_passive_metric_report requires PassiveMetricSnapshot")

    return PassiveMetricReport(
        source_snapshot_id=passive_metric_snapshot.snapshot_id,
        summary=(
            "Passive physics metrics were described from a BeliefStateSnapshot. "
            "No action is possible under the passive physics boundary."
        ),
        payload_json={
            "no_action_possible": True,
            "source_snapshot_id": passive_metric_snapshot.snapshot_id,
            "source_state_id": passive_metric_snapshot.source_state_id,
            "source_evidence_ids_json": list(
                passive_metric_snapshot.source_evidence_ids_json
            ),
            "passive_metric_outputs": [
                dict(metric) for metric in passive_metric_snapshot.metrics_json
            ],
        },
    )
