# GENUS_CORE Vocabulary

Status: active for v0.3.9 Ledger Test Modularization

Vocabulary defines how GENUS terms may be used. It is a build boundary, not a synonym list.

## Active Vocabulary Map

```text
Foundation terms: WorldEvent, Observation, EvidenceRecord, LedgerEntry, BeliefStateSnapshot, ObservationReport.
Observation terms: memory_request_observed, memory_lookup_failure_observed, guard_block_observed, unknown_input_observed, ambiguous_input_observed.
Passive layer terms: PassiveMetricSnapshot, PassiveMetricReport, PassiveTransitionPreview, PassiveTransitionReport.
Forbidden future concepts: MemoryWrite, Reaction, TransitionCandidate, ConstraintDecision, Worker, LLM, GraphDB, RuntimeShape remain unavailable unless separately accepted.
Boundary language: terms must not imply more capability than the active release permits.
```

## Modular Vocabulary Files

```text
docs/vocabulary/foundation.md - Foundation terms, observation types, and ledger enums
docs/vocabulary/forbidden_future.md - Future concepts that remain forbidden
docs/vocabulary/passive_layers.md - Passive Physics, passive transition, and metric vocabulary
```

Vocabulary blocks remain authoritative in their modular files. New terms should be added to the matching modular vocabulary file or to a new focused vocabulary file, not appended to this index.
