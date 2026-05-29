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


AUDIT_PATH = Path("docs/PASSIVE_METRIC_SAFETY_AUDIT_v0.1.6.md")
OUTPUT_SHAPE_PATH = Path("docs/PASSIVE_METRIC_OUTPUT_SHAPE_v0.1.5.md")
CI_WORKFLOW_PATH = Path(".github/workflows/ci.yml")

REQUIRED_DOCUMENTS = (
    Path("docs/PRE_PHYSICS_REQUIREMENTS_v0.1.1.md"),
    Path("docs/PASSIVE_METRIC_VOCABULARY_v0.1.2.md"),
    Path("docs/PASSIVE_METRIC_ACCEPTANCE_CRITERIA_v0.1.3.md"),
    OUTPUT_SHAPE_PATH,
    CI_WORKFLOW_PATH,
)

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


def test_passive_metric_safety_audit_document_exists() -> None:
    assert AUDIT_PATH.exists()


def test_required_metric_preparation_documents_exist() -> None:
    for path in REQUIRED_DOCUMENTS:
        assert path.exists()


def test_status_level_consistency_rules_are_documented() -> None:
    audit_text = AUDIT_PATH.read_text(encoding="utf-8")
    output_text = OUTPUT_SHAPE_PATH.read_text(encoding="utf-8")

    for text in (audit_text, output_text):
        assert "assessment_status = insufficient_input requires level = none" in text
        assert "assessment_status = not_applicable requires level = none" in text
        assert (
            "assessment_status = assessed may use level = none | low | medium | high"
            in text
            or "assessment_status = assessed` may use `level = none`" in text
        )


def test_cost_and_potential_remain_excluded() -> None:
    audit_text = AUDIT_PATH.read_text(encoding="utf-8").lower()
    output_text = OUTPUT_SHAPE_PATH.read_text(encoding="utf-8").lower()
    excluded = _section(output_text, "## excluded from first output shape")

    for metric_name in ("cost", "potential"):
        assert metric_name in excluded
        assert f"{metric_name}" in audit_text
    assert "remain excluded from the first implementation and first output shape" in audit_text


def test_ci_workflow_remains_minimal() -> None:
    text = CI_WORKFLOW_PATH.read_text(encoding="utf-8").lower()

    for required in (
        'python -m pip install -e ".[dev]"',
        "python -m pytest",
        'python -m genus_core.cli observe "merk dir das: larumipsum"',
    ):
        assert required in text

    for forbidden in (
        "coverage",
        "lint",
        "ruff",
        "black",
        "mypy",
        "format",
        "matrix:",
        "actions/cache",
        "deploy",
        "upload-artifact",
        "pypi",
        "release",
    ):
        assert forbidden not in text


def test_metric_safety_artifacts_remain_absent_from_src() -> None:
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


def test_metric_safety_does_not_expand_language_functions_or_cli(capsys) -> None:
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
