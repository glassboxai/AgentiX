"""GUI composition boundary for catalog retrieval with private provider clients.

One service serializes index operations within the GUI process. Each owner retains
its own retriever/providers in a handle; startup clients are not shared with owners.
Do not run the standalone index writer concurrently from another process.
"""

import logging
import os
import threading
import time
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from agentix.diagnostics import log_event
from agentix.storage.catalog import ToolCatalog

from . import policy
from .catalog import CatalogToolSource
from .contracts import SearchResult
from .ollama import OllamaClient, OllamaEmbeddings, OllamaKeywords
from .service import ToolRetriever

logger = logging.getLogger(__name__)


@dataclass
class RetrieverHandle:
    """Own one session's retriever and the physical catalog identity it serves."""

    retriever: Any = None  # Session-private providers; released with session state.
    root: str = ""  # Normalized absolute root, not a browser-supplied path.


def catalog_retriever(catalog: ToolCatalog) -> ToolRetriever:
    """Compose local providers and the same dedicated index used by the sync CLI."""
    client = OllamaClient()
    return ToolRetriever(
        Path(catalog.root).parent / "tool_registry",
        OllamaEmbeddings(client),
        OllamaKeywords(client),
        descriptor_source=CatalogToolSource(catalog),
    )


class GuiToolRetrieval:
    """Serialize one GUI's catalog access without retaining a shared model client."""

    def __init__(self, *, factory: Callable = catalog_retriever) -> None:
        """Inject explicit composition; construction performs no inference or filesystem IO."""
        self.factory = factory
        self.lock = threading.RLock()
        self.startup_message = "The tool index will synchronize on the first search."

    def initialize(self, catalog: ToolCatalog) -> str:
        """Load at GUI startup; record safe failure and allow later search to retry."""
        started = time.perf_counter()
        try:
            with self.lock:
                temporary = self.factory(catalog)
                report = temporary.last_sync_report
                count = report.added + report.updated + report.unchanged if report else 0
            self.startup_message = f"Tool index ready: {count} tools."
            outcome, error_type = "ready", ""
        except Exception as error:
            self.startup_message = "Tool index unavailable. Retry with Generate application."
            outcome, error_type = "unavailable", type(error).__name__
        logger.info(
            "event=gui_retrieval_startup outcome=%s duration_ms=%.3f error_type=%s",
            outcome,
            (time.perf_counter() - started) * policy.MILLISECONDS_PER_SECOND,
            error_type,
        )
        return self.startup_message

    def search(
        self, catalog: ToolCatalog, handle: RetrieverHandle, query: str, limit: int
    ) -> list[SearchResult]:
        """Synchronize/search through an owner-private client under the common index lock.

        Failures propagate to the controller for safe UI reporting. A changed catalog
        root creates a new bound client rather than reusing another source's index.
        """
        root = os.path.normcase(str(Path(catalog.root).resolve()))
        with self.lock:
            if handle.retriever is None or handle.root != root:
                log_event(logger, "retrieval_handle_creating", level=logging.DEBUG)
                handle.retriever = self.factory(catalog)
                handle.root = root
                log_event(logger, "retrieval_handle_ready", level=logging.DEBUG)
            else:
                log_event(logger, "retrieval_handle_reused", level=logging.DEBUG)
            return handle.retriever.search(query, limit=limit)
