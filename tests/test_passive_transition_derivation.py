import pytest

from genus_core.functions import (
    build_belief_state_snapshot,
    create_evidence_record,
    observe_event,
)
from genus_core.models import (
    BeliefStateSnapshot,
    EvidenceRecord,
    LedgerEntry,
    ObservationReport,
    WorldEvent,
)
from genus_core.passive_physics import (
    PassiveMetricSnapshot,
    build_passive_metric_snapshot,
)
from genus_core.passive_transition import (
    PassiveTransitionPreview,
    PassiveTransitionReport,
    build_passive_transition_preview,
    create_passive_transition_report,
)
from genus_core.truth import connect


def _memory_request_belief() -> BeliefStateSnapshot:
    observation = observe_event(
        WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    )
    evidence = create_evidence_record(observation)
    return build_belief_state_snapshot([evidence])


def _unknown_input_belief() -> BeliefStateSnapshot:
    observation = observe_event(WorldEvent(event_type="user_text", raw_text="hello"))
    evidence = create_evidence_record(observation)
    return build_belief_state_snapshot([evidence])


def test_build_passive_transition_preview_accepts_only_passive_inputs() -> None:
    belief = _memory_request_belief()
    metrics = build_passive_metric_snapshot(belief)

    with pytest.raises(TypeError, match="requires BeliefStateSnapshot"):
        build_passive_transition_preview("not a belief", metrics)  # type: ignore[arg-type]

    with pytest.raises(TypeError, match="requires PassiveMetricSnapshot"):
        build_passive_transition_preview(belief, "not metrics")  # type: ignore[arg-type]


def test_build_passive_transition_preview_rejects_mismatched_state_id() -> None:
    belief = _memory_request_belief()
    metrics = build_passive_metric_snapshot(belief)
    object.__setattr__(metrics, "source_state_id", "state_other")

    with pytest.raises(ValueError, match="source_state_id must match"):
        build_passive_transition_preview(belief, metrics)


def test_build_passive_transition_preview_rejects_mismatched_lineage() -> None:
    belief = _memory_request_belief()
    metrics = build_passive_metric_snapshot(belief)
    object.__setattr__(metrics, "source_evidence_ids_json", ["ev_other"])

    with pytest.raises(ValueError, match="evidence lineage must match"):
        build_passive_transition_preview(belief, metrics)


def test_memory_request_metrics_create_passive_tension_preview() -> None:
    belief = _memory_request_belief()
    metrics = build_passive_metric_snapshot(belief)

    preview = build_passive_transition_preview(belief, metrics)

    assert isinstance(preview, PassiveTransitionPreview)
    assert preview.preview_type == "memory_request_transition_tension_preview"
    assert preview.source_state_id == belief.state_id
    assert preview.source_metric_snapshot_id == metrics.snapshot_id
    assert preview.source_evidence_ids_json == belief.source_evidence_ids_json
    assert preview.no_action_possible is True
    assert preview.no_decision_possible is True
    assert "?" in preview.possible_future_question


def test_no_visible_tension_preview_for_neutral_metrics() -> None:
    belief = _unknown_input_belief()
    metrics = build_passive_metric_snapshot(belief)

    preview = build_passive_transition_preview(belief, metrics)

    assert preview.preview_type == "no_visible_transition_tension_preview"
    assert preview.source_evidence_ids_json == belief.source_evidence_ids_json
    assert preview.no_action_possible is True
    assert preview.no_decision_possible is True


def test_passive_transition_preview_has_no_foundation_or_action_side_effect_objects() -> None:
    belief = _memory_request_belief()
    metrics = build_passive_metric_snapshot(belief)

    preview = build_passive_transition_preview(belief, metrics)

    assert not isinstance(preview, EvidenceRecord)
    assert not isinstance(preview, LedgerEntry)
    assert not isinstance(preview, BeliefStateSnapshot)
    assert not isinstance(preview, ObservationReport)
    assert not isinstance(preview, PassiveMetricSnapshot)
    assert not isinstance(preview, PassiveTransitionReport)


def test_build_passive_transition_preview_does_not_mutate_inputs() -> None:
    belief = _memory_request_belief()
    metrics = build_passive_metric_snapshot(belief)
    belief_payload = dict(belief.payload_json)
    metric_outputs = [dict(metric) for metric in metrics.metrics_json]

    build_passive_transition_preview(belief, metrics)

    assert belief.payload_json == belief_payload
    assert metrics.metrics_json == metric_outputs


def test_create_passive_transition_report_accepts_only_preview() -> None:
    with pytest.raises(TypeError, match="requires PassiveTransitionPreview"):
        create_passive_transition_report("not a preview")  # type: ignore[arg-type]


def test_passive_transition_report_is_descriptive_only() -> None:
    belief = _memory_request_belief()
    metrics = build_passive_metric_snapshot(belief)
    preview = build_passive_transition_preview(belief, metrics)

    report = create_passive_transition_report(preview)

    assert isinstance(report, PassiveTransitionReport)
    assert report.payload_json["no_action_possible"] is True
    assert report.payload_json["no_decision_possible"] is True
    assert report.payload_json["source_preview_id"] == preview.preview_id
    assert report.payload_json["source_state_id"] == preview.source_state_id
    assert report.payload_json["source_metric_snapshot_id"] == (
        preview.source_metric_snapshot_id
    )
    assert report.payload_json["source_evidence_ids_json"] == (
        preview.source_evidence_ids_json
    )
    for field_name in (
        "transition",
        "transition_candidate",
        "decision",
        "action",
        "constraint",
        "reaction",
        "candidate",
        "memory_write",
        "truth",
        "permission",
        "recommendation",
    ):
        assert field_name not in report.payload_json


def test_passive_transition_adds_no_sqlite_tables(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")

    table_names = {
        row["name"]
        for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'"
        ).fetchall()
    }

    assert table_names == {"evidence_records", "ledger_entries"}
