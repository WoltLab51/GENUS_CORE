"""BeliefStateSnapshot model."""

from dataclasses import dataclass, field
from typing import Any

from genus_core import SCHEMA_VERSION
from genus_core.ids import new_id
from genus_core.models.observation import ALLOWED_SCOPE
from genus_core.time import utc_now_iso


@dataclass(frozen=True)
class BeliefStateSnapshot:
    scope: str
    source_evidence_ids_json: list[str]
    payload_json: dict[str, Any] = field(default_factory=dict)
    state_id: str = field(default_factory=lambda: new_id("state_"))
    created_at: str = field(default_factory=utc_now_iso)
    schema_version: str = SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.scope not in ALLOWED_SCOPE:
            raise ValueError(f"Invalid scope: {self.scope}")
        if not self.source_evidence_ids_json:
            raise ValueError("BeliefStateSnapshot requires at least one EvidenceRecord id")

    @property
    def id(self) -> str:
        return self.state_id
