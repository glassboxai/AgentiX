"""CrewAI coordination for catalog applications; artifact execution stays native.

Crews produce data and widget source for review. They receive no execution tools,
filesystem capabilities or approval authority. All external dependencies are
injected; the factory below is the local application's composition root.
"""

import json
import logging
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any

from pydantic import BaseModel

from agentix.agents.application_agents import MODEL_GATE, WidgetProposal
from agentix.agents.catalog_agents import CatalogWidgetDesigner
from agentix.domain.application_code import ApplicationCode
from agentix.storage.application_catalog import ApprovedTool

logger = logging.getLogger(__name__)
# Private evidence is bounded per task; ordinary events contain no artifact bodies.
MAX_EVIDENCE_BYTES = 262144
# Finite per-agent budgets: one reasoning turn, no retries and a bounded wall clock.
AGENT_MAX_ITERATIONS = 2
AGENT_MAX_RETRY_LIMIT = 0
AGENT_MAX_EXECUTION_SECONDS = 600
# CrewAI guardrails may not retry a rejected structured output.
TASK_GUARDRAIL_MAX_RETRIES = 0
# Default model timeout for direct callers and the accepted configuration range.
DEFAULT_MODEL_TIMEOUT_SECONDS = 120
MIN_MODEL_TIMEOUT_SECONDS = 1
MAX_MODEL_TIMEOUT_SECONDS = 600
# Local application model sampling and output limits.
MODEL_TEMPERATURE = 0.1
MODEL_MAX_TOKENS = 4096
MODEL_MAX_RETRIES = 0


class CrewApplicationCoordinator:
    """One session-owned model and two sequential creation phases with explicit context."""

    def __init__(self, evidence: Path, *, llm: Any, backend: Any) -> None:
        """Inject inert framework/model dependencies and a fresh operation evidence path."""
        self.evidence = evidence
        self.llm = llm
        self.backend = backend
        # The completed integration task supplies context to the widget crew.
        self.plan_task: Any = None

    def _save(self, name: str, value: dict) -> None:
        """Persist bounded private task evidence; never publish it in ordinary logs."""
        encoded = json.dumps(value, ensure_ascii=True, indent=2).encode("utf-8")
        if len(encoded) > MAX_EVIDENCE_BYTES:
            raise ValueError("Application task evidence exceeds its byte limit")
        self.evidence.mkdir(parents=True, exist_ok=True)
        (self.evidence / name).write_bytes(encoded)

    def _agent(self, role: str, goal: str) -> Any:
        """Create a bounded verbose role with no tools, delegation or approval authority."""
        return self.backend.Agent(
            role=role,
            goal=goal,
            backstory="You create reviewable applications strictly from approved catalog contracts.",
            llm=self.llm,
            tools=[],
            allow_delegation=False,
            allow_code_execution=False,
            verbose=True,
            max_iter=AGENT_MAX_ITERATIONS,
            max_retry_limit=AGENT_MAX_RETRY_LIMIT,
            max_execution_time=AGENT_MAX_EXECUTION_SECONDS,
        )

    def _task(
        self, name: str, agent: Any, request: dict, response: type[BaseModel], context: list
    ) -> Any:
        """Declare structured task output and explicit predecessor context in CrewAI."""
        self._save(name + "-request.json", request)
        return self.backend.Task(
            name=name,
            description=request["system"]
            + "\nOriginal task data:\n"
            + json.dumps(request["requirements"]),
            expected_output="Return one JSON object matching the declared output schema. Preserve original requirements and exact catalog contracts. No Markdown fences, approval claims or execution claims.",
            agent=agent,
            context=context,
            output_pydantic=response,
            guardrail_max_retries=TASK_GUARDRAIL_MAX_RETRIES,
        )

    def _run(self, stage: str, agents: list, tasks: list) -> list[dict]:
        """Run one sequential crew, reject missing structured output and release capacity."""
        if not MODEL_GATE.acquire(blocking=False):
            raise ValueError("Another application model operation is active")
        started = time.monotonic()
        logger.info("stage=%s event=crew_started tasks=%s", stage, len(tasks))
        try:
            crew = self.backend.Crew(
                agents=agents,
                tasks=tasks,
                process=self.backend.Process.sequential,
                verbose=True,
                memory=False,
                cache=False,
            )
            crew.kickoff()
            outputs = []
            for task in tasks:
                model = getattr(getattr(task, "output", None), "pydantic", None)
                if not isinstance(model, task.output_pydantic):
                    raise ValueError("Crew task did not return its declared structured output")
                value = model.model_dump(mode="json")
                self._save(
                    task.name + "-response.json", {"model": "qwen3-coder:30b", "output": value}
                )
                outputs.append(value)
            return outputs
        except Exception as error:
            logger.warning("stage=%s event=crew_failed error_type=%s", stage, type(error).__name__)
            raise
        finally:
            logger.info(
                "stage=%s event=crew_finished duration=%.3f", stage, time.monotonic() - started
            )
            MODEL_GATE.release()

    def plan(self, query: str, schemas: dict, feedback: dict | None) -> dict:
        """Generate and review persisted connection code; host never interprets a graph."""
        request = {
            "system": "Generate a standalone application's Python connection code from the approved catalog. Return inputs, widgets, connection_code and notes. inputs maps public input names to JSON schemas containing only `type`, `description`, `enum` and `items`. Do not use `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, `pattern`, `format`, `multipleOf`, `minLength`, `maxLength` or any other JSON Schema keyword: numeric bounds belong to the approved tool contract, not to the public input schema. widgets lists unique {id, tool} presentation instances, at most 16. connection_code is a documented Python module exporting exactly run(payload, call). Call approved tools with call(widget_id, **arguments), which returns the actual tool result. Connect calls using ordinary Python variables, literals and indexing only when the catalog return type is an array. Every widget must be called exactly once. Shared user values come directly from payload. Include every required tool argument; fixed values follow the user's requirements. Do not duplicate tool algorithms. No graph, steps/bindings DSL, tool imports, file/network/process access, agents, server startup, execution claims or acceptance expectations. Only typing imports and documented functions are permitted at module level. Use English docstrings and type annotations. The host supplies widgets and the secure call adapter separately.",
            "requirements": {
                "original_user_request": query,
                "approved_catalog": schemas,
                "supervisor_feedback": feedback,
            },
        }
        planner = self._agent(
            "Application planner", "Write reusable connection code using only the approved catalog."
        )
        integrator = self._agent(
            "Application integrator",
            "Check every input source and correct the proposed connections against the original requirements and port types.",
        )
        first = self._task("plan", planner, request, ApplicationCode, [])
        review = dict(request)
        review["system"] = (
            request["system"]
            + " Review and correct the preceding code against the original requirements and exact tool types. Preserve the complete application; do not replace code with a graph or call list."
        )
        final = self._task("connect", integrator, review, ApplicationCode, [first])
        result = self._run("application_plan", [planner, integrator], [first, final])[-1]
        result = ApplicationCode.model_validate(result).validate_catalog(schemas)
        self.plan_task = final
        return result

    def widgets(self, tools: dict[str, ApprovedTool], feedback: dict | None) -> dict[str, dict]:
        """Generate only missing widgets in one sequential crew with the reviewed plan context."""
        if not tools:
            return {}
        if self.plan_task is None:
            raise ValueError("Plan the application before generating widgets")
        designer = self._agent(
            "Application widget designer",
            "Implement only the requested missing widgets from approved tool contracts.",
        )
        tasks = [
            self._task(
                "widget_" + name,
                designer,
                CatalogWidgetDesigner.request(tool, feedback),
                WidgetProposal,
                [self.plan_task],
            )
            for name, tool in tools.items()
        ]
        outputs = self._run("application_widgets", [designer], tasks)
        proposals = dict(zip(tools, outputs, strict=True))
        for name, proposal in proposals.items():
            CatalogWidgetDesigner.validate(name, proposal)
        return proposals


def make_application_coordinator(
    evidence: Path,
    *,
    timeout: int = DEFAULT_MODEL_TIMEOUT_SECONDS,
    backend: Any = None,
    llm_factory: Callable | None = None,
    llm: Any = None,
) -> CrewApplicationCoordinator:
    """Compose a coordinator, preserving an injected session client when supplied.

    The fallback retains the legacy local application profile for direct callers.
    Session-owned UI flows inject their validated active client instead.
    """
    if (
        type(timeout) is not int
        or not MIN_MODEL_TIMEOUT_SECONDS <= timeout <= MAX_MODEL_TIMEOUT_SECONDS
    ):
        raise ValueError("Application model timeout must be an integer from 1 to 600 seconds")
    if backend is None:
        import crewai as backend
    if llm is None:
        factory = llm_factory if llm_factory is not None else backend.LLM
        llm = factory(
            model="ollama/qwen3-coder:30b",
            base_url="http://127.0.0.1:11434",
            temperature=MODEL_TEMPERATURE,
            timeout=timeout,
            max_tokens=MODEL_MAX_TOKENS,
            max_retries=MODEL_MAX_RETRIES,
        )
    return CrewApplicationCoordinator(evidence, llm=llm, backend=backend)
