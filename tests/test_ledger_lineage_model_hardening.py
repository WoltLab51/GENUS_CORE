import sqlite3

import pytest

from genus_core.functions import append_ledger_entry
from genus_core.models.ledger_entry import LedgerEntry
from genus_core.truth import connect, save_ledger_entry


def test_valid_ledger_entry_is_real_current_flow() -> None:
    ledger_entry = append_ledger_entry(
        chain_id="chain_valid",
        step=1,
        event_type="evidence_record_created",
        source_kind="observation",
        source_id="obs_1",
        target_kind="evidence_record",
        target_id="ev_1",
    )

    assert isinstance(ledger_entry, LedgerEntry)
    assert ledger_entry.event_type == "evidence_record_created"
    assert ledger_entry.source_kind == "observation"
    assert ledger_entry.target_kind == "evidence_record"


def test_invalid_ledger_event_type_rejected() -> None:
    with pytest.raises(ValueError, match="Invalid ledger event_type"):
        append_ledger_entry(
            step=1,
            event_type="belief_snapshot_created",
            source_kind="observation",
            source_id="obs_1",
            target_kind="evidence_record",
            target_id="ev_1",
        )


@pytest.mark.parametrize("source_kind", ["ledger_entry", "world_event", "memory_write"])
def test_invalid_ledger_source_kind_rejected(source_kind: str) -> None:
    with pytest.raises(ValueError, match="Invalid ledger source_kind"):
        append_ledger_entry(
            step=1,
            event_type="evidence_record_created",
            source_kind=source_kind,
            source_id="source_1",
            target_kind="evidence_record",
            target_id="ev_1",
        )


@pytest.mark.parametrize(
    "target_kind", ["ledger_entry", "belief_state_snapshot", "observation_report"]
)
def test_invalid_ledger_target_kind_rejected(target_kind: str) -> None:
    with pytest.raises(ValueError, match="Invalid ledger target_kind"):
        append_ledger_entry(
            step=1,
            event_type="evidence_record_created",
            source_kind="observation",
            source_id="obs_1",
            target_kind=target_kind,
            target_id="target_1",
        )


@pytest.mark.parametrize("target_kind", ["", "   ", None])
def test_ledger_entry_requires_target_kind(target_kind: str | None) -> None:
    with pytest.raises(ValueError, match="requires target_kind"):
        LedgerEntry(
            chain_id="chain_missing_target_kind",
            step=1,
            event_type="evidence_record_created",
            source_kind="observation",
            source_id="obs_1",
            target_kind=target_kind,  # type: ignore[arg-type]
            target_id="ev_1",
        )


@pytest.mark.parametrize("target_id", ["", "   ", None])
def test_ledger_entry_requires_target_id(target_id: str | None) -> None:
    with pytest.raises(ValueError, match="requires target_id"):
        LedgerEntry(
            chain_id="chain_missing_target_id",
            step=1,
            event_type="evidence_record_created",
            source_kind="observation",
            source_id="obs_1",
            target_kind="evidence_record",
            target_id=target_id,  # type: ignore[arg-type]
        )


@pytest.mark.parametrize(
    "field_name",
    [
        "truth",
        "world_truth",
        "belief",
        "pending_memory_request",
        "observed_memory_request",
        "decision",
        "action",
        "reaction",
        "transition",
        "physics",
        "memory_write",
    ],
)
def test_ledger_payload_rejects_truth_belief_action_fields(field_name: str) -> None:
    with pytest.raises(ValueError, match="forbidden fields"):
        append_ledger_entry(
            step=1,
            event_type="evidence_record_created",
            source_kind="observation",
            source_id="obs_1",
            target_kind="evidence_record",
            target_id="ev_1",
            payload_json={field_name: True},
        )


def test_append_ledger_entry_has_no_sqlite_side_effects(tmp_path) -> None:
    db_path = tmp_path / "truth.sqlite3"

    ledger_entry = append_ledger_entry(
        step=1,
        event_type="evidence_record_created",
        source_kind="observation",
        source_id="obs_1",
        target_kind="evidence_record",
        target_id="ev_1",
    )

    assert isinstance(ledger_entry, LedgerEntry)
    assert not db_path.exists()
