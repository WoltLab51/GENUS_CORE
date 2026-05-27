import tomllib
from pathlib import Path

import genus_core


def test_package_version_is_v0_0_6() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["version"] == "0.0.6"
    assert genus_core.__version__ == "0.0.6"


def test_schema_version_remains_v0_0_1_foundation() -> None:
    assert genus_core.SCHEMA_VERSION == "genus.foundation.v0.0.1"
