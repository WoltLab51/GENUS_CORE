import sqlite3

import pytest

from genus_core import SCHEMA_VERSION
from genus_core.functions import append_ledger_entry, create_evidence_record, observe_event
from genus_core.models import WorldEvent
from genus_core.truth import connect, fetch_evidence_record, save_evidence_record
from genus_core.truth.ledger import load_ledger_entries, save_ledger_entry


def test_evidence_record_persists_schema_version(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")
    observation = observe_event(
        WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    )
    evidence = create_evidence_record(observation)

    save_evidence_record(connection, evidence)
    stored = fetch_evidence_record(connection, evidence.evidence_id)

    assert stored is not None
    assert stored["schema_version"] == SCHEMA_VERSION


def test_ledger_entry_persists_schema_version(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")
    ledger_entry = append_ledger_entry(
        chain_id="chain_schema",
        step=1,
        event_type="evidence_record_created",
        source_kind="observation",
        source_id="obs_1",
        target_kind="evidence_record",
        target_id="ev_1",
    )

    save_ledger_entry(connection, ledger_entry)
    stored = load_ledger_entries(connection, "chain_schema")

    assert stored[0]["schema_version"] == SCHEMA_VERSION


def test_sqlite_rejects_invalid_truth_status(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")

    with pytest.raises(sqlite3.IntegrityError):
        connection.execute(
            """
            INSERT INTO evidence_records (
                evidence_id,
                source_observation_id,
                truth_status,
                provenance,
                payload_json,
                created_at,
                schema_version
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "ev_invalid_truth",
                "obs_1",
                "true",
                "user_input",
                "{}",
                "2026-05-25T00:00:00Z",
                SCHEMA_VERSION,
            ),
        )


def test_sqlite_requires_evidence_schema_version(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")

    with pytest.raises(sqlite3.IntegrityError):
        connection.execute(
            """
            INSERT INTO evidence_records (
                evidence_id,
                source_observation_id,
                truth_status,
                provenance,
                payload_json,
                created_at,
                schema_version
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "ev_missing_schema",
                "obs_1",
                "observed",
                "user_input",
                "{}",
                "2026-05-25T00:00:00Z",
                None,
            ),
        )


def test_sqlite_rejects_invalid_ledger_step(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")
    invalid_entry = append_ledger_entry(
        chain_id="chain_invalid_step",
        step=1,
        event_type="evidence_record_created",
        source_kind="observation",
        source_id="obs_1",
        target_kind="evidence_record",
        target_id="ev_1",
    )
    object.__setattr__(invalid_entry, "step", 0)

    with pytest.raises(sqlite3.IntegrityError):
        save_ledger_entry(connection, invalid_entry)


def test_sqlite_rejects_duplicate_ledger_step(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")
    first = append_ledger_entry(
        chain_id="chain_duplicate",
        step=1,
        event_type="evidence_record_created",
        source_kind="observation",
        source_id="obs_1",
        target_kind="evidence_record",
        target_id="ev_1",
    )
    second = append_ledger_entry(
        chain_id="chain_duplicate",
        step=1,
        event_type="evidence_record_created",
        source_kind="observation",
        source_id="obs_2",
        target_kind="evidence_record",
        target_id="ev_2",
    )

    save_ledger_entry(connection, first)
    with pytest.raises(sqlite3.IntegrityError):
        save_ledger_entry(connection, second)


def test_sqlite_requires_ledger_schema_version(tmp_path) -> None:
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
                "led_missing_schema",
                "chain_missing_schema",
                1,
                "evidence_record_created",
                "observation",
                "obs_1",
                "evidence_record",
                "ev_1",
                "{}",
                "2026-05-25T00:00:00Z",
                None,
            ),
        )
