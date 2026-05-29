# GENUS_CORE v0.3.3 Release Notes

Release: Quality Gates Modularization

## Summary

`GENUS_CORE v0.3.3` modularizes quality gate documentation.

It adds no runtime capability.

## What Changed

- `docs/QUALITY_GATES.md` is now an index.
- Historical gate blocks moved to `docs/quality_gates/` by version series.
- Project-structure tests now require the modular gate files and keep the index
  under the normal docs line-count target.
- `docs/QUALITY_GATES.md` is no longer a historical longfile exception.

## What Did Not Change

- No new CLI command.
- No new SQLite table.
- No schema change.
- No new runtime capability.
- No memory write, reaction, transition candidate, constraint decision, worker,
  LLM, GraphDB, or RuntimeShape.

`SCHEMA_VERSION` remains `genus.foundation.v0.0.1`.
