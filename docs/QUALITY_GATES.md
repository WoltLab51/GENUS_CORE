# GENUS_CORE Quality Gates

Status: active for v0.3.3 Quality Gates Modularization

## 1. Purpose

Quality Gates define the conditions that must be met before a GENUS_CORE phase can be accepted.

GENUS must not grow by enthusiasm alone.

Every phase must pass documentation, test, architecture, and safety checks.

## 2. Universal Quality Gate

Every GENUS_CORE phase must pass:

```text
pytest green
CLI smoke test green
all new terms documented
all new invariants tested
STATUS.md updated
DECISIONS.md updated when architecture changed
SAFETY_BOUNDARIES.md updated when power changed
no forbidden artifacts introduced
```

## 8. Architecture Review Result Format

Each phase review must output:

```text
Philosophy-Fit: green/yellow/red
Governance-Fit: green/yellow/red
Function-Granularity-Fit: green/yellow/red
Overengineering-Risk: low/medium/high
Documentation-Drift-Risk: low/medium/high
Decision: accept/harden/stop
```

## Modular Gate Files

Historical and phase-specific gates now live in focused files:

```text
docs/quality_gates/v0.0.md
docs/quality_gates/v0.1.md
docs/quality_gates/v0.2.md
docs/quality_gates/v0.3.md
docs/quality_gates/planned.md
```

Planned v0.4.0 spec-only gates live in `docs/quality_gates/planned.md`.

New phase-specific gates must be added to the matching modular gate file or to a new focused gate file. They must not be appended to this index.
