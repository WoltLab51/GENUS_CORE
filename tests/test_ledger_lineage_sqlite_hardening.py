import sqlite3

import pytest

from genus_core.functions import append_ledger_entry
from genus_core.truth import connect, save_ledger_entry


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
