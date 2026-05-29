from pathlib import Path


WORKFLOW_PATH = Path(".github/workflows/ci.yml")


def test_ci_workflow_exists() -> None:
    assert WORKFLOW_PATH.exists()


def test_ci_workflow_is_minimal_release_integrity_gate() -> None:
    text = WORKFLOW_PATH.read_text(encoding="utf-8")

    for required in (
        "runs-on: ubuntu-latest",
        "uses: actions/checkout@",
        "uses: actions/setup-python@",
        'python-version: "3.12"',
        'python -m pip install -e ".[dev]"',
        "python -m pytest",
        'python -m genus_core.cli observe "merk dir das: larumipsum"',
        "GENUS_CORE_TRUTH_DB: ${{ runner.temp }}/genus_core_truth.sqlite3",
    ):
        assert required in text


def test_ci_workflow_does_not_add_extra_release_features() -> None:
    text = WORKFLOW_PATH.read_text(encoding="utf-8").lower()

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
