from dataclasses import fields

from genus_core.functions import (
    build_belief_state_snapshot,
    create_evidence_record,
    observe_event,
)
from genus_core.models import WorldEvent
from genus_core.passive_boundary_relevance import (
    PassiveBoundaryRelevancePreview,
    build_passive_boundary_relevance_preview,
    create_passive_boundary_relevance_report,
)
from genus_core.passive_physics import build_passive_metric_snapshot
from genus_core.passive_transition import build_passive_transition_preview


def _preview(raw_text: str = "merk dir das: larumipsum") -> PassiveBoundaryRelevancePreview:
    observation = observe_event(WorldEvent(event_type="user_text", raw_text=raw_text))
    evidence = create_evidence_record(observation)
    belief = build_belief_state_snapshot([evidence])
    metrics = build_passive_metric_snapshot(belief)
    transition = build_passive_transition_preview(belief, metrics)
    return build_passive_boundary_relevance_preview(belief, metrics, transition)


def test_passive_boundary_relevance_report_summary_remains_descriptive_only() -> None:
    report = create_passive_boundary_relevance_report(_preview())
    lowered_summary = report.summary.lower()

    assert "passive boundary relevance" in lowered_summary
    for phrase in (
        "approved",
        "allowed",
        "blocked",
        "decision made",
        "policy result",
        "permission granted",
        "boundary evaluated",
        "reaction created",
        "memory written",
    ):
        assert phrase not in lowered_summary


def test_boundary_question_remains_neutral_runtime_question() -> None:
    preview = _preview()
    lowered_question = preview.boundary_question.lower()

    assert lowered_question.endswith("?")
    for word in (
        "should",
        "must",
        "allow",
        "block",
        "execute",
        "write",
        "approve",
        "recommend",
        "permit",
        "permission",
        "policy",
    ):
        assert f" {word} " not in f" {lowered_question} "


def test_observed_boundary_relevance_is_non_numeric_and_non_prioritizing() -> None:
    for raw_text in ("merk dir das: larumipsum", "hello"):
        preview = _preview(raw_text)

        assert isinstance(preview.observed_boundary_relevance, str)
        assert not preview.observed_boundary_relevance.isnumeric()
        for term in ("score", "rank", "priority", "severity", "weight"):
            assert term not in preview.observed_boundary_relevance


def test_passive_foundation_boundary_still_not_emitted() -> None:
    for raw_text in ("merk dir das: larumipsum", "hello"):
        preview = _preview(raw_text)

        assert preview.boundary_area in {"memory_boundary", "passive_preview_boundary"}
        assert preview.boundary_area != "passive_foundation_boundary"


def test_report_lineage_is_mirrored_only() -> None:
    preview = _preview()
    report = create_passive_boundary_relevance_report(preview)

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


def test_runtime_fields_and_payload_keys_do_not_contain_evaluation() -> None:
    preview = _preview()
    report = create_passive_boundary_relevance_report(preview)

    for field in fields(PassiveBoundaryRelevancePreview):
        assert "evaluation" not in field.name
    for key in report.payload_json:
        assert "evaluation" not in key
