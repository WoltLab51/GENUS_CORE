import pytest

from genus_core.functions import (
    build_belief_state_snapshot,
    create_evidence_record,
    observe_event,
)
from genus_core.models import BeliefStateSnapshot, WorldEvent


def test_belief_requires_evidence() -> None:
    with pytest.raises(ValueError, match="requires at least one EvidenceRecord"):
        BeliefStateSnapshot(scope="memory", source_evidence_ids_json=[])

    with pytest.raises(ValueError, match="Cannot build belief without evidence"):
        build_belief_state_snapshot([])


def test_belief_references_evidence_ids() -> None:
    observation = observe_event(
        WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    )
    evidence = create_evidence_record(observation)
    belief = build_belief_state_snapshot([evidence])

    assert belief.source_evidence_ids_json == [evidence.evidence_id]
    assert belief.payload_json["pending_memory_request"] is True
    assert belief.payload_json["candidate_content"] == "larumipsum"
