# GENUS_CORE v0.1.9 Release Notes

Release name: Boundary Naming Cleanup

## Summary

`GENUS_CORE v0.1.9` sharpens passive foundation terminology before v0.2.0
passive Physics work begins.

This release adds no runtime capability, no Physics implementation, no memory
write path, no Worker capability, and no CLI expansion.

## Changes

- Package version moves to 0.1.9.
- `SCHEMA_VERSION` remains `genus.foundation.v0.0.1`.
- Ephemeral Belief and Report payloads use `observed_memory_request` instead of
  `pending_memory_request`.
- Observed memory request content uses `observed_memory_content` instead of
  `candidate_content`.
- Report wording now says no action is possible under the passive foundation
  boundary.
- README separates package version, foundation schema version, capability
  boundary, durable truth layer, and ephemeral derivation.
- Historical specs now document that active v0.1.7+ Ledger flow requires
  `target_kind` and `target_id`.
- CI workflow integrity tests verify the CLI smoke command remains inside a
  YAML block scalar.

## Non-Changes

v0.1.9 does not introduce:

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

v0.1.9 is accepted only when:

- local pytest is green
- CLI smoke is green with a temporary `GENUS_CORE_TRUTH_DB`
- package version is 0.1.9
- `SCHEMA_VERSION` remains `genus.foundation.v0.0.1`
- active Belief and Report payloads use the observed-memory names only
- the CI workflow test guards the YAML block scalar smoke command
