# GENUS_CORE Vocabulary - Boundary Relevance
Status: active for v0.4.0 Passive Boundary Relevance Spec

## Passive Boundary Relevance

A passive description of boundary areas that may later be relevant for a
governed question.

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

## observed_boundary_relevance

A descriptive relevance label for a passive boundary relevance preview.

It is not numeric, level, score, rank, priority, severity, weight,
recommendation, permission, decision, or truth.

## boundary_question

A descriptive question associated with passive boundary relevance.

It is not instruction, recommendation, approval, permission, allow/block,
policy, execution, reaction, or memory write.
