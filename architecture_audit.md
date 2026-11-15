# Auditoría arquitectónica

**Alcance.** Revisión estática de `src`, configuración, infraestructura y tests. Se excluyeron `.git`, entornos virtuales, cachés, `runtime-data`, artefactos generados y dependencias. No se ejecutó la aplicación ni la suite. Los niveles indican impacto arquitectónico observable, no una vulnerabilidad confirmada.

## Hallazgos

### Crítico

No se identificó evidencia suficiente para un hallazgo crítico en el alcance estático revisado.

### Alto

**A1 — Configuración de modelo/endpoint duplicada y divergente.** El modelo, endpoint y límites aparecen en varios composition roots y capas: `src/agentix/settings.py:27-30,44-58`, `src/agentix/bootstrap.py:280`, `src/agentix/adapters/application_crewai.py:180-186`, `src/agentix/agents/application_agents.py:170-198`, `src/agentix/controllers/tool_controller.py:354-355` y `src/agentix/controllers/applications_back.py:483-489`. Esto permite que la configuración seleccionada por el usuario no sea la que usa un flujo concreto. Recom.: un único `ModelConfiguration` inyectado; eliminar literales de producción y validar una vez en la composition root.

**A2 — La frontera de ejecución depende de múltiples contratos framework-específicos.** `src/agentix/adapters/crewai.py:65-101` registra métodos por nombre mediante `getattr` y muta metadatos del decorador; `src/agentix/application/tool_workflow.py:95-103,243-249` construye `Task`/`Crew` directamente; `src/agentix/lab/widget_worker.py:168-180` importa y ejecuta módulos aprobados dinámicamente. Un cambio de CrewAI, Gradio o del contrato de artefactos puede romper creación, aprobación y ejecución simultáneamente. Recom.: puertos internos tipados para registro, planificación, callbacks y ejecución; adaptadores finos con pruebas de contrato por versión.

**A3 — La verificación de reuso y la ejecución están separadas por estado mutable y varios servicios.** `src/agentix/application/tool_workflow.py:386-410` verifica, lee especificación, solicita aceptación y luego delega ejecución; `src/agentix/execution.py:27-89` vuelve a aplicar controles. La secuencia es correcta en intención, pero no existe una transacción/objeto de decisión único que transporte identidad, revisión, función y autorización. Recom.: un `ExecutionDecision` inmutable, firmado por revisión/operación, consumido por una única frontera de ejecución.

### Medio

**M1 — ToolRetrieval no impone umbral de relevancia.** `src/agentix/retrieval/service.py:377-380` declara explícitamente “No score threshold”, y `:464-496` selecciona por RRF hasta `limit`. Un catálogo grande puede devolver candidatos débiles y desplazar la decisión al modelo. Recom.: calibrar un umbral/ margen configurable, registrar por qué se descarta o acepta un candidato y probar consultas ambiguas.

**M2 — Ranking y políticas contienen constantes de negocio dispersas.** `src/agentix/retrieval/policy.py:18-56` centraliza parte de los límites, pero `src/agentix/adapters/crewai.py:114`, `src/agentix/adapters/application_crewai.py:57,174-186`, `src/agentix/application/tool_workflow.py:72,206-210` y `src/agentix/lab/widget_worker.py:217` mantienen budgets, timeouts, puertos y tamaños independientes. Recom.: un objeto de políticas versionado por subsistema, inyectado y expuesto en diagnóstico.

**M3 — Acoplamiento de transporte local en capas de dominio/aplicación.** `src/agentix/retrieval/ollama.py:28-73`, `src/agentix/models/model_profiles.py:351-407` y los agentes legacy en `src/agentix/agents/application_agents.py:125-224` implementan HTTP y reglas de loopback en paralelo. Aunque hay inyección en Retrieval, los flujos de aplicaciones mantienen otra ruta. Recom.: un único `ModelClient`/transport adapter con políticas de origen, límites y timeout.

**M4 — El sandbox nativo concentra demasiadas responsabilidades de plataforma.** `src/agentix/sandbox/windows_process.py:113-133,426-475` combina creación de proceso, handles, Job Object, cancelación, timeout, lectura de salida y cleanup. El `finally` fuerza terminación incluso tras fallos de setup (`:466-475`), difícil de probar por fases. Recom.: separar lifecycle, límites de recursos, transporte IPC y cleanup, con contratos simulables y pruebas de cada transición.

**M5 — Observabilidad heterogénea.** Hay `logging` estructurado mediante `log_event` en `src/agentix/diagnostics.py:40-63`, pero también `print` en `src/agentix/cli.py:22-155` y `application_launch.py:50-56`. No se observa un esquema común de campos para componente, revisión, selección y resultado. Recom.: gateway único de eventos; reservar stdout para protocolo/CLI y no para diagnóstico.

### Bajo

**L1 — Alias de compatibilidad que ocultan la implementación real.** `src/agentix/windows_process.py:1-6` y `src/agentix/paths.py:1-6` reemplazan el módulo en `sys.modules`. Es útil para compatibilidad, pero dificulta navegación, análisis estático y migraciones. Recom.: wrappers explícitos con deprecación y fecha de retirada.

## Tests faltantes o insuficientes

- No se observa una prueba de contrato que demuestre que `Settings`, UI, `CrewAI LLM` y cliente HTTP usan exactamente el mismo modelo/endpoint tras cambiar configuración.
- Faltan tests de selección con catálogo grande, empate, margen bajo y ausencia de umbral en `ToolRetriever` (`tests/test_tool_retrieval.py` cubre snapshots, pero no una política de calidad extremo a extremo).
- Faltan pruebas de compatibilidad ante cambios de firmas/metadatos del decorador CrewAI y de los callbacks Gradio; `tests/integration/test_framework_adapters.py` valida integración, no una matriz de versiones.
- Faltan pruebas de carrera entre verificación, modificación de artefacto y ejecución que atraviesen `tool_workflow.py` y `execution.py` como una sola operación.
- `tests/integration/test_windows_isolation.py` cubre ejecución nativa, pero faltan casos de fallo durante setup, cierre de handles, salida excedida y cancelación simultánea con timeout.
- No se encontró evidencia de cobertura cuantitativa ni de un gate de coverage en `pytest.ini:6-15`.

## Top 5 mejoras (impacto / esfuerzo)

1. **Unificar configuración de modelo, endpoint, budgets y timeouts** mediante objetos inyectables. **Impacto alto / esfuerzo medio.**
2. **Introducir `ExecutionDecision` inmutable y una única frontera de ejecución** con revisión/operación vinculadas. **Impacto alto / esfuerzo alto.**
3. **Aislar CrewAI, Gradio y Ollama detrás de puertos internos tipados** y tests de contrato. **Impacto alto / esfuerzo alto.**
4. **Calibrar Retrieval con umbral/margen y métricas de calidad** sobre fixtures independientes. **Impacto medio-alto / esfuerzo medio.**
5. **Descomponer el sandbox Windows y normalizar eventos estructurados** con pruebas de lifecycle y cleanup. **Impacto medio-alto / esfuerzo alto.**
