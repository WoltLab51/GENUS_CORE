# GENUS_CORE Quality Gates

Status: draft for foundation freeze

## 1. Purpose

Quality Gates define the conditions that must be met before a GENUS_CORE phase can be accepted.

GENUS must not grow by enthusiasm alone.

Every phase must pass documentation, test, architecture, and safety checks.

## 2. Universal Quality Gate

Every GENUS_CORE phase must pass:

```text
pytest green
CLI smoke test green
all new terms documented
all new invariants tested
STATUS.md updated
DECISIONS.md updated when architecture changed
SAFETY_BOUNDARIES.md updated when power changed
no forbidden artifacts introduced
```

## 3. v0.0.1 Quality Gate

`v0.0.1 — Observation Truth Seed` is accepted only if:

```text
WorldEvent exists.
Observation exists.
EvidenceRecord exists.
LedgerEntry exists.
BeliefStateSnapshot exists.
ObservationReport exists.

WorldEvent is not treated as Observation.
Observation is not treated as Evidence.
Evidence is not treated as Belief.
Belief is not treated as World Truth.
Ledger is not treated as Truth.
Report is not treated as Decision.
Report is not treated as Action.
```

## 4. v0.0.1 Technical Gate

```text
SQLite persists EvidenceRecord.
SQLite persists LedgerEntry.
Ledger has UNIQUE(chain_id, step).
BeliefStateSnapshot requires Evidence IDs.
ObservationReport has no decision field.
No ReactionExecution class exists.
No MemoryWrite class exists.
No PhysicsMetric class exists.
No TransitionCandidate class exists.
No ConstraintDecision class exists.
```

## 5. v0.0.1 Test Gate

Required tests:

```text
test_world_event_is_not_observation
test_observation_is_not_evidence
test_evidence_is_not_belief
test_ledger_is_append_only
test_belief_requires_evidence
test_report_has_no_decision_power
test_no_reaction_execution_exists
test_no_memory_write_exists
test_language_rejects_unknown_sentence_type
```

## 6. v0.0.1 Smoke Gate

The following command or equivalent must pass:

```text
genus-core observe "merk dir das: larumipsum"
```

Expected output must include:

```text
Observation created
EvidenceRecord created
LedgerEntry appended
BeliefStateSnapshot created
ObservationReport created
No action possible
```

Expected output must not include:

```text
Memory written
Reaction executed
Transition allowed
Constraint decided
```

## 7. Stop Gate

Stop development if any of these occur:

```text
Observation directly creates Belief.
Report contains action fields.
Ledger is used as content truth.
BeliefStateSnapshot has no Evidence references.
A forbidden artifact appears in v0.0.1.
CLI contains hidden business logic.
A new term appears without vocabulary entry.
```

## 8. Architecture Review Result Format

Each phase review must output:

```text
Philosophy-Fit: green/yellow/red
Governance-Fit: green/yellow/red
Function-Granularity-Fit: green/yellow/red
Overengineering-Risk: low/medium/high
Documentation-Drift-Risk: low/medium/high
Decision: accept/harden/stop
```

## 9. v0.0.2 Foundation Hardening Gate

`v0.0.2 - Foundation Hardening` is accepted only if:

```text
pytest green
CLI smoke test green
forbidden objects absent
ledger append-only verified
SQLite invariants verified
model invariants verified
package version is 0.0.2
SCHEMA_VERSION remains genus.foundation.v0.0.1
documentation updated
no product scope expansion
```

## 10. v0.0.2 Technical Gate

The following must be tested:

```text
evidence_records persists EvidenceRecord.
ledger_entries persists LedgerEntry.
ledger_entries has UNIQUE(chain_id, step).
ledger_entries has CHECK(step >= 1).
truth_status only allows observed, derived, rejected.
schema_version is persisted and required for persisted v0.0.1 objects.
Observation confidence only allows low, medium, high.
Observation scope only allows input, memory, system, worker.
BeliefStateSnapshot requires Evidence IDs.
ObservationReport rejects decision/action/execute/approval/reaction/memory_write.
Unknown GENUS language sentence types are rejected.
Repeated CLI smoke runs do not collide in the ledger.
```

## 11. v0.0.2 Stop Gate

Stop development if any of these occur:

```text
A new product capability appears.
A forbidden v0.1+ artifact appears as class, module, file, import, or public export.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
CLI grows beyond thin composition.
Domain functions gain hidden persistence side effects.
Ledger update/delete APIs appear.
```

## 12. v0.0.3 Minimal Language Hardening Gate

`v0.0.3 - Minimal Language Hardening` is accepted only if:

```text
pytest green
CLI smoke test green
allowed sentence types accepted
unknown sentence types rejected
forbidden future sentence types rejected
package version is 0.0.3
SCHEMA_VERSION remains genus.foundation.v0.0.1
forbidden objects absent
documentation updated
no product scope expansion
```

## 13. v0.0.3 Technical Gate

The following must be tested:

```text
ALLOWED_SENTENCE_TYPES contains exactly WORLD_EVENT, OBSERVATION, EVIDENCE, LEDGER, BELIEF, REPORT.
validate_sentence_type returns allowed sentence types unchanged.
validate_sentence_type rejects unknown sentence types.
validate_sentence_type rejects ACTION, REACTION, EXECUTION, MEMORY_WRITE, PHYSICS, MAP, TRANSITION, CONSTRAINT, AGENT, WORKER, CELL, ORGAN.
Package version is 0.0.3.
SCHEMA_VERSION remains genus.foundation.v0.0.1.
Existing v0.0.2 hardening tests remain green.
```

## 14. v0.0.3 Stop Gate

Stop development if any of these occur:

```text
A parser, DSL, registry, dispatcher, adapter hierarchy, or grammar engine appears.
A new CLI command appears.
A new product capability appears.
A forbidden v0.1+ artifact appears as class, module, file, import, or public export.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
```

## 15. v0.0.4 Observation Classification Hardening Gate

`v0.0.4 - Observation Classification Hardening` is accepted only if:

```text
pytest green
CLI smoke test green
allowed observation classifications tested
unsupported events become unknown_input_observed
incomplete memory requests become ambiguous_input_observed
observation classification has no side effects
forbidden objects absent
package version is 0.0.4
SCHEMA_VERSION remains genus.foundation.v0.0.1
documentation updated
no product scope expansion
```

## 16. v0.0.4 Technical Gate

The following must be tested:

```text
user_text "merk dir das: larumipsum" becomes memory_request_observed.
candidate_content is preserved.
user_text "merk dir das:" becomes ambiguous_input_observed.
empty user_text becomes unknown_input_observed.
memory_lookup_failed becomes memory_lookup_failure_observed.
guard_blocked_transition becomes guard_block_observed.
unsupported event_type becomes unknown_input_observed.
unsupported event_type preserves original_event_type.
observe_event returns Observation only.
observe_event does not create EvidenceRecord, LedgerEntry, BeliefStateSnapshot, ObservationReport, MemoryWrite, Reaction, Decision, Transition, or Physics artifacts.
Package version is 0.0.4.
SCHEMA_VERSION remains genus.foundation.v0.0.1.
```

## 17. v0.0.4 Stop Gate

Stop development if any of these occur:

```text
MeaningCandidate, Intent, parser, LLM adapter, registry, manager, service class, or orchestrator appears.
A new CLI command appears.
A new product capability appears.
A forbidden v0.1+ artifact appears as class, module, file, import, or public export.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
observe_event creates Evidence, Ledger, Belief, Report, memory writes, reactions, decisions, transitions, or physics artifacts.
```

## 18. v0.0.5 Evidence Boundary Hardening Gate

`v0.0.5 - Evidence Boundary Hardening` is accepted only if:

```text
pytest green
CLI smoke test green
provenance constrained
evidence claim present
belief/action fields absent from evidence payload
side-effect-free evidence creation
forbidden objects absent
package version is 0.0.5
SCHEMA_VERSION remains genus.foundation.v0.0.1
documentation updated
no product scope expansion
```

## 19. v0.0.5 Technical Gate

The following must be tested:

```text
create_evidence_record accepts only Observation.
EvidenceRecord rejects invalid provenance.
SQLite rejects invalid evidence provenance for newly initialized stores.
Evidence payload contains evidence_claim = observation_recorded.
Evidence payload contains source observation type, payload, confidence, and scope.
Evidence payload does not contain pending_memory_request, decision, action, reaction, or memory_write.
Evidence remains not Belief and not world truth.
Evidence creation does not create LedgerEntry, BeliefStateSnapshot, ObservationReport, MemoryWrite, Reaction, Decision, Transition, or Physics artifacts.
Package version is 0.0.5.
SCHEMA_VERSION remains genus.foundation.v0.0.1.
```

## 20. v0.0.5 Stop Gate

Stop development if any of these occur:

```text
Evidence claims world truth.
Evidence contains belief, decision, action, reaction, or memory-write fields.
create_evidence_record writes SQLite, appends Ledger, builds Belief, creates Report, or creates any action-capable object.
A new CLI command appears.
A new product capability appears.
A forbidden v0.1+ artifact appears as class, module, file, import, or public export.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
```

## 21. v0.0.6 Ledger Minimal Lineage Hardening Gate

`v0.0.6 - Ledger Minimal Lineage Hardening` is accepted only if:

```text
pytest green
CLI smoke test green
real-flow-only ledger event and kinds verified
ledger append-only verified
forbidden ledger payload fields rejected
forbidden objects absent
package version is 0.0.6
SCHEMA_VERSION remains genus.foundation.v0.0.1
documentation updated
no product scope expansion
```

## 22. v0.0.6 Technical Gate

The following must be tested:

```text
Ledger event_type only allows evidence_record_created.
Ledger source_kind only allows observation.
Ledger target_kind only allows evidence_record.
ledger_entry is rejected as source_kind and target_kind.
Duplicate chain_id/step is rejected.
step = 0 is rejected.
Ledger payload rejects truth, world_truth, belief, pending_memory_request, decision, action, reaction, transition, physics, memory_write.
append_ledger_entry creates only LedgerEntry and has no SQLite side effects.
SQLite rejects invalid ledger event_type, source_kind, and target_kind for newly initialized stores.
Package version is 0.0.6.
SCHEMA_VERSION remains genus.foundation.v0.0.1.
```

## 23. v0.0.6 Stop Gate

Stop development if any of these occur:

```text
LedgerEntry becomes an allowed source_kind or target_kind.
Future ledger event types appear before there is a real flow for them.
Ledger payload contains truth, belief, decision, action, reaction, memory, transition, or physics fields.
Ledger update/delete APIs appear.
A new CLI command appears.
A new product capability appears.
A forbidden v0.1+ artifact appears as class, module, file, import, or public export.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
```

## 24. v0.0.7 Belief Derivation Hardening Gate

`v0.0.7 - Belief Derivation Hardening` is accepted only if:

```text
pytest green
CLI smoke test green
Evidence-only belief input verified
only observed EvidenceRecords accepted
unsupported observation types rejected
missing observation_scope rejected
mixed scopes rejected
all source EvidenceRecord IDs preserved exactly and in order
unsafe Belief payload fields absent
forbidden objects absent
package version is 0.0.7
SCHEMA_VERSION remains genus.foundation.v0.0.1
documentation updated
no product scope expansion
```

## 25. v0.0.7 Technical Gate

The following must be tested:

```text
build_belief_state_snapshot rejects non-EvidenceRecord input.
Empty evidence list is rejected.
truth_status = derived and truth_status = rejected are rejected.
Missing or invalid evidence_claim is rejected.
Missing observation_scope is rejected.
Unsupported observed_observation_type is rejected.
Mixed or incompatible scopes are rejected.
All supplied EvidenceRecord IDs are preserved exactly and in input order.
No EvidenceRecord is silently dropped.
pending_memory_request is true only when a source type is memory_request_observed.
ambiguous, unknown, guard, and memory lookup failure evidence derive pending_memory_request = false.
Belief payload does not contain truth, world_truth, truth_status, generic evidence, decision, approval, action, reaction, constraint, transition, physics, memory_write, execute, or generic candidate.
Package version is 0.0.7.
SCHEMA_VERSION remains genus.foundation.v0.0.1.
```

## 26. v0.0.7 Stop Gate

Stop development if any of these occur:

```text
Belief derives from rejected or derived EvidenceRecords.
Belief silently drops any supplied EvidenceRecord.
Belief mixes scopes without rejection.
Belief payload contains generic evidence, truth, decision, approval, constraint, action, reaction, transition, physics, memory_write, execute, or generic candidate fields.
Belief creation writes SQLite, appends Ledger, creates Report, writes memory, reacts, decides, transitions, or measures physics.
A new CLI command appears.
A new product capability appears.
A forbidden v0.1+ artifact appears as class, module, file, import, or public export.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
```

## 27. v0.0.8 Report Boundary Hardening Gate

`v0.0.8 - Report Boundary Hardening` is accepted only if:

```text
pytest green
CLI smoke test green
create_observation_report accepts only BeliefStateSnapshot
report has source_state_id
report payload forbidden fields rejected
report summary does not imply action taken, approval, execution, memory written, or reaction created
report creates no new artifacts
forbidden objects absent
package version is 0.0.8
SCHEMA_VERSION remains genus.foundation.v0.0.1
documentation updated
no product scope expansion
```

## 28. v0.0.8 Technical Gate

The following must be tested:

```text
create_observation_report rejects non-BeliefStateSnapshot input.
ObservationReport rejects empty or invalid source_state_id.
ObservationReport payload rejects decision, action, execute, approval, reaction, memory_write, memory, memory_object, constraint, transition, candidate, physics, metric, truth, truth_status, world_truth, evidence_claim, policy, allow, block, approved, and rejected_by_policy.
Report payload does not contain truth, truth_status, world_truth, or evidence_claim.
Report summary remains descriptive.
Report creation creates only ObservationReport.
Package version is 0.0.8.
SCHEMA_VERSION remains genus.foundation.v0.0.1.
```

## 29. v0.0.8 Stop Gate

Stop development if any of these occur:

```text
ObservationReport becomes a decision, approval, action, memory, reaction, truth, transition, constraint, or physics surface.
Report payload contains action, approval, execution, memory, truth, policy, transition, constraint, or physics fields.
Report creation writes SQLite, appends Ledger, creates Evidence, creates Belief, writes memory, reacts, decides, transitions, or measures physics.
A new CLI command appears.
A new product capability appears.
A forbidden v0.1+ artifact appears as class, module, file, import, or public export.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
```

## 30. v0.0.9 Foundation Freeze Readiness Audit Gate

`v0.0.9 - Foundation Freeze Readiness Audit` is accepted only if:

```text
pytest green
CLI smoke test green
foundation audit document present
roadmap corrected to actual v0.0.x release history
allowed sentence types remain exact
public foundation functions remain exact
public foundation functions do not reference forbidden v0.1+ artifacts
forbidden objects absent
package version is 0.0.9
SCHEMA_VERSION remains genus.foundation.v0.0.1
documentation updated
no product scope expansion
```

## 31. v0.0.9 Technical Gate

The following must be tested:

```text
Package version is 0.0.9.
SCHEMA_VERSION remains genus.foundation.v0.0.1.
ALLOWED_SENTENCE_TYPES contains exactly WORLD_EVENT, OBSERVATION, EVIDENCE, LEDGER, BELIEF, REPORT.
Public foundation functions are exactly observe_event, create_evidence_record, append_ledger_entry, build_belief_state_snapshot, create_observation_report.
The public foundation functions compose only WorldEvent -> Observation -> EvidenceRecord -> LedgerEntry -> BeliefStateSnapshot -> ObservationReport.
Public foundation function modules do not import, return, instantiate, or reference forbidden v0.1+ artifacts.
CLI exposes only the existing observe command.
Existing v0.0.8 tests remain green.
```

## 32. v0.0.9 Stop Gate

Stop development if any of these occur:

```text
Domain function behavior changes without a failing audit invariant.
A public domain function is added, removed, or repurposed.
A new CLI command appears.
A new product capability appears.
A forbidden v0.1+ artifact appears as class, module, file, import, public export, or public function reference.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
Roadmap reintroduces Physics before v0.1.0 foundation freeze.
```

## 33. v0.1.0 Full Epistemic Core Freeze Gate

`v0.1.0 - Full Epistemic Core Freeze` is accepted only if:

```text
pytest green
CLI smoke test green
package version is 0.1.0
SCHEMA_VERSION remains genus.foundation.v0.0.1
foundation chain unchanged
public foundation functions unchanged
allowed sentence types unchanged
README states the stable foundation boundary
STATUS has one clear v0.1.0 freeze acceptance state
release notes present
forbidden objects absent
no product scope expansion
```

## 34. v0.1.0 Technical Gate

The following must be tested:

```text
Package version is 0.1.0.
SCHEMA_VERSION remains genus.foundation.v0.0.1.
ALLOWED_SENTENCE_TYPES contains exactly WORLD_EVENT, OBSERVATION, EVIDENCE, LEDGER, BELIEF, REPORT.
Public foundation functions are exactly observe_event, create_evidence_record, append_ledger_entry, build_belief_state_snapshot, create_observation_report.
The active chain remains WorldEvent -> Observation -> EvidenceRecord -> LedgerEntry -> BeliefStateSnapshot -> ObservationReport.
CLI exposes only the existing observe command.
Forbidden future artifacts remain absent from modules, classes, files, imports, public exports, and public function references.
Existing v0.0.9 tests remain green.
```

## 35. v0.1.0 Stop Gate

Stop development if any of these occur:

```text
Domain function behavior changes.
A public domain function is added, removed, or repurposed.
A new CLI command appears.
A new product capability appears.
A forbidden future artifact appears as class, module, file, import, public export, or public function reference.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
README, STATUS, release notes, or roadmap describe Physics as active in v0.1.0.
```

## 36. v0.1.1 Pre-Physics Requirements Gate

`v0.1.1 - Pre-Physics Requirements` is accepted only if:

```text
pytest green
CLI smoke test green
package version is 0.1.1
SCHEMA_VERSION remains genus.foundation.v0.0.1
PRE_PHYSICS_REQUIREMENTS_v0.1.1.md exists
passive measure boundaries documented
Physics artifacts remain absent from src/genus_core
allowed sentence types unchanged
public foundation functions unchanged
CLI exposes only observe
documentation updated
no product scope expansion
```

## 37. v0.1.1 Technical Gate

The following must be tested:

```text
Package version is 0.1.1.
SCHEMA_VERSION remains genus.foundation.v0.0.1.
Pre-Physics requirements explicitly state that passive measures do not decide, prioritize, execute, react, write memory, transition, constrain, or create truth.
PhysicsMetric, Pressure, Potential, Cost, Inhibition, and Stability remain absent from src/genus_core as classes, modules, files, imports, public exports, and public function references.
ALLOWED_SENTENCE_TYPES remains exactly WORLD_EVENT, OBSERVATION, EVIDENCE, LEDGER, BELIEF, REPORT.
Public foundation functions remain exactly observe_event, create_evidence_record, append_ledger_entry, build_belief_state_snapshot, create_observation_report.
CLI exposes only observe.
Existing v0.1.0 tests remain green.
```

## 38. v0.1.1 Stop Gate

Stop development if any of these occur:

```text
PhysicsMetric or any metric model appears.
Pressure, Potential, Cost, Inhibition, or Stability appears as active code.
A metric function, metric record, or metric sentence type appears.
A new CLI command appears.
A new product capability appears.
Domain function behavior changes.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
Docs describe Physics as active in v0.1.1.
```

## 39. v0.1.2 Passive Metric Vocabulary Gate

`v0.1.2 - Passive Metric Vocabulary` is accepted only if:

```text
pytest green
CLI smoke test green
package version is 0.1.2
SCHEMA_VERSION remains genus.foundation.v0.0.1
PASSIVE_METRIC_VOCABULARY_v0.1.2.md exists
metric terms are planned-not-active
pressure, inhibition, and stability are first passive candidates
cost and potential are higher-risk and not first implementation
metric vocabulary is not metric implementation
forbidden active metric implementation artifacts remain absent from src/genus_core
allowed sentence types unchanged
public foundation functions unchanged
CLI exposes only observe
documentation updated
no product scope expansion
```

## 40. v0.1.2 Technical Gate

The following must be tested:

```text
Package version is 0.1.2.
SCHEMA_VERSION remains genus.foundation.v0.0.1.
PASSIVE_METRIC_VOCABULARY_v0.1.2.md exists.
pressure, inhibition, stability, cost, and potential are defined as planned-not-active.
pressure, inhibition, and stability are marked first passive candidates.
cost and potential are marked higher-risk and not first implementation.
Metric terms are explicitly not decisions, priorities, transitions, actions, permissions, recommendations, activations, or memory writes.
Implementation scan targets class names, module names, file stems, imports, public exports, and public function references in src/genus_core.
Metric terms may appear in docs and tests without failing the implementation scan.
PhysicsMetric, Pressure, Potential, Cost, Inhibition, Stability, calculate_pressure_metric, and related implementation names remain absent from src/genus_core.
ALLOWED_SENTENCE_TYPES remains exactly WORLD_EVENT, OBSERVATION, EVIDENCE, LEDGER, BELIEF, REPORT.
Public foundation functions remain exactly observe_event, create_evidence_record, append_ledger_entry, build_belief_state_snapshot, create_observation_report.
CLI exposes only observe.
Existing v0.1.1 tests remain green.
```

## 41. v0.1.2 Stop Gate

Stop development if any of these occur:

```text
Metric vocabulary is placed in src/genus_core as constants, enums, registries, allowed lists, classes, modules, imports, public exports, or public function references.
PhysicsMetric or any metric model appears.
A metric function, metric record, metric persistence, or metric sentence type appears.
A new CLI command appears.
A new product capability appears.
Domain function behavior changes.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
Docs describe passive metrics as active in v0.1.2.
```

## 42. v0.1.3 Passive Metric Acceptance Criteria Gate

`v0.1.3 - Passive Metric Acceptance Criteria` is accepted only if:

```text
pytest green
CLI smoke test green
package version is 0.1.3
SCHEMA_VERSION remains genus.foundation.v0.0.1
PASSIVE_METRIC_ACCEPTANCE_CRITERIA_v0.1.3.md exists
pressure, inhibition, and stability are first future implementation candidates
cost and potential remain excluded from first implementation
allowed read surface is limited
forbidden effects are documented
exact metric output shape is deferred to v0.1.5
forbidden active metric implementation artifacts remain absent from src/genus_core
allowed sentence types unchanged
public foundation functions unchanged
CLI exposes only observe
documentation updated
no product scope expansion
```

## 43. v0.1.3 Technical Gate

The following must be tested:

```text
Package version is 0.1.3.
SCHEMA_VERSION remains genus.foundation.v0.0.1.
PASSIVE_METRIC_ACCEPTANCE_CRITERIA_v0.1.3.md exists.
pressure, inhibition, and stability are accepted future first candidates.
cost and potential remain excluded from first implementation.
Allowed read surface is limited to BeliefStateSnapshot, source_evidence_ids_json, and safe descriptive foundation payload fields.
Forbidden effects include Ledger writes, Evidence creation, Belief mutation, Report triggering, TransitionCandidate, ConstraintDecision, Reaction, MemoryWrite, prioritization, recommendation, permission, activation, action, and truth creation.
Exact metric output shape is explicitly deferred to v0.1.5.
Forbidden active metric implementation artifacts remain absent from src/genus_core as class names, module names, file stems, imports, public exports, and public function references.
ALLOWED_SENTENCE_TYPES remains exactly WORLD_EVENT, OBSERVATION, EVIDENCE, LEDGER, BELIEF, REPORT.
Public foundation functions remain exactly observe_event, create_evidence_record, append_ledger_entry, build_belief_state_snapshot, create_observation_report.
CLI exposes only observe.
Existing v0.1.2 tests remain green.
```

## 44. v0.1.3 Stop Gate

Stop development if any of these occur:

```text
Metric output shape is implemented or frozen.
PhysicsMetric or any metric model appears.
A metric function, metric record, metric persistence, or metric sentence type appears.
A new CLI command appears.
A new product capability appears.
Domain function behavior changes.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
Docs describe passive metrics as active in v0.1.3.
cost or potential are admitted into first implementation.
```

## 45. v0.1.4 Release Integrity & CI Gate

`v0.1.4 - Release Integrity & CI Gate` is accepted only if:

```text
pytest green
CLI smoke test green
package version is 0.1.4
SCHEMA_VERSION remains genus.foundation.v0.0.1
GitHub Actions workflow exists
CI uses ubuntu-latest
CI uses actions/checkout and actions/setup-python
CI uses Python 3.12
CI runs only install, pytest, and CLI smoke
CI sets GENUS_CORE_TRUTH_DB under runner temp
documentation updated
no product scope expansion
```

## 46. v0.1.4 Technical Gate

The following must be tested:

```text
Package version is 0.1.4.
SCHEMA_VERSION remains genus.foundation.v0.0.1.
.github/workflows/ci.yml exists.
Workflow uses ubuntu-latest.
Workflow uses actions/checkout and actions/setup-python.
Workflow sets Python version to 3.12.
Workflow runs python -m pip install -e ".[dev]".
Workflow runs python -m pytest.
Workflow runs python -m genus_core.cli observe "merk dir das: larumipsum".
Workflow sets GENUS_CORE_TRUTH_DB to a path under runner temp.
Workflow does not add coverage, linting, formatting, matrix builds, caching, release automation, or deployment.
Existing v0.1.3 tests remain green.
```

## 47. v0.1.4 Stop Gate

Stop development if any of these occur:

```text
Domain function behavior changes.
A public domain function is added, removed, or repurposed.
A new CLI command appears.
A new product capability appears.
Metric output shape is implemented or frozen.
PhysicsMetric or any metric model appears.
A metric function, metric record, metric persistence, or metric sentence type appears.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
CI adds coverage, linting, formatting, matrix builds, caching, release automation, or deployment.
Docs describe passive metrics as active in v0.1.4.
```

## 48. v0.1.5 Passive Metric Output Shape Gate

`v0.1.5 - Passive Metric Output Shape` is accepted only if:

```text
pytest green
CLI smoke test green
package version is 0.1.5
SCHEMA_VERSION remains genus.foundation.v0.0.1
PASSIVE_METRIC_OUTPUT_SHAPE_v0.1.5.md exists
metric_name values are limited to pressure, inhibition, stability
cost and potential remain excluded from first output shape
level values are limited to none, low, medium, high
assessment_status values are limited to assessed, insufficient_input, not_applicable
none does not mean insufficient input
explanation is descriptive-only
source_evidence_ids_json is lineage only
forbidden active metric output implementation artifacts remain absent from src/genus_core
documentation updated
no product scope expansion
```

## 49. v0.1.5 Technical Gate

The following must be tested:

```text
Package version is 0.1.5.
SCHEMA_VERSION remains genus.foundation.v0.0.1.
PASSIVE_METRIC_OUTPUT_SHAPE_v0.1.5.md exists.
Allowed metric_name values are exactly pressure, inhibition, stability.
cost and potential remain excluded from first output shape.
Allowed level values are exactly none, low, medium, high.
Allowed assessment_status values are exactly assessed, insufficient_input, not_applicable.
level = none means assessed with no visible metric expression and must not mean insufficient input.
Output shape requires explanation, source_state_id, and source_evidence_ids_json.
explanation must not recommend, permit, approve, rank, prioritize, trigger, execute, transition, react, or write memory.
explanation must not introduce facts not derivable from source_state_id and source_evidence_ids_json.
source_evidence_ids_json must not imply scoring, weighting, ranking, priority, or confidence.
Forbidden output fields include score, priority, rank, recommendation, permission, decision, approval, action, execute, candidate, transition, constraint, reaction, memory_write, and truth.
Forbidden active metric output implementation artifacts remain absent from src/genus_core as class names, module names, file stems, imports, public exports, and public function references.
ALLOWED_SENTENCE_TYPES remains exactly WORLD_EVENT, OBSERVATION, EVIDENCE, LEDGER, BELIEF, REPORT.
Public foundation functions remain exactly observe_event, create_evidence_record, append_ledger_entry, build_belief_state_snapshot, create_observation_report.
CLI exposes only observe.
Existing v0.1.4 tests remain green.
```

## 50. v0.1.5 Stop Gate

Stop development if any of these occur:

```text
Metric output shape is implemented in src/genus_core.
PhysicsMetric or any metric model appears.
A metric function, metric record, metric persistence, or metric sentence type appears.
score, priority, rank, recommendation, permission, decision, approval, action, execute, candidate, transition, constraint, reaction, memory_write, or truth appear as allowed metric output fields.
cost or potential are admitted into first output shape.
A new CLI command appears.
A new product capability appears.
Domain function behavior changes.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
Docs describe passive metrics as active in v0.1.5.
```

## 51. v0.1.6 Passive Metric Safety Audit Gate

`v0.1.6 - Passive Metric Safety Audit` is accepted only if:

```text
pytest green
CLI smoke test green
package version is 0.1.6
SCHEMA_VERSION remains genus.foundation.v0.0.1
PASSIVE_METRIC_SAFETY_AUDIT_v0.1.6.md exists
Pre-Physics Requirements exist
Passive Metric Vocabulary exists
Passive Metric Acceptance Criteria exist
Passive Metric Output Shape exists
CI Gate exists
status/level consistency rules are documented
cost and potential remain excluded
forbidden active metric implementation artifacts remain absent from src/genus_core
documentation updated
no product scope expansion
```

## 52. v0.1.6 Technical Gate

The following must be tested:

```text
Package version is 0.1.6.
SCHEMA_VERSION remains genus.foundation.v0.0.1.
PASSIVE_METRIC_SAFETY_AUDIT_v0.1.6.md exists.
PRE_PHYSICS_REQUIREMENTS_v0.1.1.md exists.
PASSIVE_METRIC_VOCABULARY_v0.1.2.md exists.
PASSIVE_METRIC_ACCEPTANCE_CRITERIA_v0.1.3.md exists.
PASSIVE_METRIC_OUTPUT_SHAPE_v0.1.5.md exists.
.github/workflows/ci.yml exists.
assessment_status = insufficient_input requires level = none.
assessment_status = not_applicable requires level = none.
assessment_status = assessed may use level = none | low | medium | high.
cost and potential remain excluded from first implementation and first output shape.
Forbidden active metric implementation artifacts remain absent from src/genus_core as class names, module names, file stems, imports, public exports, and public function references.
ALLOWED_SENTENCE_TYPES remains exactly WORLD_EVENT, OBSERVATION, EVIDENCE, LEDGER, BELIEF, REPORT.
Public foundation functions remain exactly observe_event, create_evidence_record, append_ledger_entry, build_belief_state_snapshot, create_observation_report.
CLI exposes only observe.
CI workflow remains minimal: install, pytest, CLI smoke only.
Existing v0.1.5 tests remain green.
```

## 53. v0.1.6 Stop Gate

Stop development if any of these occur:

```text
Metric safety rules are implemented in src/genus_core.
PhysicsMetric or any metric model appears.
A metric function, metric record, metric persistence, or metric sentence type appears.
cost or potential are admitted into first implementation or first output shape.
A new CLI command appears.
A new product capability appears.
Domain function behavior changes.
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
Docs describe passive metrics as active in v0.1.6.
CI expands beyond install, pytest, and CLI smoke.
```

## 54. v0.1.7 Foundation Cleanup and Integrity Repair Gate

`v0.1.7 - Foundation Cleanup and Integrity Repair` is accepted only if:

```text
pytest green
CLI smoke test green
package version is 0.1.7
SCHEMA_VERSION remains genus.foundation.v0.0.1
LedgerEntry requires target_kind and target_id
New SQLite ledger_entries tables require non-empty target_id
worker remains a passive scope label, not a Worker capability
forbidden active metric implementation artifacts remain absent from src/genus_core
allowed sentence types remain unchanged
public foundation functions remain unchanged
CLI exposes only observe
no product scope expansion
```

## 55. v0.1.7 Stop Gate

Stop development if any of these occur:

```text
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
A new CLI command appears.
A new product capability appears.
Metric safety rules are implemented in src/genus_core.
PhysicsMetric or any metric model appears.
Worker becomes an object, runtime, execution surface, or capability.
Ledger entries can be created without a target EvidenceRecord id.
```

## 56. v0.1.8 Release Integrity Finalization Gate

`v0.1.8 - Release Integrity Finalization` is accepted only if:

```text
pytest green
CLI smoke test green
GitHub Actions green on the v0.1.8 commit
package version is 0.1.8
SCHEMA_VERSION remains genus.foundation.v0.0.1
DECISIONS records the Ledger target invariant
DECISIONS records the CI YAML smoke fix
v0.1.7 tag remains historical and is not rewritten
allowed sentence types remain unchanged
public foundation functions remain unchanged
CLI exposes only observe
no product scope expansion
```

## 57. v0.1.8 Stop Gate

Stop development if any of these occur:

```text
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
A new CLI command appears.
A new product capability appears.
Metric safety rules are implemented in src/genus_core.
PhysicsMetric or any metric model appears.
The v0.1.7 tag is rewritten or moved.
GitHub Actions fails on the v0.1.8 commit.
```

## 58. v0.1.9 Boundary Naming Cleanup Gate

`v0.1.9 - Boundary Naming Cleanup` is accepted only if:

```text
pytest green
CLI smoke test green
package version is 0.1.9
SCHEMA_VERSION remains genus.foundation.v0.0.1
Belief payload uses observed_memory_request and observed_memory_content
Report payload uses observed_memory_request and observed_memory_content
Active Belief and Report payloads do not use pending_memory_request or candidate_content
Report summary uses passive foundation boundary wording
CI workflow test verifies the CLI smoke command is inside a YAML block scalar
allowed sentence types remain unchanged
public foundation functions remain unchanged
CLI exposes only observe
no product scope expansion
```

## 59. v0.1.9 Stop Gate

Stop development if any of these occur:

```text
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
A new CLI command appears.
A new product capability appears.
Metric safety rules are implemented in src/genus_core.
PhysicsMetric or any metric model appears.
pending_memory_request or candidate_content appears in active Belief or Report payloads.
Report wording implies a queue, execution, memory write, decision, reaction, transition, or physics.
The CI smoke command can move outside the YAML block scalar without a failing test.
```

## 60. v0.1.10 GENUS Charter and Safety Boundary Gate

`v0.1.10 - GENUS Charter and Safety Boundary` is accepted only if:

```text
pytest green
CLI smoke test green
package version is 0.1.10
SCHEMA_VERSION remains genus.foundation.v0.0.1
GENUS_CHARTER.md exists
SAFETY_BOUNDARIES.md exists
BUILD_RULES.md references GENUS_CHARTER.md and SAFETY_BOUNDARIES.md
GENUS Charter contains LLM proposes. GENUS governs.
GENUS Charter contains Do not make GENUS powerful before making it bounded.
Safety Boundaries forbid active MemoryWrite, Reaction, TransitionCandidate, ConstraintDecision, Worker, LLM, Agent, GraphDB, and RuntimeShape
allowed sentence types remain unchanged
public foundation functions remain unchanged
CLI exposes only observe
no product scope expansion
```

## 61. v0.1.10 Stop Gate

Stop development if any of these occur:

```text
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
A new CLI command appears.
A new product capability appears.
Passive Physics is implemented.
Metric models, metric records, metric functions, metric persistence, or metric sentence types appear.
MemoryWrite, Reaction, TransitionCandidate, ConstraintDecision, Worker, LLM, Agent, GraphDB, or RuntimeShape appears as active runtime capability.
GENUS_CHARTER.md is missing.
SAFETY_BOUNDARIES.md is missing.
BUILD_RULES.md no longer references both governance documents.
```

## 62. v0.2.0 Passive Physics Seed Gate

`v0.2.0 - Passive Physics Seed` is accepted only if:

```text
pytest green
CLI smoke test green
package version is 0.2.0
SCHEMA_VERSION remains genus.foundation.v0.0.1
PassiveMetricSnapshot exists only in genus_core.passive_physics
PassiveMetricReport exists only in genus_core.passive_physics
build_passive_metric_snapshot accepts only BeliefStateSnapshot
create_passive_metric_report accepts only PassiveMetricSnapshot
metric_name values are exactly pressure, inhibition, stability
cost and potential are rejected
level values are exactly none, low, medium, high
assessment_status values are exactly assessed, insufficient_input, not_applicable
assessment_status = insufficient_input requires level = none
assessment_status = not_applicable requires level = none
PassiveMetricReport contains no decision, action, reaction, transition, constraint, memory_write, or truth fields
Passive metric outputs are not persisted
allowed sentence types remain unchanged
public foundation functions remain unchanged
CLI exposes only observe
CI remains install, pytest, CLI smoke
```

## 63. v0.2.0 Stop Gate

Stop development if any of these occur:

```text
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
A new CLI command appears.
A new SQLite table appears.
A new sentence type appears.
Metric outputs contain score, priority, rank, recommendation, permission, decision, approval, action, execute, candidate, transition, constraint, reaction, memory_write, or truth.
cost or potential become active first implementation metric names.
PhysicsMetric, PassiveMetric, Pressure, Inhibition, Stability, Cost, or Potential appears as a class, module, file, or public object.
TransitionCandidate, ConstraintDecision, Reaction, MemoryWrite, Worker, LLM, GraphDB, or RuntimeShape appears as active capability.
```

## 64. v0.2.1 Passive Physics Boundary Cleanup Gate

`v0.2.1 - Passive Physics Boundary Cleanup` is accepted only if:

```text
pytest green
CLI smoke test green
package version is 0.2.1
SCHEMA_VERSION remains genus.foundation.v0.0.1
ObservationReport is documented as foundation explanation and not physics measurement
PassiveMetricReport is documented as passive metric description only
v0.2.x passive Physics is documented as narrow passive metric description, not dynamic physics or simulation
PassiveMetricSnapshot, PassiveMetricReport, build_passive_metric_snapshot, and create_passive_metric_report are allowed only in genus_core.passive_physics
forbidden active metric implementation artifacts remain absent from src/genus_core
cost and potential remain excluded
durable truth layer remains EvidenceRecord and LedgerEntry only
allowed sentence types remain unchanged
public foundation functions remain unchanged
CLI exposes only observe
CI remains install, pytest, CLI smoke
```

## 65. v0.2.1 Stop Gate

Stop development if any of these occur:

```text
SCHEMA_VERSION changes from genus.foundation.v0.0.1.
A new CLI command appears.
A new SQLite table appears.
A new sentence type appears.
A new metric name appears beyond pressure, inhibition, or stability.
cost or potential become active first implementation metric names.
Metric outputs contain score, priority, rank, recommendation, permission, decision, approval, action, execute, candidate, transition, constraint, reaction, memory_write, or truth.
PhysicsMetric, PassiveMetric, Pressure, Inhibition, Stability, Cost, Potential, MetricRecord, MetricOutput, PassiveMetricOutput, MetricOutputShape, or calculate_*_metric appears as an active object, module, file, import, public export, or public function.
TransitionCandidate, ConstraintDecision, Reaction, MemoryWrite, Worker, LLM, RuntimeCell, Organ, Agent, GraphDB, or RuntimeShape appears as active capability.
```
