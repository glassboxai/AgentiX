"""Approval policy fingerprints must include new presentation and cleanup boundaries."""

import importlib
import shutil
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "module,function,changed",
    [
        ("agentix.storage.installed_apps", "app_policy", "widgets/styles.py"),
        ("agentix.storage.widget_store", "widget_policy", "widgets/styles.py"),
        ("agentix.security.approval_store", "policy_fingerprint", "sandbox/profile_cleanup.py"),
    ],
)
def test_changed_boundary_invalidates_policy_binding(
    tmp_path, monkeypatch, module, function, changed
):
    """Catch retaining an approval after modifying an imported validation boundary."""
    checkout = Path(__file__).resolve().parents[1]
    shutil.copytree(
        checkout / "src", tmp_path / "src", ignore=shutil.ignore_patterns("__pycache__")
    )
    (tmp_path / "infra").mkdir()
    shutil.copyfile(checkout / "infra/runtime.lock.txt", tmp_path / "infra/runtime.lock.txt")
    target = importlib.import_module(module)
    relative = Path(target.__file__).relative_to(checkout)
    monkeypatch.setattr(target, "__file__", str(tmp_path / relative))
    before = getattr(target, function)()
    path = tmp_path / "src/agentix" / changed
    path.write_bytes(path.read_bytes() + b"\n# changed maintained boundary\n")
    assert getattr(target, function)() != before
