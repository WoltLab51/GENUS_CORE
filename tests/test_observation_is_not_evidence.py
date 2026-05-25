from genus_core.functions import create_evidence_record, observe_event
from genus_core.models import EvidenceRecord, Observation, WorldEvent


def test_observation_is_not_evidence() -> None:
    observation = observe_event(
        WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    )
    evidence = create_evidence_record(observation)

    assert isinstance(observation, Observation)
    assert isinstance(evidence, EvidenceRecord)
    assert not isinstance(observation, EvidenceRecord)
    assert evidence.source_observation_id == observation.observation_id
    assert evidence.truth_status == "observed"
