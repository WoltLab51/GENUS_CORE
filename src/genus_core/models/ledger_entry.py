"""LedgerEntry model."""

from dataclasses import dataclass, field
from typing import Any

from genus_core import SCHEMA_VERSION
from genus_core.ids import new_id
from genus_core.time import utc_now_iso

ALLOWED_LEDGER_EVENT_TYPES = frozenset({"evidence_record_created"})
ALLOWED_LEDGER_SOURCE_KINDS = frozenset({"observation"})
ALLOWED_LEDGER_TARGET_KINDS = frozenset({"evidence_record"})
FORBIDDEN_LEDGER_PAYLOAD_FIELDS = frozenset(
    {
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
    }
)


@dataclass(frozen=True)
class LedgerEntry:
    chain_id: str
    step: int
    event_type: str
    source_kind: str
    source_id: str
    target_kind: str
    target_id: str
    payload_json: dict[str, Any] = field(default_factory=dict)
    ledger_id: str = field(default_factory=lambda: new_id("led_"))
    created_at: str = field(default_factory=utc_now_iso)
    schema_version: str = SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.step < 1:
            raise ValueError("Ledger step must be >= 1")
        if self.event_type not in ALLOWED_LEDGER_EVENT_TYPES:
            raise ValueError(f"Invalid ledger event_type: {self.event_type}")
        if self.source_kind not in ALLOWED_LEDGER_SOURCE_KINDS:
            raise ValueError(f"Invalid ledger source_kind: {self.source_kind}")
        if (
            not isinstance(self.target_kind, str)
            or not self.target_kind.strip()
        ):
            raise ValueError("LedgerEntry requires target_kind")
        if self.target_kind not in ALLOWED_LEDGER_TARGET_KINDS:
            raise ValueError(f"Invalid ledger target_kind: {self.target_kind}")
        if not isinstance(self.target_id, str) or not self.target_id.strip():
            raise ValueError("LedgerEntry requires target_id")
        forbidden = FORBIDDEN_LEDGER_PAYLOAD_FIELDS.intersection(self.payload_json)
        if forbidden:
            names = ", ".join(sorted(forbidden))
            raise ValueError(f"LedgerEntry cannot contain forbidden fields: {names}")

    @property
    def id(self) -> str:
        return self.ledger_id
