# GENUS_CORE v0.5.0 Draft Release Notes

Status: draft. v0.5.0 is not accepted or released by this file.

## GENUS_KERNEL STCT Spec Baseline

v0.5.0 is planned as a docs-only governance baseline for GENUS_KERNEL.

It formalizes the distinction:

```text
GENUS_CORE = Erkenntnis ohne Handlung
GENUS_KERNEL = Veraenderung ohne Handlung
```

## Planned Additions

- Kernel quality gates in `docs/quality_gates/v0.5.md`.
- Kernel decisions in `docs/decisions/v0.5.md`.
- Kernel vocabulary in `docs/vocabulary/kernel.md`.
- Kernel roadmap in `docs/roadmap/kernel.md`.
- Draft v0.5.0 release notes in this file.

## Boundaries

This planned release adds no runtime capability.

It does not change:

```text
src/
tests/
SQLite schema
CLI behavior
README.md
docs/STATUS.md
pyproject.toml
SCHEMA_VERSION
```

## Kernel Boundary

Future kernel terms remain spec-only:

```text
KernelStateSnapshot
KernelTransitionPreview
KernelConstraintCheckPreview
KernelTraceEntry
KernelReport
```

They are not active GENUS_CORE runtime artifacts.

## Release Decision

Before v0.5.0 can be accepted as a release, the repo must explicitly decide
whether to update `README.md`, `docs/STATUS.md`, package version, and release
tag. This draft does not make that decision.
