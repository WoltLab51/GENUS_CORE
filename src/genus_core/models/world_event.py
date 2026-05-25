"""WorldEvent model."""

from dataclasses import dataclass, field
from typing import Any

from genus_core import SCHEMA_VERSION
from genus_core.ids import new_id
from genus_core.time import utc_now_iso


@dataclass(frozen=True)
class WorldEvent:
    event_type: str
    raw_text: str | None = None
    payload_json: dict[str, Any] = field(default_factory=dict)
    event_id: str = field(default_factory=lambda: new_id("evt_"))
    created_at: str = field(default_factory=utc_now_iso)
    schema_version: str = SCHEMA_VERSION

    @property
    def id(self) -> str:
        return self.event_id
