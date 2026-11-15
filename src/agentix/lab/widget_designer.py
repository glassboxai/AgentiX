"""Real local Ollama Widget Designer; generates runtime artifacts, never engineering code."""

import json
from pathlib import Path
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

from agentix.lab.widget_artifacts import CONTRACT, package_digest, validate_widget
from agentix.lab.widget_identity import TESTS_FILENAME, TOOL_FILENAME, WIDGET_FILENAME


class NoRedirect(HTTPRedirectHandler):
    """Keep generation requests at the explicitly selected loopback service."""

    def redirect_request(self, *args, **kwargs):
        """Reject redirects without forwarding the local prompt."""
        return None


def generate_widget(folder: Path) -> str:
    """Generate one candidate with qwen3-coder:30b, persist and validate; do not approve."""
    system = """You are the AgentiX Widget Designer. Produce English Python source for the reviewed count_vowels_in_text tool. Its widget module is count_vowels_in_text_widget.py; proposed tests must import create_widget from count_vowels_in_text_widget. Return a JSON object with exactly widget_code, tests_code and notes (all strings). The widget must import only `gradio as gr` and define create_widget(context). It must use one gr.Group, one gr.Textbox, one gr.Number(precision=0), and one gr.Button. Each component must use context.elem_id with roles input, output, execute respectively. Bind exactly one button.click(fn=context.invoke, inputs=the_textbox, outputs=the_number, queue=False, api_name=context.api_name). Return a dict with input, output, button component references. Include English module and function docstrings. Use simple component assignments and the with group; no helper functions, extra imports, annotations, loops, HTML, JS, launch, eval, exec, file or network access. The injected gateway is the only tool execution path. Generate meaningful Python unittest tests_code using a fake context that computes ASCII vowel counts and instantiates the widget in gr.Blocks. These proposed tests are provisional, never independent acceptance. Do not invent execution results or bypass human review."""
    payload = {
        "model": "qwen3-coder:30b",
        "messages": [
            {"role": "system", "content": system},
            {
                "role": "user",
                "content": "Create a reusable vowel-counting form for this approved contract: "
                + json.dumps(CONTRACT),
            },
        ],
        "format": "json",
        "stream": False,
        "options": {"temperature": 0.1, "num_predict": 4096},
    }
    request = Request(
        "http://127.0.0.1:11434/api/chat",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    opener = build_opener(ProxyHandler({}), NoRedirect())
    with opener.open(request, timeout=120) as response:
        raw = response.read(262145)
    if len(raw) > 262144:
        raise ValueError("Model response limit")
    document = json.loads(raw)
    candidate = json.loads(document["message"]["content"])
    if set(candidate) != {"widget_code", "tests_code", "notes"} or not all(
        isinstance(value, str) for value in candidate.values()
    ):
        raise ValueError("Invalid designer response")
    if any(len(value) > 32768 for value in candidate.values()):
        raise ValueError("Candidate size limit")
    if folder.exists():
        raise ValueError("Use a new experimental package folder; do not overwrite review artifacts")
    folder.mkdir(parents=True)
    (folder / "designer-response.json").write_bytes(raw)
    (folder / WIDGET_FILENAME).write_bytes(candidate["widget_code"].encode("utf-8"))
    (folder / TESTS_FILENAME).write_bytes(candidate["tests_code"].encode("utf-8"))
    (folder / TOOL_FILENAME).write_bytes(Path(__file__).with_name("fixture_tools.py").read_bytes())
    (folder / "tool_definition.json").write_text(json.dumps(CONTRACT, indent=2))
    (folder / "DESIGN_NOTES.md").write_text(candidate["notes"], encoding="utf-8")
    validate_widget(candidate["widget_code"].encode())
    return package_digest(folder)
