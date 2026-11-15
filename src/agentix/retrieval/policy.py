"""Named retrieval policies, algorithm parameters and measurement units.

Values preserve the approved RAG-001 behavior. Limits with equal numeric values
remain separate when their meaning or units differ. These internal constants are
not a runtime configuration API. Changing INDEX_SCHEMA_VERSION requires an
explicit storage compatibility decision; ranking tuning does not change schema.
"""

from typing import Final

# Unit conversions used for byte limits and monotonic elapsed-time reporting.
BYTES_PER_KIB: Final[int] = 1_024
BYTES_PER_MIB: Final[int] = BYTES_PER_KIB**2
MILLISECONDS_PER_SECOND: Final[int] = 1_000

# Public search bounds and default result count, measured in tool candidates.
DEFAULT_SEARCH_LIMIT: Final[int] = 5
MIN_SEARCH_LIMIT: Final[int] = 1
MAX_SEARCH_LIMIT: Final[int] = 100
MIN_BRANCH_CANDIDATES: Final[int] = 20  # Minimum candidate budget per ranking branch.
BRANCH_CANDIDATE_MULTIPLIER: Final[int] = 4  # Branch budget relative to requested results.
RRF_RANK_CONSTANT: Final[int] = 60  # Reciprocal-rank smoothing from the approved specification.

# BM25 parameters: term-frequency saturation, document-length normalization and IDF smoothing.
BM25_K1: Final[float] = 1.5
BM25_B: Final[float] = 0.75
BM25_IDF_SMOOTHING: Final[float] = 0.5

# Keyword limits are shared by validation, structured generation and prompt text.
MAX_KEYWORD_COUNT: Final[int] = 20
MAX_KEYWORD_CHARACTERS: Final[int] = 100
MAX_KEYWORD_RESPONSE_CHARACTERS: Final[int] = 8_192  # Bound JSON text before parsing it.
KEYWORD_GENERATION_MAX_TOKENS: Final[int] = 512  # Ollama output-token budget.
KEYWORD_GENERATION_TEMPERATURE: Final[float] = (
    0.0  # Zero-temperature request for low-variance term extraction.
)

# Storage and input limits: character bounds and UTF-8 byte bounds have distinct contracts.
INDEX_SCHEMA_VERSION: Final[int] = 1
MAX_TOOL_ID_CHARACTERS: Final[int] = 256
MAX_DESCRIPTOR_FIELD_CHARACTERS: Final[int] = 32_768
MAX_DESCRIPTOR_BYTES: Final[int] = 256 * BYTES_PER_KIB
MAX_QUERY_BYTES: Final[int] = 32 * BYTES_PER_KIB

# Local HTTP resource limits; read one extra byte when probing response overflow.
DEFAULT_OLLAMA_TIMEOUT_SECONDS: Final[float] = 60.0
MAX_HTTP_REQUEST_BYTES: Final[int] = 2 * BYTES_PER_MIB
MAX_HTTP_RESPONSE_BYTES: Final[int] = BYTES_PER_MIB

# Diagnostic display bounds; identifiers remain truncated or hashed before logging.
MAX_LOG_MODEL_ID_CHARACTERS: Final[int] = 120
LOG_TOOL_HASH_CHARACTERS: Final[int] = 16

# Bound read-only scans to the same scale as the current installed tool catalog.
MAX_CATALOG_ENTRIES: Final[int] = 512  # Immediate entries, including non-tool files.
MAX_CATALOG_SOURCE_BYTES: Final[int] = 64 * BYTES_PER_KIB  # Per-tool Python source read bound.
