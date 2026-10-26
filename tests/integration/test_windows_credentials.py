"""Opt-in native Windows Credential Manager verification using a disposable key."""

import hashlib
import os
import subprocess
import sys
from pathlib import Path
from uuid import uuid4

import pytest

pytestmark = [
    pytest.mark.windows_credentials,
    pytest.mark.skipif(os.name != "nt", reason="Windows only"),
]


def test_real_windows_credential_roundtrip_and_delete():
    """Write/read/delete one unique test target; never access existing credentials."""
    from agentix.credentials import WindowsCredentialVault, redact

    vault = WindowsCredentialVault()
    target = f"AgentiX/v3/{uuid4().hex}/{uuid4().hex}"
    key = "synthetic-test-key-" + uuid4().hex
    try:
        vault.write(target, key)
        assert vault.read(target) == key
        child = subprocess.run(
            [
                sys.executable,
                "-c",
                "import _agentix_path,sys,hashlib; from agentix.credentials import WindowsCredentialVault; print(hashlib.sha256(WindowsCredentialVault().read(sys.argv[1]).encode()).hexdigest())",
                target,
            ],
            cwd=Path(__file__).resolve().parents[2],
            capture_output=True,
            text=True,
            timeout=20,
        )
        assert child.returncode == 0, child.stderr
        assert child.stdout.strip() == hashlib.sha256(key.encode()).hexdigest()
        assert key not in redact("Authorization: Bearer " + key)
    finally:
        vault.delete(target)
    with pytest.raises(ValueError, match="unavailable"):
        vault.read(target)
