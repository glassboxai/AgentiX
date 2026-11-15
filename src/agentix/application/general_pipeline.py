"""Catalog-driven model planning and widgets, with maintained native composition."""

import hashlib
import json
import logging
from typing import TYPE_CHECKING
from uuid import uuid4

from agentix.agents.catalog_agents import CatalogWidgetDesigner
from agentix.lab.application_artifacts import LOCK_PATH, application_digest
from agentix.storage.application_catalog import ApprovedTool
from agentix.widgets.styles import default_widget_css

if TYPE_CHECKING:
    from agentix.application.app_workflow import ApplicationPipeline, Candidate

logger = logging.getLogger(__name__)


def generate(
    pipeline: "ApplicationPipeline",
    query: str,
    tools: dict[str, ApprovedTool],
    feedback: dict | None,
) -> "Candidate":
    """Propose a workflow and exact widget files, without approving or importing code."""
    from agentix.application.app_workflow import Candidate

    identity = uuid4().hex
    folder = pipeline.root / identity
    folder.mkdir(parents=True, exist_ok=False)
    (folder / "requirements.txt").write_text(query, encoding="utf-8")
    logger.info("draft=%s event=generate_started tools=%s", identity, sorted(tools))
    coordinator = pipeline.coordinator_factory(folder / "model-evidence")
    schemas = {name: tool.schema for name, tool in tools.items()}
    assembly = coordinator.plan(query, schemas, feedback)
    logger.info("draft=%s event=plan_validated", identity)
    selected = {widget["tool"] for widget in assembly["widgets"]}
    tools = {name: tool for name, tool in tools.items() if name in selected}
    schemas = {name: schemas[name] for name in tools}
    package = folder / "application"
    package.mkdir()
    from agentix.application.code_package import SHARED as CODE_SHARED
    from agentix.application.code_package import runtime_template as code_template

    connection_code = assembly["connection_code"]
    inputs, widgets = assembly["inputs"], assembly["widgets"]
    (package / "application_logic.py").write_text(connection_code, encoding="utf-8")
    for name in CODE_SHARED:
        (package / name).write_bytes(code_template(name).read_bytes())
    proposals, previous, reuse, pending = {}, {}, {}, {}
    for name, tool in tools.items():
        stored = pipeline.widget_store.load(tool) if pipeline.widget_store is not None else None
        previous[name] = stored
        if stored is not None and (stored.approved or feedback is None):
            proposal = dict(stored.proposal)
            reuse[name] = (
                "approved widget reused"
                if stored.approved
                else "changed widget requires new review"
            )
            proposals[name] = proposal
        else:
            pending[name] = tool
            reuse[name] = "new model-generated widget"
    generated = coordinator.widgets(pending, feedback)
    if set(generated) != set(pending):
        raise ValueError("Widget crew returned unexpected or missing tool identities")
    proposals.update(generated)
    logger.info(
        "draft=%s event=widgets_proposed pending=%s reused=%s",
        identity,
        sorted(pending),
        sorted(reuse),
    )
    for name, tool in tools.items():
        proposal, stored = proposals[name], previous[name]
        try:
            CatalogWidgetDesigner.validate(name, proposal)
        except Exception:
            logger.exception("draft=%s event=widget_validation_failed tool=%s", identity, name)
            raise
        logger.info("draft=%s event=widget_validated tool=%s", identity, name)
        (package / (name + "_code.py")).write_bytes(tool.code)
        (package / (name + "_widget_tests.py")).write_bytes(proposal["tests_code"].encode("utf-8"))
        (package / (name + "_widget.py")).write_bytes(proposal["widget_code"].encode("utf-8"))
        (package / (name + "_widget.css")).write_bytes(
            (stored.css if stored is not None else default_widget_css(name)).encode("utf-8")
        )
    files = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in package.iterdir()}
    manifest = {
        "schema_version": 3,
        "name": "catalog_application",
        "gui_entry": "app:create_application",
        "data_entry": "operation:analyze_text",
        "permissions": [],
        "runtime_lock_sha256": hashlib.sha256(LOCK_PATH.read_bytes()).hexdigest(),
        "files": files,
        "tools": schemas,
        "inputs": inputs,
        "widgets": widgets,
    }
    (package / "application.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    logger.info(
        "draft=%s event=manifest_written schema_version=%s files=%s",
        identity,
        manifest["schema_version"],
        sorted(files),
    )
    from agentix.application.code_cases import propose_cases

    suggested = propose_cases(assembly, tools)
    acceptance, payload, expected = (suggested[key] for key in ("widgets", "payload", "expected"))
    if suggested["pending"]:
        logger.info(
            "draft=%s event=acceptance_pending_fields fields=%s",
            identity,
            suggested["pending"],
        )
    logger.info(
        "draft=%s event=acceptance_proposed widgets=%s payload_keys=%s expected_keys=%s",
        identity,
        acceptance,
        sorted(payload) if isinstance(payload, dict) else type(payload).__name__,
        sorted(expected) if isinstance(expected, dict) else type(expected).__name__,
    )
    dependencies = {
        name: {
            "tool_name": tool.tool_name,
            "function": tool.function,
            "contract_digest": tool.contract_digest,
            "code_sha256": hashlib.sha256(tool.code).hexdigest(),
            "tests_sha256": hashlib.sha256(tool.tests).hexdigest(),
            "unit_tests": "Previously approved; not rerun",
        }
        for name, tool in tools.items()
    }
    review = {
        "original_request": query,
        "manifest": manifest,
        "file_provenance": {
            name: "approved catalog source"
            if name.endswith("_code.py")
            else "model-generated connection code"
            if name == "application_logic.py"
            else "model-generated widget"
            if name.endswith("_widget.py")
            else "maintained compositor or scoped style"
            for name in files
        },
        "source_files": {name: (package / name).read_text(encoding="utf-8") for name in files},
        "proposed_tests_and_notes": {"widgets": proposals, "assembly": assembly},
        "approved_tool_tests": {name: tool.tests.decode() for name, tool in tools.items()},
        "approved_catalog_dependencies": dependencies,
        "tool_acceptance_contracts": {name: tool.reviewed_contract for name, tool in tools.items()},
        "widget_reuse": reuse,
        "independent_acceptance": {"widgets": acceptance, "payload": payload, "expected": expected},
    }
    review["acceptance_proposal"] = {key: suggested[key] for key in ("pending", "provenance")}
    (folder / "proposals.json").write_text(
        json.dumps(review["proposed_tests_and_notes"], indent=2), encoding="utf-8"
    )
    logger.info("draft=%s event=review_built", identity)
    try:
        digest = application_digest(package)
    except Exception:
        logger.exception("draft=%s event=digest_failed", identity)
        raise
    candidate = Candidate(uuid4().hex, folder, package, digest, json.dumps(review, indent=2))
    logger.info("draft=%s event=candidate_ready", identity)
    if pipeline.widget_store is not None:

        def check():
            """Recheck reusable widget bytes before approval/publication."""
            for name, tool in tools.items():
                if pipeline.widget_store.load(tool) != previous[name]:
                    raise ValueError("Reusable widget changed during review")

        def commit(item):
            """Publish each exact widget once after native/browser success."""
            check()
            current = json.loads(item.review_text)["proposed_tests_and_notes"]["widgets"]
            for name, tool in tools.items():
                proposal = dict(current[name])
                proposal["widget_code"] = (
                    (item.package / (name + "_widget.py")).read_bytes().decode("utf-8")
                )
                css = (item.package / (name + "_widget.css")).read_bytes().decode("utf-8")
                if (
                    previous[name] is None
                    or not previous[name].approved
                    or previous[name].proposal != proposal
                    or previous[name].css != css
                ):
                    pipeline.widget_store.publish(tool, proposal, css=css)
                    published = pipeline.widget_store.load(tool)
                    if (
                        published is None
                        or not published.approved
                        or published.proposal != proposal
                        or published.css != css
                    ):
                        raise ValueError("Published widget does not match the reviewed snapshot")
                    previous[name] = published

        candidate.dependency_check, candidate.widget_commit = check, commit
    return candidate
