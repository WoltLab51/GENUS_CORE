import pytest

from genus_core.functions import (
    build_belief_state_snapshot,
    create_evidence_record,
    create_observation_report,
    observe_event,
)
from genus_core.models import (
    BeliefStateSnapshot,
    EvidenceRecord,
    LedgerEntry,
    ObservationReport,
    WorldEvent,
)
from genus_core.models.observation_report import FORBIDDEN_REPORT_FIELDS


FORBIDDEN_SUMMARY_PHRASES = (
    "approved",
    "allowed",
    "decided",
    "execute",
    "action taken",
    "memory written",
    "reaction created",
)


def test_report_has_no_decision_power() -> None:
    observation = observe_event(
        WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    )
    evidence = create_evidence_record(observation)
    belief = build_belief_state_snapshot([evidence])
    report = create_observation_report(belief)

    assert not isinstance(report, type(belief))
    assert report.source_state_id == belief.state_id
    assert report.payload_json["no_action_possible"] is True
    assert report.payload_json["observed_memory_request"] is True
    assert report.payload_json["observed_memory_content"] == "larumipsum"
    assert "pending_memory_request" not in report.payload_json
    assert "candidate_content" not in report.payload_json
    assert report.payload_json["source_evidence_ids"] == [evidence.evidence_id]
    for field_name in FORBIDDEN_REPORT_FIELDS:
        assert not hasattr(report, field_name)
        assert field_name not in report.payload_json


def test_create_observation_report_rejects_non_belief_input() -> None:
    with pytest.raises(TypeError, match="requires BeliefStateSnapshot"):
        create_observation_report("not a belief")  # type: ignore[arg-type]


@pytest.mark.parametrize("field_name", sorted(FORBIDDEN_REPORT_FIELDS))
def test_report_rejects_forbidden_fields(field_name: str) -> None:
    with pytest.raises(ValueError, match="forbidden fields"):
        ObservationReport(
            source_state_id="state_1",
            summary="Invalid report",
            payload_json={field_name: "unsafe"},
        )


@pytest.mark.parametrize(
    "field_name",
    ["truth", "truth_status", "world_truth", "evidence_claim"],
)
def test_report_payload_contains_no_truth_or_evidence_claim_fields(
    field_name: str,
) -> None:
    observation = observe_event(
        WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    )
    evidence = create_evidence_record(observation)
    belief = build_belief_state_snapshot([evidence])
    report = create_observation_report(belief)

    assert field_name not in report.payload_json


@pytest.mark.parametrize("field_name", sorted(FORBIDDEN_REPORT_FIELDS))
def test_create_observation_report_rejects_unsafe_belief_payload(
    field_name: str,
) -> None:
    belief = BeliefStateSnapshot(
        scope="memory",
        source_evidence_ids_json=["ev_1"],
        payload_json={field_name: "unsafe"},
    )

    with pytest.raises(ValueError, match="cannot be reflected"):
        create_observation_report(belief)


def test_report_summary_remains_descriptive() -> None:
    observation = observe_event(
        WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    )
    evidence = create_evidence_record(observation)
    belief = build_belief_state_snapshot([evidence])
    report = create_observation_report(belief)

    assert "observed as a derived belief" in report.summary
    assert "passive foundation boundary" in report.summary
    assert "pending" not in report.summary.lower()
    lowered_summary = report.summary.lower()
    for phrase in FORBIDDEN_SUMMARY_PHRASES:
        assert phrase not in lowered_summary


def test_report_creation_creates_only_observation_report() -> None:
    observation = observe_event(
        WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    )
    evidence = create_evidence_record(observation)
    belief = build_belief_state_snapshot([evidence])
    report = create_observation_report(belief)

    assert isinstance(report, ObservationReport)
    assert not isinstance(report, EvidenceRecord)
    assert not isinstance(report, LedgerEntry)
    assert not isinstance(report, BeliefStateSnapshot)
