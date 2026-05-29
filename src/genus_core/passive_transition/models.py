"""Passive transition preview models for GENUS_CORE v0.3.x."""

from dataclasses import dataclass, field
import re
from typing import Any

from genus_core import SCHEMA_VERSION
from genus_core.ids import new_id
from genus_core.time import utc_now_iso

ALLOWED_PASSIVE_TRANSITION_PREVIEW_TYPES = frozenset(
    {
        "memory_request_transition_tension_preview",
        "no_visible_transition_tension_preview",
    }
)
FORBIDDEN_POSSIBLE_FUTURE_QUESTION_WORDS = frozenset(
    {"should", "must", "allow", "block", "execute", "write", "approve", "recommend"}
)
FORBIDDEN_PASSIVE_TRANSITION_FIELDS = frozenset(
    {
        "transition",
        "transition_candidate",
        "selected_transition",
        "proposed_transition",
        "target_state",
        "candidate",
        "constraint",
        "constraint_decision",
        "decision",
        "action",
        "execute",
        "approval",
        "permission",
        "recommendation",
        "priority",
        "score",
        "rank",
        "reaction",
        "memory_write",
        "truth",
        "truth_status",
        "world_truth",
        "policy",
        "policy_result",
        "allow",
        "block",
        "activation",
        "memory",
        "memory_object",
    }
)


def _contains_forbidden_question_word(value: str) -> str | None:
    lowered = value.lower()
    for word in sorted(FORBIDDEN_POSSIBLE_FUTURE_QUESTION_WORDS):
        if re.search(rf"\b{re.escape(word)}\b", lowered):
            return word
    return None


@dataclass(frozen=True)
class PassiveTransitionPreview:
    source_state_id: str
    source_metric_snapshot_id: str
    source_evidence_ids_json: list[str]
    preview_type: str
    observed_tension_summary: str
    possible_future_question: str
    no_action_possible: bool = True
    no_decision_possible: bool = True
    preview_id: str = field(default_factory=lambda: new_id("ptp_"))
    created_at: str = field(default_factory=utc_now_iso)
    schema_version: str = SCHEMA_VERSION

    def __post_init__(self) -> None:
        if not isinstance(self.source_state_id, str) or not self.source_state_id.strip():
            raise ValueError("PassiveTransitionPreview requires source_state_id")
        if (
            not isinstance(self.source_metric_snapshot_id, str)
            or not self.source_metric_snapshot_id.strip()
        ):
            raise ValueError("PassiveTransitionPreview requires source_metric_snapshot_id")
        if not isinstance(self.source_evidence_ids_json, list):
            raise TypeError("source_evidence_ids_json must be a list")
        if self.preview_type not in ALLOWED_PASSIVE_TRANSITION_PREVIEW_TYPES:
            raise ValueError(f"Invalid passive transition preview_type: {self.preview_type}")
        if (
            not isinstance(self.observed_tension_summary, str)
            or not self.observed_tension_summary.strip()
        ):
            raise ValueError("PassiveTransitionPreview requires observed_tension_summary")
        if (
            not isinstance(self.possible_future_question, str)
            or not self.possible_future_question.strip()
        ):
            raise ValueError("PassiveTransitionPreview requires possible_future_question")
        if not self.possible_future_question.strip().endswith("?"):
            raise ValueError("possible_future_question must be question-like")
        forbidden_word = _contains_forbidden_question_word(
            self.possible_future_question
        )
        if forbidden_word:
            raise ValueError(
                "possible_future_question contains forbidden runtime word: "
                f"{forbidden_word}"
            )
        if self.no_action_possible is not True:
            raise ValueError("PassiveTransitionPreview requires no_action_possible=True")
        if self.no_decision_possible is not True:
            raise ValueError("PassiveTransitionPreview requires no_decision_possible=True")

    @property
    def id(self) -> str:
        return self.preview_id


@dataclass(frozen=True)
class PassiveTransitionReport:
    source_preview_id: str
    summary: str
    payload_json: dict[str, Any] = field(default_factory=dict)
    report_id: str = field(default_factory=lambda: new_id("ptr_"))
    created_at: str = field(default_factory=utc_now_iso)
    schema_version: str = SCHEMA_VERSION

    def __post_init__(self) -> None:
        if not isinstance(self.source_preview_id, str) or not self.source_preview_id.strip():
            raise ValueError("PassiveTransitionReport requires source_preview_id")
        if not isinstance(self.summary, str) or not self.summary.strip():
            raise ValueError("PassiveTransitionReport requires summary")
        forbidden = FORBIDDEN_PASSIVE_TRANSITION_FIELDS.intersection(self.payload_json)
        if forbidden:
            names = ", ".join(sorted(forbidden))
            raise ValueError(
                f"PassiveTransitionReport cannot contain forbidden fields: {names}"
            )

    @property
    def id(self) -> str:
        return self.report_id
