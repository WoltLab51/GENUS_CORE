"""Stable ID helpers for GENUS_CORE foundation objects."""

from uuid import uuid4


def new_id(prefix: str) -> str:
    if not prefix.endswith("_"):
        raise ValueError("ID prefix must end with underscore")
    return f"{prefix}{uuid4().hex}"


def new_chain_id() -> str:
    return new_id("chain_")
