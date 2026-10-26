"""Windows user-scoped DPAPI protection with explicit machine-bound entropy.

No LOCAL_MACHINE flag is used. Native buffers are freed with LocalFree. This
protects persistent authorization records, not against same-user host malware.
"""

import ctypes
import hashlib
import os
from ctypes import wintypes


class _Blob(ctypes.Structure):
    """Native DATA_BLOB; Python owns input buffers and Windows owns output."""

    _fields_ = [("size", wintypes.DWORD), ("data", ctypes.POINTER(ctypes.c_ubyte))]


class WindowsDataProtection:
    """Seal bounded data for the current Windows user and explicit machine ID."""

    def _transform(self, data: bytes, *, decrypt: bool) -> bytes:
        """Call noninteractive DPAPI and free the returned allocation on every exit.

        Parameters: bounded input bytes and operation direction. Returns copied
        output bytes. Raises OSError on unsupported/blocked/corrupt protection.
        Native APIs and the read-only machine identifier are loaded only on use.
        """
        if os.name != "nt" or not 1 <= len(data) <= 262144:
            raise OSError("Windows protection unavailable or input exceeds limit")
        import winreg

        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Cryptography",
            0,
            winreg.KEY_READ | winreg.KEY_WOW64_64KEY,
        ) as key:
            machine = winreg.QueryValueEx(key, "MachineGuid")[0]
        entropy = hashlib.sha256(("AgentiX/v3/approvals/" + machine).encode()).digest()
        source_buffer = (ctypes.c_ubyte * len(data)).from_buffer_copy(data)
        entropy_buffer = (ctypes.c_ubyte * len(entropy)).from_buffer_copy(entropy)
        source = _Blob(len(data), source_buffer)
        extra = _Blob(len(entropy), entropy_buffer)
        output = _Blob()
        api = ctypes.WinDLL("Crypt32.dll", use_last_error=True)
        kernel = ctypes.WinDLL("Kernel32.dll", use_last_error=True)
        function = api.CryptUnprotectData if decrypt else api.CryptProtectData
        function.argtypes = [
            ctypes.POINTER(_Blob),
            ctypes.c_void_p,
            ctypes.POINTER(_Blob),
            ctypes.c_void_p,
            ctypes.c_void_p,
            wintypes.DWORD,
            ctypes.POINTER(_Blob),
        ]
        function.restype = wintypes.BOOL
        kernel.LocalFree.argtypes = [ctypes.c_void_p]
        kernel.LocalFree.restype = ctypes.c_void_p
        try:
            if not function(
                ctypes.byref(source), None, ctypes.byref(extra), None, None, 1, ctypes.byref(output)
            ):
                raise OSError("Windows data protection failed")
            if not 1 <= output.size <= 262144:
                raise OSError("Protected output exceeds limit")
            return ctypes.string_at(output.data, output.size)
        finally:
            if output.data:
                kernel.LocalFree(ctypes.cast(output.data, ctypes.c_void_p))

    def seal(self, data: bytes) -> bytes:
        """Encrypt data plus an internal version/digest envelope; return opaque bytes."""
        return self._transform(
            b"AX-APPROVAL-1" + hashlib.sha256(data).digest() + data, decrypt=False
        )

    def unseal(self, data: bytes) -> bytes:
        """Decrypt and verify the envelope; malformed or modified records fail closed."""
        import hmac

        plain = self._transform(data, decrypt=True)
        prefix = b"AX-APPROVAL-1"
        offset = len(prefix)
        if not plain.startswith(prefix) or not hmac.compare_digest(
            plain[offset : offset + 32], hashlib.sha256(plain[offset + 32 :]).digest()
        ):
            raise ValueError("Invalid protected approval envelope")
        return plain[offset + 32 :]
