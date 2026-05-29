"""Passive physics models for GENUS_CORE v0.2.0."""

from dataclasses import dataclass, field
from typing import Any

from genus_core import SCHEMA_VERSION
from genus_core.ids import new_id
from genus_core.time import utc_now_iso

ALLOWED_METRIC_NAMES = frozenset({"pressure", "inhibition", "stability"})
EXCLUDED_FIRST_METRIC_NAMES = frozenset({"cost", "potential"})
ALLOWED_METRIC_LEVELS = frozenset({"none", "low", "medium", "high"})
ALLOWED_ASSESSMENT_STATUS = frozenset(
    {"assessed", "insufficient_input", "not_applicable"}
)
ALLOWED_METRIC_OUTPUT_FIELDS = frozenset(
    {
        "metric_name",
        "level",
        "assessment_status",
        "explanation",
        "source_state_id",
        "source_evidence_ids_json",
    }
)
FORBIDDEN_METRIC_OUTPUT_FIELDS = frozenset(
    {
        "score",
        "priority",
        "rank",
        "recommendation",
        "permission",
        "decision",
        "approval",
        "action",
        "execute",
        "candidate",
        "transition",
        "constraint",
        "reaction",
        "memory_write",
        "truth",
    }
)
FORBIDDEN_PASSIVE_REPORT_FIELDS = FORBIDDEN_METRIC_OUTPUT_FIELDS.union(
    {
        "truth_status",
        "world_truth",
        "policy",
        "allow",
        "block",
        "approved",
        "rejected_by_policy",
        "memory",
        "memory_object",
    }
)


def _validate_status_level(metric_output: dict[str, Any]) -> None:
    status = metric_output["assessment_status"]
    level = metric_output["level"]
    if status in {"insufficient_input", "not_applicable"} and level != "none":
        raise ValueError(f"{status} requires level=none")


@dataclass(frozen=True)
class PassiveMetricSnapshot:
    source_state_id: str
    source_evidence_ids_json: list[str]
    metrics_json: list[dict[str, Any]]
    snapshot_id: str = field(default_factory=lambda: new_id("pms_"))
    created_at: str = field(default_factory=utc_now_iso)
    schema_version: str = SCHEMA_VERSION

    def __post_init__(self) -> None:
        if not isinstance(self.source_state_id, str) or not self.source_state_id.strip():
            raise ValueError("PassiveMetricSnapshot requires source_state_id")
        if not isinstance(self.source_evidence_ids_json, list):
            raise TypeError("source_evidence_ids_json must be a list")
        if not self.metrics_json:
            raise ValueError("PassiveMetricSnapshot requires metric outputs")

        for metric_output in self.metrics_json:
            if set(metric_output) != ALLOWED_METRIC_OUTPUT_FIELDS:
                raise ValueError("Passive metric output fields must match allowed shape")
            forbidden = FORBIDDEN_METRIC_OUTPUT_FIELDS.intersection(metric_output)
            if forbidden:
                names = ", ".join(sorted(forbidden))
                raise ValueError(f"Passive metric output cannot contain: {names}")
            if metric_output["metric_name"] not in ALLOWED_METRIC_NAMES:
                raise ValueError(f"Invalid passive metric name: {metric_output['metric_name']}")
            if metric_output["level"] not in ALLOWED_METRIC_LEVELS:
                raise ValueError(f"Invalid passive metric level: {metric_output['level']}")
            if metric_output["assessment_status"] not in ALLOWED_ASSESSMENT_STATUS:
                raise ValueError(
                    "Invalid passive metric assessment_status: "
                    f"{metric_output['assessment_status']}"
                )
            if metric_output["source_state_id"] != self.source_state_id:
                raise ValueError("Metric output source_state_id must match snapshot")
            if (
                metric_output["source_evidence_ids_json"]
                != self.source_evidence_ids_json
            ):
                raise ValueError("Metric output source evidence ids must match snapshot")
            _validate_status_level(metric_output)

    @property
    def id(self) -> str:
        return self.snapshot_id


@dataclass(frozen=True)
class PassiveMetricReport:
    source_snapshot_id: str
    summary: str
    payload_json: dict[str, Any] = field(default_factory=dict)
    report_id: str = field(default_factory=lambda: new_id("pmr_"))
    created_at: str = field(default_factory=utc_now_iso)
    schema_version: str = SCHEMA_VERSION

    def __post_init__(self) -> None:
        if (
            not isinstance(self.source_snapshot_id, str)
            or not self.source_snapshot_id.strip()
        ):
            raise ValueError("PassiveMetricReport requires source_snapshot_id")
        if not isinstance(self.summary, str) or not self.summary.strip():
            raise ValueError("PassiveMetricReport requires summary")
        forbidden = FORBIDDEN_PASSIVE_REPORT_FIELDS.intersection(self.payload_json)
        if forbidden:
            names = ", ".join(sorted(forbidden))
            raise ValueError(f"PassiveMetricReport cannot contain forbidden fields: {names}")

    @property
    def id(self) -> str:
        return self.report_id
