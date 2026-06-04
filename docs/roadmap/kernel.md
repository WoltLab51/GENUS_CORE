# GENUS_CORE Roadmap - GENUS_KERNEL

Status: planned roadmap for GENUS_KERNEL docs-only baseline.

This file records the kernel path while GENUS_KERNEL remains a spec strand
inside GENUS_CORE.

## Direction

GENUS_CORE remains:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

GENUS_KERNEL is planned as:

```text
BeliefStateSnapshot
-> KernelStateSnapshot
-> KernelTransitionPreview
-> KernelConstraintCheckPreview
-> KernelTraceEntry
-> KernelReport
-> no_action boundary statement
```

The first accepted kernel step must remain docs-only.

## Layer Order

```text
Constitution
-> GENUS_CORE
-> GENUS_KERNEL
-> Capability Dimensions
-> Cells
-> Organs
-> Organisms
-> Characters / Interfaces
```

CORE and KERNEL are not organs.

## v0.5.0 - GENUS_KERNEL STCT Spec Baseline

Planned docs-only baseline for kernel vocabulary, decisions, quality gates,
roadmap, release notes, and repo-placement review.

No runtime capability is added.

## Later Runtime Sketch

The smallest later prototype, not active in v0.5.0:

```text
BeliefStateSnapshot
-> KernelStateSnapshot
-> KernelReport
-> no_action boundary statement
```

This would test only the CORE-to-KERNEL state handoff and passive explanation.
It would not activate transition preview, constraint check preview, or trace
runtime.

## Repo Placement

Short-term recommendation:

```text
GENUS_KERNEL stays as docs/kernel/ spec strand inside GENUS_CORE.
```

Reason: the first kernel contract depends on `BeliefStateSnapshot`.

Future option:

```text
Create a separate GENUS_KERNEL repo only after vocabulary, gates, handoff, and
minimal prototype boundaries are accepted.
```

## Stop Conditions

Stop if the roadmap is used to justify runtime code, schema changes, CLI
commands, MemoryWrite, Reaction, Worker, LLM, Agent, RuntimeCell, Organ,
GraphDB, Autonomy, TransitionCandidate, ConstraintDecision, or PolicyResult.
