from genus_core.functions import observe_event
from genus_core.models import BeliefStateSnapshot, EvidenceRecord, LedgerEntry, Observation
from genus_core.models.world_event import WorldEvent


def test_user_text_memory_request_observed() -> None:
    observation = observe_event(
        WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    )

    assert observation.observation_type == "memory_request_observed"
    assert observation.scope == "memory"
    assert observation.confidence == "high"
    assert observation.payload_json["observed_memory_content"] == "larumipsum"
    assert "candidate_content" not in observation.payload_json


def test_incomplete_memory_request_is_ambiguous() -> None:
    observation = observe_event(WorldEvent(event_type="user_text", raw_text="merk dir das:"))

    assert observation.observation_type == "ambiguous_input_observed"
    assert observation.scope == "memory"
    assert observation.confidence == "medium"
    assert observation.payload_json["reason"] == "missing_memory_content"
    assert observation.payload_json["raw_text"] == "merk dir das:"


def test_empty_user_text_is_unknown_input() -> None:
    observation = observe_event(WorldEvent(event_type="user_text", raw_text="   "))

    assert observation.observation_type == "unknown_input_observed"
    assert observation.scope == "input"
    assert observation.confidence == "low"
    assert observation.payload_json["raw_text"] == ""


def test_memory_lookup_failed_observed_with_source_payload() -> None:
    source_payload = {"lookup_key": "larumipsum"}
    observation = observe_event(
        WorldEvent(event_type="memory_lookup_failed", payload_json=source_payload)
    )

    assert observation.observation_type == "memory_lookup_failure_observed"
    assert observation.scope == "memory"
    assert observation.confidence == "high"
    assert observation.payload_json == source_payload
    assert observation.payload_json is not source_payload


def test_guard_blocked_transition_observed_with_source_payload() -> None:
    source_payload = {"guard": "foundation_boundary"}
    observation = observe_event(
        WorldEvent(event_type="guard_blocked_transition", payload_json=source_payload)
    )

    assert observation.observation_type == "guard_block_observed"
    assert observation.scope == "system"
    assert observation.confidence == "high"
    assert observation.payload_json == source_payload
    assert observation.payload_json is not source_payload


def test_unsupported_event_type_is_unknown_and_preserves_source_context() -> None:
    source_payload = {"source": "probe"}
    observation = observe_event(
        WorldEvent(
            event_type="unrecognized_event",
            raw_text="raw signal",
            payload_json=source_payload,
        )
    )

    assert observation.observation_type == "unknown_input_observed"
    assert observation.scope == "input"
    assert observation.confidence == "low"
    assert observation.payload_json["original_event_type"] == "unrecognized_event"
    assert observation.payload_json["raw_text"] == "raw signal"
    assert observation.payload_json["payload_json"] == source_payload


def test_classification_returns_only_observation_without_epistemic_side_effects() -> None:
    observation = observe_event(
        WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    )

    assert isinstance(observation, Observation)
    assert not isinstance(observation, EvidenceRecord)
    assert not isinstance(observation, LedgerEntry)
    assert not isinstance(observation, BeliefStateSnapshot)
