"""Create an EvidenceRecord from an Observation."""

from genus_core.models.evidence_record import EvidenceRecord
from genus_core.models.observation import Observation


def create_evidence_record(
    observation: Observation,
    *,
    truth_status: str = "observed",
    provenance: str = "user_input",
) -> EvidenceRecord:
    payload = {
        "observed_observation_type": observation.observation_type,
        "observation_payload": dict(observation.payload_json),
    }
    return EvidenceRecord(
        source_observation_id=observation.observation_id,
        truth_status=truth_status,
        provenance=provenance,
        payload_json=payload,
    )
