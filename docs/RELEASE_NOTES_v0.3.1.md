# GENUS_CORE v0.3.1 Release Notes

Release name: Passive Transition Boundary Audit

## Summary

`GENUS_CORE v0.3.1` audits the passive transition preview layer introduced in
v0.3.0.

This release adds no runtime capability. It hardens
`PassiveTransitionReport.summary` against active wording and makes the
memory-tension `possible_future_question` more neutral.

## Changes

- Package version moves to 0.3.1.
- `SCHEMA_VERSION` remains `genus.foundation.v0.0.1`.
- The memory-tension question now asks whether observed memory content raises a
  governed memory question.
- Tests now prove `PassiveTransitionReport.summary` remains descriptive-only.

## Still Excluded

v0.3.1 does not introduce:

- TransitionCandidate
- ConstraintDecision
- Reaction
- MemoryWrite
- new preview types
- new metric names, cost, or potential
- new SQLite tables or schema migration
- CLI expansion
- LLM, Worker, RuntimeCell, Organ, Agent, GraphDB, or RuntimeShape capability

## Acceptance

v0.3.1 is accepted only when:

- pytest is green
- CLI smoke is green
- package version is 0.3.1
- public foundation functions remain unchanged
- CLI still exposes only `observe`
- durable truth layer remains `EvidenceRecord` and `LedgerEntry`
- `PassiveTransitionReport.summary` contains no active approval, decision,
  execution, memory, reaction, transition-selection, or candidate-selection
  wording
- GitHub Actions is green on the v0.3.1 commit
