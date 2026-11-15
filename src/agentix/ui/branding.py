"""Load maintained local branding; never serve an arbitrary filesystem directory."""

import base64
from pathlib import Path

ASSETS = Path(__file__).with_name("assets")
MERMAID_BUNDLE = "mermaid.min.js"
MERMAID_GLOBAL_TAIL = (
    'globalThis["mermaid"] = globalThis.__esbuild_esm_mermaid_nm["mermaid"].default;'
)


def mermaid_script() -> str:
    """Wrap the pinned bundle so Gradio's eval scope still publishes the global.

    Gradio executes the launch ``js`` string inside ``eval``, where the bundle's
    top-level ``var`` stays local; its own final assignment therefore reads an
    undefined ``globalThis`` property. The wrapper keeps that binding in scope and
    publishes ``globalThis.mermaid`` from it. The vendored bytes stay unchanged.
    """
    bundle = (ASSETS / MERMAID_BUNDLE).read_text(encoding="utf-8").rstrip()
    if not bundle.endswith(MERMAID_GLOBAL_TAIL):
        raise ValueError("Unexpected Mermaid bundle tail; review the pinned asset")
    body = bundle[: -len(MERMAID_GLOBAL_TAIL)]
    return (
        "(() => {\n"
        + body
        + '\nglobalThis["mermaid"] = __esbuild_esm_mermaid_nm["mermaid"].default;\n})();'
    )


def stylesheet() -> str:
    """Return the application CSS for Gradio's launch-time styling API."""
    return (ASSETS / "style.css").read_text(encoding="utf-8")


def header() -> str:
    """Render the approved identity using a fixed local PNG as an inline image."""
    logo = base64.b64encode((ASSETS / "Agentix.png").read_bytes()).decode("ascii")
    return (
        '<header class="agentix-brand"><div class="agentix-identity">'
        f'<img src="data:image/png;base64,{logo}" alt="AgentiX logo" width="64" height="64">'
        '<h1>AgentiX</h1></div><div class="agentix-tagline">'
        '<p>Agentic Software Engineering.</p><p class="brand-focus">Developer-in-the-Loop.</p>'
        "<p>AI-generated code. Software engineer-supervised. Built for secure, "
        "maintainable, production-quality software.</p>"
        '<p><a class="project-link" href="https://glassboxai.dev/">'
        "The Glass Box AI Project</a></p></div></header>"
    )


def launch_options() -> dict[str, object]:
    """Share appearance across normal and disposable launchers; expose no file roots."""
    return {
        "css": stylesheet(),
        "favicon_path": str(ASSETS / "Agentix.png"),
        "footer_links": [],
        "js": "() => {"
        + "\n".join(
            (ASSETS / name).read_text(encoding="utf-8")
            for name in (
                "chathelper.js",
                "review_editor.js",
                "sidebar_resize.js",
                "widget_selection.js",
                "widget_style.js",
                "mermaid_render.js",
            )
        )
        + "\n"
        + mermaid_script()
        + "}",
    }
