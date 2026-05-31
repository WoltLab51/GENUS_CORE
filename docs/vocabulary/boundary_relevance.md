# GENUS_CORE Vocabulary - Boundary Relevance
Status: active for v0.4.1 Passive Boundary Relevance Preview Seed

## Passive Boundary Relevance

A passive description of boundary areas that may be relevant for a governed
question.

It is not boundary evaluation, permission evaluation, policy evaluation,
approval, rejection, allow/block, decision, reaction, or memory write.

## boundary_area

A closed enum for the boundary area being described.

Accepted spec values:

```text
memory_boundary
passive_foundation_boundary
passive_preview_boundary
```

It is not free-form text and must not become policy, permission, score,
priority, severity, or weight.

v0.4.1 emits only:

```text
memory_boundary
passive_preview_boundary
```

`passive_foundation_boundary` remains spec-known but is not emitted until an
explicit passive derivation rule exists.

## observed_boundary_relevance

A descriptive relevance label for a passive boundary relevance preview.

It is not numeric, level, score, rank, priority, severity, weight,
recommendation, permission, decision, or truth.

## boundary_question

A descriptive question associated with passive boundary relevance.

It is not instruction, recommendation, approval, permission, allow/block,
policy, execution, reaction, or memory write.
