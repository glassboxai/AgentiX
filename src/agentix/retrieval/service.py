"""Independent persistent hybrid retrieval; candidates never authorize execution.

All operations are serialized per instance. Multiple writer processes/instances
must be coordinated by the caller. ChromaDB and provider failures remain explicit.
No generated code is imported, executed or discovered by this module.
"""

import hashlib
import json
import logging
import math
import threading
import time
import uuid
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import asdict
from pathlib import Path
from typing import Any

from . import policy
from .contracts import (
    DescriptorSource,
    EmbeddingProvider,
    KeywordProvider,
    SearchResult,
    SyncReport,
    ToolDescriptor,
    validate_keywords,
)
from .lexical import bm25

logger = logging.getLogger(__name__)


class ToolRetriever:
    """Coordinate storage, local model boundaries and hybrid candidate ranking.

    Chroma is initialized only on explicit construction. Providers are injected;
    default Ollama adapters are composed by the caller. No global handlers or
    agent wiring are changed. Use a dedicated database directory for this index.
    """

    def __init__(
        self,
        path: str | Path,
        embeddings: EmbeddingProvider,
        keyword_generator: KeywordProvider,
        *,
        collection_name: str = "agentix_tools",
        descriptor_source: DescriptorSource | None = None,
    ) -> None:
        """Open a cosine collection and reject incompatible model/schema identities.

        Unbound construction creates storage without inference. An explicitly bound
        descriptor source performs its first sync, including embeddings. The first write
        establishes embedding dimensions. Raise ValueError for incompatible indexes;
        underlying storage exceptions are propagated.
        """
        import chromadb
        from chromadb.config import Settings

        self.embeddings = embeddings
        self.keyword_generator = keyword_generator
        self._lock = threading.RLock()
        self._source = descriptor_source
        self.last_sync_report: SyncReport | None = None
        if not isinstance(embeddings.model_id, str) or not embeddings.model_id.strip():
            raise ValueError("Embedding model identity is required")
        self._client = chromadb.PersistentClient(
            path=str(path), settings=Settings(anonymized_telemetry=False)
        )
        self._collection = self._client.get_or_create_collection(
            name=collection_name,
            embedding_function=None,
            metadata={
                "embedding_model": embeddings.model_id,
                "schema": policy.INDEX_SCHEMA_VERSION,
            },
            configuration={"hnsw": {"space": "cosine"}},
        )
        metadata = self._collection.metadata or {}
        if (
            metadata.get("embedding_model") != embeddings.model_id
            or metadata.get("schema") != policy.INDEX_SCHEMA_VERSION
            or self._collection.configuration.get("hnsw", {}).get("space") != "cosine"
        ):
            raise ValueError("Index model or schema is incompatible; rebuild into a separate index")
        logger.info(
            "event=index_opened model=%s count=%d",
            self._model_tag(embeddings),
            self._collection.count(),
        )

        self._bind_source()
        if self._source is not None:
            self.synchronize()

    def _bind_source(self) -> None:
        """Persist source identity and refuse unrelated or unbound reuse of an owned index."""
        metadata = self._collection.metadata or {}
        bound = metadata.get("descriptor_source")
        if self._source is None:
            if bound is not None:
                raise ValueError("This index requires its bound descriptor source")
            return
        identity = self._source.identity
        if (
            not isinstance(identity, str)
            or not identity
            or len(identity) > policy.MAX_TOOL_ID_CHARACTERS
        ):
            raise ValueError("A bounded descriptor source identity is required")
        if bound is not None and bound != identity:
            raise ValueError("Index descriptor source differs from the requested source")
        if bound is None:
            if self._collection.count():
                raise ValueError("Binding a source requires a dedicated empty index")
            self._collection.modify(metadata={**metadata, "descriptor_source": identity})

    def synchronize(self) -> SyncReport:
        """Reconcile a complete authoritative snapshot before serving catalog candidates.

        Remove deleted/rejected entries, embed only new/changed descriptors and keep
        unchanged vectors. Scan/provider/storage failures propagate and prevent search;
        partial writes are retried on the next sync. No transaction or watcher is claimed.
        """
        with self._operation("catalog_sync") as operation:
            if self._source is None:
                raise ValueError("Synchronization requires a descriptor source")
            started = time.perf_counter()
            snapshot = self._source.snapshot()
            desired = {item.tool_id: item for item in snapshot.descriptors}
            if len(desired) != len(snapshot.descriptors):
                raise ValueError("Descriptor source returned duplicate tool IDs")
            for item in desired.values():
                self._payload(item)
            self._event(
                operation,
                "catalog_scan",
                "finished",
                started=started,
                count=len(desired),
                rejected=len(snapshot.rejected),
            )
            for entry in snapshot.rejected:
                self._event(
                    operation,
                    "catalog_entry",
                    "rejected",
                    level=logging.WARNING,
                    tool_hash=hashlib.sha256(entry.tool_id.encode()).hexdigest()[
                        : policy.LOG_TOOL_HASH_CHARACTERS
                    ],
                    reason=entry.reason,
                )
            reconcile_started = time.perf_counter()
            stored = self._collection.get(include=["metadatas"])
            existing = {
                key: ToolDescriptor(**json.loads(metadata["descriptor"]))
                for key, metadata in zip(stored["ids"], stored["metadatas"], strict=True)
            }
            removed = sorted(existing.keys() - desired.keys())
            if removed:
                started = time.perf_counter()
                self._collection.delete(ids=removed)
                self._event(
                    operation, "catalog_delete", "finished", started=started, count=len(removed)
                )
            added = updated = unchanged = 0
            for key, item in sorted(desired.items()):
                if existing.get(key) == item:
                    unchanged += 1
                    continue
                self._store_descriptor(item, operation)
                if key in existing:
                    updated += 1
                else:
                    added += 1
            report = SyncReport(added, updated, len(removed), unchanged, snapshot.rejected)
            self.last_sync_report = report
            self._event(
                operation,
                "catalog_reconcile",
                "finished",
                started=reconcile_started,
                added=added,
                updated=updated,
                removed=len(removed),
                unchanged=unchanged,
                rejected=len(snapshot.rejected),
            )
            return report

    @staticmethod
    def _model_tag(provider: Any) -> str:
        """Bound and sanitize configured model identifiers before diagnostics."""
        return (
            str(getattr(provider, "model_id", "unknown"))
            .encode("unicode_escape")
            .decode()[: policy.MAX_LOG_MODEL_ID_CHARACTERS]
        )

    @contextmanager
    def _operation(self, stage: str) -> Iterator[str]:
        """Serialize operations and log safe outcomes, elapsed milliseconds and correlation."""
        operation = uuid.uuid4().hex
        started = time.perf_counter()
        with self._lock:
            self._event(operation, stage, "started")
            try:
                yield operation
            except Exception as exc:
                self._event(
                    operation,
                    stage,
                    "failed",
                    started=started,
                    level=logging.ERROR,
                    error_type=type(exc).__name__,
                )
                raise
            else:
                self._event(operation, stage, "finished", started=started)

    @staticmethod
    def _event(
        operation: str,
        stage: str,
        outcome: str,
        *,
        started: float | None = None,
        level: int = logging.INFO,
        **details: Any,
    ) -> None:
        """Emit maintained diagnostic fields only; never accept provider payloads."""
        duration = (
            0.0
            if started is None
            else (time.perf_counter() - started) * policy.MILLISECONDS_PER_SECOND
        )
        logger.log(
            level,
            "operation=%s stage=%s outcome=%s duration_ms=%.3f details=%s",
            operation,
            stage,
            outcome,
            duration,
            details,
        )

    def _vectors(self, texts: list[str]) -> list[list[float]]:
        """Validate finite nonzero vectors and persist the initial index dimension.

        Raise ValueError on malformed output or model/dimension changes. Provider
        errors propagate; storing a dimension never constitutes a successful upsert.
        """
        vectors = self.embeddings.embed(texts)
        if not isinstance(vectors, list) or len(vectors) != len(texts):
            raise ValueError("Embedding batch shape is invalid")
        dimension = None
        for vector in vectors:
            if not isinstance(vector, list) or not vector:
                raise ValueError("Embedding vectors must be nonempty lists")
            if any(
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                for value in vector
            ) or not any(value != 0 for value in vector):
                raise ValueError("Embedding values must be finite with nonzero norm")
            if dimension is not None and dimension != len(vector):
                raise ValueError("Embedding dimensions differ within batch")
            dimension = len(vector)
        metadata = self._collection.metadata or {}
        if metadata.get("embedding_model") != self.embeddings.model_id:
            raise ValueError("Embedding model changed")
        if metadata.get("dimension", dimension) != dimension:
            raise ValueError("Embedding dimension changed")
        if "dimension" not in metadata:
            self._collection.modify(metadata={**metadata, "dimension": dimension})
        return vectors

    @staticmethod
    def _payload(descriptor: ToolDescriptor) -> tuple[str, str]:
        """Validate and snapshot JSON metadata, returning storage and searchable text."""
        if not isinstance(descriptor, ToolDescriptor):
            raise ValueError("A ToolDescriptor is required")
        data = asdict(descriptor)
        for key in (
            "tool_id",
            "name",
            "description",
            "entrypoint",
            "artifact_ref",
            "contract_digest",
        ):
            if (
                not isinstance(data[key], str)
                or not data[key].strip()
                or len(data[key]) > policy.MAX_DESCRIPTOR_FIELD_CHARACTERS
            ):
                raise ValueError("Descriptor text fields must be nonempty and bounded")
        if len(data["tool_id"]) > policy.MAX_TOOL_ID_CHARACTERS:
            raise ValueError("Tool identifier exceeds limit")
        if not isinstance(data["input_schema"], dict) or not isinstance(
            data["output_schema"], dict
        ):
            raise ValueError("Schemas must be JSON objects")
        validate_keywords(data["keywords"])
        payload = json.dumps(data, allow_nan=False, sort_keys=True)
        if len(payload.encode("utf-8")) > policy.MAX_DESCRIPTOR_BYTES:
            raise ValueError(
                f"Descriptor exceeds {policy.MAX_DESCRIPTOR_BYTES // policy.BYTES_PER_KIB} KiB"
            )
        document = " ".join(
            [
                data["name"],
                data["description"],
                data["entrypoint"],
                json.dumps(data["input_schema"]),
                json.dumps(data["output_schema"]),
                " ".join(data["keywords"]),
            ]
        )
        return payload, document

    def upsert(self, descriptor: ToolDescriptor) -> None:
        """Insert or replace a descriptor and vector by ID; never inspect artifact paths."""
        with self._operation("upsert") as operation:
            self._store_descriptor(descriptor, operation)

    def _store_descriptor(self, descriptor: ToolDescriptor, operation: str) -> None:
        """Persist one validated descriptor/vector using the owning operation's diagnostics."""
        payload, document = self._payload(descriptor)
        started = time.perf_counter()
        vectors = self._vectors([document])
        self._event(
            operation,
            "embedding",
            "finished",
            started=started,
            model=self._model_tag(self.embeddings),
            count=1,
        )
        started = time.perf_counter()
        self._collection.upsert(
            ids=[descriptor.tool_id],
            documents=[document],
            embeddings=vectors,
            metadatas=[{"descriptor": payload}],
        )
        self._event(operation, "persistence", "finished", started=started, count=1)

    def delete(self, tool_id: str) -> None:
        """Idempotently remove an explicit ID; invalid IDs raise ValueError."""
        with self._operation("delete") as operation:
            if (
                not isinstance(tool_id, str)
                or not tool_id.strip()
                or len(tool_id) > policy.MAX_TOOL_ID_CHARACTERS
            ):
                raise ValueError("A bounded nonempty tool ID is required")
            started = time.perf_counter()
            self._collection.delete(ids=[tool_id])
            self._event(operation, "persistence", "finished", started=started, requested_count=1)

    def search(
        self,
        query: str,
        keywords: list[str] | None = None,
        limit: int = policy.DEFAULT_SEARCH_LIMIT,
    ) -> list[SearchResult]:
        """Return hybrid candidates, not approvals, with at most limit entries.

        A nonempty query is bounded to 32 KiB and limit to 1..100. Empty storage
        avoids all model calls. Keyword generation failure degrades explicitly;
        embedding/storage errors propagate. Bound sources synchronize before querying.
        Changes after that scan are observed on the next search; no watcher is started.
        No score threshold is imposed.
        """
        with self._operation("search") as operation:
            if (
                not isinstance(query, str)
                or not query.strip()
                or len(query.encode("utf-8")) > policy.MAX_QUERY_BYTES
            ):
                raise ValueError(
                    f"A nonempty query of at most {policy.MAX_QUERY_BYTES // policy.BYTES_PER_KIB} KiB is required"
                )
            if (
                isinstance(limit, bool)
                or not isinstance(limit, int)
                or not policy.MIN_SEARCH_LIMIT <= limit <= policy.MAX_SEARCH_LIMIT
            ):
                raise ValueError(
                    f"Limit must be an integer from {policy.MIN_SEARCH_LIMIT} to {policy.MAX_SEARCH_LIMIT}"
                )
            supplied = validate_keywords([] if keywords is None else keywords)
            if self._source is not None:
                self.synchronize()
            started = time.perf_counter()
            snapshot = self._collection.get(include=["documents", "metadatas"])
            count = len(snapshot["ids"])
            self._event(operation, "snapshot", "finished", started=started, count=count)
            if not count:
                return []
            started = time.perf_counter()
            mode = "hybrid"
            try:
                generated = validate_keywords(self.keyword_generator.generate(query))
                self._event(
                    operation,
                    "keyword_generation",
                    "finished",
                    started=started,
                    count=len(generated),
                    model=self._model_tag(self.keyword_generator),
                )
            except Exception as exc:
                generated, mode = [], "keyword_fallback"
                self._event(
                    operation,
                    "keyword_generation",
                    "degraded",
                    started=started,
                    level=logging.WARNING,
                    error_type=type(exc).__name__,
                    model=self._model_tag(self.keyword_generator),
                )
            documents = dict(zip(snapshot["ids"], snapshot["documents"], strict=True))
            descriptors = {
                key: ToolDescriptor(**json.loads(meta["descriptor"]))
                for key, meta in zip(snapshot["ids"], snapshot["metadatas"], strict=True)
            }
            candidate_limit = min(
                count, max(policy.MIN_BRANCH_CANDIDATES, policy.BRANCH_CANDIDATE_MULTIPLIER * limit)
            )
            started = time.perf_counter()
            lexical = bm25(documents, " ".join([query, *supplied, *generated]))
            lexical_ids = sorted(lexical, key=lambda key: (-lexical[key], key))[:candidate_limit]
            self._event(operation, "lexical", "finished", started=started, count=len(lexical_ids))
            started = time.perf_counter()
            vector = self._vectors([query])
            self._event(
                operation,
                "embedding",
                "finished",
                started=started,
                model=self._model_tag(self.embeddings),
                count=1,
            )
            started = time.perf_counter()
            response = self._collection.query(
                query_embeddings=vector, n_results=candidate_limit, include=["distances"]
            )
            semantic = {
                key: 1.0 - distance
                for key, distance in zip(response["ids"][0], response["distances"][0], strict=True)
            }
            semantic_ids = sorted(semantic, key=lambda key: (-semantic[key], key))
            self._event(operation, "semantic", "finished", started=started, count=len(semantic_ids))
            started = time.perf_counter()
            scores: dict[str, float] = {}
            for branch in (semantic_ids, lexical_ids):
                for rank, key in enumerate(branch, 1):
                    scores[key] = scores.get(key, 0) + 1 / (policy.RRF_RANK_CONSTANT + rank)
            ranked = sorted(scores, key=lambda key: (-scores[key], key))[:limit]
            for rank, key in enumerate(ranked, 1):
                self._event(
                    operation,
                    "ranking",
                    "candidate",
                    level=logging.DEBUG,
                    rank=rank,
                    tool_hash=hashlib.sha256(key.encode()).hexdigest()[
                        : policy.LOG_TOOL_HASH_CHARACTERS
                    ],
                    rrf=scores[key],
                    semantic=semantic.get(key),
                    lexical=lexical.get(key),
                )
            if ranked:
                selected = ranked[0]
                self._event(
                    operation,
                    "ranking",
                    "selected",
                    level=logging.INFO,
                    rank=1,
                    tool_hash=hashlib.sha256(selected.encode()).hexdigest()[
                        : policy.LOG_TOOL_HASH_CHARACTERS
                    ],
                    rrf=scores[selected],
                )
            self._event(
                operation, "ranking", "finished", started=started, count=len(ranked), mode=mode
            )
            return [
                SearchResult(
                    descriptors[key],
                    rank,
                    scores[key],
                    semantic.get(key),
                    lexical.get(key),
                    mode,
                    self.keyword_generator.model_id,
                )
                for rank, key in enumerate(ranked, 1)
            ]
