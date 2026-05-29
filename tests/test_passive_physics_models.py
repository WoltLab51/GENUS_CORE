import pytest

from genus_core.passive_physics import PassiveMetricReport, PassiveMetricSnapshot
from genus_core.passive_physics.models import ALLOWED_METRIC_OUTPUT_FIELDS


def _metric_output(
    metric_name: str = "pressure",
    level: str = "none",
    assessment_status: str = "assessed",
) -> dict:
    return {
        "metric_name": metric_name,
        "level": level,
        "assessment_status": assessment_status,
        "explanation": "descriptive only",
        "source_state_id": "state_1",
        "source_evidence_ids_json": ["ev_1"],
    }


def test_passive_metric_snapshot_accepts_only_first_metric_names() -> None:
    for metric_name in ("pressure", "inhibition", "stability"):
        snapshot = PassiveMetricSnapshot(
            source_state_id="state_1",
            source_evidence_ids_json=["ev_1"],
            metrics_json=[_metric_output(metric_name=metric_name)],
        )

        assert snapshot.metrics_json[0]["metric_name"] == metric_name


@pytest.mark.parametrize("metric_name", ["cost", "potential", "future_metric"])
def test_passive_metric_snapshot_rejects_excluded_or_unknown_metric_names(
    metric_name: str,
) -> None:
    with pytest.raises(ValueError, match="Invalid passive metric name"):
        PassiveMetricSnapshot(
            source_state_id="state_1",
            source_evidence_ids_json=["ev_1"],
            metrics_json=[_metric_output(metric_name=metric_name)],
        )


@pytest.mark.parametrize("level", ["none", "low", "medium", "high"])
def test_passive_metric_snapshot_accepts_allowed_levels(level: str) -> None:
    snapshot = PassiveMetricSnapshot(
        source_state_id="state_1",
        source_evidence_ids_json=["ev_1"],
        metrics_json=[_metric_output(level=level)],
    )

    assert snapshot.metrics_json[0]["level"] == level


@pytest.mark.parametrize(
    "assessment_status", ["assessed", "insufficient_input", "not_applicable"]
)
def test_passive_metric_snapshot_accepts_allowed_assessment_status(
    assessment_status: str,
) -> None:
    snapshot = PassiveMetricSnapshot(
        source_state_id="state_1",
        source_evidence_ids_json=["ev_1"],
        metrics_json=[
            _metric_output(level="none", assessment_status=assessment_status)
        ],
    )

    assert snapshot.metrics_json[0]["assessment_status"] == assessment_status


@pytest.mark.parametrize(
    ("assessment_status", "level"),
    [
        ("insufficient_input", "low"),
        ("insufficient_input", "medium"),
        ("insufficient_input", "high"),
        ("not_applicable", "low"),
        ("not_applicable", "medium"),
        ("not_applicable", "high"),
    ],
)
def test_passive_metric_snapshot_enforces_status_level_consistency(
    assessment_status: str,
    level: str,
) -> None:
    with pytest.raises(ValueError, match="requires level=none"):
        PassiveMetricSnapshot(
            source_state_id="state_1",
            source_evidence_ids_json=["ev_1"],
            metrics_json=[
                _metric_output(level=level, assessment_status=assessment_status)
            ],
        )


@pytest.mark.parametrize(
    "field_name",
    [
        "score",
        "priority",
        "rank",
        "recommendation",
        "permission",
        "decision",
        "approval",
        "action",
        "execute",
        "candidate",
        "transition",
        "constraint",
        "reaction",
        "memory_write",
        "truth",
    ],
)
def test_passive_metric_snapshot_rejects_extra_or_forbidden_output_fields(
    field_name: str,
) -> None:
    metric_output = _metric_output()
    metric_output[field_name] = "unsafe"

    with pytest.raises(ValueError, match="fields must match allowed shape"):
        PassiveMetricSnapshot(
            source_state_id="state_1",
            source_evidence_ids_json=["ev_1"],
            metrics_json=[metric_output],
        )


def test_passive_metric_output_shape_is_exact() -> None:
    snapshot = PassiveMetricSnapshot(
        source_state_id="state_1",
        source_evidence_ids_json=["ev_1"],
        metrics_json=[_metric_output()],
    )

    assert set(snapshot.metrics_json[0]) == ALLOWED_METRIC_OUTPUT_FIELDS


def test_passive_metric_report_rejects_decision_action_reaction_fields() -> None:
    for field_name in (
        "decision",
        "action",
        "reaction",
        "transition",
        "constraint",
        "memory_write",
        "truth",
    ):
        with pytest.raises(ValueError, match="forbidden fields"):
            PassiveMetricReport(
                source_snapshot_id="pms_1",
                summary="descriptive only",
                payload_json={field_name: True},
            )
