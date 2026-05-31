# GENUS_CORE v0.4.3 Release Notes

## Artifact Contract and Boundary Wording Alignment

v0.4.3 adds no runtime capability. It aligns governance and wording with the
active v0.4.2 passive Boundary Relevance runtime.

## Aligned

- `ARTIFACT_CONTRACTS.md` now lists active Passive Boundary Relevance IDs,
  source references, evidence lineage, and ephemeral lifecycle.
- `BUILD_RULES.md` now lists the accepted
  `genus_core.passive_boundary_relevance` namespace exports.
- `README.md` now documents `PassiveBoundaryRelevanceReport` and the
  v0.4.0 through v0.4.3 schema boundary.
- `FUNCTION_CELLS.md` records public function-cell contracts.

## Hardened

- Passive Boundary Relevance report payloads reject additional active-planning,
  permission, policy, worker, LLM, GraphDB, and RuntimeShape fields.
- Passive Transition runtime questions use `describe` instead of `evaluate`.
- Passive Transition runtime questions reject `evaluate` and `evaluation`.

## Boundaries

- No CLI expansion.
- No SQLite expansion.
- No sentence-type expansion.
- No `SCHEMA_VERSION` change.
- No new product capability.
