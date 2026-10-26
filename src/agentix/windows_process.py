"""Windows AppContainer process lifecycle with explicit native handle ownership.

Imports are inert and portable. Native APIs are loaded only for an explicit run.
No capabilities are granted. A suspended child must have an AppContainer token
and join the limited Job Object before it can execute application code.
"""

import ctypes as c
import os
import threading
from collections.abc import Iterator
from contextlib import contextmanager
from ctypes import wintypes as w
from typing import Any
from uuid import uuid4


class NativeWindows:
    """Own typed Win32 functions; fail on every unsuccessful security operation."""

    def __init__(self) -> None:
        """Load native libraries without modifying system or user policy."""
        self.kernel = c.WinDLL("kernel32", use_last_error=True)
        self.userenv = c.WinDLL("userenv", use_last_error=True)
        self.advapi = c.WinDLL("advapi32", use_last_error=True)
        self._handles: list[Any] = []

    def api(self, library: Any, name: str, result: Any, *arguments: Any) -> Any:
        """Declare ABI widths explicitly, including pointer-sized handles."""
        function = getattr(library, name)
        function.restype, function.argtypes = result, list(arguments)
        return function

    def checked(self, result: Any) -> Any:
        """Raise a native error without continuing with weakened restrictions."""
        if not result:
            raise c.WinError(c.get_last_error())
        return result

    def close(self) -> None:
        """Close owned handles in reverse order; closing the job kills descendants."""
        for handle in reversed(self._handles):
            self.kernel.CloseHandle(handle)
        self._handles.clear()

    @contextmanager
    def profile(self) -> Iterator[tuple[Any, str]]:
        """Create a unique no-capability profile, then delete it and free its SID."""
        name = "Agentix." + uuid4().hex
        sid = c.c_void_p()
        create = self.api(
            self.userenv,
            "CreateAppContainerProfile",
            c.c_long,
            w.LPCWSTR,
            w.LPCWSTR,
            w.LPCWSTR,
            c.c_void_p,
            w.DWORD,
            c.POINTER(c.c_void_p),
        )
        status = create(name, name, "Disposable Agentix execution", None, 0, c.byref(sid))
        if status < 0:
            raise OSError(
                f"AppContainer profile creation failed: HRESULT {status & 0xFFFFFFFF:08x}"
            )
        text_sid = w.LPWSTR()
        try:
            convert = self.api(
                self.advapi, "ConvertSidToStringSidW", w.BOOL, c.c_void_p, c.POINTER(w.LPWSTR)
            )
            self.checked(convert(sid, c.byref(text_sid)))
            yield sid, text_sid.value
        finally:
            self.close()
            delete = self.api(self.userenv, "DeleteAppContainerProfile", c.c_long, w.LPCWSTR)
            status = delete(name)
            if text_sid:
                self.api(self.kernel, "LocalFree", c.c_void_p, c.c_void_p)(text_sid)
            self.api(self.advapi, "FreeSid", c.c_void_p, c.c_void_p)(sid)
            if status < 0:
                raise OSError("Disposable AppContainer profile cleanup failed")

    def run(
        self,
        executable: str,
        command: str,
        cwd: str,
        sid: Any,
        *,
        timeout: float,
        memory: int,
        processes: int,
        max_output: int,
    ) -> tuple[int, bytes, str]:
        """Run a restricted child with bounded pipes and kill the complete job on failure."""

        # Structures mirror Windows SDK layouts; pointer-sized members must not
        # be replaced with DWORDs on 64-bit Windows.
        class SecurityAttributes(c.Structure):
            """SECURITY_ATTRIBUTES: only deliberately selected pipe handles inherit."""

            _fields_ = [("length", w.DWORD), ("descriptor", c.c_void_p), ("inherit", w.BOOL)]

        class Startup(c.Structure):
            """STARTUPINFOW ABI including the three standard handle slots."""

            _fields_ = [
                ("cb", w.DWORD),
                ("reserved", w.LPWSTR),
                ("desktop", w.LPWSTR),
                ("title", w.LPWSTR),
                ("x", w.DWORD),
                ("y", w.DWORD),
                ("xs", w.DWORD),
                ("ys", w.DWORD),
                ("xc", w.DWORD),
                ("yc", w.DWORD),
                ("fill", w.DWORD),
                ("flags", w.DWORD),
                ("show", w.WORD),
                ("reserved2", w.WORD),
                ("bytes", c.c_void_p),
                ("stdin", w.HANDLE),
                ("stdout", w.HANDLE),
                ("stderr", w.HANDLE),
            ]

        class ExtendedStartup(c.Structure):
            """STARTUPINFOEXW holds the validated capability and handle attributes."""

            _fields_ = [("startup", Startup), ("attributes", c.c_void_p)]

        class Process(c.Structure):
            """PROCESS_INFORMATION handles owned by this invocation."""

            _fields_ = [
                ("process", w.HANDLE),
                ("thread", w.HANDLE),
                ("pid", w.DWORD),
                ("tid", w.DWORD),
            ]

        class Capabilities(c.Structure):
            """SECURITY_CAPABILITIES grants the profile SID and zero capabilities."""

            _fields_ = [
                ("sid", c.c_void_p),
                ("capabilities", c.c_void_p),
                ("count", w.DWORD),
                ("reserved", w.DWORD),
            ]

        class BasicLimits(c.Structure):
            """JOBOBJECT_BASIC_LIMIT_INFORMATION with native pointer alignment."""

            _fields_ = [
                ("process_time", c.c_longlong),
                ("job_time", c.c_longlong),
                ("flags", w.DWORD),
                ("minimum", c.c_size_t),
                ("maximum", c.c_size_t),
                ("processes", w.DWORD),
                ("affinity", c.c_size_t),
                ("priority", w.DWORD),
                ("scheduling", w.DWORD),
            ]

        class Limits(c.Structure):
            """JOBOBJECT_EXTENDED_LIMIT_INFORMATION for memory/process bounds."""

            _fields_ = [
                ("basic", BasicLimits),
                ("io", c.c_ulonglong * 6),
                ("process_memory", c.c_size_t),
                ("job_memory", c.c_size_t),
                ("peak_process", c.c_size_t),
                ("peak_job", c.c_size_t),
            ]

        kernel = self.kernel
        close = self.api(kernel, "CloseHandle", w.BOOL, w.HANDLE)
        job = self.checked(
            self.api(kernel, "CreateJobObjectW", w.HANDLE, c.c_void_p, w.LPCWSTR)(None, None)
        )
        self._handles.append(job)
        limits = Limits()
        limits.basic.flags = 0x2000 | 0x200 | 0x8  # kill-on-close, job memory, process count
        limits.basic.processes, limits.job_memory = processes, memory
        self.checked(
            self.api(
                kernel, "SetInformationJobObject", w.BOOL, w.HANDLE, c.c_int, c.c_void_p, w.DWORD
            )(job, 9, c.byref(limits), c.sizeof(limits))
        )
        read, write = w.HANDLE(), w.HANDLE()
        attrs = SecurityAttributes(c.sizeof(SecurityAttributes), None, True)
        self.checked(
            self.api(
                kernel,
                "CreatePipe",
                w.BOOL,
                c.POINTER(w.HANDLE),
                c.POINTER(w.HANDLE),
                c.c_void_p,
                w.DWORD,
            )(c.byref(read), c.byref(write), c.byref(attrs), 0)
        )
        self._handles.extend([read, write])
        self.checked(
            self.api(kernel, "SetHandleInformation", w.BOOL, w.HANDLE, w.DWORD, w.DWORD)(read, 1, 0)
        )
        nul = self.api(
            kernel,
            "CreateFileW",
            w.HANDLE,
            w.LPCWSTR,
            w.DWORD,
            w.DWORD,
            c.c_void_p,
            w.DWORD,
            w.DWORD,
            w.HANDLE,
        )("NUL", 0x80000000, 3, c.byref(attrs), 3, 0, None)
        if nul == c.c_void_p(-1).value:
            raise c.WinError(c.get_last_error())
        self._handles.append(nul)
        size = c.c_size_t()
        init = self.api(
            kernel,
            "InitializeProcThreadAttributeList",
            w.BOOL,
            c.c_void_p,
            w.DWORD,
            w.DWORD,
            c.POINTER(c.c_size_t),
        )
        init(None, 2, 0, c.byref(size))
        buffer = c.create_string_buffer(size.value)
        self.checked(init(buffer, 2, 0, c.byref(size)))
        process = Process()
        reader = None
        output = bytearray()
        excessive = threading.Event()
        terminate = self.api(kernel, "TerminateJobObject", w.BOOL, w.HANDLE, w.UINT)
        try:
            update = self.api(
                kernel,
                "UpdateProcThreadAttribute",
                w.BOOL,
                c.c_void_p,
                w.DWORD,
                c.c_size_t,
                c.c_void_p,
                c.c_size_t,
                c.c_void_p,
                c.c_void_p,
            )
            caps = Capabilities(sid, None, 0, 0)
            self.checked(update(buffer, 0, 0x20009, c.byref(caps), c.sizeof(caps), None, None))
            inherited = (w.HANDLE * 2)(write, nul)
            self.checked(update(buffer, 0, 0x20002, inherited, c.sizeof(inherited), None, None))
            startup = ExtendedStartup()
            startup.startup.cb = c.sizeof(startup)
            startup.startup.flags = 0x100  # STARTF_USESTDHANDLES
            startup.startup.stdin, startup.startup.stdout, startup.startup.stderr = (
                nul,
                write,
                write,
            )
            startup.attributes = c.cast(buffer, c.c_void_p)
            # A minimal environment omits credentials, proxies and Python overrides.
            root = os.environ.get("SystemRoot", r"C:\Windows")
            # Windows requires LOCALAPPDATA while resolving the AppContainer
            # profile. Omitting it causes ERROR_ENVVAR_NOT_FOUND (203), even
            # though the executable and profile both exist. It conveys a path,
            # not access rights; the child token still enforces the ACL boundary.
            local_app_data = os.environ["LOCALAPPDATA"]
            environment = c.create_unicode_buffer(
                f"LOCALAPPDATA={local_app_data}\0SystemRoot={root}\0WINDIR={root}\0\0"
            )
            create = self.api(
                kernel,
                "CreateProcessW",
                w.BOOL,
                w.LPCWSTR,
                w.LPWSTR,
                c.c_void_p,
                c.c_void_p,
                w.BOOL,
                w.DWORD,
                c.c_void_p,
                w.LPCWSTR,
                c.c_void_p,
                c.POINTER(Process),
            )
            self.checked(
                create(
                    executable,
                    c.create_unicode_buffer(command),
                    None,
                    None,
                    True,
                    0x80000 | 0x400 | 0x4 | 0x08000000,
                    environment,
                    cwd,
                    c.byref(startup),
                    c.byref(process),
                )
            )
            self._handles.extend([process.process, process.thread])
            # No generated instruction runs before both identity and job checks.
            token = w.HANDLE()
            self.checked(
                self.api(
                    self.advapi, "OpenProcessToken", w.BOOL, w.HANDLE, w.DWORD, c.POINTER(w.HANDLE)
                )(process.process, 8, c.byref(token))
            )
            try:
                is_container, returned = w.DWORD(), w.DWORD()
                self.checked(
                    self.api(
                        self.advapi,
                        "GetTokenInformation",
                        w.BOOL,
                        w.HANDLE,
                        c.c_int,
                        c.c_void_p,
                        w.DWORD,
                        c.POINTER(w.DWORD),
                    )(token, 29, c.byref(is_container), 4, c.byref(returned))
                )
                if is_container.value != 1:
                    raise OSError("Child token is not AppContainer")
            finally:
                close(token)
            self.checked(
                self.api(kernel, "AssignProcessToJobObject", w.BOOL, w.HANDLE, w.HANDLE)(
                    job, process.process
                )
            )
            read_file = self.api(
                kernel,
                "ReadFile",
                w.BOOL,
                w.HANDLE,
                c.c_void_p,
                w.DWORD,
                c.POINTER(w.DWORD),
                c.c_void_p,
            )

            def drain() -> None:
                """Drain the pipe without allowing child-controlled memory growth."""
                chunk, count = c.create_string_buffer(4096), w.DWORD()
                while read_file(read, chunk, 4096, c.byref(count), None) and count.value:
                    available = max_output - len(output)
                    output.extend(chunk.raw[: min(count.value, available)])
                    if count.value > available:
                        excessive.set()
                        terminate(job, 122)
                        break

            reader = threading.Thread(target=drain, daemon=True)
            reader.start()
            resume = self.api(kernel, "ResumeThread", w.DWORD, w.HANDLE)(process.thread)
            if resume == 0xFFFFFFFF:
                raise c.WinError(c.get_last_error())
            # Close the host pipe writer now, otherwise EOF would never arrive.
            close(write)
            self._handles.remove(write)
            wait = self.api(kernel, "WaitForSingleObject", w.DWORD, w.HANDLE, w.DWORD)
            status = wait(process.process, int(timeout * 1000))
            failure = ""
            if status == 258:
                failure = "timeout"
            elif status != 0:
                failure = "wait_failed"
            terminate(job, 124 if failure else 0)  # Also terminate surviving children.
            wait(process.process, 5000)
            reader.join(5)
            if reader.is_alive():
                failure = "pipe_cleanup_failed"
            if excessive.is_set():
                failure = "output_limit"
            exit_code = w.DWORD()
            self.checked(
                self.api(kernel, "GetExitCodeProcess", w.BOOL, w.HANDLE, c.POINTER(w.DWORD))(
                    process.process, c.byref(exit_code)
                )
            )
            return exit_code.value if not failure else 124, bytes(output), failure
        finally:
            if process.process:
                # Terminate even when setup fails before job assignment.
                self.api(kernel, "TerminateProcess", w.BOOL, w.HANDLE, w.UINT)(process.process, 125)
            terminate(job, 125)
            if process.process:
                self.api(kernel, "WaitForSingleObject", w.DWORD, w.HANDLE, w.DWORD)(
                    process.process, 5000
                )
            if write in self._handles:
                close(write)
                self._handles.remove(write)
            if reader is not None:
                reader.join(5)
            self.api(kernel, "DeleteProcThreadAttributeList", None, c.c_void_p)(buffer)
