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
    PassiveMetricReport,
    PassiveMetricSnapshot,
    build_passive_metric_snapshot,
    create_passive_metric_report,
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


def _metrics_by_name(snapshot: PassiveMetricSnapshot) -> dict[str, dict]:
    return {metric["metric_name"]: metric for metric in snapshot.metrics_json}


def test_build_passive_metric_snapshot_accepts_only_belief_state_snapshot() -> None:
    with pytest.raises(TypeError, match="requires BeliefStateSnapshot"):
        build_passive_metric_snapshot("not a belief")  # type: ignore[arg-type]


def test_memory_request_belief_derives_first_passive_metrics() -> None:
    belief = _memory_request_belief()

    snapshot = build_passive_metric_snapshot(belief)
    metrics = _metrics_by_name(snapshot)

    assert set(metrics) == {"pressure", "inhibition", "stability"}
    assert metrics["pressure"]["assessment_status"] == "assessed"
    assert metrics["pressure"]["level"] == "medium"
    assert metrics["inhibition"]["assessment_status"] == "assessed"
    assert metrics["inhibition"]["level"] == "high"
    assert metrics["stability"]["assessment_status"] == "assessed"
    assert metrics["stability"]["level"] == "high"
    for metric in metrics.values():
        assert metric["source_state_id"] == belief.state_id
        assert metric["source_evidence_ids_json"] == belief.source_evidence_ids_json


def test_non_memory_request_belief_derives_no_pressure_and_no_inhibition() -> None:
    belief = _unknown_input_belief()

    snapshot = build_passive_metric_snapshot(belief)
    metrics = _metrics_by_name(snapshot)

    assert metrics["pressure"]["assessment_status"] == "assessed"
    assert metrics["pressure"]["level"] == "none"
    assert metrics["inhibition"]["assessment_status"] == "not_applicable"
    assert metrics["inhibition"]["level"] == "none"
    assert metrics["stability"]["assessment_status"] == "assessed"
    assert metrics["stability"]["level"] == "high"


def test_invalid_lineage_derives_insufficient_stability_only() -> None:
    belief = BeliefStateSnapshot(
        scope="memory",
        source_evidence_ids_json=["   "],
        payload_json={"observed_memory_request": True},
    )

    snapshot = build_passive_metric_snapshot(belief)
    metrics = _metrics_by_name(snapshot)

    assert metrics["pressure"]["level"] == "medium"
    assert metrics["inhibition"]["level"] == "high"
    assert metrics["stability"]["assessment_status"] == "insufficient_input"
    assert metrics["stability"]["level"] == "none"


def test_passive_metric_snapshot_has_no_foundation_or_action_side_effect_objects() -> None:
    belief = _memory_request_belief()

    snapshot = build_passive_metric_snapshot(belief)

    assert isinstance(snapshot, PassiveMetricSnapshot)
    assert not isinstance(snapshot, EvidenceRecord)
    assert not isinstance(snapshot, LedgerEntry)
    assert not isinstance(snapshot, BeliefStateSnapshot)
    assert not isinstance(snapshot, ObservationReport)
    assert not isinstance(snapshot, PassiveMetricReport)


def test_create_passive_metric_report_accepts_only_passive_metric_snapshot() -> None:
    with pytest.raises(TypeError, match="requires PassiveMetricSnapshot"):
        create_passive_metric_report("not a snapshot")  # type: ignore[arg-type]


def test_passive_metric_report_is_descriptive_only() -> None:
    snapshot = build_passive_metric_snapshot(_memory_request_belief())

    report = create_passive_metric_report(snapshot)

    assert isinstance(report, PassiveMetricReport)
    assert report.payload_json["no_action_possible"] is True
    assert report.payload_json["source_snapshot_id"] == snapshot.snapshot_id
    assert report.payload_json["source_state_id"] == snapshot.source_state_id
    assert report.payload_json["source_evidence_ids_json"] == (
        snapshot.source_evidence_ids_json
    )
    assert report.payload_json["passive_metric_outputs"] == snapshot.metrics_json
    for field_name in (
        "decision",
        "action",
        "reaction",
        "transition",
        "constraint",
        "memory_write",
        "truth",
    ):
        assert field_name not in report.payload_json


def test_passive_physics_adds_no_sqlite_tables(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")

    table_names = {
        row["name"]
        for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'"
        ).fetchall()
    }

    assert table_names == {"evidence_records", "ledger_entries"}
