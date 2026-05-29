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


REQUIREMENTS_PATH = Path("docs/PRE_PHYSICS_REQUIREMENTS_v0.1.1.md")

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

PRE_PHYSICS_FORBIDDEN_ARTIFACTS = {
    "PhysicsMetric",
    "Pressure",
    "Potential",
    "Cost",
    "Inhibition",
    "Stability",
}


def _snake_case(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def test_pre_physics_requirements_document_exists() -> None:
    assert REQUIREMENTS_PATH.exists()


def test_pre_physics_requirements_define_passive_boundaries() -> None:
    text = REQUIREMENTS_PATH.read_text(encoding="utf-8").lower()

    for phrase in (
        "does not decide",
        "does not prioritize",
        "does not execute",
        "does not react",
        "does not write memory",
        "does not transition",
        "does not constrain",
        "does not create truth",
    ):
        assert phrase in text


def test_pre_physics_artifacts_remain_absent_from_src() -> None:
    source_root = Path(genus_core.__file__).parent
    forbidden_file_stems = {
        _snake_case(name) for name in PRE_PHYSICS_FORBIDDEN_ARTIFACTS
    }
    forbidden_names = PRE_PHYSICS_FORBIDDEN_ARTIFACTS.union(forbidden_file_stems)
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

    assert forbidden_names.isdisjoint(discovered_names)
    assert forbidden_names.isdisjoint(discovered_imports)


def test_pre_physics_does_not_expand_language_or_public_functions() -> None:
    assert ALLOWED_SENTENCE_TYPES == EXPECTED_SENTENCE_TYPES
    assert set(foundation_functions.__all__) == FOUNDATION_FUNCTIONS


def test_pre_physics_cli_still_exposes_only_observe(
    capsys,
) -> None:
    try:
        cli.main(["--help"])
    except SystemExit as exc:
        assert exc.code == 0

    help_text = capsys.readouterr().out
    assert "{observe}" in help_text
    assert "observe" in help_text
    assert "physics" not in help_text
    assert "metric" not in help_text
