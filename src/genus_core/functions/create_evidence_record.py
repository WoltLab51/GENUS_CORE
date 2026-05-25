"""Create an EvidenceRecord from an Observation."""

from genus_core.models.evidence_record import EvidenceRecord
from genus_core.models.observation import Observation


def create_evidence_record(
    observation: Observation,
    *,
    truth_status: str = "observed",
    provenance: str = "user_input",
) -> EvidenceRecord:
    if not isinstance(observation, Observation):
        raise TypeError("create_evidence_record requires an Observation")

    payload = {
        "evidence_claim": "observation_recorded",
        "observed_observation_type": observation.observation_type,
        "observation_payload": dict(observation.payload_json),
        "observation_confidence": observation.confidence,
        "observation_scope": observation.scope,
    }
    return EvidenceRecord(
        source_observation_id=observation.observation_id,
        truth_status=truth_status,
        provenance=provenance,
        payload_json=payload,
    )
