import ast
import importlib
import inspect
import pkgutil
import re
from pathlib import Path

import genus_core


FORBIDDEN_OBJECTS = {
    "PhysicsMetric",
    "Pressure",
    "Potential",
    "Cost",
    "Inhibition",
    "Stability",
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
    "Character",
    "LLM",
    "Autonomy",
    "Mutation",
    "Evolution",
    "GraphDB",
    "RuntimeShape",
}


def _snake_case(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def test_no_forbidden_objects_exist() -> None:
    discovered_names: set[str] = set()
    source_root = Path(genus_core.__file__).parent
    forbidden_file_stems = {_snake_case(name) for name in FORBIDDEN_OBJECTS}

    for module_info in pkgutil.walk_packages(
        genus_core.__path__, genus_core.__name__ + "."
    ):
        module = importlib.import_module(module_info.name)
        discovered_names.add(module_info.name.rsplit(".", 1)[-1])
        discovered_names.update(getattr(module, "__all__", ()))
        discovered_names.update(
            name for name in vars(module) if not name.startswith("_")
        )
        for name, value in inspect.getmembers(module):
            if inspect.isclass(value) and value.__module__.startswith("genus_core"):
                discovered_names.add(name)

    assert FORBIDDEN_OBJECTS.isdisjoint(discovered_names)
    assert forbidden_file_stems.isdisjoint(
        path.stem for path in source_root.rglob("*.py")
    )


def test_no_forbidden_imports_exist() -> None:
    source_root = Path(genus_core.__file__).parent
    forbidden_file_stems = {_snake_case(name) for name in FORBIDDEN_OBJECTS}
    forbidden_imports = FORBIDDEN_OBJECTS.union(forbidden_file_stems)
    discovered_imports: set[str] = set()

    for source_file in source_root.rglob("*.py"):
        tree = ast.parse(source_file.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    discovered_imports.add(alias.name.rsplit(".", 1)[-1])
                    discovered_imports.add(alias.asname or "")
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    discovered_imports.add(node.module.rsplit(".", 1)[-1])
                for alias in node.names:
                    discovered_imports.add(alias.name)
                    discovered_imports.add(alias.asname or "")

    assert forbidden_imports.isdisjoint(discovered_imports)
