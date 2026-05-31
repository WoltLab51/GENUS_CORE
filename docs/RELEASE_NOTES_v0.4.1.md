# GENUS_CORE v0.4.1 Release Notes

## Passive Boundary Relevance Preview Seed

v0.4.1 activates the first narrow passive Boundary Relevance runtime layer.

## Added

- `genus_core.passive_boundary_relevance`
- `PassiveBoundaryRelevancePreview`
- `PassiveBoundaryRelevanceReport`
- `build_passive_boundary_relevance_preview(...)`
- `create_passive_boundary_relevance_report(...)`

## Boundaries

- No CLI expansion.
- No SQLite expansion.
- No sentence-type expansion.
- No `SCHEMA_VERSION` change.
- No `ConstraintDecision`, `PolicyResult`, permission, allow/block, Reaction,
  MemoryWrite, Worker, LLM, GraphDB, or RuntimeShape.
- `passive_foundation_boundary` is spec-known but not emitted in v0.4.1.

## Verification

- `python -m pytest`
- CLI smoke with temporary `GENUS_CORE_TRUTH_DB`
- `git diff --check`
