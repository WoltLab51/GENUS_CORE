from pathlib import Path


NORMAL_DOC_LIMIT = 260
NORMAL_TEST_LIMIT = 220


def _line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


def test_roadmap_is_modularized_and_indexed() -> None:
    index_text = Path("docs/ROADMAP_STABLE_CORE.md").read_text(encoding="utf-8")
    modular_files = {
        Path("docs/roadmap/foundation.md"): "v0.1.0",
        Path("docs/roadmap/pre_physics.md"): "v0.1.10",
        Path("docs/roadmap/passive_layers.md"): "v0.3.1",
        Path("docs/roadmap/governance.md"): "v0.3.9",
        Path("docs/roadmap/planned.md"): "Planned v0.4.0",
    }

    assert _line_count(Path("docs/ROADMAP_STABLE_CORE.md")) <= NORMAL_DOC_LIMIT
    assert "docs/roadmap/" in index_text

    for path, expected_label in modular_files.items():
        assert path.exists()
        assert path.as_posix() in index_text
        assert expected_label in path.read_text(encoding="utf-8")


def test_historical_specs_are_frozen_reference_documents() -> None:
    boundary_text = Path("docs/SPEC_BOUNDARIES.md").read_text(encoding="utf-8")

    assert "frozen historical references" in boundary_text
    assert "active governance documents" in boundary_text
    for path_text in (
        "docs/FOUNDATION_SPEC_v0.0.1.md",
        "docs/GENUS_LANGUAGE_SPEC_v0.0.1.md",
    ):
        text = Path(path_text).read_text(encoding="utf-8")
        assert "frozen historical reference" in text
        assert "must not override" in text


def test_ledger_lineage_tests_are_modularized() -> None:
    model_tests = Path("tests/test_ledger_lineage_model_hardening.py")
    sqlite_tests = Path("tests/test_ledger_lineage_sqlite_hardening.py")

    assert model_tests.exists()
    assert sqlite_tests.exists()
    assert not Path("tests/test_ledger_lineage_hardening.py").exists()
    assert _line_count(model_tests) <= NORMAL_TEST_LIMIT
    assert _line_count(sqlite_tests) <= NORMAL_TEST_LIMIT
