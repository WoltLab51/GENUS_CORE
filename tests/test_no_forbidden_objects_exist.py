import importlib
import inspect
import pkgutil

import genus_core


FORBIDDEN_OBJECTS = {
    "PhysicsMetric",
    "CognitiveStateMap",
    "TransitionCandidate",
    "ConstraintDecision",
    "Reaction",
    "ReactionExecution",
    "MemoryWrite",
    "MemoryObject",
    "Worker",
    "RuntimeCell",
    "Organ",
    "Agent",
    "LLM",
}


def test_no_forbidden_objects_exist() -> None:
    discovered_names: set[str] = set()

    for module_info in pkgutil.walk_packages(
        genus_core.__path__, genus_core.__name__ + "."
    ):
        module = importlib.import_module(module_info.name)
        discovered_names.add(module_info.name.rsplit(".", 1)[-1])
        for name, value in inspect.getmembers(module):
            if inspect.isclass(value) and value.__module__.startswith("genus_core"):
                discovered_names.add(name)

    assert FORBIDDEN_OBJECTS.isdisjoint(discovered_names)
