"""Create an Observation from a WorldEvent."""

from genus_core.models.observation import Observation
from genus_core.models.world_event import WorldEvent

MEMORY_REQUEST_PREFIX = "merk dir das:"


def observe_event(world_event: WorldEvent) -> Observation:
    text = (world_event.raw_text or "").strip()
    lowered = text.lower()

    if lowered.startswith(MEMORY_REQUEST_PREFIX):
        candidate = text[len(MEMORY_REQUEST_PREFIX) :].strip()
        return Observation(
            source_event_id=world_event.event_id,
            observation_type="memory_request_observed",
            scope="memory",
            confidence="high",
            payload_json={"candidate_content": candidate},
        )

    return Observation(
        source_event_id=world_event.event_id,
        observation_type="unknown_input_observed",
        scope="input",
        confidence="low",
        payload_json={"raw_text": text},
    )
