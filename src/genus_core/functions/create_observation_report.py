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

    observed_memory_request = bool(
        belief_state_snapshot.payload_json.get("observed_memory_request")
    )
    if observed_memory_request:
        summary = (
            "A memory request was observed as a derived belief. "
            "No action is possible under the passive foundation boundary."
        )
    else:
        summary = (
            "A belief was derived from recorded evidence. "
            "No action is possible under the passive foundation boundary."
        )

    payload_json = {
        "no_action_possible": True,
        "observed_memory_request": observed_memory_request,
        "source_evidence_ids": list(belief_state_snapshot.source_evidence_ids_json),
    }
    if (
        observed_memory_request
        and "observed_memory_content" in belief_state_snapshot.payload_json
    ):
        payload_json["observed_memory_content"] = belief_state_snapshot.payload_json[
            "observed_memory_content"
        ]

    return ObservationReport(
        source_state_id=belief_state_snapshot.state_id,
        summary=summary,
        payload_json=payload_json,
    )
