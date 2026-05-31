# GENUS_CORE v0.3.6 Release Notes

Release: Vocabulary Modularization

Status: governance/documentation release; no new runtime capability

## Summary

`GENUS_CORE v0.3.6` modularizes vocabulary documentation.

It keeps vocabulary as an active build boundary while turning
`docs/VOCABULARY.md` into an index and moving vocabulary blocks into focused
files under `docs/vocabulary/`.

## Changes

- `docs/VOCABULARY.md` is now an active vocabulary index.
- `docs/vocabulary/foundation.md` contains foundation, observation, report,
  and ledger vocabulary.
- `docs/vocabulary/forbidden_future.md` contains future concepts that remain
  forbidden.
- `docs/vocabulary/passive_layers.md` contains passive Physics and passive
  transition vocabulary.
- Build rules now direct new vocabulary blocks into modular vocabulary files,
  not the index.
- Quality gates and decision docs record the v0.3.6 governance boundary.

## Boundaries

No runtime source package, CLI command, SQLite table, sentence type,
`SCHEMA_VERSION` change, worker, LLM, memory write, reaction, transition
candidate, constraint decision, GraphDB, or RuntimeShape is introduced.
