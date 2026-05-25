"""Observation model."""

from dataclasses import dataclass, field
from typing import Any

from genus_core import SCHEMA_VERSION
from genus_core.ids import new_id
from genus_core.time import utc_now_iso

ALLOWED_CONFIDENCE = frozenset({"low", "medium", "high"})
ALLOWED_SCOPE = frozenset({"input", "memory", "system", "worker"})


@dataclass(frozen=True)
class Observation:
    source_event_id: str
    observation_type: str
    scope: str
    confidence: str
    payload_json: dict[str, Any] = field(default_factory=dict)
    observation_id: str = field(default_factory=lambda: new_id("obs_"))
    created_at: str = field(default_factory=utc_now_iso)
    schema_version: str = SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.confidence not in ALLOWED_CONFIDENCE:
            raise ValueError(f"Invalid confidence: {self.confidence}")
        if self.scope not in ALLOWED_SCOPE:
            raise ValueError(f"Invalid scope: {self.scope}")

    @property
    def id(self) -> str:
        return self.observation_id
