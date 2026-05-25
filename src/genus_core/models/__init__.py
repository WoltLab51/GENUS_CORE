"""Foundation model exports and small language validation helpers."""

from genus_core.models.belief_state_snapshot import BeliefStateSnapshot
from genus_core.models.evidence_record import EvidenceRecord
from genus_core.models.ledger_entry import LedgerEntry
from genus_core.models.observation import Observation
from genus_core.models.observation_report import ObservationReport
from genus_core.models.world_event import WorldEvent

ALLOWED_SENTENCE_TYPES = frozenset(
    {"WORLD_EVENT", "OBSERVATION", "EVIDENCE", "LEDGER", "BELIEF", "REPORT"}
)


def validate_sentence_type(sentence_type: str) -> str:
    if sentence_type not in ALLOWED_SENTENCE_TYPES:
        raise ValueError(f"Unsupported GENUS sentence type: {sentence_type}")
    return sentence_type


__all__ = [
    "ALLOWED_SENTENCE_TYPES",
    "BeliefStateSnapshot",
    "EvidenceRecord",
    "LedgerEntry",
    "Observation",
    "ObservationReport",
    "WorldEvent",
    "validate_sentence_type",
]
