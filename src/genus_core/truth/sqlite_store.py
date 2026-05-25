"""SQLite storage for the v0.0.1 truth layer."""

import json
import sqlite3
from pathlib import Path

from genus_core.models.evidence_record import EvidenceRecord
from genus_core.models.ledger_entry import LedgerEntry


def connect(path: str | Path) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    initialize_schema(connection)
    return connection


def initialize_schema(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS evidence_records (
            evidence_id TEXT PRIMARY KEY,
            source_observation_id TEXT NOT NULL,
            truth_status TEXT NOT NULL CHECK (
                truth_status IN ('observed', 'derived', 'rejected')
            ),
            provenance TEXT NOT NULL CHECK (
                provenance IN (
                    'user_input',
                    'system_event',
                    'runtime_probe',
                    'manual_entry'
                )
            ),
            payload_json TEXT NOT NULL,
            created_at TEXT NOT NULL,
            schema_version TEXT NOT NULL
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS ledger_entries (
            ledger_id TEXT PRIMARY KEY,
            chain_id TEXT NOT NULL,
            step INTEGER NOT NULL CHECK (step >= 1),
            event_type TEXT NOT NULL,
            source_kind TEXT NOT NULL,
            source_id TEXT NOT NULL,
            target_kind TEXT,
            target_id TEXT,
            payload_json TEXT NOT NULL,
            created_at TEXT NOT NULL,
            schema_version TEXT NOT NULL,
            UNIQUE(chain_id, step)
        )
        """
    )
    connection.commit()


def save_evidence_record(
    connection: sqlite3.Connection, evidence_record: EvidenceRecord
) -> None:
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
            evidence_record.evidence_id,
            evidence_record.source_observation_id,
            evidence_record.truth_status,
            evidence_record.provenance,
            json.dumps(evidence_record.payload_json, sort_keys=True),
            evidence_record.created_at,
            evidence_record.schema_version,
        ),
    )
    connection.commit()


def fetch_evidence_record(
    connection: sqlite3.Connection, evidence_id: str
) -> sqlite3.Row | None:
    return connection.execute(
        "SELECT * FROM evidence_records WHERE evidence_id = ?", (evidence_id,)
    ).fetchone()


def save_ledger_entry(connection: sqlite3.Connection, ledger_entry: LedgerEntry) -> None:
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
            ledger_entry.ledger_id,
            ledger_entry.chain_id,
            ledger_entry.step,
            ledger_entry.event_type,
            ledger_entry.source_kind,
            ledger_entry.source_id,
            ledger_entry.target_kind,
            ledger_entry.target_id,
            json.dumps(ledger_entry.payload_json, sort_keys=True),
            ledger_entry.created_at,
            ledger_entry.schema_version,
        ),
    )
    connection.commit()
