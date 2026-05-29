# GENUS_CORE v0.3.2 Release Notes

Release: Build Structure Guardrails

## Summary

`GENUS_CORE v0.3.2` adds governance for the repository structure itself.

It adds no runtime capability.

## What Changed

- `docs/BUILD_RULES.md` now treats code, tests, docs, specs, decisions, and
  quality gates as governed artifacts.
- `docs/PROJECT_STRUCTURE.md` defines document responsibilities and historical
  longfile handling.
- Structure tests now enforce normal line-count targets and explicit
  historical longfile exceptions.
- Historical longfile exceptions require `max_lines`, `reason`, and
  `planned_split_or_review`.

## What Did Not Change

- No new CLI command.
- No new SQLite table.
- No schema change.
- No new runtime capability.
- No memory write, reaction, transition candidate, constraint decision, worker,
  LLM, GraphDB, or RuntimeShape.

`SCHEMA_VERSION` remains `genus.foundation.v0.0.1`.
