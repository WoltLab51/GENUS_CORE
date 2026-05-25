"""Minimal CLI smoke path for GENUS_CORE v0.0.1."""

import argparse
import os
from pathlib import Path

from genus_core.functions import (
    append_ledger_entry,
    build_belief_state_snapshot,
    create_evidence_record,
    create_observation_report,
    observe_event,
)
from genus_core.models.world_event import WorldEvent
from genus_core.truth import connect, save_evidence_record, save_ledger_entry

DEFAULT_DB_PATH = ".genus_core_truth.sqlite3"


def _observe(text: str) -> int:
    db_path = Path(os.environ.get("GENUS_CORE_TRUTH_DB", DEFAULT_DB_PATH))
    world_event = WorldEvent(event_type="user_text", raw_text=text)
    observation = observe_event(world_event)
    evidence_record = create_evidence_record(observation)
    ledger_entry = append_ledger_entry(
        step=1,
        event_type="evidence_record_created",
        source_kind="observation",
        source_id=observation.observation_id,
        target_kind="evidence_record",
        target_id=evidence_record.evidence_id,
    )
    belief_state_snapshot = build_belief_state_snapshot([evidence_record])
    observation_report = create_observation_report(belief_state_snapshot)

    with connect(db_path) as connection:
        save_evidence_record(connection, evidence_record)
        save_ledger_entry(connection, ledger_entry)

    print(f"WorldEvent created: {world_event.event_id}")
    print(f"Observation created: {observation.observation_id}")
    print(f"EvidenceRecord created: {evidence_record.evidence_id}")
    print(f"LedgerEntry appended: {ledger_entry.ledger_id}")
    print(f"BeliefStateSnapshot created: {belief_state_snapshot.state_id}")
    print(f"ObservationReport created: {observation_report.report_id}")
    print("No action possible in v0.0.1")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="genus-core")
    subparsers = parser.add_subparsers(dest="command", required=True)
    observe_parser = subparsers.add_parser("observe")
    observe_parser.add_argument("text")

    args = parser.parse_args(argv)
    if args.command == "observe":
        return _observe(args.text)
    parser.error(f"Unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
