"""Create an explanatory ObservationReport from a BeliefStateSnapshot."""

from genus_core.models.belief_state_snapshot import BeliefStateSnapshot
from genus_core.models.observation_report import (
    FORBIDDEN_REPORT_FIELDS,
    ObservationReport,
)


def create_observation_report(
    belief_state_snapshot: BeliefStateSnapshot,
) -> ObservationReport:
    if not isinstance(belief_state_snapshot, BeliefStateSnapshot):
        raise TypeError("create_observation_report requires BeliefStateSnapshot")

    forbidden = FORBIDDEN_REPORT_FIELDS.intersection(
        belief_state_snapshot.payload_json
    )
    if forbidden:
        names = ", ".join(sorted(forbidden))
        raise ValueError(
            f"BeliefStateSnapshot payload cannot be reflected in report: {names}"
        )

    pending_memory_request = bool(
        belief_state_snapshot.payload_json.get("pending_memory_request")
    )
    if pending_memory_request:
        summary = (
            "A memory request is pending as a derived belief. "
            "No action possible in v0.0.1."
        )
    else:
        summary = (
            "A belief was derived from recorded evidence. "
            "No action possible in v0.0.1."
        )

    payload_json = {
        "no_action_possible": True,
        "pending_memory_request": pending_memory_request,
        "source_evidence_ids": list(belief_state_snapshot.source_evidence_ids_json),
    }
    if (
        pending_memory_request
        and "candidate_content" in belief_state_snapshot.payload_json
    ):
        payload_json["candidate_content"] = belief_state_snapshot.payload_json[
            "candidate_content"
        ]

    return ObservationReport(
        source_state_id=belief_state_snapshot.state_id,
        summary=summary,
        payload_json=payload_json,
    )
