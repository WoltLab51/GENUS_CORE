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
