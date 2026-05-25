import pytest

from genus_core.models import BeliefStateSnapshot, EvidenceRecord, Observation
from genus_core.models.observation_report import (
    FORBIDDEN_REPORT_FIELDS,
    ObservationReport,
)


def test_observation_rejects_invalid_confidence() -> None:
    with pytest.raises(ValueError, match="Invalid confidence"):
        Observation(
            source_event_id="evt_1",
            observation_type="unknown_input_observed",
            scope="input",
            confidence="certain",
        )


def test_observation_rejects_invalid_scope() -> None:
    with pytest.raises(ValueError, match="Invalid scope"):
        Observation(
            source_event_id="evt_1",
            observation_type="unknown_input_observed",
            scope="decision",
            confidence="low",
        )


def test_evidence_record_rejects_invalid_truth_status() -> None:
    with pytest.raises(ValueError, match="Invalid truth_status"):
        EvidenceRecord(
            source_observation_id="obs_1",
            truth_status="true",
            provenance="user_input",
        )


def test_evidence_record_rejects_invalid_provenance() -> None:
    with pytest.raises(ValueError, match="Invalid provenance"):
        EvidenceRecord(
            source_observation_id="obs_1",
            truth_status="observed",
            provenance="rumor",
        )


def test_belief_state_snapshot_rejects_empty_evidence_ids() -> None:
    with pytest.raises(ValueError, match="requires at least one EvidenceRecord"):
        BeliefStateSnapshot(scope="memory", source_evidence_ids_json=[])


@pytest.mark.parametrize("field_name", sorted(FORBIDDEN_REPORT_FIELDS))
def test_observation_report_rejects_every_forbidden_payload_field(
    field_name: str,
) -> None:
    with pytest.raises(ValueError, match="forbidden fields"):
        ObservationReport(
            source_state_id="state_1",
            summary="Invalid report",
            payload_json={field_name: True},
        )
