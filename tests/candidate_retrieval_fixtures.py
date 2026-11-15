"""Explicit retrieval double for legacy browser fixtures; never contacts a model.

Legacy role aliases are test data. This adapter deliberately represents them in
search metadata without claiming production canonical-catalog discovery support.
"""

import ast
from collections.abc import Callable
from dataclasses import replace
from pathlib import Path
from typing import Any

from agentix.retrieval import SearchResult, ToolDescriptor, descriptor_from_source
from agentix.storage.application_catalog import CatalogDependencyError


class RegistryRetrievalDouble:
    """Return authored fixture descriptors through the same candidate acceptance gate."""

    startup_message = "Fixture tool index ready (retrieval model is doubled)."

    def __init__(self, registry_factory: Callable, audit: Callable | None = None) -> None:
        """Inject the browser fixture's catalog-to-owner registry factory and audit hook."""
        self.registry_factory = registry_factory
        self.audit = audit

    @staticmethod
    def _descriptor(name: str, function: str, source: str) -> ToolDescriptor:
        """Represent an explicit legacy function alias using the generic descriptor contract."""
        item = descriptor_from_source(function, source, artifact_ref=name)
        return replace(item, tool_id=name, name=name, entrypoint=f"{name}_code.py:{function}")

    def search(self, catalog: Any, handle: Any, query: str, limit: int) -> list[SearchResult]:
        """Extract trusted temporary fixture metadata; never approve or execute source."""
        if self.audit is not None:
            self.audit(limit)
        try:
            tools = self.registry_factory(catalog).resolve()
            descriptors = [
                self._descriptor(tool.tool_name, tool.function, tool.code.decode("utf-8"))
                for tool in tools.values()
            ]
        except CatalogDependencyError:
            descriptors = []
            for folder in sorted(Path(catalog.root).iterdir()):
                source = folder / f"{folder.name}_code.py"
                if not source.is_file():
                    continue
                text = source.read_text(encoding="utf-8")
                functions = [
                    node
                    for node in ast.parse(text).body
                    if isinstance(node, ast.FunctionDef) and not node.name.startswith("_")
                ]
                if len(functions) != 1:
                    raise ValueError("Trusted legacy fixture requires exactly one public function")
                descriptors.append(self._descriptor(folder.name, functions[0].name, text))
        return [
            SearchResult(item, rank, 1 / (60 + rank), 0.9, 1.0, "hybrid")
            for rank, item in enumerate(descriptors[:limit], 1)
        ]
