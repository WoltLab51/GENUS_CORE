# GENUS_CORE Roadmap - Governance
Status: active for v0.4.0 Passive Boundary Relevance Spec
Moved from `docs/ROADMAP_STABLE_CORE.md`.

### v0.3.2 - Build Structure Guardrails

Adds project-structure governance without runtime capability.

It treats code, tests, docs, specs, decisions, and quality gates as governed
artifacts and freezes historical longfiles behind explicit ceilings, reasons,
and planned split/review notes.

### v0.3.3 - Quality Gates Modularization

Modularizes `QUALITY_GATES.md` without runtime capability.

It turns `QUALITY_GATES.md` into an index and moves historical gate content
into `docs/quality_gates/` by version series.

### v0.3.4 - Artifact Contract Alignment

Documents shared artifact contracts without runtime capability.

It defines ID, source-lineage, evidence-lineage, snapshot/preview/report,
durable/ephemeral, report-boundary, compatibility, and watched-wording rules in
`ARTIFACT_CONTRACTS.md`.

### v0.3.5 - Decisions Modularization

Modularizes `DECISIONS.md` without runtime capability.

It keeps decisions as active GENUS build laws while moving decision blocks into
`docs/decisions/` by version series.

### v0.3.6 - Vocabulary Modularization

Modularizes `VOCABULARY.md` without runtime capability.

It keeps vocabulary as an active GENUS build boundary while moving vocabulary
blocks into `docs/vocabulary/` by role.

### v0.3.7 - Roadmap Modularization

Modularizes `ROADMAP_STABLE_CORE.md` without runtime capability.

It turns the roadmap into an index and moves phase notes into
`docs/roadmap/` by lifecycle area.

### v0.3.8 - Historical Spec Boundary

Marks historical foundation and language specs as frozen reference material
without runtime capability.

It clarifies that active build contracts live in current governance docs, not
in historical v0.0.1 specs.

### v0.3.9 - Ledger Test Modularization

Modularizes ledger lineage hardening tests without runtime capability.

It splits model/function and SQLite ledger hardening coverage into focused test
files and removes the ledger test longfile exception.
