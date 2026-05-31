from pathlib import Path


FUNCTION_CELLS_PATH = Path("docs/FUNCTION_CELLS.md")


PUBLIC_FUNCTIONS = (
    "observe_event",
    "create_evidence_record",
    "append_ledger_entry",
    "build_belief_state_snapshot",
    "create_observation_report",
    "build_passive_metric_snapshot",
    "create_passive_metric_report",
    "build_passive_transition_preview",
    "create_passive_transition_report",
    "build_passive_boundary_relevance_preview",
    "create_passive_boundary_relevance_report",
)


def test_function_cells_document_exists_and_uses_contract_shape() -> None:
    text = FUNCTION_CELLS_PATH.read_text(encoding="utf-8")

    for section in (
        "Purpose",
        "Inputs",
        "Outputs",
        "Side effects",
        "Allowed writes",
        "Forbidden effects",
        "Tests",
    ):
        assert section in text


def test_all_public_genus_functions_have_function_cell_contracts() -> None:
    text = FUNCTION_CELLS_PATH.read_text(encoding="utf-8")

    for function_name in PUBLIC_FUNCTIONS:
        assert f"`{function_name}(...)" in text


def test_function_cells_keep_runtime_boundaries_explicit() -> None:
    text = FUNCTION_CELLS_PATH.read_text(encoding="utf-8")

    for forbidden_effect in (
        "no persistence",
        "no decision",
        "no permission",
        "no reaction",
        "no memory write",
        "no new lineage",
    ):
        assert forbidden_effect in text
