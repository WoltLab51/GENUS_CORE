"""Build a BeliefStateSnapshot from EvidenceRecords."""

from collections.abc import Sequence

from genus_core.models.belief_state_snapshot import BeliefStateSnapshot
from genus_core.models.evidence_record import EvidenceRecord

ALLOWED_BELIEF_OBSERVATION_TYPES = frozenset(
    {
        "memory_request_observed",
        "memory_lookup_failure_observed",
        "guard_block_observed",
        "unknown_input_observed",
        "ambiguous_input_observed",
    }
)

FORBIDDEN_BELIEF_PAYLOAD_FIELDS = frozenset(
    {
        "truth",
        "world_truth",
        "truth_status",
        "evidence",
        "decision",
        "approval",
        "action",
        "reaction",
        "constraint",
        "transition",
        "physics",
        "memory_write",
        "execute",
        "candidate",
    }
)


def build_belief_state_snapshot(
    evidence_records: Sequence[EvidenceRecord],
) -> BeliefStateSnapshot:
    if not evidence_records:
        raise ValueError("Cannot build belief without evidence")

    for evidence in evidence_records:
        if not isinstance(evidence, EvidenceRecord):
            raise TypeError("Belief derivation requires EvidenceRecord inputs")

    pending_memory_request = False
    candidate_content: str | None = None
    observed_scope: str | None = None

    for evidence in evidence_records:
        if evidence.truth_status != "observed":
            raise ValueError("Belief derivation only accepts observed EvidenceRecords")
        if evidence.payload_json.get("evidence_claim") != "observation_recorded":
            raise ValueError("Belief derivation requires evidence_claim=observation_recorded")
        observation_type = evidence.payload_json.get("observed_observation_type")
        if observation_type not in ALLOWED_BELIEF_OBSERVATION_TYPES:
            raise ValueError(f"Unsupported belief observation type: {observation_type}")
        observation_scope = evidence.payload_json.get("observation_scope")
        if not observation_scope:
            raise ValueError("Belief derivation requires observation_scope")
        if observed_scope is None:
            observed_scope = observation_scope
        elif observation_scope != observed_scope:
            raise ValueError("Belief derivation rejects mixed observation scopes")

        observation_payload = evidence.payload_json.get("observation_payload", {})
        if observation_type == "memory_request_observed":
            pending_memory_request = True
            candidate_content = observation_payload.get("candidate_content")

    payload: dict[str, object] = {"pending_memory_request": pending_memory_request}
    if candidate_content:
        payload["candidate_content"] = candidate_content
    forbidden = FORBIDDEN_BELIEF_PAYLOAD_FIELDS.intersection(payload)
    if forbidden:
        names = ", ".join(sorted(forbidden))
        raise ValueError(f"Belief payload cannot contain forbidden fields: {names}")

    return BeliefStateSnapshot(
        scope=observed_scope or "input",
        source_evidence_ids_json=[record.evidence_id for record in evidence_records],
        payload_json=payload,
    )
