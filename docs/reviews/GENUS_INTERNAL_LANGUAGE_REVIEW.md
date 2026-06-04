# GENUS Internal Language Review

Status: review document only. No runtime capability is introduced.

Purpose: define the minimal internal-language question behind
`MeaningObject`, so GENUS can later work structurally instead of repeatedly
reinterpreting broad natural-language context.

References:

```text
docs/reviews/GENUS_EFFICIENCY_METHOD.md
docs/reviews/GENUS_PRESENCE_SELF_STATE_REVIEW.md
docs/reviews/GENUS_KERNEL_REPO_LEARNING_MAP.md
docs/vocabulary/kernel.md
```

## Executive Summary

GENUS should not become efficient by keeping more natural language hot.

GENUS should become efficient by compiling raw or observed language into small,
typed, evidence-linked meaning records that downstream layers can reference.

Review concept:

```text
MeaningObject = compact governed meaning representation
```

Core rule:

```text
Natural language is interface.
MeaningObject is internal structure.
Evidence and Ledger remain the audit base.
```

`MeaningObject` is not active runtime, not a schema, and not a permission,
decision, memory, or truth object.

## Why Internal Language

GENUS needs an internal language because the long-term system should not ask a
model to repeatedly rediscover:

```text
intent
content reference
risk
effect class
room
sensitivity
source evidence
trace
forbidden effects
```

Compiled meaning lets GENUS operate cheaply with references:

```text
meaning_ref + state_ref + trace_ref -> preview/report
```

instead of:

```text
full text history -> large model -> broad reinterpretation
```

## Placement

Safe future placement:

```text
WorldEvent / Observation
-> EvidenceRecord
-> MeaningObject
-> BeliefStateSnapshot / KernelStateSnapshot
-> Preview / Report
```

Meaning may be proposed from language, but it must be tied back to evidence
before downstream use.

Boundary:

```text
MeaningObject != Observation
MeaningObject != EvidenceRecord
MeaningObject != LedgerEntry
MeaningObject != BeliefStateSnapshot
MeaningObject != Memory
MeaningObject != Decision
MeaningObject != Permission
```

## Minimal Candidate Fields

Candidate field set for future specs:

| Field | Role |
| --- | --- |
| `meaning_id` | Stable ID for the compiled meaning object. |
| `source_ref` | Reference to Observation, EvidenceRecord, or approved input artifact. |
| `content_ref` | Pointer to content, not necessarily copied content. |
| `intent` | What kind of meaning was recognized. |
| `effect_class` | What kind of effect is implied or explicitly excluded. |
| `risk_class` | Low-level risk label for routing and review. |
| `confidence` | Confidence in the compilation, not truth. |
| `room` | Context boundary such as private, repo, device, or public. |
| `sensitivity` | Data sensitivity label. |
| `trace_ref` | Link to evidence or trace lineage. |
| `requires_review` | Whether escalation is needed. |
| `forbidden_effects` | Effects that this meaning must not trigger. |

This field set is a review candidate only. It is not an accepted runtime
schema.

## Example Shape

Review-only example:

```json
{
  "meaning_id": "meaning_example",
  "source_ref": "ev_example",
  "content_ref": "content_example",
  "intent": "memory_request",
  "effect_class": "proposal_only",
  "risk_class": "low",
  "confidence": "medium",
  "room": "private",
  "sensitivity": "user_provided",
  "trace_ref": "led_example",
  "requires_review": true,
  "forbidden_effects": ["memory_write", "external_call", "reaction"]
}
```

This example does not authorize memory, action, external calls, or persistence.

## Field Boundaries

`intent` must not mean decision or goal.

`effect_class` must not mean permission.

`risk_class` must not mean allow/block.

`confidence` must not mean truth.

`room` must not mean access grant.

`sensitivity` must not mean policy result.

`trace_ref` must not mean Ledger replacement.

`requires_review` must not mean approval.

`forbidden_effects` must be restrictive only.

## Allowed Uses

Future internal language may support:

```text
cheap routing
state reconstruction
attention selection
kernel preview input
presence/self-state references
small model handoff
report generation
uncertainty escalation
```

These uses must remain passive until separate governance accepts runtime
capability.

## Forbidden Uses

MeaningObject must not:

```text
write memory
execute tools
call networks
authorize action
grant permission
replace EvidenceRecord
replace LedgerEntry
become world truth
create ConstraintDecision
create PolicyResult
start Worker, Agent, Organ, or RuntimeCell
```

## Model Role

Small local models may later propose or assist compilation:

```text
intent classification
similarity lookup
ambiguity detection
short summarization
surface wording
```

But models remain proposers. GENUS must validate and bound their output before
it becomes internal meaning.

Boundary:

```text
model output != MeaningObject until validated
MeaningObject != truth
validated meaning != permission
```

## Compatibility

With CORE: MeaningObject must preserve evidence lineage and must not weaken
the active foundation chain.

With KERNEL: MeaningObject may later feed `KernelStateSnapshot` only through an
accepted handoff spec.

With Efficiency Method: MeaningObject is the compact unit that allows
`Interpret rarely` and `Operate structurally`.

With Presence/SelfState: MeaningObject provides refs for attention and
self-state without broad prompt-only belief.

## Open Questions

```text
Should the first accepted artifact be MeaningObject or MeaningObjectPreview?
Should content be copied, referenced, or both?
Which intent enum is safe as the first minimal set?
Can MeaningObject exist before Memory exists?
Which fields are required for replay?
Should room and sensitivity live here or in a separate context artifact?
```

## Final Recommendation

Accept internal language as the next review axis. Start with MeaningObject as a
review concept, but do not implement it until vocabulary, gates, tests, and
artifact contracts are accepted.

Assessment:

```text
Plausibel: ja
Konsistent: ja
Vollstaendig: teilweise
Empfehlung: akzeptieren als Review-Methode, noch nicht als Runtime
```
