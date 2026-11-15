# ADR 0006: keep terminal review in the main thread

Status: accepted for CLI-001 and E2E-001.

The shared workflow blocks while waiting for permission. Running it in the terminal input thread prevents that same terminal from resolving the request. A daemon worker now runs the workflow; the main thread polls owner-bound snapshots and exclusively reads terminal input. The existing coordinator remains responsible for identity, expiry, single-use decisions and mandatory acceptance. Editing content is separate from approving it. EOF and interruption close the owner and deny pending/future permissions. A daemon thread is not a mechanism for forcibly cancelling model calls.

The terminal prints independent host validation state after the model response. Review text escapes terminal control characters without changing approval bytes. Payload-free diagnostic events retain operation/request context. Legacy injected workflows without a coordinator remain synchronous for compatibility.

Browser regressions use a separate real Gradio server with temporary trusted fixtures and a fresh Playwright browser profile. They exercise public controls and real host services without models or production storage. Edge is selected by default to reuse a system browser; managed Chromium and Chrome are explicit alternatives. Browser dependencies and tests are opt-in. Native isolation is verified independently, never inferred from the trusted-fixture subprocess double.
