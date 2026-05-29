# GENUS_CORE v0.3.4 Release Notes

Release: Artifact Contract Alignment

## Summary

`GENUS_CORE v0.3.4` documents shared artifact contracts.

It adds no runtime capability.

## What Changed

- Added `docs/ARTIFACT_CONTRACTS.md`.
- Documented ID, source-lineage, evidence-lineage, snapshot/preview/report,
  durable/ephemeral, report-boundary, compatibility, and watched-wording
  contracts.
- Added tests proving active artifacts keep primary IDs, common metadata,
  source references, evidence lineage, and unchanged SQLite durability.
- Updated v0.4.0 spec-only planning to preserve active package version `0.3.4`.

## What Did Not Change

- No new CLI command.
- No new SQLite table.
- No schema change.
- No new runtime capability.
- No memory write, reaction, transition candidate, constraint decision, worker,
  LLM, GraphDB, or RuntimeShape.

`SCHEMA_VERSION` remains `genus.foundation.v0.0.1`.
