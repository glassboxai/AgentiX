"""Readable, owner-controller-invoked review of whitelisted application artifacts.

Generated source is data on the host. Explicit edits invalidate approval; this
service never imports candidate modules or executes their proposed tests.
"""

import hashlib
import json
import logging
from uuid import uuid4

from agentix.agents.application_agents import validate_source
from agentix.application.app_workflow import Candidate
from agentix.lab.application_artifacts import application_digest
from agentix.security.reuse_policy import allowed_modules, computation_only

logger = logging.getLogger(__name__)


class ApplicationReview:
    """Present real files separately from provisional tests and independent cases."""

    def _contracts(self, item: Candidate) -> dict:
        """Use the selected catalog closure, retaining explicit legacy compatibility."""
        return self._snapshot(item).get("manifest", {}).get("tools") or self._legacy_contracts(item)

    def _legacy_contracts(self, item: Candidate) -> dict:
        """Derive tool modules from the reviewed package files, never a fixed registry."""
        package = item.package
        return {
            name.removesuffix("_code.py"): {"module": name.removesuffix(".py")}
            for name in sorted(path.name for path in package.glob("*_code.py"))
        }

    def _files(self, item: Candidate) -> set[str]:
        """Return only source members from the owner-bound manifest."""
        return set(self._snapshot(item).get("manifest", {}).get("files", {}))

    def _editable(self, item: Candidate) -> set[str]:
        """Connection logic, reviewed cases, widget source, styles and tests are editable."""
        return {"application_logic.py", "application_acceptance.json"} | {
            name
            for name in self._files(item)
            if name.endswith(("_widget.py", "_widget.css", "_widget_tests.py"))
        }

    def _snapshot(self, item: Candidate) -> dict:
        """Load only the server-owned bounded review, never browser-supplied JSON."""
        return json.loads(item.review_text)

    def entries(self, item: Candidate) -> list[tuple[str, str]]:
        """Return a finite display-name/key list; keys are not arbitrary paths."""
        tool_sources = {contract["module"] + ".py" for contract in self._contracts(item).values()}
        entries = [
            (
                name
                + (
                    " — tool revision"
                    if name in tool_sources
                    else " — editable"
                    if name in self._editable(item)
                    else " — read-only dependency"
                ),
                name,
            )
            for name in sorted(self._files(item))
        ]
        entries.append(
            (
                "application_acceptance.json — independent host-held cases (editable)",
                "application_acceptance.json",
            )
        )
        entries.append(("application.json — package contract (read-only)", "application.json"))
        entries.extend(
            (name + "_tests.py — approved tool tests", name + "_tests.py")
            for name in self._snapshot(item).get("approved_tool_tests", {})
        )
        return entries

    def _review_key(self, item: Candidate, name: str) -> str:
        """Normalize only a whitelisted general widget-test member to its proposal view."""
        if name in self._files(item) and name.endswith("_widget_tests.py"):
            return "proposed_tests/" + name.removesuffix("_widget_tests.py") + "_tests.py"
        return name

    def read(self, item: Candidate, name: str) -> tuple[str, bool, str]:
        """Read a whitelisted member or virtual proposed test; reject path injection."""
        if name not in {key for _, key in self.entries(item)}:
            raise ValueError("Select a file from this application's review")
        if name == "application_acceptance.json":
            from agentix.application.code_cases import acceptance_status

            snapshot = self._snapshot(item)
            acceptance = snapshot["independent_acceptance"]
            return (
                json.dumps({key: acceptance[key] for key in ("payload", "expected")}, indent=2),
                True,
                acceptance_status(snapshot)[1],
            )
        name = self._review_key(item, name)
        for tool_name, source in self._snapshot(item).get("approved_tool_tests", {}).items():
            if name == tool_name + "_tests.py":
                return (
                    source,
                    False,
                    "Approved tool tests. Edit only as a pending tool revision in the grouped view.",
                )
        if name.startswith("proposed_tests/"):
            role = name.removeprefix("proposed_tests/").removesuffix("_tests.py")
            return (
                self._snapshot(item)["proposed_tests_and_notes"]["widgets"][role]["tests_code"],
                True,
                "Provisional model tests. Saving does not execute or approve them; independent functional checks remain mandatory.",
            )
        if name in self._files(item):
            text = (item.package / name).read_text(encoding="utf-8")
        else:
            text = json.dumps(self._snapshot(item).get("manifest", {}), indent=2)
        editable = name in self._editable(item)
        return (
            text,
            editable,
            "Save changes explicitly; a fresh review is then required."
            if editable
            else "Read-only dependency. Change an installed tool through Tools and obtain a new approval there.",
        )

    def save(self, item: Candidate, name: str, text: str, identity: str) -> bool:
        """Validate an explicit edit, persist it and report whether the grant was revoked.

        The caller holds the owner controller lock and rejects concurrent work.
        Executable members revoke the previous application grant before any write.
        A scoped ``<tool>_widget.css`` edit returns ``False``: its closed grammar is
        the gate, so the approval stays valid and no re-review is required.
        No crash-transaction guarantee is made for multiple filesystem writes.
        """
        _, editable, _ = self.read(item, name)
        name = self._review_key(item, name)
        if not editable or identity != item.identity:
            raise ValueError("File is read-only or the displayed review is stale")
        if not isinstance(text, str) or len(text.encode("utf-8")) > 65536:
            raise ValueError("Edited file exceeds 64 KiB")
        if name == "application_acceptance.json":
            from agentix.application.code_package import validate_acceptance

            snapshot = self._snapshot(item)
            try:
                value = validate_acceptance(json.loads(text), snapshot["manifest"])
            except ValueError as error:
                from agentix.application.code_cases import acceptance_status

                logger.warning(
                    "event=application_acceptance_invalid detail=%s",
                    acceptance_status(snapshot)[1],
                    exc_info=True,
                )
                raise error
            logger.info("event=application_acceptance_saved")
            item.close()
            item.approved = item.verified = False
            item.snapshot = None
            item.identity = uuid4().hex
            snapshot["independent_acceptance"].update(value)
            item.review_text = json.dumps(snapshot, indent=2)
            (item.folder / "review-current.json").write_text(item.review_text, encoding="utf-8")
            return
        if name == "application_logic.py":
            from agentix.domain.application_code import validate_connection_source

            validate_connection_source(text)
        if name.endswith("_widget.css"):
            from agentix.application.style_member import write_style_member
            from agentix.widgets.styles import validate_widget_css

            validate_widget_css(
                text,
                next(
                    role
                    for role, contract in self._contracts(item).items()
                    if contract["module"].replace("_code", "_widget") + ".css" == name
                ),
            )
            # A scoped style is gated by its grammar, not by the code grant: persist
            # it, rebind the declared member hash and keep the approval usable.
            write_style_member(item.package, name, text)
            snapshot = self._snapshot(item)
            snapshot.setdefault("source_files", {})[name] = text
            snapshot.setdefault("file_provenance", {})[name] = (
                "owner style edit; scoped grammar validated, approval retained"
            )
            item.review_text = json.dumps(snapshot, indent=2)
            (item.folder / "review-current.json").write_bytes(item.review_text.encode("utf-8"))
            return False
        try:
            if not name.endswith(".css"):
                compile(text, name, "exec")
        except (SyntaxError, ValueError, RecursionError) as error:
            raise ValueError("Edited Python has invalid syntax") from error
        snapshot = self._snapshot(item)
        if name.startswith("proposed_tests/"):
            role = name.removeprefix("proposed_tests/").removesuffix("_tests.py")
            snapshot["proposed_tests_and_notes"]["widgets"][role]["tests_code"] = text
        elif not name.endswith(".css") and name != "application_logic.py":
            imports = {
                "gradio",
                "typing",
                "application_context",
                "operation",
                "count_words_in_text_widget",
                "count_vowels_in_text_widget",
                "count_words_in_text_code",
                "count_vowels_in_text_code",
            } | {contract["module"] for contract in self._contracts(item).values()}
            validate_source(
                text, imports, "create_application" if name == "app.py" else "create_widget"
            )
        # Revoke before writes: an IO failure must never preserve a stale grant.
        item.close()
        item.approved = item.verified = False
        item.snapshot = None
        item.catalog_id = ""
        item.identity = uuid4().hex
        if not name.startswith("proposed_tests/"):
            (item.package / name).write_bytes(text.encode("utf-8"))
        for role, proposal in (
            snapshot.get("proposed_tests_and_notes", {}).get("widgets", {}).items()
        ):
            (item.package / (role + "_widget_tests.py")).write_bytes(
                proposal["tests_code"].encode("utf-8")
            )
        manifest = json.loads((item.package / "application.json").read_bytes())
        from agentix.domain.tool_schema import extract_tool_schema

        manifest["tools"] = {
            tool: extract_tool_schema(
                tool, (item.package / (tool + "_code.py")).read_text(encoding="utf-8")
            )
            for tool in manifest["tools"]
        }
        manifest["files"] = {
            key: hashlib.sha256((item.package / key).read_bytes()).hexdigest()
            for key in self._files(item)
        }
        (item.package / "application.json").write_text(
            json.dumps(manifest, indent=2), encoding="utf-8"
        )
        item.digest = application_digest(item.package)
        snapshot["manifest"] = manifest
        snapshot["source_files"] = {
            key: (item.package / key).read_text(encoding="utf-8")
            for key in sorted(self._files(item))
        }
        snapshot.setdefault("file_provenance", {})[name] = (
            "human-edited proposal; new approval required"
        )
        item.review_text = json.dumps(snapshot, indent=2)
        (item.folder / "review-current.json").write_bytes(item.review_text.encode("utf-8"))
        (item.folder / "proposals.json").write_text(
            json.dumps(snapshot.get("proposed_tests_and_notes", {}), indent=2), encoding="utf-8"
        )
        return True

    def panes(self, item: Candidate, name: str) -> dict:
        """Resolve one whitelisted tool-related selection to consistent review buffers."""
        snapshot = self._snapshot(item)
        for role, contract in self._contracts(item).items():
            tool = contract["module"].removesuffix("_code")
            names = {
                tool + "_code.py",
                tool + "_widget.py",
                tool + "_tests.py",
                tool + "_widget_tests.py",
                f"proposed_tests/{role}_tests.py",
            }
            if name in names:
                proposal = (
                    snapshot.get("proposed_tests_and_notes", {}).get("widgets", {}).get(role, {})
                )
                return {
                    "role": role,
                    "code": (item.package / (tool + "_code.py")).read_text(encoding="utf-8"),
                    "widget": (item.package / (tool + "_widget.py")).read_text(encoding="utf-8"),
                    "tool_tests": snapshot.get("tool_test_drafts", {}).get(
                        tool, snapshot.get("approved_tool_tests", {}).get(tool, "")
                    ),
                    "widget_tests": proposal.get("tests_code", ""),
                }
        raise ValueError("Select a tool implementation, widget or tests for the grouped view")

    def save_group(self, item: Candidate, values: dict, identity: str) -> bool:
        """Validate every pane before writing a pending app/tool revision, never import it."""
        if (
            identity != item.identity
            or set(values) != {"role", "code", "widget", "tool_tests", "widget_tests"}
            or values["role"] not in self._contracts(item)
        ):
            raise ValueError("Stale or invalid tool review selection")
        role = values["role"]
        current = self.panes(item, self._contracts(item)[role]["module"] + ".py")
        # Gradio Code strips outer whitespace on submission. Preserve the exact
        # approved bytes when a pane's displayed content was not actually edited.
        values = dict(values)
        for key in ("code", "widget", "tool_tests", "widget_tests"):
            if values[key] == current[key].strip():
                values[key] = current[key]
        if current == values:
            return False
        contract = self._contracts(item)[role]
        tool = contract["module"].removesuffix("_code")
        snapshot = self._snapshot(item)
        function = (
            snapshot.get("approved_catalog_dependencies", {}).get(role, {}).get("function")
            or contract.get("function")
            or tool
        )
        for key in ("code", "widget", "tool_tests", "widget_tests"):
            text = values[key]
            if not isinstance(text, str) or len(text.encode("utf-8")) > 65536:
                raise ValueError("Edited pane exceeds 64 KiB")
            try:
                compile(text, key + ".py", "exec")
            except (SyntaxError, ValueError, RecursionError) as error:
                raise ValueError("One edited pane has invalid Python syntax") from error
        if not computation_only(values["code"]):
            raise ValueError("This application supports computation-only tool revisions")
        validate_source(values["code"], set(allowed_modules()), function)
        validate_source(values["widget"], {"gradio", "typing", contract["module"]}, "create_widget")
        original_code = (item.package / (tool + "_code.py")).read_text(encoding="utf-8")
        original_tests = snapshot.get("approved_tool_tests", {}).get(tool, "")
        base = snapshot.setdefault("tool_revision_bases", {}).setdefault(
            role, {"code": original_code, "tests": original_tests}
        )
        pending = snapshot.setdefault("pending_tool_revisions", {})
        if values["code"] != base["code"] or values["tool_tests"] != base["tests"]:
            pending[role] = {
                "tool_name": tool,
                "code": values["code"],
                "tests": values["tool_tests"],
            }
        else:
            pending.pop(role, None)
        item.close()
        item.approved = item.verified = False
        item.snapshot = None
        item.catalog_id = ""
        item.identity = uuid4().hex
        revision = item.folder / "tool-revisions" / tool
        revision.mkdir(parents=True, exist_ok=True)
        for suffix, key in (
            ("code", "code"),
            ("widget", "widget"),
            ("tests", "tool_tests"),
            ("widget_tests", "widget_tests"),
        ):
            (revision / (tool + "_" + suffix + ".py")).write_bytes(values[key].encode("utf-8"))
        # CodeMirror normalizes line endings. Unchanged displayed text must not
        # rewrite the exact approved source bytes (notably Windows CRLF files).
        if values["code"] != original_code:
            (item.package / (tool + "_code.py")).write_bytes(values["code"].encode("utf-8"))
        (item.package / (tool + "_widget.py")).write_bytes(values["widget"].encode("utf-8"))
        snapshot.setdefault("tool_test_drafts", {})[tool] = values["tool_tests"]
        widgets = snapshot.setdefault("proposed_tests_and_notes", {}).setdefault("widgets", {})
        proposal = widgets.setdefault(
            role, {"widget_code": "", "tests_code": "", "notes": "Human-reviewed revision"}
        )
        proposal["widget_code"], proposal["tests_code"] = values["widget"], values["widget_tests"]
        for role, proposal in (
            snapshot.get("proposed_tests_and_notes", {}).get("widgets", {}).items()
        ):
            (item.package / (role + "_widget_tests.py")).write_bytes(
                proposal["tests_code"].encode("utf-8")
            )
        manifest = json.loads((item.package / "application.json").read_bytes())
        from agentix.domain.tool_schema import extract_tool_schema

        manifest["tools"] = {
            tool: extract_tool_schema(
                tool, (item.package / (tool + "_code.py")).read_text(encoding="utf-8")
            )
            for tool in manifest["tools"]
        }
        manifest["files"] = {
            name: hashlib.sha256((item.package / name).read_bytes()).hexdigest()
            for name in self._files(item)
        }
        (item.package / "application.json").write_text(
            json.dumps(manifest, indent=2), encoding="utf-8"
        )
        item.digest = application_digest(item.package)
        snapshot["manifest"] = manifest
        snapshot["source_files"] = {
            name: (item.package / name).read_text(encoding="utf-8")
            for name in sorted(self._files(item))
        }
        snapshot.setdefault("file_provenance", {})[tool + "_widget.py"] = (
            "human-edited pending revision"
        )
        item.review_text = json.dumps(snapshot, indent=2)
        (item.folder / "review-current.json").write_bytes(item.review_text.encode("utf-8"))
        (item.folder / "proposals.json").write_text(
            json.dumps(snapshot["proposed_tests_and_notes"], indent=2), encoding="utf-8"
        )

        return True
