"""Create an Observation from a WorldEvent."""

from typing import Any

from genus_core.models.observation import Observation
from genus_core.models.world_event import WorldEvent

MEMORY_REQUEST_PREFIX = "merk dir das:"


def _source_payload(world_event: WorldEvent) -> dict[str, Any]:
    return dict(world_event.payload_json)


def observe_event(world_event: WorldEvent) -> Observation:
    text = (world_event.raw_text or "").strip()
    lowered = text.lower()

    if world_event.event_type == "memory_lookup_failed":
        return Observation(
            source_event_id=world_event.event_id,
            observation_type="memory_lookup_failure_observed",
            scope="memory",
            confidence="high",
            payload_json=_source_payload(world_event),
        )

    if world_event.event_type == "guard_blocked_transition":
        return Observation(
            source_event_id=world_event.event_id,
            observation_type="guard_block_observed",
            scope="system",
            confidence="high",
            payload_json=_source_payload(world_event),
        )

    if world_event.event_type == "user_text" and lowered.startswith(MEMORY_REQUEST_PREFIX):
        observed_memory_content = text[len(MEMORY_REQUEST_PREFIX) :].strip()
        if not observed_memory_content:
            return Observation(
                source_event_id=world_event.event_id,
                observation_type="ambiguous_input_observed",
                scope="memory",
                confidence="medium",
                payload_json={
                    "reason": "missing_memory_content",
                    "raw_text": text,
                },
            )
        return Observation(
            source_event_id=world_event.event_id,
            observation_type="memory_request_observed",
            scope="memory",
            confidence="high",
            payload_json={"observed_memory_content": observed_memory_content},
        )

    if world_event.event_type != "user_text":
        payload: dict[str, Any] = {"original_event_type": world_event.event_type}
        if world_event.raw_text is not None:
            payload["raw_text"] = text
        if world_event.payload_json:
            payload["payload_json"] = _source_payload(world_event)
        return Observation(
            source_event_id=world_event.event_id,
            observation_type="unknown_input_observed",
            scope="input",
            confidence="low",
            payload_json=payload,
        )

    return Observation(
        source_event_id=world_event.event_id,
        observation_type="unknown_input_observed",
        scope="input",
        confidence="low",
        payload_json={"raw_text": text},
    )
