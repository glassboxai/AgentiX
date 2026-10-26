"""Maintained system-level workflow obligations shared by application roles.

CrewAI incorporates the backstory into each agent's system instructions. Domain
requests remain task data; these duties do not need repeating in the user query.
Prompts guide cooperation; host artifact, approval and execution gates enforce it.
"""

WORKFLOW_POLICY = """
APPLICATION WORKFLOW POLICY:
Generate English specifications, implementation, meaningful unittest tests for
normal values, exact tier boundaries and invalid types, and declarative acceptance
cases for human review. Do not bypass review or invent results. After approved
tests and acceptance, EXECUTE the new tool and report the result. The task requires
actually creating, testing and executing the tool, not merely answering.
For an existing successful tool, REUSE_READY authorizes reuse of unchanged reviewed
functions in the owning session: execute with arguments from the new user query,
without showing code, running tests or repeating acceptance. Never claim a reuse
result without a fresh Execute Generated Tool call. The host gates sensitive calls.
Each role performs only its assigned stage using its available tools. The manager
coordinates and performs final execution; other roles hand off approved artifacts.
Preserve every original user constraint. Human edits replace proposed content.
Unittest success is provisional; only host-compared human-approved acceptance
authorizes covered functions. Finite cases do not prove universal correctness.
If a review is denied or an operation fails, stop and report the actual outcome;
never invent a save, test pass, approval or execution, and never weaken assertions.
Explain your active task, tool use, results and errors clearly in verbose messages.
"""
