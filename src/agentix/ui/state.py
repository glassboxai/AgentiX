"""Workflow state and thread-safe stdout capture, without process-wide installation."""

import re
import threading
from collections import deque
from dataclasses import dataclass, field
from typing import Any, TextIO
from uuid import uuid4

ANSI_ESCAPE = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


class ConsoleThoughtsCapture:
    """Mirror output and expose a locked, ANSI-stripped activity snapshot.

    Construction never replaces sys.stdout. Retain at most 256 completed lines
    and one 4096-character partial line per session. Visible tails are capped at
    256 lines, so fragmented SDK output cannot grow indefinitely in memory.
    """

    def __init__(self, original_stdout: TextIO) -> None:
        """Retain the host stream and create a private lock/buffer."""
        self.original_stdout = original_stdout
        self.lock = threading.Lock()
        self.logs_buffer: deque[str] = deque(maxlen=256)
        self._partial = ""

    def write(self, text: str) -> None:
        """Retain Unicode activity and mirror it safely to the host console.

        Windows redirected consoles may reject CrewAI's emoji panels. Escape
        only that console copy instead of losing the owning GUI's verbose text.
        Other I/O errors still propagate; diagnostic events keep their own policy.
        """
        from ..credentials import redact

        text = redact(text)
        with self.lock:
            # Rich writes panels as many styled fragments. Reassemble logical
            # lines before stripping ANSI, including escape sequences split
            # across writes; otherwise a single panel consumes the whole tail.
            lines = (self._partial + text).split("\n")
            for line in lines[:-1]:
                clean = ANSI_ESCAPE.sub("", line).rstrip("\r")
                if clean.strip():
                    self.logs_buffer.append(clean[:4096])
            self._partial = lines[-1][:4096]
        try:
            self.original_stdout.write(text)
        except UnicodeEncodeError:
            self.original_stdout.write(
                text.encode("ascii", errors="backslashreplace").decode("ascii")
            )

    def flush(self) -> None:
        """Flush the underlying stream so server logs remain visible promptly."""
        self.original_stdout.flush()

    def isatty(self) -> bool:
        """Preserve terminal detection used by the server logging framework."""
        return getattr(self.original_stdout, "isatty", lambda: False)()

    def __getattr__(self, name: str) -> Any:
        """Delegate stream metadata such as encoding and file descriptors."""
        return getattr(self.original_stdout, name)

    def get_logs(self, max_lines: int = 35) -> str:
        """Return bounded logical lines, including an unfinished streaming line."""
        with self.lock:
            lines = list(self.logs_buffer)
            partial = ANSI_ESCAPE.sub("", self._partial)
            if partial.strip():
                lines.append(partial)
            return "\n".join(lines[-min(max_lines, 256) :])

    def clear(self) -> None:
        """Clear previous activity before a new workflow begins."""
        with self.lock:
            self.logs_buffer.clear()
            self._partial = ""


@dataclass
class ExecutionState:
    """Mutable state for one workflow owner, with an independent chat history.

    The history factory prevents accidental sharing between instances. Callers
    coordinating worker threads must still synchronize access appropriately.
    """

    is_running: bool = False
    session_id: str = field(default_factory=lambda: uuid4().hex)
    operation_id: str = ""
    last_response: str = ""
    error_message: str = ""
    chat_history: list[dict[str, str]] = field(default_factory=list)
    last_displayed_filepath: str | None = None
    last_displayed_request_id: str | None = None
    active_message_index: int | None = None
