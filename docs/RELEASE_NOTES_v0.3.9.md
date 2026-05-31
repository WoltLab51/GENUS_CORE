# GENUS_CORE v0.3.9 Release Notes

Release: Ledger Test Modularization

Status: governance/test-structure release; no new runtime capability

## Summary

`GENUS_CORE v0.3.9` splits Ledger lineage hardening tests into focused model /
function and SQLite constraint test files.

The Ledger hardening coverage remains, but the old test longfile exception is
removed.

## Boundaries

No runtime source package, CLI command, SQLite table, sentence type,
`SCHEMA_VERSION` change, worker, LLM, memory write, reaction, transition
candidate, constraint decision, GraphDB, or RuntimeShape is introduced.
