import importlib
import inspect
import pkgutil
import tomllib
from pathlib import Path

import genus_core
import genus_core.cli as cli
import genus_core.functions as foundation_functions
from genus_core.truth import connect


SPEC_PATH = Path("docs/PASSIVE_BOUNDARY_RELEVANCE_SPEC_v0.4.0.md")

ACTIVE_ARTIFACTS = {
    "PassiveBoundaryRelevancePreview",
    "PassiveBoundaryRelevanceReport",
    "build_passive_boundary_relevance_preview",
    "create_passive_boundary_relevance_report",
}

PLANNED_BOUNDARY_AREAS = {
    "memory_boundary",
    "passive_foundation_boundary",
    "passive_preview_boundary",
}

HARD_EXCLUSIONS = {
    "ConstraintDecision",
    "Decision",
    "PolicyResult",
    "policy",
    "policy_status",
    "policy_result",
    "Authorization",
    "permission",
    "allow",
    "block",
    "approve",
    "reject",
    "recommendation",
    "priority",
    "score",
    "rank",
    "severity",
    "weight",
    "execute",
    "Reaction",
    "MemoryWrite",
    "TransitionCandidate",
    "target_state",
    "selected_transition",
    "proposed_transition",
    "LLM",
    "Worker",
    "GraphDB",
    "RuntimeShape",
}

FOUNDATION_FUNCTIONS = {
    "observe_event",
    "create_evidence_record",
    "append_ledger_entry",
    "build_belief_state_snapshot",
    "create_observation_report",
}

DOCS_WITH_PLANNED_V0_4_0_REFERENCES = (
    Path("README.md"),
    Path("docs/ROADMAP_STABLE_CORE.md"),
    Path("docs/DECISIONS.md"),
    Path("docs/QUALITY_GATES.md"),
    Path("docs/SAFETY_BOUNDARIES.md"),
)


def _spec_text() -> str:
    return SPEC_PATH.read_text(encoding="utf-8")


def _discover_runtime_names() -> set[str]:
    discovered_names: set[str] = set()

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
            elif inspect.isfunction(value) and value.__module__.startswith(
                "genus_core"
            ):
                discovered_names.add(name)

    return discovered_names


def test_passive_boundary_relevance_spec_exists_and_marks_runtime_seed() -> None:
    assert SPEC_PATH.exists()

    text = _spec_text()
    assert "Status: accepted spec baseline with narrow v0.4.1 runtime seed" in text
    assert "The v0.4.0 baseline was docs and tests only." in text
    assert "The v0.4.1 baseline activates" in text
    assert "passive preview and report artifacts" in text
    assert "No CLI commands, SQLite tables, sentence types" in text


def test_passive_boundary_relevance_spec_preserves_active_versions() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))
    text = _spec_text()

    assert pyproject["project"]["version"] == "0.4.1"
    assert genus_core.__version__ == "0.4.1"
    assert genus_core.SCHEMA_VERSION == "genus.foundation.v0.0.1"
    assert "Package version is `0.4.1`." in text
    assert "`SCHEMA_VERSION` remains `genus.foundation.v0.0.1`." in text


def test_passive_boundary_relevance_artifacts_are_active_but_not_foundation() -> None:
    text = _spec_text()
    runtime_names = _discover_runtime_names()

    for artifact in ACTIVE_ARTIFACTS:
        assert artifact in text
        assert artifact in runtime_names
    assert "These names are active in v0.4.1:" in text


def test_passive_boundary_relevance_spec_defines_closed_enum_and_rejections() -> None:
    text = _spec_text()

    assert "`boundary_area` must be a closed enum, not free-form text." in text
    for boundary_area in PLANNED_BOUNDARY_AREAS:
        assert boundary_area in text
    assert "Unknown `boundary_area` values must be rejected" in text


def test_passive_boundary_relevance_spec_keeps_relevance_descriptive_only() -> None:
    text = _spec_text()

    assert "Relevance means descriptive boundary relevance mapping only." in text
    assert "It does not evaluate boundaries." in text
    assert "It does not evaluate permission." in text
    assert "It does not evaluate policy." in text
    assert "`observed_boundary_relevance` must be descriptive only." in text
    for forbidden_shape in (
        "numeric",
        "level",
        "score",
        "rank",
        "priority",
        "severity",
        "weight",
        "recommendation",
        "permission",
    ):
        assert forbidden_shape in text


def test_passive_boundary_relevance_spec_contains_non_equivalence_rules() -> None:
    text = _spec_text()

    assert "PassiveBoundaryRelevancePreview != ConstraintDecision" in text
    assert "PassiveBoundaryRelevanceReport != PolicyResult" in text
    assert "observed_boundary_relevance != permission" in text
    assert "boundary_question != allow/block" in text


def test_passive_boundary_relevance_spec_contains_all_hard_exclusions() -> None:
    text = _spec_text()

    for exclusion in HARD_EXCLUSIONS:
        assert exclusion in text


def test_passive_boundary_relevance_docs_link_to_v0_4_boundary() -> None:
    for path in DOCS_WITH_PLANNED_V0_4_0_REFERENCES:
        text = path.read_text(encoding="utf-8").lower()
        assert "v0.4.0" in text
        assert "v0.4.1" in text or "passive boundary relevance" in text


def test_passive_boundary_relevance_keeps_foundation_api_unchanged() -> None:
    assert set(foundation_functions.__all__) == FOUNDATION_FUNCTIONS
    assert ACTIVE_ARTIFACTS.isdisjoint(foundation_functions.__all__)


def test_passive_boundary_relevance_keeps_cli_observe_only(capsys) -> None:
    try:
        cli.main(["--help"])
    except SystemExit as exc:
        assert exc.code == 0

    help_text = capsys.readouterr().out
    assert "{observe}" in help_text
    assert "boundary" not in help_text
    assert "relevance" not in help_text


def test_passive_boundary_relevance_keeps_sqlite_tables_unchanged(tmp_path) -> None:
    connection = connect(tmp_path / "truth.sqlite3")
    tables = {
        row[0]
        for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'"
        ).fetchall()
    }

    assert tables == {"evidence_records", "ledger_entries"}
