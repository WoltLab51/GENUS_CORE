# GENUS_KERNEL Vocabulary

Status: planned vocabulary for GENUS_KERNEL STCT docs-only baseline.

These terms are future spec terms only. They are not active GENUS_CORE runtime
artifacts.

## GENUS_KERNEL

What it is: future governed transition layer for modelling change without
action.

What it is not: observation core, memory system, reaction system, worker,
agent, organ, LLM layer, GraphDB, or autonomy layer.

Allowed phase: docs-only v0.5.0 planning and later accepted kernel specs.

Forbidden misuse: treating GENUS_KERNEL as active runtime before explicit
acceptance.

## KernelStateSnapshot

What it is: future kernel state view derived from `BeliefStateSnapshot` or a
future explicit `StateInput`.

What it is not: `BeliefStateSnapshot`, raw input parser, evidence record,
ledger entry, memory object, or world truth.

Allowed phase: future spec only.

Forbidden misuse: observing raw text, raw user request, raw external event, or
LLM-only interpretation.

## KernelTransitionPreview

What it is: future preview of a possible change question.

What it is not: `TransitionCandidate`, selected target state, recommendation,
priority, permission, or action plan.

Allowed phase: future spec only.

Forbidden misuse: using preview language as permission or execution readiness.

## KernelConstraintCheckPreview

What it is: future preview of constraint areas that would need review.

What it is not: `ConstraintDecision`, `PolicyResult`, allow/block,
approval/rejection, permission, or safety certification.

Allowed phase: future spec only.

Forbidden misuse: treating relevance, check, or ambiguity as a decision.

## KernelTraceEntry

What it is: future spec-level trace concept for explaining how a kernel preview
was formed.

What it is not: `LedgerEntry`, Memory, Weltwahrheit, durable truth layer, or
SQLite schema expansion.

Allowed phase: future spec only.

Forbidden misuse: persisting kernel trace or mapping it to Ledger without a
separate accepted spec.

## KernelReport

What it is: future passive explanation of a kernel chain.

What it is not: decision, permission result, policy result, action plan,
execution command, MemoryWrite, or Reaction.

Allowed phase: future spec only.

Forbidden misuse: treating `no_action` as `ConstraintDecision(no_action)`.

## StateInput

What it is: reserved future explicit kernel input concept.

What it is not: defined by v0.5.0, raw input shortcut, observation replacement,
memory lookup, or LLM interpretation.

Allowed phase: not active.

Forbidden misuse: using `StateInput` before a separate accepted spec defines it.

## no_action boundary statement

What it is: future report statement that no action is authorized by the kernel
chain.

What it is not: `ConstraintDecision(no_action)`, allow/block, permission,
policy result, recommendation, or execution command.

Allowed phase: future spec/report language only.

Forbidden misuse: treating it as a decision value before an accepted decision
release.
