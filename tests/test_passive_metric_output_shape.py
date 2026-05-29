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


OUTPUT_SHAPE_PATH = Path("docs/PASSIVE_METRIC_OUTPUT_SHAPE_v0.1.5.md")

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
    "MetricOutput",
    "PassiveMetricOutput",
    "MetricOutputShape",
    "calculate_pressure_metric",
    "calculate_inhibition_metric",
    "calculate_stability_metric",
    "calculate_cost_metric",
    "calculate_potential_metric",
}


def _snake_case(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def _section(text: str, heading: str) -> str:
    return text.split(heading, maxsplit=1)[1].split("## ", maxsplit=1)[0]


def test_passive_metric_output_shape_document_exists() -> None:
    assert OUTPUT_SHAPE_PATH.exists()


def test_output_shape_metric_names_and_exclusions() -> None:
    text = OUTPUT_SHAPE_PATH.read_text(encoding="utf-8").lower()
    allowed = _section(text, "## allowed first output metric names")
    excluded = _section(text, "## excluded from first output shape")

    for metric_name in ("pressure", "inhibition", "stability"):
        assert f"metric_name = {metric_name}" in allowed
    for metric_name in ("cost", "potential"):
        assert metric_name not in allowed
        assert metric_name in excluded


def test_output_shape_field_values_are_explicit_and_limited() -> None:
    text = OUTPUT_SHAPE_PATH.read_text(encoding="utf-8")

    for field in (
        "metric_name",
        "level",
        "assessment_status",
        "explanation",
        "source_state_id",
        "source_evidence_ids_json",
    ):
        assert field in text

    level_section = _section(text.lower(), "## level values")
    for value in ("none", "low", "medium", "high"):
        assert value in level_section

    status_section = _section(text.lower(), "## assessment status values")
    for value in ("assessed", "insufficient_input", "not_applicable"):
        assert value in status_section


def test_none_level_is_not_insufficient_input() -> None:
    text = OUTPUT_SHAPE_PATH.read_text(encoding="utf-8")

    assert "level = none" in text
    assert "must not mean insufficient input" in text
    assert "assessment_status = insufficient_input" in text


def test_explanation_and_lineage_boundaries_are_descriptive_only() -> None:
    text = OUTPUT_SHAPE_PATH.read_text(encoding="utf-8")

    for phrase in (
        "`explanation` is descriptive-only",
        "must not recommend, permit, approve, rank, prioritize, trigger, execute",
        "must not introduce facts not derivable from `source_state_id` and",
        "`source_evidence_ids_json` preserves evidence lineage only",
        "must not imply scoring, weighting, ranking, priority, or confidence",
    ):
        assert phrase in text


def test_forbidden_output_fields_are_excluded() -> None:
    text = OUTPUT_SHAPE_PATH.read_text(encoding="utf-8")
    forbidden_section = _section(text.lower(), "## forbidden output fields")

    for field in (
        "score",
        "priority",
        "rank",
        "recommendation",
        "permission",
        "decision",
        "approval",
        "action",
        "execute",
        "candidate",
        "transition",
        "constraint",
        "reaction",
        "memory_write",
        "truth",
    ):
        assert field in forbidden_section


def test_metric_output_shape_artifacts_remain_absent_from_src() -> None:
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


def test_metric_output_shape_does_not_expand_language_functions_or_cli(capsys) -> None:
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
