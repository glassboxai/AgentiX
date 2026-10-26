"""Opt-in Windows DPAPI integrity and cross-process approval persistence."""

import os
import subprocess
import sys
from pathlib import Path

import pytest

pytestmark = [
    pytest.mark.windows_credentials,
    pytest.mark.skipif(os.name != "nt", reason="Windows DPAPI required"),
]


def test_dpapi_survives_new_process_and_rejects_altered_blob(tmp_path):
    """The real user/machine protector restores after restart and rejects corruption."""
    from agentix.data_protection import WindowsDataProtection

    protector = WindowsDataProtection()
    payload = b"synthetic-reviewed-approval-data"
    protected = protector.seal(payload)
    assert payload not in protected
    path = tmp_path / "approval.bin"
    path.write_bytes(protected)
    script = "import _agentix_path; from pathlib import Path; from agentix.data_protection import WindowsDataProtection; import sys; assert WindowsDataProtection().unseal(Path(sys.argv[1]).read_bytes()) == b'synthetic-reviewed-approval-data'; print('dpapi-cross-process-ok')"
    result = subprocess.run(
        [sys.executable, "-c", script, str(path)],
        cwd=Path(__file__).resolve().parents[2],
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, result.stderr
    assert "dpapi-cross-process-ok" in result.stdout
    for corrupt in (
        b"plaintext approved",
        protected[:-20],
        protected[:-1] + bytes([protected[-1] ^ 1]),
    ):
        with pytest.raises((OSError, ValueError)):
            protector.unseal(corrupt)
