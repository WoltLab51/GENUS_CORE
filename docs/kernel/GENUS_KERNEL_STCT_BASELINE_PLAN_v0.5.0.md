# GENUS_KERNEL STCT Baseline Plan v0.5.0

Status: planning document only. v0.5.0 is not accepted by this file.

Scope: define the next safe docs-only baseline question for GENUS_KERNEL after
the STCT prototype spec.

References:

```text
docs/reviews/GENUS_CORE_NEW_IDEA_COMPATIBILITY_CHECK.md
docs/reviews/GENUS_KERNEL_REPO_LEARNING_MAP.md
docs/kernel/GENUS_KERNEL_STCT_PROTOTYPE_SPEC.md
```

## Summary

GENUS_CORE is stable enough to serve as the passive epistemic foundation:

```text
GENUS_CORE = Erkenntnis ohne Handlung
```

GENUS_KERNEL should begin only as a docs-only governed transition baseline:

```text
GENUS_KERNEL = Veraenderung ohne Handlung
```

v0.5.0 should not introduce runtime behavior. Its job is to decide how the
kernel language becomes governed enough that a later minimal prototype can be
reviewed without drifting into action, memory, permission, or autonomy.

## Baseline Question

The v0.5.0 baseline question:

```text
Can GENUS describe a kernel state boundary and transition-language contract
without adding runtime capability?
```

The answer must remain documentation-only.

## Layer Position

GENUS_KERNEL sits below later capability systems:

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

GENUS_CORE and GENUS_KERNEL are not organs. They are foundation/kernel layers.

## Proposed v0.5.0 Output

v0.5.0 should produce a docs-only baseline containing:

| Artifact | Purpose |
| --- | --- |
| Kernel vocabulary contract | Defines future kernel terms and forbidden uses. |
| Kernel acceptance gate | Defines what must be true before runtime work. |
| Kernel stop gate | Lists terms and effects that halt the phase. |
| Repo placement decision | Decides whether GENUS_KERNEL stays here as spec or moves to its own repo later. |
| Minimal prototype sketch | Names the smallest future `KernelStateSnapshot` proof without implementing it. |

## Future Kernel Names

The approved planning names remain:

```text
KernelStateSnapshot
KernelTransitionPreview
KernelConstraintCheckPreview
KernelTraceEntry
KernelReport
```

These are future GENUS_KERNEL spec names. They are not active GENUS_CORE
runtime artifacts.

## Minimal Testable Prototype Sketch

The smallest later runtime prototype, not for v0.5.0, would ask:

```text
BeliefStateSnapshot -> KernelStateSnapshot -> KernelReport -> no_action boundary statement
```

This would test only state handoff and report explanation. It would not yet add
`KernelTransitionPreview`, `KernelConstraintCheckPreview`, or
`KernelTraceEntry` runtime objects.

Reason: the safest first proof is that GENUS_KERNEL can receive a state view
without re-observing raw input.

## Boundary Laws

v0.5.0 must preserve:

```text
GENUS_KERNEL must not observe raw input.
GENUS_KERNEL consumes BeliefStateSnapshot or explicit future StateInput.
Preview != Permission.
Report != Decision.
Ledger != Memory.
Ledger != Weltwahrheit.
Passive != Active.
Policy != fachliche Decision.
CORE/KERNEL != Organ.
```

`StateInput` remains undefined until a separate approved spec exists.

## no_action Boundary

`no_action` may appear only as a boundary statement in a future report.

```text
KernelReport no_action statement != ConstraintDecision(no_action)
```

It is not an allow/block decision, permission result, policy result,
recommendation, or execution command.

## Trace Boundary

`KernelTraceEntry` remains spec-level only.

It must not replace `LedgerEntry`, create a durable truth layer, expand SQLite,
become memory, or become world truth.

Any later mapping to `LedgerEntry` or `DecisionTrace` requires a separate
approved spec.

## Hard Exclusions

v0.5.0 must not introduce:

```text
Runtime code
SQLite schema change
CLI command
MemoryWrite
Reaction
Worker
LLM
Agent
RuntimeCell
Organ
GraphDB
Autonomy
Self-mutation
TransitionCandidate
ConstraintDecision
PolicyResult
allow/block
approval/rejection
```

## Repo Placement Decision

v0.5.0 should decide one of two paths:

| Path | Meaning |
| --- | --- |
| Stay as spec strand | Kernel remains in `GENUS_CORE/docs/kernel/` until runtime is justified. |
| Create later repo | A future `GENUS_KERNEL` repo starts only after vocabulary, gates, and handoff rules are accepted. |

Recommended short-term path: stay as a spec strand inside GENUS_CORE. The
handoff contract still depends on `BeliefStateSnapshot`.

## Files Likely Affected In v0.5.0

Docs-only v0.5.0 may add focused files under:

```text
docs/kernel/
docs/quality_gates/
docs/decisions/
docs/vocabulary/
docs/roadmap/
```

Indexes may be updated only if v0.5.0 is promoted from planning to accepted
baseline.

## Files That Must Stay Unchanged Until Runtime Approval

The following must stay unchanged for v0.5.0 planning:

```text
src/
tests/
SQLite schema
CLI behavior
README.md
docs/STATUS.md
pyproject.toml
```

## Suggested v0.5.0 Acceptance Gate

v0.5.0 can be accepted only if:

```text
pytest green
CLI smoke test green
package version remains 0.4.3 unless a separate release bump is accepted
SCHEMA_VERSION remains genus.foundation.v0.0.1
kernel docs stay under 260 lines each
kernel vocabulary forbids active decision/action semantics
kernel stop gate excludes runtime capability
GENUS_CORE foundation chain remains unchanged
```

## Final Recommendation

Proceed with v0.5.0 as a docs-only kernel governance baseline before any
KernelStateSnapshot runtime prototype.

Assessment:

```text
Plausibel: ja
Konsistent: ja
Vollstaendig: teilweise
Empfehlung: akzeptieren als naechsten Plan, nicht als Runtime
```
