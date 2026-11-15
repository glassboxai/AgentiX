"""Guard the module closure that keeps application code independent of the Lab UI.

The Lab package mixes presentation with reviewed runtime sources. These checks fail
before a removal step deletes a module that is still imported, copied by path into
the sandbox, or referenced by an installed-application policy digest.
"""

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "src" / "agentix"

REMOVABLE = frozenset(
    {
        "agentix.lab.application_followup",
        "agentix.lab.application_gateway",
        "agentix.lab.direct_widget_designer",
        "agentix.lab.engine",
        "agentix.lab.gateway",
        "agentix.lab.view",
    }
)

COPIED_BY_PATH = (
    "widget_worker.py",
    "callback_runtime.py",
    "reference_widget.py",
    "fixture_tools.py",
)


def _module_name(path: Path) -> str:
    """Return the dotted import name of a source file inside the package."""
    parts = list(path.relative_to(ROOT / "src").with_suffix("").parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts)


def _imports(path: Path) -> set[str]:
    """Collect absolute module names imported by one source file."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                base = _module_name(path).split(".")
                prefix = ".".join(base[: len(base) - node.level])
                module = prefix + ("." + node.module if node.module else "")
            else:
                module = node.module or ""
            found.add(module)
            found.update(module + "." + alias.name for alias in node.names)
    return found


def test_no_maintained_module_imports_a_removable_lab_module():
    """Catch a removal step that leaves a live importer behind."""
    offenders = {}
    for path in sorted(PACKAGE.rglob("*.py")):
        if "__pycache__" in path.parts:
            continue
        name = _module_name(path)
        if name in REMOVABLE:
            continue
        hits = sorted(_imports(path) & REMOVABLE)
        if hits:
            offenders[name] = hits
    assert offenders == {}


def test_sandbox_staging_sources_stay_present():
    """Catch deletion of a module that is copied by path instead of imported."""
    lab = PACKAGE / "lab"
    missing = [name for name in COPIED_BY_PATH if not (lab / name).is_file()]
    assert missing == []


def test_staging_sources_are_referenced_by_name():
    """Catch a staging reference removed while its source file still exists."""
    sources = "\n".join(
        path.read_text(encoding="utf-8") for path in sorted((PACKAGE / "lab").glob("*.py"))
    )
    unreferenced = [name for name in COPIED_BY_PATH if f'"{name}"' not in sources]
    assert unreferenced == []


def test_installed_application_policy_paths_exist():
    """Catch a policy digest path that no longer resolves after a move or removal."""
    source = (PACKAGE / "storage" / "installed_apps.py").read_text(encoding="utf-8")
    names: list[str] = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.FunctionDef) and node.name == "app_policy":
            for inner in ast.walk(node):
                if isinstance(inner, ast.For) and isinstance(inner.iter, ast.Tuple):
                    names = [
                        element.value
                        for element in inner.iter.elts
                        if isinstance(element, ast.Constant) and isinstance(element.value, str)
                    ]
    assert len(names) >= 20
    missing = [name for name in names if not (PACKAGE / name).is_file()]
    assert missing == []
