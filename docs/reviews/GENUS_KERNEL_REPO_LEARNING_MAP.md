# GENUS_KERNEL Repo Learning Map

Status: review document only. No runtime capability is introduced.

Purpose: collect what GENUS_KERNEL should learn from previous GENUS repos,
specs, and the STCT study before any implementation exists.

Reference: `docs/reviews/GENUS_CORE_NEW_IDEA_COMPATIBILITY_CHECK.md`.

## Executive Summary

GENUS should not be rebuilt by discarding GENUS_CORE. The safer path is to
separate two proof questions:

```text
GENUS_CORE = Erkenntnis ohne Handlung
GENUS_KERNEL = Veraenderung ohne Handlung
```

GENUS_CORE already proves passive observation, evidence, lineage, and report
generation. GENUS_KERNEL should later prove that GENUS can model possible
change, identify relevant boundaries, and explain the trace of that modelling
without executing anything.

Layer order:

```text
Constitution
-> GENUS_CORE
-> GENUS_KERNEL
-> Capability Dimensions
-> Cells
-> Organs
-> Organisms
-> Characters / Interfaces
```

GENUS_CORE and GENUS_KERNEL are not organs. They are lower foundation/kernel
layers under future cells, organs, organisms, characters, and interfaces.

## Sources Reviewed

This map synthesizes lessons from:

| Source | Main lesson |
| --- | --- |
| `GENUS_CORE` | Passive evidence foundation must stay stable. |
| `GENUS_EGG` | Reaction can exist only behind explicit governance. |
| `PiGenus_Codex` | Contracts, rooms, guards, dry-run, and trace prevent drift. |
| `Genus` | Character and warmth belong above the safe core, not inside it. |
| `UrPi` | Local robustness, small surface area, and SQLite simplicity matter. |
| Phase-0 Kernel Spec | Constitutional objects should exist before capability objects. |
| STCT study | `State -> Transition -> Constraint -> Trace` is the strongest kernel hypothesis. |

## Architecture DNA To Preserve

| DNA | Meaning for GENUS_KERNEL |
| --- | --- |
| Passive first | Kernel work starts as previews and reports only. |
| Evidence lineage | Kernel traces must remain explainable and auditable. |
| Contract language | Every artifact needs a clear role and forbidden role. |
| Boundary wording | Terms must not imply permissions or decisions accidentally. |
| Small interfaces | Future APIs should expose narrow, inspectable objects. |
| Local durability discipline | No persistence expansion without a separate accepted spec. |
| Vocabulary discipline | Similar terms must be split before runtime work begins. |

## Historical Fossils

These ideas are useful as fossils but must not be imported directly into the
first GENUS_KERNEL spec:

| Fossil | Keep as lesson | Do not import yet |
| --- | --- | --- |
| MessageBus / DevLoop | Systems need orchestration boundaries. | Worker or runtime loop. |
| MemoryObject | Memory needs governance. | MemoryWrite or memory layer. |
| ReactionProduct | Reaction must be traceable. | Reaction capability. |
| GovernanceDecision | Decisions need strict shape. | ConstraintDecision in prototype spec. |
| Rooms / Actors | Context boundaries matter. | Active actors or agents. |
| Character layer | GENUS should later feel coherent. | Character in core/kernel. |

## Terms To Carry Forward

Preferred future GENUS_KERNEL spec terms:

```text
KernelStateSnapshot
KernelTransitionPreview
KernelConstraintCheckPreview
KernelTraceEntry
KernelReport
```

These names are intentionally prefixed because GENUS_CORE already has
`BeliefStateSnapshot`, `PassiveTransitionPreview`,
`PassiveBoundaryRelevancePreview`, reports, evidence records, and ledger
entries.

## Terms Not To Mix

Hard non-equivalences:

```text
KernelTransitionPreview != TransitionCandidate
KernelConstraintCheckPreview != ConstraintDecision
KernelTraceEntry != LedgerEntry
KernelTraceEntry != Memory
KernelTraceEntry != Weltwahrheit
KernelReport != Decision
KernelReport no_action statement != ConstraintDecision(no_action)
Preview != Permission
CORE/KERNEL != Organ
```

The key language rule is simple: a preview may describe shape, pressure,
uncertainty, relevance, or possible next questions. It must not grant
permission, choose a target, recommend action, persist memory, or execute.

## External Layers

The following belong above GENUS_CORE and GENUS_KERNEL:

| Layer | Why external for now |
| --- | --- |
| Cells | They compose functions into capability surfaces. |
| Organs | They coordinate cells toward purposes. |
| Organisms | They imply broader integrated behavior. |
| Characters | They imply persona, continuity, and interface behavior. |
| Workers | They imply runtime execution. |
| LLMs | They imply model integration and inference behavior. |
| Memory | It implies durable semantic continuity beyond evidence lineage. |
| Reactions | They imply outward behavior or internal execution. |

## CORE To KERNEL Handoff

GENUS_KERNEL must not observe raw input.

Safe handoff:

```text
WorldEvent
-> Observation
-> EvidenceRecord
-> LedgerEntry
-> BeliefStateSnapshot
-> KernelStateSnapshot
```

Future alternative:

```text
explicit StateInput -> KernelStateSnapshot
```

The future `StateInput` must be specified separately and must not become a
shortcut around GENUS_CORE evidence boundaries.

## Lessons For The First Kernel Spec

1. Start with documents, not runtime.
2. Use kernel-prefixed artifact names.
3. Keep all objects passive.
4. Treat `no_action` as a boundary statement, not a decision.
5. Treat trace as explanation, not durable truth.
6. Do not import historical reaction, memory, worker, agent, organ, or LLM ideas.
7. Require a later approved spec before any persistence, CLI, schema, or runtime
   expansion.

## Final Recommendation

Proceed with a spec-only GENUS_KERNEL prototype based on:

```text
State -> Transition -> Constraint -> Trace
```

but implement it first only as vocabulary, boundary law, and artifact contract.

Assessment:

```text
Plausibel: ja
Konsistent: ja
Vollstaendig: teilweise
Empfehlung: akzeptieren als Spec-/Review-Schritt
```
