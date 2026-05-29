# GENUS_CORE Project Structure

Status: active for v0.3.2 Build Structure Guardrails

GENUS_CORE treats code, tests, docs, specs, decisions, and quality gates as
governed artifacts.

Each artifact must stay bounded, readable, reviewable, and auditable.

## Document Responsibilities

`GENUS_CHARTER.md`

Defines the GENUS constitution: identity, growth ladder, truth discipline,
action discipline, learning discipline, LLM role, and top-level build
principles.

`SAFETY_BOUNDARIES.md`

Defines operative stop boundaries for current and planned work. It records what
the current system must not do.

`BUILD_RULES.md`

Defines how Codex and future builders must shape changes. It governs function
granularity, side effects, file growth, split rules, and documentation hygiene.

`QUALITY_GATES.md`

Records historical acceptance and stop gates. It is currently a historical
longfile and must not receive unbounded new phase-specific bulk content.

`DECISIONS.md`

Records architectural decisions. It is currently a historical longfile and
should not absorb large new decision blocks indefinitely.

`STATUS.md`

States the current baseline and active acceptance state. It is not the place
for full design specs.

`ROADMAP_STABLE_CORE.md`

Summarizes accepted and planned phases. It should stay navigational, not become
a second spec archive.

`VOCABULARY.md`

Defines active and planned terms. It should clarify language boundaries without
becoming an implementation guide.

`PASSIVE_*_SPEC_*.md` and related spec files

Describe planned or accepted narrow concepts. Specs should stay focused on one
boundary or artifact family.

`RELEASE_NOTES_*.md`

Summarize release-specific changes. They should not redefine architecture.

## Historical Longfiles

The following files are accepted historical longfiles for v0.3.2:

```text
docs/QUALITY_GATES.md
docs/DECISIONS.md
docs/FOUNDATION_SPEC_v0.0.1.md
docs/GENUS_LANGUAGE_SPEC_v0.0.1.md
docs/VOCABULARY.md
docs/CODEX_IMPLEMENTATION_PROMPT_v0.0.1.md
docs/ROADMAP_STABLE_CORE.md
tests/test_ledger_lineage_hardening.py
```

They may remain in place, but they are not permission to keep growing.

Each historical longfile must have:

```text
max_lines
reason
planned_split_or_review
```

## New Content Rule

New content should go into focused documents or focused tests.

If a change would push a file over its normal target or declared historical
ceiling, Codex must propose a split, a justified exception, or a dedicated
modularization step.

## Planned Modularization

`v0.3.3 Documentation Modularization` is the expected future cleanup step if
historical longfiles need structural reduction.

Likely candidates:

```text
docs/QUALITY_GATES.md
docs/DECISIONS.md
```

Until then, v0.3.2 freezes their growth through explicit ceilings.
