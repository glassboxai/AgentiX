"""Bounded local model transport and legacy compatibility application roles.

These agents propose artifacts, never approval. Engineering code/tests are not
produced through this service; only explicit application generation invokes it.
"""

import ast
import json
import logging
import threading
import time
from collections.abc import Callable
from pathlib import Path
from urllib.request import ProxyHandler, Request, build_opener
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

from agentix.lab.ipc_protocol import decode_frame
from agentix.lab.widget_designer import NoRedirect

logger = logging.getLogger(__name__)

# Bounded local transport: one process-wide inference, bounded wait and response.
DEFAULT_MODEL_TIMEOUT_SECONDS = 120
MAX_MODEL_TIMEOUT_SECONDS = 600
MODEL_KEEP_ALIVE = "30s"
MODEL_TEMPERATURE = 0.1
MAX_MODEL_OUTPUT_TOKENS = 4096
MAX_MODEL_RESPONSE_BYTES = 262144

# Proposal envelopes: schema length in characters, size checks in UTF-8 bytes.
MAX_PROPOSAL_FIELD_LENGTH = 65536
MAX_PROPOSAL_FIELD_BYTES = 65536
MAX_APPLICATION_QUERY_LENGTH = 16000

# Evidence stage labels; also the accepted application role identities.
ROLE_WIDGET_DESIGNER = "Widget Designer"
ROLE_GENERAL_WIDGET_DESIGNER = "General Widget Designer"
ROLE_GENERAL_ASSEMBLER = "General Assembler"
APPLICATION_ROLES = frozenset(
    {
        ROLE_WIDGET_DESIGNER,
        ROLE_GENERAL_WIDGET_DESIGNER,
        ROLE_GENERAL_ASSEMBLER,
    }
)

MODEL_GATE = threading.BoundedSemaphore(1)


class WidgetProposal(BaseModel):
    """Strict proposed artifact envelope; source remains untrusted data."""

    model_config = ConfigDict(extra="forbid", strict=True)
    widget_code: str = Field(max_length=MAX_PROPOSAL_FIELD_LENGTH)
    tests_code: str = Field(max_length=MAX_PROPOSAL_FIELD_LENGTH)
    notes: str = Field(max_length=MAX_PROPOSAL_FIELD_LENGTH)


class LocalModelClient:
    """Legacy pilot/fixture transport; production catalog creation uses CrewAI coordination."""

    def __init__(self, evidence: Path, *, timeout: int = DEFAULT_MODEL_TIMEOUT_SECONDS) -> None:
        """Inject operation evidence and a strict bounded HTTP wait in seconds.

        The default remains 120 seconds. A composition root may explicitly allow
        up to 600 seconds; invalid values fail before evidence or model activity.
        """
        if type(timeout) is not int or not 1 <= timeout <= MAX_MODEL_TIMEOUT_SECONDS:
            raise ValueError("Application model timeout must be an integer from 1 to 600 seconds")
        self.evidence = evidence
        # Per-client HTTP wait, owned by this session; never an unbounded retry.
        self.timeout = timeout

    def __call__(self, role: str, content: dict) -> dict:
        """Persist exact request/response; propagate errors without automatic retries.

        At most one application inference runs process-wide. The injected HTTP timeout
        is bounded to 600 seconds; response is bounded; model residency is requested for 30 seconds.
        Ollama is shared, so residency is a request, not ownership of the service.
        """
        if role not in APPLICATION_ROLES:
            raise ValueError("Unknown application role")
        if not MODEL_GATE.acquire(blocking=False):
            raise ValueError("Another application model operation is active")
        identity = uuid4().hex
        started = time.monotonic()
        try:
            self.evidence.mkdir(parents=True, exist_ok=True)
            from agentix.domain.application_code import ApplicationCode

            response_contract = WidgetProposal if "Widget" in role else ApplicationCode
            schema = response_contract.model_json_schema()
            payload = {
                "model": "qwen3-coder:30b",
                "stream": False,
                "format": schema,
                "keep_alive": MODEL_KEEP_ALIVE,
                "messages": [
                    {"role": "system", "content": content["system"]},
                    {"role": "user", "content": json.dumps(content["requirements"])},
                ],
                "options": {
                    "temperature": MODEL_TEMPERATURE,
                    "num_predict": MAX_MODEL_OUTPUT_TOKENS,
                },
            }
            stem = self.evidence / identity
            stem.with_suffix(".request.json").write_text(
                json.dumps(payload, indent=2), encoding="utf-8"
            )
            logger.info("operation=%s stage=%s event=model_started", identity, role)
            request = Request(
                "http://127.0.0.1:11434/api/chat",
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
            )
            with build_opener(ProxyHandler({}), NoRedirect()).open(
                request, timeout=self.timeout
            ) as response:
                raw = response.read(MAX_MODEL_RESPONSE_BYTES + 1)
            stem.with_suffix(".response.json").write_bytes(raw)
            if len(raw) > MAX_MODEL_RESPONSE_BYTES:
                raise ValueError("Model response limit")
            document = decode_frame(raw)
            if document.get("done") is not True or document.get("model") != "qwen3-coder:30b":
                raise ValueError("Incomplete or unexpected model response")
            content = document["message"]["content"].encode("utf-8")
            decode_frame(content)
            return response_contract.model_validate_json(content).model_dump(mode="json")
        except Exception as error:
            logger.warning(
                "operation=%s stage=%s event=model_failed error_type=%s",
                identity,
                role,
                type(error).__name__,
            )
            raise
        finally:
            logger.info(
                "operation=%s stage=%s event=model_finished duration=%.3f",
                identity,
                role,
                time.monotonic() - started,
            )
            MODEL_GATE.release()


def validate_source(source: str, imports: set[str], entry: str) -> None:
    """Filter syntax/imports/entry without importing generated code on the host.

    This is not a sandbox and does not establish semantic correctness. Review
    and native execution remain mandatory, including for module-level statements.
    """
    if (
        not isinstance(source, str)
        or not source
        or len(source.encode("utf-8")) > MAX_PROPOSAL_FIELD_BYTES
    ):
        raise ValueError("Source size limit")
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in {"__import__", "eval", "exec", "compile", "open"}
        ):
            raise ValueError("Forbidden dynamic execution or file builtin")
        if isinstance(node, ast.Import) and any(item.name not in imports for item in node.names):
            raise ValueError("Unapproved import")
        if isinstance(node, ast.ImportFrom) and (node.level or node.module not in imports):
            raise ValueError("Unapproved import")
    if not any(isinstance(node, ast.FunctionDef) and node.name == entry for node in tree.body):
        raise ValueError("Missing source entry")
    compile(tree, "candidate.py", "exec")


def validate_proposal_fields(candidate: dict, names: set[str]) -> None:
    """Reject missing/extra keys and oversized/nonstring proposal fields."""
    if (
        not isinstance(candidate, dict)
        or set(candidate) != names
        or any(
            not isinstance(candidate[name], str)
            or len(candidate[name].encode("utf-8")) > MAX_PROPOSAL_FIELD_BYTES
            for name in names
        )
    ):
        raise ValueError("Invalid proposal schema")


class WidgetDesigner:
    """Generate independent widget proposals from approved tool metadata only."""

    def __init__(self, client: Callable, *, contracts: dict | None = None) -> None:
        """Inject the model boundary; construction performs no network operation."""
        self.client = client
        self.contracts = contracts or {}

    def generate(self, tool: str) -> dict:
        """Request code/tests/notes, preserving the model implementation unchanged."""
        if tool not in self.contracts:
            raise ValueError("Unsupported pilot tool")
        contract = self.contracts[tool]
        content = {
            "system": "You are AgentiX Widget Designer. Generate concise English Python and at most four focused meaningful unittest tests. Return exactly widget_code, tests_code, notes strings as JSON. The module must define create_widget(context), build a Gradio Group and return input/output/button component references in a dictionary. context is an object with callable elem_id(role) for input/output/execute and attribute api_name. Choose components and event wiring yourself. Import the approved tool directly; never duplicate its algorithm. Show read-only integer results, including zero. Invalid input clears prior results. Include module/function/helper docstrings and type annotations. The event API name must use the context api_name attribute. On invalid values return an empty display, never zero; delegate strict validation to the tool, and do not treat arbitrary falsey values as empty text. Place a module docstring before imports, document helpers and annotate parameters/returns. Only gradio, typing and the approved tool module may be imported. No server launch, files, processes, network, dynamic execution or environment access. No reference implementation is supplied. Proposed tests are provisional; never invent test results or authorization.",
            "requirements": {
                "tool": contract,
                "input": "strict string up to 16000 characters; invalid values raise ValueError",
                "output": {
                    "valid_text": "nonnegative integer",
                    "empty_text": 0,
                    "invalid_type_or_overlong_text": None,
                },
                "invalid_ui_policy": "On ValueError clear the old display with a null result. Zero is only a valid successful count. Do not classify other falsey values as valid empty text.",
                "widget_filename": contract["module"].replace("_code", "_widget") + ".py",
                "task": "Create the reusable input/action/result widget for this approved tool.",
            },
        }
        candidate = self.client(ROLE_WIDGET_DESIGNER, content)
        validate_proposal_fields(candidate, {"widget_code", "tests_code", "notes"})
        validate_source(
            candidate["widget_code"], {"gradio", "typing", contract["module"]}, "create_widget"
        )
        compile(candidate["tests_code"], "proposed_tests.py", "exec")
        return candidate


# Compatibility for the earlier private helper import; new code uses the public contract.
_strings = validate_proposal_fields
