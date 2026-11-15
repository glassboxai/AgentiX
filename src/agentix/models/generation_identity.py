"""Local Ollama generation identity checks without model execution."""

import json
import re
from collections.abc import Callable
from typing import Any
from urllib.request import HTTPRedirectHandler, ProxyHandler, build_opener

from agentix.models.model_profiles import ModelProfile

_DIGEST = re.compile(r"[a-f0-9]{64}")

CATALOG_TIMEOUT_SECONDS = 5
CATALOG_MAX_BYTES = 1_048_576
CATALOG_READ_BYTES = CATALOG_MAX_BYTES + 1


class _NoRedirects(HTTPRedirectHandler):
    """Reject redirects so local model metadata cannot leave the selected endpoint."""

    def redirect_request(
        self, req: Any, fp: Any, code: int, msg: str, headers: Any, newurl: str
    ) -> None:
        """Deny every redirect without creating a replacement request."""
        return None


def _catalog(endpoint: str) -> dict[str, Any]:
    """Read bounded local model metadata without proxies, inference, or model pulls."""
    with build_opener(ProxyHandler({}), _NoRedirects()).open(
        endpoint.rstrip("/") + "/api/tags", timeout=CATALOG_TIMEOUT_SECONDS
    ) as response:
        body = response.read(CATALOG_READ_BYTES)
    if len(body) > CATALOG_MAX_BYTES:
        raise ValueError("Model catalog exceeds the size limit")
    result = json.loads(body)
    if not isinstance(result, dict) or not isinstance(result.get("models"), list):
        raise ValueError("Invalid model catalog")
    return result


def verify_generation_identity(
    profile: ModelProfile,
    trusted_digest: str,
    *,
    reader: Callable[[str], dict[str, Any]] = _catalog,
) -> str:
    """Require an exact trusted local model digest before generation.

    The check performs a bounded metadata read only. It rejects remote providers,
    absent/malformed baselines, unavailable models, and changed identities.
    """
    profile.validate()
    if (
        profile.provider != "Ollama"
        or not isinstance(trusted_digest, str)
        or not _DIGEST.fullmatch(trusted_digest)
    ):
        raise ValueError("Trusted local generation identity is required")
    try:
        models = reader(profile.endpoint)["models"]
        matches = [
            item for item in models if isinstance(item, dict) and item.get("name") == profile.model
        ]
        digest = matches[0].get("digest") if len(matches) == 1 else None
    except Exception:
        raise ValueError("Local generation identity could not be read") from None
    if not isinstance(digest, str) or not _DIGEST.fullmatch(digest) or digest != trusted_digest:
        raise ValueError("Local generation identity changed or is unavailable")
    return digest


def read_generation_identity(
    profile: ModelProfile, *, reader: Callable[[str], dict[str, Any]] = _catalog
) -> str:
    """Return one current local model digest for explicit user review without inference."""
    profile.validate()
    if profile.provider != "Ollama":
        raise ValueError("A local Ollama profile is required")
    try:
        models = reader(profile.endpoint)["models"]
        matches = [
            item for item in models if isinstance(item, dict) and item.get("name") == profile.model
        ]
        digest = matches[0].get("digest") if len(matches) == 1 else None
    except Exception:
        raise ValueError("Local generation identity could not be read") from None
    if not isinstance(digest, str) or not _DIGEST.fullmatch(digest):
        raise ValueError("Local generation identity is unavailable")
    return digest
