from genus_core import cli


REQUIRED_OUTPUT_LINES = (
    "WorldEvent created",
    "Observation created",
    "EvidenceRecord created",
    "LedgerEntry appended",
    "BeliefStateSnapshot created",
    "ObservationReport created",
    "No action is possible under the passive foundation boundary.",
)

FORBIDDEN_OUTPUT_TEXT = (
    "Memory written",
    "Reaction executed",
    "Transition allowed",
    "Constraint decided",
)


def test_cli_observe_smoke_outputs_foundation_artifacts(
    tmp_path, monkeypatch, capsys
) -> None:
    monkeypatch.setenv("GENUS_CORE_TRUTH_DB", str(tmp_path / "truth.sqlite3"))

    exit_code = cli.main(["observe", "merk dir das: larumipsum"])

    assert exit_code == 0
    output = capsys.readouterr().out
    for required_line in REQUIRED_OUTPUT_LINES:
        assert required_line in output
    for forbidden_text in FORBIDDEN_OUTPUT_TEXT:
        assert forbidden_text not in output


def test_cli_observe_can_run_twice_without_ledger_collision(
    tmp_path, monkeypatch, capsys
) -> None:
    monkeypatch.setenv("GENUS_CORE_TRUTH_DB", str(tmp_path / "truth.sqlite3"))

    assert cli.main(["observe", "merk dir das: larumipsum"]) == 0
    assert cli.main(["observe", "merk dir das: larumipsum"]) == 0

    output = capsys.readouterr().out
    assert output.count("LedgerEntry appended") == 2
