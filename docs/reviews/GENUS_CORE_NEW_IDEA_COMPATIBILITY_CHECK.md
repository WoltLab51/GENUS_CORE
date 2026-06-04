# GENUS_CORE New Idea Compatibility Check

Status: review document only. No runtime capability is introduced.

Reviewed baseline: `GENUS_CORE v0.4.3 - Artifact Contract and Boundary Wording Alignment`

Reviewed idea: `State -> Transition -> Constraint -> Trace`

## Executive Summary

The Governed Transition System idea is compatible with GENUS_CORE as a
long-term architectural direction, but not as an immediate runtime replacement.

The current repo is a frozen passive foundation plus narrow passive preview
layers. It is not a transition engine, constraint engine, policy system,
memory system, worker runtime, LLM runtime, or autonomous agent.

Safe mapping:

| Idea term | Current safe fit |
| --- | --- |
| State | `BeliefStateSnapshot` and passive snapshots |
| Transition | `PassiveTransitionPreview` only |
| Constraint | `PassiveBoundaryRelevancePreview` only, not evaluation |
| Trace | Evidence lineage, report lineage, and evidence-only `LedgerEntry` |

Accept the idea only as staged roadmap analysis. Do not rename, replace, or
weaken the passive foundation.

## Current Repo Baseline

Active foundation chain: `WorldEvent -> Observation -> EvidenceRecord -> LedgerEntry -> BeliefStateSnapshot -> ObservationReport`.

Active passive layers: `BeliefStateSnapshot -> PassiveMetricSnapshot -> PassiveMetricReport`; `BeliefStateSnapshot + PassiveMetricSnapshot -> PassiveTransitionPreview -> PassiveTransitionReport`; `BeliefStateSnapshot + PassiveMetricSnapshot + PassiveTransitionPreview -> PassiveBoundaryRelevancePreview -> PassiveBoundaryRelevanceReport`.

Durable layer: `EvidenceRecord`, `LedgerEntry`, SQLite tables `evidence_records` and `ledger_entries`, with `SCHEMA_VERSION = genus.foundation.v0.0.1`.

Active CLI capability: `observe`.

Explicitly not active: `TransitionCandidate`, `ConstraintDecision`, `PolicyResult`, `Reaction`, `ReactionExecution`, `MemoryWrite`, `MemoryObject`, `Worker`, `RuntimeCell`, `Organ`, `Agent`, `Character`, `LLM`, `Autonomy`, `Mutation`, `Evolution`, `GraphDB`, `RuntimeShape`.

## New Idea Summary

The study frames GENUS as a Governed Transition System:

| Primitive | Meaning |
| --- | --- |
| State | What is represented now. |
| Transition | What could change. |
| Constraint | What bounds a change. |
| Trace | What remains auditable. |

This is plausible and matches the charter's future growth order: `Passive Foundation -> Passive Physics -> Transition Preview -> Constraint Decision -> Controlled Reaction -> Memory`.

For this repo, the idea must be mapped onto existing passive artifacts, not
imported as a new core model.

## Compatibility Matrix

| Idea term | Current fit | Compatibility | Boundary |
| --- | --- | --- | --- |
| State | `BeliefStateSnapshot`, passive snapshots | High | Derived state, not world truth. |
| Transition | `PassiveTransitionPreview` | Partial | Preview only; not `TransitionCandidate`. |
| Constraint | Boundary relevance and safety docs | Partial | Relevance only; not decision. |
| Trace | Ledger and lineage fields | Partial | Ledger is evidence lineage only. |
| Governance | Charter, safety, contracts, gates, decisions, vocabulary | High | Already enforced. |
| Runtime STCT core | None | No | Would exceed current boundary. |

## Conflicts / Risks

Required non-equivalences: `Preview != Permission`; `Report != Decision`; `Ledger != Memory`; `Ledger != Weltwahrheit`; `Passive != Active`; `Policy != fachliche Decision`; `TransitionPreview != TransitionCandidate`; `BoundaryRelevance != ConstraintDecision`.

Concrete risks:

| Risk | Why it conflicts |
| --- | --- |
| Replacing the foundation | Violates the v0.1.0 passive foundation freeze. |
| Treating preview as candidate | `TransitionCandidate` is explicitly forbidden. |
| Treating relevance as decision | `ConstraintDecision`, policy result, permission, and allow/block are forbidden. |
| Treating report as decision | Reports may explain only. |
| Treating ledger as memory or truth | Ledger is append-only evidence lineage, not memory and not world truth. |
| Importing the study literally | The study proposes a minimal STCT core, but this repo already has a frozen baseline. |
| Adding new runtime power | No new CLI, SQLite table, schema, worker, LLM, reaction, memory write, or autonomy is allowed. |

## Safe Integration Path

Safe rule: add future concepts downstream of the passive chain; never replace
the frozen foundation; keep each new step passive until governance accepts more
power.

### v0.5.0 TransitionCandidatePreview

Recommended shape: `BeliefStateSnapshot + PassiveMetricSnapshot + PassiveTransitionPreview -> TransitionCandidatePreview -> TransitionCandidatePreviewReport -> no decision -> no action`.

Hard boundary: `TransitionCandidatePreview != TransitionCandidate`; no
`target_state` selection, recommendation, permission, persistence, action, or
CLI expansion.

### v0.6.0 PassiveConstraintCheckPreview

Recommended shape: `upstream passive artifacts + TransitionCandidatePreview + PassiveBoundaryRelevancePreview -> PassiveConstraintCheckPreview -> PassiveConstraintCheckReport -> no decision -> no action`.

Hard boundary: `PassiveConstraintCheckPreview != ConstraintDecision`; no policy
evaluation, permission evaluation, allow/block, approve/reject, action, or
memory write.

### v0.7.0 Minimal ConstraintDecision(no_action | preview_only)

This is the first stage that may introduce a real decision artifact, but only
after v0.5.0 and v0.6.0 prove passive separation.

Allowed values: `no_action`, `preview_only`.

Forbidden values: `allow`, `block`, `approve`, `reject`, `execute`,
`write_memory`, `react`.

Even then, no Reaction, MemoryWrite, Worker, LLM, autonomy, or execution should
be introduced.

## Recommended Release Plan

1. Keep v0.4.x unchanged.
2. Accept this file as review-only documentation.
3. Before v0.5.0, add focused spec, vocabulary, decision, quality gate, and tests for `TransitionCandidatePreview`.
4. Before v0.6.0, define passive constraint-check vocabulary that separates relevance, check preview, policy, and decision.
5. Before v0.7.0, require an explicit governance decision for minimal `ConstraintDecision`.
6. Keep `SCHEMA_VERSION` unchanged unless a separate schema release is accepted.
7. Keep CLI at `observe` unless a separate CLI release is accepted.

## Files Likely Affected

Future governance/spec work would likely affect `docs/SAFETY_BOUNDARIES.md`, `docs/ARTIFACT_CONTRACTS.md`, `docs/BUILD_RULES.md`, `docs/FUNCTION_CELLS.md`, `docs/QUALITY_GATES.md`, `docs/DECISIONS.md`, `docs/STATUS.md`, `docs/VOCABULARY.md`, `docs/roadmap/planned.md`, `docs/vocabulary/forbidden_future.md`, `docs/vocabulary/passive_layers.md`, and `tests/test_no_forbidden_objects_exist.py`.

Future runtime work, only after acceptance, should use focused namespaces:

```text
src/genus_core/passive_transition_candidate_preview/
src/genus_core/passive_constraint_check/
src/genus_core/constraint_decision/
```

The last namespace must stay absent until a real decision release is accepted.

## Files That Must Stay Unchanged

These files should not be changed for this review-only step: `src/genus_core/models/world_event.py`, `src/genus_core/models/observation.py`, `src/genus_core/models/evidence_record.py`, `src/genus_core/models/ledger_entry.py`, `src/genus_core/models/belief_state_snapshot.py`, `src/genus_core/models/observation_report.py`, `src/genus_core/functions/`, `src/genus_core/truth/sqlite_store.py`, `src/genus_core/cli.py`, `tests/test_ledger_append_only.py`, `tests/test_report_has_no_decision_power.py`, `tests/test_no_forbidden_objects_exist.py`.

They may receive future hardening only when a governed release requires it.

## Test Strategy

Review-only phase: no runtime test is required because no runtime code changed.
Optional regression: `python -m pytest`.

Future v0.5.0 tests: `TransitionCandidatePreview is not TransitionCandidate`; no permission, recommendation, priority, `target_state`, action, persistence, CLI, or schema change; lineage matches `BeliefStateSnapshot`, `PassiveMetricSnapshot`, and `PassiveTransitionPreview`.

Future v0.6.0 tests: `PassiveConstraintCheckPreview is not ConstraintDecision`; no policy evaluation, permission evaluation, allow/block, approve/reject, action, reaction, or `memory_write`; `BoundaryRelevance` remains relevance only.

Future v0.7.0 tests: `ConstraintDecision` accepts only `no_action` and `preview_only`; Policy is not fachliche Decision; Decision is not action; Ledger remains evidence lineage unless separate trace persistence is accepted.

## Final Recommendation

Accept the idea as a compatible direction, but sharpen it before
implementation.

Do not implement it now. Do not rename the foundation into STCT. Do not
introduce `TransitionCandidate` in v0.5.0. Do not introduce
`ConstraintDecision` before v0.7.0. Do not broaden Ledger into memory, world
truth, or general transition trace.

Final assessment:

```text
Plausibel: ja
Konsistent: teilweise
Vollstaendig: teilweise
Empfehlung: nachschaerfen
```

Reason: The direction fits the charter and existing passive progression, but
repo-local phase definitions must be stricter before any runtime change.
