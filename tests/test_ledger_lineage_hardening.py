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


def test_sqlite_rejects_invalid_ledger_event_type(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")

    with pytest.raises(sqlite3.IntegrityError):
        connection.execute(
            """
            INSERT INTO ledger_entries (
                ledger_id,
                chain_id,
                step,
                event_type,
                source_kind,
                source_id,
                target_kind,
                target_id,
                payload_json,
                created_at,
                schema_version
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "led_invalid_event",
                "chain_invalid_event",
                1,
                "belief_snapshot_created",
                "observation",
                "obs_1",
                "evidence_record",
                "ev_1",
                "{}",
                "2026-05-25T00:00:00Z",
                "genus.foundation.v0.0.1",
            ),
        )


def test_sqlite_rejects_invalid_ledger_source_kind(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")

    with pytest.raises(sqlite3.IntegrityError):
        connection.execute(
            """
            INSERT INTO ledger_entries (
                ledger_id,
                chain_id,
                step,
                event_type,
                source_kind,
                source_id,
                target_kind,
                target_id,
                payload_json,
                created_at,
                schema_version
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "led_invalid_source",
                "chain_invalid_source",
                1,
                "evidence_record_created",
                "ledger_entry",
                "led_1",
                "evidence_record",
                "ev_1",
                "{}",
                "2026-05-25T00:00:00Z",
                "genus.foundation.v0.0.1",
            ),
        )


def test_sqlite_rejects_invalid_ledger_target_kind(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")

    with pytest.raises(sqlite3.IntegrityError):
        connection.execute(
            """
            INSERT INTO ledger_entries (
                ledger_id,
                chain_id,
                step,
                event_type,
                source_kind,
                source_id,
                target_kind,
                target_id,
                payload_json,
                created_at,
                schema_version
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "led_invalid_target",
                "chain_invalid_target",
                1,
                "evidence_record_created",
                "observation",
                "obs_1",
                "ledger_entry",
                "led_1",
                "{}",
                "2026-05-25T00:00:00Z",
                "genus.foundation.v0.0.1",
            ),
        )


@pytest.mark.parametrize("target_id", [None, "", "   "])
def test_sqlite_requires_ledger_target_id(tmp_path, target_id: str | None) -> None:
    connection = connect(tmp_path / "truth.sqlite3")

    with pytest.raises(sqlite3.IntegrityError):
        connection.execute(
            """
            INSERT INTO ledger_entries (
                ledger_id,
                chain_id,
                step,
                event_type,
                source_kind,
                source_id,
                target_kind,
                target_id,
                payload_json,
                created_at,
                schema_version
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "led_missing_target",
                "chain_missing_target",
                1,
                "evidence_record_created",
                "observation",
                "obs_1",
                "evidence_record",
                target_id,
                "{}",
                "2026-05-25T00:00:00Z",
                "genus.foundation.v0.0.1",
            ),
        )


def test_save_valid_ledger_entry_after_hardening(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")
    ledger_entry = append_ledger_entry(
        step=1,
        event_type="evidence_record_created",
        source_kind="observation",
        source_id="obs_1",
        target_kind="evidence_record",
        target_id="ev_1",
    )

    save_ledger_entry(connection, ledger_entry)

    stored = connection.execute(
        "SELECT event_type, source_kind, target_kind FROM ledger_entries"
    ).fetchone()
    assert dict(stored) == {
        "event_type": "evidence_record_created",
        "source_kind": "observation",
        "target_kind": "evidence_record",
    }
