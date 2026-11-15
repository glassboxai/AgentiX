"""Load/synchronize the GUI's installed tool root into a dedicated local RAG index.

Uses Settings and ToolCatalog rather than guessing a tools directory. Reads source
as bounded AST metadata only. Never imports tools, changes approval state, installs
models, starts a GUI or restarts services. Run again to refresh without searching;
bound ToolRetriever instances also synchronize automatically before every search.
"""

import argparse
import json
import logging
import sys
from collections.abc import Sequence
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from agentix.retrieval import (  # noqa: E402
    CatalogToolSource,
    OllamaClient,
    OllamaEmbeddings,
    OllamaKeywords,
    ToolRetriever,
)
from agentix.settings import Settings  # noqa: E402
from agentix.storage.catalog import ToolCatalog  # noqa: E402


def main(argv: Sequence[str] | None = None) -> None:
    """Synchronize configured tools and print counts/rejections as JSON.

    Optional explicit roots support the exact deployment launcher configuration.
    The index defaults to a sibling tool_registry directory beside the tools root.
    Failures propagate; unavailable models never trigger downloads or fallback.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tools-root", type=Path, help="Override the configured GUI tools root")
    parser.add_argument("--index", type=Path, help="Dedicated persistent retrieval directory")
    args = parser.parse_args(argv)
    settings = Settings.from_environment()
    catalog = ToolCatalog(args.tools_root if args.tools_root is not None else settings.tools_root)
    index = args.index if args.index is not None else Path(catalog.root).parent / "tool_registry"
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
    client = OllamaClient(settings.ollama_url)
    retriever = ToolRetriever(
        index,
        OllamaEmbeddings(client),
        OllamaKeywords(client),
        descriptor_source=CatalogToolSource(catalog),
    )
    print(json.dumps({"index": str(index), "sync": asdict(retriever.last_sync_report)}))


if __name__ == "__main__":
    main()
