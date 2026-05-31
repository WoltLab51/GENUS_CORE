# GENUS_CORE Spec Boundaries

Status: active for v0.4.3 Artifact Contract and Boundary Wording Alignment

## Purpose

Historical specs are governed artifacts, but they are not the current source of
active build contracts.

GENUS keeps old specs readable for lineage while routing current build rules to
active governance documents.

## Historical Specs

These files are frozen historical references:

```text
docs/FOUNDATION_SPEC_v0.0.1.md
docs/GENUS_LANGUAGE_SPEC_v0.0.1.md
```

They may explain why the passive foundation exists. They must not be used to
override current artifact contracts, safety boundaries, build rules, quality
gates, decisions, status, or vocabulary.

## Active Contract Sources

Current build authority lives in:

```text
docs/GENUS_CHARTER.md
docs/SAFETY_BOUNDARIES.md
docs/ARTIFACT_CONTRACTS.md
docs/BUILD_RULES.md
docs/QUALITY_GATES.md
docs/DECISIONS.md
docs/VOCABULARY.md
docs/STATUS.md
```

## Update Rule

Historical specs should receive only boundary notes or explicit historical
annotations. New runtime contracts, future planning, or acceptance rules must
go into focused active governance or spec files.

## Stop Rule

Stop if a historical spec is treated as permission to introduce runtime
capability, schema changes, CLI commands, SQLite tables, MemoryWrite, Reaction,
TransitionCandidate, ConstraintDecision, Worker, LLM, GraphDB, or RuntimeShape.
