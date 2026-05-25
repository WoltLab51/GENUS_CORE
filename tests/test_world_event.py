from genus_core.functions import observe_event
from genus_core.models import Observation, WorldEvent


def test_world_event_is_not_observation() -> None:
    world_event = WorldEvent(event_type="user_text", raw_text="merk dir das: larumipsum")
    observation = observe_event(world_event)

    assert isinstance(world_event, WorldEvent)
    assert isinstance(observation, Observation)
    assert not isinstance(world_event, Observation)
    assert world_event.event_id != observation.observation_id
    assert observation.source_event_id == world_event.event_id
