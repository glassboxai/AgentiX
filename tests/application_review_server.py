"""Disposable real GUI/native server with trusted installed tools and model doubles.

Approval publication below is an explicit trusted test boundary, not a production
approval shortcut. No existing artifacts, live model, API keys or user data are used.
"""

# ruff: noqa: E402
import json
import logging
import os
import sys
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "src"), str(ROOT / "tests")]
os.environ.update(GRADIO_ANALYTICS_ENABLED="False", OTEL_SDK_DISABLED="true")
import gradio as gr
from schema3_package import widget_source
from test_application_catalog import installed
from trusted_sandbox import TrustedFixtureSandbox

from agentix.application.app_workflow import ApplicationPipeline, ApplicationSupervisor
from agentix.controllers.applications import ApplicationsBackend
from agentix.controllers.sessions import SessionRegistry
from agentix.controllers.tool_controller import UiController
from agentix.lab.application_session import execute_application
from agentix.models.model_profiles import ModelProfile
from agentix.storage.installed_apps import InstalledApps
from agentix.tools import ArtifactTools
from agentix.ui.branding import launch_options
from agentix.ui.shell import build_view


def main():
    """Own temporary installed tool grants and one disposable loopback listener."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
    port, root = int(sys.argv[1]), Path(sys.argv[2]).resolve()
    os.environ["AGENTIX_HOME"] = str(root / "runtime-home")
    audit = {
        "tool_test_runs_during_application_work": 0,
        "generation_roles": [],
        "simulated_verification_failures": 0,
        "tool_test_runs": 0,
    }

    def record():
        """Persist only bounded test audit metadata, never prompts/secrets."""
        (root / "audit.json").write_text(json.dumps(audit), encoding="utf-8")

    record()

    controllers_by_catalog: dict[str, UiController] = {}  # Explicit fixture owner routing.

    def create(identity):
        """Provide real catalog/ledger services with explicit fixture grants per owner."""
        folder = root / identity
        folder.mkdir()
        fixture = installed(folder, owner_id=identity)
        mode = sys.argv[3] if len(sys.argv) > 3 else "normal"
        if mode == "missing":
            (folder / "count_words_in_text" / "count_words_in_text_code.py").unlink()
        elif mode == "unapproved":
            fixture.ledger._reuse.pop("count_words_in_text")
        security = fixture.ledger.security
        from agentix.sandbox import WindowsSandbox

        sandbox_type = WindowsSandbox if mode == "native-repair" else TrustedFixtureSandbox

        class CountingSandbox(sandbox_type):
            """Observe actual fixture unittest requests without claiming native isolation."""

            def execute(self, code, tests, tool_name, function_name, kwargs, *, observation=False):
                """Count test invocations independently of orchestration messages."""
                if tests is not None:
                    audit["tool_test_runs"] += 1
                    record()
                return super().execute(
                    code, tests, tool_name, function_name, kwargs, observation=observation
                )

        operations = ArtifactTools(security, sandbox=CountingSandbox())
        operations.verification._reuse.update(fixture.ledger._reuse)
        for name, grant in list(operations.verification._reuse.items()):
            function = "count_words" if "words" in name else "count_vowels"
            contract = {
                "version": 1,
                "cases": [
                    {
                        "id": "normal",
                        "purpose": "Normal text",
                        "function": function,
                        "kwargs": {"text": "Hello World!"},
                        "expect": {"kind": "value", "value": 2 if "words" in name else 3},
                    }
                ],
            }
            operations.verification._reuse[name] = (*grant[:5], contract)
        fixture.ledger = operations.verification

        def workflow(query):
            """Simulate background latency without executing model/tool code."""
            time.sleep(2.5)
            if query == "Please create a calculator that doubles numbers.":
                package = folder / "repair_demo"
                package.mkdir(exist_ok=True)
                (package / "repair_demo_specifications.md").write_text(
                    "Double integer values, including zero and negative values. Reject strings and booleans with ValueError.",
                    encoding="utf-8",
                )
                return operations.compile_and_save_code_tool(
                    "repair_demo",
                    '"""Deliberately wrong trusted fixture proposal."""\ndef double(value):\n    if not isinstance(value, int) or isinstance(value, bool):\n        raise ValueError("Invalid value")\n    return value * 3\n',
                )
            if query == "What is twice five?":
                operations.verify_existing_tool_tool("repair_demo")
                execution = operations.execute_generated_tool_tool(
                    "repair_demo", "double", '{"value":5}'
                )
                observed = operations.verification.execution_result()
                if observed is not None:
                    return (
                        "Host-observed execution: tool.repair_demo.double\nArguments: "
                        + json.dumps(observed["kwargs"])
                        + "\nResult: "
                        + observed["result"]
                    )
                return execution
            return "Trusted background work completed."

        controller = UiController(
            workflow,
            fixture.catalog.render,
            security,
            gr.update,
            validation=operations.acceptance,
            tool_operations=operations,
        )

        def models(url):
            """Simulate local tags latency; no download or inference."""
            time.sleep(1.5)
            return {"models": [{"name": "qwen3-coder:30b"}]}

        for name in ("count_words_in_text", "count_vowels_in_text"):
            (folder / name / (name + "_specifications.md")).write_text(
                "Count words or ASCII vowels in text. Invalid types are rejected.", encoding="utf-8"
            )

        class ExplanationClient:
            """Synthetic read-only model boundary; no inference or credentials."""

            def call(self, messages):
                """Retain fixture-only input for independent browser assertions."""
                if "declarative acceptance" in messages[0]["content"]:
                    return json.dumps(
                        {
                            "version": 1,
                            "cases": [
                                {
                                    "id": "normal",
                                    "purpose": "Double a normal integer",
                                    "function": "double",
                                    "kwargs": {"value": 2},
                                    "expect": {"kind": "value", "value": 4},
                                },
                                {
                                    "id": "zero",
                                    "purpose": "Preserve zero",
                                    "function": "double",
                                    "kwargs": {"value": 0},
                                    "expect": {"kind": "value", "value": 0},
                                },
                                {
                                    "id": "negative",
                                    "purpose": "Double a negative integer",
                                    "function": "double",
                                    "kwargs": {"value": -2},
                                    "expect": {"kind": "value", "value": -4},
                                },
                                {
                                    "id": "invalid",
                                    "purpose": "Reject strings",
                                    "function": "double",
                                    "kwargs": {"value": "2"},
                                    "expect": {"kind": "raises", "type": "ValueError"},
                                },
                                {
                                    "id": "boolean",
                                    "purpose": "Reject booleans",
                                    "function": "double",
                                    "kwargs": {"value": True},
                                    "expect": {"kind": "raises", "type": "ValueError"},
                                },
                            ],
                        }
                    )
                (root / "chat-context.json").write_text(json.dumps(messages), encoding="utf-8")
                return "Trusted fixture explanation: this code counts text without modifying files."

        controller.model_configuration = SimpleNamespace(
            profile=ModelProfile(),
            catalog_reader=models,
            close=lambda: None,
            vault=None,
            llm_factory=lambda **options: ExplanationClient(),
            ensure_generation_identity=lambda: "a" * 64,
            client=None,
        )
        controllers_by_catalog[fixture.catalog.root] = controller
        return controller

    def client_factory(folder):
        """Return deterministic model proposals, clearly separate from native evidence."""

        def client(role, content):
            """Use reviewed maintained fixture widgets as model-boundary test doubles."""
            time.sleep(0.8)
            audit["generation_roles"].append(role)
            record()
            if role == "General Widget Designer":
                module = content["requirements"]["approved_tool_contract"]["module"]
                return {
                    "widget_code": widget_source(module),
                    "tests_code": '"""Provisional fixture tests; not executed as tool tests."""',
                    "notes": "Deterministic model double",
                }
            catalog = content["requirements"]["approved_catalog"]
            return {
                "inputs": {"text": {"type": "string", "description": "Text to inspect"}},
                "widgets": [{"id": name, "tool": name} for name in sorted(catalog)],
                "connection_code": (
                    '"""Connect approved catalog calls."""\n'
                    "def run(payload: dict, call) -> None:\n"
                    '    """Call every approved tool with the shared text input."""\n'
                    + "".join(
                        f'    call("{name}", text=payload["text"])\n' for name in sorted(catalog)
                    )
                ),
                "notes": "Deterministic connection double",
            }

        return client

    class CodeCasesCoordinator:
        """Use canonical authored calculator fixtures for schema-3 browser review."""

        def plan(self, query, schemas, feedback):
            """Return a dependent call with no matching second reviewed value."""
            from test_code_application import proposal

            return proposal()

        def widgets(self, tools, feedback):
            """Supply inert widgets with the current named-controls contract."""
            from test_general_application_pipeline import WIDGET

            return {
                name: {"widget_code": WIDGET, "tests_code": "# provisional", "notes": "fixture"}
                for name in tools
            }

    failures = [True]

    def native(snapshot, payload):
        """Inject one controlled failure, then use the real Windows isolation boundary."""
        if failures[0]:
            failures[0] = False
            time.sleep(2)
            audit["simulated_verification_failures"] += 1
            record()
            raise ValueError("Controlled verification failure")
        return execute_application(snapshot, payload)

    sessions = SessionRegistry(create)
    backend = ApplicationsBackend(
        sessions,
        pipeline_factory=lambda folder: ApplicationPipeline(
            root / "applications",
            client_factory,
            coordinator_factory=(lambda _: CodeCasesCoordinator())
            if len(sys.argv) > 3 and sys.argv[3] == "code-cases"
            else None,
        ),
        supervisor=ApplicationSupervisor(native=native),
        parent_port=port,
        library_factory=lambda: InstalledApps(root / "installed-apps", root / "app-records"),
    )
    if len(sys.argv) > 3 and sys.argv[3] == "code-cases":
        from test_application_crews import approved_tool

        # This review-only mode doubles widget storage and never verifies/publishes.
        backend.pipeline_factory = lambda folder: SimpleNamespace(
            generate=ApplicationPipeline(
                root / "applications", coordinator_factory=lambda _: CodeCasesCoordinator()
            ).generate
        )
        backend.registry_factory = lambda controller: SimpleNamespace(
            resolve=lambda: {"calculator": approved_tool()}, recheck=lambda tools: None
        )

    if len(sys.argv) > 3 and sys.argv[3] == "maintenance":
        from test_installed_apps import published_with_tools

        seed_root = root / "seed"
        seed_root.mkdir()
        seed_library, seeded, fixture = published_with_tools(seed_root)
        # Re-publish a verified fixture into this disposable server's injected library;
        # this is a test grant, never a production migration or model evidence.
        from uuid import uuid4

        from agentix.application.app_workflow import Candidate
        from agentix.lab.application_artifacts import approve_application

        item = Candidate(
            uuid4().hex,
            seed_root,
            seeded.package,
            seeded.digest,
            json.dumps(seeded.review),
            approved=True,
            verified=True,
            snapshot=approve_application(seeded.package, seeded.digest),
            display_name="Maintenance demo",
        )
        backend.library_factory().publish(item)

    from candidate_retrieval_fixtures import RegistryRetrievalDouble

    def record_candidate_limit(limit: int) -> None:
        """Record model-double requests without storing descriptions or source."""
        audit.setdefault("candidate_limits", []).append(limit)
        record()

    backend.retrieval = RegistryRetrievalDouble(
        lambda catalog: backend.registry_factory(controllers_by_catalog[catalog.root]),
        audit=record_candidate_limit,
    )
    original_pipeline_factory = backend.pipeline_factory

    def observed_pipeline(folder: Path) -> Any:
        """Record exactly which tool roles reach the unchanged generation boundary."""
        pipeline = original_pipeline_factory(folder)
        original_generate = pipeline.generate

        def generate(query: str, **kwargs: Any) -> Any:
            """Delegate fixture generation and retain only dependency names in the audit."""
            audit.setdefault("candidate_generation_tools", []).append(
                sorted(kwargs.get("tools", {}))
            )
            record()
            return original_generate(query, **kwargs)

        pipeline.generate = generate
        return pipeline

    backend.pipeline_factory = observed_pipeline
    view = build_view(sessions, applications_backend=backend)
    view.demo.queue().launch(
        server_name="127.0.0.1",
        server_port=port,
        inbrowser=False,
        theme=view.theme,
        **launch_options(),
    )


if __name__ == "__main__":
    main()
