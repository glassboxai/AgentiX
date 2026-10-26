"""Disposable real UI with trusted fixtures; never load a model or project artifacts.

This executable is test infrastructure only. Its OS boundary double must never
be used for untrusted input. The parent owns process and temporary-directory cleanup.
"""

# Imports below require process policy and checkout paths before framework loading.
# ruff: noqa: E402

import json
import os
import sys
from pathlib import Path
from types import SimpleNamespace

os.environ.update(GRADIO_ANALYTICS_ENABLED="False", OTEL_SDK_DISABLED="true")
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tests"))

import gradio as gr
from trusted_sandbox import TrustedFixtureSandbox

from agentix.security import SecurityManager
from agentix.tools import ArtifactTools
from agentix.ui.branding import launch_options
from agentix.ui.controller import UiController
from agentix.ui.sessions import SessionRegistry
from agentix.ui.view import build_view


def main() -> None:
    """Serve only loopback on the supplied temporary port and artifact root."""
    folder, port = Path(sys.argv[1]), int(sys.argv[2])

    fixture_values = {}

    def fixture_write(reference, key):
        """Model validation and a deterministic denial without exposing the key."""
        from agentix.credentials import register_secret

        register_secret(key)
        if key == "synthetic-denied-vault-key":
            raise PermissionError("private-vault-diagnostic")
        fixture_values[reference] = key

    fixture_vault = SimpleNamespace(
        write=fixture_write,
        read=lambda ref: fixture_values[ref],
        delete=lambda ref: fixture_values.pop(ref, None),
    )

    def create(identity: str) -> UiController:
        """Give each browser its own real approvals, ledger and artifact services."""
        security = SecurityManager.for_owner(identity, timeout=60)
        security.TOOLS_ROOT_DIR = str(folder / identity)
        service = ArtifactTools(security, sandbox=TrustedFixtureSandbox())

        reuse_counts = {"review_requests": 0, "test_runs": 0}

        def workflow(query: str) -> str:
            """Exercise actual storage, provisional tests, review and host comparison."""
            if query in {
                "reuse create",
                "reuse next",
                "durable create",
                "durable next",
                "durable mutate",
            }:
                if query.startswith("durable"):
                    from agentix.approval_store import ApprovalStore
                    from agentix.data_protection import WindowsDataProtection

                    security.TOOLS_ROOT_DIR = str(folder / "durable-artifacts")
                    service.verification.store = ApprovalStore(
                        folder / "protected-approvals",
                        Path(security.TOOLS_ROOT_DIR),
                        protector=WindowsDataProtection(),
                        policy="browser-fixture-policy",
                    )
                if query == "durable mutate":
                    path = Path(security.TOOLS_ROOT_DIR) / "adder" / "adder_code.py"
                    path.write_bytes(path.read_bytes() + b"\n# changed trusted fixture")
                    return "Trusted fixture source changed"
                security.operation_id = query
                if query.endswith("create"):
                    service.compile_and_save_code_tool("adder", "def add(a,b=2): return a+b")
                    tests = "import unittest\nfrom adder_code import add\nclass Checks(unittest.TestCase):\n def test_sum(self): self.assertEqual(add(10),12)\n"
                    reuse_counts["test_runs"] += 1
                    provisional = service.run_and_save_tests_tool("adder", tests)
                    if not provisional.startswith("TESTS_PROVISIONAL_PASSED:"):
                        return provisional
                    reuse_counts["review_requests"] += 1
                    acceptance = service.submit_acceptance_cases_tool(
                        "adder",
                        json.dumps(
                            {
                                "version": 1,
                                "cases": [
                                    {
                                        "id": "sum_case",
                                        "purpose": "Add two",
                                        "function": "add",
                                        "kwargs": {"a": 10},
                                        "expect": {"kind": "value", "value": 12},
                                    }
                                ],
                            }
                        ),
                    )
                    if not acceptance.startswith("ACCEPTANCE_VERIFIED:"):
                        return acceptance
                else:
                    prepared = service.verify_existing_tool_tool("adder")
                    if not prepared.startswith("REUSE_READY:"):
                        if not prepared.startswith("TESTS_PROVISIONAL_PASSED:"):
                            return prepared
                        reuse_counts["test_runs"] += 1
                        reuse_counts["review_requests"] += 1
                        reviewed = service.submit_acceptance_cases_tool(
                            "adder",
                            json.dumps(
                                {
                                    "version": 1,
                                    "cases": [
                                        {
                                            "id": "sum_case",
                                            "purpose": "Add two",
                                            "function": "add",
                                            "kwargs": {"a": 10},
                                            "expect": {"kind": "value", "value": 12},
                                        }
                                    ],
                                }
                            ),
                        )
                        if not reviewed.startswith("ACCEPTANCE_VERIFIED:"):
                            return reviewed
                result = service.execute_generated_tool_tool(
                    "adder", "add", json.dumps({"a": 10 if query.endswith("create") else 40})
                )
                receipt = service.verification.execution_result()
                if receipt is None:
                    return result
                return (
                    "Host-observed execution: adder.add\nArguments: "
                    + json.dumps(receipt["kwargs"])
                    + "\nResult: "
                    + repr({"value": int(receipt["result"]), **reuse_counts})
                )
            if query.startswith("presentation"):
                # Trusted display fixture only, never evidence of model execution.
                cases = [
                    {
                        "id": f"case_{i}",
                        "passed": True,
                        "expected": {"kind": "value", "value": i},
                        "observed": {"kind": "observation", "status": "returned", "value": i},
                    }
                    for i in range(16)
                ]
                controller.validation = SimpleNamespace(
                    status=lambda: {
                        "stage": "verified",
                        "tool": "electricity_bill_calculator",
                        "cases": cases,
                    }
                )
                return (
                    "Host-observed execution: electricity_bill_calculator.calculate\n"
                    'Arguments: {"consumption_kwh": 350}\n'
                    "Result: {'total_cost': 67.5, 'breakdown': ["
                    "{'tier': 1, 'kwh': 100, 'rate': 0.12, 'cost': 12.0}, "
                    "{'tier': 2, 'kwh': 100, 'rate': 0.18, 'cost': 18.0}, "
                    "{'tier': 3, 'kwh': 150, 'rate': 0.25, 'cost': 37.5}]}"
                )
            if query == "file":
                return service.save_specifications_tool("fixture", "Original specification")
            if query != "acceptance":
                return "Fixture response: " + query
            # The browser explicitly enables file auto-approval first. Acceptance
            # must still pause for human review despite that switch.
            service.compile_and_save_code_tool("adder", "def add(): return 3")
            tests = (
                "import unittest\nclass Checks(unittest.TestCase):\n"
                " def test_sum(self): self.assertEqual(1 + 2, 3)\n"
            )
            provisional = service.run_and_save_tests_tool("adder", tests)
            if not provisional.startswith("TESTS_PROVISIONAL_PASSED:"):
                return provisional
            contract = {
                "version": 1,
                "cases": [
                    {
                        "id": "sum_case",
                        "purpose": "Check sum",
                        "function": "add",
                        "kwargs": {},
                        "expect": {"kind": "value", "value": 99},
                    }
                ],
            }
            return service.submit_acceptance_cases_tool("adder", json.dumps(contract))

        controller = UiController(
            workflow,
            lambda: "- Tool Name: `electricity_bill_calculator`\n"
            "    * Function: `calculate(consumption_kwh)`\n"
            "      Description: Trusted display fixture.\n"
            "- Tool Name: `adder`\n    * Function: `add(a, b)`\n",
            security,
            gr.update,
            validation=service.acceptance,
        )
        from agentix.model_profiles import SessionModelConfiguration
        from agentix.profile_store import SavedProfiles

        controller.state.session_id = identity
        fixture_runtime = SimpleNamespace(
            orchestrator=SimpleNamespace(run_system=workflow),
            operations=SimpleNamespace(acceptance=service.acceptance),
            catalog=SimpleNamespace(render=controller.get_installed_tools_catalog),
        )
        catalog_reads = [0]

        def local_catalog(url):
            """Make the manual refresh reveal an additional installed model."""
            catalog_reads[0] += 1
            names = ["qwen3-coder:30b"] + (["qwen3:14b"] if catalog_reads[0] > 1 else [])
            return {"models": [{"name": name} for name in names]}

        def configured_runtime(client):
            """Expose the configured fake client identity through the real query UI."""
            return SimpleNamespace(
                orchestrator=SimpleNamespace(
                    run_system=lambda query: "Configured model: " + client.model
                    if query == "model identity"
                    else workflow(query)
                ),
                operations=fixture_runtime.operations,
                catalog=fixture_runtime.catalog,
            )

        controller.model_configuration = SessionModelConfiguration(
            controller,
            configured_runtime,
            llm_factory=lambda **kwargs: SimpleNamespace(model=kwargs["model"]),
            vault_factory=lambda: fixture_vault,
            store_factory=lambda vault: SavedProfiles(
                folder / "model-profiles", vault, resolver=lambda host: ["93.184.216.34"]
            ),
            resolver=lambda host: ["93.184.216.34"],
            catalog_reader=local_catalog,
        )
        return controller

    view = build_view(SessionRegistry(create), gradio_module=gr)
    view.demo.queue().launch(
        server_name="127.0.0.1",
        server_port=port,
        theme=view.theme,
        inbrowser=False,
        show_error=True,
        **launch_options(),
    )


if __name__ == "__main__":
    main()
