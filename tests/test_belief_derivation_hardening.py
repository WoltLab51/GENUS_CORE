import pytest

from genus_core.functions import (
    build_belief_state_snapshot,
    create_evidence_record,
    observe_event,
)
from genus_core.models import BeliefStateSnapshot, EvidenceRecord, WorldEvent
from genus_core.models.ledger_entry import LedgerEntry
from genus_core.models.observation_report import ObservationReport


def _evidence_for(
    event_type: str = "user_text",
    raw_text: str | None = "merk dir das: larumipsum",
    payload_json: dict | None = None,
    truth_status: str = "observed",
) -> EvidenceRecord:
    observation = observe_event(
        WorldEvent(event_type=event_type, raw_text=raw_text, payload_json=payload_json or {})
    )
    return create_evidence_record(observation, truth_status=truth_status)


def test_belief_derivation_rejects_non_evidence_record_input() -> None:
    with pytest.raises(TypeError, match="requires EvidenceRecord"):
        build_belief_state_snapshot([WorldEvent(event_type="user_text")])


@pytest.mark.parametrize("truth_status", ["derived", "rejected"])
def test_belief_derivation_rejects_non_observed_truth_status(
    truth_status: str,
) -> None:
    evidence = _evidence_for(truth_status=truth_status)

    with pytest.raises(ValueError, match="only accepts observed"):
        build_belief_state_snapshot([evidence])


def test_belief_derivation_rejects_missing_or_invalid_evidence_claim() -> None:
    evidence = _evidence_for()
    bad_payload = dict(evidence.payload_json)
    bad_payload["evidence_claim"] = "world_truth"
    bad_evidence = EvidenceRecord(
        source_observation_id=evidence.source_observation_id,
        truth_status="observed",
        provenance=evidence.provenance,
        payload_json=bad_payload,
    )

    with pytest.raises(ValueError, match="evidence_claim"):
        build_belief_state_snapshot([bad_evidence])


def test_belief_derivation_rejects_missing_observation_scope() -> None:
    evidence = _evidence_for()
    bad_payload = dict(evidence.payload_json)
    bad_payload.pop("observation_scope")
    bad_evidence = EvidenceRecord(
        source_observation_id=evidence.source_observation_id,
        truth_status="observed",
        provenance=evidence.provenance,
        payload_json=bad_payload,
    )

    with pytest.raises(ValueError, match="requires observation_scope"):
        build_belief_state_snapshot([bad_evidence])


def test_belief_derivation_rejects_unsupported_observation_type() -> None:
    evidence = _evidence_for()
    bad_payload = dict(evidence.payload_json)
    bad_payload["observed_observation_type"] = "future_observation"
    bad_evidence = EvidenceRecord(
        source_observation_id=evidence.source_observation_id,
        truth_status="observed",
        provenance=evidence.provenance,
        payload_json=bad_payload,
    )

    with pytest.raises(ValueError, match="Unsupported belief observation type"):
        build_belief_state_snapshot([bad_evidence])


def test_belief_derivation_rejects_mixed_scopes() -> None:
    memory_evidence = _evidence_for()
    input_evidence = _evidence_for(raw_text="")

    with pytest.raises(ValueError, match="mixed observation scopes"):
        build_belief_state_snapshot([memory_evidence, input_evidence])


def test_belief_derivation_preserves_all_source_evidence_ids_in_order() -> None:
    first = _evidence_for(
        event_type="memory_lookup_failed",
        raw_text=None,
        payload_json={"lookup_key": "alpha"},
    )
    second = _evidence_for(raw_text="merk dir das:")
    third = _evidence_for(raw_text="merk dir das: larumipsum")

    belief = build_belief_state_snapshot([first, second, third])

    assert belief.source_evidence_ids_json == [
        first.evidence_id,
        second.evidence_id,
        third.evidence_id,
    ]


def test_memory_request_evidence_derives_observed_memory_request() -> None:
    evidence = _evidence_for()

    belief = build_belief_state_snapshot([evidence])

    assert belief.payload_json["observed_memory_request"] is True
    assert belief.payload_json["observed_memory_content"] == "larumipsum"
    assert "pending_memory_request" not in belief.payload_json
    assert "candidate_content" not in belief.payload_json


@pytest.mark.parametrize(
    ("event_type", "raw_text", "payload_json"),
    [
        ("user_text", "", None),
        ("user_text", "merk dir das:", None),
        ("memory_lookup_failed", None, {"lookup_key": "alpha"}),
        ("guard_blocked_transition", None, {"guard": "foundation_boundary"}),
    ],
)
def test_non_memory_request_evidence_derives_no_observed_memory_request(
    event_type: str,
    raw_text: str | None,
    payload_json: dict | None,
) -> None:
    evidence = _evidence_for(
        event_type=event_type,
        raw_text=raw_text,
        payload_json=payload_json,
    )

    belief = build_belief_state_snapshot([evidence])

    assert belief.payload_json["observed_memory_request"] is False
    assert "pending_memory_request" not in belief.payload_json
    assert "candidate_content" not in belief.payload_json


def test_belief_payload_excludes_forbidden_fields_but_keeps_source_ids() -> None:
    evidence = _evidence_for()

    belief = build_belief_state_snapshot([evidence])

    forbidden_fields = {
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

    assert forbidden_fields.isdisjoint(belief.payload_json)
    assert belief.source_evidence_ids_json == [evidence.evidence_id]


def test_belief_derivation_creates_only_belief_snapshot() -> None:
    evidence = _evidence_for()

    belief = build_belief_state_snapshot([evidence])

    assert isinstance(belief, BeliefStateSnapshot)
    assert not isinstance(belief, EvidenceRecord)
    assert not isinstance(belief, LedgerEntry)
    assert not isinstance(belief, ObservationReport)
