import pytest

from genus_core.functions import (
    build_belief_state_snapshot,
    create_evidence_record,
    observe_event,
)
from genus_core.models import BeliefStateSnapshot, WorldEvent
from genus_core.passive_boundary_relevance import (
    PassiveBoundaryRelevancePreview,
    PassiveBoundaryRelevanceReport,
    build_passive_boundary_relevance_preview,
    create_passive_boundary_relevance_report,
)
from genus_core.passive_physics import PassiveMetricSnapshot, build_passive_metric_snapshot
from genus_core.passive_transition import (
    PassiveTransitionPreview,
    build_passive_transition_preview,
)
from genus_core.truth import connect


def _belief(raw_text: str) -> BeliefStateSnapshot:
    observation = observe_event(WorldEvent(event_type="user_text", raw_text=raw_text))
    evidence = create_evidence_record(observation)
    return build_belief_state_snapshot([evidence])


def _passive_chain(raw_text: str) -> tuple[
    BeliefStateSnapshot,
    PassiveMetricSnapshot,
    PassiveTransitionPreview,
]:
    belief = _belief(raw_text)
    metrics = build_passive_metric_snapshot(belief)
    transition = build_passive_transition_preview(belief, metrics)
    return belief, metrics, transition


def test_build_passive_boundary_relevance_preview_accepts_only_passive_inputs() -> None:
    belief, metrics, transition = _passive_chain("merk dir das: larumipsum")

    with pytest.raises(TypeError, match="requires BeliefStateSnapshot"):
        build_passive_boundary_relevance_preview("not belief", metrics, transition)  # type: ignore[arg-type]

    with pytest.raises(TypeError, match="requires PassiveMetricSnapshot"):
        build_passive_boundary_relevance_preview(belief, "not metrics", transition)  # type: ignore[arg-type]

    with pytest.raises(TypeError, match="requires PassiveTransitionPreview"):
        build_passive_boundary_relevance_preview(belief, metrics, "not preview")  # type: ignore[arg-type]


def test_build_passive_boundary_relevance_preview_rejects_mismatched_state_id() -> None:
    belief, metrics, transition = _passive_chain("merk dir das: larumipsum")
    object.__setattr__(transition, "source_state_id", "state_other")

    with pytest.raises(ValueError, match="source_state_id must match"):
        build_passive_boundary_relevance_preview(belief, metrics, transition)


def test_build_passive_boundary_relevance_preview_rejects_mismatched_lineage() -> None:
    belief, metrics, transition = _passive_chain("merk dir das: larumipsum")
    object.__setattr__(metrics, "source_evidence_ids_json", ["ev_other"])

    with pytest.raises(ValueError, match="evidence lineage must match"):
        build_passive_boundary_relevance_preview(belief, metrics, transition)


def test_build_passive_boundary_relevance_preview_rejects_mismatched_metric_snapshot() -> None:
    belief, metrics, transition = _passive_chain("merk dir das: larumipsum")
    object.__setattr__(transition, "source_metric_snapshot_id", "pms_other")

    with pytest.raises(ValueError, match="source_metric_snapshot_id must match"):
        build_passive_boundary_relevance_preview(belief, metrics, transition)


def test_memory_request_tension_creates_memory_boundary_relevance_preview() -> None:
    belief, metrics, transition = _passive_chain("merk dir das: larumipsum")

    preview = build_passive_boundary_relevance_preview(belief, metrics, transition)

    assert isinstance(preview, PassiveBoundaryRelevancePreview)
    assert preview.boundary_area == "memory_boundary"
    assert preview.observed_boundary_relevance == "memory_request_relevance_observed"
    assert preview.source_state_id == belief.state_id
    assert preview.source_metric_snapshot_id == metrics.snapshot_id
    assert preview.source_transition_preview_id == transition.preview_id
    assert preview.source_evidence_ids_json == belief.source_evidence_ids_json
    assert preview.no_decision_possible is True
    assert preview.no_action_possible is True


def test_neutral_transition_preview_creates_passive_preview_boundary_relevance() -> None:
    belief, metrics, transition = _passive_chain("hello")

    preview = build_passive_boundary_relevance_preview(belief, metrics, transition)

    assert preview.boundary_area == "passive_preview_boundary"
    assert preview.observed_boundary_relevance == "no_boundary_relevance_observed"
    assert preview.source_evidence_ids_json == belief.source_evidence_ids_json


def test_passive_foundation_boundary_is_not_emitted_by_derivation() -> None:
    belief, metrics, transition = _passive_chain("merk dir das: larumipsum")

    preview = build_passive_boundary_relevance_preview(belief, metrics, transition)

    assert preview.boundary_area != "passive_foundation_boundary"


def test_boundary_relevance_preview_does_not_mutate_inputs() -> None:
    belief, metrics, transition = _passive_chain("merk dir das: larumipsum")
    belief_payload = dict(belief.payload_json)
    metric_outputs = [dict(metric) for metric in metrics.metrics_json]
    transition_question = transition.possible_future_question

    build_passive_boundary_relevance_preview(belief, metrics, transition)

    assert belief.payload_json == belief_payload
    assert metrics.metrics_json == metric_outputs
    assert transition.possible_future_question == transition_question


def test_create_passive_boundary_relevance_report_accepts_only_preview() -> None:
    with pytest.raises(TypeError, match="requires PassiveBoundaryRelevancePreview"):
        create_passive_boundary_relevance_report("not preview")  # type: ignore[arg-type]


def test_passive_boundary_relevance_report_mirrors_preview_lineage_only() -> None:
    belief, metrics, transition = _passive_chain("merk dir das: larumipsum")
    preview = build_passive_boundary_relevance_preview(belief, metrics, transition)

    report = create_passive_boundary_relevance_report(preview)

    assert isinstance(report, PassiveBoundaryRelevanceReport)
    assert report.source_relevance_preview_id == preview.preview_id
    assert report.payload_json["source_relevance_preview_id"] == preview.preview_id
    assert report.payload_json["source_state_id"] == preview.source_state_id
    assert report.payload_json["source_metric_snapshot_id"] == (
        preview.source_metric_snapshot_id
    )
    assert report.payload_json["source_transition_preview_id"] == (
        preview.source_transition_preview_id
    )
    assert report.payload_json["source_evidence_ids_json"] == (
        preview.source_evidence_ids_json
    )


def test_passive_boundary_relevance_adds_no_sqlite_tables(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")
    tables = {
        row["name"]
        for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'"
        ).fetchall()
    }

    assert tables == {"evidence_records", "ledger_entries"}
