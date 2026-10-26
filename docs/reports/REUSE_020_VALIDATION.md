# REUSE-002 / UI-REVIEW-002 verification

Date: 2026-10-25. Project: AgentiX v3.

## Outcome and scope

The first reuse implementation preserved approval only in one session. Its real Playwright/Ollama evidence covered consecutive queries but omitted page reload and restart. The user rejected that lifetime and explicitly approved persistence across reloads, other sessions and application restart.

ApprovalStore now persists successful host-accepted function approval outside tool storage, protected by Windows user DPAPI with machine-bound entropy. Records bind canonical tool root, tool name, exact implementation/test hashes, reviewed contract/functions and a maintained security-policy fingerprint. A new query still requires a fresh native call receipt. Sensitive/unclassified code still needs manual exact-call permission, including after restoring durable approval; no native capability is expanded. Historic tools with no protected record require one first review because old child reports cannot reconstruct authorization.

The sole review editor/buttons and Authorization & Test Review accordion are now in the right column below Tool validation. The sidebar contains model configuration. The pending acceptance text discloses future-session authorization when persistence is configured.

## SDD/TDD evidence

- `reuse-020-layout-red.txt`: real Playwright found the review editor inside the sidebar before relocation.
- `reuse-020-durable-red.txt`: nine initial persistence regressions failed before the protected store existed.
- `reuse-020-browser-durable-red.txt`: the dedicated browser lifecycle scenario initially failed before its fixture workflow was implemented.
- `reuse-020-consent-red.txt`: the browser captured the missing future-session authorization notice before it was added.
- `reuse-020-focused.txt` and `reuse-020-layout-and-dpapi.txt`: passing unit behavior and real Gradio/browser plus native protection checks.
- Final offline/integration/native logs provide the authoritative completion totals below. All tests use temporary infrastructure; engineering never reads existing project generated_tools.

## Browser coverage

Playwright/headless Edge uses the real Gradio GUI and actual temporary DPAPI records. Independently authored trusted code is executed by an explicit OS-boundary double in the reproducible browser fixture. The browser performs initial manual acceptance, obtains 12, submits a different input and obtains 42. Additional coverage reloads the page, opens another browser context, replaces the owned disposable server process with retained storage, and obtains a new 42 without another review. Changing the trusted fixture source then requires review again, which the browser rejects. Tests check actual geometry, editor uniqueness, accessibility with the sidebar closed and visible future-session consent. No fixture result is claimed as live model or OS-isolation evidence.

The native DPAPI integration encrypts synthetic data, restores it in a separate Python process and rejects plaintext, truncated and modified blobs. Other Windows Credential Manager checks still use disposable synthetic targets. Ordinary persistence tests use an authenticated fixture protector rather than Windows APIs.

## Real qwen3-coder:30b GUI run

The separate supervised run used real local Ollama, CrewAI, Gradio, Playwright and Windows AppContainer execution with fresh temporary storage and native protected approval records. The user query specified a conversion factor of 0.621371 miles per kilometre and three-place rounding, without software instructions.

| GUI transition | Query | Host-observed result | Additional review/tests |
| --- | --- | --- | --- |
| Initial creation | Convert 10 km | 6.214 miles | Five explicit engineer reviews; eight provisional Python tests and eleven host-compared acceptance cases |
| Page reload into a new session | Convert 25 km | 15.534 miles | None |
| Actual owned-server restart into another new session | Convert 12 km | 7.456 miles | None |

The two reuse inputs were not included in the approved acceptance cases. Three distinct session owners and different pre/post server PIDs were recorded. Each reuse query had zero approval requests, provisional-test events, acceptance-review events, code/artifact reads or artifact writes, and one successful native execution/final observation. The host did update its protected approval metadata; zero artifact writes does not mean zero host filesystem activity.

`reuse-020-live-evidence.json` contains asserted event counts, outcomes, process identities and opaque-record integrity metadata. `reuse-020-live-*` preserves raw logs, results, initial review capture and result screenshots. Protected approval bytes were not copied into the project. All initial reviews were manual with file auto-approval unchecked. No real API keys, paid inference, existing user tools or v2 runtime were used.

The engineer clarified bool/nonfinite/type/rounding behavior, corrected generated code that omitted those validations, removed unnecessary executable demonstration code, corrected the generated unittest import, strengthened exact return-type assertions and expanded acceptance from three examples to eleven cases. Initial creation is explicitly supervised, not claimed autonomous. The legacy operational harness logs a safe optional model-menu action error because it does not compose the profile service; model settings were not used and local inference proceeded. Dedicated full browser/profile integrations cover those settings.

## Incidents and solutions

REUSE-ERR-004: memory-only approval expired on reload/restart. Protected host-owned persistence fixes the missing lifecycle, with drift/root/policy/tamper/revocation and fresh-owner regressions.

UI-REVIEW-020: the review was nested in the sidebar. Move the existing single component set below validation without altering owner/request-bound callbacks. Replace the obsolete source-text layout assertion with actual Gradio component ancestry/uniqueness and retain real browser geometry and visibility checks.

FRAMEWORK-020: an old framework fixture created ArtifactTools with an empty security namespace; the new stable owner binding requires owner_id. Supply an explicit fixture owner, preserving the production ownership contract. The old browser sidebar-placement assertion was updated to assert review absence from the sidebar and presence in the main workspace.

UI-CONTRAST-020: visual inspection revealed near-white text on a light group background after relocation. A Playwright contrast regression measured 1.1407:1. Styling the outer group alone did not fix it; the captured DOM background chain identified Gradio's opaque nested `.styler` fill. Scope the approved dark background to that inner styler as well. The browser requires at least 4.5:1 and captures the readable final review. The original live review screenshot remains evidence of the discovered defect, not the final styling.

## Limits and provenance

DPAPI and machine entropy protect user data, not against same-user malware. Browser routing identity is not Windows account authentication. Finite cases do not prove universal correctness or honest arbitrary child behavior. Corrupt/unavailable storage denies durable reuse; a currently valid execution may still return its result if saving approval fails. Cross-process revocation is checked on later calls, not guaranteed instantaneous; no cross-service transaction, perfect rollback protection or crash-atomic artifact publication is claimed. No automatic trust migration from historical tools was attempted.

The local qwen3:14b model drafted prose only after real qwen3-coder evaluation ended. Its draft/provenance are retained. The engineering agent checked claims against raw logs, clarified that artifact writes exclude protected host metadata updates, and supplied exact final totals independently. No local model wrote engineering code or tests. The application's supervised temporary tool generation is separate.

Native API references: [CryptProtectData](https://learn.microsoft.com/en-us/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata), [CryptUnprotectData](https://learn.microsoft.com/en-us/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata).
