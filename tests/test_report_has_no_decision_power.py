import pytest

from genus_core.functions import (
    build_belief_state_snapshot,
    create_evidence_record,
    create_observation_report,
    observe_event,
)
from genus_core.models import ObservationReport, WorldEvent
from genus_core.models.observation_report import FORBIDDEN_REPORT_FIELDS


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
    for field_name in FORBIDDEN_REPORT_FIELDS:
        assert not hasattr(report, field_name)
        assert field_name not in report.payload_json


def test_report_rejects_forbidden_fields() -> None:
    with pytest.raises(ValueError, match="forbidden fields"):
        ObservationReport(
            source_state_id="state_1",
            summary="Invalid report",
            payload_json={"decision": "approve"},
        )
