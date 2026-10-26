# Unverified local-model report draft

On 2026-10-25, the project D:/AI/AgentiX_v3 was evaluated against approved requirement UI-MODEL-002. Offline testing revealed 412 passed tests, with 24 tests deselected and 15 existing CrewAI warnings noted. Browser testing using actual Edge/Playwright and disposable Gradio showed 8 passed tests. Framework and Windows Vault testing demonstrated 7 passed tests, with synthetic credential roundtrip across processes successfully executed.

Verified button functionality included: "Refresh models reveals newly available choice," "Apply model changes injected client identity used by query backend," "Save profile persists and updates metadata," "Refresh saved profiles discovers profile created after browser load," and "Delete selected profile removes JSON and refreshed catalog entry." GUI changes observed included: "Glass Box dark translucent secondary buttons, light text, subtle border," "Ollama hides key/remote consent," and "provider changes clear key and consent."

Unresolved defects and limitations include: UI browser model/network/vault doubles; no actual model inference or paid APIs are implemented, live instance not restarted, and generated_tools not inspected.
