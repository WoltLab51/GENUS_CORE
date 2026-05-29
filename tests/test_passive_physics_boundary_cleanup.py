import ast
import importlib
import inspect
import pkgutil
import re
from pathlib import Path

import genus_core
import genus_core.cli as cli
import genus_core.functions as foundation_functions
import genus_core.passive_physics as passive_physics
import genus_core.passive_transition as passive_transition
from genus_core.language import ALLOWED_SENTENCE_TYPES
from genus_core.truth import connect


ALLOWED_PASSIVE_PHYSICS_ARTIFACTS = {
    "PassiveMetricSnapshot",
    "PassiveMetricReport",
    "build_passive_metric_snapshot",
    "create_passive_metric_report",
}
ALLOWED_PASSIVE_TRANSITION_PREVIEW_ARTIFACTS = {
    "PassiveTransitionPreview",
    "PassiveTransitionReport",
    "build_passive_transition_preview",
    "create_passive_transition_report",
}

FORBIDDEN_ACTIVE_ARTIFACTS = {
    "PhysicsMetric",
    "PassiveMetric",
    "Pressure",
    "Inhibition",
    "Stability",
    "Cost",
    "Potential",
    "MetricRecord",
    "MetricOutput",
    "PassiveMetricOutput",
    "MetricOutputShape",
    "calculate_pressure_metric",
    "calculate_inhibition_metric",
    "calculate_stability_metric",
    "calculate_cost_metric",
    "calculate_potential_metric",
    "TransitionCandidate",
    "ConstraintDecision",
    "Reaction",
    "MemoryWrite",
    "Worker",
    "LLM",
    "RuntimeCell",
    "Organ",
    "Agent",
    "GraphDB",
    "RuntimeShape",
}

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


def _snake_case(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def _discover_src_names_and_imports() -> tuple[set[str], set[str]]:
    source_root = Path(genus_core.__file__).parent
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

    return discovered_names, discovered_imports


def test_allowed_passive_physics_artifacts_are_explicitly_exported() -> None:
    assert ALLOWED_PASSIVE_PHYSICS_ARTIFACTS.issubset(set(passive_physics.__all__))

    for name in ALLOWED_PASSIVE_PHYSICS_ARTIFACTS:
        assert hasattr(passive_physics, name)


def test_allowed_passive_transition_preview_artifacts_are_explicitly_exported() -> None:
    assert ALLOWED_PASSIVE_TRANSITION_PREVIEW_ARTIFACTS.issubset(
        set(passive_transition.__all__)
    )

    for name in ALLOWED_PASSIVE_TRANSITION_PREVIEW_ARTIFACTS:
        assert hasattr(passive_transition, name)


def test_allowed_passive_physics_artifacts_do_not_expand_foundation_api() -> None:
    assert set(foundation_functions.__all__) == FOUNDATION_FUNCTIONS
    assert ALLOWED_PASSIVE_PHYSICS_ARTIFACTS.isdisjoint(foundation_functions.__all__)
    assert ALLOWED_PASSIVE_TRANSITION_PREVIEW_ARTIFACTS.isdisjoint(
        foundation_functions.__all__
    )


def test_forbidden_active_artifacts_remain_absent_from_src() -> None:
    discovered_names, discovered_imports = _discover_src_names_and_imports()
    forbidden_file_stems = {_snake_case(name) for name in FORBIDDEN_ACTIVE_ARTIFACTS}
    forbidden_names = FORBIDDEN_ACTIVE_ARTIFACTS.union(forbidden_file_stems)

    assert forbidden_names.isdisjoint(discovered_names)
    assert forbidden_names.isdisjoint(discovered_imports)


def test_cli_language_and_truth_layer_remain_foundation_only(tmp_path, capsys) -> None:
    assert ALLOWED_SENTENCE_TYPES == EXPECTED_SENTENCE_TYPES

    try:
        cli.main(["--help"])
    except SystemExit as exc:
        assert exc.code == 0

    help_text = capsys.readouterr().out
    assert "{observe}" in help_text
    assert "metric" not in help_text
    assert "physics" not in help_text

    connection = connect(tmp_path / "truth.sqlite3")
    tables = {
        row[0]
        for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'"
        ).fetchall()
    }

    assert tables == {"evidence_records", "ledger_entries"}
