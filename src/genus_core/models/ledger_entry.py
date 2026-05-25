"""LedgerEntry model."""

from dataclasses import dataclass, field
from typing import Any

from genus_core import SCHEMA_VERSION
from genus_core.ids import new_id
from genus_core.time import utc_now_iso


@dataclass(frozen=True)
class LedgerEntry:
    chain_id: str
    step: int
    event_type: str
    source_kind: str
    source_id: str
    target_kind: str | None = None
    target_id: str | None = None
    payload_json: dict[str, Any] = field(default_factory=dict)
    ledger_id: str = field(default_factory=lambda: new_id("led_"))
    created_at: str = field(default_factory=utc_now_iso)
    schema_version: str = SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.step < 1:
            raise ValueError("Ledger step must be >= 1")

    @property
    def id(self) -> str:
        return self.ledger_id
