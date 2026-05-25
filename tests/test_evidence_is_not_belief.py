from genus_core.functions import (
    build_belief_state_snapshot,
    create_evidence_record,
    observe_event,
)
from genus_core.models import BeliefStateSnapshot, EvidenceRecord, WorldEvent
from genus_core.truth import connect, fetch_evidence_record, save_evidence_record


def test_evidence_is_not_belief(tmp_path) -> None:
    observation = observe_event(
        WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    )
    evidence = create_evidence_record(observation)
    belief = build_belief_state_snapshot([evidence])

    assert isinstance(evidence, EvidenceRecord)
    assert isinstance(belief, BeliefStateSnapshot)
    assert not isinstance(evidence, BeliefStateSnapshot)
    assert belief.source_evidence_ids_json == [evidence.evidence_id]

    connection = connect(tmp_path / "truth.sqlite3")
    save_evidence_record(connection, evidence)
    stored = fetch_evidence_record(connection, evidence.evidence_id)

    assert stored is not None
    assert stored["evidence_id"] == evidence.evidence_id
    assert stored["truth_status"] == "observed"
