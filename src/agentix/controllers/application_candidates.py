"""Server-owned application candidate snapshots and exact dependency selection.

Selection is a generation constraint, not an approval grant. Existing catalog
eligibility and current approved source bytes are rechecked at acceptance and use.
"""

import hashlib
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any, Final
from uuid import uuid4

from agentix.retrieval import SearchResult
from agentix.retrieval.gui import RetrieverHandle
from agentix.storage.application_catalog import ApprovedTool, CatalogDependencyError

CANDIDATE_SUMMARY_CHARACTERS: Final[int] = 240  # Bounded first-line text in the candidate table.


@dataclass(frozen=True)
class AcceptedCandidates:
    """Bind accepted dependencies to the exact application description on the server."""

    query: str  # Original user description, never logged.
    expected: dict[str, str]  # Tool IDs mapped to raw source SHA-256 fingerprints.
    identity: str = ""  # Search revision for generation-log correlation, not a capability.


@dataclass(frozen=True)
class CandidateSelection:
    """Present one immutable search revision; its identity is checked with owner/token."""

    identity: str  # Search revision identifier; never sufficient without owner/session checks.
    query: str  # Exact server-held description for acceptance comparison; omitted from logs.
    limit: int  # Validated result count requested for this revision.
    results: tuple[
        SearchResult, ...
    ]  # Ordered candidates returned by retrieval without silent eligibility filtering.
    rows: tuple[
        tuple[str, str, float, str], ...
    ]  # Bounded display metadata, escaped by the frontend renderer.
    ready: bool  # All candidates currently eligible; no application execution approval is granted.
    message: str  # Safe owner-visible status without provider error bodies.

    eligible_ids: frozenset[str] = (
        frozenset()
    )  # Snapshot eligibility, independent of presentation labels.

    @property
    def expected(self) -> dict[str, str]:
        """Return a fresh mapping of candidate identities to their source fingerprints."""
        return {item.descriptor.tool_id: item.descriptor.contract_digest for item in self.results}

    def selected_expected(self, selected_ids: list[str] | None) -> dict[str, str]:
        """Validate a nonempty browser subset against this snapshot and its eligibility."""
        chosen = list(self.expected) if selected_ids is None else selected_ids
        if (
            not isinstance(chosen, list)
            or not chosen
            or any(not isinstance(item, str) for item in chosen)
            or len(set(chosen)) != len(chosen)
            or not set(chosen).issubset(self.expected)
        ):
            raise ValueError("Select at least one tool from the current candidates.")
        if not set(chosen).issubset(self.eligible_ids):
            raise ValueError(
                "Selected tools require current reusable approval. Review them in Tools and search again."
            )
        return {key: value for key, value in self.expected.items() if key in chosen}


@dataclass
class CandidateState:
    """Retain retrieval state only within the owning application session."""

    handle: RetrieverHandle = field(default_factory=RetrieverHandle)
    revision: str = ""  # Latest attempted revision; replaced on edits, acceptance and cleanup.
    selection: CandidateSelection | None = (
        None  # Current preview, consumed on acceptance or invalidation.
    )

    def invalidate(self) -> str:
        """Clear a displayed selection and advance its revision before asynchronous work."""
        self.revision = uuid4().hex
        self.selection = None
        return self.revision


class SelectedToolRegistry:
    """Constrain an existing approval registry to exactly the accepted tool names."""

    def __init__(self, registry: Any, expected: Mapping[str, str]) -> None:
        """Copy server-owned expected source identities; never accept browser descriptors."""
        self.registry, self.expected = registry, dict(expected)

    def resolve(self) -> dict[str, ApprovedTool]:
        """Revalidate eligibility and exact source hashes, returning only selected tools."""
        if not self.expected:
            raise CatalogDependencyError(
                "Search for tool candidates and accept a nonempty list first."
            )
        available = {tool.tool_name: (role, tool) for role, tool in self.registry.resolve().items()}
        selected = {}
        for name, digest in self.expected.items():
            entry = available.get(name)
            if entry is None or hashlib.sha256(entry[1].code).hexdigest() != digest:
                raise CatalogDependencyError(
                    f"Candidate {name} changed or has no current reusable approval. Search again after approving it in Tools."
                )
            role, tool = entry
            selected[role] = tool
        return selected

    def recheck(self, expected: Mapping[str, ApprovedTool]) -> None:
        """Reject source/grant changes without introducing unrelated catalog dependencies."""
        if self.resolve() != dict(expected):
            raise CatalogDependencyError("Accepted application candidates changed; search again.")


def _candidate_status(reason: str | None) -> str:
    """Map one bounded ineligibility reason to an owner-actionable row label."""
    if not reason:
        return "Approve or refresh in Tools"
    lowered = reason.lower()
    if "approval" in lowered or "acceptance" in lowered:
        return "Approve or refresh in Tools"
    return "Not portable for applications"


def present_candidates(
    identity: str, query: str, limit: int, results: list[SearchResult], registry: Any
) -> CandidateSelection:
    """Mark every returned candidate's current eligibility without silently filtering it."""
    try:
        available = {tool.tool_name: tool for tool in registry.resolve().values()}
    except CatalogDependencyError:
        available = {}
    reasons: dict[str, str] = {}
    skip_reasons = getattr(registry, "skip_reasons", None)
    if callable(skip_reasons):
        try:
            reasons = dict(skip_reasons())
        except CatalogDependencyError:
            reasons = {}
    rows, ready = [], bool(results)
    eligible_ids: set[str] = set()  # IDs passing current approval and source checks.
    blocked: list[str] = []  # Reasons behind ineligible rows, for an accurate message.
    for item in results:
        descriptor = item.descriptor
        tool = available.get(descriptor.tool_id)
        valid = (
            tool is not None and hashlib.sha256(tool.code).hexdigest() == descriptor.contract_digest
        )
        ready = ready and valid
        if valid:
            eligible_ids.add(descriptor.tool_id)
        else:
            blocked.append(reasons.get(descriptor.tool_id) or "")
        summary = descriptor.description.strip().splitlines()[0][:CANDIDATE_SUMMARY_CHARACTERS]
        rows.append(
            (
                descriptor.name,
                summary,
                item.score,
                "Ready" if valid else _candidate_status(reasons.get(descriptor.tool_id)),
            )
        )
    approval_blocked = any(
        "approval" in reason.lower() or "acceptance" in reason.lower() for reason in blocked
    )
    message = (
        "Accept these candidates to start application generation."
        if ready
        else "No candidates found."
        if not results
        else "Some candidates lack current reusable approval. Approve them in Tools and search again."
        if approval_blocked
        else "Some candidates are not portable for applications. Review each candidate reason and extend "
        "portable_modules.json in the AgentiX data folder if the module is safe."
    )
    message = f"Found {len(results)} candidate(s) with limit {limit}. " + message
    if any(item.mode == "keyword_fallback" for item in results):
        message += " Keyword generation unavailable; original query terms were used."
    return CandidateSelection(
        identity, query, limit, tuple(results), tuple(rows), ready, message, frozenset(eligible_ids)
    )
