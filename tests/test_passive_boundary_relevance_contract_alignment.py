from pathlib import Path


SPEC_PATH = Path("docs/PASSIVE_BOUNDARY_RELEVANCE_SPEC_v0.4.0.md")
PLANNED_GATES_PATH = Path("docs/quality_gates/planned.md")


def _spec_text() -> str:
    return SPEC_PATH.read_text(encoding="utf-8")


def test_passive_boundary_relevance_spec_references_artifact_contracts() -> None:
    text = _spec_text()

    assert "A later implementation must comply with `ARTIFACT_CONTRACTS.md`." in text
    assert "Common contracts define compatibility, not identical field shape." in text
    assert "Reports may explain source lineage, but reports must not create new lineage." in text


def test_passive_boundary_relevance_preview_shape_preserves_contract_lineage() -> None:
    text = _spec_text()

    for planned_field in (
        "preview_id",
        "source_state_id",
        "source_metric_snapshot_id",
        "source_transition_preview_id",
        "source_evidence_ids_json",
        "boundary_question",
        "boundary_area",
        "observed_boundary_relevance",
        "no_boundary_evaluation_possible",
        "no_decision_possible",
        "no_action_possible",
    ):
        assert planned_field in text
    assert "`source_state_id`, `source_metric_snapshot_id`, and" in text
    assert "`source_transition_preview_id` must reference the three planned input artifacts." in text
    assert "must be inherited from the source" in text
    assert "must match the passive metric and passive" in text


def test_passive_boundary_relevance_report_shape_explains_without_new_lineage() -> None:
    text = _spec_text()

    for planned_field in (
        "report_id",
        "source_relevance_preview_id",
        "summary",
        "payload_json",
    ):
        assert planned_field in text
    assert "The report payload may repeat the preview source references" in text
    assert "The report must not invent source references or evidence lineage." in text


def test_passive_boundary_relevance_spec_keeps_planned_artifacts_ephemeral_only() -> None:
    text = _spec_text()

    assert "ephemeral-only lifecycle" in text
    assert "No classes, functions, runtime exports, CLI commands, SQLite tables" in text
    assert "SQLite table" in text


def test_planned_quality_gate_tracks_contract_alignment_and_active_version() -> None:
    text = PLANNED_GATES_PATH.read_text(encoding="utf-8")

    assert "package version remains 0.3.4" in text
    assert "the spec references ARTIFACT_CONTRACTS.md" in text
    assert "planned preview shape includes preview_id" in text
    assert "planned report shape includes report_id" in text
    assert "planned report does not create new lineage" in text
    assert "planned artifacts remain ephemeral-only" in text
