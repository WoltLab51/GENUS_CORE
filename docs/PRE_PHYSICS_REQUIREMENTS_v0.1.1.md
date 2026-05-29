# GENUS_CORE Pre-Physics Requirements v0.1.1

Status: historical requirements; activated narrowly in v0.2.0 as PassiveMetricSnapshot/PassiveMetricReport

Activated narrowly in v0.2.0 as PassiveMetricSnapshot/PassiveMetricReport.

## Purpose

v0.1.1 defines the safety and language requirements for a future passive
Physics layer.

It does not implement `PhysicsMetric`, metrics, metric records, metric
functions, new sentence types, new CLI commands, or product behavior.

## Passive Measure Definition

A passive measure reads from or derives from existing foundation artifacts.

A passive measure:

```text
does not decide
does not prioritize
does not execute
does not react
does not write memory
does not transition
does not constrain
does not create truth
```

A passive measure may only help explain an already-derived internal state. It
must not choose a next state, approve a candidate, rank actions, or cause side
effects.

## Allowed Read Surface

Future passive Physics may read from:

```text
BeliefStateSnapshot
source_evidence_ids_json
safe descriptive payload fields already present in the frozen foundation
```

Future passive Physics must not read from hidden runtime state, external LLMs,
agents, workers, mutable memory stores, transition engines, constraint engines,
or reaction systems.

## Position In The Future Chain

Future passive Physics must remain:

```text
downstream of the frozen foundation
upstream of any future Map, Transition, or Constraint layer
```

It must not bypass Observation, Evidence, Ledger, Belief, or Report.

## Planned Passive Concepts

Likely first passive concepts:

```text
pressure
inhibition
stability
```

Higher-risk planned concepts:

```text
cost
potential
```

`cost` and `potential` are closer to prioritization and transition reasoning.
They must not be implemented without a later accepted release plan.

## Non-Scope

v0.1.1 does not introduce:

```text
PhysicsMetric
Pressure
Potential
Cost
Inhibition
Stability
CognitiveStateMap
TransitionCandidate
ConstraintDecision
Reaction
ReactionExecution
MemoryWrite
MemoryObject
Worker
RuntimeCell
Organ
Agent
Character
LLM
Autonomy
Mutation
Evolution
GraphDB
RuntimeShape
```

## Acceptance Requirements

```text
Package version is 0.1.1
SCHEMA_VERSION remains genus.foundation.v0.0.1
No Physics class, module, file, import, public export, or public function reference exists
Foundation sentence types remain unchanged
Public foundation functions remain unchanged
CLI exposes only observe
All existing foundation tests remain green
```
