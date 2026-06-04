# GENUS Efficiency Method

Status: review document only. No runtime capability is introduced.

Purpose: define the efficiency method that should guide GENUS before any
performance-oriented runtime, model routing, cache, graph, memory, worker, or
agent implementation exists.

References:

```text
docs/reviews/GENUS_CORE_NEW_IDEA_COMPATIBILITY_CHECK.md
docs/reviews/GENUS_KERNEL_REPO_LEARNING_MAP.md
docs/kernel/GENUS_KERNEL_STCT_PROTOTYPE_SPEC.md
docs/kernel/GENUS_KERNEL_STCT_BASELINE_PLAN_v0.5.0.md
docs/vocabulary/kernel.md
```

## Executive Summary

GENUS should not become efficient by putting every situation into a large
model, asking it to reason from scratch, and repeating that loop.

The GENUS efficiency method is:

```text
Governed Semantic Compilation
```

Core rule:

```text
Interpret rarely.
Operate structurally.
Escalate only on uncertainty, novelty, risk, or ambiguity.
```

This means GENUS becomes efficient because raw language is compiled into
small, typed, governed meaning objects. GENUS then operates on structured
state, previews, constraints, traces, and reports instead of re-reading broad
natural-language context every time.

## Why Not LLM First

LLM-first orchestration is rejected as the GENUS core method.

It is flexible, but it is expensive, slow, hard to test, difficult to audit, and
too likely to mix truth, memory, permission, decision, and action.

Allowed future model role: parser, proposer, classifier, summarizer, renderer,
or uncertainty aid.

Forbidden model role: truth source, permission authority, decision authority,
memory writer, action executor, or governance bypass.

GENUS should be architecture-first intelligent. Small local models may assist
perception and wording, but GENUS structure must decide what a model output is
allowed to mean.

## Compared Methods

| Method | GENUS fit | Reason |
| --- | --- | --- |
| Pure LLM orchestration | Low | Flexible but costly, opaque, and unsafe as core. |
| Classical pipeline | Medium | Fast and testable, but too rigid alone. |
| Event sourcing / Ledger-first | High as trace | Auditable, but not enough for live efficiency. |
| Graph-first | Medium | Useful projection, not truth layer. |
| Semantic compilation | Very high | Turns language into reusable governed meaning. |
| State / belief cache | Very high | Enables live state without full replay. |
| Model routing | High later | Powerful after internal meaning is typed. |
| Hot / Governed path split | Required | Saves cost while preserving boundaries. |

Optimal method:

```text
Semantic Compilation
+ State Cache
+ Model Routing
+ Hot/Governed Path
+ Ledger Trace
```

## Core Flow

Target efficiency flow:

```text
Raw Language
-> MeaningObject
-> Belief/State Object
-> Kernel Preview
-> Constraint Boundary
-> Trace
-> Report
```

Operating law:

```text
LLM interprets.
GENUS compiles.
Kernel computes.
Governance bounds.
Ledger evidences.
```

The model may help propose meaning. GENUS must validate, type, bound, and trace
that meaning before it can influence downstream state.

## Structured Internal Language

GENUS should prefer compact internal meaning over repeated natural-language
reasoning.

Candidate internal fields: `intent`, `context_ref`, `risk`, `effect_class`,
`room`, `sensitivity`, `state_ref`, `transition_preview_ref`,
`constraint_preview_ref`, `trace_ref`, `capability_ref`, and `resource_ref`.

Example shape:

```json
{
  "intent": "memory_request",
  "effect_class": "proposal_only",
  "risk": "low",
  "requires_trace": true,
  "forbidden": ["direct_write", "external_call"]
}
```

This is not an accepted runtime schema. It is a review-level example of the
kind of compact meaning object GENUS may later specify.

## Hot Path

Hot paths are allowed only when they are already bounded.

Allowed hot-path operations: read cache, reconstruct state, classify low-risk
intent, create passive preview, create passive report, or route to a no-effect
capability description.

Forbidden hot-path operations: `MemoryWrite`, `Reaction`, tool execution,
external call, permission, `ConstraintDecision`, `PolicyResult`, allow/block,
or approval/rejection.

Hot path means less work, not less governance.

## State Cache

GENUS needs live state, but cache must not become truth.

Allowed cache role: fast projection, derived state, reviewable shortcut, or
replayable summary.

Forbidden cache role: Ledger replacement, Memory replacement, world truth,
permission source, or decision source.

Every important cached state must be traceable back to evidence, ledger, or
explicit prior artifacts.

## Graph Projection

A future graph may help with relation lookup, capability mapping, dependency
inspection, and habitat routing.

Boundary:

```text
Graph = projection
Graph != truth
Graph != Memory
Graph != ConstraintDecision
```

Graph-first is rejected. Graph-as-projection is compatible.

## Model Routing

Future model routing should prefer the cheapest sufficient mechanism:
deterministic rule, small local classifier, small local language model,
specialized adapter, and larger model only on uncertainty, novelty, risk, or
ambiguity.

Routing must be governed. The router must not decide truth, permission, memory
write, reaction, or external effect.

## Commission Boundary

Efficiency must not become hidden autonomy.

Later execution may use:

```text
Organ -> Commission -> AgentInstance -> Trace -> Report
```

But not before CORE/KERNEL grounding and explicit governance exist.

Boundary:

```text
No agent without commission.
No commission without organ boundary.
No organ without CORE/KERNEL grounding.
```

## What GENUS Already Uses

GENUS_CORE already uses small artifacts, typed boundaries, evidence lineage,
passive previews, reports without decisions, and tests against forbidden
effects.

What is not yet fully used: `MeaningObject`, structured internal language,
state cache policy, model routing, hot/governed path taxonomy, memory
lifecycle, graph projection boundary, and habitat-aware execution.

## Final Recommendation

Adopt Governed Semantic Compilation as the GENUS efficiency method before
runtime optimization work begins.

Do not implement it yet. First specify vocabulary, acceptance gates, stop
gates, and artifact boundaries.

Assessment:

```text
Plausibel: ja
Konsistent: ja
Vollstaendig: teilweise
Empfehlung: akzeptieren als Review-Methode, noch nicht als Runtime
```
