import pytest

from genus_core.passive_boundary_relevance import (
    ALLOWED_BOUNDARY_AREAS,
    PassiveBoundaryRelevancePreview,
    PassiveBoundaryRelevanceReport,
)


def _preview() -> PassiveBoundaryRelevancePreview:
    return PassiveBoundaryRelevancePreview(
        source_state_id="state_1",
        source_metric_snapshot_id="pms_1",
        source_transition_preview_id="ptp_1",
        source_evidence_ids_json=["ev_1"],
        boundary_question=(
            "Could a later governed boundary describe whether observed memory "
            "content raises a memory boundary question?"
        ),
        boundary_area="memory_boundary",
        observed_boundary_relevance="memory_request_relevance_observed",
    )


def test_passive_boundary_relevance_preview_accepts_allowed_shape() -> None:
    preview = _preview()

    assert preview.boundary_area == "memory_boundary"
    assert preview.observed_boundary_relevance == "memory_request_relevance_observed"
    assert preview.no_decision_possible is True
    assert preview.no_action_possible is True
    assert preview.boundary_question.endswith("?")


def test_boundary_area_enum_includes_spec_only_foundation_area() -> None:
    assert ALLOWED_BOUNDARY_AREAS == {
        "memory_boundary",
        "passive_preview_boundary",
        "passive_foundation_boundary",
    }


def test_passive_foundation_boundary_is_not_emitted_in_v0_4_1() -> None:
    with pytest.raises(ValueError, match="not emitted in v0.4.1"):
        PassiveBoundaryRelevancePreview(
            source_state_id="state_1",
            source_metric_snapshot_id="pms_1",
            source_transition_preview_id="ptp_1",
            source_evidence_ids_json=["ev_1"],
            boundary_question="Could a later governed boundary describe it?",
            boundary_area="passive_foundation_boundary",
            observed_boundary_relevance="no_boundary_relevance_observed",
        )


def test_passive_boundary_relevance_preview_rejects_unknown_area() -> None:
    with pytest.raises(ValueError, match="Invalid boundary_area"):
        PassiveBoundaryRelevancePreview(
            source_state_id="state_1",
            source_metric_snapshot_id="pms_1",
            source_transition_preview_id="ptp_1",
            source_evidence_ids_json=["ev_1"],
            boundary_question="Could a later governed boundary describe it?",
            boundary_area="policy_boundary",
            observed_boundary_relevance="no_boundary_relevance_observed",
        )


def test_passive_boundary_relevance_preview_rejects_unknown_relevance() -> None:
    with pytest.raises(ValueError, match="Invalid observed_boundary_relevance"):
        PassiveBoundaryRelevancePreview(
            source_state_id="state_1",
            source_metric_snapshot_id="pms_1",
            source_transition_preview_id="ptp_1",
            source_evidence_ids_json=["ev_1"],
            boundary_question="Could a later governed boundary describe it?",
            boundary_area="passive_preview_boundary",
            observed_boundary_relevance="priority_relevance",
        )


@pytest.mark.parametrize(
    "word",
    (
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
    ),
)
def test_boundary_question_rejects_forbidden_runtime_words(word: str) -> None:
    with pytest.raises(ValueError, match="forbidden runtime word"):
        PassiveBoundaryRelevancePreview(
            source_state_id="state_1",
            source_metric_snapshot_id="pms_1",
            source_transition_preview_id="ptp_1",
            source_evidence_ids_json=["ev_1"],
            boundary_question=f"Could a later governed boundary {word} it?",
            boundary_area="passive_preview_boundary",
            observed_boundary_relevance="no_boundary_relevance_observed",
        )


def test_boundary_question_must_be_question_like() -> None:
    with pytest.raises(ValueError, match="question-like"):
        PassiveBoundaryRelevancePreview(
            source_state_id="state_1",
            source_metric_snapshot_id="pms_1",
            source_transition_preview_id="ptp_1",
            source_evidence_ids_json=["ev_1"],
            boundary_question="A later governed boundary can describe it.",
            boundary_area="passive_preview_boundary",
            observed_boundary_relevance="no_boundary_relevance_observed",
        )


@pytest.mark.parametrize(
    "field_name",
    (
        "permission",
        "policy",
        "policy_result",
        "policy_status",
        "authorization",
        "permission_status",
        "allow",
        "block",
        "approve",
        "reject",
        "recommendation",
        "score",
        "rank",
        "priority",
        "severity",
        "weight",
        "execute",
        "decision",
        "action",
        "reaction",
        "memory_write",
        "memory",
        "memory_object",
        "truth",
        "transition",
        "transition_candidate",
        "candidate",
        "constraint",
        "constraint_decision",
        "target_state",
        "selected_transition",
        "proposed_transition",
        "llm",
        "worker",
        "graphdb",
        "runtime_shape",
        "evaluation",
        "no_boundary_evaluation_possible",
    ),
)
def test_passive_boundary_relevance_report_rejects_forbidden_payload_fields(
    field_name: str,
) -> None:
    preview = _preview()

    with pytest.raises(ValueError, match="forbidden fields"):
        PassiveBoundaryRelevanceReport(
            source_relevance_preview_id=preview.preview_id,
            summary="Passive boundary relevance report.",
            payload_json={field_name: "forbidden"},
        )


def test_passive_boundary_relevance_report_accepts_descriptive_payload() -> None:
    preview = _preview()
    report = PassiveBoundaryRelevanceReport(
        source_relevance_preview_id=preview.preview_id,
        summary="Passive boundary relevance report.",
        payload_json={
            "source_relevance_preview_id": preview.preview_id,
            "source_state_id": preview.source_state_id,
            "source_metric_snapshot_id": preview.source_metric_snapshot_id,
            "source_transition_preview_id": preview.source_transition_preview_id,
            "source_evidence_ids_json": preview.source_evidence_ids_json,
            "boundary_question": preview.boundary_question,
            "boundary_area": preview.boundary_area,
            "observed_boundary_relevance": preview.observed_boundary_relevance,
            "no_decision_possible": True,
            "no_action_possible": True,
        },
    )

    assert report.payload_json["no_decision_possible"] is True
    assert report.payload_json["no_action_possible"] is True
