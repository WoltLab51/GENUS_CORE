# GENUS_CORE v0.2.1 Release Notes

Release name: Passive Physics Boundary Cleanup

## Summary

`GENUS_CORE v0.2.1` clarifies the v0.2.0 passive Physics seed without adding
new runtime capability.

The release keeps passive Physics as a narrow descriptive metric layer
downstream of `BeliefStateSnapshot`. It updates documentation and tests so the
allowed v0.2.x passive artifacts are clear while active Physics, transition,
constraint, reaction, memory, worker, LLM, GraphDB, and RuntimeShape capability
remain forbidden.

## Changes

- Package version moves to 0.2.1.
- `SCHEMA_VERSION` remains `genus.foundation.v0.0.1`.
- `ObservationReport` is documented as foundation explanation, not physics
  measurement.
- `PassiveMetricReport` is documented as passive metric description only.
- v0.2.x passive Physics is clarified as narrow passive metric description, not
  dynamic physics, simulation, transition, constraint decision, or reaction.
- Pre-Physics gates now distinguish allowed passive v0.2.x artifacts from
  forbidden active metric implementation artifacts.

## Allowed Passive v0.2.x Artifacts

```text
PassiveMetricSnapshot
PassiveMetricReport
build_passive_metric_snapshot
create_passive_metric_report
```

These remain in `genus_core.passive_physics` and are not public foundation
functions.

## Still Excluded

v0.2.1 does not introduce:

- new metric names
- cost or potential
- scoring, priority, recommendation, permission, or decision
- transition, constraint, reaction, or memory write
- new SQLite tables or schema migration
- CLI expansion
- LLM, Worker, GraphDB, RuntimeShape, Cell, Organ, or Agent capability

## Acceptance

v0.2.1 is accepted only when:

- pytest is green
- CLI smoke is green
- package version is 0.2.1
- public foundation functions remain unchanged
- CLI still exposes only `observe`
- durable truth layer remains `EvidenceRecord` and `LedgerEntry`
- GitHub Actions is green on the v0.2.1 commit
