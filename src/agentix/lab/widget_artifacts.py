"""Review-only widget packages: bounded syntax policy plus exact content binding.

AST checks reduce the supported UI surface; they are not OS isolation. Generated source
is parsed/compiled for syntax only on the host and executed solely in AppContainer.
"""

import ast
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

from agentix.lab.widget_identity import CONTRACT, TESTS_FILENAME, TOOL_FILENAME, WIDGET_FILENAME

__all__ = ["CONTRACT", "ApprovedWidget", "approve_package", "package_digest", "validate_widget"]


@dataclass(frozen=True)
class ApprovedWidget:
    """Engineer-reviewed immutable source snapshots; never load approval from child files."""

    widget: bytes
    tool: bytes
    digest: str
    tests: bytes = b""


def validate_widget(source: bytes) -> None:
    """Accept a narrow widget grammar, rejecting arbitrary imports/callback capabilities."""
    if len(source) > 32768:
        raise ValueError("Widget source limit")
    try:
        tree = ast.parse(source)
    except (SyntaxError, UnicodeError, RecursionError) as error:
        raise ValueError("Invalid widget Python") from error
    imports = [node for node in tree.body if isinstance(node, ast.Import)]
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    if (
        len(imports) != 1
        or len(imports[0].names) != 1
        or imports[0].names[0].name != "gradio"
        or imports[0].names[0].asname != "gr"
        or len(functions) != 1
    ):
        raise ValueError("Only gradio and create_widget are allowed")
    function = functions[0]
    if (
        function.name != "create_widget"
        or [arg.arg for arg in function.args.args] != ["context"]
        or function.decorator_list
        or function.args.vararg
        or function.args.kwarg
        or function.args.defaults
        or function.returns
    ):
        raise ValueError("Unsupported widget entrypoint")
    allowed = (
        ast.Module,
        ast.Import,
        ast.alias,
        ast.FunctionDef,
        ast.arguments,
        ast.arg,
        ast.With,
        ast.withitem,
        ast.Assign,
        ast.Name,
        ast.Load,
        ast.Store,
        ast.Call,
        ast.Attribute,
        ast.keyword,
        ast.Constant,
        ast.Expr,
        ast.Return,
        ast.Dict,
    )
    components = {}
    roles = set()
    clicks = 0
    for node in ast.walk(tree):
        if not isinstance(node, allowed):
            raise ValueError("Unsupported widget syntax")
        if isinstance(node, ast.Name) and node.id.startswith("_"):
            raise ValueError("Private names are forbidden")
        if isinstance(node, ast.Attribute):
            if not isinstance(node.value, ast.Name) or node.attr.startswith("_"):
                raise ValueError("Attribute chaining is forbidden")
            owner = node.value.id
            valid = (
                owner == "gr"
                and node.attr in ("Group", "Textbox", "Number", "Button")
                or owner == "context"
                and node.attr in ("elem_id", "invoke", "api_name")
                or node.attr == "click"
                and owner in components
            )
            if not valid:
                raise ValueError("Unsupported widget attribute")
        if isinstance(node, ast.Assign):
            if (
                len(node.targets) != 1
                or not isinstance(node.targets[0], ast.Name)
                or not isinstance(node.value, ast.Call)
                or not isinstance(node.value.func, ast.Attribute)
                or not isinstance(node.value.func.value, ast.Name)
                or node.value.func.value.id != "gr"
            ):
                raise ValueError("Only component variables may be assigned")
            components[node.targets[0].id] = node.value.func.attr
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Attribute) or not isinstance(
                node.func.value, ast.Name
            ):
                raise ValueError("Unsupported call")
            owner, name = node.func.value.id, node.func.attr
            if owner == "context" and name == "elem_id":
                if (
                    len(node.args) != 1
                    or not isinstance(node.args[0], ast.Constant)
                    or node.args[0].value not in CONTRACT["roles"]
                    or node.args[0].value in roles
                ):
                    raise ValueError("Missing, duplicate or unknown component role")
                roles.add(node.args[0].value)
            elif name == "click":
                keywords = {item.arg: item.value for item in node.keywords}
                if (
                    set(keywords) != {"fn", "inputs", "outputs", "queue", "api_name"}
                    or not isinstance(keywords["queue"], ast.Constant)
                    or keywords["queue"].value is not False
                    or not isinstance(keywords["fn"], ast.Attribute)
                    or ast.unparse(keywords["fn"]) != "context.invoke"
                    or ast.unparse(keywords["api_name"]) != "context.api_name"
                ):
                    raise ValueError("Callback must use the approved gateway without queue")
                if (
                    not isinstance(keywords["inputs"], ast.Name)
                    or components.get(keywords["inputs"].id) != "Textbox"
                    or not isinstance(keywords["outputs"], ast.Name)
                    or components.get(keywords["outputs"].id) != "Number"
                ):
                    raise ValueError("Incompatible callback component binding")
                clicks += 1
            elif owner != "gr":
                raise ValueError("Only Gradio constructors and approved context calls allowed")
            elif any(
                item.arg
                not in ("label", "elem_id", "precision", "value", "interactive", "max_lines")
                for item in node.keywords
            ):
                raise ValueError("Unsupported component option")
    for node in ast.walk(tree):
        if isinstance(node, ast.keyword) and node.arg in ("interactive", "max_lines"):
            if not isinstance(node.value, ast.Constant):
                raise ValueError("Presentation options must be literals")
            if node.arg == "interactive" and type(node.value.value) is not bool:
                raise ValueError("interactive must be boolean")
            if node.arg == "max_lines" and (
                type(node.value.value) is not int or not 1 <= node.value.value <= 100
            ):
                raise ValueError("max_lines must be bounded")
    if roles != set(CONTRACT["roles"]) or clicks != 1:
        raise ValueError("Widget must bind all three controls exactly once")
    for node in tree.body:
        if not isinstance(node, (ast.Import, ast.FunctionDef)) and not (
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Constant)
            and isinstance(node.value.value, str)
        ):
            raise ValueError("No executable module-level widget code")
    compile(tree, "<reviewed widget>", "exec")


def _digest(widget: bytes, tool: bytes, tests: bytes = b"", definition: bytes = b"") -> str:
    """Bind exact source bytes and fixed contract without ambiguous concatenation."""
    payload = json.dumps(
        {
            "widget": hashlib.sha256(widget).hexdigest(),
            "tool": hashlib.sha256(tool).hexdigest(),
            "contract": CONTRACT,
            "filenames": [WIDGET_FILENAME, TOOL_FILENAME, TESTS_FILENAME],
            "tests": hashlib.sha256(tests).hexdigest(),
            "definition": hashlib.sha256(definition).hexdigest(),
        },
        sort_keys=True,
    ).encode()
    return hashlib.sha256(payload).hexdigest()


def package_digest(folder: Path) -> str:
    """Compute the review identity; this does not grant approval or execute source."""
    return _digest(
        (folder / WIDGET_FILENAME).read_bytes(),
        (folder / TOOL_FILENAME).read_bytes(),
        (folder / TESTS_FILENAME).read_bytes() if (folder / TESTS_FILENAME).exists() else b"",
        (folder / "tool_definition.json").read_bytes()
        if (folder / "tool_definition.json").exists()
        else b"",
    )


def approve_package(folder: Path, reviewed_digest: str) -> ApprovedWidget:
    """Capture reviewed bytes only if the caller's explicit digest still matches."""
    widget, tool = (folder / WIDGET_FILENAME).read_bytes(), (folder / TOOL_FILENAME).read_bytes()
    tests = (folder / TESTS_FILENAME).read_bytes() if (folder / TESTS_FILENAME).exists() else b""
    definition = (
        (folder / "tool_definition.json").read_bytes()
        if (folder / "tool_definition.json").exists()
        else b""
    )
    if definition and (
        json.loads(definition) != CONTRACT or type(json.loads(definition).get("schema")) is not int
    ):
        raise ValueError("Package contract differs from supported tool")
    if len(tests) > 32768 or len(tool) > 1048576:
        raise ValueError("Package size limit")
    if tests:
        compile(tests, "<proposed widget tests>", "exec")
    digest = _digest(widget, tool, tests, definition)
    if digest != reviewed_digest:
        raise ValueError("Package changed since review")
    validate_widget(widget)
    return ApprovedWidget(widget, tool, digest, tests)
