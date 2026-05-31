import re
import tomllib
from pathlib import Path

import genus_core


DECISIONS_INDEX = Path("docs/DECISIONS.md")
DECISION_MODULES = (
    Path("docs/decisions/v0.0.md"),
    Path("docs/decisions/v0.1.md"),
    Path("docs/decisions/v0.2.md"),
    Path("docs/decisions/v0.3.md"),
)
EXPECTED_DECISION_TITLES = {
    "0001": "Start smaller than Full Cognitive Physics",
    "0002": "Observation is first true GENUS act",
    "0003": "Ledger is lineage, not truth",
    "0004": "Report has no decision power",
    "0005": "Function-first, responsibility-first",
    "0006": "v0.0.1 builds no action path",
    "0007": "v0.0.2 is Foundation Hardening only",
    "0008": "v0.0.3 centralizes minimal sentence types",
    "0009": "v0.0.4 hardens observation classification",
    "0010": "v0.0.5 hardens the Evidence boundary",
    "0011": "v0.0.6 constrains Ledger to real lineage only",
    "0012": "v0.0.7 hardens Belief derivation",
    "0013": "v0.0.8 hardens Report as descriptive-only",
    "0014": "v0.0.9 audits foundation freeze readiness",
    "0015": "v0.1.0 freezes the passive epistemic core",
    "0016": "v0.1.1 defines Pre-Physics requirements only",
    "0017": "v0.1.2 defines passive metric vocabulary only",
    "0018": "v0.1.3 defines passive metric acceptance criteria only",
    "0019": "v0.1.4 adds a minimal CI release integrity gate",
    "0020": "v0.1.5 defines passive metric output shape only",
    "0021": "v0.1.6 audits passive metric safety before implementation",
    "0022": "v0.1.7 requires concrete Ledger targets",
    "0023": "v0.1.8 finalizes CI release integrity",
    "0024": "v0.1.9 uses observation-only memory request names",
    "0025": "v0.1.10 anchors the GENUS charter and safety boundary",
    "0026": "v0.2.0 activates passive Physics narrowly",
    "0027": "v0.2.1 clarifies passive Physics boundary language",
    "0028": "v0.3.0 adds passive transition preview",
    "0029": "v0.3.1 audits passive transition report language",
    "0030": "v0.4.0 is planned as passive boundary relevance, not evaluation",
    "0031": "v0.3.2 governs build structure",
    "0032": "v0.3.3 modularizes quality gates first",
    "0033": "v0.3.4 aligns artifact contracts",
    "0034": "v0.4.0 spec must follow artifact contracts",
    "0035": "v0.3.6 modularizes vocabulary",
    "0036": "v0.3.7 modularizes the roadmap",
    "0037": "v0.3.8 freezes historical specs as references",
    "0038": "v0.3.9 modularizes Ledger lineage tests",
}


def _module_text() -> str:
    return "\n".join(path.read_text(encoding="utf-8") for path in DECISION_MODULES)


def test_decisions_index_is_active_map_not_monolith() -> None:
    text = DECISIONS_INDEX.read_text(encoding="utf-8")

    assert len(text.splitlines()) <= 260
    assert "Decisions govern how GENUS may be built." in text
    assert "Active Decision Map" in text
    assert "Epistemic boundary: Observation, Evidence, Ledger, Belief, and Report" in text
    assert "No-action boundary: Report is not Decision; no MemoryWrite or Reaction exists." in text
    assert "Capability order: Foundation -> passive Physics -> passive transition preview -> boundary relevance spec." in text
    assert "v0.4.0 constraint: Boundary Relevance, not Boundary Evaluation." in text
    assert "## Decision 0001" not in text


def test_decisions_index_links_all_modular_decision_files() -> None:
    text = DECISIONS_INDEX.read_text(encoding="utf-8")

    for path in DECISION_MODULES:
        assert path.as_posix() in text
        assert path.exists()


def test_decision_numbers_exist_exactly_once_in_modules() -> None:
    headings = re.findall(r"^## Decision (\d{4})", _module_text(), flags=re.MULTILINE)

    assert headings == [f"{number:04d}" for number in range(1, 39)]
    assert len(headings) == len(set(headings)) == 38


def test_decision_headings_keep_expected_titles() -> None:
    module_text = _module_text()

    for number, title in EXPECTED_DECISION_TITLES.items():
        assert re.search(
            rf"^## Decision {number} .+{re.escape(title)}$",
            module_text,
            flags=re.MULTILINE,
        )


def test_decisions_modularization_updates_active_version_without_schema_change() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["version"] == "0.3.9"
    assert genus_core.__version__ == "0.3.9"
    assert genus_core.SCHEMA_VERSION == "genus.foundation.v0.0.1"
