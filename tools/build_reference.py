"""Build and verify English reference documents without importing application code.

Only named root entrypoints and Python files inside src, tools and tests are read.
Existing generated_tools and dependencies are never traversed. References contain
names, contracts and scope/type information, never assigned values or secrets.
"""

import argparse
import ast
import hashlib
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

ROOT_ENTRIES = (
    "app.py",
    "main.py",
    "config.py",
    "custom_tools.py",
    "security_manager.py",
    "_agentix_path.py",
)
MEANINGS = {
    "self": "Owning instance; its attributes retain state for the instance lifetime.",
    "cls": "Class receiving this class-level operation.",
    "tool_name": "Validated public tool identifier within the configured storage boundary.",
    "function_name": "Public callable selected for the current operation; empty selects test mode.",
    "kwargs": "Bounded JSON keyword arguments; no executable objects are accepted.",
    "kwargs_json": "Untrusted JSON argument text to validate before execution.",
    "code": "Source snapshot passed through approval, syntax checks and isolated staging.",
    "tests": "Optional unittest source snapshot; child-authored success remains provisional.",
    "test_code": "Proposed unittest source requiring approval and isolated execution.",
    "security": "Owner-scoped approval and path boundary injected into this service.",
    "sandbox": "Injected execution boundary; structural type alone cannot prove OS isolation.",
    "execution_backend": "One process boundary selected by the composition root for all owner services.",
    "verification": "Content-bound ledger used to authorize only the current approved operation.",
    "owner_id": "Session owner identity used to prevent cross-session authorization.",
    "operation_id": "Identity of one user operation; new operations invalidate earlier evidence.",
    "request_id": "Displayed approval identity checked against the owner and expiry; not a secret.",
    "session_id": "Browser or terminal session identifier for state and diagnostic ownership.",
    "settings": "Immutable startup configuration; constructing it does not start external services.",
    "runtime": "Explicitly composed application services for one owner or compatibility facade.",
    "logger": "Module logger emitting bounded operation diagnostics rather than artifact bodies.",
    "root": "Explicit root directory against which named paths are resolved.",
    "path": "Path under validation or an explicitly scoped maintained source path.",
    "pending": "Defensive pending-approval snapshot; never a capability to approve another owner.",
    "result": "Intermediate or returned outcome; consult the callable contract for trust/validation.",
    "response": "Bounded response text to render or validate; it is not executable code.",
    "query": "Original user request or a trusted test query; avoid payload logging by default.",
    "user_query": "Original requirements retained across agent handoffs and final execution.",
    "state": "Owner-local mutable workflow/UI state guarded by its documented synchronization.",
    "content": "Artifact or review text whose encoding, size and approval state must be checked.",
    "source": "Explicit source document or source-code text; never imported for reference generation.",
    "identity": "Explicit owner identity used by a session factory or fixture.",
    "backend": "Injected framework/execution provider; callers determine the required protocol.",
    "document": "Structured reference/Word/AST document owned by the current authoring operation.",
    "manifest": "Versioned inventory or launch record; not an execution-authorization capability.",
    "expected": "Reviewed expected observation kept outside untrusted child execution.",
    "observed": "Returned observation checked against the reviewed host-side expectation.",
    "contract": "Validated declarative acceptance data bound to current artifact identities.",
    "digest": "Content fingerprint for change detection; not a substitute for human approval.",
    "line": "Current source or text line scoped to parsing; no implicit execution occurs.",
    "value": "Value at the current validation/rendering boundary; apply the enclosing contract.",
    "name": "Current identifier selected by parsing, lookup or dependency registration.",
}


def maintained_sources(root: Path) -> list[Path]:
    """Enumerate only maintained directories, skipping bytecode and linked paths."""
    result = [root / name for name in ROOT_ENTRIES if (root / name).is_file()]
    for folder in ("src", "tools", "tests"):
        base = root / folder
        if base.exists():
            result.extend(
                path
                for path in base.rglob("*.py")
                if "__pycache__" not in path.parts and not path.is_symlink()
            )
    return sorted(result)


def expression_type(node: ast.AST | None) -> str:
    """Describe static expression shape without exposing assigned literal values."""
    if isinstance(node, ast.Constant):
        return type(node.value).__name__
    if isinstance(node, (ast.List, ast.ListComp)):
        return "list"
    if isinstance(node, (ast.Dict, ast.DictComp)):
        return "dict"
    if isinstance(node, (ast.Set, ast.SetComp)):
        return "set"
    if isinstance(node, ast.Tuple):
        return "tuple"
    if isinstance(node, ast.Call):
        target = node.func
        label = target.id if isinstance(target, ast.Name) else getattr(target, "attr", "callable")
        return f"Return type of {label}; see its callable contract"
    return "Runtime-dependent; see the enclosing callable contract"


class SourceInventory(ast.NodeVisitor):
    """Collect declarations and scoped bindings without evaluating annotations."""

    def __init__(self) -> None:
        """Create independent state for one maintained Python module."""
        self.scope: list[str] = []
        self.symbols: list[dict[str, Any]] = []
        self.variables: dict[tuple[str, str], dict[str, Any]] = {}

    def binding(self, name: str, node: ast.AST, kind: str, declared: str) -> None:
        """Record a named binding's type, role and source location without its value."""
        scope = ".".join(self.scope) or "module"
        lifecycle = (
            "Module/process lifetime"
            if not self.scope
            else "Enclosing invocation or class/instance lifetime"
        )
        if kind == "caught exception":
            lifecycle = "Current exception handler; Python clears this binding afterward"
        elif kind == "comprehension item":
            lifecycle = "This comprehension only; does not leak into its enclosing scope"
        elif kind == "managed resource":
            lifecycle = "Context-manager block; exit invokes its cleanup protocol"
        meaning = MEANINGS.get(name.removeprefix("self."))
        if meaning is None:
            words = name.removeprefix("self.").strip("_").replace("_", " ")
            meaning = f"{kind.capitalize()} for {words} in {scope}; use the enclosing contract and type below."
        key = (scope, name)
        if key in self.variables:
            self.variables[key]["writes"].append(getattr(node, "lineno", 1))
        else:
            self.variables[key] = {
                "scope": scope,
                "name": name,
                "kind": kind,
                "type": declared,
                "meaning": meaning,
                "lifecycle": lifecycle,
                "writes": [getattr(node, "lineno", 1)],
            }

    def target(self, target: ast.AST, node: ast.AST, kind: str, declared: str) -> None:
        """Flatten tuple bindings and retain explicit attribute ownership."""
        if isinstance(target, ast.Name):
            self.binding(target.id, node, kind, declared)
        elif isinstance(target, ast.Attribute):
            self.binding(ast.unparse(target), node, "attribute", declared)
        elif isinstance(target, (ast.Tuple, ast.List)):
            for item in target.elts:
                self.target(item, node, kind, declared)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """Capture a class contract and then collect its owned declarations."""
        self.definition(node, "class")

    def visit_FunctionDef(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        """Capture callable contracts, parameters, locals and nested definitions."""
        self.definition(node, "callable")

    visit_AsyncFunctionDef = visit_FunctionDef

    def definition(self, node: Any, kind: str) -> None:
        """Describe a declaration before entering its lexical scope."""
        qualified = ".".join([*self.scope, node.name])
        self.symbols.append(
            {
                "name": qualified,
                "kind": kind,
                "line": node.lineno,
                "docstring": ast.get_docstring(node) or "",
                "returns": ast.unparse(node.returns)
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.returns
                else "Not declared / class",
            }
        )
        self.scope.append(node.name)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            args = [*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs]
            args.extend(arg for arg in (node.args.vararg, node.args.kwarg) if arg is not None)
            for argument in args:
                self.binding(
                    argument.arg,
                    argument,
                    "parameter",
                    ast.unparse(argument.annotation)
                    if argument.annotation
                    else "Not explicitly annotated",
                )
        self.generic_visit(node)
        self.scope.pop()

    def visit_Assign(self, node: ast.Assign) -> None:
        """Capture assigned names and statically observable type categories."""
        for target in node.targets:
            self.target(
                target,
                node,
                "local binding" if self.scope else "module binding",
                expression_type(node.value),
            )
        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        """Preserve declared types without resolving generated expressions."""
        self.target(node.target, node, "typed binding", ast.unparse(node.annotation))
        self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        """Record updates to existing variables as additional write locations."""
        self.target(node.target, node, "updated binding", "Preserved or operator-dependent type")
        self.generic_visit(node)

    def visit_For(self, node: ast.For | ast.AsyncFor) -> None:
        """Document each loop target within the enclosing callable."""
        self.target(node.target, node, "loop item", "Element of the declared iterable")
        self.generic_visit(node)

    visit_AsyncFor = visit_For

    def visit_comprehension(self, node: ast.comprehension) -> None:
        """Document comprehension-local names without executing their iterators."""
        self.target(
            node.target, node.target, "comprehension item", "Element of the declared iterable"
        )
        self.generic_visit(node)

    def visit_ListComp(self, node: Any) -> None:
        """Separate comprehension bindings from the enclosing function's locals."""
        self.scope.append(f"comprehension_{node.lineno}")
        self.generic_visit(node)
        self.scope.pop()

    visit_SetComp = visit_ListComp
    visit_DictComp = visit_ListComp
    visit_GeneratorExp = visit_ListComp

    def visit_Lambda(self, node: ast.Lambda) -> None:
        """Document anonymous callback parameters under their own lexical scope."""
        self.scope.append(f"lambda_{node.lineno}")
        for argument in [*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs]:
            self.binding(
                argument.arg,
                argument,
                "callback parameter",
                "Defined by the enclosing callback contract",
            )
        self.generic_visit(node)
        self.scope.pop()

    def visit_With(self, node: ast.With | ast.AsyncWith) -> None:
        """Capture context-manager resources and their lexical cleanup boundary."""
        for item in node.items:
            if item.optional_vars is not None:
                self.target(
                    item.optional_vars, node, "managed resource", expression_type(item.context_expr)
                )
        self.generic_visit(node)

    visit_AsyncWith = visit_With

    def visit_ExceptHandler(self, node: ast.ExceptHandler) -> None:
        """Document exception values without recording sensitive exception text."""
        if node.name:
            self.binding(
                node.name,
                node,
                "caught exception",
                ast.unparse(node.type) if node.type else "BaseException",
            )
        self.generic_visit(node)

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        """Capture assignment-expression targets as normal scoped bindings."""
        self.target(node.target, node, "expression binding", expression_type(node.value))
        self.generic_visit(node)

    def visit_Import(self, node: ast.Import | ast.ImportFrom) -> None:
        """Describe imported names as explicit module dependencies."""
        for alias in node.names:
            self.binding(
                alias.asname or alias.name.split(".")[0],
                node,
                "imported dependency",
                "Module or imported public symbol",
            )

    visit_ImportFrom = visit_Import


def scan_source(path: Path, name: str) -> dict[str, Any]:
    """Return one deterministic source-bound inventory, including its module contract."""
    source = path.read_bytes()
    tree = ast.parse(source.decode("utf-8-sig"))
    visitor = SourceInventory()
    visitor.visit(tree)
    return {
        "path": name,
        "sha256": hashlib.sha256(source).hexdigest(),
        "module_docstring": ast.get_docstring(tree) or "",
        "symbols": visitor.symbols,
        "variables": list(visitor.variables.values()),
    }


def escape(text: str) -> str:
    """Keep table delimiters and line breaks from changing reference structure."""
    return text.replace("|", "&#124;").replace("\n", " ")


def module_document(item: dict[str, Any]) -> str:
    """Explain module/callable contracts and every inventoried scoped binding."""
    parts = [
        f"# Reference for {item['path']}",
        "",
        item["module_docstring"],
        "",
        f"Source fingerprint: {item['sha256']}",
        "",
        "This reference is generated from maintained source without imports or execution. "
        "Assigned values are intentionally omitted. Runtime-dependent types are explicit; "
        "the enclosing docstring defines the behavioral contract. See [architecture](../ARCHITECTURE_QUALITY.md) "
        "for manually reviewed responsibility and dependency decisions.",
        "",
        "## Classes and callables",
        "",
    ]
    for symbol in item["symbols"]:
        parts.extend(
            [
                f"### {symbol['name']}",
                "",
                symbol["docstring"] or "Missing docstring: completion is blocked.",
                "",
                f"Kind: {symbol['kind']}. Declared return: {symbol['returns']}. Source line: {symbol['line']}.",
                "",
            ]
        )
    parts.extend(
        [
            "## Variables and parameters",
            "",
            "| Scope | Name | Role and meaning | Type | Lifetime | Writes |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for variable in item["variables"]:
        cells = [
            variable["scope"],
            variable["name"],
            variable["meaning"],
            variable["type"],
            variable["lifecycle"],
            ", ".join(map(str, sorted(set(variable["writes"])))),
        ]
        parts.append("| " + " | ".join(escape(cell) for cell in cells) + " |")
    return "\n".join(parts) + "\n"


def powershell_documents(root: Path) -> dict[str, str]:
    """Document fixed infrastructure ASTs without importing or executing their source.

    The trusted inventory helper uses PowerShell's parser. Missing PowerShell or
    malformed source fails this gate rather than silently dropping reference entries.
    """
    helper = root / "infra" / "Get-ReferenceInventory.ps1"
    if not helper.is_file():
        return {}
    executable = shutil.which("pwsh") or shutil.which("powershell.exe")
    if not executable:
        raise RuntimeError("PowerShell is required for infrastructure source references")
    result = subprocess.run(
        [executable, "-NoProfile", "-NonInteractive", "-File", str(helper)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
        timeout=30,
    )
    documents = {}
    for item in json.loads(result.stdout):
        name = item["source"]
        fingerprint = hashlib.sha256((root / name).read_bytes()).hexdigest()
        lines = [
            f"# {name}",
            "",
            f"Source SHA-256: {fingerprint}",
            "",
            item["contract"],
            "",
            "## Functions",
            "",
        ]
        for function in item["functions"]:
            lines.extend([f"### {function['name']}", "", function["contract"], ""])
        lines.extend(
            [
                "## Scoped variables",
                "",
                "Assigned values are excluded. Parameter/temporary meaning follows the owning function contract; process and script scopes are explicit.",
                "",
                "| Name | Scope | Static type | Lifecycle |",
                "| --- | --- | --- | --- |",
            ]
        )
        for variable in item["variables"]:
            lines.append(
                f"| {variable['name']} | {variable['scope']} | {variable['type']} | {variable['lifecycle']} |"
            )
        documents[name.replace("/", "__") + ".md"] = "\n".join(lines) + "\n"
    return documents


def expected_documents(root: Path) -> dict[str, str]:
    """Compute expected reference bytes from the complete maintained source inventory."""
    documents = {}
    index = [
        "# Maintained Python reference",
        "",
        "Regenerate with python tools/build_reference.py. Check freshness with --check.",
        "",
        "References cover maintained application, compatibility, developer tooling and tests. "
        "Existing generated_tools and dependency directories are excluded.",
        "",
    ]
    for path in maintained_sources(root):
        name = path.relative_to(root).as_posix()
        item = scan_source(path, name)
        target = name.replace("/", "__").removesuffix(".py") + ".md"
        documents[target] = module_document(item)
        index.append(f"- [{name}]({target})")
    infrastructure = powershell_documents(root)
    documents.update(infrastructure)
    index.extend(f"- [{name}]({name})" for name in sorted(infrastructure))
    documents["README.md"] = "\n".join(index) + "\n"
    return documents


def build_documents(root: Path, *, check: bool = False) -> list[str]:
    """Write references or return stale/missing entries without mutating files.

    Freshness is exact, including contracts and source fingerprints. Passing the
    check establishes inventory consistency, not semantic correctness; meaningful
    manual documentation review remains required by AGENTS.md.
    """
    destination = root / "docs" / "reference"
    expected = expected_documents(root)
    issues = []
    for name, content in expected.items():
        target = destination / name
        if check:
            if not target.is_file() or target.read_text(encoding="utf-8") != content:
                issues.append(name)
        else:
            destination.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
    if destination.exists():
        issues.extend(path.name for path in destination.glob("*.md") if path.name not in expected)
    return issues


def main() -> None:
    """Run the reference generation/freshness gate for this checkout only."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    issues = build_documents(root, check=args.check)
    print(json.dumps({"mode": "check" if args.check else "write", "issues": issues}, indent=2))
    raise SystemExit(bool(issues))


if __name__ == "__main__":
    main()
