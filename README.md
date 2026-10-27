<p align="center">
  <img src="assets/agentix-logo.png"
       alt="AgentiX Logo"
       width="180">
</p>

<h1 align="center">AgentiX</h1>

<p align="center">
  Agentic Software Development — Human in the Loop
</p>


![Status: Under Active Development](https://img.shields.io/badge/Status-Under%20Active%20Development-orange)

> 🚧 **Under Active Development**
>
> This aplication is currently under active development. Its architecture, features, and documentation are evolving and may change as research and implementation progress. **Not yet recommended for production use**.
  

## About AgentiX

**AgentiX** is an open-source, AI-powered software development system designed **for software developers, not end users**.

Built around a **Human-in-the-Loop** philosophy, AgentiX combines agentic AI with human engineering expertise to develop reliable, maintainable, and well-tested software. Rather than simply generating code, it emphasizes modular architecture, software reuse, systematic validation, and developer oversight to minimize technical debt and improve software quality.

AgentiX is part of **[The Glass Box AI Project](https://glassboxai.dev/)**, an independent research and development initiative dedicated to building understandable, inspectable, and trustworthy Artificial Intelligence.

# AgentiX v3: Infrastructure as Code

For reproducible Windows-user setup, use [Plan/Apply/Test](infra/README.md).
The managed GUI uses loopback port 7873; GUI and CLI start manually after validation.
The independent environment pins Python 3.11.9, Ollama 0.40.6, DSC 3.3.0 and hashed
Python dependencies. Required model: ollama/qwen3-coder:30b, with explicit download consent.
No Docker, administrator rights, autostart or graphical application installer is used.
Existing compatible prerequisites are reused. See the [implementation evidence](docs/reports/IAC_IMPLEMENTATION.md)
for current-machine verification and clean-machine limitations.

The following legacy entrypoints and engineering notes remain compatible.

# AgentiX v3

Version 3.0.0 is a curated continuation of AgentiX v2. It retains the Gradio GUI,
interactive terminal workflow, mandatory human approvals, native Windows isolation,
and execution-backed answers. The Python package remains `agentix` for compatibility.

## Start

Use a Windows CPython environment with the dependencies described in
[the installation manual](docs/INSTALLATION.md). From this directory:

```powershell
$env:OLLAMA_MODEL = 'ollama/qwen3-coder:30b'
python app.py
# Alternatively, interactive terminal review:
python main.py
```

The existing v2 application is not stopped or upgraded by this copy. The new checkout
contains no copied environment or generated artifacts. A normal application run may
create its own tool storage. Review generated specifications, code, tests and acceptance
cases before approving execution. Generated test success remains provisional.

## Engineering

Read [AGENTS.md](AGENTS.md), [the architecture and quality guide](docs/ARCHITECTURE_QUALITY.md),
[the source reference](docs/reference/README.md), and
[the v3 specification](docs/specs/014-v3-engineering-quality.md).
All comments, docstrings and maintained documentation are English.

```powershell
python -m ruff check src tests tools app.py main.py config.py custom_tools.py security_manager.py _agentix_path.py
python -m ruff format --check src tests tools app.py main.py config.py custom_tools.py security_manager.py _agentix_path.py
python tools/build_reference.py --check
python -m pytest
# Separate, explicit integration validation:
python -m pytest -m frameworks
python -m pytest -m windows_isolation
python -m pytest -m browser
```

After source changes, review contracts and variable semantics, run
`python tools/build_reference.py`, and commit the updated references with the source.
The offline suite rejects stale references. Reference generation parses source and
never imports application modules or reads the excluded generated_tools directory.

The Widget Designer, Assembler and Supervisor agents remain proposed work in the
[four-week proposal](docs/proposals/AgentiX_v2_Project_Proposal.md).
Docker and an application installer are not included.
