# ADR-0004: native Windows execution and current-operation evidence

Date: 2026-10-19. Status: implemented, within the limits below.

The user rejected Docker and deferred the installer. Use Windows AppContainer plus Job Objects, with no production fallback to ordinary host execution. Only selected pipe handles inherit. The child starts suspended, its AppContainer token is checked, and job limits apply before it resumes. Unique profiles and freshly copied standard-library runtimes prevent reusing another invocation's files or process state.

The application owns the observed exit status, bounds, snapshots and evidence ledger. Generated source/tests enter only the child; host syntax compilation is non-executing. The final manager stage requires ledger evidence, independent of crew prose. Existing tools need a fresh test-service check for each operation.

AppContainer is an OS security boundary, not a separate kernel. Existing OS permissions for AppContainers still apply. Profile storage remains writable; no disk quota is imposed. Third-party Python packages are intentionally absent. Runtime staging is slower than reusing a process and occurs outside the execution timeout. Setup and cleanup failures deny success.

The child runs unittest in the same interpreter as generated Python. It can manipulate counts or emit forged protocol output. Therefore observed tests are not an attestation of malicious-test honesty or semantic coverage. A future stronger design needs separately authored acceptance criteria and protected control/observation infrastructure; an agent saying tests passed is never sufficient.

References:

- [Microsoft: launch an AppContainer](https://learn.microsoft.com/en-us/windows/win32/secauthz/implementing-an-appcontainer)
- [Microsoft: AppContainer isolation](https://learn.microsoft.com/en-us/windows/win32/secauthz/appcontainer-isolation)
- [Microsoft: Job Objects](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects)
