from pathlib import Path


CHARTER_PATH = Path("docs/GENUS_CHARTER.md")
SAFETY_BOUNDARIES_PATH = Path("docs/SAFETY_BOUNDARIES.md")
BUILD_RULES_PATH = Path("docs/BUILD_RULES.md")


def test_governance_documents_exist() -> None:
    assert CHARTER_PATH.exists()
    assert SAFETY_BOUNDARIES_PATH.exists()


def test_build_rules_reference_charter_and_safety_boundaries() -> None:
    text = BUILD_RULES_PATH.read_text(encoding="utf-8")

    assert "GENUS_CHARTER.md" in text
    assert "SAFETY_BOUNDARIES.md" in text


def test_charter_contains_core_genus_directives() -> None:
    text = CHARTER_PATH.read_text(encoding="utf-8")

    required = (
        "GENUS is a governed digital reaction organism",
        "LLM proposes. GENUS governs.",
        "Do not make GENUS powerful before making it bounded.",
        "GENUS darf erst handeln, wenn es vorher wahrgenommen, belegt, "
        "abgeleitet, bewertet, begrenzt und entschieden hat.",
        "Function-first, Cell-ready, Organ-later, Agent-last",
        "Evidence is not Belief. Belief is not Truth. Report is not Decision.",
    )
    for phrase in required:
        assert phrase in text


def test_safety_boundaries_keep_current_forbidden_capabilities_out() -> None:
    text = SAFETY_BOUNDARIES_PATH.read_text(encoding="utf-8")

    required = (
        "passive foundation plus passive Physics only",
        "The only new product capability allowed in v0.2.0 is passive Physics.",
        "MemoryWrite",
        "Reaction",
        "TransitionCandidate",
        "ConstraintDecision",
        "Worker",
        "LLM",
        "Agent",
        "GraphDB",
        "RuntimeShape",
        "Self-mutation",
    )
    for phrase in required:
        assert phrase in text
