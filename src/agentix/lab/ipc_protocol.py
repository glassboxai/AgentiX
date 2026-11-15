"""Bounded JSON framing and explicit HTTP route policy for the native widget bridge."""

import json
import re
import struct
from urllib.parse import unquote

MAX_FRAME = 262144
MAX_BODY = 65536


def _pairs(pairs: list) -> dict:
    """Reject duplicate JSON names rather than authorizing ambiguous requests."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate message field")
        result[key] = value
    return result


def _constant(value: str) -> None:
    """Forbid JSON NaN and infinity across the process boundary."""
    raise ValueError("Nonfinite message value")


def decode_frame(payload: bytes) -> dict:
    """Decode one bounded object; no pickle, code or implicit deserialization."""
    if len(payload) > MAX_FRAME:
        raise ValueError("Message exceeds frame limit")
    try:
        value = json.loads(payload, object_pairs_hook=_pairs, parse_constant=_constant)
    except (RecursionError, UnicodeError) as error:
        raise ValueError("Invalid message") from error
    if not isinstance(value, dict):
        raise ValueError("Message must be an object")
    return value


def encode_frame(message: dict) -> bytes:
    """Prefix strict JSON bytes with a little-endian unsigned payload length."""
    try:
        payload = json.dumps(message, allow_nan=False, separators=(",", ":")).encode()
    except (TypeError, RecursionError) as error:
        raise ValueError("Unsupported message") from error
    decode_frame(payload)
    return struct.pack("<I", len(payload)) + payload


def validate_http_request(method: str, path: str, body: bytes) -> None:
    """Expose required Gradio endpoints, excluding arbitrary file/proxy/upload routes."""
    decoded = unquote(path)
    if (
        method not in ("GET", "POST", "HEAD")
        or len(body) > MAX_BODY
        or len(decoded) > 2048
        or "\\" in decoded
        or ".." in decoded.split("/")
    ):
        raise ValueError("Unsupported HTTP request")
    fixed = {
        "/",
        "/config",
        "/theme.css",
        "/favicon.ico",
        "/manifest.json",
        "/gradio_api/info",
        "/gradio_api/startup-events",
    }
    assets = re.fullmatch(r"/assets/[A-Za-z0-9_./-]+", decoded)
    events = re.fullmatch(r"/gradio_api/(run|call|queue|heartbeat)/[A-Za-z0-9_/-]+", decoded)
    if decoded not in fixed and not assets and not events:
        raise ValueError("Route not allowed")
