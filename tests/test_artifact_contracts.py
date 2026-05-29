from pathlib import Path

from genus_core import SCHEMA_VERSION
from genus_core.functions import (
    append_ledger_entry,
    build_belief_state_snapshot,
    create_evidence_record,
    create_observation_report,
    observe_event,
)
from genus_core.models import WorldEvent
from genus_core.passive_physics import (
    build_passive_metric_snapshot,
    create_passive_metric_report,
)
from genus_core.passive_transition import (
    build_passive_transition_preview,
    create_passive_transition_report,
)
from genus_core.truth import connect


CONTRACTS_PATH = Path("docs/ARTIFACT_CONTRACTS.md")


def _artifact_chain() -> dict[str, object]:
    event = WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    observation = observe_event(event)
    evidence = create_evidence_record(observation)
    ledger = append_ledger_entry(
        step=1,
        event_type="evidence_record_created",
        source_kind="observation",
        source_id=observation.observation_id,
        target_kind="evidence_record",
        target_id=evidence.evidence_id,
    )
    belief = build_belief_state_snapshot([evidence])
    observation_report = create_observation_report(belief)
    metric_snapshot = build_passive_metric_snapshot(belief)
    metric_report = create_passive_metric_report(metric_snapshot)
    transition_preview = build_passive_transition_preview(belief, metric_snapshot)
    transition_report = create_passive_transition_report(transition_preview)

    return {
        "event": event,
        "observation": observation,
        "evidence": evidence,
        "ledger": ledger,
        "belief": belief,
        "observation_report": observation_report,
        "metric_snapshot": metric_snapshot,
        "metric_report": metric_report,
        "transition_preview": transition_preview,
        "transition_report": transition_report,
    }


def test_artifact_contracts_document_exists_and_defines_shared_contracts() -> None:
    text = CONTRACTS_PATH.read_text(encoding="utf-8")

    for phrase in (
        "ID Contract",
        "Source Lineage Contract",
        "Evidence Lineage Contract",
        "Snapshot, Preview, And Report Contract",
        "Durable And Ephemeral Contract",
        "Report Boundary Contract",
    ):
        assert phrase in text


def test_artifact_contracts_prevent_field_shape_equalization_and_lineage_drift() -> None:
    text = CONTRACTS_PATH.read_text(encoding="utf-8")

    assert "Common artifact contracts define compatibility, not identical field shape." in text
    assert "reports do not create new lineage" in text
    assert "Reports explain existing artifacts." in text


def test_artifact_contracts_mark_evaluation_as_watched_wording() -> None:
    text = CONTRACTS_PATH.read_text(encoding="utf-8")

    assert "`evaluate` and `evaluation` are watched terms." in text
    assert "descriptive relevance mapping" in text
    assert "permission evaluation" in text
    assert "policy evaluation" in text


def test_active_artifacts_have_primary_ids_and_common_metadata() -> None:
    artifacts = _artifact_chain()
    primary_id_fields = {
        "event": "event_id",
        "observation": "observation_id",
        "evidence": "evidence_id",
        "ledger": "ledger_id",
        "belief": "state_id",
        "observation_report": "report_id",
        "metric_snapshot": "snapshot_id",
        "metric_report": "report_id",
        "transition_preview": "preview_id",
        "transition_report": "report_id",
    }

    for name, primary_id_field in primary_id_fields.items():
        artifact = artifacts[name]
        primary_id = getattr(artifact, primary_id_field)
        assert artifact.id == primary_id
        assert primary_id
        assert artifact.created_at
        assert artifact.schema_version == SCHEMA_VERSION


def test_reports_reference_their_single_source_artifact() -> None:
    artifacts = _artifact_chain()

    assert (
        artifacts["observation_report"].source_state_id
        == artifacts["belief"].state_id
    )
    assert (
        artifacts["metric_report"].source_snapshot_id
        == artifacts["metric_snapshot"].snapshot_id
    )
    assert (
        artifacts["transition_report"].source_preview_id
        == artifacts["transition_preview"].preview_id
    )


def test_passive_downstream_artifacts_preserve_belief_evidence_lineage() -> None:
    artifacts = _artifact_chain()
    source_evidence_ids = artifacts["belief"].source_evidence_ids_json

    assert artifacts["metric_snapshot"].source_evidence_ids_json == source_evidence_ids
    assert artifacts["transition_preview"].source_evidence_ids_json == source_evidence_ids
    assert (
        artifacts["metric_report"].payload_json["source_evidence_ids_json"]
        == source_evidence_ids
    )
    assert (
        artifacts["transition_report"].payload_json["source_evidence_ids_json"]
        == source_evidence_ids
    )
    for metric in artifacts["metric_snapshot"].metrics_json:
        assert metric["source_evidence_ids_json"] == source_evidence_ids


def test_artifact_contract_alignment_keeps_durable_sqlite_layer_unchanged(tmp_path) -> None:
    with connect(tmp_path / "truth.sqlite3") as connection:
        tables = {
            row[0]
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            ).fetchall()
        }

    assert tables == {"evidence_records", "ledger_entries"}
