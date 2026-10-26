"""Conservative unattended-call eligibility; native isolation remains mandatory.

This module never imports generated code. Unknown syntax/capabilities require
manual call approval. Classification does not establish semantic correctness or
purity and cannot grant filesystem, network or process permissions.
"""

import ast

# Explicit safe call vocabulary; aliases and dynamic dispatch fail closed.
_CALLS = frozenset(
    "abs all any bool dict enumerate float int isinstance len list max min range reversed round set sorted str sum tuple zip ValueError TypeError ZeroDivisionError OverflowError AssertionError".split()
)
_MODULES = frozenset({"math", "statistics", "decimal", "typing"})
_METHODS = frozenset(
    "split strip lstrip rstrip lower upper casefold startswith endswith count replace join append extend items keys values get copy isdigit isalpha isspace capitalize title find index pop sort reverse".split()
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


def computation_only(code: bytes) -> bool:
    """Return whether exact source uses only the explicit computation vocabulary.

    Parameters: UTF-8 Python source bytes. Returns False for invalid/unknown
    constructs, private introspection, dynamic calls or unapproved imports.
    No source is executed; callers must still use OS isolation and reviewed grants.
    """
    try:
        tree = ast.parse(code)
        functions = {node.name for node in tree.body if isinstance(node, ast.FunctionDef)}
        modules = set()
        calls = set(_CALLS) | functions
        for node in ast.walk(tree):
            if type(node).__name__ not in _NODES:
                return False
            if isinstance(node, ast.Name) and node.id.startswith("_"):
                return False
            if isinstance(node, ast.FunctionDef) and node.decorator_list:
                return False
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name not in _MODULES or alias.asname:
                            return False
                        modules.add(alias.name)
                else:
                    if node.module not in _MODULES or node.level:
                        return False
                    for alias in node.names:
                        if alias.name.startswith("_") or alias.asname:
                            return False
                        if node.module != "typing":
                            calls.add(alias.name)
            if isinstance(node, ast.Attribute):
                module_attribute = isinstance(node.value, ast.Name) and node.value.id in modules
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
