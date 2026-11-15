"""V5-042: CrewAI coordinates creation; native execution and review stay separate."""

import json
from pathlib import Path
from types import SimpleNamespace

import pytest
from test_general_application_pipeline import WIDGET
from test_v5_tool_contracts import CODE

from agentix.domain.tool_schema import extract_tool_schema
from agentix.storage.application_catalog import ApprovedTool


def approved_tool() -> ApprovedTool:
    """Return independently authored tool metadata without importing its code."""
    schema = extract_tool_schema("calculator", CODE)
    case = {
        "function": "calculator",
        "kwargs": {"a": 2, "b": 3},
        "expect": {"kind": "value", "value": 5},
    }
    return ApprovedTool(
        "calculator",
        "calculator",
        "calculator",
        CODE.encode(),
        b"# reviewed fixture",
        "a" * 64,
        {"cases": [case]},
        schema,
    )


def plan() -> dict:
    """Declare ordinary readable IDs and external ports without catalog prefixes."""
    return {
        "workflow": {
            "nodes": [
                {
                    "id": "calculator",
                    "tool": "calculator",
                    "inputs": {
                        "a": {"node": None, "input": "a"},
                        "b": {"node": None, "input": "b"},
                    },
                }
            ]
        },
        "notes": "Independent calculator plan",
    }


def steps_plan(proposal: dict | None = None) -> dict:
    """Translate authored fixture labels into the new ordered-call task envelope."""
    value = proposal or plan()
    steps = []
    for node in value["workflow"]["nodes"]:
        arguments = {}
        for parameter, binding in node["inputs"].items():
            if binding["node"] is None:
                arguments[parameter] = {"input": binding.get("input", parameter)}
            else:
                arguments[parameter] = {"result": binding["node"]}
        steps.append({"id": node["id"], "tool": node["tool"], "arguments": arguments})
    return {"steps": steps, "notes": value["notes"]}


def code_plan(proposal: dict | None = None) -> dict:
    """Return an authored code envelope; inventory has no input/output connections."""
    value = proposal or plan()
    return {
        "inputs": {"a": {"type": "number"}, "b": {"type": "number"}},
        "widgets": [
            {"id": node["id"], "tool": node["tool"]} for node in value["workflow"]["nodes"]
        ],
        "connection_code": '"""Authored fixture."""\ndef run(payload, call):\n    """Use the secure native call adapter."""\n    call("calculator", a=payload["a"], b=payload["b"])\n',
        "notes": "Independent code fixture",
    }


def backend(proposal: dict | None = None) -> SimpleNamespace:
    """Record actual coordination contracts with inert framework/model doubles."""
    crews, agents, models = [], [], []

    def agent(**options: object) -> SimpleNamespace:
        """Retain explicit role and verbose/resource options."""
        value = SimpleNamespace(**options)
        agents.append(value)
        return value

    def task(**options: object) -> SimpleNamespace:
        """Retain task dependencies and structured output schema."""
        return SimpleNamespace(output=None, **options)

    def llm(**options: object) -> object:
        """Record pinned local model construction without inference."""
        models.append(options)
        return object()

    class Crew:
        """Populate structured fixture outputs without executing model-produced Python."""

        def __init__(self, **options: object) -> None:
            """Record the sequential crew definition."""
            self.__dict__.update(options)
            crews.append(self)

        def kickoff(self) -> None:
            """Complete the authored tasks in their declared order."""
            for item in self.tasks:
                value = (
                    code_plan(proposal)
                    if item.output_pydantic.__name__ == "ApplicationCode"
                    else {"widget_code": WIDGET, "tests_code": "# proposed", "notes": "fixture"}
                )
                item.output = SimpleNamespace(
                    pydantic=item.output_pydantic.model_validate(value), raw=json.dumps(value)
                )

    return SimpleNamespace(
        Agent=agent,
        Task=task,
        Crew=Crew,
        LLM=llm,
        Process=SimpleNamespace(sequential="sequential"),
        crews=crews,
        agents=agents,
        models=models,
    )


def test_crews_use_sequential_context_and_only_pending_widgets(tmp_path: Path) -> None:
    """Planning precedes integration; reused widgets require no additional crew."""
    from agentix.adapters.application_crewai import make_application_coordinator

    framework = backend()
    coordinator = make_application_coordinator(tmp_path, backend=framework)
    tool = approved_tool()
    assert (
        coordinator.plan("Build an arithmetic application", {"calculator": tool.schema}, None)
        == code_plan()
    )
    assert coordinator.widgets({}, None) == {}
    assert len(framework.crews) == 1
    assert coordinator.widgets({"calculator": tool}, None)["calculator"]["widget_code"] == WIDGET
    assert len(framework.crews) == 2
    first, second = framework.crews
    assert first.process == second.process == "sequential"
    assert len(first.tasks) == 2
    assert first.tasks[1].context == [first.tasks[0]]
    assert second.tasks[0].context == [first.tasks[1]]
    assert all(crew.verbose is True for crew in framework.crews)
    assert all(
        agent.verbose is True and agent.allow_delegation is False for agent in framework.agents
    )
    assert framework.models[0]["model"] == "ollama/qwen3-coder:30b"
    assert framework.models[0]["base_url"] == "http://127.0.0.1:11434"
    assert list(tmp_path.glob("*.json"))


def test_plan_prompt_closes_the_public_input_schema_keys(tmp_path: Path) -> None:
    """V7-059: the host prompt forbids numeric bounds instead of relying on the user."""
    from agentix.adapters.application_crewai import make_application_coordinator

    framework = backend()
    coordinator = make_application_coordinator(tmp_path, backend=framework)
    coordinator.plan(
        "Build an arithmetic application", {"calculator": approved_tool().schema}, None
    )
    request = json.loads((tmp_path / "plan-request.json").read_text(encoding="utf-8"))
    system = request["system"]
    assert "only `type`, `description`, `enum` and `items`" in system
    for keyword in ("minimum", "maximum", "exclusiveMinimum", "exclusiveMaximum", "pattern"):
        assert keyword in system
    assert "numeric bounds belong to the approved tool contract" in system
    review = json.loads((tmp_path / "connect-request.json").read_text(encoding="utf-8"))
    assert review["system"].startswith(system)
    assert "only `type`, `description`, `enum` and `items`" in review["system"]


def test_coordinator_uses_an_injected_session_llm_without_rebuilding_it(tmp_path: Path) -> None:
    """The application coordinator must preserve the active session model client."""
    from agentix.adapters.application_crewai import make_application_coordinator

    framework = backend()
    client = object()
    coordinator = make_application_coordinator(tmp_path, backend=framework, llm=client)
    assert coordinator.llm is client
    assert framework.models == []


def test_invalid_final_plan_stops_before_widgets_or_approval(tmp_path: Path) -> None:
    """Crew output remains data; unavailable tools fail host validation."""
    from agentix.adapters.application_crewai import make_application_coordinator

    invalid = plan()
    invalid["workflow"]["nodes"][0]["tool"] = "unavailable"
    framework = backend(invalid)
    coordinator = make_application_coordinator(tmp_path, backend=framework)
    with pytest.raises(ValueError):
        coordinator.plan(
            "Build an arithmetic application", {"calculator": approved_tool().schema}, None
        )
    assert len(framework.crews) == 1


def test_pipeline_injects_coordinator_without_legacy_http_client(tmp_path: Path) -> None:
    """A real package can be assembled with CrewAI coordination and no host code import."""
    from agentix.adapters.application_crewai import make_application_coordinator
    from agentix.application.app_workflow import ApplicationPipeline

    framework = backend()
    item = ApplicationPipeline(
        tmp_path,
        coordinator_factory=lambda evidence: make_application_coordinator(
            evidence, backend=framework
        ),
    ).generate("Build a calculator", tools={"calculator": approved_tool()})
    assert not item.approved and not item.verified
    assert json.loads(item.review_text)["manifest"]["widgets"] == code_plan()["widgets"]
    assert "workflow" not in json.loads(item.review_text)["manifest"]
    assert len(framework.crews) == 2


@pytest.mark.frameworks
def test_real_crewai_task_context_and_pydantic_outputs_without_inference(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Construct actual CrewAI agents/tasks/crews; only kickoff uses authored outputs."""
    from crewai import Crew
    from crewai.tasks.task_output import TaskOutput

    from agentix.adapters.application_crewai import make_application_coordinator

    calls = []

    def kickoff(self: Crew) -> None:
        """Substitute inference only while keeping real framework schemas and context."""
        for task in self.tasks:
            if task.context:
                assert Crew._get_context(task, [])
            value = (
                code_plan()
                if task.output_pydantic.__name__ == "ApplicationCode"
                else {"widget_code": WIDGET, "tests_code": "# proposed", "notes": "fixture"}
            )
            task.output = TaskOutput(
                description=task.description,
                agent=task.agent.role,
                raw=json.dumps(value),
                pydantic=task.output_pydantic.model_validate(value),
            )
        calls.append(self)

    monkeypatch.setattr(Crew, "kickoff", kickoff)
    coordinator = make_application_coordinator(tmp_path)
    assert (
        coordinator.plan("Build a calculator", {"calculator": approved_tool().schema}, None)
        == code_plan()
    )
    assert (
        coordinator.widgets({"calculator": approved_tool()}, None)["calculator"]["widget_code"]
        == WIDGET
    )
    assert len(calls) == 2


def test_failed_crew_releases_capacity_without_retry(tmp_path: Path) -> None:
    """One failed kickoff must not retry or prevent the next explicit operation."""
    from agentix.adapters.application_crewai import make_application_coordinator

    framework = backend()
    original = framework.Crew.kickoff
    attempts = []

    def fail(self: object) -> None:
        """Expose one controlled framework failure."""
        attempts.append(self)
        raise RuntimeError("Controlled framework failure")

    framework.Crew.kickoff = fail
    coordinator = make_application_coordinator(tmp_path, backend=framework)
    with pytest.raises(RuntimeError, match="Controlled"):
        coordinator.plan("Build calculator", {"calculator": approved_tool().schema}, None)
    assert len(attempts) == 1
    framework.Crew.kickoff = original
    assert (
        coordinator.plan("Build calculator", {"calculator": approved_tool().schema}, None)
        == code_plan()
    )


def test_missing_structured_output_cannot_reach_approval(tmp_path: Path) -> None:
    """A successful framework return alone cannot establish a valid application plan."""
    from agentix.adapters.application_crewai import make_application_coordinator

    framework = backend()
    framework.Crew.kickoff = lambda self: None
    coordinator = make_application_coordinator(tmp_path, backend=framework)
    with pytest.raises(ValueError, match="structured output"):
        coordinator.plan("Build calculator", {"calculator": approved_tool().schema}, None)
    assert coordinator.plan_task is None


def test_application_verbose_and_events_belong_to_the_owning_session(tmp_path: Path) -> None:
    """Application crews must not send verbose output or events to another session."""
    import io
    import logging
    from threading import RLock

    from agentix.controllers.applications import ApplicationsBackend
    from agentix.controllers.sessions import SessionRegistry
    from agentix.controllers.state import ConsoleThoughtsCapture
    from agentix.diagnostics import activity_output, log_event

    def controller(identity: str) -> SimpleNamespace:
        """Create only the controller contracts needed by generation."""
        return SimpleNamespace(
            _lock=RLock(),
            state=SimpleNamespace(
                is_running=False, application_busy=False, application_review_pending=False
            ),
            model_configuration=SimpleNamespace(
                profile=SimpleNamespace(provider="Ollama"),
                generation_digest="fixture-digest",
                ensure_generation_identity=lambda: None,
            ),
            security=SimpleNamespace(get_pending_request=lambda: None),
            captured_stdout=ConsoleThoughtsCapture(io.StringIO()),
        )

    sessions = SessionRegistry(controller)
    alice = sessions.resolve(None, "alice")
    bob = sessions.resolve(None, "bob")

    class Pipeline:
        """Expose verbose and technical output without model/storage execution."""

        def __init__(self, root: Path) -> None:
            """Retain the injected root without touching it."""
            self.root = root

        def generate(self, query: str, *, tools: dict) -> SimpleNamespace:
            """Emit both streams under the caller's ownership scope."""
            print("OWNED_CREW_VERBOSE")
            log_event(logging.getLogger(__name__), "owned_crew_event")
            return SimpleNamespace(
                dependency_check=None, identity="candidate", review_text="{}", close=lambda: None
            )

    service = ApplicationsBackend(
        sessions,
        pipeline_factory=Pipeline,
        registry_factory=lambda _: SimpleNamespace(resolve=lambda: {}),
    )
    with activity_output():
        rows = list(
            service.generate("Compose tools", alice.token, SimpleNamespace(session_hash="alice"))
        )
    assert "Human review required" in rows[-1][0]
    output = alice.controller.captured_stdout.get_logs()
    assert "OWNED_CREW_VERBOSE" in output and "owned_crew_event" in output
    assert "OWNED_CREW_VERBOSE" not in bob.controller.captured_stdout.get_logs()
    service.close_all()
