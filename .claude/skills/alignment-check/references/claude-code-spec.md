# Especificacion neutral Claude Code

Esta referencia resume reglas operativas de Claude Code para auditorias de alineacion. No describe problemas de E-SELEC. Los problemas se detectan leyendo el repo.

Ultima revision local: 2026-05-15.

## Fuentes locales

Usa `indice-tematico.md` para decidir que documento oficial local leer antes de emitir hallazgos fuertes.

La documentacion oficial scrapeada vive en `claude-docs/`. El manifest esta en `claude-docs/manifest.md`.

Regla de control:

- Ningun hallazgo `alto` o `critico` debe emitirse sin leer antes la fuente oficial local del tema.
- Ningun cambio estructural debe recomendarse como ejecutable sin citar la fuente local que lo justifica.
- Si la fuente local falta o contradice este resumen, prevalece la fuente local.

## Principio

Claude Code funciona mejor cuando cada tipo de conocimiento vive en la primitiva correcta:

- instrucciones persistentes pequenas;
- reglas condicionales;
- skills bajo demanda;
- subagents con contexto propio;
- commands para flujos invocados;
- settings para permisos y hooks;
- MCP para herramientas externas;
- archivos de proyecto como memoria, evidencia o datos.

## CLAUDE.md

- Se carga al iniciar sesiones del proyecto.
- Debe contener lo que casi siempre importa.
- Si una seccion es larga o procedimental, probablemente pertenece a una rule o skill.
- Las importaciones con `@archivo` deben usarse con cuidado porque inyectan contexto.

## Rules

- Viven en `.claude/rules/`.
- Sirven para reglas que aplican por tema, ruta o contexto.
- No deben duplicar grandes bloques de `CLAUDE.md` o skills.
- Si una regla se vuelve un procedimiento paso a paso, conviene moverla a skill.

## Skills

- Viven en `.claude/skills/<nombre>/SKILL.md`.
- La descripcion ayuda a decidir cuando usar la skill.
- El cuerpo se carga cuando la skill se usa.
- Los archivos de apoyo deben quedar en `references/`, `templates/`, `checklists/` o `scripts/` y estar mencionados desde `SKILL.md`.
- Una skill debe representar un procedimiento, criterio o capacidad reutilizable.
- Los comandos personalizados y las skills comparten mecanismo. Un command y una skill con el mismo nombre crean el mismo slash command; si ambos existen, la skill tiene prioridad.
- `description` y `when_to_use` compiten por presupuesto de listado. El caso de uso clave debe ir al inicio.
- El texto combinado de `description` y `when_to_use` se trunca en 1.536 caracteres por entrada.
- `disable-model-invocation: true` evita que Claude cargue automaticamente la skill y tambien impide precargarla en subagents.
- `user-invocable: false` oculta la skill del menu `/`, pero no la elimina del contexto automatico.
- `allowed-tools` otorga permiso para herramientas mientras la skill esta activa; no restringe el resto de herramientas disponibles.
- `context: fork` ejecuta la skill en un subagent aislado cuando el flujo necesita separarse del contexto principal.
- `skillListingBudgetFraction`, `skillOverrides` y `maxSkillDescriptionChars` ayudan a gestionar el presupuesto de skills.

Fuentes locales: `claude-docs/es/skills.md`, `claude-docs/es/commands.md`, `claude-docs/es/settings.md`.

## Subagents

- Viven en `.claude/agents/*.md`.
- Deben tener `name` y `description`.
- Pueden definir herramientas con `tools`.
- Si `tools` esta definido, actua como lista acotada.
- Campos soportados relevantes: `description`, `prompt`, `tools`, `disallowedTools`, `model`, `permissionMode`, `mcpServers`, `hooks`, `maxTurns`, `skills`, `initialPrompt`, `memory`, `effort`, `background`, `isolation` y `color`.
- `permissionMode`, `maxTurns`, `memory`, `skills`, `model`, `effort` y `color` ayudan a controlar comportamiento.
- Un subagent se justifica cuando necesita contexto propio, herramientas acotadas o delegacion repetida.
- Si solo lee y reformatea una instruccion, podria ser skill en vez de agente.
- Si `tools` se define, el subagent no hereda todas las herramientas; queda limitado a esa lista.
- `disallowedTools` permite heredar herramientas excepto las bloqueadas.
- `skills` precarga contenido de skills en el contexto del subagent. La skill debe existir y no tener `disable-model-invocation: true`.
- `mcpServers` puede dar acceso a servidores MCP configurados o definidos para ese subagent.
- `hooks` puede aplicarse al ciclo de vida del subagent.
- `memory` puede ser `user`, `project` o `local`, segun el alcance del aprendizaje.
- `background: true` lo ejecuta como tarea de fondo.
- `isolation: worktree` ejecuta el trabajo en un worktree aislado.
- Un agente que promete editar, crear o corregir debe tener herramientas coherentes o declarar que solo recomienda.

Fuentes locales: `claude-docs/es/sub-agents.md`, `claude-docs/es/agents.md`, `claude-docs/es/tools-reference.md`.

## Commands

- Viven en `.claude/commands/`.
- Sirven para flujos invocados por slash command o por el usuario.
- Si un command y una skill resuelven exactamente el mismo flujo, hay que reportar posible duplicacion.
- No se debe borrar un command solo por existir. Primero hay que mapear su uso, equivalencia y riesgo.
- Los archivos en `.claude/commands/` siguen funcionando, pero las skills se recomiendan cuando el flujo necesita archivos de apoyo, frontmatter o carga automatica.

Fuentes locales: `claude-docs/es/commands.md`, `claude-docs/es/skills.md`.

## Settings

- `.claude/settings.json` controla permisos, allow/deny, hooks y entorno del proyecto.
- Modos validos observados por Claude Code actual: `default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`.
- `default` es comportamiento estandar.
- `plan` evita ejecucion y sirve para auditorias.
- `bypassPermissions` es de alto riesgo y debe justificarse muy bien.
- Los hooks deben reducir riesgo sin imprimir secretos.
- Las reglas `allow` y `deny` pueden aplicar a herramientas y patrones, incluyendo rutas y comandos.
- Las configuraciones pueden existir en distintos alcances; el proyecto compartido debe evitar secretos.
- Si `settings.json` contiene valores invalidos, Claude Code puede saltar el archivo completo.

Fuentes locales: `claude-docs/es/settings.md`, `claude-docs/es/permissions.md`, `claude-docs/es/permission-modes.md`.

## Hooks

- `PreToolUse` sirve para bloquear antes de ejecutar.
- `PostToolUse` sirve para validar despues.
- `Stop` y eventos de subagent sirven para cierre y trazabilidad.
- Un hook debe ser verificable, estable y no depender de secretos en repo.
- Los hooks reciben entrada estructurada y pueden bloquear con codigo de salida segun el evento.
- Un hook de seguridad debe tener autoprueba o una forma clara de validacion.

Fuentes locales: `claude-docs/es/hooks.md`, `claude-docs/es/hooks-guide.md`.

## MCP

- `.mcp.json` define servidores MCP compartidos por el proyecto.
- No debe contener secretos reales.
- Si el sistema promete usar Notion, GSC, GA4, Ads, Drive u otros datos vivos, debe existir un mecanismo documentado: MCP, script seguro o conector externo.
- Los servidores pueden configurarse para el proyecto o para subagents mediante `mcpServers`.
- Cuando haya secretos, deben ir por entorno local o gestor externo, no en repo.

Fuentes locales: `claude-docs/es/mcp.md`, `claude-docs/es/settings.md`, `claude-docs/es/security.md`.

## Tools

Herramientas internas relevantes para auditoria:

- `Read`: leer archivos.
- `Write`: crear o sobrescribir archivos.
- `Edit`: editar archivos existentes.
- `Bash`: ejecutar comandos shell.
- `Glob`: buscar archivos por patron.
- `Grep`: buscar texto con ripgrep.
- `Agent`: lanzar subagents.
- `LSP`: inteligencia de codigo cuando este disponible.
- Otras herramientas pueden existir segun plataforma, plugins o version.

Regla de auditoria:

- No asumas que una herramienta esta disponible porque la recuerdas. Confirma en `tools-reference.md` o en la configuracion actual.
- Si un agente promete una accion y no tiene la herramienta necesaria, marca evidencia concreta y severidad segun impacto.

Fuente local: `claude-docs/es/tools-reference.md`.

## Carpetas fuera de `.claude`

- `clients/`, `agency/`, `core/`, `protocols/`, `quality/`, `planning/`, `registries/` y `scripts/` son archivos del proyecto.
- Claude puede leerlos si una regla, skill, agente o instruccion los llama.
- No se cargan automaticamente solo por existir.
- Si contienen instrucciones criticas, debe existir una ruta clara para cargarlas.

## Auditoria profunda

En auditoria profunda del sistema:

1. Leer `claude-docs/manifest.md`.
2. Leer `indice-tematico.md`.
3. Revisar todas las categorias oficiales por lotes.
4. Leer el sistema por capas.
5. Emitir hallazgos solo despues de cruzar fuente oficial local + evidencia del repo.

Si no cabe todo en contexto, resumir cada lote antes de pasar al siguiente y declarar cobertura.

## Anti-patrones a verificar

- Instrucciones siempre cargadas que solo aplican a casos raros.
- Duplicacion entre `CLAUDE.md`, `AGENTS.md`, rules y skills.
- Agentes que prometen ejecutar pero no tienen herramientas para hacerlo.
- Skills con referencias no enlazadas.
- Commands y skills equivalentes sin razon clara.
- MCP prometido pero no configurado.
- Hooks ausentes para acciones sensibles.
- Archivos de otro sistema dentro de skills sin uso por Claude Code.
- Hallazgos fuertes basados en memoria, opiniones previas o reportes antiguos en vez de fuente oficial local.
