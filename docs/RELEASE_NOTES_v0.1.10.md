# GENUS_CORE v0.1.10 Release Notes

Release name: GENUS Charter and Safety Boundary

## Summary

`GENUS_CORE v0.1.10` anchors the GENUS vision as repository governance before
v0.2.0 passive Physics work begins.

This release adds no runtime capability, no passive Physics implementation, no
memory write path, no Worker capability, and no CLI expansion.

## Changes

- Package version moves to 0.1.10.
- `SCHEMA_VERSION` remains `genus.foundation.v0.0.1`.
- `docs/GENUS_CHARTER.md` defines the GENUS purpose, growth order, truth model,
  action discipline, LLM role, and top build instructions.
- `docs/SAFETY_BOUNDARIES.md` defines current operative boundaries and stop
  conditions for new power.
- `docs/BUILD_RULES.md` now explicitly references the Charter and Safety
  Boundaries.
- Governance tests prove these documents exist and contain the required GENUS
  directives.

## Non-Changes

v0.1.10 does not introduce:

- PhysicsMetric, PassiveMetric, Pressure, Potential, Cost, Inhibition, or
  Stability implementation
- CognitiveStateMap
- TransitionCandidate
- ConstraintDecision
- Reaction or ReactionExecution
- MemoryObject or MemoryWrite
- Worker, RuntimeCell, Organ, Agent, LLM, Mutation, Evolution, GraphDB, or
  RuntimeShape
- new persistence tables
- provenance default changes
- chain_id propagation changes
- new CLI commands

## Acceptance

v0.1.10 is accepted only when:

- local pytest is green
- CLI smoke is green with a temporary `GENUS_CORE_TRUTH_DB`
- package version is 0.1.10
- `SCHEMA_VERSION` remains `genus.foundation.v0.0.1`
- Charter and Safety Boundaries exist
- Build Rules reference both governance documents
- GitHub Actions is green on the v0.1.10 commit
