# GENUS_CORE Decisions

Status: draft for foundation freeze

## Decision 0001 — Start smaller than Full Cognitive Physics

Decision:

`GENUS_CORE` starts with `v0.0.1 — Observation Truth Seed`, not full `v0.1 Cognitive Physics Seed`.

Reason:

The first stable core must prove that GENUS can distinguish Observation, Evidence, Ledger, Belief, and Report before introducing Physics, Map, Transition, Constraint, or Reaction.

Impact:

The following concepts are out of scope for v0.0.1:

```text
PhysicsMetric
CognitiveStateMap
TransitionCandidate
ConstraintDecision
ReactionExecution
MemoryWrite
LLM
Worker
Cell
Organ
```

## Decision 0002 — Observation is first true GENUS act

Decision:

`WorldEvent` is an occasion. `Observation` is the first true GENUS act.

Reason:

GENUS does not possess the world. GENUS observes world events.

Impact:

`WorldEvent` must never be treated as `Observation`.

## Decision 0003 — Ledger is lineage, not truth

Decision:

`LedgerEntry` proves sequence and lineage, not content truth.

Reason:

A ledger can prove that a record was created, but not that the content of that record is world-true.

Impact:

`EvidenceRecord.truth_status` is the truth-status marker, not `LedgerEntry`.

## Decision 0004 — Report has no decision power

Decision:

`ObservationReport` explains but never decides, approves, or executes.

Reason:

Reports must remain inspectable explanations and must not become hidden control surfaces.

Impact:

Report models must not contain `decision`, `action`, `approval`, `execute`, `reaction`, or `memory_write` fields.

## Decision 0005 — Function-first, responsibility-first

Decision:

GENUS_CORE is built from small responsibility-focused functions, not a monolith, manager, service god-object, or atomized helper files.

Reason:

The core must be testable, inspectable, and later refinable without creating a hidden orchestration monolith.

Impact:

Public functions must carry a GENUS responsibility. Helpers stay private.

## Decision 0006 - v0.0.1 builds no action path

Decision:

v0.0.1 baut nur Observation -> Evidence -> Belief und keine Handlung.

Reason:

The first implementation must freeze the epistemic foundation before any
decision, reaction, memory write, worker, runtime cell, organ, agent, LLM, or
physics capability exists.

Impact:

The CLI may compose the smoke path and print an explanation, but it must not
execute memory writes, reactions, decisions, transitions, or constraints.

## Decision 0007 - v0.0.2 is Foundation Hardening only

Decision:

v0.0.2 introduces no new GENUS capability and exists only to harden the v0.0.1
Observation Truth Seed.

Reason:

The epistemic foundation must be robust before Physics, Map, Transition,
Constraint, Reaction, Memory, Worker, Cell, Organ, Agent, or LLM concepts are
introduced.

Impact:

No product scope expansion is allowed in v0.0.2. The package version may move to
0.0.2, but the foundation schema version remains `genus.foundation.v0.0.1`.

## Decision 0008 - v0.0.3 centralizes minimal sentence types

Decision:

v0.0.3 centralizes and hardens the minimal internal GENUS sentence types without
expanding product scope.

Reason:

Before Physics, Map, Transition, Constraint, Reaction, Memory, Worker, Cell,
Organ, Agent, or LLM concepts exist, GENUS must prevent uncontrolled internal
vocabulary drift.

Impact:

Only WORLD_EVENT, OBSERVATION, EVIDENCE, LEDGER, BELIEF, and REPORT are valid
sentence types in the foundation language. The package version may move to
0.0.3, but `SCHEMA_VERSION` remains `genus.foundation.v0.0.1`.

## Decision 0009 - v0.0.4 hardens observation classification

Decision:

v0.0.4 hardens deterministic observation classification without introducing
Meaning, Intent, Parser, LLM, Physics, Transition, Constraint, Reaction, or
Memory concepts.

Reason:

Before GENUS can measure forces or propose transitions, it must safely classify
raw WorldEvents into limited and explicit Observations.

Impact:

The allowed observation types are limited to:

```text
memory_request_observed
memory_lookup_failure_observed
guard_block_observed
unknown_input_observed
ambiguous_input_observed
```

Observation classification remains side-effect free and must not create
EvidenceRecord, LedgerEntry, BeliefStateSnapshot, ObservationReport, memory
writes, reactions, decisions, transitions, or physics artifacts.

## Decision 0010 - v0.0.5 hardens the Evidence boundary

Decision:

v0.0.5 hardens Evidence as a provenance-marked record of Observation, not world
truth, belief, decision, memory, or action.

Reason:

Before GENUS can derive stronger belief states or introduce later cognitive
mechanics, the Observation -> EvidenceRecord boundary must prove that evidence
records only claim that an Observation was recorded with provenance and truth
status.

Impact:

Evidence payloads include `evidence_claim = "observation_recorded"`, source
observation type, source observation payload, confidence snapshot, and scope
snapshot. Evidence payloads must not contain belief, decision, action, reaction,
or memory-write fields. Provenance is limited to `user_input`, `system_event`,
`runtime_probe`, and `manual_entry`.

## Decision 0011 - v0.0.6 constrains Ledger to real lineage only

Decision:

v0.0.6 constrains Ledger to the single real current lineage event and does not
make LedgerEntry itself a provenance source or target.

Reason:

The current v0.0.x runtime only records that an Observation led to creation of
an EvidenceRecord. Allowing future Ledger event types or LedgerEntry-as-source
would make the language larger than the system and invite metadata chains that
do not yet have a real epistemic role.

Impact:

The only allowed Ledger event is `evidence_record_created`, with
`source_kind = observation` and `target_kind = evidence_record`. Ledger payloads
must not contain truth, belief, decision, action, reaction, memory, transition,
or physics fields.

## Decision 0012 - v0.0.7 hardens Belief derivation

Decision:

v0.0.7 hardens BeliefStateSnapshot as a scoped derivation from all supplied
observed EvidenceRecords, not truth, memory, decision, approval, constraint, or
action.

Reason:

Belief must remain a derived, inspectable internal state. It must not silently
drop EvidenceRecords, mix scopes, derive from rejected or derived evidence, or
become a hidden decision or memory-writing surface.

Impact:

Belief derivation accepts only EvidenceRecords with `truth_status = "observed"`,
`evidence_claim = "observation_recorded"`, a supported observation type, and an
`observation_scope`. All source EvidenceRecord IDs are preserved exactly and in
input order. Generic payload fields such as `evidence`, `truth_status`,
`decision`, `approval`, `constraint`, `action`, `reaction`, `memory_write`, and
`candidate` are forbidden in Belief payloads.

## Decision 0013 - v0.0.8 hardens Report as descriptive-only

Decision:

v0.0.8 hardens ObservationReport as a descriptive-only explanation of
BeliefStateSnapshot.

Reason:

The final artifact in the v0.0.x epistemic chain must not become a hidden
decision, approval, action, memory, reaction, truth, transition, constraint, or
physics surface.

Impact:

ObservationReport may explain Belief and preserve safe lineage references, but
it may not create new facts, decisions, approvals, actions, or side effects.

## Decision 0014 - v0.0.9 audits foundation freeze readiness

Decision:

v0.0.9 performs a Foundation Freeze Readiness Audit and introduces no new GENUS
capability.

Reason:

After hardening every boundary in the current foundation chain, GENUS_CORE needs
one audit-only release to verify release history, language boundaries, public
function boundaries, forbidden-object absence, and roadmap alignment before
v0.1.0 freezes the epistemic core.

Impact:

v0.0.9 may change documentation, release metadata, and audit tests. It must not
change domain function behavior, add public functions, add CLI commands, or
introduce Physics, Map, Transition, Constraint, Reaction, Memory, Worker, Cell,
Organ, Agent, LLM, RuntimeShape, GraphDB, or other v0.1+ concepts.

## Decision 0015 - v0.1.0 freezes the passive epistemic core

Decision:

v0.1.0 freezes the full passive epistemic core as the first stable GENUS_CORE
foundation baseline.

Reason:

The v0.0.x series has hardened every boundary in the current epistemic chain.
Before any Physics, Map, Transition, Constraint, Reaction, Memory, Worker, Cell,
Organ, Agent, LLM, RuntimeShape, or GraphDB concept is introduced, the
foundation must be marked stable and conserved.

Impact:

v0.1.0 may change release metadata, README/status documentation, release notes,
and freeze tests. It must not change domain function behavior, add public
functions, add CLI commands, change `SCHEMA_VERSION`, or expand product scope.

## Decision 0016 - v0.1.1 defines Pre-Physics requirements only

Decision:

v0.1.1 defines requirements for a future passive Physics layer without
implementing Physics.

Reason:

Physics is the first planned layer that can introduce measurements such as
pressure, inhibition, stability, cost, or potential. Those concepts are closer
to prioritization, transition reasoning, and eventual action than the frozen
foundation. GENUS_CORE must define their boundaries before any metric code
exists.

Impact:

v0.1.1 may change release metadata, requirements documentation, roadmap/status
documentation, vocabulary entries marked as planned, and tests proving Physics
remains absent. It must not add `PhysicsMetric`, metric records, metric
functions, sentence types, CLI commands, domain behavior, or product capability.

## Decision 0017 - v0.1.2 defines passive metric vocabulary only

Decision:

v0.1.2 defines planned passive metric vocabulary without implementing metrics.

Reason:

Metric terms such as pressure, inhibition, stability, cost, and potential can
drift into priority, recommendation, transition, permission, activation, or
action semantics if they are introduced casually. GENUS_CORE must name these
terms precisely before any metric implementation exists.

Impact:

v0.1.2 may change release metadata, vocabulary documentation, roadmap/status
documentation, and tests proving metric implementation remains absent. Metric
vocabulary may exist only in docs and tests. No metric constants, enums,
registries, allowed lists, classes, modules, files, imports, public exports, or
public function references may be added to `src/genus_core`.

## Decision 0018 - v0.1.3 defines passive metric acceptance criteria only

Decision:

v0.1.3 defines acceptance criteria for future passive metrics without
implementing metrics.

Reason:

Before any passive Physics implementation exists, GENUS_CORE must define what
future metrics may read, what they may output at a high level, which concepts
are first candidates, which concepts remain excluded, and which effects are
forbidden. This prevents metrics from becoming hidden priority, transition,
permission, action, or truth surfaces.

Impact:

v0.1.3 may change release metadata, acceptance criteria documentation,
roadmap/status documentation, and tests proving metric implementation remains
absent. It must not add metric output schemas, metric models, metric records,
metric functions, metric persistence, sentence types, CLI commands, domain
behavior, or product capability.

## Decision 0019 - v0.1.4 adds a minimal CI release integrity gate

Decision:

v0.1.4 adds a minimal GitHub Actions CI gate without changing GENUS_CORE
product behavior.

Reason:

The frozen foundation and pre-Physics documentation line are now valuable
enough that every push and pull request to `main` should automatically prove
pytest and the CLI smoke path still pass. This protects the existing local
quality gates before any future metric output shape or passive Physics work.

Impact:

v0.1.4 may change release metadata, documentation, tests, and GitHub Actions
workflow configuration. It must not add coverage, linting, formatting, matrix
builds, caching, release automation, deployment, metric output shape, metric
models, metric functions, sentence types, CLI commands, domain behavior, or
product capability.

## Decision 0020 - v0.1.5 defines passive metric output shape only

Decision:

v0.1.5 defines the planned-not-active output shape for future passive metrics
without implementing metrics.

Reason:

Before passive Physics can exist, GENUS_CORE must define how future metric
results may describe state without becoming scores, priorities,
recommendations, permissions, transitions, decisions, actions, or memory-write
surfaces. `level = none` must also stay distinct from insufficient input.

Impact:

v0.1.5 may change release metadata, output-shape documentation, roadmap/status
documentation, and tests proving metric implementation remains absent. It must
not add metric classes, metric records, metric functions, metric persistence,
sentence types, CLI commands, domain behavior, or product capability.

## Decision 0021 - v0.1.6 audits passive metric safety before implementation

Decision:

v0.1.6 performs a passive metric safety audit before the first passive Physics
implementation.

Reason:

Requirements, vocabulary, acceptance criteria, output shape, and CI now exist,
but GENUS_CORE must still prove that these documents agree on non-agentic
metric boundaries. The audit also closes the status/level consistency gap so
`insufficient_input` and `not_applicable` cannot later pair with non-`none`
levels.

Impact:

v0.1.6 may change release metadata, safety audit documentation, roadmap/status
documentation, and tests proving metric implementation remains absent. It must
not add metric classes, metric records, metric functions, metric persistence,
sentence types, CLI commands, domain behavior, or product capability.

## Decision 0022 - v0.1.7 requires concrete Ledger targets

Decision:

Ledger entries for the current foundation lineage require a concrete
`target_kind` and `target_id`.

Reason:

The only active Ledger event records that an Observation led to creation of an
EvidenceRecord. A LedgerEntry without an EvidenceRecord target is incomplete
lineage, not a valid current foundation event.

Impact:

`append_ledger_entry` requires `target_kind` and `target_id`.
`LedgerEntry` rejects missing or blank targets. New SQLite `ledger_entries`
tables require non-empty `target_id`. No migration is added for existing local
SQLite files.

## Decision 0023 - v0.1.8 finalizes CI release integrity

Decision:

The GitHub Actions CLI smoke command uses a YAML block scalar.

Reason:

The smoke text contains `das: larumipsum`. In a YAML plain scalar, the colon can
be parsed as YAML syntax before any job is created, producing a failed workflow
with zero jobs. A block scalar preserves the command text as the CLI argument.

Impact:

The CI workflow remains minimal: install, pytest, CLI smoke. v0.1.8 records the
green post-fix baseline and preserves the v0.1.7 tag as historical rather than
rewriting it.

## Decision 0024 - v0.1.9 uses observation-only memory request names

Decision:

Ephemeral Belief and Report payloads use `observed_memory_request` and
`observed_memory_content` instead of `pending_memory_request` and
`candidate_content`.

Reason:

`pending` can imply an execution queue, and `candidate` can imply a selected
transition or action surface. The passive foundation must only say what was
observed and derived, not what should be executed, stored, or chosen.

Impact:

v0.1.9 changes active ephemeral payload names, report wording, documentation,
and tests. It does not change `SCHEMA_VERSION`, add compatibility aliases, add
persistence tables, introduce passive Physics, expand the CLI, or add product
capability.

## Decision 0025 - v0.1.10 anchors the GENUS charter and safety boundary

Decision:

v0.1.10 adds `GENUS_CHARTER.md` and `SAFETY_BOUNDARIES.md` as active repository
governance documents.

Reason:

The passive foundation is technically bounded, but the larger GENUS vision must
be discoverable and test-protected before v0.2.0 begins. Future builds need a
single charter for purpose and a single safety boundary for admissible power.

Impact:

v0.1.10 changes documentation, release metadata, and governance tests only. It
does not change `SCHEMA_VERSION`, public foundation functions, CLI commands,
SQLite schema, persistence behavior, passive Physics implementation, memory,
reaction, transition, worker, LLM, or product capability.

## Decision 0026 - v0.2.0 activates passive Physics narrowly

Decision:

v0.2.0 introduces `PassiveMetricSnapshot`, `PassiveMetricReport`,
`build_passive_metric_snapshot`, and `create_passive_metric_report` in the
separate `genus_core.passive_physics` namespace.

Reason:

The passive foundation, metric requirements, output shape, safety audit, and
GENUS charter are accepted. GENUS_CORE can now add a first descriptive Physics
layer downstream of `BeliefStateSnapshot` without introducing action,
transition, decision, memory, worker execution, LLM calls, or persistence.

Impact:

The first metric names are only `pressure`, `inhibition`, and `stability`.
`cost` and `potential` remain excluded. The public foundation functions,
sentence types, CLI commands, SQLite schema, and `SCHEMA_VERSION` remain
unchanged.

## Decision 0027 - v0.2.1 clarifies passive Physics boundary language

Decision:

v0.2.1 treats `PassiveMetricSnapshot`, `PassiveMetricReport`,
`build_passive_metric_snapshot`, and `create_passive_metric_report` as the only
allowed passive v0.2.x Physics artifacts. Older pre-Physics gates now refer to
forbidden active metric implementation artifacts rather than all metric
implementation artifacts.

Reason:

v0.2.0 intentionally activated a narrow passive metric description layer. The
historical v0.1.x gates still protected against premature active Physics, but
some wording could be read as conflicting with the accepted passive v0.2.0
artifacts.

Impact:

v0.2.1 changes documentation, release metadata, and tests only. It does not add
metric names, dynamic Physics, simulation, scoring, priority, recommendation,
permission, decision, transition, constraint, reaction, memory write, CLI
commands, SQLite persistence, worker execution, LLM calls, GraphDB, RuntimeShape,
or schema changes.

## Decision 0028 - v0.3.0 adds passive transition preview

Decision:

v0.3.0 introduces `PassiveTransitionPreview`, `PassiveTransitionReport`,
`build_passive_transition_preview`, and `create_passive_transition_report` in
the separate `genus_core.passive_transition` namespace.

Reason:

Passive Physics can describe visible tension, but GENUS still must not create
transition candidates, decisions, reactions, or memory writes. A passive preview
layer can describe that a later governed question may exist without selecting,
recommending, permitting, blocking, or executing anything.

Impact:

`transition` may appear in passive v0.3.0 artifact names, module names,
function names, docs, and tests only when clearly qualified as passive preview
or forbidden active capability. It must not appear as a standalone output or
payload field. The runtime `possible_future_question` field must remain
question-like and must not contain `should`, `must`, `allow`, `block`,
`execute`, `write`, `approve`, or `recommend`.

v0.3.0 does not change public foundation functions, sentence types, CLI
commands, SQLite schema, durable truth layer, or `SCHEMA_VERSION`.

## Decision 0029 - v0.3.1 audits passive transition report language

Decision:

v0.3.1 adds no capability. It hardens `PassiveTransitionReport.summary` against
active wording and neutralizes the memory-tension `possible_future_question`.

Reason:

v0.3.0 correctly keeps transition preview passive, but summary text deserves
the same explicit descriptive-only guard used for earlier report layers. The
memory-tension question should say that content raises a governed memory
question, not that content belongs in governed memory.

Impact:

Public foundation functions, passive transition artifacts, preview types,
sentence types, CLI commands, SQLite schema, durable truth layer, and
`SCHEMA_VERSION` remain unchanged. v0.3.1 does not add TransitionCandidate,
ConstraintDecision, Reaction, MemoryWrite, worker execution, LLM calls, GraphDB,
RuntimeShape, or product capability.

## Decision 0030 - v0.4.0 is planned as passive boundary relevance, not evaluation

Decision:

v0.4.0 planning uses `Passive Boundary Relevance` language instead of
`Passive Boundary Evaluation`.

Reason:

GENUS_CORE must not evaluate boundaries yet. The next planned step should only
define how a later passive boundary relevance description may look. `Evaluation`
can imply permission evaluation, policy evaluation, approval, rejection,
allow/block, or decision, so the planned vocabulary stays on descriptive
relevance mapping.

Impact:

This decision is spec-only. It adds documentation and tests only. It does not
add runtime source packages, classes, functions, exports, CLI commands, SQLite
tables, sentence types, a package version bump, or a `SCHEMA_VERSION` change.

## Decision 0031 - v0.3.2 governs build structure

Decision:

v0.3.2 treats code, tests, docs, specs, decisions, and quality gates as
governed artifacts with line-count guardrails and explicit historical
longfile exceptions.

Reason:

GENUS must remain bounded not only at runtime, but also while being built.
Oversized docs and tests make boundaries harder to audit and invite accidental
scope drift.

Impact:

This adds build rules, project-structure documentation, and structure tests
only. It does not add runtime capability, CLI commands, SQLite tables, sentence
types, schema changes, workers, LLMs, reactions, memory writes, transition
candidates, constraint decisions, GraphDB, or RuntimeShape.

## Decision 0032 - v0.3.3 modularizes quality gates first

Decision:

v0.3.3 modularizes `QUALITY_GATES.md` by version series before modularizing
`DECISIONS.md` or other historical longfiles.

Reason:

`QUALITY_GATES.md` was the largest governance document and the clearest
candidate for the v0.3.2 build-structure guardrails. Moving gate blocks into
focused files reduces navigation cost without changing runtime behavior or
rewriting historical acceptance criteria.

Impact:

`QUALITY_GATES.md` becomes an index. Historical gate content moves under
`docs/quality_gates/`. `DECISIONS.md` remains a capped historical longfile for
now. No runtime source package, class, function, CLI command, SQLite table,
sentence type, schema version, worker, LLM, reaction, memory write, transition
candidate, constraint decision, GraphDB, or RuntimeShape is introduced.

## Decision 0033 - v0.3.4 aligns artifact contracts

Decision:

v0.3.4 adds `ARTIFACT_CONTRACTS.md` as the shared contract document for active
GENUS artifacts.

Reason:

GENUS artifacts should be similar where compatibility matters and different
where their role requires it. ID, source lineage, evidence lineage,
snapshot/preview/report roles, durable/ephemeral boundaries, and report limits
need one visible contract before v0.4.0 planning adds another passive layer.

Impact:

This is a governance and test release only. It does not change runtime
behavior, package schema, SQLite tables, CLI commands, sentence types,
persistence, workers, LLMs, reactions, memory writes, transition candidates,
constraint decisions, GraphDB, or RuntimeShape.
