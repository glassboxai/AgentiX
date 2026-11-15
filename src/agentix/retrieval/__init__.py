"""Public independent tool retrieval API; importing it performs no model or DB I/O."""

from .catalog import CatalogToolSource
from .contracts import (
    CatalogRejection,
    CatalogSnapshot,
    DescriptorSource,
    EmbeddingProvider,
    KeywordProvider,
    SearchResult,
    SyncReport,
    ToolDescriptor,
    descriptor_from_source,
)
from .ollama import OllamaClient, OllamaEmbeddings, OllamaKeywords
from .service import ToolRetriever

__all__ = [
    "CatalogToolSource",
    "CatalogRejection",
    "CatalogSnapshot",
    "DescriptorSource",
    "SyncReport",
    "EmbeddingProvider",
    "KeywordProvider",
    "SearchResult",
    "ToolDescriptor",
    "ToolRetriever",
    "descriptor_from_source",
    "OllamaClient",
    "OllamaEmbeddings",
    "OllamaKeywords",
]
