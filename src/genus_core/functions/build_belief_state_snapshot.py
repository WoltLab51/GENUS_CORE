"""Build a BeliefStateSnapshot from EvidenceRecords."""

from collections.abc import Sequence

from genus_core.models.belief_state_snapshot import BeliefStateSnapshot
from genus_core.models.evidence_record import EvidenceRecord


def build_belief_state_snapshot(
    evidence_records: Sequence[EvidenceRecord],
) -> BeliefStateSnapshot:
    if not evidence_records:
        raise ValueError("Cannot build belief without evidence")

    pending_memory_request = False
    candidate_content: str | None = None

    for evidence in evidence_records:
        observation_type = evidence.payload_json.get("observed_observation_type")
        observation_payload = evidence.payload_json.get("observation_payload", {})
        if observation_type == "memory_request_observed":
            pending_memory_request = True
            candidate_content = observation_payload.get("candidate_content")

    payload: dict[str, object] = {"pending_memory_request": pending_memory_request}
    if candidate_content:
        payload["candidate_content"] = candidate_content

    scope = "memory" if pending_memory_request else "input"
    return BeliefStateSnapshot(
        scope=scope,
        source_evidence_ids_json=[record.evidence_id for record in evidence_records],
        payload_json=payload,
    )
