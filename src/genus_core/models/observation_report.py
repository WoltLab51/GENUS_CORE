"""ObservationReport model."""

from dataclasses import dataclass, field
from typing import Any

from genus_core import SCHEMA_VERSION
from genus_core.ids import new_id
from genus_core.time import utc_now_iso

FORBIDDEN_REPORT_FIELDS = frozenset(
    {"decision", "action", "execute", "approval", "reaction", "memory_write"}
)


@dataclass(frozen=True)
class ObservationReport:
    source_state_id: str
    summary: str
    payload_json: dict[str, Any] = field(default_factory=dict)
    report_id: str = field(default_factory=lambda: new_id("rep_"))
    created_at: str = field(default_factory=utc_now_iso)
    schema_version: str = SCHEMA_VERSION

    def __post_init__(self) -> None:
        forbidden = FORBIDDEN_REPORT_FIELDS.intersection(self.payload_json)
        if forbidden:
            names = ", ".join(sorted(forbidden))
            raise ValueError(f"ObservationReport cannot contain forbidden fields: {names}")

    @property
    def id(self) -> str:
        return self.report_id
