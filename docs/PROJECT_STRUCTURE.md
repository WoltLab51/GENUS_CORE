# GENUS_CORE Project Structure

Status: active for v0.4.1 Passive Boundary Relevance Preview Seed

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

`ARTIFACT_CONTRACTS.md`

Defines how GENUS artifacts compose through IDs, source lineage, evidence
lineage, snapshot/preview/report roles, durable/ephemeral boundaries, and report
limits.

`SPEC_BOUNDARIES.md`

Marks historical specs as frozen references and points active contracts to
current governance docs.

`QUALITY_GATES.md`

Indexes modular quality gate files. Historical acceptance and stop gates live
under `docs/quality_gates/`.

`DECISIONS.md`

Indexes modular architectural decisions. Decisions are active GENUS build laws,
not only historical notes. Decision blocks live under `docs/decisions/`.

`STATUS.md`

States the current baseline and active acceptance state. It is not the place
for full design specs.

`ROADMAP_STABLE_CORE.md`

Indexes modular roadmap files. It should stay navigational, not become a
second spec archive.

`VOCABULARY.md`

Indexes modular vocabulary files. Vocabulary defines how GENUS terms may be
used. It is a build boundary, not a synonym list.

`PASSIVE_*_SPEC_*.md` and related spec files

Describe planned or accepted narrow concepts. Specs should stay focused on one
boundary or artifact family.

`RELEASE_NOTES_*.md`

Summarize release-specific changes. They should not redefine architecture.

## Historical Longfiles

The following files are accepted historical longfiles for v0.3.9:

```text
docs/FOUNDATION_SPEC_v0.0.1.md
docs/GENUS_LANGUAGE_SPEC_v0.0.1.md
docs/CODEX_IMPLEMENTATION_PROMPT_v0.0.1.md
docs/decisions/v0.0.md
docs/vocabulary/foundation.md
docs/quality_gates/v0.0.md
docs/quality_gates/v0.1.md
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

Quality gates were modularized in v0.3.3.
Decisions were modularized in v0.3.5.
Vocabulary was modularized in v0.3.6.
Roadmap was modularized in v0.3.7.
Historical spec boundaries were clarified in v0.3.8.
Ledger lineage tests were modularized in v0.3.9.

Remaining historical longfiles stay frozen through explicit ceilings until a
future modularization step changes them.
