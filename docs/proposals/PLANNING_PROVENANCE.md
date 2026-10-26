# Planning provenance and document verification

Date: 2026-10-23. Scope: documentation only.

The proposal uses the project's maintained architecture, approved isolation and
acceptance specifications, UI-013 report, supervised domain-only review report
and maintained sandbox/contracts source to size the next work. Historical test
counts were not rerun or represented as current execution evidence. Existing
project-generated artifacts were not inspected, executed or modified. All work
inside the proposal is pending, including baseline establishment and acceptance.

The capacity estimate assumes one full-time senior engineer, twenty eight-hour
working days, sixteen planned days and four contingency days; reviewer time is
additional. The indicative dates are subject to kickoff agreement. The estimate
commits only to a bounded supervised pilot. Direct generated Gradio execution
requires the early native-boundary decision and may require replanning.

Official Gradio, Pydantic and Playwright references were checked for event
sequencing, elem_id, strict validation and browser locators/assertions. Installed
versions must still be pinned and checked during the proposed first week.

Local Ollama qwen3:14b produced a prose-only narrative draft. The draft was reviewed
against source evidence and not accepted as implementation authority. Its phrase
"no Docker installer" conflated two separate exclusions; the final proposal states
Docker and installer work separately. No engineering code or tests were requested
from Ollama. The final proposal was authored and reviewed by the engineering agent.

DOC-PROP-001: initial document rendering could not locate LibreOffice on PATH,
and sandbox temporary cleanup reported permission errors. On Windows the packaged
renderer supports the installed native executable. Explicitly supplying its path
and running the renderer with the required permissions resolved rendering.
DOC-PROP-002: the first render inherited a blue title rule, split a short milestone
table and split an acceptance row across pages. Removing paragraph borders,
reordering the milestone summary, preventing split rows and adding deliberate
section breaks corrected those layout defects. Short clickable source labels
removed isolated reference lines. The final seven page images were inspected.

The document build uses the bundled artifact Python runtime and python-docx.
The packaged render_docx.py uses installed LibreOffice and bundled Poppler.
Final verification checks the four pending milestone rows, required agent/schema/
Playwright terms, effort arithmetic, seven PDF pages, no paragraph borders and
non-splitting table rows. Rendered PDF/PNG files are internal QA artifacts, not
additional requested deliverables. No application regression-suite execution is
needed or claimed for this document-only change.
