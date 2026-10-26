"""Disposable standard-library Python execution in a native Windows AppContainer.

No host execution fallback exists. Only trusted runtime files, the trusted worker
and explicit input bytes are copied; no project directories are mounted/shared.
"""

import json
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .diagnostics import log_event

logger = logging.getLogger(__name__)


class IsolationUnavailable(RuntimeError):
    """The requested OS boundary could not be provisioned; execution is denied."""


@dataclass(frozen=True)
class SandboxResult:
    """Host observation plus an explicitly untrusted child-authored report."""

    exit_code: int
    output: str
    report: dict[str, Any] | None
    isolated: bool
    failure: str = ""


def decode_report(output: str) -> dict[str, Any]:
    """Require one complete bounded JSON frame; never parse plain success text."""
    from .acceptance import _unique

    frames = [
        line.removeprefix("AGENTIX_REPORT:")
        for line in output.splitlines()
        if line.startswith("AGENTIX_REPORT:")
    ]
    if len(frames) != 1:
        raise ValueError("Missing or ambiguous sandbox report")
    report = json.loads(frames[0], object_pairs_hook=_unique)
    if not isinstance(report, dict):
        raise ValueError("Sandbox report must be an object")
    if report.get("kind") == "call" and set(report) == {"kind", "result"}:
        if isinstance(report["result"], str):
            return report
    elif report.get("kind") == "observation":
        from .acceptance import validate_json

        validate_json(report)
        if (
            report.get("status") == "returned"
            and set(report) == {"kind", "status", "value"}
            or report.get("status") == "raised"
            and set(report) == {"kind", "status", "exception_type"}
            and isinstance(report["exception_type"], str)
        ):
            return report
    elif report.get("kind") == "tests" and set(report) == {
        "kind",
        "run",
        "failures",
        "errors",
        "skipped",
        "successful",
    }:
        if (
            all(
                type(report[key]) is int and report[key] >= 0
                for key in ("run", "failures", "errors", "skipped")
            )
            and type(report["successful"]) is bool
        ):
            return report
    raise ValueError("Invalid sandbox report schema")


class WindowsSandbox:
    """Provision a fresh runtime/profile/job per invocation; never reuse child state."""

    def __init__(
        self,
        *,
        timeout: float = 30,
        memory: int = 512 * 1024 * 1024,
        processes: int = 8,
        max_output: int = 256 * 1024,
    ) -> None:
        """Set finite host-enforced bounds without starting native work."""
        if not (
            0 < timeout <= 120
            and 16 * 1024 * 1024 <= memory <= 1024**3
            and 1 <= processes <= 16
            and 1024 <= max_output <= 1024**2
        ):
            raise ValueError("Invalid sandbox resource limits")
        self.timeout, self.memory = timeout, memory
        self.processes, self.max_output = processes, max_output

    def execute(
        self,
        code: bytes,
        tests: bytes | None,
        tool_name: str,
        function_name: str,
        kwargs: dict[str, Any],
        *,
        observation: bool = False,
    ) -> SandboxResult:
        """Copy inputs and execute only after all OS restrictions are established.

        Raises IsolationUnavailable on unsupported hosts/setup failures. A timeout,
        failed child or malformed report is returned as an unsuccessful result.
        Provisioning time is separate from the child execution deadline.
        """
        if sys.platform != "win32":
            raise IsolationUnavailable("Native Windows AppContainer is required")
        if not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", tool_name):
            raise ValueError("Invalid sandbox module name")
        if len(code) > 1024**2 or (tests is not None and len(tests) > 1024**2):
            raise ValueError("Sandbox input exceeds 1 MiB per artifact")
        from .windows_process import NativeWindows

        started = time.monotonic()
        log_event(logger, "sandbox_provisioning")
        try:
            native = NativeWindows()
            with (
                native.profile() as (sid, sid_text),
                tempfile.TemporaryDirectory(prefix="agentix-isolated-") as temporary,
            ):
                root = Path(temporary)
                runtime, work = root / "runtime", root / "work"
                runtime.mkdir()
                work.mkdir()
                self._copy_runtime(runtime)
                shutil.copyfile(Path(__file__).with_name("sandbox_worker.py"), work / "worker.py")
                (work / f"{tool_name}_code.py").write_bytes(code)
                if tests is not None:
                    (work / f"{tool_name}_tests.py").write_bytes(tests)
                request = dict(
                    kind="tests" if tests is not None else "observation" if observation else "call",
                    tool_name=tool_name,
                    function_name=function_name,
                    kwargs=kwargs,
                )
                (work / "request.json").write_text(json.dumps(request), encoding="utf-8")
                # Explicit SID-only read/execute grant, never ALL APPLICATION
                # PACKAGES. Child receives no write access to staged input files.
                icacls = Path(os.environ.get("SystemRoot", r"C:\Windows")) / "System32/icacls.exe"
                grant = subprocess.run(
                    [str(icacls), str(root), "/grant", f"*{sid_text}:(OI)(CI)RX", "/T", "/Q"],
                    capture_output=True,
                    timeout=30,
                    check=False,
                    creationflags=subprocess.CREATE_NO_WINDOW,
                )
                if grant.returncode:
                    raise IsolationUnavailable("Cannot provision sandbox file permissions")
                executable = runtime / "python.exe"
                command = subprocess.list2cmdline(
                    [str(executable), "-I", "-S", "-B", str(work / "worker.py")]
                )
                exit_code, output, failure = native.run(
                    str(executable),
                    command,
                    str(work),
                    sid,
                    timeout=self.timeout,
                    memory=self.memory,
                    processes=self.processes,
                    max_output=self.max_output,
                )
                decoded = output.decode("utf-8", errors="replace")
                report = None
                if not failure:
                    try:
                        report = decode_report(decoded)
                    except (ValueError, RecursionError):
                        failure = "invalid_report"
                result = SandboxResult(exit_code, decoded, report, True, failure)
        except IsolationUnavailable:
            log_event(logger, "sandbox_unavailable", level=logging.ERROR)
            raise
        except Exception as exc:
            log_event(logger, "sandbox_setup_failed", error=exc, level=logging.ERROR)
            raise IsolationUnavailable("Native isolation setup or cleanup failed") from exc
        logger.info(
            "event=sandbox_finished duration_seconds=%.3f exit_code=%d failure=%s",
            time.monotonic() - started,
            result.exit_code,
            result.failure or "none",
        )
        return result

    def evaluate(
        self, code: bytes, tool_name: str, function_name: str, kwargs: dict[str, Any]
    ) -> SandboxResult:
        """Observe one function call in a new child without supplying expected values."""
        return self.execute(code, None, tool_name, function_name, kwargs, observation=True)

    @staticmethod
    def _copy_runtime(destination: Path) -> None:
        """Stage CPython's standard library; never copy site-packages or the project."""
        base = Path(sys.base_prefix)
        shutil.copyfile(base / "python.exe", destination / "python.exe")
        for filename in base.glob("*.dll"):
            shutil.copyfile(filename, destination / filename.name)
        ignore = shutil.ignore_patterns(
            "site-packages",
            "__pycache__",
            "test",
            "tests",
            "ensurepip",
            "idlelib",
            "tkinter",
            "turtledemo",
        )
        for directory in ("Lib", "DLLs"):
            shutil.copytree(base / directory, destination / directory, ignore=ignore)
