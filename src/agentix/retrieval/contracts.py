"""Typed retrieval contracts and static Python descriptor extraction.

Descriptors are search metadata, never execution capabilities. Source is parsed
with AST only; no imports, annotation evaluation or fixture execution occurs.
"""

import ast
import hashlib
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Any, Protocol

from . import policy


class EmbeddingProvider(Protocol):
    """Inject a stable model identity and batch embedding boundary."""

    model_id: str

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Return one finite, fixed-dimension vector per text or raise an error."""
        ...


class KeywordProvider(Protocol):
    """Inject local generation independently from embedding and storage."""

    model_id: str

    def generate(self, query: str) -> list[str]:
        """Return at most twenty bounded keyword strings, or raise an error."""
        ...


@dataclass(frozen=True)
class ToolDescriptor:
    """Describe one canonical public function without approval or test claims.

    Schemas are JSON data. Artifact references are opaque catalog identifiers,
    not filesystem access grants. The digest identifies the indexed contract.
    """

    tool_id: str  # Stable storage key, at most 256 characters.
    name: str  # Canonical public function name for agent context.
    description: str  # Functional search text; never an authorization claim.
    entrypoint: str  # Module/function spelling, not an import instruction.
    input_schema: dict[str, Any]  # JSON-compatible parameter/type descriptions.
    output_schema: dict[str, Any]  # JSON-compatible return/type description.
    keywords: list[str]  # At most twenty explicit domain terms.
    artifact_ref: str  # Opaque reference resolved by a future catalog adapter.
    contract_digest: str  # Indexed contract/source identity for stale-entry detection.


@dataclass(frozen=True)
class SearchResult:
    """Return a candidate with one-based rank and non-probabilistic RRF score.

    Semantic score is cosine similarity; lexical score is BM25. A missing branch
    has a None score. Mode is hybrid or keyword_fallback, never authorization.
    """

    descriptor: ToolDescriptor  # Snapshot metadata copied from the index.
    rank: int  # One-based result position for this search.
    score: float  # Equal-weight reciprocal-rank fusion score.
    semantic_score: float | None  # Cosine similarity, absent outside semantic candidates.
    lexical_score: float | None  # BM25 score, absent outside lexical candidates.
    mode: str  # Hybrid success or explicit keyword_fallback.
    keyword_model: str = field(default="", repr=False)


def validate_keywords(value: object) -> list[str]:
    """Validate bounded JSON-style terms and deduplicate case-insensitively.

    Raise ValueError on malformed output; callers distinguish generated failure
    from invalid caller input. No coercion of arbitrary objects is performed.
    """
    if not isinstance(value, list) or len(value) > policy.MAX_KEYWORD_COUNT:
        raise ValueError(f"Keywords must be a list of at most {policy.MAX_KEYWORD_COUNT} strings")
    result, seen = [], set()
    for term in value:
        if (
            not isinstance(term, str)
            or not term.strip()
            or len(term) > policy.MAX_KEYWORD_CHARACTERS
        ):
            raise ValueError(
                f"Keywords must contain nonempty strings of at most {policy.MAX_KEYWORD_CHARACTERS} characters"
            )
        clean = term.strip()
        if clean.casefold() not in seen:
            result.append(clean)
            seen.add(clean.casefold())
    return result


def _annotation(node: ast.expr | None) -> dict[str, str]:
    """Extract Python type spelling and literal Annotated description without eval."""
    if node is None:
        return {"python_type": "Any"}
    if isinstance(node, ast.Subscript) and ast.unparse(node.value).split(".")[-1] == "Annotated":
        parts: Sequence[ast.expr] = (
            node.slice.elts if isinstance(node.slice, ast.Tuple) else [node.slice]
        )
        result = {"python_type": ast.unparse(parts[0])}
        if (
            len(parts) > 1
            and isinstance(parts[1], ast.Constant)
            and isinstance(parts[1].value, str)
        ):
            result["description"] = parts[1].value
        return result
    return {"python_type": ast.unparse(node)}


def descriptor_from_source(name: str, source: str, *, artifact_ref: str) -> ToolDescriptor:
    """Parse a canonical synchronous function into search metadata, never executing it.

    Parameters are the canonical function name, explicit Python source and opaque
    catalog reference. Return a source-bound descriptor; reject ambiguous, missing
    or private entrypoints with ValueError and propagate SyntaxError for bad source.
    """
    tree = ast.parse(source)
    functions = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name]
    if len(functions) != 1 or name.startswith("_"):
        raise ValueError("Exactly one canonical public function is required")
    function = functions[0]
    positional = function.args.posonlyargs + function.args.args
    parameters = positional + function.args.kwonlyargs
    properties = {arg.arg: _annotation(arg.annotation) for arg in parameters}
    required = [arg.arg for arg in positional[: len(positional) - len(function.args.defaults)]]
    required.extend(
        arg.arg
        for arg, default in zip(function.args.kwonlyargs, function.args.kw_defaults, strict=True)
        if default is None
    )
    for arg in (function.args.vararg, function.args.kwarg):
        if arg:
            properties[arg.arg] = {**_annotation(arg.annotation), "variadic": "true"}
    return ToolDescriptor(
        tool_id=name,
        name=name,
        description=ast.get_docstring(function) or ast.get_docstring(tree) or name,
        entrypoint=f"{name}_code.py:{name}",
        input_schema={"type": "object", "properties": properties, "required": required},
        output_schema=_annotation(function.returns),
        keywords=[name],
        artifact_ref=artifact_ref,
        contract_digest=hashlib.sha256(source.encode("utf-8")).hexdigest(),
    )


@dataclass(frozen=True)
class CatalogRejection:
    """Identify an omitted tool and a maintained safe reason code, without source text."""

    tool_id: str  # Catalog directory identifier; never an execution authorization.
    reason: str  # Bounded adapter-owned reason, not a raw exception message.


@dataclass(frozen=True)
class CatalogSnapshot:
    """Represent one complete bounded source scan; unreadable roots must raise."""

    descriptors: tuple[ToolDescriptor, ...]  # Eligible canonical search metadata.
    rejected: tuple[CatalogRejection, ...] = ()  # Entries omitted from this scan.


class DescriptorSource(Protocol):
    """Inject an authoritative descriptor snapshot independently of storage and UI."""

    identity: str  # Stable source identity; persisted to prevent cross-catalog pruning.

    def snapshot(self) -> CatalogSnapshot:
        """Read a complete snapshot or raise; never convert a failed scan to an empty catalog."""
        ...


@dataclass(frozen=True)
class SyncReport:
    """Describe a completed incremental sync; rejected tools cannot remain searchable."""

    added: int  # Newly indexed descriptors in this successful synchronization.
    updated: int  # Existing descriptors whose source or metadata changed.
    removed: int  # Disappeared or rejected entries removed from the owned index.
    unchanged: int  # Descriptors reused without another document embedding.
    rejected: tuple[CatalogRejection, ...]  # Rejected source identities and safe reasons.
