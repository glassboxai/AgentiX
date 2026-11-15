"""LAB-003 framing and bridge policies reject data before native dispatch."""

import pytest

from agentix.lab.ipc_protocol import decode_frame, encode_frame, validate_http_request


def test_frames_preserve_json_and_reject_duplicates_or_executable_values():
    """Catch ambiguous messages, coercion and unbounded cross-process data."""
    message = {"type": "request", "id": "a", "value": 0}
    wire = encode_frame(message)
    assert decode_frame(wire[4:]) == message
    for raw in (b'{"id":"a","id":"b"}', b"[]", b'{"n":NaN}'):
        with pytest.raises(ValueError):
            decode_frame(raw)
    with pytest.raises(ValueError):
        encode_frame({"body": "x" * 262145})


@pytest.mark.parametrize(
    "method,path",
    [("GET", "/"), ("GET", "/assets/index.js"), ("POST", "/gradio_api/run/vowels_first")],
)
def test_bridge_admits_only_supported_http_routes(method, path):
    """Catch accidental rejection of required Gradio startup and event routes."""
    validate_http_request(method, path, b"")


@pytest.mark.parametrize(
    "method,path",
    [
        ("DELETE", "/"),
        ("GET", "/gradio_api/file=/secret"),
        ("POST", "/gradio_api/upload"),
        ("GET", "/../secret"),
        ("GET", "/assets/../../secret"),
    ],
)
def test_bridge_denies_files_uploads_and_unknown_methods(method, path):
    """Catch host filesystem/proxy features leaking through the HTTP bridge."""
    with pytest.raises(ValueError):
        validate_http_request(method, path, b"")


def test_bridge_checks_origin_and_streams_bounded_response():
    """Exercise the real ASGI bridge, observing HTTP rejection and streamed payload."""
    import asyncio
    import base64

    import httpx

    from agentix.lab.widget_bridge import WidgetBridge

    class Session:
        """Deterministic IPC boundary double; the maintained HTTP policy remains real."""

        def events(self, *args, **kwargs):
            yield {
                "type": "start",
                "status": 200,
                "headers": [["content-type", "text/plain"], ["set-cookie", "not-forwarded"]],
            }
            yield {"type": "body", "data": base64.b64encode(b"foo").decode(), "more": True}
            yield {"type": "body", "data": base64.b64encode(b"bar").decode(), "more": False}

    async def exercise():
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=WidgetBridge(Session(), 7875)),
            base_url="http://127.0.0.1:7875",
        ) as client:
            response = await client.get("/")
            assert response.content == b"foobar"
            assert "set-cookie" not in response.headers
            assert "connect-src 'self'" in response.headers["content-security-policy"]
            assert (
                await client.post(
                    "/gradio_api/run/vowels_first", headers={"Origin": "https://untrusted.example"}
                )
            ).status_code == 403
            assert (await client.get("/gradio_api/file=/secret")).status_code == 403
            assert (await client.get("/", headers={"Host": "untrusted.example"})).status_code == 403

    asyncio.run(exercise())


@pytest.mark.parametrize("seconds", [0, -1, 601, True])
def test_preview_rejects_unbounded_lifetime(seconds):
    """A caller cannot turn the isolated preview into an unbounded background job."""
    from agentix.lab.widget_session import WidgetSession

    with pytest.raises(ValueError):
        WidgetSession(lifetime=seconds)


def test_invalid_tool_input_reports_error_without_killing_preview():
    """Validation failure is recoverable and must not cancel the whole native UI."""
    from agentix.lab.widget_session import WidgetSession

    session = WidgetSession()
    messages = []
    session._write = messages.append
    session.tool_slots.acquire()
    try:
        session._invoke_tool(
            {"type": "tool", "id": "a" * 32, "instance": "first", "text": "x" * 16001}
        )
        assert not session.cancel.is_set()
        assert messages[0]["result"] == {}
    finally:
        session.close()


def test_unapproved_widget_bytes_never_start_a_native_process():
    """Callers must present the reviewed capability, not arbitrary source bytes."""
    from agentix.lab.widget_session import WidgetSession

    with pytest.raises(ValueError):
        WidgetSession(b'print("unapproved")')


def test_partial_staging_failure_removes_private_runtime(monkeypatch):
    """A failed dependency stage must not leak its owned temporary directory."""
    from agentix.lab import widget_session

    def fail(root):
        raise RuntimeError("synthetic staging failure")

    monkeypatch.setattr(widget_session, "stage_runtime", fail)
    session = widget_session.WidgetSession()
    with pytest.raises(RuntimeError, match="synthetic staging failure"):
        session.__enter__()
    assert not session.root.exists()


def test_bridge_frame_policy_allows_only_explicit_lab_origin():
    """Embedding must never turn into an unrestricted frame-ancestors wildcard."""
    import asyncio
    import base64

    import httpx

    from agentix.lab.widget_bridge import WidgetBridge

    class Session:
        """Replace only the external IPC events with a literal response."""

        def events(self, *args, **kwargs):
            yield {"type": "start", "status": 200, "headers": []}
            yield {"type": "body", "data": base64.b64encode(b"ok").decode(), "more": False}

    async def check():
        app = WidgetBridge(Session(), 50001, parent_origin="http://127.0.0.1:7874")
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://127.0.0.1:50001"
        ) as client:
            result = await client.get("/")
            assert (
                "frame-ancestors http://127.0.0.1:7874" in result.headers["content-security-policy"]
            )
            assert "frame-ancestors *" not in result.headers["content-security-policy"]

    asyncio.run(check())
    with pytest.raises(ValueError):
        WidgetBridge(Session(), 50001, parent_origin="https://untrusted.example")
