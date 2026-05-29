import ast
import importlib
import inspect
import pkgutil
import re
from pathlib import Path

import genus_core
import genus_core.cli as cli
import genus_core.functions as foundation_functions
from genus_core.language import ALLOWED_SENTENCE_TYPES


CRITERIA_PATH = Path("docs/PASSIVE_METRIC_ACCEPTANCE_CRITERIA_v0.1.3.md")

EXPECTED_SENTENCE_TYPES = frozenset(
    {"WORLD_EVENT", "OBSERVATION", "EVIDENCE", "LEDGER", "BELIEF", "REPORT"}
)

FOUNDATION_FUNCTIONS = {
    "observe_event",
    "create_evidence_record",
    "append_ledger_entry",
    "build_belief_state_snapshot",
    "create_observation_report",
}

METRIC_IMPLEMENTATION_NAMES = {
    "PhysicsMetric",
    "Pressure",
    "Potential",
    "Cost",
    "Inhibition",
    "Stability",
    "MetricRecord",
    "PassiveMetric",
    "calculate_pressure_metric",
    "calculate_inhibition_metric",
    "calculate_stability_metric",
    "calculate_cost_metric",
    "calculate_potential_metric",
}


def _snake_case(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def test_passive_metric_acceptance_criteria_document_exists() -> None:
    assert CRITERIA_PATH.exists()


def test_acceptance_criteria_define_candidates_and_exclusions() -> None:
    text = CRITERIA_PATH.read_text(encoding="utf-8").lower()
    candidates = text.split("## first implementation candidates", maxsplit=1)[
        1
    ].split("## excluded from first implementation", maxsplit=1)[0]
    excluded = text.split("## excluded from first implementation", maxsplit=1)[
        1
    ].split("## allowed read surface", maxsplit=1)[0]

    for term in ("pressure", "inhibition", "stability"):
        assert term in candidates
    for term in ("cost", "potential"):
        assert term in excluded


def test_acceptance_criteria_limit_read_surface() -> None:
    text = CRITERIA_PATH.read_text(encoding="utf-8")

    for phrase in (
        "BeliefStateSnapshot",
        "source_evidence_ids_json",
        "safe descriptive foundation payload fields",
    ):
        assert phrase in text


def test_acceptance_criteria_forbid_effects() -> None:
    text = CRITERIA_PATH.read_text(encoding="utf-8")

    for phrase in (
        "Ledger writes",
        "Evidence creation",
        "Belief mutation",
        "Report triggering",
        "TransitionCandidate",
        "ConstraintDecision",
        "Reaction",
        "MemoryWrite",
        "prioritization",
        "recommendation",
        "permission",
        "activation",
        "action",
        "truth creation",
    ):
        assert phrase in text


def test_metric_output_shape_is_deferred_to_v0_1_5() -> None:
    text = CRITERIA_PATH.read_text(encoding="utf-8")

    assert "passive descriptive label plus explanation only" in text
    assert "exact output shape is deferred to v0.1.5" in text


def test_metric_implementation_artifacts_remain_absent_from_src() -> None:
    source_root = Path(genus_core.__file__).parent
    forbidden_file_stems = {_snake_case(name) for name in METRIC_IMPLEMENTATION_NAMES}
    forbidden_names = METRIC_IMPLEMENTATION_NAMES.union(forbidden_file_stems)
    discovered_names: set[str] = set()
    discovered_imports: set[str] = set()

    for module_info in pkgutil.walk_packages(
        genus_core.__path__, genus_core.__name__ + "."
    ):
        module = importlib.import_module(module_info.name)
        discovered_names.add(module_info.name.rsplit(".", 1)[-1])
        discovered_names.update(getattr(module, "__all__", ()))
        discovered_names.update(
            name for name in vars(module) if not name.startswith("_")
        )
        for name, value in inspect.getmembers(module):
            if inspect.isclass(value) and value.__module__.startswith("genus_core"):
                discovered_names.add(name)

    for source_file in source_root.rglob("*.py"):
        discovered_names.add(source_file.stem)
        tree = ast.parse(source_file.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    discovered_imports.add(alias.name.rsplit(".", 1)[-1])
                    discovered_imports.add(alias.asname or "")
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    discovered_imports.add(node.module.rsplit(".", 1)[-1])
                for alias in node.names:
                    discovered_imports.add(alias.name)
                    discovered_imports.add(alias.asname or "")
            elif isinstance(node, ast.FunctionDef):
                discovered_names.add(node.name)

    assert forbidden_names.isdisjoint(discovered_names)
    assert forbidden_names.isdisjoint(discovered_imports)


def test_metric_acceptance_does_not_expand_language_functions_or_cli(capsys) -> None:
    assert ALLOWED_SENTENCE_TYPES == EXPECTED_SENTENCE_TYPES
    assert set(foundation_functions.__all__) == FOUNDATION_FUNCTIONS

    try:
        cli.main(["--help"])
    except SystemExit as exc:
        assert exc.code == 0

    help_text = capsys.readouterr().out
    assert "{observe}" in help_text
    assert "observe" in help_text
    assert "metric" not in help_text
    assert "physics" not in help_text
