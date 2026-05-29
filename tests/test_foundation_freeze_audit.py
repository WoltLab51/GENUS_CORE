import ast
import re
from pathlib import Path

import pytest

import genus_core
import genus_core.cli as cli
import genus_core.functions as foundation_functions
from genus_core.functions import (
    append_ledger_entry,
    build_belief_state_snapshot,
    create_evidence_record,
    create_observation_report,
    observe_event,
)
from genus_core.language import ALLOWED_SENTENCE_TYPES
from genus_core.models import (
    BeliefStateSnapshot,
    EvidenceRecord,
    LedgerEntry,
    Observation,
    ObservationReport,
    WorldEvent,
)


FOUNDATION_FUNCTIONS = (
    "observe_event",
    "create_evidence_record",
    "append_ledger_entry",
    "build_belief_state_snapshot",
    "create_observation_report",
)

EXPECTED_SENTENCE_TYPES = frozenset(
    {"WORLD_EVENT", "OBSERVATION", "EVIDENCE", "LEDGER", "BELIEF", "REPORT"}
)

FORBIDDEN_FUTURE_ARTIFACTS = {
    "PhysicsMetric",
    "Pressure",
    "Potential",
    "Cost",
    "Inhibition",
    "Stability",
    "CognitiveStateMap",
    "TransitionCandidate",
    "ConstraintDecision",
    "Reaction",
    "ReactionExecution",
    "MemoryWrite",
    "MemoryObject",
    "Worker",
    "RuntimeCell",
    "Organ",
    "Agent",
    "Character",
    "LLM",
    "Autonomy",
    "Mutation",
    "Evolution",
    "GraphDB",
    "RuntimeShape",
}


def _snake_case(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def test_current_version_and_foundation_schema_are_frozen() -> None:
    assert genus_core.__version__ == "0.3.3"
    assert genus_core.SCHEMA_VERSION == "genus.foundation.v0.0.1"


def test_foundation_sentence_types_remain_exact() -> None:
    assert ALLOWED_SENTENCE_TYPES == EXPECTED_SENTENCE_TYPES


def test_public_foundation_functions_remain_exact() -> None:
    assert set(foundation_functions.__all__) == set(FOUNDATION_FUNCTIONS)


def test_foundation_chain_composes_only_existing_artifacts() -> None:
    world_event = WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    observation = observe_event(world_event)
    evidence = create_evidence_record(observation)
    ledger = append_ledger_entry(
        step=1,
        event_type="evidence_record_created",
        source_kind="observation",
        source_id=observation.observation_id,
        target_kind="evidence_record",
        target_id=evidence.evidence_id,
    )
    belief = build_belief_state_snapshot([evidence])
    report = create_observation_report(belief)

    assert isinstance(observation, Observation)
    assert isinstance(evidence, EvidenceRecord)
    assert isinstance(ledger, LedgerEntry)
    assert isinstance(belief, BeliefStateSnapshot)
    assert isinstance(report, ObservationReport)


def test_public_foundation_functions_do_not_reference_future_artifacts() -> None:
    function_root = Path(genus_core.__file__).parent / "functions"
    forbidden_identifiers = FORBIDDEN_FUTURE_ARTIFACTS.union(
        {_snake_case(name) for name in FORBIDDEN_FUTURE_ARTIFACTS}
    )
    discovered: set[str] = set()

    for source_file in function_root.glob("*.py"):
        tree = ast.parse(source_file.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    discovered.add(alias.name.rsplit(".", 1)[-1])
                    discovered.add(alias.asname or "")
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    discovered.add(node.module.rsplit(".", 1)[-1])
                for alias in node.names:
                    discovered.add(alias.name)
                    discovered.add(alias.asname or "")
            elif isinstance(node, ast.Name):
                discovered.add(node.id)
            elif isinstance(node, ast.Attribute):
                discovered.add(node.attr)

    assert forbidden_identifiers.isdisjoint(discovered)


def test_cli_exposes_only_observe_command(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc_info:
        cli.main(["--help"])

    assert exc_info.value.code == 0
    help_text = capsys.readouterr().out
    assert "{observe}" in help_text
    assert "observe" in help_text
    assert "react" not in help_text
    assert "memory" not in help_text
    assert "physics" not in help_text
