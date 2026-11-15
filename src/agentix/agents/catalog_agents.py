"""Catalog-derived application model roles; proposals never authorize execution.

These roles receive approved tool metadata and produce data/widget source for
explicit human review. They contain no reference widget implementation. Framework,
provider, filesystem, native execution and UI lifecycle concerns are injected or
owned by application services, not these roles.
"""

from collections.abc import Callable
from pathlib import Path
from typing import Protocol

from agentix.agents.application_agents import (
    ROLE_GENERAL_ASSEMBLER,
    ROLE_GENERAL_WIDGET_DESIGNER,
    validate_proposal_fields,
    validate_source,
)
from agentix.storage.application_catalog import ApprovedTool


class CatalogAssembler:
    """Propose bounded connection code from actual installed catalog capabilities."""

    def __init__(self, client: Callable[[str, dict], dict]) -> None:
        """Inject the selected model boundary; initialization performs no IO."""
        self.client = client

    @staticmethod
    def request(query: str, schemas: dict, feedback: dict | None = None) -> dict:
        """Build original requirements and catalog context without reference implementation."""
        content = {
            "system": "Propose one bounded Python connection module plus its public inputs and widget inventory. Return inputs, widgets, connection_code and notes matching the output schema. connection_code defines exactly run(payload, call) and calls only supplied catalog tools through call(tool_name, **arguments); read user values from payload and reuse earlier results as local variables. Declare one widget per tool invocation identity with its exact catalog tool. Include every required parameter; fix settings explicitly requested by the user. Use only the supplied catalog contracts. Write concise English notes explaining the connections. No execution or approval claims.",
            "requirements": {
                "original_user_request": query,
                "approved_catalog": schemas,
                "supervisor_feedback": feedback,
            },
        }
        return content

    @staticmethod
    def validate(proposal: dict, schemas: dict) -> dict:
        """Validate a structured code proposal before packaging or any generated execution."""
        from agentix.domain.application_code import ApplicationCode

        return ApplicationCode.model_validate(proposal).validate_catalog(schemas)

    def generate(self, query: str, schemas: dict, feedback: dict | None = None) -> dict:
        """Retain an explicitly injected callable boundary for compatibility fixtures."""
        return self.validate(
            self.client(ROLE_GENERAL_ASSEMBLER, self.request(query, schemas, feedback)), schemas
        )


class CatalogWidgetDesigner:
    """Write the Gradio widget implementation and provisional tests once per tool."""

    def __init__(self, client: Callable[[str, dict], dict]) -> None:
        """Inject the model client without reading tool files or importing source."""
        self.client = client

    @staticmethod
    def request(tool: ApprovedTool, feedback: dict | None = None) -> dict:
        """Build one widget task from approved metadata and independent cases only."""
        name = tool.tool_name
        request = {
            "system": "You are AgentiX Widget Designer. Return exactly widget_code, tests_code and notes strings as JSON. Generate concise English Gradio Python and at most three concise meaningful unittest methods; use subTest tables rather than duplicated scaffolding. Define create_widget(context); use 'with gr.Group():' only as the layout container for the controls. The return value MUST be the dictionary described in return_contract with the exact keys inputs, output, button and render; NEVER return the gr.Group itself or any bare component, because returning a gr.Group instead of the dictionary fails application composition. Import and call the supplied approved tool; never duplicate its algorithm. Return a dictionary: inputs maps EVERY exact parameter name to its component, output is the result component, button is its action button, render is a callable formatting a raw tool result for that component. Register a callback on the button using context.api_name. Use context.elem_id(parameter_name) for inputs, context.elem_id('output') and context.elem_id('execute') for the other controls. Do NOT put an ID on gr.Group. Choose suitable typed input controls from the contract; do not round invalid fractional integer inputs into valid values; show scalar outputs read-only, sequences in a Dataframe (render as rows). Do not use gr.JSON. Preserve zero values and seeded reproducibility. Clear stale output on errors; do not silently change input values or tool logic. Use module/function/helper docstrings and type annotations. Only gradio, typing and the exact approved tool module may be imported in the widget module: write 'import gradio as gr' (the package is named gradio; there is no 'gr' package) and 'from <tool>_code import <function>'. The widget module must never import application_context or element_ids — those imports belong ONLY to the tests module, never to widget_code; context arrives as the create_widget argument. No server, filesystem, networking, processes, environment access, dynamic execution or approval. Tests are provisional. No reference implementation is supplied.",
            "requirements": {
                "approved_tool_contract": tool.schema,
                "reviewed_acceptance": tool.reviewed_contract,
                "widget_filename": name + "_widget.py",
                "integer_input_policy": "Preserve raw entered numbers: no precision=0 rounding and no int() truncation. The approved tool must reject fractional or boolean integer settings itself.",
                "error_policy": "Callbacks must return None on expected TypeError or ValueError to clear old output; do not raise gr.Error leaving a successful old result. Null is not zero.",
                "sequence_output_policy": "Use one numeric table column with one row per item. Empty sequence means zero rows; None clears the display. Do not transpose the sequence into one row.",
                "context_contract": {
                    "kind": "Injected maintained object; never gr.Context",
                    "api_name": {"type": "string", "callable": False},
                    "elem_id": {
                        "callable": True,
                        "arguments": "one declared parameter name, output or execute",
                        "returns": "stable string",
                    },
                    "return_contract": {
                        "inputs": "exact parameter-to-component dictionary",
                        "output": "component",
                        "button": "component",
                        "render": "callable from raw result to displayed value",
                    },
                },
                "testing_contract": "Construct widgets inside real gr.Blocks. Tests must be unittest.TestCase classes whose checks live in test_* methods; module-level pytest-style functions collect ZERO tests under the maintained unittest runner and fail verification. Use application_context.Context and element_ids.ElementIds as supplied maintained context classes with their exact constructors: ids = ElementIds() (no arguments) and context = Context(instance, ids, parameters), where instance is one lowercase widget identifier string and parameters is the list of the tool's declared parameter names. Context has no api_name constructor argument; context.api_name is a read-only attribute derived from ids. Every test module must import create_widget from the widget module and set up the context exactly like this template: 'from application_context import Context', 'from element_ids import ElementIds', 'from <tool>_widget import create_widget', 'ids = ElementIds()', 'context = Context(instance, ids, parameters)'. The Context argument order is (instance, ids, parameters); passing parameters before ids is a common mistake — do not swap them. create_widget(context) must be called INSIDE a 'with gr.Blocks() as demo:' block in every test; registering callbacks outside a Blocks context raises AttributeError ('Cannot call click outside of a gradio.Blocks context'), so the template continues: 'with gr.Blocks() as demo:', then indented 'widget = create_widget(context)'. Invoke the registered callback directly through demo.fns: 'result = demo.fns[0].fn(\"some input\")' or 'next(event for event in demo.fns.values() if event.api_name == context.api_name).fn(\"some input\")'. Button.fn, component.fn, gr.Context and demo.test_api do not exist; never call demo.test_api(...). Write checks with self.assert* methods (self.assertEqual, self.assertIsNone, self.assertTrue), never bare names like self.callable. Test actual callbacks against independent expected values and invalid clearing, not only a formatting function. Element IDs are host-allocated by ElementIds as 'application_<instance>_<role>'; never hardcode expected elem_id strings in assertions — assert structure instead (non-empty, unique per control, or equal to context.elem_id(role) itself). The same rule applies to context.api_name: it is host-derived from the allocated scope and its exact value is unpredictable to you; never assert a literal api_name string — instead verify the registered event exists via demo.fns (e.g. any(event.api_name == context.api_name for event in demo.fns.values())). Keep subTest tables concise. Do not import sys/os or edit import paths. No reference implementation is supplied.",
                "supervisor_feedback": feedback,
            },
        }
        return request

    def generate(self, tool: ApprovedTool, feedback: dict | None = None) -> dict:
        """Retain the callable fixture boundary without executing generated source."""
        proposal = self.client(ROLE_GENERAL_WIDGET_DESIGNER, self.request(tool, feedback))
        self.validate(tool.tool_name, proposal)
        return proposal

    @staticmethod
    def validate(name: str, proposal: dict) -> None:
        """Bound and compile proposal data without importing or executing model code."""
        validate_proposal_fields(proposal, {"widget_code", "tests_code", "notes"})
        validate_source(
            proposal["widget_code"], {"gradio", "typing", name + "_code"}, "create_widget"
        )
        compile(proposal["tests_code"], name + "_widget_tests.py", "exec")


class ApplicationCoordinator(Protocol):
    """Explicit two-phase creation contract; neither phase approves or executes artifacts."""

    def plan(self, query: str, schemas: dict, feedback: dict | None) -> dict:
        """Return the validated catalog plan for the original requirements."""
        ...

    def widgets(self, tools: dict[str, ApprovedTool], feedback: dict | None) -> dict[str, dict]:
        """Return proposals only for the requested missing widget identities."""
        ...


class CallableCoordinator:
    """Compatibility for explicitly injected legacy/test callables, never a fallback."""

    def __init__(self, evidence: Path, *, client_factory: Callable) -> None:
        """Construct the caller-supplied model double for one operation."""
        self.client = client_factory(evidence)

    def plan(self, query: str, schemas: dict, feedback: dict | None) -> dict:
        """Use the same host contract with the explicitly supplied boundary."""
        return CatalogAssembler(self.client).generate(query, schemas, feedback)

    def widgets(self, tools: dict[str, ApprovedTool], feedback: dict | None) -> dict[str, dict]:
        """Preserve existing fixture calls while production uses a sequential crew."""
        designer = CatalogWidgetDesigner(self.client)
        return {name: designer.generate(tool, feedback) for name, tool in tools.items()}
