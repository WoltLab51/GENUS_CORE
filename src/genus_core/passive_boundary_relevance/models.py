"""Passive boundary relevance models for GENUS_CORE v0.4.x."""

from dataclasses import dataclass, field
import re
from typing import Any

from genus_core import SCHEMA_VERSION
from genus_core.ids import new_id
from genus_core.time import utc_now_iso

ALLOWED_BOUNDARY_AREAS = frozenset(
    {
        "memory_boundary",
        "passive_preview_boundary",
        "passive_foundation_boundary",
    }
)
EMITTED_BOUNDARY_AREAS_V0_4_1 = frozenset(
    {
        "memory_boundary",
        "passive_preview_boundary",
    }
)
ALLOWED_OBSERVED_BOUNDARY_RELEVANCE = frozenset(
    {
        "memory_request_relevance_observed",
        "no_boundary_relevance_observed",
    }
)
FORBIDDEN_BOUNDARY_QUESTION_WORDS = frozenset(
    {
        "should",
        "must",
        "allow",
        "block",
        "execute",
        "write",
        "approve",
        "recommend",
        "permit",
        "permission",
        "policy",
    }
)
FORBIDDEN_BOUNDARY_RELEVANCE_PAYLOAD_FIELDS = frozenset(
    {
        "permission",
        "policy",
        "policy_result",
        "allow",
        "block",
        "approve",
        "reject",
        "recommendation",
        "score",
        "rank",
        "priority",
        "severity",
        "weight",
        "execute",
        "decision",
        "action",
        "reaction",
        "memory_write",
        "truth",
        "evaluation",
        "boundary_evaluation",
        "no_boundary_evaluation_possible",
    }
)


def _contains_forbidden_question_word(value: str) -> str | None:
    lowered = value.lower()
    for word in sorted(FORBIDDEN_BOUNDARY_QUESTION_WORDS):
        if re.search(rf"\b{re.escape(word)}\b", lowered):
            return word
    return None


def _require_non_empty_string(value: object, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"PassiveBoundaryRelevancePreview requires {field_name}")


@dataclass(frozen=True)
class PassiveBoundaryRelevancePreview:
    source_state_id: str
    source_metric_snapshot_id: str
    source_transition_preview_id: str
    source_evidence_ids_json: list[str]
    boundary_question: str
    boundary_area: str
    observed_boundary_relevance: str
    no_decision_possible: bool = True
    no_action_possible: bool = True
    preview_id: str = field(default_factory=lambda: new_id("pbrp_"))
    created_at: str = field(default_factory=utc_now_iso)
    schema_version: str = SCHEMA_VERSION

    def __post_init__(self) -> None:
        for field_name in (
            "source_state_id",
            "source_metric_snapshot_id",
            "source_transition_preview_id",
            "boundary_question",
            "boundary_area",
            "observed_boundary_relevance",
        ):
            _require_non_empty_string(getattr(self, field_name), field_name)
        if not isinstance(self.source_evidence_ids_json, list):
            raise TypeError("source_evidence_ids_json must be a list")
        if self.boundary_area not in ALLOWED_BOUNDARY_AREAS:
            raise ValueError(f"Invalid boundary_area: {self.boundary_area}")
        if self.boundary_area not in EMITTED_BOUNDARY_AREAS_V0_4_1:
            raise ValueError(
                f"boundary_area is not emitted in v0.4.1: {self.boundary_area}"
            )
        if (
            self.observed_boundary_relevance
            not in ALLOWED_OBSERVED_BOUNDARY_RELEVANCE
        ):
            raise ValueError(
                "Invalid observed_boundary_relevance: "
                f"{self.observed_boundary_relevance}"
            )
        if not self.boundary_question.strip().endswith("?"):
            raise ValueError("boundary_question must be question-like")
        forbidden_word = _contains_forbidden_question_word(self.boundary_question)
        if forbidden_word:
            raise ValueError(
                f"boundary_question contains forbidden runtime word: {forbidden_word}"
            )
        if self.no_decision_possible is not True:
            raise ValueError(
                "PassiveBoundaryRelevancePreview requires no_decision_possible=True"
            )
        if self.no_action_possible is not True:
            raise ValueError(
                "PassiveBoundaryRelevancePreview requires no_action_possible=True"
            )

    @property
    def id(self) -> str:
        return self.preview_id


@dataclass(frozen=True)
class PassiveBoundaryRelevanceReport:
    source_relevance_preview_id: str
    summary: str
    payload_json: dict[str, Any] = field(default_factory=dict)
    report_id: str = field(default_factory=lambda: new_id("pbrr_"))
    created_at: str = field(default_factory=utc_now_iso)
    schema_version: str = SCHEMA_VERSION

    def __post_init__(self) -> None:
        if (
            not isinstance(self.source_relevance_preview_id, str)
            or not self.source_relevance_preview_id.strip()
        ):
            raise ValueError(
                "PassiveBoundaryRelevanceReport requires source_relevance_preview_id"
            )
        if not isinstance(self.summary, str) or not self.summary.strip():
            raise ValueError("PassiveBoundaryRelevanceReport requires summary")
        forbidden = FORBIDDEN_BOUNDARY_RELEVANCE_PAYLOAD_FIELDS.intersection(
            self.payload_json
        )
        if forbidden:
            names = ", ".join(sorted(forbidden))
            raise ValueError(
                "PassiveBoundaryRelevanceReport cannot contain forbidden fields: "
                f"{names}"
            )

    @property
    def id(self) -> str:
        return self.report_id
