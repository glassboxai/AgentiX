"""Read an AST catalog without importing or executing tool source."""

import ast
import json
import logging
import os
import re
from pathlib import Path

from agentix.diagnostics import log_event

logger = logging.getLogger(__name__)


class ToolCatalog:
    """Render the existing Markdown catalog for an explicit storage root."""

    def __init__(self, root: str | Path) -> None:
        """Remember the root; construction never reads its contents."""
        self.root = str(root)

    def contains(self, tool_name: str) -> bool:
        """Check exact catalog membership without importing or enumerating source.

        Path containment/links are independently enforced by the approval ledger.
        Membership alone never establishes authorization or functional correctness.
        """
        if not isinstance(tool_name, str) or not re.fullmatch(
            r"[A-Za-z][A-Za-z0-9_]{0,127}", tool_name
        ):
            return False
        folder = Path(self.root) / tool_name
        return folder.is_dir() and (folder / f"{tool_name}_code.py").is_file()

    def render(self) -> str:
        """
        Safely inspects generated_tools/ using Python AST (without executing code).
        Extracts available tools, standalone functions, argument signatures, and docstrings.
        """
        log_event(logger, "catalog_rendering", level=logging.DEBUG)
        if not os.path.exists(self.root):
            return "No tools installed yet."

        catalog_entries = []

        for item in sorted(os.listdir(self.root)):
            tool_dir = os.path.join(self.root, item)
            code_file = os.path.join(tool_dir, f"{item}_code.py")

            if os.path.isdir(tool_dir) and os.path.exists(code_file):
                try:
                    with open(code_file, encoding="utf-8") as f:
                        tree = ast.parse(f.read())

                    functions_info = []
                    for node in tree.body:
                        if isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
                            args_list = [arg.arg for arg in node.args.args]
                            doc = ast.get_docstring(node) or "No description provided."
                            first_line_doc = doc.strip().splitlines()[0]
                            functions_info.append(
                                f"    * Function: `{node.name}({', '.join(args_list)})`\n"
                                f"      Description: {first_line_doc}"
                            )

                    if functions_info:
                        entry = f"- Tool Name: `{item}`\n" + "\n".join(functions_info)
                    else:
                        entry = f"- Tool Name: `{item}` (No standalone functions detected)"

                    try:
                        from agentix.domain.tool_schema import extract_tool_schema

                        contract = extract_tool_schema(item, ast.unparse(tree))
                    except (ValueError, SyntaxError):
                        contract = None
                    if contract is not None:
                        entry += "\n    Canonical typed contract: " + json.dumps(
                            contract, ensure_ascii=True
                        )
                    entry += (
                        f"\n    Conventional artifact filenames: `{item}_specifications.md`, "
                        f"`{item}_code.py`, `{item}_tests.py`. "
                        "Use these exact names with Read Artifact Tool; do not guess package files."
                    )
                    catalog_entries.append(entry)

                except Exception as e:
                    log_event(logger, "catalog_entry_rejected", error=e, level=logging.WARNING)
                    catalog_entries.append(f"- Tool Name: `{item}` (Error parsing code file: {e})")

        log_event(logger, "catalog_rendered", level=logging.DEBUG)
        return "\n\n".join(catalog_entries) if catalog_entries else "No tools installed yet."

    def contracts(self) -> dict:
        """Read a bounded canonical metadata catalog without imports or test execution."""
        from agentix.domain.tool_schema import extract_tool_schema

        root = Path(self.root)
        if not root.exists():
            return {}
        entries = list(root.iterdir())
        if len(entries) > 512:
            raise ValueError("Tool routing catalog exceeds its limit")
        contracts = {}
        for folder in sorted(entries):
            if not self.contains(folder.name):
                continue
            source = folder / (folder.name + "_code.py")
            if folder.is_symlink() or source.is_symlink() or source.stat().st_size > 65536:
                continue
            try:
                contracts[folder.name] = extract_tool_schema(
                    folder.name, source.read_text(encoding="utf-8")
                )
            except (ValueError, SyntaxError):
                continue
        return contracts
