"""Stage only installed pinned Gradio distributions into a private native runtime.

No project tool directory or user data is enumerated. Files must resolve inside the
selected environment's site-packages; .pth files are copied as data, never processed.
"""

import importlib.metadata as metadata
import re
import shutil
import sys
from pathlib import Path

from packaging.requirements import Requirement
from packaging.utils import canonicalize_name

from agentix.sandbox import WindowsSandbox


def stage_runtime(root: Path) -> None:
    """Copy CPython and the Gradio dependency closure after exact lock-version checks."""
    WindowsSandbox._copy_runtime(root)
    lock = Path(__file__).resolve().parents[3] / "infra" / "runtime.lock.txt"
    pins = {
        canonicalize_name(name): version
        for name, version in re.findall(
            r"^([A-Za-z0-9_.-]+)==([^\s\\]+)", lock.read_text(), re.MULTILINE
        )
    }
    pending, visited = ["gradio"], set()
    site = root / "site-packages"
    site.mkdir()
    boundary = (Path(sys.prefix) / "Lib" / "site-packages").resolve()
    while pending:
        name = canonicalize_name(pending.pop())
        if name in visited:
            continue
        visited.add(name)
        distribution = metadata.distribution(name)
        if distribution.version != pins.get(name):
            raise RuntimeError("Gradio dependency differs from reviewed lock")
        for item in distribution.files or ():
            if ".." in item.parts or item.suffix == ".pyc":
                continue
            source = Path(distribution.locate_file(item))
            if (
                not source.is_file()
                or source.is_symlink()
                or not source.resolve().is_relative_to(boundary)
            ):
                raise RuntimeError("Dependency source escapes selected environment")
            destination = site / Path(item)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
        for raw in distribution.requires or ():
            requirement = Requirement(raw)
            if requirement.marker is None or requirement.marker.evaluate({"extra": ""}):
                pending.append(requirement.name)
