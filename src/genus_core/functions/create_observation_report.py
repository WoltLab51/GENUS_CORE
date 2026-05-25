"""Create an explanatory ObservationReport from a BeliefStateSnapshot."""

from genus_core.models.belief_state_snapshot import BeliefStateSnapshot
from genus_core.models.observation_report import ObservationReport


def create_observation_report(
    belief_state_snapshot: BeliefStateSnapshot,
) -> ObservationReport:
    pending_memory_request = bool(
        belief_state_snapshot.payload_json.get("pending_memory_request")
    )
    if pending_memory_request:
        summary = (
            "A memory request was observed and recorded. "
            "This version cannot write memory."
        )
    else:
        summary = "An observation was recorded. This version cannot perform actions."

    return ObservationReport(
        source_state_id=belief_state_snapshot.state_id,
        summary=summary,
        payload_json={
            "no_action_possible": True,
            "source_evidence_ids": list(
                belief_state_snapshot.source_evidence_ids_json
            ),
        },
    )
