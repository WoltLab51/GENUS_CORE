import pytest

from genus_core.models import validate_sentence_type


def test_language_rejects_unknown_sentence_type() -> None:
    with pytest.raises(ValueError, match="Unsupported GENUS sentence type"):
        validate_sentence_type("ACTION")


def test_language_accepts_v0_0_1_sentence_types() -> None:
    assert validate_sentence_type("WORLD_EVENT") == "WORLD_EVENT"
    assert validate_sentence_type("REPORT") == "REPORT"
