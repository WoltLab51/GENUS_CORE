from pathlib import Path

import genus_core.functions as foundation_functions
from genus_core import SCHEMA_VERSION
from genus_core.truth import connect


ROOTS = (Path("src"), Path("tests"), Path("docs"))
NORMAL_LIMITS = {
    "src": 220,
    "tests": 220,
    "docs": 260,
}

HISTORICAL_LONGFILE_EXCEPTIONS = {
    "docs/QUALITY_GATES.md": {
        "max_lines": 1307,
        "reason": "Historical acceptance and stop gates accumulated before modularization.",
        "planned_split_or_review": "v0.3.3 Documentation Modularization",
    },
    "docs/DECISIONS.md": {
        "max_lines": 642,
        "reason": "Historical architecture decision log accumulated before ADR split.",
        "planned_split_or_review": "v0.3.3 Documentation Modularization",
    },
    "docs/FOUNDATION_SPEC_v0.0.1.md": {
        "max_lines": 507,
        "reason": "Frozen historical foundation specification.",
        "planned_split_or_review": "Review only if foundation spec is superseded.",
    },
    "docs/GENUS_LANGUAGE_SPEC_v0.0.1.md": {
        "max_lines": 372,
        "reason": "Frozen historical language specification.",
        "planned_split_or_review": "Review only if language spec is superseded.",
    },
    "docs/VOCABULARY.md": {
        "max_lines": 486,
        "reason": "Historical vocabulary ledger for active and planned terms.",
        "planned_split_or_review": "v0.3.3 Documentation Modularization",
    },
    "docs/CODEX_IMPLEMENTATION_PROMPT_v0.0.1.md": {
        "max_lines": 279,
        "reason": "Historical implementation prompt snapshot.",
        "planned_split_or_review": "Review only if historical prompts are archived.",
    },
    "docs/ROADMAP_STABLE_CORE.md": {
        "max_lines": 361,
        "reason": "Historical phase roadmap accumulated before roadmap split.",
        "planned_split_or_review": "v0.3.3 Documentation Modularization",
    },
    "tests/test_ledger_lineage_hardening.py": {
        "max_lines": 305,
        "reason": "Historical focused ledger lineage hardening coverage.",
        "planned_split_or_review": "Review only when ledger tests are modularized.",
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


def test_project_structure_defines_document_roles_and_longfiles() -> None:
    text = Path("docs/PROJECT_STRUCTURE.md").read_text(encoding="utf-8")

    for doc_name in (
        "GENUS_CHARTER.md",
        "SAFETY_BOUNDARIES.md",
        "BUILD_RULES.md",
        "QUALITY_GATES.md",
        "DECISIONS.md",
        "STATUS.md",
        "ROADMAP_STABLE_CORE.md",
        "VOCABULARY.md",
    ):
        assert doc_name in text
    assert "historical longfile" in text.lower()
    assert "max_lines" in text
    assert "planned_split_or_review" in text


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
