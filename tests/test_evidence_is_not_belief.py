import pytest

from genus_core.functions import (
    build_belief_state_snapshot,
    create_evidence_record,
    observe_event,
)
from genus_core.models import BeliefStateSnapshot, EvidenceRecord, Observation, WorldEvent
from genus_core.models.ledger_entry import LedgerEntry
from genus_core.models.observation_report import ObservationReport
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


def test_evidence_payload_records_observation_without_claiming_world_truth() -> None:
    observation = observe_event(
        WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    )
    evidence = create_evidence_record(observation)

    assert evidence.payload_json["evidence_claim"] == "observation_recorded"
    assert evidence.payload_json["observed_observation_type"] == (
        "memory_request_observed"
    )
    assert evidence.payload_json["observation_payload"] == {
        "observed_memory_content": "larumipsum"
    }
    assert evidence.payload_json["observation_confidence"] == "high"
    assert evidence.payload_json["observation_scope"] == "memory"


def test_evidence_payload_excludes_belief_decision_and_action_fields() -> None:
    observation = observe_event(
        WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    )
    evidence = create_evidence_record(observation)

    forbidden_fields = {
        "pending_memory_request",
        "observed_memory_request",
        "decision",
        "action",
        "reaction",
        "memory_write",
    }

    assert forbidden_fields.isdisjoint(evidence.payload_json)


def test_create_evidence_record_accepts_only_observation() -> None:
    with pytest.raises(TypeError, match="requires an Observation"):
        create_evidence_record(WorldEvent(event_type="user_text"))


def test_evidence_creation_has_no_epistemic_side_effect_objects() -> None:
    observation = observe_event(
        WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    )
    evidence = create_evidence_record(observation)

    assert isinstance(observation, Observation)
    assert isinstance(evidence, EvidenceRecord)
    assert not isinstance(evidence, LedgerEntry)
    assert not isinstance(evidence, BeliefStateSnapshot)
    assert not isinstance(evidence, ObservationReport)
