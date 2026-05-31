# GENUS_CORE Status
Current baseline: `v0.4.1 - Passive Boundary Relevance Preview Seed`

Status: accepted narrow Passive Boundary Relevance runtime baseline.

## Released baselines

```text
v0.0.1 Observation Truth Seed
Tag: genus-core-v0.0.1-observation-truth-seed
Commit: 3cbb2d4416d4011bf53a9af9ead63932cf0be408

v0.0.2 Foundation Hardening
Tag: genus-core-v0.0.2-foundation-hardening
Commit: 44c4dfac04e83455d489d4961ac656f7884e48d8

v0.0.3 Minimal Language Hardening
Tag: genus-core-v0.0.3-minimal-language-hardening
Commit: ebed5c31bfbbfb112cefcace6c684d7dbee0a107

v0.0.4 Observation Classification Hardening
Tag: genus-core-v0.0.4-observation-classification-hardening
Commit: 139ee05e1c6f5a02c430fdce3352fd931f80052f

v0.0.5 Evidence Boundary Hardening
Tag: genus-core-v0.0.5-evidence-boundary-hardening
Commit: 1cde6bccaed6c27290284762a5f05b9dd7a1aaad

v0.0.6 Ledger Minimal Lineage Hardening
Tag: genus-core-v0.0.6-ledger-lineage-hardening
Commit: 2407d153fa91e86796cd9f85cf5fed334f603b74

v0.0.7 Belief Derivation Hardening
Tag: genus-core-v0.0.7-belief-derivation-hardening
Commit: e0ea167167f3cb010b60b497631762b6501b5731

v0.0.8 Report Boundary Hardening
Tag: genus-core-v0.0.8-report-boundary-hardening
Commit: 4f738f10bf221f2b215f765effab80871b9838bb

v0.0.9 Foundation Freeze Readiness Audit
Tag: genus-core-v0.0.9-foundation-freeze-readiness
Commit: adc53da7ad645a034bfa07ade2f4a3a8cac1b4ac

v0.1.0 Full Epistemic Core Freeze
Tag: genus-core-v0.1.0-full-epistemic-core-freeze
Commit: 57aa74f9e841befa521c9cff23c996e50ec36d47

v0.1.1 Pre-Physics Requirements
Tag: genus-core-v0.1.1-pre-physics-requirements
Commit: f32aa894f34efbdc4fb007a709f4961a6f4e9731

v0.1.2 Passive Metric Vocabulary
Tag: genus-core-v0.1.2-passive-metric-vocabulary
Commit: 96d9176e3020cea8c20a2fd8e7d835292fb60160

v0.1.3 Passive Metric Acceptance Criteria
Tag: genus-core-v0.1.3-passive-metric-acceptance-criteria
Commit: 38e0aa8569dce2d7463ff0db972cf6c77f2c7f18

v0.1.4 Release Integrity & CI Gate
Tag: genus-core-v0.1.4-release-integrity-ci-gate
Commit: 43720b9005b134a96a0876981274b42b0ee39f42

v0.1.5 Passive Metric Output Shape
Tag: genus-core-v0.1.5-passive-metric-output-shape
Commit: 28d0b66c74ffbdd2cbf8ab893aa24815314f31d7

v0.1.6 Passive Metric Safety Audit
Tag: genus-core-v0.1.6-passive-metric-safety-audit
Commit: f0bcd1b23212daf1435939576ccc2287663fe35f

v0.1.7 Foundation Cleanup and Integrity Repair
Tag: genus-core-v0.1.7-foundation-cleanup-integrity-repair
Commit: f288fd8a78e5fa400c76a909ab07a5233104ce0d

v0.1.8 Release Integrity Finalization
Tag: genus-core-v0.1.8-release-integrity-finalization
Commit: e16b89d5e7ed81f8b4305ceee0bcaf2b3c235443

v0.1.9 Boundary Naming Cleanup
Tag: genus-core-v0.1.9-boundary-naming-cleanup
Commit: 7054a9dd31a864c382f7da4962c7d8f284ccd167

v0.1.10 GENUS Charter and Safety Boundary
Tag: genus-core-v0.1.10-genus-charter-safety-boundary
Commit: 6744752de25105a299d1e36952e966e4bb27bb7d

v0.2.0 Passive Physics Seed
Tag: genus-core-v0.2.0-passive-physics-seed
Commit: ea0e8a78876f689643bfc335e817bfe49729506a

v0.2.1 Passive Physics Boundary Cleanup
Tag: genus-core-v0.2.1-passive-physics-boundary-cleanup
Commit: 2caeeabb60f9ce34470519448b4c814634bbd8a9

v0.3.0 Passive Transition Preview Seed
Tag: genus-core-v0.3.0-passive-transition-preview-seed
Commit: 2c2bfe1ba8d44662126ba13e9f073475aa96ebe0

v0.3.1 Passive Transition Boundary Audit
Tag: genus-core-v0.3.1-passive-transition-boundary-audit
Commit: aa829e0f36edf715ab0ab41f96720edfaabf2e5b

v0.4.0 Passive Boundary Relevance Spec
Tag: genus-core-v0.4.0-passive-boundary-relevance-spec
Commit: d51baee9b7e88532853a810dd3185cdb561e418c
```

## Frozen foundation chain

The only active epistemic chain remains:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> ObservationReport
```

## Current implementation state

`GENUS_CORE v0.4.1` is Passive Boundary Relevance Preview Seed.

It adds the narrow `genus_core.passive_boundary_relevance` runtime namespace
for `PassiveBoundaryRelevancePreview` and `PassiveBoundaryRelevanceReport`.
The layer is descriptive, side-effect free, ephemeral, and downstream of
`BeliefStateSnapshot`, `PassiveMetricSnapshot`, and `PassiveTransitionPreview`.

The allowed passive v0.3.x artifacts remain
`PassiveTransitionPreview`, `PassiveTransitionReport`,
`build_passive_transition_preview`, and `create_passive_transition_report` in
the separate `genus_core.passive_transition` namespace. The allowed v0.4.1
artifacts are `PassiveBoundaryRelevancePreview`,
`PassiveBoundaryRelevanceReport`, `build_passive_boundary_relevance_preview`,
and `create_passive_boundary_relevance_report` in the separate
`genus_core.passive_boundary_relevance` namespace. It does not add
TransitionCandidate, ConstraintDecision, PolicyResult, permission, allow/block,
Reaction, MemoryWrite, metric or boundary persistence, sentence types, CLI
commands, workers, LLM calls, GraphDB, or RuntimeShape.

Package version is `0.4.1`; `SCHEMA_VERSION` remains `genus.foundation.v0.0.1`.

## Explicitly not active

```text
PhysicsMetric
Potential
Cost
MetricRecord
PassiveMetric
MetricOutput
PassiveMetricOutput
MetricOutputShape
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

`pressure`, `inhibition`, and `stability` are active only as passive
`metric_name` string values inside `PassiveMetricSnapshot` outputs.

`transition` is active only as part of passive v0.3.x artifact, module,
function, docs, and test names when clearly qualified as passive preview. It is
not an output or payload field and does not imply an active transition.

## Acceptance Pointers

Current acceptance gates live in `docs/quality_gates/v0.4.md`.

The short status document must not duplicate the quality gate ledger.
