"""Candidate preview controls below application deletion, with explicit generation consent."""

from collections.abc import Iterator
from typing import Any, Final

from agentix.retrieval import policy

CANDIDATE_CONTROL_POLL_SECONDS: Final[float] = (
    1.0  # Refresh control availability without inference.
)


def candidate_choices(view: Any) -> list[tuple[str, str]]:
    """Return plain-text checkbox labels and snapshot IDs; Gradio renders labels as text."""
    return [
        (f"{row[0]} - {row[1]} (score {row[2]:.4f}; {row[3]})", item.descriptor.tool_id)
        for item, row in zip(view.results, view.rows, strict=True)
    ]


def build_candidate_panel(
    gr: Any, backend: Any, bind: Any, session_state: Any, workspace: dict, progress: Any
) -> None:
    """Wire search, integer spinner and owner-checked acceptance without starting agents early."""
    dialog = workspace["dialog"]
    operation = (
        {"show_progress": "full", "show_progress_on": progress} if progress is not None else {}
    )
    with gr.Column(elem_id="application-candidates-panel"):
        gr.Markdown("### Application tool candidates")
        status = gr.Markdown(
            backend.retrieval.startup_message, elem_id="application-candidates-status"
        )
        limit = gr.Number(
            value=policy.DEFAULT_SEARCH_LIMIT,
            minimum=policy.MIN_SEARCH_LIMIT,
            maximum=policy.MAX_SEARCH_LIMIT,
            step=1,
            precision=0,
            label="Candidate limit",
            interactive=True,
            elem_id="application-candidate-limit",
        )
        candidates = gr.CheckboxGroup(
            choices=[],
            value=[],
            label="Tools to use",
            interactive=True,
            elem_id="application-candidates-list",
        )
        identity = gr.Textbox(value="", visible=False, interactive=False)
        accept = gr.Button(
            "Accept candidates and generate",
            interactive=False,
            elem_id="application-candidates-accept",
        )
    candidate_outputs = [status, candidates, identity, accept, session_state]

    def clear_candidates(token: str | None, request: Any) -> tuple[Any, ...]:
        """Invalidate explicitly queued candidate snapshots before slow inference starts."""
        owned = backend.invalidate_candidates(token, request)
        return (
            "Search for candidates before accepting.",
            gr.update(choices=[], value=[]),
            "",
            gr.update(interactive=False),
            owned,
        )

    def search_candidates(
        name: str, query: str, count: int, token: str | None, request: Any
    ) -> Iterator[tuple[Any, ...]]:
        """Stream a visible search stage and publish only the latest backend revision."""
        yield (
            "Searching tool candidates...",
            gr.update(choices=[], value=[]),
            "",
            gr.update(interactive=False),
            gr.skip(),
        )
        view, owned = backend.request_candidates(query, count, token, request, name=name)
        if view is not None:
            yield (
                view.message,
                gr.update(
                    choices=candidate_choices(view),
                    value=list(view.expected),
                ),
                view.identity,
                gr.update(interactive=view.ready),
                owned,
            )

    search_inputs = [workspace["name"], workspace["query"], limit, session_state]
    for event in (workspace["generate"].click, limit.input):
        event(
            fn=bind(dialog.guard_result(clear_candidates, len(candidate_outputs))),
            inputs=[session_state],
            outputs=candidate_outputs + dialog.outputs(),
            api_name=False,
            queue=False,
        ).then(
            fn=bind(dialog.wrap_stream(search_candidates, len(candidate_outputs))),
            inputs=search_inputs,
            outputs=candidate_outputs + dialog.outputs(),
            api_name=False,
            trigger_mode="always_last",
            concurrency_id="application-candidate-search",
            concurrency_limit=1,
            **operation,
        )

    def accept_candidates(
        name: str,
        query: str,
        count: int,
        selection_id: str,
        chosen: list[str],
        token: str | None,
        request: Any,
    ) -> Iterator[tuple[Any, ...]]:
        """Disable repeat consent immediately and show the submitted selection's status."""
        untouched = tuple(gr.skip() for _ in workspace["outputs"])
        yield *untouched, "Validating candidate selection…", gr.update(interactive=False)
        try:
            for row in backend.accept_candidates(
                name, query, count, selection_id, token, request, selected_ids=chosen
            ):
                yield (
                    *row,
                    "Accepted candidates submitted to the application workflow.",
                    gr.update(interactive=False),
                )
        except ValueError:
            yield (
                *untouched,
                "Candidate acceptance failed. Search again.",
                gr.update(interactive=False),
            )
            raise

    acceptance_outputs = [*workspace["outputs"], status, accept]
    accept.click(
        fn=bind(dialog.wrap_stream(accept_candidates, len(acceptance_outputs))),
        inputs=[workspace["name"], workspace["query"], limit, identity, candidates, session_state],
        outputs=acceptance_outputs + dialog.outputs(),
        api_name=False,
        **operation,
    )

    def refresh_controls(chosen: list[str], token: str | None, request: Any) -> tuple[Any, ...]:
        """Keep busy/review controls disabled and name the reason inside the button label."""
        idle, ready, owned, reason = backend.candidate_controls(token, request, selected_ids=chosen)
        label = f"Accept {len(chosen)} selected tools and generate"
        if not ready and reason:
            label = f"{label} - {reason}"
        return (
            gr.update(interactive=idle),
            gr.update(interactive=ready, value=label),
            gr.update(interactive=idle),
            owned,
        )

    control_outputs = [limit, accept, workspace["generate"], session_state]
    gr.Timer(value=CANDIDATE_CONTROL_POLL_SECONDS).tick(
        fn=bind(dialog.guard_result(refresh_controls, len(control_outputs))),
        inputs=[candidates, session_state],
        outputs=control_outputs + dialog.outputs(),
        api_name=False,
        show_progress="hidden",
    )

    candidates.input(
        fn=bind(dialog.guard_result(refresh_controls, len(control_outputs))),
        inputs=[candidates, session_state],
        outputs=control_outputs + dialog.outputs(),
        api_name=False,
        queue=False,
        show_progress="hidden",
    )
