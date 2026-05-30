# GENUS_CORE v0.3.5 Release Notes

Release: Decisions Modularization

## Summary

`GENUS_CORE v0.3.5` modularizes decision documentation.

It adds no runtime capability.

## What Changed

- `docs/DECISIONS.md` is now an active index.
- Decision blocks moved to `docs/decisions/` by version series.
- The index keeps an Active Decision Map so core GENUS build laws remain visible.
- Structure tests now require modular decision files and decision-number
  preservation.
- `docs/DECISIONS.md` is no longer a historical longfile exception.

## What Did Not Change

- No new CLI command.
- No new SQLite table.
- No schema change.
- No new runtime capability.
- No memory write, reaction, transition candidate, constraint decision, worker,
  LLM, GraphDB, or RuntimeShape.

`SCHEMA_VERSION` remains `genus.foundation.v0.0.1`.
