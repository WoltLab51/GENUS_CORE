import sqlite3

import pytest

from genus_core.functions import append_ledger_entry
from genus_core.truth import connect, load_ledger_entries, save_ledger_entry


def test_ledger_is_append_only(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")
    first = append_ledger_entry(
        chain_id="chain_test",
        step=1,
        event_type="evidence_record_created",
        source_kind="observation",
        source_id="obs_1",
        target_kind="evidence_record",
        target_id="ev_1",
    )
    duplicate_step = append_ledger_entry(
        chain_id="chain_test",
        step=1,
        event_type="evidence_record_created_again",
        source_kind="observation",
        source_id="obs_2",
        target_kind="evidence_record",
        target_id="ev_2",
    )

    save_ledger_entry(connection, first)
    with pytest.raises(sqlite3.IntegrityError):
        save_ledger_entry(connection, duplicate_step)

    entries = load_ledger_entries(connection, "chain_test")
    assert len(entries) == 1
    assert entries[0]["ledger_id"] == first.ledger_id


def test_no_ledger_update_or_delete_api() -> None:
    import genus_core.truth.sqlite_store as sqlite_store

    public_names = {name for name in dir(sqlite_store) if not name.startswith("_")}

    assert "update_ledger_entry" not in public_names
    assert "delete_ledger_entry" not in public_names
