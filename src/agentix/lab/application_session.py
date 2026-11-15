"""Composite application snapshots executed inside the existing native ASGI boundary.

Only browser HTTP uses IPC. Tool imports/calls remain inside the application worker;
legacy host RPC requests are explicitly rejected. Headless use imports no Gradio.
"""

import json
import re
import time

from pydantic import TypeAdapter

from agentix.lab.application_artifacts import ApprovedApplication, validate_result
from agentix.lab.contracts import Text
from agentix.lab.widget_session import WidgetSession

STYLE_MARKER = b"/* agentix-widget-styles */"


def served_style(css: bytes, tool: str, node_id: str, *, restaged: bool = False) -> bytes:
    """Render one scoped stylesheet for the served page, not for the saved file.

    The preview's own sheet forces radius and background with ``!important`` at
    specificity (0,5,0), so a plain ``:where()`` rule loses there. The served copy
    repeats ``[id]`` to reach (0,10,0) and marks every declaration important.
    Gradio prefixes its startup copy with three container classes. A restaged
    copy adds four more attribute selectors so a saved style beats that snapshot.
    The reviewed file on disk keeps its plain form.
    """
    scoped = css.replace(
        ("application_" + tool + "_").encode(), ("application_" + node_id + "_").encode()
    ).decode("utf-8")
    repetitions = 13 if restaged else 9
    scoped = re.sub(
        r':where\((\[id\^="[^"]+"\])\)',
        lambda match: match.group(1) + "[id]" * repetitions,
        scoped,
    )

    def strengthen(match: re.Match) -> str:
        """Mark each declaration important and repeat font rules on form controls.

        A form control does not inherit font from its container, so the text a user
        reads keeps the framework font unless the served sheet targets it directly.
        """
        declarations = [part.strip() for part in match.group(1).split(";") if part.strip()]
        body = "; ".join(
            part if part.endswith("!important") else part + " !important" for part in declarations
        )
        return "{ " + body + "; }"

    rendered = re.sub(r"\{([^{}]*)\}", strengthen, scoped)
    font_rules = []
    for selector, body in re.findall(r"([^{}]+)\{([^{}]*)\}", rendered):
        fonts = [
            part.strip()
            for part in body.split(";")
            if part.strip().startswith(("font-family", "font-size"))
        ]
        if not fonts:
            continue
        base = selector.strip()
        # Form controls do not inherit font, and Gradio styles the caption span
        # directly, so both are targeted. A caption block already ends in ``label``,
        # so its descendant target is the span itself; appending ``label span`` there
        # would build an impossible ``label label span`` selector. Layout grips are
        # excluded so their glyph size never follows the widget font.
        subject = base.rsplit(" ", 1)[-1]
        if subject in ("label", ".label-wrap"):
            targets = ("span",)
        else:
            targets = (
                "input:not(.application-visibility-toggle)",
                "textarea",
                "select",
                "button:not(.application-layout-handle)",
                "label span",
                ".label-wrap span",
            )
        controls = ", ".join(f"{base} {tag}" for tag in targets)
        font_rules.append(controls + " { " + "; ".join(fonts) + "; }")
    return (rendered + "\n" + "\n".join(font_rules)).encode("utf-8")


class WidgetTestsFailed(RuntimeError):
    """Carry bounded private diagnostic data without exposing child text in user errors."""

    def __init__(self, report: dict) -> None:
        """Copy bounded JSON diagnostics; the report cannot establish successful execution."""
        super().__init__("New widget tests failed or contained no executed tests")
        encoded = json.dumps(report, ensure_ascii=True)
        self.report = (
            json.loads(encoded) if len(encoded.encode()) <= 16384 else {"diagnostics": "size limit"}
        )


class ApplicationSession(WidgetSession):
    """Reuse maintained transport/job lifecycle with a complete reviewed application payload."""

    def __init__(
        self,
        approved: ApprovedApplication,
        *,
        payload: dict | None = None,
        lifetime: int | None = 300,
        widget_tests: list[str] | None = None,
        display_name: str = "",
    ) -> None:
        """Validate capability and optional strict JSON input before allocating native resources."""
        if not isinstance(approved, ApprovedApplication):
            raise ValueError("Reviewed application required")
        if lifetime is not None and (type(lifetime) is not int or not 1 <= lifetime <= 300):
            raise ValueError("Application lifetime exceeds its manifest limit")
        if type(display_name) is not str or len(display_name) > 120:
            raise ValueError("Invalid application display name")
        self.display_name = display_name
        self.manifest = json.loads(dict(approved.files)["application.json"])
        if payload is not None:
            if lifetime is None:
                raise ValueError("Headless execution must have a finite deadline")
            if self.manifest.get("schema_version") == 3:
                from agentix.application.general_package import validate_payload

                payload = validate_payload(payload, self.manifest)
            elif type(payload) is not dict or set(payload) != {"text"}:
                raise ValueError("Invalid application input")
            if self.manifest.get("schema_version") != 3:
                payload = {"text": TypeAdapter(Text).validate_python(payload["text"])}
        if widget_tests is not None and (
            payload is not None
            or self.manifest.get("schema_version") != 3
            or not widget_tests
            or len(widget_tests) != len(set(widget_tests))
            or not set(widget_tests) <= set(self.manifest["tools"])
        ):
            raise ValueError("Invalid reviewed widget test selection")
        self.widget_tests = widget_tests
        super().__init__(lifetime=lifetime, tests_only=widget_tests is not None)
        self.application = approved
        self.payload = payload
        self.headless = payload is not None
        self.clock = time.monotonic
        self.callback_leases: dict[str, float] = {}

    def _stage_payload(self) -> None:
        """Write immutable reviewed snapshots, never reread sources from their original paths."""
        for name, content in self.application.files:
            (self.root / name).write_bytes(content)
        styles = [
            content for name, content in self.application.files if name.endswith("_widget.css")
        ]
        if self.manifest.get("schema_version") == 3:
            members = dict(self.application.files)
            styles = [
                served_style(members[node["tool"] + "_widget.css"], node["tool"], node["id"])
                for node in (
                    self.manifest["widgets"]
                    if self.manifest["schema_version"] == 3
                    else self.manifest["workflow"]["nodes"]
                )
            ]
        css_path = self.root / "application.css"
        css_path.write_bytes(
            css_path.read_bytes() + b"\n" + STYLE_MARKER + b"\n" + b"\n".join(styles)
        )
        if self.display_name:
            (self.root / "application_display.json").write_text(
                json.dumps({"name": self.display_name}), encoding="utf-8"
            )
        if self.widget_tests is not None:
            (self.root / "application_widget_test_plan.json").write_text(
                json.dumps(self.widget_tests), encoding="utf-8"
            )
        if self.headless:
            (self.root / "application_input.json").write_text(
                json.dumps(self.payload), encoding="utf-8"
            )

    def restage_styles(self, member: str, css: str) -> None:
        """Rewrite the served stylesheet so any page load sees the saved style.

        ``_stage_payload`` writes ``application.css`` once at startup. A style saved
        afterwards must reach that same file, otherwise a reload and the separate
        "View as web" tab keep serving the old declarations. The member bytes are
        accumulated in a session-owned copy of the immutable approved snapshot.
        Scoped styles are rebuilt with the same tool-to-instance rewrite used at
        startup, plus four attribute selectors to outrank Gradio's prefixed copy
        of the original startup stylesheet. The owner writes each individual CSS
        member before calling this method; this method only writes the served sheet.
        """
        members = dict(getattr(self, "_staged_style_members", dict(self.application.files)))
        if member not in members:
            raise ValueError("Unknown widget style member")
        members[member] = css.encode("utf-8")
        styles = [
            served_style(
                members[node["tool"] + "_widget.css"], node["tool"], node["id"], restaged=True
            )
            for node in self.manifest["widgets"]
        ]
        # The staged file is the base UI stylesheet plus an appended widget block.
        # Truncating at the marker keeps the base sheet; rebuilding from the members
        # alone would drop it and leave the served page unstyled.
        current = (self.root / "application.css").read_bytes()
        base = current.split(STYLE_MARKER, 1)[0].rstrip(b"\n")
        (self.root / "application.css").write_bytes(
            base + b"\n" + STYLE_MARKER + b"\n" + b"\n".join(styles)
        )
        # The approved snapshot is immutable. Keep the latest per-widget bytes for
        # subsequent saves so rebuilding the web sheet cannot restore an old style.
        self._staged_style_members = members

    def _worker_arguments(self) -> list[str]:
        """Select only maintained application/headless worker modes."""
        return [
            "--application",
            *(
                ["--headless"]
                if self.headless
                else ["--application-tests"]
                if self.widget_tests is not None
                else []
            ),
        ]

    def _check_runtime(self) -> None:
        """Kill the owned job when a reviewed callback exceeds 45 seconds."""
        with self.state_lock:
            expired = any(self.clock() - started >= 45 for started in self.callback_leases.values())
        if expired:
            self.diagnostics["failure"] = "callback_timeout"
            self.cancel.set()

    def _control_message(self, message: dict) -> bool:
        """Validate structured result separately; it is not a proof of semantic correctness."""
        kind = message.get("type")
        if kind == "supervisor_stop" and set(message) == {"type"}:
            self.diagnostics["stop_reason"] = "user_stop"
            self.cancel.set()
            return True
        if kind in ("callback_start", "callback_end"):
            identity = message.get("id")
            if (
                set(message) != {"type", "id"}
                or not isinstance(identity, str)
                or len(identity) != 32
                or any(c not in "0123456789abcdef" for c in identity)
            ):
                raise ValueError("Invalid callback lease")
            with self.state_lock:
                if kind == "callback_start":
                    if identity in self.callback_leases or len(self.callback_leases) >= 16:
                        raise ValueError("Callback lease limit")
                    self.callback_leases[identity] = self.clock()
                elif identity not in self.callback_leases:
                    raise ValueError("Unknown callback lease")
                else:
                    self.callback_leases.pop(identity)
            return True
        if message.get("type") != "application_result":
            return super()._control_message(message)
        if (
            not self.headless
            or set(message) != {"type", "result"}
            or "application_result" in self.diagnostics
        ):
            raise ValueError("Unexpected application result")
        self.diagnostics["application_result"] = validate_result(message["result"], self.manifest)
        self.ready.set()
        return True

    def _invoke_tool(self, message: dict) -> None:
        """Deny legacy host tool capabilities; application tools must execute in the child."""
        self.cancel.set()
        raise ValueError("Host tool dispatch is unavailable for composite applications")


def execute_application(approved: ApprovedApplication, payload: dict) -> dict[str, object]:
    """Run the reviewed composite data operation natively without UI/server startup.

    Validate host-observed successful process exit as well as result shape. Native
    execution establishes isolation, not functional correctness of arbitrary code.
    """
    with ApplicationSession(approved, payload=payload) as session:
        session.native_thread.join(10)
        session.reader_thread.join(3)
        observation = session.diagnostics.get("native")
        if (
            not observation
            or observation[0] != 0
            or observation[2]
            or "application_result" not in session.diagnostics
        ):
            raise RuntimeError("Isolated application execution failed")
        return validate_result(session.diagnostics["application_result"], session.manifest)


def run_application_widget_tests(approved: ApprovedApplication, names: list[str]) -> dict:
    """Run only new reviewed widget test modules natively; success remains provisional."""
    with ApplicationSession(approved, widget_tests=names) as session:
        session.native_thread.join(10)
        observation = session.diagnostics.get("native")
        report = session.diagnostics.get("provisional_tests", {})
        if (
            not observation
            or observation[0] != 0
            or observation[2]
            or report.get("successful") is not True
            or type(report.get("run")) is not int
            or report["run"] <= 0
        ):
            raise WidgetTestsFailed(
                {
                    "native_exit_code": observation[0] if observation else None,
                    "timed_out": bool(observation[2]) if observation else None,
                    "untrusted_report": report,
                }
            )
        return report
