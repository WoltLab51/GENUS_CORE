# GENUS_CORE Vocabulary - Passive Layers
Status: active for v0.4.0 Passive Boundary Relevance Spec
Vocabulary blocks moved verbatim from `docs/VOCABULARY.md`.

## PassiveMetricSnapshot

An ephemeral v0.2.x passive Physics artifact derived from a BeliefStateSnapshot.

It contains descriptive metric outputs for `pressure`, `inhibition`, and
`stability`.

It is not a PhysicsMetric, score, priority, recommendation, permission,
decision, transition, reaction, memory write, truth claim, or persistence
record.

Allowed in: v0.2.x

## PassiveMetricReport

An ephemeral v0.2.x descriptive report explaining a PassiveMetricSnapshot.

It contains `no_action_possible = true` and safe lineage references.

It is not an ObservationReport, decision, approval, action, recommendation,
priority, permission, reaction, transition, constraint, memory write, dynamic
physics simulation, or truth claim.

Allowed in: v0.2.x

## PassiveTransitionPreview

An ephemeral v0.3.0 passive preview artifact derived from a BeliefStateSnapshot
and a PassiveMetricSnapshot.

It describes visible passive tension as a possible later governed question. It
contains `no_action_possible = true` and `no_decision_possible = true`.

It is not TransitionCandidate, ConstraintDecision, Reaction, MemoryWrite,
recommendation, permission, priority, target state, selected transition,
proposed transition, action, truth claim, or persistence record.

Allowed in: v0.3.0

## PassiveTransitionReport

An ephemeral v0.3.0 descriptive report explaining a PassiveTransitionPreview.

It is not ConstraintDecision, approval, permission, recommendation, priority,
Reaction, MemoryWrite, selected transition, proposed transition, target state,
action, or truth claim.

Allowed in: v0.3.0

## passive measure

A planned future concept for describing a derived state without decision,
priority, execution, reaction, memory write, transition, constraint, or truth
creation.

It is planned-not-active in v0.1.2.

## pressure

A planned future passive metric concept for describing accumulated demand or
tension in an internal state.

It is planned-not-active in v0.1.2 and is not a decision, priority, action,
permission, recommendation, activation, transition, constraint, truth claim, or
memory write.

## inhibition

A planned future passive metric concept for describing resistance or blocking
signals in an internal state.

It is planned-not-active in v0.1.2 and is not ConstraintDecision, action,
reaction, permission, recommendation, activation, transition, policy, truth
claim, or memory write.

## stability

A planned future passive metric concept for describing whether an internal state
appears steady or fragile.

It is planned-not-active in v0.1.2 and is not approval, decision, action,
permission, recommendation, activation, truth, or memory write.

## cost

A higher-risk planned future passive metric concept.

It is planned-not-active in v0.1.2. Because cost can drift toward prioritization
and decision matrices, it requires later acceptance before implementation. It is
not a scheduler, optimizer, budget allocator, permission, recommendation,
activation, action, truth claim, or memory write.

## potential

A higher-risk planned future passive metric concept.

It is planned-not-active in v0.1.2. Because potential can drift toward
transition selection, it requires later acceptance before implementation. It is
not TransitionCandidate, recommendation, permission, execution plan, activation,
decision, action, truth claim, or memory write.
