# GENUS_CORE Roadmap to Stable Core

Status: draft

## Stable Core Goal

GENUS_CORE becomes stable when it can safely and auditably perform the following chain:

```text
WorldEvent
→ Observation
→ EvidenceRecord
→ LedgerEntry
→ BeliefStateSnapshot
→ PhysicsMetric
→ CognitiveStateMap
→ TransitionCandidate
→ ConstraintDecision
→ ReactionPreview
→ Controlled Minimal Reaction
→ MemoryWrite
→ MaturationObservation
```

But it must not start with the full chain.

It must grow through quality-gated phases.

## Phase 0 — Foundation Freeze

Deliver documentation only.

```text
FOUNDATION_SPEC_v0.0.1.md
GENUS_LANGUAGE_SPEC_v0.0.1.md
QUALITY_GATES.md
BUILD_RULES.md
VOCABULARY.md
DECISIONS.md
STATUS.md
```

Gate:

```text
All primitives defined.
All non-confusions defined.
All forbidden artifacts listed.
No implementation before acceptance.
```

## Phase 1 — v0.0.1 Observation Truth Seed

Scope:

```text
WorldEvent
Observation
EvidenceRecord
LedgerEntry
BeliefStateSnapshot
ObservationReport
```

Goal:

```text
Observation ≠ Evidence ≠ Belief
Ledger ≠ Truth
Report ≠ Action
```

## Phase 2 — v0.0.2 Foundation Hardening

Scope:

```text
SQLite constraints
append-only ledger tests
invalid enum rejection
store-level invariants
```

Goal:

```text
Foundational invariants are technically enforced.
```

## Phase 3 — v0.0.3 Minimal Language Layer

Scope:

```text
WORLD_EVENT
OBSERVATION
EVIDENCE
LEDGER
BELIEF
REPORT
```

Goal:

```text
Internal GENUS language is versioned and controlled.
```

## Phase 4 — v0.0.4 Physics Seed

Scope:

```text
belief_confidence
observation_pressure
inhibition_hint
```

Goal:

```text
Belief can generate metrics without generating action.
```

## Phase 5 — v0.0.5 Cognitive Map Seed

Scope:

```text
CognitiveStateMap
```

Goal:

```text
Map is projection, not truth.
```

## Phase 6 — v0.0.6 Transition Seed

Scope:

```text
TransitionCandidate
```

Goal:

```text
Possibility is represented without action.
```

## Phase 7 — v0.0.7 Constraint Seed

Scope:

```text
ConstraintDecision = no_action only
```

Goal:

```text
Candidates are constrained before any reaction exists.
```

## Phase 8 — v0.1.0 Full Passive Cognitive Physics

Scope:

```text
WorldEvent
→ Observation
→ EvidenceRecord
→ LedgerEntry
→ BeliefStateSnapshot
→ PhysicsMetric
→ CognitiveStateMap
→ TransitionCandidate
→ ConstraintDecision
→ RegulationReport
```

Goal:

```text
Full passive cognition, still no action.
```

## Phase 9 — v0.2.0 Reaction Preview

Scope:

```text
ReactionPreview
```

Goal:

```text
GENUS can describe possible reactions but not execute them.
```

## Phase 10 — v0.3.0 Controlled Minimal Reaction

Scope:

```text
ReactionExecution minimal
explicit allow boundary
ledger entry required
```

Goal:

```text
First controlled effect, still tiny.
```

## Phase 11 — v0.4.0 Memory Write

Scope:

```text
MemoryObject
MemoryWrite
MemoryStore
```

Goal:

```text
Memory requires Evidence, Constraint Allow, ReactionExecution, and Ledger.
```

## Phase 12 — v0.5.0 Maturation Seed

Scope:

```text
ReactionOutcome
PatternObservation
CapabilityNeed
ImprovementProposal
```

Goal:

```text
GENUS observes patterns and proposes improvements without activation.
```

## Phase 13 — v0.6.0 Function Contract

Scope:

```text
FunctionContract
InputSchema
OutputSchema
EffectDeclaration
```

Goal:

```text
Key functions gain explicit contracts.
```

## Phase 14 — v0.7.0 Cell Candidate

Scope:

```text
CellCandidate
CellIdentity
CellContract
CellTrace
```

Goal:

```text
A function can become a candidate for a governed capability.
```

## Phase 15 — v1.0.0 Stable Core

Scope:

```text
Observation/Evidence/Belief
Physics
Map
Transition
Constraint
ReactionPreview
Controlled Minimal Reaction
MemoryWrite
Maturation Proposal
FunctionContract
CellCandidate
```

Goal:

```text
GENUS has a stable governed core for future organs, workers, LLM adapters, and runtime forms.
```

Still forbidden at v1.0:

```text
free agents
runtime cells
organ runtime
autonomous worker execution
LLM-dispatched internal commands
self-mutation
GraphDB as truth
trading automation
federation
```
