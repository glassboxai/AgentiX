"""Windows Credential Manager adapter and host-output secret redaction.

Generic credentials are protected by the Windows user boundary, not against
malware running as that same user. No secret is written into project files or
process environment variables. Saved targets persist until explicit deletion; ephemeral targets are removed on cleanup.
"""

import ctypes
import logging
import os
import threading
from collections.abc import Callable
from ctypes import wintypes
from typing import Any

from .profile_errors import ProfileError

_values: set[str] = set()
_lock = threading.RLock()


def redact(text: str) -> str:
    """Replace registered API key values before publishing host output."""
    with _lock:
        for value in sorted(_values, key=len, reverse=True):
            text = text.replace(value, "[REDACTED]")
    return text


def register_secret(value: str) -> None:
    """Register a bounded key for process-lifetime redaction, or deny capacity."""
    if (
        not isinstance(value, str)
        or not 8 <= len(value) <= 2048
        or any(ord(c) < 33 or ord(c) > 126 for c in value)
    ):
        raise ProfileError("key_format")
    with _lock:
        if len(_values) >= 128 and value not in _values:
            raise ProfileError("key_capacity")
        _values.add(value)


class SecretFilter(logging.Filter):
    """Redact formatted vendor log messages and exception text at host handlers."""

    def filter(self, record: logging.LogRecord) -> bool:
        """Normalize messages without exposing original formatting arguments."""
        record.msg = redact(record.getMessage())
        record.args = ()
        if record.exc_info:
            record.exc_text = redact(logging.Formatter().formatException(record.exc_info))
            record.exc_info = None
        return True


class _Credential(ctypes.Structure):
    """Native CREDENTIALW layout; blob bytes are copied then freed by Windows."""

    _fields_ = [
        ("Flags", wintypes.DWORD),
        ("Type", wintypes.DWORD),
        ("TargetName", wintypes.LPWSTR),
        ("Comment", wintypes.LPWSTR),
        ("LastWritten", wintypes.FILETIME),
        ("CredentialBlobSize", wintypes.DWORD),
        ("CredentialBlob", ctypes.POINTER(ctypes.c_ubyte)),
        ("Persist", wintypes.DWORD),
        ("AttributeCount", wintypes.DWORD),
        ("Attributes", ctypes.c_void_p),
        ("TargetAlias", wintypes.LPWSTR),
        ("UserName", wintypes.LPWSTR),
    ]


class WindowsCredentialVault:
    """Generic user-and-machine persistent credentials addressed by opaque owned targets."""

    def __init__(self) -> None:
        """Load user-level Windows APIs; fail closed on unsupported systems."""
        if os.name != "nt":
            raise RuntimeError("Windows Credential Manager is required")
        self.api = ctypes.WinDLL("Advapi32.dll", use_last_error=True)
        self.api.CredWriteW.argtypes = [ctypes.POINTER(_Credential), wintypes.DWORD]
        self.api.CredWriteW.restype = wintypes.BOOL
        self.api.CredReadW.argtypes = [
            wintypes.LPCWSTR,
            wintypes.DWORD,
            wintypes.DWORD,
            ctypes.POINTER(ctypes.POINTER(_Credential)),
        ]
        self.api.CredReadW.restype = wintypes.BOOL
        self.api.CredDeleteW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD]
        self.api.CredDeleteW.restype = wintypes.BOOL
        self.api.CredFree.argtypes = [ctypes.c_void_p]

    @staticmethod
    def _target(reference: str) -> str:
        """Constrain every access to the application namespace."""
        import re

        if not isinstance(reference, str) or not re.fullmatch(
            r"AgentiX/v3/[a-f0-9]{32}/[a-f0-9]{32}", reference
        ):
            raise ValueError("Invalid credential reference")
        return reference

    def write(self, reference: str, key: str) -> None:
        """Store a key without filesystem or environment persistence."""
        reference = self._target(reference)
        register_secret(key)
        blob = key.encode("utf-16-le")
        if len(blob) > 2560:
            raise ProfileError("key_storage_limit")
        buffer = (ctypes.c_ubyte * len(blob)).from_buffer_copy(blob)
        credential = _Credential(
            Type=1,
            TargetName=reference,
            CredentialBlobSize=len(blob),
            CredentialBlob=buffer,
            Persist=2,
            UserName="AgentiX",
        )
        if not self.api.CredWriteW(ctypes.byref(credential), 0):
            raise ProfileError("credential_write", ctypes.get_last_error())

    def read(self, reference: str) -> str:
        """Read an owned key; free the native allocation even on decoding failure."""
        reference = self._target(reference)
        pointer = ctypes.POINTER(_Credential)()
        if not self.api.CredReadW(reference, 1, 0, ctypes.byref(pointer)):
            raise ProfileError("credential_read", ctypes.get_last_error())
        try:
            value = ctypes.string_at(
                pointer.contents.CredentialBlob, pointer.contents.CredentialBlobSize
            ).decode("utf-16-le")
            register_secret(value)
            return value
        finally:
            self.api.CredFree(pointer)

    def delete(self, reference: str) -> None:
        """Remove one owned target; missing targets are already compliant."""
        reference = self._target(reference)
        if not self.api.CredDeleteW(reference, 1, 0) and ctypes.get_last_error() != 1168:
            raise ProfileError("credential_delete", ctypes.get_last_error())


class DeferredCredentialVault:
    """Defer native credential construction until a credential operation is needed.

    Local metadata operations never call the factory. SavedProfiles serializes its
    writes; the lock also protects lazy construction for concurrent read callers.
    """

    def __init__(self, factory: Callable[[], Any]) -> None:
        """Retain the injected factory without accessing the Windows API."""
        self.factory = factory
        self._instance = None
        self._instance_lock = threading.RLock()

    def _backend(self) -> Any:
        """Create the native boundary once, replacing unsafe initialization errors."""
        with self._instance_lock:
            if self._instance is None:
                try:
                    self._instance = self.factory()
                except Exception:
                    raise ProfileError("credential_unavailable") from None
            return self._instance

    def write(self, reference: str, key: str) -> None:
        """Write only an explicitly requested credential through the lazy backend."""
        self._backend().write(reference, key)

    def read(self, reference: str) -> str:
        """Read only the selected opaque reference through the lazy backend."""
        return self._backend().read(reference)

    def delete(self, reference: str) -> None:
        """Delete only an explicitly owned reference through the lazy backend."""
        self._backend().delete(reference)
