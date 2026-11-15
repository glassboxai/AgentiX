"""Conservative unattended-call eligibility; native isolation remains mandatory.

This module never imports generated code. Unknown syntax/capabilities require
manual call approval. Classification does not establish semantic correctness or
purity and cannot grant filesystem, network or process permissions.

The importable-module list is owner-extensible through portable_modules.json in
the deployment data root. Policy allowance never installs packages: third-party
imports still require the managed environment to provide them.
"""

import ast
import json
import re
from pathlib import Path

# Explicit safe call vocabulary; aliases and dynamic dispatch fail closed.
_CALLS = frozenset(
    "abs all any bool dict enumerate float int isinstance len list max min range reversed round set sorted str sum tuple zip ValueError TypeError ZeroDivisionError OverflowError AssertionError".split()
)
# Maintained default; portable_modules.json may replace it (typing stays forced).
_MODULES = frozenset(
    {
        "math",
        "statistics",
        "decimal",
        "typing",
        "random",
        "re",
        "string",
        "itertools",
        "functools",
        "collections",
        "datetime",
        "json",
        "textwrap",
        "unicodedata",
    }
)
_MODULE_NAME = re.compile(r"[a-z][a-z0-9_]*")


def allowed_modules(path: "Path | None" = None) -> frozenset[str]:
    """Return the effective owner-approved importable modules.

    Reads portable_modules.json ({"allowed_modules": ["re", ...]}) from the
    deployment data root, or from an explicit path in tests. A missing or
    invalid file fails closed to the maintained default. A valid list fully
    replaces the default; typing is always forced because canonical Annotated
    contracts require it. The file is read on every call so owner edits apply
    without a restart.
    """
    if path is None:
        from agentix.storage.locations import data_directory

        path = data_directory() / "portable_modules.json"
    try:
        document = json.loads(Path(path).read_text(encoding="utf-8"))
        entries = document["allowed_modules"]
        if not isinstance(entries, list) or any(
            not isinstance(entry, str) or not _MODULE_NAME.fullmatch(entry) for entry in entries
        ):
            raise ValueError("Invalid portable module list")
        return frozenset(entries) | {"typing"}
    except (OSError, ValueError, TypeError, KeyError, UnicodeError):
        return _MODULES


def unapproved_imports(code: bytes, modules: frozenset[str]) -> set[str]:
    """Return imported module roots outside the allowed set, without executing code."""
    try:
        tree = ast.parse(code)
    except (SyntaxError, ValueError, RecursionError):
        return {"<unparseable>"}
    rejected = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            rejected.update(
                alias.name.split(".")[0] for alias in node.names if alias.name not in modules
            )
        elif isinstance(node, ast.ImportFrom):
            if node.level or node.module not in modules:
                rejected.add(node.module or "<relative>")
    return rejected


_METHODS = frozenset(
    "split strip lstrip rstrip lower upper casefold startswith endswith count replace join append extend items keys values get copy isdigit isalpha isalnum isspace capitalize title find index pop sort reverse randint random uniform choice sample randrange".split()
)
_NODES = frozenset(
    {
        "Module",
        "FunctionDef",
        "arguments",
        "arg",
        "Return",
        "Assign",
        "AnnAssign",
        "AugAssign",
        "Expr",
        "Constant",
        "Name",
        "Load",
        "Store",
        "List",
        "Tuple",
        "Dict",
        "Set",
        "BinOp",
        "UnaryOp",
        "BoolOp",
        "Compare",
        "If",
        "IfExp",
        "For",
        "While",
        "Break",
        "Continue",
        "Pass",
        "Raise",
        "Try",
        "ExceptHandler",
        "Assert",
        "Call",
        "keyword",
        "Attribute",
        "Subscript",
        "Slice",
        "ListComp",
        "SetComp",
        "DictComp",
        "GeneratorExp",
        "comprehension",
        "JoinedStr",
        "FormattedValue",
        "Import",
        "ImportFrom",
        "alias",
        "Add",
        "Sub",
        "Mult",
        "Div",
        "FloorDiv",
        "Mod",
        "Pow",
        "USub",
        "UAdd",
        "Not",
        "And",
        "Or",
        "Eq",
        "NotEq",
        "Lt",
        "LtE",
        "Gt",
        "GtE",
        "Is",
        "IsNot",
        "In",
        "NotIn",
        "BitOr",
    }
)


def computation_only(code: bytes, modules: frozenset[str] | None = None) -> bool:
    """Return whether exact source uses only the explicit computation vocabulary.

    Parameters: UTF-8 Python source bytes and, optionally, the allowed import
    set; None loads the owner-configured allowed_modules(). Returns False for
    invalid/unknown constructs, private introspection, dynamic calls or
    unapproved imports. No source is executed; callers must still use OS
    isolation and reviewed grants.
    """
    if modules is None:
        modules = allowed_modules()
    try:
        tree = ast.parse(code)
        functions = {
            node.name
            for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef) and not node.name.startswith("__")
        }
        imported = set()
        calls = set(_CALLS) | functions
        for node in ast.walk(tree):
            if type(node).__name__ not in _NODES:
                return False
            if (
                isinstance(node, ast.Name)
                and node.id.startswith("_")
                and node.id not in functions
                and not (node.id == "_" and isinstance(node.ctx, ast.Store))
            ):
                return False
            if isinstance(node, ast.FunctionDef) and node.decorator_list:
                return False
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name not in modules or alias.asname:
                            return False
                        imported.add(alias.name)
                else:
                    if node.module not in modules or node.level:
                        return False
                    for alias in node.names:
                        if alias.name.startswith("_") or alias.asname:
                            return False
                        if node.module != "typing":
                            calls.add(alias.name)
            if isinstance(node, ast.Attribute):
                module_attribute = isinstance(node.value, ast.Name) and node.value.id in imported
                if node.attr.startswith("_") or not (module_attribute or node.attr in _METHODS):
                    return False
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id not in calls:
                        return False
                elif isinstance(node.func, ast.Attribute):
                    if isinstance(node.func.value, ast.Name) and node.func.value.id == "typing":
                        return False
                else:
                    return False
        return True
    except (SyntaxError, ValueError, RecursionError, UnicodeError):
        return False
