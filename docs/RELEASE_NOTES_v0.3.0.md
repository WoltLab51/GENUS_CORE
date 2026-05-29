# GENUS_CORE v0.3.0 Release Notes

Release name: Passive Transition Preview Seed

## Summary

`GENUS_CORE v0.3.0` introduces a narrow passive preview layer after passive
Physics.

The new layer reads a `BeliefStateSnapshot` and `PassiveMetricSnapshot` and
describes a possible later governed question. It does not create a transition
candidate, constraint decision, reaction, memory write, recommendation,
permission, priority, approval, target state, or action.

## Changes

- Package version moves to 0.3.0.
- `SCHEMA_VERSION` remains `genus.foundation.v0.0.1`.
- Adds `PassiveTransitionPreview` and `PassiveTransitionReport`.
- Adds `build_passive_transition_preview` and `create_passive_transition_report`.
- Keeps the new artifacts in `genus_core.passive_transition`.
- Keeps public foundation functions unchanged.
- Keeps durable truth storage limited to `EvidenceRecord` and `LedgerEntry`.

## Naming Boundary

The word `transition` may appear in passive v0.3.0 artifact names, module names,
function names, docs, and tests only when clearly qualified as passive preview
or forbidden active capability. It must not appear as a standalone output or
payload field and must not imply an active transition.

`possible_future_question` is a runtime field. Its value must remain
descriptive and question-like, and must not contain:

```text
should
must
allow
block
execute
write
approve
recommend
```

## Still Excluded

v0.3.0 does not introduce:

- TransitionCandidate
- ConstraintDecision
- Reaction
- MemoryWrite
- target_state
- selected_transition
- proposed_transition
- policy_result
- approval, permission, recommendation, priority, score, or rank
- new metric names, cost, or potential
- new SQLite tables or schema migration
- CLI expansion
- LLM, Worker, GraphDB, RuntimeShape, Cell, Organ, or Agent capability

## Acceptance

v0.3.0 is accepted only when:

- pytest is green
- CLI smoke is green
- package version is 0.3.0
- public foundation functions remain unchanged
- CLI still exposes only `observe`
- durable truth layer remains `EvidenceRecord` and `LedgerEntry`
- GitHub Actions is green on the v0.3.0 commit
