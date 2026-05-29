import pytest

from genus_core.passive_transition import (
    PassiveTransitionPreview,
    PassiveTransitionReport,
)


def _preview() -> PassiveTransitionPreview:
    return PassiveTransitionPreview(
        source_state_id="state_1",
        source_metric_snapshot_id="pms_1",
        source_evidence_ids_json=["ev_1"],
        preview_type="memory_request_transition_tension_preview",
        observed_tension_summary="A passive memory-request tension is visible.",
        possible_future_question=(
            "Could a later governed boundary evaluate whether observed memory "
            "content raises a governed memory question?"
        ),
    )


def test_passive_transition_preview_accepts_allowed_shape() -> None:
    preview = _preview()

    assert preview.no_action_possible is True
    assert preview.no_decision_possible is True
    assert preview.preview_type == "memory_request_transition_tension_preview"
    assert preview.possible_future_question.endswith("?")


def test_passive_transition_preview_rejects_unknown_preview_type() -> None:
    with pytest.raises(ValueError, match="Invalid passive transition preview_type"):
        PassiveTransitionPreview(
            source_state_id="state_1",
            source_metric_snapshot_id="pms_1",
            source_evidence_ids_json=["ev_1"],
            preview_type="transition_candidate",
            observed_tension_summary="A passive tension is visible.",
            possible_future_question="Could a later governed boundary evaluate it?",
        )


def test_passive_transition_preview_requires_passive_no_action_flags() -> None:
    with pytest.raises(ValueError, match="no_action_possible=True"):
        PassiveTransitionPreview(
            source_state_id="state_1",
            source_metric_snapshot_id="pms_1",
            source_evidence_ids_json=["ev_1"],
            preview_type="no_visible_transition_tension_preview",
            observed_tension_summary="No passive tension is visible.",
            possible_future_question="Could a later governed boundary evaluate it?",
            no_action_possible=False,
        )

    with pytest.raises(ValueError, match="no_decision_possible=True"):
        PassiveTransitionPreview(
            source_state_id="state_1",
            source_metric_snapshot_id="pms_1",
            source_evidence_ids_json=["ev_1"],
            preview_type="no_visible_transition_tension_preview",
            observed_tension_summary="No passive tension is visible.",
            possible_future_question="Could a later governed boundary evaluate it?",
            no_decision_possible=False,
        )


@pytest.mark.parametrize(
    "word",
    ("should", "must", "allow", "block", "execute", "write", "approve", "recommend"),
)
def test_possible_future_question_rejects_forbidden_runtime_words(word: str) -> None:
    with pytest.raises(ValueError, match="forbidden runtime word"):
        PassiveTransitionPreview(
            source_state_id="state_1",
            source_metric_snapshot_id="pms_1",
            source_evidence_ids_json=["ev_1"],
            preview_type="no_visible_transition_tension_preview",
            observed_tension_summary="No passive tension is visible.",
            possible_future_question=f"Could a later boundary {word} this?",
        )


def test_possible_future_question_must_be_question_like() -> None:
    with pytest.raises(ValueError, match="question-like"):
        PassiveTransitionPreview(
            source_state_id="state_1",
            source_metric_snapshot_id="pms_1",
            source_evidence_ids_json=["ev_1"],
            preview_type="no_visible_transition_tension_preview",
            observed_tension_summary="No passive tension is visible.",
            possible_future_question="A later governed boundary could evaluate it.",
        )


def test_passive_transition_preview_rejects_extra_output_fields() -> None:
    with pytest.raises(TypeError):
        PassiveTransitionPreview(
            source_state_id="state_1",
            source_metric_snapshot_id="pms_1",
            source_evidence_ids_json=["ev_1"],
            preview_type="no_visible_transition_tension_preview",
            observed_tension_summary="No passive tension is visible.",
            possible_future_question="Could a later governed boundary evaluate it?",
            transition="forbidden",  # type: ignore[call-arg]
        )


@pytest.mark.parametrize(
    "field_name",
    (
        "transition",
        "transition_candidate",
        "target_state",
        "selected_transition",
        "proposed_transition",
        "candidate",
        "recommendation",
        "permission",
        "allow",
        "block",
        "decision",
        "action",
        "reaction",
        "memory_write",
        "truth",
    ),
)
def test_passive_transition_report_rejects_forbidden_payload_fields(
    field_name: str,
) -> None:
    preview = _preview()

    with pytest.raises(ValueError, match="forbidden fields"):
        PassiveTransitionReport(
            source_preview_id=preview.preview_id,
            summary="Passive preview report.",
            payload_json={field_name: "forbidden"},
        )


def test_passive_transition_report_accepts_descriptive_payload() -> None:
    preview = _preview()
    report = PassiveTransitionReport(
        source_preview_id=preview.preview_id,
        summary="Passive preview report.",
        payload_json={
            "no_action_possible": True,
            "no_decision_possible": True,
            "source_preview_id": preview.preview_id,
            "source_state_id": preview.source_state_id,
            "source_metric_snapshot_id": preview.source_metric_snapshot_id,
            "source_evidence_ids_json": preview.source_evidence_ids_json,
            "preview_type": preview.preview_type,
            "observed_tension_summary": preview.observed_tension_summary,
            "possible_future_question": preview.possible_future_question,
        },
    )

    assert report.payload_json["no_action_possible"] is True
    assert report.payload_json["no_decision_possible"] is True
