"""Explicit ownership cleanup for disposable browser-test process trees only."""

import os
import subprocess


def stop_process_tree(process) -> None:
    """Stop the exact Popen-owned test tree; never discover or terminate live apps."""
    if process.poll() is None:
        if os.name == "nt":
            subprocess.run(
                ["taskkill", "/PID", str(process.pid), "/T", "/F"],
                capture_output=True,
                timeout=20,
                check=False,
            )
        else:
            process.terminate()
        process.wait(timeout=40)
