"""LAB-003 native local named-pipe transport prerequisite; no model or host fallback."""

import ctypes
import json
import subprocess
import tempfile
import threading
from ctypes import wintypes
from pathlib import Path
from uuid import uuid4

import pytest

from agentix.sandbox import WindowsSandbox
from agentix.sandbox.windows_process import NativeWindows


@pytest.mark.windows_isolation
@pytest.mark.xfail(
    strict=True,
    raises=AssertionError,
    reason="LAB-003-NAMED-PIPE: host LOCAL name is not visible in current AppContainer namespace",
)
def test_appcontainer_duplex_named_pipe_round_trip():
    """Require real typed host-child exchange through a profile-scoped local pipe."""
    import pywintypes
    import win32api
    import win32con
    import win32event
    import win32file
    import win32pipe
    import win32security

    native = NativeWindows()
    with (
        native.profile() as (sid, sid_text),
        tempfile.TemporaryDirectory(prefix="agentix-ipc-probe-") as temporary,
    ):
        root = Path(temporary)
        runtime = root / "runtime"
        runtime.mkdir()
        WindowsSandbox._copy_runtime(runtime)
        pipe_name = r"\\.\pipe\LOCAL\AgentiX." + uuid4().hex
        token = win32security.OpenProcessToken(win32api.GetCurrentProcess(), win32con.TOKEN_QUERY)
        try:
            owner = win32security.GetTokenInformation(token, win32security.TokenUser)[0]
            owner_text = win32security.ConvertSidToStringSid(owner)
        finally:
            token.Close()
        descriptor = win32security.ConvertStringSecurityDescriptorToSecurityDescriptor(
            f"D:P(A;;GA;;;{owner_text})(A;;GRGW;;;{sid_text})", 1
        )
        attributes = pywintypes.SECURITY_ATTRIBUTES()
        attributes.SECURITY_DESCRIPTOR = descriptor
        pipe = win32pipe.CreateNamedPipe(
            pipe_name,
            win32pipe.PIPE_ACCESS_DUPLEX | win32file.FILE_FLAG_OVERLAPPED,
            win32pipe.PIPE_TYPE_BYTE | win32pipe.PIPE_READMODE_BYTE | win32pipe.PIPE_WAIT | 8,
            1,
            65536,
            65536,
            0,
            attributes,
        )
        source = f"""import json
try:
    with open({pipe_name!r}, 'r+b', buffering=0) as pipe:
        pipe.write(b'{{"kind":"hello","value":41}}\\n')
        reply = bytearray()
        while len(reply) < 4096:
            chunk = pipe.read(1)
            if not chunk:
                break
            reply.extend(chunk)
            if chunk == b'\\n':
                break
        print(json.dumps({{"reply":json.loads(reply)}}), flush=True)
except OSError as error:
    print(json.dumps({{"error_type":type(error).__name__,"winerror":getattr(error,"winerror",None)}}), flush=True)
"""
        worker = root / "ipc_probe.py"
        worker.write_text(source)
        grant = subprocess.run(
            [
                "C:\\Windows\\System32\\icacls.exe",
                str(root),
                "/grant",
                f"*{sid_text}:(OI)(CI)RX",
                "/T",
                "/Q",
            ],
            capture_output=True,
            timeout=30,
            check=False,
        )
        assert grant.returncode == 0
        observation = {}

        def run():
            """Own native child handles; job kills all descendants on exit or deadline."""
            try:
                observation["native"] = native.run(
                    str(runtime / "python.exe"),
                    subprocess.list2cmdline(
                        [str(runtime / "python.exe"), "-I", "-S", "-B", str(worker)]
                    ),
                    str(root),
                    sid,
                    timeout=10,
                    memory=512 * 1024 * 1024,
                    processes=2,
                    max_output=65536,
                )
            except Exception as error:
                observation["error"] = type(error).__name__

        connect = pywintypes.OVERLAPPED()
        connect.hEvent = win32event.CreateEvent(None, True, False, None)
        connected = False
        thread = threading.Thread(target=run)
        try:
            try:
                win32pipe.ConnectNamedPipe(pipe, connect)
            except pywintypes.error as error:
                if error.winerror != 997:
                    raise
            thread.start()
            connected = (
                win32event.WaitForSingleObject(connect.hEvent, 12000) == win32event.WAIT_OBJECT_0
            )
            if connected:
                read = pywintypes.OVERLAPPED()
                read.hEvent = win32event.CreateEvent(None, True, False, None)
                try:
                    _, data = win32file.ReadFile(pipe, 4096, read)
                    if (
                        win32event.WaitForSingleObject(read.hEvent, 3000)
                        != win32event.WAIT_OBJECT_0
                    ):
                        raise RuntimeError("Pipe read deadline")
                    count = win32file.GetOverlappedResult(pipe, read, False)
                    assert json.loads(bytes(data[:count])) == {"kind": "hello", "value": 41}
                finally:
                    read.hEvent.Close()
                write = pywintypes.OVERLAPPED()
                write.hEvent = win32event.CreateEvent(None, True, False, None)
                try:
                    win32file.WriteFile(pipe, b'{"value":42}\n', write)
                    if (
                        win32event.WaitForSingleObject(write.hEvent, 3000)
                        != win32event.WAIT_OBJECT_0
                    ):
                        raise RuntimeError("Pipe write deadline")
                    win32file.GetOverlappedResult(pipe, write, False)
                finally:
                    write.hEvent.Close()
        finally:
            native.api(
                native.kernel, "CancelIoEx", wintypes.BOOL, wintypes.HANDLE, ctypes.c_void_p
            )(int(pipe), None)
            pipe.Close()
            connect.hEvent.Close()
            if thread.ident is not None:
                thread.join(20)
        print(
            json.dumps(
                {
                    "connected": connected,
                    "thread_stopped": not thread.is_alive(),
                    "observation": observation,
                },
                default=lambda value: value.decode() if isinstance(value, bytes) else str(value),
                indent=2,
            )
        )
        assert not thread.is_alive()
        assert connected, (
            "LAB-003-IPC: isolated client cannot reach owner/profile-scoped local pipe"
        )
        assert observation["native"][0] == 0
        assert not observation["native"][2]
        assert json.loads(observation["native"][1]) == {"reply": {"value": 42}}


@pytest.mark.windows_isolation
def test_appcontainer_duplex_inherited_pipe_round_trip():
    """Require profile-independent duplex IPC via explicit inherited pipe handles."""
    import time

    import pywintypes
    import win32api
    import win32con
    import win32file
    import win32pipe

    native = NativeWindows()
    attributes = pywintypes.SECURITY_ATTRIBUTES()
    attributes.bInheritHandle = True
    child_read, host_write = win32pipe.CreatePipe(attributes, 65536)
    host_read, child_write = win32pipe.CreatePipe(attributes, 65536)
    for handle in (host_write, host_read):
        win32api.SetHandleInformation(handle, win32con.HANDLE_FLAG_INHERIT, 0)
    with (
        native.profile() as (sid, sid_text),
        tempfile.TemporaryDirectory(prefix="agentix-inherited-ipc-") as temporary,
    ):
        root = Path(temporary)
        runtime = root / "runtime"
        runtime.mkdir()
        WindowsSandbox._copy_runtime(runtime)
        worker = root / "inherited_probe.py"
        worker.write_text(f"""import json,os,msvcrt
reader = msvcrt.open_osfhandle({int(child_read)}, os.O_RDONLY | os.O_BINARY)
writer = msvcrt.open_osfhandle({int(child_write)}, os.O_WRONLY | os.O_BINARY)
request = json.loads(os.read(reader, 4096))
os.write(writer, json.dumps({{"value":request["value"]+1}}).encode())
print("inherited IPC completed", flush=True)
""")
        grant = subprocess.run(
            [
                "C:\\Windows\\System32\\icacls.exe",
                str(root),
                "/grant",
                f"*{sid_text}:(OI)(CI)RX",
                "/T",
                "/Q",
            ],
            capture_output=True,
            timeout=30,
            check=False,
        )
        if grant.returncode:
            raise RuntimeError("Cannot stage native probe")
        observation = {}

        def run():
            """Execute through the same verified token/job lifecycle as ordinary tools."""
            try:
                observation["result"] = native.run(
                    str(runtime / "python.exe"),
                    subprocess.list2cmdline(
                        [str(runtime / "python.exe"), "-I", "-S", "-B", str(worker)]
                    ),
                    str(root),
                    sid,
                    timeout=10,
                    memory=512 * 1024 * 1024,
                    processes=2,
                    max_output=65536,
                    channel_handles=(int(child_read), int(child_write)),
                )
            except Exception as error:
                observation["error"] = type(error).__name__

        thread = threading.Thread(target=run)
        thread.start()
        response = b""
        try:
            win32file.WriteFile(host_write, b'{"value":41}')
            deadline = time.monotonic() + 15
            while time.monotonic() < deadline:
                available = win32pipe.PeekNamedPipe(host_read, 0)[1]
                if available:
                    response = win32file.ReadFile(host_read, min(available, 4096))[1]
                    break
                if "error" in observation or not thread.is_alive():
                    break
                time.sleep(0.02)
        finally:
            thread.join(20)
            for handle in (child_read, child_write, host_read, host_write):
                handle.Close()
        print(
            json.dumps(
                {
                    "response": response.decode(),
                    "observation": observation,
                    "stopped": not thread.is_alive(),
                },
                default=lambda value: value.decode() if isinstance(value, bytes) else str(value),
            )
        )
        assert not thread.is_alive()
        assert "error" not in observation, observation
        assert json.loads(response) == {"value": 42}
        assert observation["result"][0] == 0 and not observation["result"][2]
