# GENUS_CORE Decisions

Status: active for v0.3.5 Decisions Modularization

Decisions govern how GENUS may be built. They are active build laws, not only historical notes.

## Decision Log Format

Each decision record uses:

```text
Decision
Reason
Impact
```

## Active Decision Map

```text
Epistemic boundary: Observation, Evidence, Ledger, Belief, and Report stay distinct.
No-action boundary: Report is not Decision; no MemoryWrite or Reaction exists.
Capability order: Foundation -> passive Physics -> passive transition preview -> boundary relevance spec.
Build governance: governed artifacts, modular quality gates, modular decisions, and artifact contracts.
v0.4.0 constraint: Boundary Relevance, not Boundary Evaluation.
v0.4.0 remains planned spec-only until separately accepted.
```

## Modular Decision Files

```text
docs/decisions/v0.0.md - Decisions 0001-0015
docs/decisions/v0.1.md - Decisions 0016-0025
docs/decisions/v0.2.md - Decisions 0026-0027
docs/decisions/v0.3.md - Decisions 0028-0034
```

Decision blocks remain numbered and authoritative in their modular files. New decision blocks should be added to the matching modular decision file or to a new focused decision file, not appended to this index.
