"""Allowed sentence types for the minimal GENUS foundation language."""

ALLOWED_SENTENCE_TYPES = frozenset(
    {"WORLD_EVENT", "OBSERVATION", "EVIDENCE", "LEDGER", "BELIEF", "REPORT"}
)


def validate_sentence_type(sentence_type: str) -> str:
    if sentence_type not in ALLOWED_SENTENCE_TYPES:
        raise ValueError(f"Unsupported GENUS sentence type: {sentence_type}")
    return sentence_type
