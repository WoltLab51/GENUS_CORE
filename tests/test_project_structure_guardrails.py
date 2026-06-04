from pathlib import Path

import genus_core.functions as foundation_functions
from genus_core import SCHEMA_VERSION
from genus_core.truth import connect

ROOTS = (Path("src"), Path("tests"), Path("docs"))
NORMAL_LIMITS = {"src": 220, "tests": 220, "docs": 260}

HISTORICAL_LONGFILE_EXCEPTIONS = {
    "docs/FOUNDATION_SPEC_v0.0.1.md": {
        "max_lines": 512,
        "reason": "Frozen historical foundation specification.",
        "planned_split_or_review": "Review only if foundation spec is superseded.",
    },
    "docs/GENUS_LANGUAGE_SPEC_v0.0.1.md": {
        "max_lines": 377,
        "reason": "Frozen historical language specification.",
        "planned_split_or_review": "Review only if language spec is superseded.",
    },
    "docs/CODEX_IMPLEMENTATION_PROMPT_v0.0.1.md": {
        "max_lines": 279,
        "reason": "Historical implementation prompt snapshot.",
        "planned_split_or_review": "Review only if historical prompts are archived.",
    },
    "docs/decisions/v0.0.md": {
        "max_lines": 294,
        "reason": "Moved historical v0.0 through v0.1.0 decisions.",
        "planned_split_or_review": "Review only if historical decision files are split per release.",
    },
    "docs/vocabulary/foundation.md": {
        "max_lines": 305,
        "reason": "Moved historical foundation vocabulary and observation vocabulary.",
        "planned_split_or_review": "Review only if vocabulary files are split per release.",
    },
    "docs/quality_gates/v0.0.md": {
        "max_lines": 540,
        "reason": "Moved historical v0.0 quality gates.",
        "planned_split_or_review": "Review only if historical gate files are split per release.",
    },
    "docs/quality_gates/v0.1.md": {
        "max_lines": 490,
        "reason": "Moved historical v0.1 quality gates.",
        "planned_split_or_review": "Review only if historical gate files are split per release.",
    },
}

FOUNDATION_FUNCTIONS = {
    "observe_event",
    "create_evidence_record",
    "append_ledger_entry",
    "build_belief_state_snapshot",
    "create_observation_report",
}


def _line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


def _tracked_guarded_files() -> list[Path]:
    files: list[Path] = []
    for root in ROOTS:
        files.extend(
            path
            for path in root.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        )
    return files


def _repo_path(path: Path) -> str:
    return path.as_posix()


def test_build_rules_define_governed_artifacts_and_codex_split_rule() -> None:
    text = Path("docs/BUILD_RULES.md").read_text(encoding="utf-8")

    assert "GENUS_CORE build artifacts are governed artifacts." in text
    for term in ("runtime code", "tests", "docs", "specs", "decisions"):
        assert term in text
    assert "Codex must not silently append bulk content to oversized files." in text
    assert "split into a focused document" in text
    assert "genus_core.passive_boundary_relevance" in text
    assert "PassiveBoundaryRelevancePreview" in text
    assert "These artifacts must not enter `genus_core.functions.__all__`." in text


def test_project_structure_defines_document_roles_and_longfiles() -> None:
    text = Path("docs/PROJECT_STRUCTURE.md").read_text(encoding="utf-8")

    for doc_name in (
        "GENUS_CHARTER.md",
        "SAFETY_BOUNDARIES.md",
        "BUILD_RULES.md",
        "ARTIFACT_CONTRACTS.md",
        "FUNCTION_CELLS.md",
        "SPEC_BOUNDARIES.md",
        "QUALITY_GATES.md",
        "DECISIONS.md",
        "STATUS.md",
        "ROADMAP_STABLE_CORE.md",
        "VOCABULARY.md",
    ):
        assert doc_name in text
    for expected in ("docs/reviews/*.md", "docs/kernel/*.md", "review-only synthesis", "GENUS_KERNEL spec and planning strand"):
        assert expected in text
    assert "historical longfile" in text.lower()
    assert "max_lines" in text
    assert "planned_split_or_review" in text


def test_quality_gates_are_modularized_and_indexed() -> None:
    index_text = Path("docs/QUALITY_GATES.md").read_text(encoding="utf-8")
    modular_files = {
        Path("docs/quality_gates/v0.0.md"): "v0.0.1",
        Path("docs/quality_gates/v0.1.md"): "v0.1.10",
        Path("docs/quality_gates/v0.2.md"): "v0.2.1",
        Path("docs/quality_gates/v0.3.md"): "v0.3.3",
        Path("docs/quality_gates/v0.3.6.md"): "v0.3.6",
        Path("docs/quality_gates/v0.3.7.md"): "v0.3.7",
        Path("docs/quality_gates/v0.3.8.md"): "v0.3.8",
        Path("docs/quality_gates/v0.3.9.md"): "v0.3.9",
        Path("docs/quality_gates/v0.4.md"): "v0.4.1",
        Path("docs/quality_gates/planned.md"): "Planned v0.4.0",
    }

    assert _line_count(Path("docs/QUALITY_GATES.md")) <= NORMAL_LIMITS["docs"]
    assert "docs/quality_gates/" in index_text
    assert "docs/QUALITY_GATES.md" not in HISTORICAL_LONGFILE_EXCEPTIONS

    for path, expected_label in modular_files.items():
        assert path.exists()
        assert path.as_posix() in index_text
        assert expected_label in path.read_text(encoding="utf-8")


def test_decisions_are_modularized_and_indexed() -> None:
    index_text = Path("docs/DECISIONS.md").read_text(encoding="utf-8")
    modular_files = {
        Path("docs/decisions/v0.0.md"): "Decision 0015",
        Path("docs/decisions/v0.1.md"): "Decision 0025",
        Path("docs/decisions/v0.2.md"): "Decision 0027",
        Path("docs/decisions/v0.3.md"): "Decision 0038",
        Path("docs/decisions/v0.4.md"): "Decision 0042",
    }

    assert _line_count(Path("docs/DECISIONS.md")) <= NORMAL_LIMITS["docs"]
    assert "Active Decision Map" in index_text
    assert "docs/DECISIONS.md" not in HISTORICAL_LONGFILE_EXCEPTIONS

    for path, expected_label in modular_files.items():
        assert path.exists()
        assert path.as_posix() in index_text
        assert expected_label in path.read_text(encoding="utf-8")


def test_vocabulary_is_modularized_and_indexed() -> None:
    index_text = Path("docs/VOCABULARY.md").read_text(encoding="utf-8")
    modular_files = {
        Path("docs/vocabulary/foundation.md"): "WorldEvent",
        Path("docs/vocabulary/forbidden_future.md"): "MemoryWrite",
        Path("docs/vocabulary/passive_layers.md"): "PassiveMetricSnapshot",
        Path("docs/vocabulary/boundary_relevance.md"): "Passive Boundary Relevance",
    }

    assert _line_count(Path("docs/VOCABULARY.md")) <= NORMAL_LIMITS["docs"]
    assert "Active Vocabulary Map" in index_text
    assert "Vocabulary defines how GENUS terms may be used." in index_text
    assert "docs/VOCABULARY.md" not in HISTORICAL_LONGFILE_EXCEPTIONS

    for path, expected_label in modular_files.items():
        assert path.exists()
        assert path.as_posix() in index_text
        assert expected_label in path.read_text(encoding="utf-8")


def test_historical_longfile_exceptions_are_documented_and_bounded() -> None:
    assert HISTORICAL_LONGFILE_EXCEPTIONS

    for path_text, metadata in HISTORICAL_LONGFILE_EXCEPTIONS.items():
        assert metadata["max_lines"] > 0
        assert metadata["reason"]
        assert metadata["planned_split_or_review"]
        assert Path(path_text).exists()
        assert _line_count(Path(path_text)) <= metadata["max_lines"]


def test_guarded_files_stay_within_limits_or_explicit_exceptions() -> None:
    exceptions = set(HISTORICAL_LONGFILE_EXCEPTIONS)

    for path in _tracked_guarded_files():
        path_text = _repo_path(path)
        root_name = path.parts[0]
        line_count = _line_count(path)
        limit = NORMAL_LIMITS[root_name]

        if path_text in exceptions:
            assert line_count <= HISTORICAL_LONGFILE_EXCEPTIONS[path_text][
                "max_lines"
            ]
            continue

        assert line_count <= limit, f"{path_text} has {line_count} lines"


def test_build_structure_guardrails_do_not_expand_runtime_boundaries(tmp_path) -> None:
    assert SCHEMA_VERSION == "genus.foundation.v0.0.1"
    assert set(foundation_functions.__all__) == FOUNDATION_FUNCTIONS

    with connect(tmp_path / "truth.sqlite3") as connection:
        tables = {
            row[0]
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            ).fetchall()
        }

    assert tables == {"evidence_records", "ledger_entries"}
