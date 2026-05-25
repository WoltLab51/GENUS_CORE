"""EvidenceRecord model."""

from dataclasses import dataclass, field
from typing import Any

from genus_core import SCHEMA_VERSION
from genus_core.ids import new_id
from genus_core.time import utc_now_iso

ALLOWED_TRUTH_STATUS = frozenset({"observed", "derived", "rejected"})


@dataclass(frozen=True)
class EvidenceRecord:
    source_observation_id: str
    truth_status: str
    provenance: str
    payload_json: dict[str, Any] = field(default_factory=dict)
    evidence_id: str = field(default_factory=lambda: new_id("ev_"))
    created_at: str = field(default_factory=utc_now_iso)
    schema_version: str = SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.truth_status not in ALLOWED_TRUTH_STATUS:
            raise ValueError(f"Invalid truth_status: {self.truth_status}")

    @property
    def id(self) -> str:
        return self.evidence_id
