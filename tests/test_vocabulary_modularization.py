import re
import tomllib
from pathlib import Path

import genus_core


VOCABULARY_INDEX = Path("docs/VOCABULARY.md")
VOCABULARY_MODULES = (
    Path("docs/vocabulary/foundation.md"),
    Path("docs/vocabulary/forbidden_future.md"),
    Path("docs/vocabulary/passive_layers.md"),
    Path("docs/vocabulary/boundary_relevance.md"),
)
EXPECTED_HEADINGS = {
    "WorldEvent",
    "Observation",
    "EvidenceRecord",
    "LedgerEntry",
    "BeliefStateSnapshot",
    "observed_memory_request",
    "observed_memory_content",
    "source_evidence_ids_json",
    "ObservationReport",
    "source_state_id",
    "report payload",
    "descriptive-only report",
    "TruthStatus",
    "Provenance",
    "Confidence",
    "Scope",
    "memory_request_observed",
    "memory_lookup_failure_observed",
    "guard_block_observed",
    "unknown_input_observed",
    "ambiguous_input_observed",
    "LedgerEventType",
    "LedgerSourceKind",
    "LedgerTargetKind",
    "ReactionExecution",
    "MemoryWrite",
    "PhysicsMetric",
    "TransitionCandidate",
    "ConstraintDecision",
    "Reaction",
    "CognitiveStateMap",
    "MemoryObject",
    "Worker",
    "RuntimeCell",
    "Organ",
    "Agent",
    "LLM",
    "PassiveMetricSnapshot",
    "PassiveMetricReport",
    "PassiveTransitionPreview",
    "PassiveTransitionReport",
    "passive measure",
    "pressure",
    "inhibition",
    "stability",
    "cost",
    "potential",
    "Passive Boundary Relevance",
    "boundary_area",
    "observed_boundary_relevance",
    "boundary_question",
}


def _module_text() -> str:
    return "\n".join(path.read_text(encoding="utf-8") for path in VOCABULARY_MODULES)


def test_vocabulary_index_is_active_map_not_monolith() -> None:
    text = VOCABULARY_INDEX.read_text(encoding="utf-8")

    assert len(text.splitlines()) <= 260
    assert "Vocabulary defines how GENUS terms may be used." in text
    assert "Active Vocabulary Map" in text
    assert "docs/vocabulary/foundation.md" in text
    assert "docs/vocabulary/forbidden_future.md" in text
    assert "docs/vocabulary/passive_layers.md" in text
    assert "docs/vocabulary/boundary_relevance.md" in text
    assert "## WorldEvent" not in text


def test_vocabulary_modules_keep_expected_terms_once() -> None:
    headings = re.findall(r"^## (.+)$", _module_text(), flags=re.MULTILINE)

    assert set(headings) == EXPECTED_HEADINGS
    assert len(headings) == len(set(headings)) == len(EXPECTED_HEADINGS)


def test_vocabulary_terms_remain_in_expected_modules() -> None:
    foundation = Path("docs/vocabulary/foundation.md").read_text(encoding="utf-8")
    forbidden = Path("docs/vocabulary/forbidden_future.md").read_text(encoding="utf-8")
    passive = Path("docs/vocabulary/passive_layers.md").read_text(encoding="utf-8")
    boundary = Path("docs/vocabulary/boundary_relevance.md").read_text(encoding="utf-8")

    for term in ("WorldEvent", "ObservationReport", "LedgerTargetKind"):
        assert f"## {term}" in foundation
    for term in ("MemoryWrite", "Reaction", "TransitionCandidate", "ConstraintDecision", "Worker", "LLM"):
        assert f"## {term}" in forbidden
    for term in ("PassiveMetricSnapshot", "PassiveTransitionPreview", "pressure", "cost", "potential"):
        assert f"## {term}" in passive
    for term in ("Passive Boundary Relevance", "boundary_area", "observed_boundary_relevance", "boundary_question"):
        assert f"## {term}" in boundary


def test_vocabulary_modularization_updates_active_version_without_schema_change() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["version"] == "0.4.1"
    assert genus_core.__version__ == "0.4.1"
    assert genus_core.SCHEMA_VERSION == "genus.foundation.v0.0.1"
