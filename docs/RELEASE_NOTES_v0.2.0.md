# GENUS_CORE v0.2.0 Release Notes

Release name: Passive Physics Seed

## Summary

`GENUS_CORE v0.2.0` introduces the first narrow passive Physics layer after the
passive foundation and governance baseline.

This release remains descriptive, side-effect free, and downstream of
`BeliefStateSnapshot`.

## Changes

- Package version moves to 0.2.0.
- `SCHEMA_VERSION` remains `genus.foundation.v0.0.1`.
- Adds `PassiveMetricSnapshot` and `PassiveMetricReport`.
- Adds `build_passive_metric_snapshot` and `create_passive_metric_report` in
  `genus_core.passive_physics`.
- First active metric names are exactly `pressure`, `inhibition`, and
  `stability`.
- `cost` and `potential` remain excluded from the first implementation.
- Passive metric outputs use the v0.1.5 output shape:
  `metric_name`, `level`, `assessment_status`, `explanation`,
  `source_state_id`, and `source_evidence_ids_json`.

## Non-Changes

v0.2.0 does not introduce:

- PhysicsMetric, PassiveMetric, Pressure, Potential, Cost, Inhibition, or
  Stability classes
- TransitionCandidate
- ConstraintDecision
- Reaction or ReactionExecution
- MemoryObject or MemoryWrite
- Worker, RuntimeCell, Organ, Agent, LLM, Mutation, Evolution, GraphDB, or
  RuntimeShape
- new sentence types
- new CLI commands
- new persistence tables
- passive metric persistence

## Acceptance

v0.2.0 is accepted only when:

- local pytest is green
- CLI smoke is green with a temporary `GENUS_CORE_TRUTH_DB`
- package version is 0.2.0
- `SCHEMA_VERSION` remains `genus.foundation.v0.0.1`
- public foundation functions remain unchanged
- CLI still exposes only `observe`
- GitHub Actions is green on the v0.2.0 commit
