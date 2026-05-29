# GENUS_CORE Build Rules

Status: active for v0.3.0 Passive Transition Preview Seed

These rules implement the repository-level governance defined in
`GENUS_CHARTER.md` and `SAFETY_BOUNDARIES.md`.

## 1. Function-first, not Monolith

GENUS_CORE must be built from small responsible functions.

It must not be built as:

```text
god service
large manager
agent loop
hidden orchestrator
monolith kernel
service class
registry
plugin system
```

## 2. Function-first, not Atomistic

Do not create a separate file for every helper.

A separate public function/file is justified only when it has a GENUS responsibility.

Examples that deserve public functions:

```text
observe_event()
create_evidence_record()
append_ledger_entry()
build_belief_state_snapshot()
create_observation_report()
```

Examples that do not deserve public function files:

```text
normalize_string()
format_json()
make_label()
is_high()
```

Helpers should remain private inside the module that uses them.

## 3. Function Definition Standard

Every public GENUS function must declare:

```text
Purpose
Inputs
Outputs
Side effects
Allowed writes
Forbidden effects
Tests
```

## 4. Side Effects

Public foundation functions should be pure unless explicitly named as persistence functions.

Allowed persistence functions in v0.0.1:

```text
save_evidence_record()
save_ledger_entry()
```

Forbidden side effects:

```text
memory write
reaction execution
worker execution
network call
LLM call
file mutation outside SQLite store
```

## 5. CLI Rule

CLI is not business logic.

CLI may:

```text
read arguments
call functions
print reports
return exit codes
```

CLI must not:

```text
calculate belief logic
hide validation rules
create actions
bypass store rules
bypass documentation rules
```

## 6. No New Power Without Boundary

A new capability or action can only be introduced if:

```text
GENUS_CHARTER.md allows the direction.
SAFETY_BOUNDARIES.md defines it.
QUALITY_GATES.md defines acceptance.
Tests cover it.
DECISIONS.md records why it exists.
STATUS.md reflects it.
```

## 7. No New Concepts Without Vocabulary

Every new concept must be defined in `VOCABULARY.md` before code uses it.

A concept definition must include:

```text
What it is
What it is not
Required fields
Allowed phase
Forbidden misuse
```

## 8. No New Capability Without Test

Every new capability must have a test before it is accepted.

For the foundation namespace, this means only the accepted foundation
capabilities may exist:

```text
observe_event()
create_evidence_record()
append_ledger_entry()
build_belief_state_snapshot()
create_observation_report()
save_evidence_record()
save_ledger_entry()
```

The separate `genus_core.passive_physics` namespace may expose only the
accepted passive v0.2.x artifacts:

```text
PassiveMetricSnapshot
PassiveMetricReport
build_passive_metric_snapshot()
create_passive_metric_report()
```

The separate `genus_core.passive_transition` namespace may expose only the
accepted passive v0.3.0 preview artifacts:

```text
PassiveTransitionPreview
PassiveTransitionReport
build_passive_transition_preview()
create_passive_transition_report()
```
