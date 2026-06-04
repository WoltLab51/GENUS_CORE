# GENUS_KERNEL STCT Prototype Spec

Status: spec-only. No runtime capability is introduced.

Scope: define a future GENUS_KERNEL vocabulary for modelling governed change
without action.

Reference: `docs/reviews/GENUS_KERNEL_REPO_LEARNING_MAP.md`.

## Summary

GENUS_KERNEL is the future governed transition layer beneath capability cells
and organs.

```text
GENUS_CORE = Erkenntnis ohne Handlung
GENUS_KERNEL = Veraenderung ohne Handlung
```

This spec defines names and boundaries only. It does not add Python modules,
CLI commands, SQLite tables, workers, LLMs, reactions, memory writes, agents,
organs, autonomy, or runtime behavior.

## Kernel Chain

Target chain:

```text
BeliefStateSnapshot
-> KernelStateSnapshot
-> KernelTransitionPreview
-> KernelConstraintCheckPreview
-> KernelTraceEntry
-> KernelReport
-> no_action boundary statement
```

This chain is a prototype vocabulary, not an active GENUS_CORE runtime chain.

## Architecture Law

GENUS_KERNEL must not observe raw input.

Allowed future inputs: `BeliefStateSnapshot` or explicit future `StateInput`.

Forbidden inputs: raw text, raw user request, raw sensor event, raw external
event, implicit memory, or LLM-only interpretation.

`StateInput` is not defined by this spec. It may exist only after a separate
approved specification.

## Artifact Roles

### KernelStateSnapshot

Role: represent the kernel's internal state view derived from
`BeliefStateSnapshot` or a future explicit `StateInput`.

Not role: observation, evidence record, ledger entry, memory object, world
truth, or raw input parser.

### KernelTransitionPreview

Role: describe a possible change question from a `KernelStateSnapshot`.

Allowed wording: possible transition shape, unknowns, dependencies, missing
evidence, and downstream questions.

Forbidden wording: selected target state, recommended action, priority to
execute, permission, or candidate chosen for execution.

Boundary:

```text
KernelTransitionPreview != TransitionCandidate
```

### KernelConstraintCheckPreview

Role: describe which constraint areas would need review if the previewed
transition were ever evaluated later.

Allowed wording: relevant boundary area, missing constraint evidence, open
governance question, and known ambiguity.

Forbidden wording: allow, block, approve, reject, policy passed, permission
granted, or execution safe.

Boundary:

```text
KernelConstraintCheckPreview != ConstraintDecision
```

### KernelTraceEntry

Role: provide a spec-level trace concept explaining how the kernel preview was
formed from prior state and boundary inputs.

Trace law:

```text
KernelTraceEntry is spec-level only.
It does not replace LedgerEntry.
It does not create a new durable truth layer.
It does not expand SQLite schema.
It may later map to LedgerEntry or DecisionTrace only through a separate approved spec.
```

Boundary:

```text
KernelTraceEntry != LedgerEntry
KernelTraceEntry != Memory
KernelTraceEntry != Weltwahrheit
```

### KernelReport

Role: explain the passive kernel chain in a human-readable report.

Not role: decision, permission result, action plan, execution command, memory
write, or policy result.

`no_action` rule:

```text
KernelReport no_action statement != ConstraintDecision(no_action)
```

In this spec, `no_action` is only a boundary statement inside `KernelReport`.
It is not an allow/block decision, not permission, not a policy result, and does
not authorize or start anything.

## Hard Exclusions

This spec explicitly excludes:

```text
No raw input.
No decision.
No permission.
No action.
No persistence expansion.
No runtime capability.
No MemoryWrite.
No Reaction.
No Worker.
No LLM.
No Agent.
No RuntimeCell.
No Organ.
No GraphDB.
No Autonomy.
No Self-mutation.
```

## Compatibility With GENUS_CORE

GENUS_CORE remains unchanged:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

GENUS_KERNEL starts after the passive foundation has produced a state view.
It does not replace `Observation`, `EvidenceRecord`, `LedgerEntry`,
`BeliefStateSnapshot`, or `ObservationReport`.

## Release Path

Recommended staged path:

| Release | Concept | Boundary |
| --- | --- | --- |
| v0.5.0 | `TransitionCandidatePreview` | Preview only, not candidate. |
| v0.6.0 | `PassiveConstraintCheckPreview` | Check preview only, not decision. |
| v0.7.0 | minimal `ConstraintDecision(no_action | preview_only)` | Decision vocabulary only, no action. |

This STCT prototype spec does not implement any of these releases. It only
defines the safer kernel language that should guide them.

## Files That Must Stay Unchanged For This Step

This spec-only step must not change `README.md`, `docs/STATUS.md`,
`docs/DECISIONS.md`, `docs/VOCABULARY.md`, `src/`, `tests/`, SQLite schema, or
CLI behavior.

The existing review file
`docs/reviews/GENUS_CORE_NEW_IDEA_COMPATIBILITY_CHECK.md` remains prior work
and should not be rewritten by this step.

## Test Strategy

No runtime tests are required because this spec adds no runtime behavior.

Recommended verification: `python -m pytest tests/test_project_structure_guardrails.py`
and `python -m pytest tests/test_no_forbidden_objects_exist.py`.

Manual checks: `docs/kernel/` contains spec documents only; all new docs stay
under 260 lines; no runtime, schema, CLI, README, STATUS, DECISIONS, or
VOCABULARY change exists.

## Final Recommendation

Accept this as the first GENUS_KERNEL specification step. Do not implement
runtime behavior yet.

Assessment:

```text
Plausibel: ja
Konsistent: ja
Vollstaendig: ja fuer den Spec-Schritt
Empfehlung: akzeptieren
```
