import pytest

from genus_core.language import ALLOWED_SENTENCE_TYPES, validate_sentence_type
from genus_core.models import (
    ALLOWED_SENTENCE_TYPES as MODEL_ALLOWED_SENTENCE_TYPES,
)
from genus_core.models import (
    validate_sentence_type as model_validate_sentence_type,
)

EXPECTED_ALLOWED_SENTENCE_TYPES = frozenset(
    {"WORLD_EVENT", "OBSERVATION", "EVIDENCE", "LEDGER", "BELIEF", "REPORT"}
)

FORBIDDEN_FUTURE_SENTENCE_TYPES = (
    "ACTION",
    "REACTION",
    "EXECUTION",
    "MEMORY_WRITE",
    "PHYSICS",
    "MAP",
    "TRANSITION",
    "CONSTRAINT",
    "AGENT",
    "WORKER",
    "CELL",
    "ORGAN",
)


def test_allowed_sentence_type_set_is_exact() -> None:
    assert ALLOWED_SENTENCE_TYPES == EXPECTED_ALLOWED_SENTENCE_TYPES


@pytest.mark.parametrize("sentence_type", sorted(EXPECTED_ALLOWED_SENTENCE_TYPES))
def test_language_accepts_all_allowed_sentence_types(sentence_type: str) -> None:
    assert validate_sentence_type(sentence_type) == sentence_type


def test_language_rejects_unknown_sentence_type() -> None:
    with pytest.raises(ValueError, match="Unsupported GENUS sentence type"):
        validate_sentence_type("UNKNOWN")


@pytest.mark.parametrize("sentence_type", FORBIDDEN_FUTURE_SENTENCE_TYPES)
def test_language_rejects_forbidden_future_sentence_types(
    sentence_type: str,
) -> None:
    with pytest.raises(ValueError, match="Unsupported GENUS sentence type"):
        validate_sentence_type(sentence_type)


def test_models_reexport_language_validation_for_compatibility() -> None:
    assert MODEL_ALLOWED_SENTENCE_TYPES is ALLOWED_SENTENCE_TYPES
    assert model_validate_sentence_type("REPORT") == "REPORT"
