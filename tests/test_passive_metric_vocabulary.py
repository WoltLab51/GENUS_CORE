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


VOCABULARY_PATH = Path("docs/PASSIVE_METRIC_VOCABULARY_v0.1.2.md")

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

FORBIDDEN_ACTIVE_METRIC_IMPLEMENTATION_NAMES = {
    "PhysicsMetric",
    "Pressure",
    "Potential",
    "Cost",
    "Inhibition",
    "Stability",
    "calculate_pressure_metric",
    "calculate_inhibition_metric",
    "calculate_stability_metric",
    "calculate_cost_metric",
    "calculate_potential_metric",
    "MetricRecord",
    "PassiveMetric",
}


def _snake_case(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def test_passive_metric_vocabulary_document_exists() -> None:
    assert VOCABULARY_PATH.exists()


def test_metric_terms_are_defined_as_planned_not_active() -> None:
    text = VOCABULARY_PATH.read_text(encoding="utf-8").lower()

    for term in ("pressure", "inhibition", "stability", "cost", "potential"):
        assert f"## {term}" in text
        section = text.split(f"## {term}", maxsplit=1)[1].split("## ", maxsplit=1)[0]
        assert "planned-not-active" in section


def test_metric_vocabulary_marks_candidate_and_high_risk_groups() -> None:
    text = VOCABULARY_PATH.read_text(encoding="utf-8").lower()
    first_candidates = text.split("## first passive candidates", maxsplit=1)[1].split(
        "## higher-risk planned terms", maxsplit=1
    )[0]
    high_risk = text.split("## higher-risk planned terms", maxsplit=1)[1].split(
        "## vocabulary boundaries", maxsplit=1
    )[0]

    for term in ("pressure", "inhibition", "stability"):
        assert term in first_candidates
    for term in ("cost", "potential"):
        assert term in high_risk
    assert "not first implementation" in high_risk


def test_metric_terms_have_required_non_equivalence_boundaries() -> None:
    text = VOCABULARY_PATH.read_text(encoding="utf-8")

    for boundary in (
        "Metric Vocabulary != Metric Implementation",
        "Metric Term != Decision",
        "Metric Term != Priority",
        "Metric Term != Transition",
        "Metric Term != Action",
        "Metric Term != Permission",
        "Metric Term != Recommendation",
        "Metric Term != Activation",
        "Metric Term != MemoryWrite",
    ):
        assert boundary in text


def test_forbidden_active_metric_implementation_artifacts_remain_absent_from_src() -> None:
    source_root = Path(genus_core.__file__).parent
    forbidden_file_stems = {
        _snake_case(name) for name in FORBIDDEN_ACTIVE_METRIC_IMPLEMENTATION_NAMES
    }
    forbidden_names = FORBIDDEN_ACTIVE_METRIC_IMPLEMENTATION_NAMES.union(
        forbidden_file_stems
    )
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


def test_docs_and_tests_may_name_planned_metric_terms() -> None:
    docs_text = VOCABULARY_PATH.read_text(encoding="utf-8").lower()
    test_text = Path(__file__).read_text(encoding="utf-8").lower()

    assert "pressure" in docs_text
    assert "pressure" in test_text


def test_metric_vocabulary_does_not_expand_language_functions_or_cli(capsys) -> None:
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
