"""Ledger-specific append and read helpers."""

import sqlite3

from genus_core.models.ledger_entry import LedgerEntry
from genus_core.truth.sqlite_store import save_ledger_entry as _save_ledger_entry


def save_ledger_entry(connection: sqlite3.Connection, ledger_entry: LedgerEntry) -> None:
    _save_ledger_entry(connection, ledger_entry)


def load_ledger_entries(
    connection: sqlite3.Connection, chain_id: str
) -> list[sqlite3.Row]:
    return list(
        connection.execute(
            "SELECT * FROM ledger_entries WHERE chain_id = ? ORDER BY step",
            (chain_id,),
        ).fetchall()
    )
