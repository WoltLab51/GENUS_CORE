# GENUS_CORE Roadmap - Pre-Physics
Status: active for v0.4.2 Passive Boundary Relevance Boundary Audit
Moved from `docs/ROADMAP_STABLE_CORE.md`.

### v0.1.1 - Pre-Physics Requirements

Defines requirements for future passive Physics without implementing metrics,
metric records, metric functions, or new sentence types.

Likely first passive concepts are `pressure`, `inhibition`, and `stability`.
Higher-risk planned concepts are `cost` and `potential`.

### v0.1.2 - Passive Metric Vocabulary

Defines planned-not-active passive metric vocabulary while keeping metric
implementation inactive.

First passive candidates:

```text
pressure
inhibition
stability
```

Higher-risk planned terms:

```text
cost
potential
```

### v0.1.3 - Passive Metric Acceptance Criteria

Defines accepted inputs, output category, forbidden effects, and quality gates
for a future passive Physics seed without implementing metrics.

First future implementation candidates remain:

```text
pressure
inhibition
stability
```

Still excluded from first implementation:

```text
cost
potential
```

The exact metric output shape is deferred to v0.1.5.

### v0.1.4 - Release Integrity & CI Gate

Adds a minimal GitHub Actions gate for the frozen foundation and pre-Physics
documentation line.

CI runs only:

```text
install
pytest
CLI smoke
```

It does not add coverage, linting, formatting, matrix builds, caching, release
automation, deployment, metric output shape, or product behavior.

### v0.1.5 - Passive Metric Output Shape

Defines the exact planned-not-active passive metric output shape without
implementing metrics.

The first output metric names are limited to:

```text
pressure
inhibition
stability
```

The output shape separates `level` from `assessment_status` so `none` does not
mean insufficient input.

`cost` and `potential` remain excluded from the first output shape.

### v0.1.6 - Passive Metric Safety Audit

Audits requirements, vocabulary, acceptance criteria, output shape, CI,
forbidden-object absence, and non-agentic metric boundaries before the first
passive Physics implementation.

The audit requires:

```text
assessment_status = insufficient_input -> level = none
assessment_status = not_applicable -> level = none
assessment_status = assessed -> level = none | low | medium | high
```

### v0.1.7 - Foundation Cleanup and Integrity Repair

Cleans up the v0.1.6 baseline before passive Physics begins.

It tightens Ledger lineage target requirements, clarifies that `worker` remains
only a passive observation scope label, records the current GitHub Actions
signal, and keeps `SCHEMA_VERSION` at `genus.foundation.v0.0.1`.

### v0.1.8 - Release Integrity Finalization

Finalizes the green pre-v0.2.0 baseline.

It records the concrete Ledger target invariant and the GitHub Actions YAML
smoke fix while preserving the v0.1.7 tag as historical.

### v0.1.9 - Boundary Naming Cleanup

Sharpens passive foundation terminology before passive Physics begins.

It renames ephemeral Belief and Report memory-request payload fields from
`pending_memory_request` and `candidate_content` to `observed_memory_request`
and `observed_memory_content`, clarifies package/schema/capability boundaries,
and hardens the CI workflow test for the YAML block scalar CLI smoke command.

### v0.1.10 - GENUS Charter and Safety Boundary

Anchors the GENUS vision as repository governance before passive Physics begins.

It adds the GENUS charter, operational safety boundaries, and tests proving the
core build directives are present. It adds no runtime capability.
