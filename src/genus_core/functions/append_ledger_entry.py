"""Create a LedgerEntry value for later append-only persistence."""

from typing import Any

from genus_core.ids import new_chain_id
from genus_core.models.ledger_entry import LedgerEntry


def append_ledger_entry(
    *,
    step: int,
    event_type: str,
    source_kind: str,
    source_id: str,
    target_kind: str,
    target_id: str,
    chain_id: str | None = None,
    payload_json: dict[str, Any] | None = None,
) -> LedgerEntry:
    return LedgerEntry(
        chain_id=chain_id or new_chain_id(),
        step=step,
        event_type=event_type,
        source_kind=source_kind,
        source_id=source_id,
        target_kind=target_kind,
        target_id=target_id,
        payload_json=payload_json or {},
    )
